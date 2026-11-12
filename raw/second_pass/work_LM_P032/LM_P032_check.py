"""LM_P032 helper: brace/dollar balance and word-level diff of two transcriptions."""
import difflib
import re
import sys

BS = chr(92)
a = open(sys.argv[1], encoding="utf-8").read()
b = open(sys.argv[2], encoding="utf-8").read()
for name, t in (("first", a), ("checked", b)):
    t2 = t.replace(BS + "{", "").replace(BS + "}", "")
    print(name, "braces", t2.count("{"), t2.count("}"),
          "dollar-parity", t.count("$") % 2,
          "unsure", t.count(BS + "unsure{"))
ta = re.findall(r"\S+", a)
tb = re.findall(r"\S+", b)
sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
n = 0
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op != "equal":
        n += 1
        print(n, op, "|", " ".join(ta[i1:i2])[:170], "=>", " ".join(tb[j1:j2])[:170])
