"""Print, for each pilot item, the API difference line(s) that matched and the transcription context (for the review by hand)."""
import re, sys, pathlib, csv
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import pilot_eval as E
from parse import results, sections
res = results()
for n, x in enumerate(E.I):
    if not x["key"].startswith(("ps", "esq")):
        continue
    sec = sections(res[x["key"]][0])
    hits = []
    if x["diff"]:
        for line in sec.get("DIFFERENCES", "").splitlines():
            if re.search(x["diff"], E.norm(line), re.I):
                hits.append(line.replace('"class": ', "").replace('"draft": ', "D=").replace('"page": ', "P=")[:150])
    t = E.test_trans(x["trans"], sec.get("TRANSCRIPTION", ""))
    print(f"#{n} {x['key'][-8:]} {x['desc'][:60]} | T={t} | " + (" || ".join(hits[:2]) if hits else "NO DIFF"))
