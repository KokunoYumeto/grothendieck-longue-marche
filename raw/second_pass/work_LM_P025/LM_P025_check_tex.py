"""LM_P025: brace balance per scan block and $-parity per line group (comments stripped)."""
import re
import sys

text = open(sys.argv[1], encoding="utf-8").read()
blocks = re.split(r"(?=\\scanpage\{)", text)
for b in blocks:
    if not b.strip():
        continue
    name = re.match(r"\\scanpage\{(\d+)\}", b)
    body = "\n".join(line.split("%")[0] if not line.lstrip().startswith("%") else "" for line in b.splitlines())
    body = body.replace(r"\{", "").replace(r"\}", "").replace(r"\$", "")
    depth = 0
    bad = False
    for ch in body:
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0:
                bad = True
    dollars = body.count("$")
    disp_open, disp_close = body.count(r"\["), body.count(r"\]")
    print(name.group(1) if name else "?", "braces", depth, "neg" if bad else "", "dollars", dollars, "even" if dollars % 2 == 0 else "ODD", "displays", disp_open, disp_close)
