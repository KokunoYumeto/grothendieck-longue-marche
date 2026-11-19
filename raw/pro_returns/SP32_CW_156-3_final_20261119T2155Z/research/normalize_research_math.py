"""Repair inline math delimiters in two research drafts only; never touches TeX."""
from pathlib import Path
import re

ROOT = Path(__file__).parent
NAMES = ("reconstruction_context.md", "peer_review.md")

def mathematical(s):
    s = s.strip()
    if "\\" in s or "_" in s or "=" in s or "<" in s or ">" in s or "^" in s:
        return True
    if s in {"prec", "operatorname{Tr}(L)"}:
        return True
    return bool(re.fullmatch(r"[\sA-Za-z0-9'{}\[\](),/+-]+", s)) and all(
        len(w) <= 1 for w in re.findall(r"[A-Za-z]+", s)
    )

def clean(s):
    s = s.strip().rstrip("\\")
    if s == "prec":
        return r"\prec"
    if s.startswith("operatorname{"):
        s = "\\" + s
    if s.startswith("{") and s.endswith(r"\}"):
        s = "\\" + s
    return s

def segment(s):
    out = []
    i = 0
    while i < len(s):
        if s[i] in (chr(96), "$"):
            mark = s[i]
            end = s.find(mark, i + 1)
            if end >= 0:
                out.append(s[i:end + 1])
                i = end + 1
                continue
        if s.startswith(r"\(", i):
            end = s.find(r"\)", i + 2)
            if end >= 0:
                out.append("$" + clean(s[i + 2:end]) + "$")
                i = end + 2
                continue
        if s[i] == "(" and not (i and s[i-1].isalnum()):
            depth = 1
            j = i + 1
            while j < len(s) and depth:
                if s[j] == "(":
                    depth += 1
                elif s[j] == ")":
                    depth -= 1
                j += 1
            if depth == 0:
                inner = s[i + 1:j - 1]
                if mathematical(inner):
                    out.append("$" + clean(inner) + "$")
                else:
                    out.append("(" + segment(inner) + ")")
                i = j
                continue
        out.append(s[i])
        i += 1
    return "".join(out)

for name in NAMES:
    p = ROOT / name
    text = p.read_text()
    lines = []
    display = False
    for ln in text.splitlines(keepends=True):
        if ln.strip() == r"\[":
            display = True
            lines.append(ln)
        elif ln.strip() == r"\]":
            display = False
            lines.append(ln)
        elif display:
            lines.append(ln)
        else:
            lines.append(segment(ln))
    p.write_text("".join(lines))
    print(name, "inline math normalized")
