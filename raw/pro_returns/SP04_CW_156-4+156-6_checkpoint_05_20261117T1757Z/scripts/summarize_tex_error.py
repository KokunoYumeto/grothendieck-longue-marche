#!/usr/bin/env python3
"""Map compiler diagnostics mechanically; never emit manuscript prose.

Exact reassembly of a current page-file prefix must match the compiled byte
snapshot before a corpus line is mapped to a page/local line. No input is
edited. The report emits compiler categories and control-word tokens only.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

OUT = Path(__file__).resolve().parents[1]


def error_category(message):
    known = ["Undefined control sequence", "Missing $ inserted", "Missing } inserted",
             "Missing { inserted", "Extra }, or forgotten $", "Double superscript", "Double subscript",
             "Extra alignment tab has been changed to", "Missing \\cr inserted",
             "Misplaced alignment tab character", "Misplaced \\noalign", "Misplaced \\cr",
             "Bad math environment delimiter", "Display math should end with $$",
             "Paragraph ended before", "File ended while scanning", "TeX capacity exceeded",
             "Missing number, treated as zero", "Illegal unit of measure", "Improper \\prevdepth",
             "Extra \\endgroup", "Missing \\endgroup inserted", "Missing \\right inserted",
             "Extra \\right", "Emergency stop"]
    for category in known:
        if category in message:
            return category
    if "Argument of" in message and "has an extra }" in message:
        return "Macro argument has an extra }"
    match = re.search(r"Package ([A-Za-z0-9-]+) Error", message)
    if match:
        return "Package " + match.group(1) + " Error"
    if "LaTeX Error" in message:
        return "LaTeX Error"
    return "Unclassified TeX error (see compiler log)"


def page_map_for_snapshot(snapshot, out):
    data = snapshot.read_bytes()
    fragments, boundaries = [], []
    next_line = 1
    page_pattern = re.compile(r"^J156-[46]-\d{2}_156-[46]_scan\d{3}\.tex$")
    for path in sorted((out / "pages").glob("*.tex")):
        if not page_pattern.fullmatch(path.name):
            continue
        fragment = path.read_text(encoding="utf-8").rstrip()
        fragments.append(fragment)
        count = fragment.count("\n")
        boundaries.append({"filename": path.name, "start": next_line, "end": next_line + count})
        next_line += count + 2
        assembled = ("\n\n".join(fragments) + "\n").encode("utf-8")
        if assembled == data:
            return boundaries
        if len(assembled) > len(data):
            break
    return None


def summarize(result_path, out=OUT):
    out = Path(out).resolve()
    result = json.loads(Path(result_path).read_text(encoding="utf-8"))
    directory = Path(result["directory"])
    snapshot = directory / "transcription.tex"
    mapping = page_map_for_snapshot(snapshot, out)
    diagnostics = []
    for job in result["jobs"]:
        if job.get("exit_code") == 0:
            continue
        log_path = Path(job["log"])
        if not log_path.is_file():
            diagnostics.append({"error_type": "Compiler log unavailable", "page_filename": None,
                                "local_line": None, "macro_control_word_tokens": [], "compiler_log_path": str(log_path)})
            continue
        lines = log_path.read_text(encoding="utf-8", errors="replace").splitlines()
        found = False
        for index, line in enumerate(lines):
            match = re.match(r"^(.+?\.tex):(\d+):\s*(.*)$", line)
            if not match:
                continue
            compiled_file, line_number, message = match.groups()
            global_line = int(line_number)
            page = None
            local = None
            if Path(compiled_file).name == "transcription.tex" and mapping:
                for boundary in mapping:
                    if boundary["start"] <= global_line <= boundary["end"]:
                        page = boundary["filename"]
                        local = global_line - boundary["start"] + 1
                        break
            elif Path(compiled_file).name != "transcription.tex":
                page, local = Path(compiled_file).name, global_line
            tokens = re.findall(r"\\[A-Za-z@]+", message)
            if not tokens:
                # Retain only control words from TeX's diagnostic context; no
                # surrounding text, formula arguments, or manuscript words.
                for context in lines[index+1:index+8]:
                    if context.startswith("l.") or context.lstrip().startswith("<"):
                        tokens.extend(re.findall(r"\\[A-Za-z@]+", context))
            diagnostics.append({"error_type": error_category(message), "page_filename": page,
                                "local_line": local, "macro_control_word_tokens": list(dict.fromkeys(tokens)),
                                "compiler_log_path": str(log_path)})
            found = True
            break
        if not found:
            diagnostics.append({"error_type": "Compiler stopped without a file-line diagnostic", "page_filename": None,
                                "local_line": None, "macro_control_word_tokens": [], "compiler_log_path": str(log_path)})
    return {"recorded_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
            "snapshot_sha256": hashlib.sha256(snapshot.read_bytes()).hexdigest(),
            "page_line_mapping_exact": mapping is not None, "all_passed": result["all_passed"],
            "result_path": str(result_path), "diagnostics": diagnostics}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("result", type=Path)
    parser.add_argument("--out", type=Path, default=OUT)
    args = parser.parse_args()
    report = summarize(args.result, args.out)
    print(json.dumps(report["diagnostics"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
