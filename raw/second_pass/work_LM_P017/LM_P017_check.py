"""LM_P017: brace/bracket balance per scan and a line diff against the first pass."""
import difflib
import re
import sys

BASE = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104"
first = open(BASE + r"\answers\unzipped\LM_P017\LM_P017_transcription.tex", encoding="utf-8").read()
checked = open(BASE + r"\second_pass\LM_P017_checked.tex", encoding="utf-8").read()


def per_scan(text):
    parts = re.split(r"(?=\\scanpage\{)", text)
    return [p for p in parts if p.strip()]


for name, text in (("first", first), ("checked", checked)):
    for p in per_scan(text):
        scan = re.match(r"\\scanpage\{(\d+)\}", p).group(1)
        body = re.sub(r"\\[{}]", "", p)
        b = body.count("{") - body.count("}")
        d = body.count("\\[") - body.count("\\]")
        print(f"{name} scan {scan}: brace balance {b}, display balance {d}")

for k in ("\\deleted{", "\\inserted{", "\\unsure{", "\\illegible{", "\\margin{", "\\diagram{"):
    print(k, "first", first.count(k), "checked", checked.count(k))

words_first = re.findall(r"\w+", first)
words_checked = re.findall(r"\w+", checked)
sm = difflib.SequenceMatcher(a=words_first, b=words_checked, autojunk=False)
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag != "equal":
        print(tag, " ".join(words_first[i1:i2]), "=>", " ".join(words_checked[j1:j2]))
