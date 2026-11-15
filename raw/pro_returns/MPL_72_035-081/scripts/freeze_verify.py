#!/usr/bin/env python3
"""Verify the transcription freeze without writing files or changing any log record."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

PREFIX = "MPL_72_035-081"
SCANS = tuple(range(35, 82))
PAGE_PATHS = tuple(f"pages/{PREFIX}_72_scan{scan:03d}.tex" for scan in SCANS)
COMBINED_PATH = f"{PREFIX}_transcription.tex"
EXPECTED_PATHS = PAGE_PATHS + (COMBINED_PATH,)
TIME_PATTERN = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC"
TIME_FORMAT = "%Y-%m-%d %H:%M:%S UTC"
DIGEST_PATTERN = r"[0-9A-Fa-f]{64}"
AUDIT_RE = re.compile(rf"scan (\d{{3}}) audited ({TIME_PATTERN})")
FREEZE_RE = re.compile(rf"transcription frozen ({TIME_PATTERN})")
CONTEXT_RE = re.compile(rf"context opened ({TIME_PATTERN})")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def hash_record(line: str):
    """Return (path, digest) for the documented manifest line forms."""
    patterns = (
        (rf"\s*({DIGEST_PATTERN})\s+\*?(\S+)\s*", True),
        (rf"\s*SHA-?256\s+({DIGEST_PATTERN})\s+\*?(\S+)\s*", True),
        (rf"\s*SHA-?256\s+(\S+?)\s+({DIGEST_PATTERN})\s*", False),
        (rf"\s*(\S+?)\s*:\s*({DIGEST_PATTERN})\s*", False),
    )
    for pattern, digest_first in patterns:
        match = re.fullmatch(pattern, line, flags=re.IGNORECASE)
        if match:
            first, second = match.groups()
            path, digest = (second, first) if digest_first else (first, second)
            return path, digest.lower()
    return None


def canonical_hash_path(value: str, root: Path):
    """Map a recorded path onto one expected relative path, preserving identity."""
    path = Path(value)
    if path.is_absolute():
        try:
            relative = path.relative_to(root).as_posix()
        except ValueError:
            return None
    else:
        relative = path.as_posix()
    if ".." in Path(relative).parts:
        return None
    if relative in EXPECTED_PATHS:
        return relative
    # Bare page filenames are unambiguous within this fixed package.
    bare_pages = {Path(name).name: name for name in PAGE_PATHS}
    if len(Path(relative).parts) == 1 and relative in bare_pages:
        return bare_pages[relative]
    return None


def verify_freeze(root: Path, require_context: bool = False):
    root = root.resolve()
    errors = []
    facts = {
        "expected_page_count": 47,
        "expected_hash_count": 48,
        "expected_audit_count": 47,
        "require_context": require_context,
    }

    def fail(message):
        errors.append(message)

    def parse_time(value, label):
        if not re.fullmatch(TIME_PATTERN, value):
            fail(f"{label}: timestamp must use YYYY-MM-DD HH:MM:SS UTC")
            return None
        try:
            return datetime.strptime(value, TIME_FORMAT).replace(tzinfo=timezone.utc)
        except ValueError as exc:
            fail(f"{label}: invalid UTC timestamp ({exc})")
            return None

    log_path = root / "progress.log"
    if not log_path.is_file():
        return {"ok": False, "root": str(root), "errors": ["progress.log is absent"], "facts": facts}
    try:
        log_bytes = log_path.read_bytes()
        lines = log_bytes.decode("utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        return {"ok": False, "root": str(root), "errors": [f"Cannot read progress.log: {exc}"], "facts": facts}
    facts["progress_log_sha256"] = sha256(log_bytes)
    start_time = parse_time(lines[0], "Log first line") if lines else None
    if not lines:
        fail("progress.log is empty")

    audits = []
    freezes = []
    contexts = []
    manifest = []
    non_tex_hashes = []
    timestamps = []
    for index, line in enumerate(lines, 1):
        match = AUDIT_RE.fullmatch(line)
        if match:
            scan = int(match[1])
            time = parse_time(match[2], f"Audit line {index}")
            audits.append({"scan": scan, "line": index, "time": time})
            timestamps.append((index, time, "audit"))
        elif re.match(r"\s*scan\b.*\baudited\b", line):
            fail(f"Line {index}: malformed audit record")
        match = FREEZE_RE.fullmatch(line)
        if match:
            time = parse_time(match[1], f"Freeze line {index}")
            freezes.append({"line": index, "time": time})
            timestamps.append((index, time, "freeze"))
        elif line.lstrip().startswith("transcription frozen"):
            fail(f"Line {index}: malformed freeze record")
        match = CONTEXT_RE.fullmatch(line)
        if match:
            time = parse_time(match[1], f"Context line {index}")
            contexts.append({"line": index, "time": time})
            timestamps.append((index, time, "context"))
        elif line.lstrip().startswith("context opened"):
            fail(f"Line {index}: malformed context-open record")
        parsed = hash_record(line)
        if parsed:
            recorded_path, digest = parsed
            if recorded_path.lower().endswith(".tex"):
                canonical = canonical_hash_path(recorded_path, root)
                manifest.append({"path": canonical, "recorded_path": recorded_path, "digest": digest, "line": index})
                if canonical is None:
                    fail(f"Hash line {index}: unexpected or noncanonical TeX path {recorded_path!r}")
            else:
                non_tex_hashes.append({"path": recorded_path, "line": index})
        elif ".tex" in line and (
            re.search(rf"(?<![0-9A-Fa-f]){DIGEST_PATTERN}(?![0-9A-Fa-f])", line)
            or re.match(r"\s*SHA-?256\b", line, re.IGNORECASE)
        ):
            fail(f"Line {index}: malformed TeX hash record; use a documented manifest format")

    facts["audit_entry_count"] = len(audits)
    facts["hash_entry_count"] = len(manifest)
    facts["freeze_entry_count"] = len(freezes)
    facts["context_entry_count"] = len(contexts)
    facts["non_tex_hash_records_ignored"] = non_tex_hashes
    if len(audits) != 47:
        fail(f"Expected exactly 47 audit entries; found {len(audits)}")
    audit_counts = Counter(item["scan"] for item in audits)
    for scan in SCANS:
        if audit_counts[scan] == 0:
            fail(f"Missing audit for scan {scan:03d}")
        elif audit_counts[scan] > 1:
            fail(f"Duplicate audits for scan {scan:03d}: {audit_counts[scan]} entries")
    for scan in sorted(set(audit_counts) - set(SCANS)):
        fail(f"Unexpected audit scan {scan:03d}")
    if len(freezes) != 1:
        fail(f"Expected exactly one transcription frozen record; found {len(freezes)}")
    if len(contexts) > 1:
        fail(f"Expected at most one context opened record; found {len(contexts)}")
    if require_context and len(contexts) != 1:
        fail("Final verification requires exactly one context opened record")

    previous_time = start_time
    for index, time, label in sorted(timestamps):
        if time is None:
            continue
        if previous_time is not None and time < previous_time:
            fail(f"Line {index}: {label} timestamp precedes an earlier logged status timestamp")
        previous_time = time
    if len(freezes) == 1:
        freeze = freezes[0]
        for audit in audits:
            if audit["line"] >= freeze["line"]:
                fail(f"Scan {audit['scan']:03d} audit is not before the freeze record")
            if audit["time"] is not None and freeze["time"] is not None and audit["time"] > freeze["time"]:
                fail(f"Scan {audit['scan']:03d} audit timestamp is later than freeze timestamp")
        if len(contexts) == 1:
            context = contexts[0]
            if context["line"] <= freeze["line"]:
                fail("Context-open record precedes the freeze record")
            if context["time"] is not None and freeze["time"] is not None and context["time"] < freeze["time"]:
                fail("Context-open timestamp precedes freeze timestamp")
    if contexts:
        first_context_line = min(item["line"] for item in contexts)
        for item in manifest:
            if item["line"] >= first_context_line:
                fail(f"Hash for {item['recorded_path']} was recorded after opening context")

    if len(manifest) != 48:
        fail(f"Expected exactly 48 transcription hash entries; found {len(manifest)}")
    path_counts = Counter(item["path"] for item in manifest if item["path"] is not None)
    for relative in EXPECTED_PATHS:
        if path_counts[relative] == 0:
            fail(f"Missing frozen hash: {relative}")
        elif path_counts[relative] > 1:
            fail(f"Duplicate frozen hashes: {relative} ({path_counts[relative]} entries)")

    recorded_hashes = {item["path"]: item["digest"] for item in manifest if item["path"] is not None}
    current_bytes = {}
    current_hashes = {}
    for relative in EXPECTED_PATHS:
        path = root / relative
        if path.is_symlink():
            fail(f"Expected regular source file, found symlink: {relative}")
            continue
        try:
            data = path.read_bytes()
        except OSError as exc:
            fail(f"Cannot read {relative}: {exc}")
            continue
        current_bytes[relative] = data
        digest = sha256(data)
        current_hashes[relative] = digest
        recorded = recorded_hashes.get(relative)
        if recorded is not None and recorded != digest:
            fail(f"Frozen SHA-256 mismatch: {relative}")
    observed_pages = {path.relative_to(root).as_posix() for path in (root / "pages").glob("*.tex")}
    for relative in sorted(observed_pages - set(PAGE_PATHS)):
        fail(f"Unexpected page fragment in pages/: {relative}")
    if all(relative in current_bytes for relative in EXPECTED_PATHS):
        matches = current_bytes[COMBINED_PATH] == b"".join(current_bytes[relative] for relative in PAGE_PATHS)
        facts["combined_is_direct_byte_concatenation"] = matches
        if not matches:
            fail("Combined transcription differs from direct byte concatenation of scans 035–081")
    else:
        facts["combined_is_direct_byte_concatenation"] = None
    facts["readable_expected_files"] = len(current_bytes)
    facts["matching_unique_expected_hashes"] = sum(
        path_counts[relative] == 1 and current_hashes.get(relative) == recorded_hashes.get(relative)
        for relative in EXPECTED_PATHS
    )
    facts["scope"] = (
        "Recorded-file integrity and log consistency only. Audit records are checked as records; "
        "this tool does not establish that visual readings were performed or that transcription/notes are complete. "
        "It writes no freeze, verification, or completion record."
    )
    return {"ok": not errors, "root": str(root), "errors": errors, "facts": facts}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--require-context", action="store_true", help="Require the single later context-open record for final verification")
    parser.add_argument("--json", action="store_true", help="Print the full diagnostic result as JSON")
    args = parser.parse_args()
    result = verify_freeze(args.root, args.require_context)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("Freeze integrity: " + ("PASS" if result["ok"] else "FAIL"))
        facts = result["facts"]
        print(f"Audit entries: {facts.get('audit_entry_count', 0)}/47; transcription hash entries: {facts.get('hash_entry_count', 0)}/48; matching unique hashes: {facts.get('matching_unique_expected_hashes', 0)}/48")
        for error in result["errors"]:
            print("ERROR: " + error)
        print(facts.get("scope", "Read-only verification; no task record was changed."))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
