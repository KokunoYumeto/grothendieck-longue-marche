"""Align the current unindexed cancellation decision with its completed audit."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];p=R/'records/149_scan053.json';r=json.loads(p.read_text());t=R/'pages/149_scan053.tex';before=hashlib.sha256(t.read_bytes()).hexdigest()
d=next(d for d in r['unindexed_decisions'] if d['place']=='Canceled clause after courbe algébrique')
row=r['rows'][31]
d.update(reading=r'\unsure{que je suppose de|qui je suppose de}',ink=row['scan_shows'],crop=row['crop'],box=row['box'],confidence='low')
for c in r['crops']:
    if c['file']=='crops/149_scan053_p11.jpg':c['reason']='Whole cancelled clause after courbe algébrique and its separate raised replacement; historical first-phase crop, retained unchanged.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
assert before==hashlib.sha256(t.read_bytes()).hexdigest()
with (R/'records/final_metadata_review.md').open('a') as f:f.write('\nReader A checked the final 053 metadata and identified an old unindexed cancellation decision and its crop descriptor. Both now agree with the completed blind audit, retaining the low-confidence que/qui je suppose de prose alternatives. Reader A also confirmed that saved blind B03 and B12 are the exact regions rotated 22 and 90 degrees clockwise, respectively; those images and frozen input tables were not altered.\n')
print('053 unindexed decision reconciled; page TeX unchanged')
