#!/usr/bin/env python3
"""Read-only TeX syntax and inventory-count checks; never interpret readings.

Writes this check's reports in records/ and a temporary compilation wrapper
outside the deliverable root. Never changes page fragments or inventories.
No images, context archives, or contextual documents are opened.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent


def load_helper(name):
    spec = importlib.util.spec_from_file_location(name, HERE / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=HERE.parent)
    args = parser.parse_args()
    root = args.root.resolve()
    fm = load_helper("finalize_mechanical")
    validator = load_helper("validate_structure")
    fm.TARGETS |= {"diagram", "figure", "begin", "end"}
    known = validator.COMMON | validator.CUSTOM | {"boxed", "rotatebox", "varprojlim", "wr"}
    before_hashes = {}
    issues = []
    environment_counts = Counter()
    unknown_commands = []
    inventory_counts = []
    row_kind_219 = []
    paths = []
    for cote, scan in fm.EXPECTED:
        path = root / "pages" / fm.page_name(cote, scan)
        paths.append(path)
        data = path.read_bytes()
        before_hashes[path.name] = hashlib.sha256(data).hexdigest()
        text = data.decode("utf-8")
        try:
            mask, macros = fm.scan_macros(text, path.name)
        except fm.MechanicalError as exc:
            issues.append({"file": path.name, "issue": str(exc)})
            continue
        stack = []
        for macro in macros:
            if macro.name == "begin":
                stack.append((macro.argument.strip(), macro.line))
                environment_counts[macro.argument.strip()] += 1
            elif macro.name == "end":
                name = macro.argument.strip()
                if not stack:
                    issues.append({"file": path.name, "line": macro.line,
                                   "issue": f"Unmatched end of environment {name}"})
                elif stack[-1][0] != name:
                    issues.append({"file": path.name, "line": macro.line,
                                   "issue": f"Environment end {name} does not match open {stack[-1][0]} on line {stack[-1][1]}"})
                else:
                    stack.pop()
        for name, line in stack:
            issues.append({"file": path.name, "line": line,
                           "issue": f"Unclosed environment {name}"})
        # TikZ loop variables are scoped commands, not undefined source macros.
        loop_vars = set()
        for match in re.finditer(r"\\foreach\s+((?:\\[A-Za-z]+\s*/?\s*)+)\s+in\b", mask):
            loop_vars.update(re.findall(r"\\([A-Za-z]+)", match.group(1)))
        index = 0
        while index < len(mask):
            if mask[index] != "\\":
                index += 1
                continue
            end = fm.control_end(mask, index)
            name = mask[index + 1:end]
            if name.isalpha() and name not in known and name not in loop_vars:
                unknown_commands.append({"file": path.name,
                                         "line": mask.count("\n", 0, index) + 1,
                                         "command": "\\" + name})
            index = end
        source_counts = Counter(macro.name for macro in macros)
        record = root / "records" / f"{cote}_{scan:03d}_inventory.json"
        rows = json.loads(record.read_text(encoding="utf-8"))
        manual_counts = Counter(row[4] for row in rows if len(row) == 8)
        comparison = {
            "cote": cote, "scan": scan,
            "diagram_macros": source_counts["diagram"],
            "diagram_rows": manual_counts["diagram"],
            "figure_macros": source_counts["figure"],
            "drawing_rows": manual_counts["drawing"],
            "diagram_row_deficit": max(0, source_counts["diagram"] - manual_counts["diagram"]),
            "drawing_row_deficit": max(0, source_counts["figure"] - manual_counts["drawing"]),
        }
        inventory_counts.append(comparison)
        if (cote, scan) == (15, 219):
            row_kind_219 = [{"element": row[3], "kind": row[4]} for row in rows
                            if len(row) == 8 and row[4] in {"diagram", "drawing"}]

    tex_info = {name: shutil.which(name) for name in ("pdflatex", "xelatex", "lualatex", "kpsewhich")}
    dependencies = {}
    if tex_info["kpsewhich"]:
        for name in ("pdflatex.fmt", "article.cls", "amsmath.sty", "amssymb.sty", "mathrsfs.sty", "graphicx.sty", "tikz-cd.sty"):
            result = subprocess.run([tex_info["kpsewhich"], name], capture_output=True, text=True, timeout=20)
            dependencies[name] = result.stdout.strip() or None
    temporary = Path(tempfile.mkdtemp(prefix="mpl_tex_check_", dir=root.parent))
    wrapper = r"""\documentclass{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb,mathrsfs,graphicx,tikz-cd}
