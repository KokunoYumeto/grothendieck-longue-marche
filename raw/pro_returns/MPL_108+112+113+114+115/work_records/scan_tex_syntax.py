#!/usr/bin/env python3
"""Read-only mechanical checks, without interpreting manuscript text."""
from pathlib import Path
import collections
import importlib.util
import json
import re

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent
spec = importlib.util.spec_from_file_location("packet_validator", BASE / "validate_packet.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)
STATE_MACROS = {"cotefile", "scanpage", "mspage", "deleted", "inserted", "margin",
                "uline", "uuline", "diagram", "figure", "unsure", "illegible"}

def lineno(text, position):
    return text.count("\n", 0, position) + 1

def inspect():
    problems = []
    commands = collections.Counter()
    environments = collections.Counter()
    for path in sorted((ROOT / "pages").glob("*.tex")):
        raw = path.read_text(encoding="utf-8")
        text = validator.strip_tex_comments(raw)
        name = str(path.relative_to(ROOT))
        for issue in validator.brace_errors(raw):
            problems.append({"file": name, "issue": issue})
        for m in re.finditer(r"\\([A-Za-z]+|.)", text):
            command = m.group(1)
            commands[command] += 1
            if command in STATE_MACROS:
                after = text[m.end():].lstrip()
                if not after.startswith("{"):
                    problems.append({"file": name, "line": lineno(text,m.start()),
                                     "issue": f"unbraced argument after \\{command}"})
        stack = []
        for m in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", text):
            action, env = m.groups()
            line = lineno(text,m.start())
            if action == "begin":
                environments[env] += 1
                stack.append((env,line))
            elif not stack:
                problems.append({"file": name, "line": line, "issue": f"unmatched end of {env}"})
            elif stack[-1][0] != env:
                problems.append({"file": name, "line": line,
                                 "issue": f"environment mismatch: closing {env}, open {stack[-1][0]}"})
            else:
                stack.pop()
        for env,line in stack:
            problems.append({"file": name, "line": line, "issue": f"unclosed environment {env}"})
        for m in re.finditer(r"\\(?:arrow|ar)\s*\[([^\]\n]*)\]", text):
            options = m.group(1)
            first = options.split(",",1)[0].strip()
            if re.fullmatch(r"[a-z]+",first) and not re.fullmatch(r"[rlud]+",first):
                if first not in {"phantom", "equal", "dashed", "dotted", "Rightarrow", "Leftrightarrow", "hook", "tail", "mapsto", "twoheads", "squiggly"}:
                    problems.append({"file": name, "line": lineno(text,m.start()),
                                     "issue": f"possible invalid TikZ-cd direction/key: {first}"})
    return {"scope":"Mechanical syntax only; no mathematical or reading assessment.",
            "problems":problems, "commands":dict(sorted(commands.items())),
            "environments":dict(sorted(environments.items()))}

if __name__ == "__main__":
    report = inspect()
    print(json.dumps(report,ensure_ascii=False,indent=2))
