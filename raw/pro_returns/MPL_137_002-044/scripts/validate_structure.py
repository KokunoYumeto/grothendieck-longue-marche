#!/usr/bin/env python3
"""Read-only validation of the transcription's packaging and LaTeX structure.

This checker does not open scans or context, read image pixels, recognize text,
interpret mathematics, or alter any page. Its sole output file is the report in
records/structural_validation.txt. Run again after the last audit and at freeze.
"""
from __future__ import annotations

import ast
import csv
import hashlib
import json
import re
import shutil
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = tuple(i for i in range(2, 45) if i != 6)
COLUMNS = (
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
)
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
MACROS = (
    "cotefile", "scanpage", "mspage", "deleted", "inserted", "margin",
    "uline", "uuline", "diagram", "figure", "unsure", "illegible",
)
IMAGE_COMMANDS = {
    "includegraphics", "includepdf", "epsfig", "epsfbox", "pdfximage",
    "pdfrefximage", "XeTeXpicfile", "XeTeXpdffile", "pgfimage",
}
OCR_ENGINES = {
    "tesseract", "pytesseract", "easyocr", "paddleocr", "keras_ocr",
    "ocrmypdf", "pyocr", "rapidocr", "doctr",
}


def uncomment(source: str) -> str:
    """Remove unescaped TeX comments, retaining line numbers and escaped %."""
    out = []
    for line in source.splitlines(keepends=True):
        cut = None
        for i, char in enumerate(line):
            if char != "%":
                continue
            slashes = 0
            j = i - 1
            while j >= 0 and line[j] == "\\":
                slashes += 1
                j -= 1
            if slashes % 2 == 0:
                cut = i
                break
        out.append(line if cut is None else line[:cut] + ("\n" if line.endswith("\n") else ""))
    return "".join(out)


def lexical_issues(source: str) -> list[str]:
    """Check grouping, explicit environments, and explicit math delimiters.

    This is a lexical check, not TeX expansion. Dollar math nested inside a
    display may occur in a text argument, so only its delimiter pairing is
    checked. User macros are treated as ordinary braced arguments.
    """
    source = uncomment(source)
    braces = []
    environments = []
    math = []
    issues = []
    pattern = re.compile(
        r"\\(?:begin\s*\{([^}]+)\}|end\s*\{([^}]+)\}|[A-Za-z]+|.)|\$\$|[{}$]",
        re.DOTALL,
    )
    for match in pattern.finditer(source):
        token = match.group()
        line = source.count("\n", 0, match.start()) + 1
        if token == "{":
            braces.append(line)
        elif token == "}":
            if braces:
                braces.pop()
            else:
                issues.append(f"line {line}: extra closing brace")
        elif match.group(1):
            environments.append((match.group(1), line))
        elif match.group(2):
            name = match.group(2)
            if environments and environments[-1][0] == name:
                environments.pop()
            else:
                issues.append(f"line {line}: unmatched end of {name!r}; open stack {environments!r}")
        elif token in (r"\[", r"\("):
            if math:
                issues.append(f"line {line}: explicit math opener {token!r} within {math[-1]!r}")
            math.append((token, line))
        elif token in (r"\]", r"\)"):
            expected = r"\[" if token == r"\]" else r"\("
            if math and math[-1][0] == expected:
                math.pop()
            else:
                issues.append(f"line {line}: unmatched math closer {token!r}; open stack {math!r}")
        elif token in ("$", "$$"):
            if math and math[-1][0] == token:
                math.pop()
            else:
                math.append((token, line))
    issues.extend(f"line {line}: unclosed brace" for line in braces)
    issues.extend(f"line {line}: unclosed environment {name!r}" for name, line in environments)
    issues.extend(f"line {line}: unclosed math delimiter {name!r}" for name, line in math)
    return issues


def call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return call_name(node.value) + "." + node.attr
    return ""


def ocr_code_issues(path: Path) -> list[str]:
    """Inspect executable Python syntax, excluding comments/docstrings.

    Known engine imports/calls and command invocations are checked. PIL/numpy
    cropping, contrast changes and other visual enhancement are not OCR.
    This cannot establish the history of tools run outside the saved scripts.
    """
    issues = []
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError as exc:
        return [f"line {exc.lineno}: Python syntax error: {exc.msg}"]
    engine_re = re.compile(r"(?<![A-Za-z0-9_])(?:" + "|".join(sorted(OCR_ENGINES)) + r")(?![A-Za-z0-9_])", re.I)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names = [item.name.split(".")[0] for item in node.names]
            for name in names:
                if name.lower() in OCR_ENGINES:
                    issues.append(f"line {node.lineno}: known OCR engine import {name!r}")
        elif isinstance(node, ast.ImportFrom):
            name = (node.module or "").split(".")[0]
            if name.lower() in OCR_ENGINES:
                issues.append(f"line {node.lineno}: known OCR engine import {name!r}")
        elif isinstance(node, ast.Call):
            name = call_name(node.func)
            if engine_re.search(name):
                issues.append(f"line {node.lineno}: known OCR engine call {name!r}")
            if name in {"os.system", "os.popen", "subprocess.run", "subprocess.call", "subprocess.Popen", "subprocess.check_call", "subprocess.check_output"}:
                for arg in node.args:
                    for value in ast.walk(arg):
                        if isinstance(value, ast.Constant) and isinstance(value.value, str) and engine_re.search(value.value):
                            issues.append(f"line {node.lineno}: known OCR engine command invocation")
    return issues


