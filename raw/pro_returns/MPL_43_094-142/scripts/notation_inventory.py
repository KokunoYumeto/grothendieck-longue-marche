#!/usr/bin/env python3
"""Text-only notation/markup inventory; never select readings or edit pages."""

from __future__ import annotations

import argparse
import bisect
import csv
import hashlib
import importlib.util
import io
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


PREFIX = "MPL_43_094-142"
SCANS = [n for n in range(94, 143) if n not in {99, 111, 127}]
FONT_COMMANDS = {
    "mathcal", "mathscr", "mathfrak", "mathbb", "mathbf", "mathrm",
    "mathsf", "mathtt", "mathit", "mathnormal", "boldsymbol", "bm",
}
ACCENT_COMMANDS = {
    "underline", "overline", "hat", "widehat", "tilde", "widetilde",
    "bar", "vec", "dot", "ddot", "dddot", "ddddot", "acute", "grave",
    "breve", "check", "mathring", "uline", "uuline", "textcircled",
}
STATE_COMMANDS = {"unsure", "deleted", "inserted", "margin", "uline", "uuline"}
TEXT_COMMANDS = {"text", "textrm", "textsf", "texttt", "textbf", "textit", "textnormal", "mbox"}
ARGUMENT_COMMANDS = FONT_COMMANDS | ACCENT_COMMANDS | STATE_COMMANDS | TEXT_COMMANDS | {
    "operatorname", "mathop", "cotefile", "scanpage", "mspage",
}
MATH_ENVS = {
    "equation", "equation*", "align", "align*", "aligned", "gather", "gather*",
    "gathered", "multline", "multline*", "eqnarray", "eqnarray*", "array",
    "matrix", "pmatrix", "bmatrix", "Bmatrix", "vmatrix", "Vmatrix", "cases",
    "tikzcd", "displaymath", "math",
}
COMMAND_RE = re.compile(r"\\([A-Za-z@]+|.)", re.DOTALL)
COEFFICIENTS = {"sigma", "gamma", "tau", "Sigma", "Gamma", "Tau"}
UNICODE_COEFFICIENTS = {"σ": "sigma", "γ": "gamma", "τ": "tau", "Σ": "Sigma", "Γ": "Gamma", "Τ": "Tau"}
UNICODE_N = {"ℕ": "U+2115", "𝒩": "U+1D4A9", "𝓝": "U+1D4DD"}


def masked_tex(text: str) -> str:
    """Hide comments and inline verbatim while retaining all source offsets."""
    out = list(text)
    i = 0
    while i < len(text):
        if text[i] == "%":
            end = text.find("\n", i)
            end = len(text) if end < 0 else end
            out[i:end] = " " * (end - i)
            i = end
        elif text[i] == "\\":
            match = COMMAND_RE.match(text, i)
            if not match:
                i += 1
                continue
            start = i
            i = match.end()
            if match.group(1) == "verb":
                if i < len(text) and text[i] == "*":
                    i += 1
                if i < len(text) and not text[i].isspace():
                    end = text.find(text[i], i + 1)
                    if end >= 0 and "\n" not in text[i:end]:
                        out[start:end + 1] = " " * (end + 1 - start)
                        i = end + 1
        else:
            i += 1
    return "".join(out)


