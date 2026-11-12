"""LM_P018 check: brace balance per scan and a line diff of first pass vs checked text."""
import difflib
import re
import sys

base = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104"
a = open(base + r"\answers\unzipped\LM_P018\LM_P018_transcription.tex", encoding="utf-8").read()
b = open(base + r"\second_pass\LM_P018_checked.tex", encoding="utf-8").read()


def balance(t):
    t = t.replace(r"\{", "").replace(r"\}", "")
    d = 0
    for i, ch in enumerate(t):
        if ch == "{":
            d += 1
        elif ch == "}":
            d -= 1
        if d < 0:
            return "negative at %d" % i
    return d


for name, t in (("first", a), ("checked", b)):
    parts = re.split(r"(\\scanpage\{\d+\})", t)
    print(name, "total balance", balance(t), "dollars", t.count("$") % 2)
    for i in range(1, len(parts), 2):
        seg = parts[i + 1]
        bal = balance(seg)
        if bal != 0 or seg.count("$") % 2:
            print("  ", parts[i], "brace", bal, "dollar parity", seg.count("$") % 2)

for line in difflib.unified_diff(a.splitlines(), b.splitlines(), lineterm="", n=0):
    if line.startswith(("+", "-")) and not line.startswith(("+++", "---")):
        sys.stdout.buffer.write((line + "\n").encode("utf-8"))
