#!/usr/bin/env python3
"""Reproduce mathematical computations without changing the shipped records.

Run from any working directory.  Default: all independent mathematical programs,
including two C++17 builds.  --quick: independent certificate verification and
selected exact calculations, using the shipped inputs and no C++ compiler.
Editorial assembly and PDF production are separate commands in README.md.
"""
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import shlex
import shutil
import subprocess
import sys
import tempfile
import time

CODE = Path(__file__).resolve().parent
PACKAGE = CODE.parent


@dataclass(frozen=True)
class Task:
    name: str
    source: str
    args: tuple[str, ...] = ()
    artifacts: tuple[str, ...] = ()
    stdout_reference: str | None = None
    stdout_kind: str = "tokens"
    cpp: bool = False
    stdin_name: str | None = None


TASKS = (
    Task("ab_lie", "ab_lie.py", ("6",), ("ab_lie_results.json",)),
    Task("ab_kernel", "ab_kernel.py", artifacts=("ab_kernel_results.json",)),
    Task("ab_weight5_witness", "ab_weight5_witness.py", artifacts=("ab_weight5_witness.json",)),
    Task("ab_degree3_conjugators", "ab_degree3_conjugators.py", artifacts=("ab_degree3_conjugators.json",)),
    Task("ab_elliptic", "ab_elliptic.py", artifacts=("ab_elliptic_results.json",)),
    Task("ab_elliptic_normalizer", "ab_elliptic_normalizer.py", artifacts=("ab_elliptic_normalizer_results.json",)),
    Task("ceh_checks", "ceh_checks.py", artifacts=("ceh_checks.json",)),
    Task("ceh_pro2_cover", "ceh_pro2_cover.cpp", artifacts=("ceh_pro2_certificates.json",),
         stdout_reference="ceh_pro2_cover.out", stdout_kind="cover", cpp=True),
    Task("ceh_pro2_verify", "ceh_pro2_verify.py", artifacts=("ceh_pro2_verification.json",)),
    Task("dg_checks", "dg_checks.py", stdout_reference="dg_checks.out", stdout_kind="json"),
    Task("fg_prepare", "fg_prepare.py", ("12",), ("fg_candidates.json",)),
    Task("fg_certify", "fg_certify.py", artifacts=("fg_certify_results.json", "fg_pentagon_input.txt")),
    Task("fg_pentagon", "fg_pentagon.cpp", stdout_reference="fg_pentagon.out", cpp=True,
         stdin_name="fg_pentagon_input.txt"),
    Task("fh_finite", "fh_finite.py", artifacts=("fh_finite_results.json", "fh_abelian_images.csv")),
    Task("quaternion_shadow", "quaternion_shadow.py", artifacts=("quaternion_shadow_results.json",)),
    Task("g_operator", "g_operator.py", artifacts=("g_operator_results.json",)),
)
QUICK_SKIP = {"ab_lie", "ab_kernel", "ab_elliptic_normalizer", "ceh_pro2_cover", "fg_prepare", "fg_pentagon"}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def output_hashes() -> dict[str, str]:
    return {p.name: digest(p) for p in sorted(CODE.iterdir())
            if p.is_file() and p.suffix in {".json", ".csv", ".txt", ".out"}}


def read_value(path: Path, kind: str):
    if kind == "json":
        value = json.loads(path.read_text())
        # This hash binds a verifier run to its own certificate bytes.  It is
        # independently checked below; JSON formatting need not be identical.
        if path.name == "ceh_pro2_verification.json":
            value = dict(value)
            value.pop("certificate_sha256", None)
        return value
    if kind == "csv":
        with path.open(newline="") as stream:
            return list(csv.DictReader(stream))
    if kind == "cover":
        return [line.split() for line in path.read_text().splitlines()
                if not line.startswith("dual_certificates_written=")]
    return path.read_text().split()


def compare(reference: Path, generated: Path, kind: str, report: dict) -> None:
    if not reference.is_file() or not generated.is_file():
        raise RuntimeError(f"Missing comparison file: {reference} or {generated}")
    same = read_value(reference, kind) == read_value(generated, kind)
    report["comparisons"].append({
        "reference": reference.name,
        "generated": str(generated),
        "method": kind,
        "match": same,
        "reference_sha256": digest(reference),
        "generated_sha256": digest(generated),
    })
    if not same:
        raise RuntimeError(f"Regenerated result differs from the shipped record: {reference.name}")