class Page:
    def __init__(self, scan: int, data: bytes):
        self.scan = scan
        self.text = data.decode("utf-8")
        self.clean = masked_tex(self.text)
        self.newlines = [-1] + [m.start() for m in re.finditer("\n", self.text)]
        self.commands = [
            {"name": m.group(1), "start": m.start(), "end": m.end()}
            for m in COMMAND_RE.finditer(self.clean)
        ]
        self.command_at = {item["start"]: item for item in self.commands}
        self.command_positions = set()
        for item in self.commands:
            self.command_positions.update(range(item["start"], item["end"]))
        self.braces = {}
        stack = []
        i = 0
        while i < len(self.clean):
            if i in self.command_at:
                i = self.command_at[i]["end"]
                continue
            if self.clean[i] == "{":
                stack.append(i)
            elif self.clean[i] == "}" and stack:
                self.braces[stack.pop()] = i
            i += 1
        self.arguments = []
        for item in self.commands:
            if item["name"] in ARGUMENT_COMMANDS:
                arg = self.argument(item["end"])
                if arg:
                    item["argument"] = arg
                    self.arguments.append(item)
        self.math_flags = self.math_syntax_flags()
        self.arrow_options, self.arrow_labels = self.arrow_ranges()
        self.paired_close_quotes = {
            match.end() - 2
            for match in re.finditer(r"``[\s\S]*?''", self.clean)
        }

    def line(self, position: int) -> int:
        return bisect.bisect_right(self.newlines, position - 1)

    def column(self, position: int) -> int:
        return position - self.newlines[self.line(position) - 1]

    def argument(self, position: int) -> dict | None:
        while position < len(self.clean) and self.clean[position].isspace():
            position += 1
        if position < len(self.clean) and self.clean[position] == "*":
            position += 1
            while position < len(self.clean) and self.clean[position].isspace():
                position += 1
        if position >= len(self.clean):
            return None
        if self.clean[position] == "{" and position in self.braces:
            end = self.braces[position] + 1
            return {"start": position, "end": end, "body_start": position + 1, "body_end": end - 1, "form": "braced"}
        if position in self.command_at:
            end = self.command_at[position]["end"]
            return {"start": position, "end": end, "body_start": position, "body_end": end, "form": "control_sequence"}
        return {"start": position, "end": position + 1, "body_start": position, "body_end": position + 1, "form": "single_character"}

    def ancestors(self, position: int) -> list[dict]:
        result = [item for item in self.arguments if item["argument"]["body_start"] <= position < item["argument"]["body_end"]]
        return sorted(result, key=lambda item: item["argument"]["end"] - item["start"], reverse=True)

    def math_syntax_flags(self) -> list[bool]:
        flags = [False] * len(self.clean)
        delimiters = []
        environments = []
        i = 0
        while i < len(self.clean):
            active = bool(delimiters or environments)
            flags[i] = active
            item = self.command_at.get(i)
            if item:
                name = item["name"]
                end = item["end"]
                flags[i:end] = [active] * (end - i)
                if name in {"[", "("}:
                    delimiters.append(name)
                elif name in {"]", ")"}:
                    if delimiters:
                        delimiters.pop()
                elif name in {"begin", "end"}:
                    arg = self.argument(end)
                    if arg and arg["form"] == "braced":
                        env = self.clean[arg["body_start"]:arg["body_end"]]
                        if env in MATH_ENVS:
                            if name == "begin":
                                environments.append(env)
                            elif env in environments:
                                environments.remove(env)
                        flags[end:arg["end"]] = [active] * (arg["end"] - end)
                        end = arg["end"]
                i = end
            elif self.clean[i] == "$":
                delimiter = "$$" if self.clean.startswith("$$", i) else "$"
                if delimiters and delimiters[-1] == delimiter:
                    delimiters.pop()
                else:
                    delimiters.append(delimiter)
                i += len(delimiter)
            else:
                i += 1
        return flags

    def arrow_ranges(self) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
        options = []
        labels = []
        for item in self.commands:
            if item["name"] not in {"arrow", "ar"}:
                continue
            i = item["end"]
            while i < len(self.clean) and self.clean[i].isspace():
                i += 1
            if i >= len(self.clean) or self.clean[i] != "[":
                continue
            start = i
            depth = 1
            i += 1
            quote_start = None
            while i < len(self.clean) and depth:
                command = self.command_at.get(i)
                if command:
                    i = command["end"]
                    continue
                if self.clean[i] == "{" and i in self.braces:
                    # Grouped labels may themselves contain quote characters.
                    # Scan their contents; brackets inside braces do not close options.
                    closing = self.braces[i]
                    for match in re.finditer('"', self.clean[i + 1:closing]):
                        at = i + 1 + match.start()
                        if quote_start is None:
                            quote_start = at
                        else:
                            labels.append((quote_start + 1, at))
                            quote_start = None
                    i = closing + 1
                    continue
                if self.clean[i] == '"':
                    if quote_start is None:
                        quote_start = i
                    else:
                        labels.append((quote_start + 1, i))
                        quote_start = None
                elif quote_start is None and self.clean[i] == "[":
                    depth += 1
                elif quote_start is None and self.clean[i] == "]":
                    depth -= 1
                i += 1
            options.append((start, i))
        return options, labels

    @staticmethod
    def within(position: int, ranges: list[tuple[int, int]]) -> bool:
        return any(start <= position < end for start, end in ranges)

    def row(self, category: str, start: int, end: int, detail: dict | None = None) -> dict:
        parents = self.ancestors(start)
        state = [item["name"] for item in parents if item["name"] in STATE_COMMANDS]
        return {
            "category": category, "cote": 43, "scan": self.scan,
            "line": self.line(start), "column": self.column(start),
            "end_line": self.line(max(start, end - 1)),
            "source_tex": self.text[start:end],
            "context": self.text[max(0, start - 75):min(len(self.text), end + 75)],
            "state": state,
            "ancestor_macros": [item["name"] for item in parents],
            "math_syntax_context": bool(self.math_flags[start]) if start < len(self.math_flags) else False,
            "detail": detail or {},
        }

    def inventory(self) -> list[dict]:
        rows = []
        for item in self.commands:
            name = item["name"]
            start, end = item["start"], item["end"]
            arg = item.get("argument")
            if name == "unsure" and arg:
                outer = [parent for parent in self.ancestors(start) if parent["name"] == "unsure"]
                if outer:
                    rows.append(self.row("nested_unsure", start, arg["end"], {
                        "depth": len(outer) + 1,
                        "outer_locations": [{"line": self.line(parent["start"]), "source_tex": self.text[parent["start"]:parent["argument"]["end"]]} for parent in outer],
                    }))
            if name in ACCENT_COMMANDS | FONT_COMMANDS and arg and arg["form"] == "control_sequence":
                next_command = self.command_at.get(arg["start"])
                if next_command and next_command["name"] == "unsure":
                    next_arg = next_command.get("argument")
                    through = next_arg["end"] if next_arg else next_command["end"]
                    rows.append(self.row("unbraced_format_before_unsure", start, through, {
                        "format_command": name,
                        "note": "No explicit braces enclose the following unsure macro. This is a location for compiler/visual review, not an automatic edit.",
                    }))
            if name in FONT_COMMANDS and arg:
                rows.append(self.row("alphabet_macro", start, arg["end"], {
                    "command": name, "argument_form": arg["form"],
                    "argument_tex": self.text[arg["body_start"]:arg["body_end"]],
                }))
            if name in COEFFICIENTS:
                rows.append(self.row("coefficient", start, end, {"form": "control_sequence", "letter": name}))
            if name == "prime":
                rows.append(self.row("prime_candidate", start, end, {"form": "prime_command"}))

        for position, character in enumerate(self.clean):
            if position in self.command_positions:
                continue
            if character == "^":
                arg = self.argument(position + 1)
                if not arg:
                    continue
                through = arg["end"]
                nested = self.command_at.get(arg["start"])
                if nested and nested.get("argument"):
                    through = nested["argument"]["end"]
                exponent = self.clean[arg["start"]:through]
                forms = []
                if re.search(r"(?<!\\)!", exponent):
                    forms.append("literal_exclamation")
                if r"\!" in exponent:
                    forms.append("backslash_exclamation_spacing_command")
                if r"\prime" in exponent:
                    forms.append("prime_command")
                if "'" in exponent:
                    forms.append("apostrophe")
                if any(mark in exponent for mark in "′″‴"):
                    forms.append("unicode_prime")
                if forms:
                    rows.append(self.row("superscript_mark", position, through, {"forms": forms, "exponent_tex": self.text[arg["start"]:through]}))
            if character == "N":
                previous = self.clean[position - 1] if position else ""
                following = self.clean[position + 1] if position + 1 < len(self.clean) else ""
                parents = self.ancestors(position)
                families = [item["name"] for item in parents if item["name"] in FONT_COMMANDS | {"operatorname", "mathop"}]
                text_parents = [item["name"] for item in parents if item["name"] in TEXT_COMMANDS]
                adjacent_letters = previous.isalpha() or following.isalpha()
                if adjacent_letters and not families and not (self.math_flags[position] and not text_parents):
                    continue
                rows.append(self.row("capital_N", position, position + 1, {"family": families[-1] if families else "plain_N", "text_wrapper": text_parents, "form": "ASCII_N", "adjacent_letters": adjacent_letters}))
            elif character in UNICODE_N:
                rows.append(self.row("capital_N", position, position + 1, {"family": "literal_unicode", "form": UNICODE_N[character]}))
            if character in UNICODE_COEFFICIENTS:
                rows.append(self.row("coefficient", position, position + 1, {"form": "literal_unicode", "letter": UNICODE_COEFFICIENTS[character]}))

        for match in re.finditer(r"`+|'+|[\"“”„‟«»‘’′″‴]", self.clean):
            start, end = match.span()
            if start in self.command_positions:
                continue
            mark = match.group(0)
            option = self.within(start, self.arrow_options)
            label = self.within(start, self.arrow_labels)
            if mark == '"':
                form = "raw_ASCII_double_quote"
            elif mark == "``":
                form = "TeX_open_double_quote"
            elif mark == "''" and start in self.paired_close_quotes:
                form = "TeX_close_double_quote_paired_on_page"
            elif mark.startswith("'"):
                form = "apostrophe_run"
            elif mark.startswith("`"):
                form = "backtick_run"
            else:
                form = {"“": "U+201C_left_double", "”": "U+201D_right_double", "„": "U+201E_low_double", "‟": "U+201F_reversed_double", "«": "left_guillemet", "»": "right_guillemet", "‘": "U+2018_left_single", "’": "U+2019_right_single", "′": "U+2032_prime", "″": "U+2033_double_prime", "‴": "U+2034_triple_prime"}[mark]
            rows.append(self.row("quote_form", start, end, {"form": form, "in_arrow_options": option, "inside_arrow_label": label}))
            parents = self.ancestors(start)
            prose_wrapper = any(item["name"] in TEXT_COMMANDS for item in parents)
            apostrophe = mark.startswith("'") and start not in self.paired_close_quotes
            unicode_prime = mark in "′″‴"
            if (apostrophe or unicode_prime) and self.math_flags[start] and not prose_wrapper and not (option and not label):
                rows.append(self.row("prime_candidate", start, end, {"form": "apostrophe_shorthand" if apostrophe else "unicode_prime", "run_length": len(mark), "inside_arrow_label": label}))
        return sorted(rows, key=lambda item: (item["scan"], item["line"], item["column"], item["category"]))


