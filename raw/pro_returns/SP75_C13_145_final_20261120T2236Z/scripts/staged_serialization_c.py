#!/usr/bin/env python3
"""Staged serialization maintenance; default is a read-only preflight.

This script is prepared for root review. It must not be run with --apply until
root authorizes one stage and supplies the exact reviewed plan SHA-256.
It never compiles TeX, imports edition evidence scripts, or recursively rewrites
JSON. Reviewed reports may contain unrelated field changes, but selected field
values/hashes and identities are exact and all other observed bytes are preserved. Historical readings, comparison files, seals and initial reports are
outside its write allowlist.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
import tempfile
import uuid

STAGE_SCANS = {"serialization": (12, 13, 14, 15, 18, 19), "gamma": (24,),
               "prime026": (26,), "superscript027": (27,)}
STAGE_COUNTS = {"serialization": (18, 45, 35), "gamma": (3, 14, 13),
                "prime026": (3, 8, 7), "superscript027": (3, 10, 9)}
PAGE_CASES = {
    12: {"D6"}, 13: {"D1", "D2", "D3", "D4"}, 14: {"I1"},
    15: {"D7"}, 18: {"D8", "D9"}, 19: {"D5"}, 24: {"F1"}, 26: {"P1"},
    27: {"S1"}
}


S1_OLD = r"\unsure{\dot\rho|\rho}^{\deleted{\unsure{2}}}"
S1_NEW = r"{\unsure{\dot\rho|\rho}}^{\deleted{\unsure{2}}}"
S1_RHO_BEFORE = r"\unsure{\deleted{\unsure{\dot\rho^2}}|\unsure{\dot\rho|\rho}^{\deleted{\unsure{2}}}}"
S1_RHO_AFTER = r"\unsure{\deleted{\unsure{\dot\rho^2}}|{\unsure{\dot\rho|\rho}}^{\deleted{\unsure{2}}}}"
S1_C_QUOTE_OLD = r"\deleted{\unsure{\dot\rho}}"


class StageError(RuntimeError):
    pass


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def require(ok, message):
    if not ok:
        raise StageError(message)


def json_value(obj, pointer):
    value = obj
    for key in pointer:
        if isinstance(value, list):
            require(type(key) is int, "array pointer must use an integer")
        else:
            require(isinstance(value, dict) and isinstance(key, str),
                    "object pointer must use a string")
        value = value[key]
    return value


def allowed_paths(stage):
    paths = set()
    for scan in STAGE_SCANS[stage]:
        stem = f"145_scan{scan:03d}"
        paths.update((f"pages/{stem}.tex",
                      f"reader_reports/{stem}_reviewed.json",
                      f"second/{stem}_adjudication.json"))
    return paths


def target_path(root, relative, stage):
    require(relative in allowed_paths(stage), f"disallowed target: {relative}")
    p = root / relative
    require(not p.is_symlink(), f"target is a symlink: {relative}")
    resolved = p.resolve()
    require(resolved.is_relative_to(root), "target escapes edition root")
    return resolved


def current_field_allowed(kind, p):
    if kind == "adjudication":
        return (len(p) == 3 and p[0] == "differences"
                and type(p[1]) is int and p[2] == "final")
    if kind != "report":
        return False
    if p == ["c_markup_audit", "items", 1, "reading"]:
        return True
    if (len(p) == 4 and p[:2] == ["audit", "differences"]
            and type(p[2]) is int and p[3] == "final"):
        return True
    if (len(p) == 3 and type(p[1]) is int):
        return ((p[0] == "changes" and p[2] == "final")
                or (p[0] in ("decisions", "unlisted_decisions", "doubts")
                    and p[2] == "reading")
                or (p[0] == "inventory" and p[2] == "first_words_or_objects")
                or (p[0] == "notation" and p[2] == "form"))
    return (len(p) == 4 and p[0] == "doubts" and type(p[1]) is int
            and p[2] == "alternatives" and type(p[3]) is int)


def changed_leaf_paths(a, b, path=()):
    if type(a) is not type(b):
        return {path}
    if isinstance(a, dict):
        if a.keys() != b.keys():
            return {path}
        out = set()
        for key in a:
            out |= changed_leaf_paths(a[key], b[key], path + (key,))
        return out
    if isinstance(a, list):
        if len(a) != len(b):
            return {path}
        out = set()
        for index, (x, y) in enumerate(zip(a, b)):
            out |= changed_leaf_paths(x, y, path + (index,))
        return out
    return set() if a == b else {path}

class JsonStringSpans:
    """Locate value string literals without reserializing enclosing JSON."""
    def __init__(self, text):
        self.text = text
        self.decoder = json.JSONDecoder()
        self.spans = {}

    def ws(self, i):
        while i < len(self.text) and self.text[i].isspace():
            i += 1
        return i

    def value(self, i, path):
        i = self.ws(i)
        if i >= len(self.text):
            raise ValueError("truncated JSON")
        c = self.text[i]
        if c == '"':
            value, end = self.decoder.raw_decode(self.text, i)
            self.spans[path] = (i, end, value)
            return end
        if c == "{":
            i = self.ws(i + 1)
            keys = set()
            if self.text[i] == "}":
                return i + 1
            while True:
                key, end = self.decoder.raw_decode(self.text, i)
                if not isinstance(key, str) or key in keys:
                    raise ValueError("non-string or duplicate object key")
                keys.add(key)
                i = self.ws(end)
                if self.text[i] != ":":
                    raise ValueError("missing JSON colon")
                i = self.ws(self.value(i + 1, path + (key,)))
                if self.text[i] == "}":
                    return i + 1
                if self.text[i] != ",":
                    raise ValueError("missing JSON comma")
                i = self.ws(i + 1)
        if c == "[":
            i = self.ws(i + 1)
            if self.text[i] == "]":
                return i + 1
            index = 0
            while True:
                i = self.ws(self.value(i, path + (index,)))
                if self.text[i] == "]":
                    return i + 1
                if self.text[i] != ",":
                    raise ValueError("missing JSON array comma")
                index += 1
                i = self.ws(i + 1)
        _, end = self.decoder.raw_decode(self.text, i)
        return end

    def parse(self):
        end = self.ws(self.value(0, ()))
        if end != len(self.text):
            raise ValueError("trailing JSON data")
        return self.spans

def control_end(s, i):
    j = i + 1
    if j < len(s) and s[j].isascii() and s[j].isalpha():
        while j < len(s) and s[j].isascii() and s[j].isalpha():
            j += 1
    elif j < len(s):
        j += 1
    return j


def group_end(s, i):
    depth = 0
    while i < len(s):
        if s[i] == "\\":
            i = control_end(s, i)
            continue
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    raise ValueError("unclosed TeX group")


def payload_tokens(s):
    def strip(text):
        out, i = [], 0
        while i < len(text):
            if text[i] != "\\":
                out.append(text[i])
                i += 1
                continue
            end = control_end(text, i)
            name = text[i + 1:end]
            if name == "displaystyle":
                i = end
                continue
            if name in ("deleted", "inserted", "mbox"):
                j = end
                while j < len(text) and text[j].isspace():
                    j += 1
                if j >= len(text) or text[j] != "{":
                    raise ValueError("serialization wrapper lacks braced argument")
                close = group_end(text, j)
                out.append(strip(text[j + 1:close]))
                i = close + 1
                continue
            out.append(text[i:end])
            i = end
        return "".join(out)
    return re.findall(r"\\[A-Za-z]+|\\[\s\S]|[^\s]", strip(s))

def validate_plan_shape(plan, stage_name):
    require(plan.get("schema_version") == 1, "unsupported plan schema")
    stage = plan["stages"][stage_name]
    require(stage.get("ready_for_root_review") is True, "stage is not ready")
    files = stage["files"]
    expected_files, expected_operations, expected_fields = STAGE_COUNTS[stage_name]
    require(len(files) == expected_files, "unexpected target-file count")
    require({f["path"] for f in files} == allowed_paths(stage_name),
            "target allowlist differs")
    require(sum(len(f["operations"]) for f in files) == expected_operations,
            "unexpected operation count")
    require(sum(len(f["operations"]) for f in files if f["kind"] != "page")
            == expected_fields, "unexpected exact-field count")
    seen_ids = set()
    for f in files:
        scan = int(re.search(r"scan(\d+)", f["path"]).group(1))
        require(not f.get("allow_unrelated_field_drift", False)
                or f["kind"] == "report", "drift is allowed only for current reports")
        require(re.fullmatch(r"[0-9a-f]{64}", f["before_sha256"]) is not None,
                "missing before hash")
        require(re.fullmatch(r"[0-9a-f]{64}", f["after_sha256"]) is not None,
                "missing after hash")
        if f["kind"] == "page":
            ids = {case for op in f["operations"] for case in op["case_ids"]}
            require(ids == PAGE_CASES[scan], "page case IDs differ")
        pointers = set()
        for op in f["operations"]:
            require(op["id"] not in seen_ids, "duplicate operation ID")
            seen_ids.add(op["id"])
            require(isinstance(op["old"], str) and isinstance(op["new"], str)
                    and op["old"] != op["new"], "invalid string replacement")
            require(digest(op["old"].encode()) == op["old_sha256"],
                    "old-string hash mismatch in plan")
            require(digest(op["new"].encode()) == op["new_sha256"],
                    "new-string hash mismatch in plan")
            require(set(op["case_ids"]).issubset(PAGE_CASES[scan]),
                    "operation case is from another page")
            if f["kind"] == "page":
                require(op["kind"] == "replace_text", "wrong page operation")
                require(op["count"] == (7 if stage_name == "gamma" else 1),
                        "unexpected page replacement count")
            else:
                require(op["kind"] == "set_string" and op["count"] == 1,
                        "wrong exact-field operation")
                require(current_field_allowed(f["kind"], op["pointer"]),
                        "historical or unsupported JSON field")
                pointer = tuple(op["pointer"])
                require(pointer not in pointers, "duplicate JSON pointer")
                pointers.add(pointer)
            if stage_name == "serialization":
                require(payload_tokens(op["old"]) == payload_tokens(op["new"]),
                        "visible payload tokens differ: " + op["id"])
            elif stage_name == "gamma":
                gamma = next(x for x in files if x["kind"] == "page")["operations"][0]
                require(gamma["old"] == r"\mathbb\Gamma",
                        "Gamma stage old token differs")
                require(op["new"] == op["old"].replace(gamma["old"], gamma["new"]),
                        "Gamma operation changes more than its glyph token")
                if f["kind"] != "page":
                    require(op["old"].count(gamma["old"])
                            == op["token_replacement_count"],
                            "Gamma field occurrence count differs")
            elif stage_name == "prime026":
                require(op["new"] == op["old"].replace(
                    r"\alpha\prime", r"\alpha'"),
                    "prime026 changes more than the requested prime positioning")
                require(op["old"].count(r"\alpha\prime") == 1,
                        "prime026 exact occurrence count differs")
            elif op.get("current_quote_sync"):
                require(f["path"] == "reader_reports/145_scan027_reviewed.json"
                        and op["pointer"] == ["c_markup_audit", "items", 1, "reading"]
                        and op["id"] == "S1-current-quote-c_markup",
                        "unapproved current-quotation synchronization")
                require(op["old"] == S1_C_QUOTE_OLD and op["new"] == S1_RHO_AFTER,
                        "current rho quotation differs from the accepted source")
            else:
                require(op["old"].count(S1_OLD) == 1
                        and op["new"] == op["old"].replace(S1_OLD, S1_NEW),
                        "S1 changes more than the approved grouping")
    return stage


def guard_sources(root, plan, stage_name):
    guards = (
        ("source_review", "reader_reports/final_static_review_c.md"),
        ("final_recheck", "reader_reports/final_static_recheck_c.md"),
        ("preamble_guard", "../source/SP75_C13_145_texts/PREAMBLE.tex"),
    )
    for key, expected_path in guards:
        guard = plan[key]
        require(guard["path"] == expected_path, "unexpected guard path: " + key)
        require(digest((root / guard["path"]).read_bytes()) == guard["sha256"],
                key + " changed; re-review required")
    if stage_name != "serialization":
        scan = {"gamma": 24, "prime026": 26, "superscript027": 27}[stage_name]
        gate = plan["stages"][stage_name]["audit_gate"]
        require(gate["path"] == f"second/145_scan{scan:03d}_adjudication.json",
                "wrong audit gate")
        raw = (root / gate["path"]).read_bytes()
        require(digest(raw) == gate["sha256"], f"page{scan:03d} audit gate hash changed")
        require(json_value(json.loads(raw), gate["required_field"])
                == gate["required_value"], f"page{scan:03d} audit gate incomplete")
        require(gate["required_field"]
                == ["main_reader_viewed_all_differing_crops"]
                and gate["required_value"] is True,
                "weakened audit gate")
        require(bool(plan["stages"][stage_name].get("audit_completed_at")),
                "audit completion time is missing")
    if stage_name == "prime026":
        release = plan["stages"][stage_name]["post_audits_release"]
        require(release["ready"] is True,
                "prime026 awaits root's final-audit/static-recheck release")
        require(release["audit_path"] == "second/145_scan027_adjudication.json",
                "wrong final-audit release path")
        s1 = plan["stages"]["superscript027"]
        s1_after = next(f for f in s1["files"] if f["kind"] == "adjudication")["after_sha256"]
        expected = [s1["audit_gate"]["sha256"], s1_after]
        require(release["allowed_audit_sha256"] == expected
                and release["audit_sha256"] == expected[0],
                "final027 release states differ from the reviewed S1 states")
        raw = (root / release["audit_path"]).read_bytes()
        require(digest(raw) in expected, "final027 audit hash is unrecognized")
        require(json.loads(raw).get("main_reader_viewed_all_differing_crops") is True,
                "final027 audit is not marked complete")


def prepare_target(root, file_plan, stage_name):
    p = target_path(root, file_plan["path"], stage_name)
    before = p.read_bytes()
    observed_before = digest(before)
    drift = observed_before != file_plan["before_sha256"]
    require(not drift or (file_plan["kind"] == "report"
                          and file_plan.get("allow_unrelated_field_drift") is True),
            f"before hash mismatch: {file_plan['path']}")
    text = before.decode("utf-8")
    if file_plan["kind"] == "page":
        after_text = text
        for op in file_plan["operations"]:
            require(after_text.count(op["old"]) == op["count"],
                    "exact occurrence count mismatch: " + op["id"])
            after_text = after_text.replace(op["old"], op["new"], op["count"])
        if stage_name == "superscript027":
            require(text.count(S1_RHO_BEFORE) == 1
                    and after_text.count(S1_RHO_AFTER) == 1,
                    "S1 canonical page quotation differs")
    else:
        original = json.loads(text)
        spans = JsonStringSpans(text).parse()
        patches = []
        expected_paths = set()
        for op in file_plan["operations"]:
            pointer = tuple(op["pointer"])
            require(pointer in spans, "JSON pointer is not a string")
            start, end, value = spans[pointer]
            require(value == op["old"]
                    and digest(value.encode()) == op["old_sha256"],
                    "exact field value/hash mismatch: " + op["id"])
            parent = json_value(original, op["pointer"][:-1])
            for key, expected in op.get("identity", {}).items():
                require(isinstance(parent, dict) and parent.get(key) == expected,
                        "field identity mismatch: " + op["id"])
            patches.append((start, end, json.dumps(op["new"], ensure_ascii=False)))
            expected_paths.add(pointer)
        after_text = text
        for start, end, encoded in sorted(patches, reverse=True):
            after_text = after_text[:start] + encoded + after_text[end:]
        result = json.loads(after_text)
        require(changed_leaf_paths(original, result) == expected_paths,
                "unlisted JSON field changed")
    after = after_text.encode("utf-8")
    observed_after = digest(after)
    if not drift:
        require(observed_after == file_plan["after_sha256"],
                "planned output hash mismatch: " + file_plan["path"])
        require(len(after) == file_plan["after_bytes"], "planned output size differs")
    # Under report drift, all named old fields/hashes/identities still matched,
    # and only their raw string spans changed. Pin the whole observed preimage
    # for the immediate-before-apply check; preserve every other observed byte.
    return {"plan": file_plan, "path": p, "before": before, "after": after,
            "before_sha256": observed_before, "after_sha256": observed_after,
            "unrelated_field_drift": drift,
            "mode": stat.S_IMODE(p.stat().st_mode)}


def preflight(root, plan, stage_name):
    stage = validate_plan_shape(plan, stage_name)
    errors, prepared = [], []
    try:
        guard_sources(root, plan, stage_name)
    except (OSError, ValueError, KeyError, StageError) as exc:
        errors.append(str(exc))
    for f in stage["files"]:
        try:
            prepared.append(prepare_target(root, f, stage_name))
        except (OSError, ValueError, KeyError, StageError) as exc:
            errors.append(f["path"] + ": " + str(exc))
    return prepared, errors


def atomic_write(path, data, mode=0o644):
    fd, temporary = tempfile.mkstemp(prefix="serialization-", suffix=".tmp",
                                     dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temporary, mode)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def save_receipt(path, receipt):
    data = (json.dumps(receipt, ensure_ascii=False, indent=2) + "\n").encode()
    atomic_write(path, data)


def append_progress(root, line):
    data = (line.rstrip("\n") + "\n").encode("utf-8")
    fd = os.open(root / "progress.log", os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o644)
    try:
        # One append write keeps this entry together with other append-only users.
        require(os.write(fd, data) == len(data), "short progress-log write")
        os.fsync(fd)
    finally:
        os.close(fd)


def apply_stage(root, plan, plan_hash, script_hash, stage_name, prepared):
    lock = root / "reader_reports" / "serialization_stage.lock"
    fd = os.open(lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    os.close(fd)
    transaction = None
    receipt_path = None
    receipt = None
    attempted = []
    try:
        guard_sources(root, plan, stage_name)
        for item in prepared:
            require(digest(item["path"].read_bytes())
                    == item["before_sha256"],
                    "target changed after preflight: " + item["plan"]["path"])
        stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
        transaction = (root / "reader_reports" / "serialization_receipts"
                       / (stamp + "_" + stage_name + "_" + uuid.uuid4().hex[:8]))
        transaction.mkdir(parents=True, exist_ok=False)
        # Preserve exact preimages and planned postimages; no initial report is overwritten.
        for item in prepared:
            for directory, data in (("before", item["before"]), ("after", item["after"])):
                saved = transaction / directory / item["plan"]["path"]
                saved.parent.mkdir(parents=True, exist_ok=True)
                with saved.open("xb") as stream:
                    stream.write(data)
                    stream.flush()
                    os.fsync(stream.fileno())
        receipt = {
            "plan_id": plan["plan_id"], "stage": stage_name,
            "plan_sha256": plan_hash, "script_sha256": script_hash,
            "started_at": utc(), "status": "prepared",
            "source_review": plan["source_review"],
            "targets": [{
                "path": item["plan"]["path"],
                "before_sha256": item["before_sha256"],
                "after_sha256": item["after_sha256"],
                "reference_before_sha256": item["plan"]["before_sha256"],
                "reference_after_sha256": item["plan"]["after_sha256"],
                "unrelated_field_drift": item["unrelated_field_drift"],
                "operations": [{
                    "id": op["id"], "case_ids": op["case_ids"],
                    "pointer": op.get("pointer"), "count": op["count"],
                    "old_sha256": op["old_sha256"], "new_sha256": op["new_sha256"]
                } for op in item["plan"]["operations"]]
            } for item in prepared],
            "committed_paths": [], "rollback": []
        }
        receipt_path = transaction / "receipt.json"
        save_receipt(receipt_path, receipt)
        append_progress(root, f"static serialization {stage_name} started {utc()} "
                        f"plan_sha256 {plan_hash} receipt {receipt_path.relative_to(root)}")
        receipt["status"] = "applying"
        save_receipt(receipt_path, receipt)
        for item in prepared:
            require(digest(item["path"].read_bytes())
                    == item["before_sha256"],
                    "target changed immediately before write: " + item["plan"]["path"])
            attempted.append(item)
            atomic_write(item["path"], item["after"], item["mode"])
            require(digest(item["path"].read_bytes())
                    == item["after_sha256"],
                    "post-write hash mismatch: " + item["plan"]["path"])
            receipt["committed_paths"].append(item["plan"]["path"])
            save_receipt(receipt_path, receipt)
        for item in prepared:
            require(digest(item["path"].read_bytes())
                    == item["after_sha256"],
                    "final target hash mismatch: " + item["plan"]["path"])
        receipt["status"] = "committed"
        receipt["completed_at"] = utc()
        save_receipt(receipt_path, receipt)
        append_progress(root, f"static serialization {stage_name} applied {utc()} "
                        f"files {len(prepared)} plan_sha256 {plan_hash} "
                        f"receipt {receipt_path.relative_to(root)}")
        return receipt_path
    except Exception as exc:
        rollback = []
        for item in reversed(attempted):
            try:
                observed = digest(item["path"].read_bytes())
                if observed == item["after_sha256"]:
                    atomic_write(item["path"], item["before"], item["mode"])
                    require(digest(item["path"].read_bytes())
                            == item["before_sha256"], "rollback hash mismatch")
                    state = "restored_before"
                elif observed == item["before_sha256"]:
                    state = "already_before"
                else:
                    state = "not_overwritten_unexpected_hash"
                rollback.append({"path": item["plan"]["path"], "status": state})
            except Exception as rollback_error:
                rollback.append({"path": item["plan"]["path"], "status": "rollback_failed",
                                 "error": str(rollback_error)})
        if receipt is not None:
            receipt["status"] = ("failed_rolled_back" if all(
                x["status"] in ("restored_before", "already_before") for x in rollback
            ) else "failed_requires_manual_recovery")
            receipt["error"] = str(exc)
            receipt["failed_at"] = utc()
            receipt["rollback"] = rollback
            try:
                save_receipt(receipt_path, receipt)
                append_progress(root, f"static serialization {stage_name} failed {utc()} "
                                f"status {receipt['status']} "
                                f"receipt {receipt_path.relative_to(root)}")
            except Exception as log_error:
                raise StageError(f"{exc}; receipt/log update failed: {log_error}; "
                                 f"transaction directory: {transaction}") from exc
        raise StageError(f"{exc}; transaction directory: {transaction}") from exc
    finally:
        lock.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", choices=tuple(STAGE_SCANS), default="serialization")
    parser.add_argument("--plan", type=Path,
                        default=Path(__file__).with_name("staged_serialization_plan_c.json"))
    parser.add_argument("--plan-sha256",
                        help="Exact reviewed plan digest; mandatory for --apply.")
    parser.add_argument("--apply", action="store_true",
                        help="Apply one stage only after all preconditions pass.")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    raw_plan = args.plan.read_bytes()
    plan_hash = digest(raw_plan)
    plan = json.loads(raw_plan)
    require(root == Path(plan["edition_root"]).resolve(), "edition-root mismatch")
    if args.plan_sha256 is not None:
        require(args.plan_sha256 == plan_hash, "reviewed plan digest mismatch")
    if args.apply:
        require(args.plan_sha256 is not None, "--apply requires --plan-sha256")
    script_hash = digest(Path(__file__).read_bytes())
    require(script_hash == plan["script_sha256"], "staged script digest mismatch")
    prepared, errors = preflight(root, plan, args.stage)
    result = {
        "mode": "apply" if args.apply else "preflight",
        "status": "blocked" if errors else "ready",
        "stage": args.stage, "checked_at": utc(),
        "plan_sha256": plan_hash, "script_sha256": script_hash,
        "writes_performed": False,
        "errors": errors,
        "targets": [{
            "path": item["plan"]["path"],
            "before_sha256": item["before_sha256"],
            "after_sha256": item["after_sha256"],
            "reference_before_sha256": item["plan"]["before_sha256"],
            "reference_after_sha256": item["plan"]["after_sha256"],
            "unrelated_field_drift": item["unrelated_field_drift"],
            "operation_count": len(item["plan"]["operations"]),
            "pointers": [op["pointer"] for op in item["plan"]["operations"]
                         if "pointer" in op]
        } for item in prepared]
    }
    if errors:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 2
    if args.apply:
        receipt = apply_stage(root, plan, plan_hash, script_hash, args.stage, prepared)
        result.update(status="committed", writes_performed=True, receipt=str(receipt))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, StageError) as error:
        print(json.dumps({"status": "blocked_or_failed", "error": str(error)},
                         ensure_ascii=False), file=sys.stderr)
        raise SystemExit(2)