def run_command(label: str, command: list[str], cwd: Path, log: Path,
                report: dict, env: dict, stdin_path: Path | None = None) -> None:
    print(f"[{label}] {shlex.join(command)}", flush=True)
    start = time.monotonic()
    input_stream = stdin_path.open("rb") if stdin_path else None
    try:
        with log.open("w") as output:
            result = subprocess.run(command, cwd=cwd, env=env, stdin=input_stream,
                                    stdout=output, stderr=subprocess.STDOUT, check=False)
    finally:
        if input_stream is not None:
            input_stream.close()
    elapsed = time.monotonic() - start
    report["steps"].append({"name": label, "command": command,
                            "stdin": str(stdin_path) if stdin_path else None,
                            "elapsed_seconds": round(elapsed, 3),
                            "returncode": result.returncode, "log": str(log)})
    if result.returncode:
        tail = "\n".join(log.read_text(errors="replace").splitlines()[-12:])
        raise RuntimeError(f"{label} exited with status {result.returncode}.\n{tail}")
    print(f"  completed in {elapsed:.3f} s", flush=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--quick", action="store_true", help="verify shipped certificates and selected exact checks; no C++ compiler")
    parser.add_argument("--output", type=Path, help="new or empty directory for logs, regenerated artifacts, and report.json")
    parser.add_argument("--compiler", default=os.environ.get("CXX", "g++"), help="C++ executable for full mode (default: CXX or g++)")
    args = parser.parse_args()
    mode = "quick" if args.quick else "full"
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    destination = (args.output.expanduser().resolve() if args.output else
                   PACKAGE / "reproduction" / f"{mode}-{timestamp}-{os.getpid()}")
    if destination.exists() and any(destination.iterdir()):
        parser.error(f"Output directory must be new or empty: {destination}")
    destination.mkdir(parents=True, exist_ok=True)
    logs = destination / "logs"
    generated = destination / "generated"
    logs.mkdir()
    generated.mkdir()
    before = output_hashes()
    report = {"mode": mode, "started_utc": utc_now(), "source_directory": str(CODE),
              "output_directory": str(destination), "python": sys.version,
              "platform": platform.platform(), "steps": [], "comparisons": [],
              "completed_programs": [], "success": False,
              "scope": ("Independent verification of shipped pro-2 dual certificates and candidate-reduction ranks, plus selected exact computations. No C++ search, direct pentagon matrix, high-degree special normalizer, or elliptic normalizer rerun."
                        if args.quick else
                        "Rerun every supplied mathematical program, including both C++ searches/rank calculations. This reproduces finite computations; the paper contains the lifting, infinite-group, and literature-dependent proofs.")}
    started = time.monotonic()
    try:
        if sys.version_info < (3, 10):
            raise RuntimeError("Python 3.10 or newer is required.")
        try:
            import sympy
        except ImportError as exc:
            raise RuntimeError("Install SymPy for this Python interpreter, e.g. python -m pip install sympy==1.14.0") from exc
        report["sympy"] = sympy.__version__
        compiler = None
        if not args.quick:
            compiler = shutil.which(args.compiler)
            if not compiler:
                raise RuntimeError(f"C++ compiler not found: {args.compiler!r}; use --compiler /path/to/g++")
            version = subprocess.run([compiler, "--version"], text=True, capture_output=True, check=True)
            report["compiler"] = version.stdout.splitlines()[0]
        selected = [t for t in TASKS if not args.quick or t.name not in QUICK_SKIP]
        report["requested_programs"] = [t.name for t in selected]
        report["source_sha256"] = {p.name: digest(p) for p in sorted(CODE.iterdir())
                                   if p.is_file() and p.suffix in {".py", ".cpp"}}
        env = os.environ.copy()
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        env["PYTHONOPTIMIZE"] = "0"  # The mathematical assertions must execute.
        # Temporary sources and binaries stay inside the selected writable run
        # directory and are removed even on failure; they are never deliverables.
        with tempfile.TemporaryDirectory(prefix=".work-", dir=destination) as temporary:
            work = Path(temporary)
            stage = work / "code"
            build = work / "build"
            stage.mkdir()
            build.mkdir()
            for source in CODE.iterdir():
                if source.is_file() and source.suffix in {".py", ".cpp"}:
                    shutil.copy2(source, stage / source.name)
            if args.quick:
                for name in ("fg_candidates.json", "ceh_pro2_certificates.json"):
                    shutil.copy2(CODE / name, stage / name)
            for task in selected:
                if task.cpp:
                    executable = build / task.name
                    run_command("compile_" + task.name,
                                [compiler, "-O2", "-std=c++17", str(stage / task.source), "-o", str(executable)],
                                work, logs / ("compile_" + task.name + ".out"), report, env)
                    command = [str(executable)]
                    if task.name == "ceh_pro2_cover":
                        command.append(str(stage / "ceh_pro2_certificates.json"))
                else:
                    command = [sys.executable, "-B", str(stage / task.source), *task.args]
                    if task.name == "ceh_pro2_verify":
                        command.append(str(stage / "ceh_pro2_certificates.json"))
                log = logs / (task.name + ".out")
                stdin_path = stage / task.stdin_name if task.stdin_name else None
                run_command(task.name, command, work, log, report, env, stdin_path)
                if task.name == "ceh_pro2_verify":
                    verification = json.loads((stage / "ceh_pro2_verification.json").read_text())
                    expected_hash = digest(stage / "ceh_pro2_certificates.json")
                    if verification["certificate_sha256"] != expected_hash:
                        raise RuntimeError("Independent verifier report does not bind to the certificate bytes used.")
                    report["verified_certificate_sha256"] = expected_hash
                for name in task.artifacts:
                    target = generated / name
                    shutil.copy2(stage / name, target)
                    kind = "json" if target.suffix == ".json" else "csv" if target.suffix == ".csv" else "tokens"
                    compare(CODE / name, target, kind, report)
                if task.stdout_reference:
                    compare(CODE / task.stdout_reference, log, task.stdout_kind, report)
                report["completed_programs"].append(task.name)
        report["success"] = True
    except (Exception, KeyboardInterrupt) as exc:
        report["error"] = f"{type(exc).__name__}: {exc}"
        print(report["error"], file=sys.stderr, flush=True)
    finally:
        after = output_hashes()
        report["shipped_output_files_unchanged"] = before == after
        if before != after:
            report["success"] = False
            report["changed_shipped_outputs"] = sorted(k for k in before.keys() | after.keys() if before.get(k) != after.get(k))
        report["finished_utc"] = utc_now()
        report["elapsed_seconds"] = round(time.monotonic() - started, 3)
        report["completed_program_count"] = len(report["completed_programs"])
        report["comparison_count"] = len(report["comparisons"])
        (destination / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"{mode.upper()}: {'PASS' if report['success'] else 'FAIL'}; "
          f"{report['completed_program_count']} programs; {report['comparison_count']} artifact comparisons; "
          f"{report['elapsed_seconds']:.3f} s", flush=True)
    print(f"Report: {destination / 'report.json'}", flush=True)
    return 0 if report["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