def compact(value: str, limit: int = 220) -> str:
    shown = value.replace("\n", r"\n").replace("\r", r"\r")
    return shown if len(shown) <= limit else shown[:limit] + " [excerpt continues in CSV/JSON]"


def summary(report: dict) -> str:
    rows = report["rows"]
    result = [
        "Text-only notation and markup inventory", "=======================================",
        "Captured at: " + report["captured_at_utc"],
        f"Page files: {len(report['files'])}; extracted occurrence rows: {len(rows)}.",
        "",
        "All excerpts are literal saved TeX. No readings are selected and no page",
        "files are edited. Comments and inline verbatim are masked for extraction.",
        "The math-syntax flag follows explicit delimiters and mathematical",
        "environments, including tikzcd/array. It is a lexical aid, not a TeX",
        "execution trace. Text wrappers and editorial-state ancestors are recorded.",
        "Counts include occurrences inside alternatives and deleted text; their",
        "state fields allow those occurrences to be distinguished explicitly.",
        "All occurrences, full extracted arguments, and contexts are in CSV/JSON.",
        "",
        "Counts by category", "------------------",
    ]
    result += [f"{key}: {value}" for key, value in sorted(Counter(row["category"] for row in rows).items())]
    for category in ("nested_unsure", "unbraced_format_before_unsure", "superscript_mark"):
        matches = [row for row in rows if row["category"] == category]
        result += ["", category, "-" * len(category)]
        if not matches:
            result.append("No occurrences in this snapshot.")
        for row in matches:
            result.append(f"43 scan {row['scan']:03d}, line {row['line']}, column {row['column']}: {compact(row['source_tex'])}")
            result.append("  " + compact(json.dumps(row["detail"], ensure_ascii=False), 600))
    result += ["", "Capital N forms", "---------------"]
    groups = defaultdict(list)
    for row in rows:
        if row["category"] == "capital_N":
            group = row["detail"]["family"]
            if row["detail"].get("text_wrapper"):
                group += " / inside " + ",".join(row["detail"]["text_wrapper"])
            elif not row["math_syntax_context"]:
                group += " / outside marked math"
            groups[group].append(row)
    for group, items in sorted(groups.items()):
        result.append(f"{group}: {len(items)} occurrence(s); scans " + ", ".join(f"{scan:03d}" for scan in sorted({r['scan'] for r in items})))
    for row in rows:
        if row["category"] == "capital_N":
            result.append(f"  scan {row['scan']:03d}, line {row['line']}: {row['detail']['family']}; {compact(row['context'], 240)}")
    result += ["", "Sigma / gamma / tau command and Unicode occurrences", "---------------------------------------------------"]
    groups = defaultdict(list)
    for row in rows:
        if row["category"] == "coefficient":
            groups[(row["detail"]["letter"], row["detail"]["form"])].append(row)
    for (letter, form), items in sorted(groups.items()):
        uncertain = sum("unsure" in row["state"] for row in items)
        deleted = sum("deleted" in row["state"] for row in items)
        result.append(f"{letter} ({form}): {len(items)}; inside unsure {uncertain}; inside deleted {deleted}; scans " + ", ".join(f"{scan:03d}" for scan in sorted({r['scan'] for r in items})))
    result += ["", "Quote forms", "-----------"]
    groups = defaultdict(list)
    for row in rows:
        if row["category"] == "quote_form":
            group = row["detail"]["form"] + (" / arrow options" if row["detail"]["in_arrow_options"] else " / elsewhere")
            groups[group].append(row)
    for group, items in sorted(groups.items()):
        result.append(f"{group}: {len(items)}; scans " + ", ".join(f"{scan:03d}" for scan in sorted({r['scan'] for r in items})))
    result += ["", "Alphabet macro counts", "---------------------"]
    counts = Counter(row["detail"]["command"] for row in rows if row["category"] == "alphabet_macro")
    result += [f"\\{name}: {count}" for name, count in sorted(counts.items())]
    result += ["", "Prime candidates", "----------------"]
    primes = [row for row in rows if row["category"] == "prime_candidate"]
    result.append(f"{len(primes)} literal candidates; each is located in the CSV/JSON.")
    for form, count in sorted(Counter(row["detail"]["form"] for row in primes).items()):
        result.append(f"{form}: {count}")
    return "\n".join(result) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--out-prefix", type=Path, required=True, help="New report prefix, without extension; writes .json, .csv, and .txt.")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    files = [(scan, root / "pages" / f"{PREFIX}_43_scan{scan:03d}.tex") for scan in SCANS]
    for attempt in range(1, 9):
        before = {scan: (path.stat().st_mtime_ns, path.stat().st_size) for scan, path in files}
        contents = {scan: path.read_bytes() for scan, path in files}
        after = {scan: (path.stat().st_mtime_ns, path.stat().st_size) for scan, path in files}
        if before == after:
            break
    else:
        raise RuntimeError("Page files kept changing during snapshot capture.")
    report = {
        "captured_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "root": str(root), "snapshot_attempt": attempt,
        "method": "Literal TeX token/brace and delimiter inventory; no handwriting or context inspection and no page edits.",
        "files": {f"pages/{path.name}": {"bytes": len(contents[scan]), "sha256": hashlib.sha256(contents[scan]).hexdigest()} for scan, path in files},
        "rows": [],
    }
    for scan in SCANS:
        report["rows"].extend(Page(scan, contents[scan]).inventory())
    report["counts"] = dict(sorted(Counter(row["category"] for row in report["rows"]).items()))
    prefix = args.out_prefix.resolve()
    prefix.parent.mkdir(parents=True, exist_ok=True)
    destinations = {suffix: Path(str(prefix) + suffix) for suffix in (".json", ".csv", ".txt")}
    if any(path.exists() for path in destinations.values()):
        raise FileExistsError("A report with this prefix already exists; choose a new prefix.")
    destinations[".json"].write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    fields = ["category", "cote", "scan", "line", "column", "end_line", "source_tex", "context", "state", "ancestor_macros", "math_syntax_context", "detail"]
    with destinations[".csv"].open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for row in report["rows"]:
            serialized = dict(row)
            for key in ("state", "ancestor_macros", "detail"):
                serialized[key] = json.dumps(row[key], ensure_ascii=False)
            writer.writerow(serialized)
    readable = summary(report)
    destinations[".txt"].write_text(readable, encoding="utf-8")
    print(readable)
    print(json.dumps({"files": [str(path) for path in destinations.values()]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
