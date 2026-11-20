"""Add three mandatory handwritten-symbol boxes found by the root coverage review.
Run before blind packets exist; these are selections, not new source readings.
"""
from pathlib import Path
import csv, json, datetime
O=Path(__file__).resolve().parents[1]
adds={
 'H97-01_97_scan019': [('b32','handwritten formula',1368,778,1491,843,r'$Y\handwritten{\cap}U$')],
 'C123-01_123_scan017': [('b30','handwritten formula',572,533,767,606,r'$i:\underline{G}_m\handwritten{\longrightarrow}G$'),('b31','handwritten formula',960,1389,1145,1464,r'$\underline{G}_m\handwritten{\longrightarrow}H/U$')]
}
for page,boxes in adds.items():
 if (O/'second'/f'{page}_second.tsv').exists(): raise SystemExit('Blind reading exists: immutable first readings must not change.')
 p=O/'work'/f'{page}_decided.json';r=json.loads(p.read_text());existing={x['box'] for x in r['boxes']}
 for row in boxes:
  if row[0] in existing: raise SystemExit('Already added: '+page+' '+row[0])
  r['boxes'].append(dict(zip(['box','kind','x0','y0','x1','y1','reading'],row)))
 p.write_text(json.dumps(r,ensure_ascii=False,indent=2))
 for suffix,fields in [('boxes',['box','kind','x0','y0','x1','y1']),('first',['box','reading'])]:
  with (O/'second'/f'{page}_{suffix}.tsv').open('w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(r['boxes'])
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (O/'progress.log').open('a') as f:f.write(f'Pre-blind coverage amendment {now}: explicit whole-formula boxes added for handwritten intersection 97/019 b32 and handwritten arrows 123/017 b30,b31; current page readings copied unchanged. No second reading had begun.\n')
with (O/'work/box_coverage_review.md').open('a') as f:f.write('\n## Handwritten-symbol coverage supplement\n\nA separate content check of all 323 handwritten-wrapper occurrences on the first thirteen pages left sixteen textual candidates. Most were portions of an already covered paragraph or diagram. The root inspected the whole-page images of 97/019 and 123/017 and added three explicit formula boxes: 97/019 b32 (Y intersection U), and 123/017 b30,b31 (the two handwritten arrows with their domains and codomains). The current page readings are unchanged. Boxes are selections for the independent second reading; no duplicate first-stage crop was made.\n')
print('Added 3 boxes before any blind reading.')
