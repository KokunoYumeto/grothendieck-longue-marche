#!/usr/bin/env python3
"""Count the four cover-led runs and every saved manuscript-number inscription."""
from pathlib import Path
import csv,json,re
root=Path(__file__).resolve().parent.parent
rows=[]
for scan,start,end in [(44,45,55),(56,57,71),(72,73,78),(79,80,81)]:
    members=[n for n in range(start,end+1) if (root/"pages"/f"MPL_72_035-081_72_scan{n:03d}.tex").is_file()]
    assert members==list(range(start,end+1))
    rows.append({"cover_scan":scan,"first_following_scan":start,"last_following_scan":end,"supplied_following_scans":len(members),"source_inscribed_extent":""})
with (root/"research"/"title_scope_counts.csv").open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
numbers=[]
for p in sorted((root/"pages").glob("*.tex")):
    scan=int(re.search(r"scan(\d+)",p.name).group(1))
    values=re.findall(r"\\mspage\{([^}]+)\}",p.read_text())
    numbers.append({"scan":scan,"mspage_occurrences":values})
assert len(numbers)==47
assert all(all(int(v)==r["scan"]-1 for v in r["mspage_occurrences"]) for r in numbers)
result={"page_count":47,"mspage_occurrences":sum(len(r["mspage_occurrences"]) for r in numbers),"cover_runs":rows,"number_occurrences":numbers}
(root/"research"/"title_scope_counts.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({k:result[k] for k in ["page_count","mspage_occurrences"]}))
