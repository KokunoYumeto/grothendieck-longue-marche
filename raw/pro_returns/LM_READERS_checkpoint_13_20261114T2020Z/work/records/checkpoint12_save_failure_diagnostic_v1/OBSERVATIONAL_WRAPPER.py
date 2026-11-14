#!/usr/bin/env python3
"""Observe the unchanged Library helper; never select or replace its transport.

Run only after explicit diagnostic-attempt authorization. The helper retains
normal JSON stdin/EOF, stdout, stderr, exceptions, exit status, and all network
operations. New private diagnostic files are the only added side effect.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import runpy
import stat
import sys
import threading

EXPECTED = {
    "library_upload.py": "b11e4929596e321366c2f7291890fbb6d6bf8b413ae6d24593e9548f9bf50f23",
    "library_hosted_apps.py": "cf40f74293ed9f4739c9ce2bca38003155a278420c375fb412de633efed7dbf8",
    "library_file_transfer.py": "acd44c7471495a240e4f2d97037fe6f83c48793ab98938801e5393f5584a029b",
}
TARGETS = {
    "library_upload.py": {
        "_prepare", "upload", "_is_estuary_upload", "_upload_one",
        "_upload_estuary", "_finalize", "_result", "main",
    },
    "library_hosted_apps.py": {"_rpc"},
}


def exact_int(value):
    return value if type(value) is int else None


def safe_exception(error):
    result = {"exception_class": type(error).__name__}
    # Never stringify exceptions or inspect their headers/body/URL/args.
    for name in ("code", "errno"):
        value = exact_int(getattr(error, name, None))
        if value is not None:
            result["http_status" if name == "code" else "errno"] = value
    reason = getattr(error, "reason", None)
    if isinstance(reason, BaseException):
        result["reason_exception_class"] = type(reason).__name__
        value = exact_int(getattr(reason, "errno", None))
        if value is not None:
            result["reason_errno"] = value
    return result


class Observer:
    def __init__(self, files, directory):
        self.targets = {str(files[name]): names for name, names in TARGETS.items()}
        self.directory = directory
        self.raw_directory = directory / "private_transport_logs"
        self.raw_directory.mkdir(mode=0o700)
        self.stream = (directory / "SAFE_EVENTS.jsonl").open("x", encoding="utf-8")
        os.chmod(directory / "SAFE_EVENTS.jsonl", 0o600)
        self.lock = threading.Lock()
        self.copied = []
        self.copy_done = set()
        self.errors = 0
        self.events = 0
        self.suppressed_events = 0

    def emit(self, value):
        # Diagnostic failures must never escape into helper control flow.
        try:
            with self.lock:
                if self.events >= 4096:
                    self.suppressed_events += 1
                    return
                self.stream.write(json.dumps(value, sort_keys=True) + "\n")
                self.stream.flush()
                self.events += 1
        except Exception:
            self.errors += 1

    def copy_logs(self, frame):
        # Called on _upload_one return, after subprocess.run and its output
        # context have finished, but before helper TemporaryDirectory cleanup.
        state = frame.f_locals.get("state_directory")
        upload = frame.f_locals.get("upload")
        request = getattr(upload, "request", None)
        index = exact_int(getattr(request, "index", None))
        if not isinstance(state, Path) or index is None:
            return
        with self.lock:
            if index in self.copy_done:
                return
            self.copy_done.add(index)
        candidates = [state / ("transfer-%d.log" % index)]
        logs = state / "logs"
        if logs.is_dir() and not logs.is_symlink():
            candidates.extend(sorted(logs.glob("*.log")))
        for source in candidates:
            try:
                info = source.lstat()
                if not stat.S_ISREG(info.st_mode):
                    continue
                with self.lock:
                    number = len(self.copied) + 1
                    # The diagnostic attempt is a single-file request; generic
                    # destination names disclose no signed-URL/job identifiers.
                    target = self.raw_directory / ("transport_%04d.log" % number)
                    digest = hashlib.sha256()
                    size = 0
                    with source.open("rb") as incoming, target.open("xb") as output:
                        os.chmod(target, 0o600)
                        while True:
                            data = incoming.read(1024 * 1024)
                            if not data:
                                break
                            output.write(data)
                            digest.update(data)
                            size += len(data)
                    self.copied.append({
                        "path": "private_transport_logs/" + target.name,
                        "bytes": size,
                        "sha256": digest.hexdigest(),
                    })
            except FileNotFoundError:
                continue
            except Exception:
                self.errors += 1

    def trace(self, frame, event, arg):
        names = self.targets.get(frame.f_code.co_filename)
        name = frame.f_code.co_name
        if names is None or name not in names:
            return None
        try:
            frame.f_trace_lines = False
            frame.f_trace_opcodes = False
            item = {"function": name, "event": event}
            if event == "call":
                if name == "_upload_estuary":
                    item["transport_branch"] = "estuary"
                elif name == "_finalize":
                    uploads = frame.f_locals.get("uploads")
                    if type(uploads) is tuple:
                        item["item_count"] = len(uploads)
                self.emit(item)
            elif event == "exception":
                item.update(safe_exception(arg[1]))
                self.emit(item)
            elif event == "return":
                if type(arg) is bool:
                    item["boolean_return"] = arg
                elif type(arg) is int:
                    item["integer_return"] = arg
                if name == "_upload_one":
                    result = frame.f_locals.get("result")
                    returncode = exact_int(getattr(result, "returncode", None))
                    if returncode is not None:
                        item["transport_branch"] = "azcopy"
                        item["process_returncode"] = returncode
                    executable = frame.f_locals.get("executable")
                    item["executable_available"] = executable is not None
                    self.copy_logs(frame)
                self.emit(item)
        except Exception:
            self.errors += 1
        return self.trace

    def finish(self, pins_before, files):
        # Observation remains best effort; preserve helper's exact exit behavior.
        try:
            pins_after = {name: hashlib.sha256(path.read_bytes()).hexdigest()
                          for name, path in files.items()}
            self.stream.close()
            summary = {
                "schema": "library-helper-observational-diagnostic-v1",
                "helper_sha256_before": pins_before,
                "helper_sha256_after": pins_after,
                "helper_bytes_unchanged": pins_before == pins_after,
                "events": self.events,
                "suppressed_events": self.suppressed_events,
                "diagnostic_errors": self.errors,
                "private_logs": self.copied,
                "scope": "Observed unchanged helper; no transport/configuration/request/result override.",
            }
            path = self.directory / "SAFE_SUMMARY.json"
            with path.open("x", encoding="utf-8") as output:
                os.chmod(path, 0o600)
                json.dump(summary, output, indent=2, sort_keys=True)
                output.write("\n")
        except Exception:
            pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--diagnostic-dir", required=True)
    args = parser.parse_args()
    helper_directory = (Path.cwd() / ".library_helpers_current").resolve()
    files = {name: helper_directory / name for name in EXPECTED}
    pins_before = {name: hashlib.sha256(path.read_bytes()).hexdigest()
                   for name, path in files.items()}
    if pins_before != EXPECTED:
        raise SystemExit("Diagnostic preflight failed: helper identity mismatch")
    output = Path(args.diagnostic_dir)
    output.mkdir(mode=0o700, parents=False, exist_ok=False)
    observer = Observer(files, output)
    previous_trace = sys.gettrace()
    previous_thread_trace = threading.gettrace()
    previous_argv = sys.argv
    sys.argv = [str(files["library_upload.py"])]
    try:
        sys.settrace(observer.trace)
        threading.settrace(observer.trace)
        runpy.run_path(str(files["library_upload.py"]), run_name="__main__")
    finally:
        sys.settrace(previous_trace)
        threading.settrace(previous_thread_trace)
        sys.argv = previous_argv
        observer.finish(pins_before, files)


if __name__ == "__main__":
    main()
