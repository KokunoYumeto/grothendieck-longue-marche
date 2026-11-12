"""List the API's reported differences on the pilot pages that match none of the check's items (the 'new' findings)."""
import csv, re, sys, pathlib
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import pilot_eval as E
BASE = pathlib.Path(__file__).resolve().parent.parent
out = []
for f in ("pursuing_stacks", "esquisse"):
    for r in csv.DictReader(open(BASE / f / "DIFFERENCES.tsv", encoding="utf-8"), delimiter="\t"):
        line = E.norm(" ".join([r["draft"], r["page"], r["note"]]))
        items = [x for x in E.I if x["key"] == r["key"] and x["diff"]]
        if not any(re.search(x["diff"], line, re.I) for x in items if x["diff"] not in (r"\bthe\b", r"\bone\b", r"Hot", r"\bwhere\b", r"\bmany\b")):
            out.append(r)
w = csv.DictWriter(open(BASE / "pilot" / "pilot_new_findings.tsv", "w", encoding="utf-8", newline=""), fieldnames=list(out[0]) + ["verdict_on_crop"], delimiter="\t", lineterminator="\n")
w.writeheader()
for r in out:
    w.writerow(r)
from collections import Counter
print(len(out), Counter(r["class"] for r in out))
for i, r in enumerate(out):
    print(i, r["key"][-8:], r["class"], "| D:", r["draft"][:70], "| P:", r["page"][:70], "|", r["note"][:70])
