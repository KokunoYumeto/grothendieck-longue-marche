"""LM_P013_check.py -- sanity checks on the second-pass outputs (braces, scan markers, change counts)."""
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
base = sys.argv[1]
t = open(base + "/LM_P013_checked.tex", encoding="utf-8").read()
print("scanpages", re.findall(r"\\scanpage\{(\d+)\}", t))
print("mspages", re.findall(r"\\mspage\{(\d+)\}", t))
depth = 0
for n, line in enumerate(t.splitlines(), 1):
    s = line.replace(r"\{", "").replace(r"\}", "")
    depth += s.count("{") - s.count("}")
    if depth < 0:
        print("negative depth at line", n)
print("net brace depth", depth)
for env in ["tikzcd", "gathered"]:
    print(env, t.count(r"\begin{" + env + "}"), t.count(r"\end{" + env + "}"))
print("display open/close", t.count(r"\["), t.count(r"\]"))
md = open(base + "/LM_P013_changes.md", encoding="utf-8").read()
table = md.split("**Totals:**")[0]
rows = [l for l in table.splitlines() if re.match(r"\| \d+ \| \d{3}", l)]
conf = Counter(l.rstrip().rstrip("|").split("|")[-1].strip() for l in rows)
print("rows", len(rows), dict(conf))
nums = [int(l.split("|")[1]) for l in rows]
print("numbering ok", nums == list(range(1, len(nums) + 1)))
