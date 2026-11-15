#!/usr/bin/env python3
"""One-time source encoding repairs, preserving manuscript tokens.

Run only before the transcription freeze. No image or context is accessed.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
if "transcription frozen " in (ROOT / "progress.log").read_text():
    raise SystemExit("Frozen transcription: refusing changes.")

protected = {"array", "aligned", "alignedat", "matrix", "pmatrix",
             "bmatrix", "cases", "smallmatrix", "tabular"}

def fix_cd(match):
    block = match.group()
    if "ampersand replacement=" not in block:
        start = r"\begin{tikzcd}"
        if block.startswith(start + "["):
            block = block.replace(start + "[", start + r"[ampersand replacement=\&,", 1)
        else:
            block = block.replace(start, start + r"[ampersand replacement=\&]", 1)
    out, stack, pos = [], [], 0
    for m in re.finditer(r"\\(begin|end)\{([^}]+)\}|(?<!\\)&", block):
        out.append(block[pos:m.start()])
        token = m.group()
        if token == "&":
            out.append("&" if any(x in protected for x in stack) else r"\&")
        else:
            if m.group(1) == "begin":
                stack.append(m.group(2))
            elif stack:
                stack.pop()
            out.append(token)
        pos = m.end()
    out.append(block[pos:])
    return "".join(out)

changed = []
for p in sorted((ROOT / "pages").glob("*.tex")):
    before = p.read_text()
    after = re.sub(r"\\begin\{tikzcd\}[\s\S]*?\\end\{tikzcd\}", fix_cd, before)
    after = after.replace("name=inc,", "every matrix/.append style={name=inc,nodes in empty cells},")
    after = after.replace("name=bs,", "every matrix/.append style={name=bs,nodes in empty cells},")
    after = re.sub(
        r"\\diagram\{(\\begin\{array\}[\s\S]*?\\end\{array\})\}",
        lambda m: r"\diagram{\(" + m.group(1) + r"\)}", after)
    if after != before:
        p.write_text(after)
        changed.append(p.name)
sys.path.insert(0, str(ROOT / "scripts"))
from record_page import rebuild, utc
rebuild()
with (ROOT / "progress.log").open("a") as f:
    f.write("source encoding reviewed: TikZ-CD cell separators, matrix anchors, explicit array math mode " + utc() + "\n")
print("\n".join(changed))