def main() -> int:
    errors = []
    warnings = []
    checks = []
    pages = sorted((ROOT / "pages").glob("*.tex"))
    page_sources = {}
    actual = []
    for path in pages:
        match = re.fullmatch(r"MPL_137_002-044_137_scan(\d{3})\.tex", path.name)
        if not match:
            errors.append(f"unexpected page filename: {path.name}")
            continue
        scan = int(match.group(1))
        actual.append(scan)
        page_sources[path] = path.read_text(encoding="utf-8")
    if tuple(actual) != EXPECTED:
        errors.append(f"page scan set/order {actual!r} differs from {list(EXPECTED)!r}")
    else:
        checks.append("42 page files: exact scan set/order 002–044, excluding 006.")

    combined_path = ROOT / "MPL_137_002-044_transcription.tex"
    combined = combined_path.read_text(encoding="utf-8")
    if combined != "\n".join(page_sources.values()):
        errors.append("combined fragment is not exactly the sorted page files joined with one newline")
    else:
        checks.append("Combined fragment is byte-for-byte the sorted page text joined with one newline (UTF-8).")

    clean_combined = uncomment(combined)
    if re.findall(r"\\scanpage\{(\d+)\}", clean_combined) != [str(i) for i in EXPECTED]:
        errors.append("combined scanpage macro sequence differs from expected scans")
    if re.findall(r"\\cotefile\{([^}]*)\}", clean_combined) != ["137"]:
        errors.append("combined fragment must contain exactly one cotefile{137}")
    if not re.match(r"\s*\\cotefile\{137\}\s*\\scanpage\{2\}", clean_combined):
        errors.append("combined fragment does not begin with cotefile{137}, then scanpage{2}")

    for path, source in page_sources.items():
        scan = int(path.stem[-3:])
        clean = uncomment(source)
        if re.findall(r"\\scanpage\{([^}]*)\}", clean) != [str(scan)]:
            errors.append(f"{path.name}: expected exactly one matching scanpage macro")
        expected_cote = ["137"] if scan == 2 else []
        if re.findall(r"\\cotefile\{([^}]*)\}", clean) != expected_cote:
            errors.append(f"{path.name}: unexpected cotefile macro")
        errors.extend(f"{path.name}: {message}" for message in lexical_issues(source))
        commands = set(re.findall(r"\\([A-Za-z]+)", clean))
        forbidden = sorted(commands & IMAGE_COMMANDS)
        if forbidden:
            errors.append(f"{path.name}: forbidden image inclusion commands {forbidden!r}")
        if re.search(r"\\(?:documentclass|usepackage)\b|\\begin\{document\}", clean):
            errors.append(f"{path.name}: preamble/document wrapper appears in fragment")
        if re.search(r"\\special\s*\{[^}]*\b(?:psfile|pdf|image)\b", clean, re.I):
            errors.append(f"{path.name}: image-related special command")
    errors.extend(f"combined fragment: {message}" for message in lexical_issues(combined))
    checks.append("Checked per-page and combined braces, explicit environments and explicit math delimiters lexically.")
    checks.append("Checked page/cote macro counts, absence of preamble, and image inclusion commands in all TeX pages.")

    with (ROOT / "MPL_137_002-044_inventory.csv").open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        if tuple(reader.fieldnames or ()) != COLUMNS:
            errors.append(f"inventory columns differ from required schema: {reader.fieldnames!r}")
    row_scans = Counter()
    element_ids = []
    for index, row in enumerate(rows, 2):
        if None in row:
            errors.append(f"inventory row {index}: extra unnamed columns")
        if row.get("kind") not in KINDS:
            errors.append(f"inventory row {index}: invalid kind {row.get('kind')!r}")
        if row.get("sheet_kind") not in SHEET_KINDS:
            errors.append(f"inventory row {index}: invalid sheet_kind {row.get('sheet_kind')!r}")
        if row.get("cote") != "137":
            errors.append(f"inventory row {index}: cote is not 137")
        if row.get("transcribed") != "yes":
            errors.append(f"inventory row {index}: transcribed is not yes")
        try:
            row_scans[int(row.get("scan", ""))] += 1
        except ValueError:
            errors.append(f"inventory row {index}: non-numeric scan")
        element_ids.append(row.get("element"))
    if tuple(sorted(row_scans)) != EXPECTED:
        errors.append("inventory scan coverage differs from expected scans")
    duplicate_ids = sorted(str(key) for key, n in Counter(element_ids).items() if n > 1)
    if duplicate_ids:
        errors.append(f"duplicate inventory element IDs: {duplicate_ids!r}")
    checks.append(f"Inventory: {len(rows)} rows; required columns, kinds, sheet kinds, scan coverage, unique element IDs and yes status checked.")

    record_paths = sorted((ROOT / "records").glob("[0-9][0-9][0-9].json"))
    if [int(p.stem) for p in record_paths] != list(EXPECTED):
        errors.append("JSON record set differs from expected scans")
    for path in record_paths:
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.name}: invalid record: {exc}")
            continue
        if record.get("scan") != int(path.stem):
            errors.append(f"{path.name}: mismatched internal scan number")
        if record.get("sheet_kind") not in SHEET_KINDS:
            errors.append(f"{path.name}: invalid sheet_kind")
        for index, element in enumerate(record.get("elements", []), 1):
            if not isinstance(element, list) or len(element) != 3 or element[0] not in KINDS:
                errors.append(f"{path.name}: invalid element structure at {index}")
    checks.append(f"JSON records: {len(record_paths)} expected records, scan identities and structural fields checked.")

    python_paths = sorted((ROOT / "scripts").glob("*.py"))
    for path in python_paths:
        if path.resolve() == Path(__file__).resolve():
            continue
        errors.extend(f"{path.name}: {message}" for message in ocr_code_issues(path))
    checks.append(f"Saved Python scripts: {len(python_paths) - 1} inspected for known OCR engine imports/calls or subprocess invocations; comments and visual enhancement are not treated as OCR.")

    compile_info = []
    for name in ("pdflatex", "xelatex", "lualatex", "tectonic", "kpsewhich"):
        compile_info.append(f"{name}: {shutil.which(name) or 'not found'}")
    packages = ("tikz-cd.sty", "tikz.sty", "amsmath.sty", "amssymb.sty", "fontspec.sty", "ulem.sty")
    kpsewhich = shutil.which("kpsewhich")
    absent = []
    if kpsewhich:
        for name in packages:
            result = subprocess.run([kpsewhich, name], capture_output=True, text=True, timeout=10, check=False)
            location = result.stdout.strip()
            compile_info.append(f"{name}: {location or 'not found'}")
            if not location:
                absent.append(name)
    if absent or not kpsewhich:
        warnings.append("Compilation not performed: required TeX packages are unavailable; this report establishes lexical structure, not successful typesetting.")

    # Detect a concurrent audit edit rather than misreport a stale snapshot as final.
    for path, source in page_sources.items():
        if path.read_text(encoding="utf-8") != source:
            warnings.append(f"{path.name} changed while validation ran; rerun after the audit.")
    if combined_path.read_text(encoding="utf-8") != combined:
        warnings.append("Combined fragment changed while validation ran; rerun after the audit.")

    macro_counts = {name: len(re.findall(r"\\" + name + r"\b", clean_combined)) for name in MACROS}
    lines = [
        "MPL_137_002-044 structural validation",
        "UTC: " + datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "Result: " + ("FAIL" if errors else "PASS (lexical checks; see compilation limitation)"),
        "Scope: packaging and syntax only; no scans/context opened, no OCR, no mathematical or palaeographic judgment, no page edits.",
        "Combined snapshot SHA-256: " + hashlib.sha256(combined.encode("utf-8")).hexdigest(),
        "",
        "Checks:",
        *["- " + text for text in checks],
        "",
        "Combined user-macro counts:",
        *[f"- \\{name}: {count}" for name, count in macro_counts.items()],
        "",
        "Errors:",
        *(["- " + text for text in errors] or ["- None."]),
        "",
        "Warnings and limits:",
        *(["- " + text for text in warnings] or ["- None."]),
        "- OCR screening checks saved executable code for known engines; it cannot establish the history of unsaved external commands.",
        "- Balanced syntax does not establish transcription completeness, semantic correctness, or faithful diagram geometry.",
        "",
        "TeX availability:",
        *["- " + text for text in compile_info],
        "",
        "Rerun: python scripts/validate_structure.py (from the deliverable directory).",
    ]
    report = "\n".join(lines) + "\n"
    (ROOT / "records" / "structural_validation.txt").write_text(report, encoding="utf-8")
    print(report)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
