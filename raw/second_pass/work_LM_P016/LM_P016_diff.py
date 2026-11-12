"""LM_P016: sanity checks of the checked transcription against the first pass."""
import difflib
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
A = os.path.join(ROOT, "answers", "unzipped", "LM_P016", "LM_P016_transcription.tex")
B = os.path.join(ROOT, "second_pass", "LM_P016_checked.tex")
BS = chr(92)

a = open(A, encoding="utf-8").read()
b = open(B, encoding="utf-8").read()
for name, t in (("first", a), ("checked", b)):
    depth = 0
    neg = 0
    for ch in t:
        depth += (ch == "{") - (ch == "}")
        if depth < 0:
            neg += 1
    print(name, "brace-depth-end", depth, "negative", neg,
          "math-open", t.count(BS + "("), "math-close", t.count(BS + ")"),
          "unsure", t.count(BS + "unsure{"),
          "scanpages", re.findall(BS * 2 + r"scanpage\{(\d+)\}", t))
d = list(difflib.unified_diff(a.splitlines(), b.splitlines(), lineterm="", n=0))
print("changed hunks", sum(1 for line in d if line.startswith("@@")))
print("residual unsure{E}", b.count(BS + "unsure{E}"), "unsure{T}", b.count(BS + "unsure{T}"))