\usetikzlibrary{arrows.meta,decorations.pathmorphing,patterns}
\pagestyle{empty}
\newcommand{\cotefile}[1]{}
\newcommand{\scanpage}[1]{\par\bigskip}
\newcommand{\mspage}[1]{}
\long\def\deleted#1{#1}
\long\def\inserted#1{#1}
\long\def\margin#1{#1}
\long\def\uline#1{#1}
\long\def\uuline#1{#1}
\long\def\unsure#1{#1}
\long\def\illegible#1{\ifmmode\textnormal{[ill. #1]}\else[ill. #1]\fi}
% Retokenize diagram/drawing bodies so captured TikZ ampersands retain their
% intended runtime catcodes, including diagrams nested in other state macros.
\long\def\diagram#1{\begingroup\everyeof{}\scantokens{\unexpanded{#1}}\endgroup}
\long\def\figure#1{\begingroup\everyeof{}\scantokens{\unexpanded{#1}}\endgroup}
\begin{document}
"""
    wrapper += "\n".join("\\input{" + path.as_posix() + "}\n\\clearpage" for path in paths)
    wrapper += "\n\\end{document}\n"
    wrapper_path = temporary / "syntax_wrapper.tex"
    wrapper_path.write_text(wrapper, encoding="utf-8")
    compilation = {"temporary_directory": str(temporary), "wrapper": str(wrapper_path),
                   "attempted": False, "successful": False}
    if tex_info["pdflatex"]:
        command = [tex_info["pdflatex"], "-no-shell-escape", "-no-mktex=fmt", "-interaction=nonstopmode",
                   "-halt-on-error", "-file-line-error", str(wrapper_path)]
        compilation["attempted"] = True
        try:
            result = subprocess.run(command, cwd=temporary, capture_output=True, text=True, timeout=45)
            output = result.stdout + result.stderr
            compilation["exit_code"] = result.returncode
            compilation["successful"] = result.returncode == 0
        except subprocess.TimeoutExpired as exc:
            output = str(exc)
            compilation["timed_out"] = True
        (HERE / "tex_compile_probe.log").write_text(output, encoding="utf-8")
        compilation["output_log"] = "records/tex_compile_probe.log"
        if not compilation["successful"] and any(value is None for value in dependencies.values()):
            compilation["status"] = "TeX binaries exist but required format/class/package files are unavailable; manuscript compilation not validated."
        elif not compilation["successful"]:
            compilation["status"] = "Compilation failed; inspect the probe log for concrete source/wrapper errors."
        else:
            compilation["status"] = "Temporary wrapper compilation succeeded."
    else:
        compilation["status"] = "No pdflatex executable available; compilation not attempted."
    after_hashes = {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
    changed = [name for name, digest in before_hashes.items() if after_hashes[name] != digest]
    report = {
        "scope": "Read-only mechanical checks; no manuscript meaning, source images, or context inspected.",
        "page_count": len(paths), "brace_environment_issues": issues,
        "environment_occurrences": dict(environment_counts),
        "unclassified_commands": unknown_commands,
        "standard_commands_not_in_original_advisory_list": ["\\boxed", "\\rotatebox", "\\varprojlim", "\\wr"],
        "inventory_comparisons": inventory_counts,
        "inventory_count_deficits": [row for row in inventory_counts if row["diagram_row_deficit"] or row["drawing_row_deficit"]],
        "cote_15_scan_219_diagram_drawing_rows": row_kind_219,
        "tex_executables": tex_info, "tex_dependencies": dependencies, "compilation": compilation,
        "page_hashes_unchanged_during_check": not changed, "changed_page_files_during_check": changed,
        "page_sha256_at_check_start": before_hashes,
        "limits": "Equal macro/row counts do not establish semantic correspondence or inventory completeness; compilation cannot be claimed if the TeX installation lacks dependencies.",
    }
    (HERE / "tex_mechanical_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "page_count": len(paths), "brace_environment_issues": issues,
        "unclassified_commands": unknown_commands,
        "inventory_count_deficits": report["inventory_count_deficits"],
        "cote_15_scan_219_diagram_drawing_rows": row_kind_219,
        "compilation": compilation, "page_hashes_unchanged_during_check": not changed,
        "report": str(HERE / "tex_mechanical_report.json"),
    }, ensure_ascii=False, indent=2))
    return 0 if not issues and not changed else 1


if __name__ == "__main__":
    raise SystemExit(main())
