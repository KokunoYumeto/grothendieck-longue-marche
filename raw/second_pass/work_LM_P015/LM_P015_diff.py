"""Brace/dollar balance of the first pass and the checked LM_P015 transcription, and a token-level diff between them.
usage: python -I LM_P015_diff.py FIRST.tex CHECKED.tex"""
import difflib
import re
import sys

BS = chr(92)


def balance(s):
    d = 0
    for i, ch in enumerate(s):
        if i and s[i - 1] == BS:
            continue
        if ch == "{":
            d += 1
        elif ch == "}":
            d -= 1
        if d < 0:
            return "negative at %d" % i
    return d


a = open(sys.argv[1], encoding="utf-8").read()
b = open(sys.argv[2], encoding="utf-8").read()
print("brace balance first/checked:", balance(a), balance(b))
print("dollar parity first/checked:", a.count("$") % 2, b.count("$") % 2)
for name in ("deleted", "inserted", "unsure", "margin", "uline", "illegible", "scanpage", "mspage"):
    print(name, a.count(BS + name + "{"), b.count(BS + name + "{"))
ta = re.findall(r"\S+", a)
tb = re.findall(r"\S+", b)
sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
n = 0
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op != "equal":
        n += 1
        print(n, op, "|", " ".join(ta[i1:i2])[:170], "=>", " ".join(tb[j1:j2])[:170])
