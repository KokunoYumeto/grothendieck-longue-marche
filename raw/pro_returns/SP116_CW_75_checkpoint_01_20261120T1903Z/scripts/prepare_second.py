"""Freeze blind-reading box lists and first readings after all first-pass pages exist.
No recognition. Duplicate coordinate boxes are combined and the fullest recorded
reading is retained; kinds are made neutral so they do not disclose readings.
"""
from pathlib import Path
import csv,json,hashlib
w=Path(__file__).resolve().parents[1]
records=[json.loads((w/'records'/f'scan{n:03}.json').read_text()) for n in range(2,16)]
assert all((w/'pages'/f"{'J75-01' if n<=9 else 'J75-02'}_75_scan{n:03}.tex").exists() for n in range(2,16))
out=w/'second';out.mkdir(exist_ok=True)
packets=w.parent/'audit_packets';packets.mkdir(exist_ok=True)
report=[]
for n,r in zip(range(2,16),records):
 base=f"{'J75-01' if n<=9 else 'J75-02'}_75_scan{n:03}"
 bycoords={}
 for b in r['second_boxes']:
  key=tuple(b[k] for k in ['x0','y0','x1','y1'])
  if key in bycoords:
   old=bycoords[key]
   old['kind']+='; '+b['kind']
   if len(b['reading'])>len(old['reading']):old['reading']=b['reading']
  else:bycoords[key]=dict(b)
 boxes=list(bycoords.values())
 for b in boxes:
  k=b['kind'].lower();terms=[]
  for term,needle in [('insertion','insert'),('margin note','margin'),('deletion','delet'),('formula','formula'),('diagram','diagram'),('drawing','drawing'),('number','number')]:
   if needle in k:terms.append(term)
  if 'numeral' in k or 'exponent' in k or 'superscript' in k:
   if 'number' not in terms:terms.append('number')
  b['kind']='; '.join(terms) if terms else 'text or symbol'
 bp=out/f'{base}_boxes.tsv';fp=out/f'{base}_first.tsv'
 if bp.exists() or fp.exists():raise RuntimeError('Refusing to overwrite frozen first-reading inputs')
 for p,fields in [(bp,['box','kind','x0','y0','x1','y1']),(fp,['box','reading'])]:
  with p.open('w',newline='') as f:
   wr=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');wr.writeheader();wr.writerows(boxes)
 packet=packets/f'scan{n:03}';packet.mkdir(exist_ok=True)
 (packet/'boxes.tsv').write_bytes(bp.read_bytes())
 meta=json.loads((w.parent/'packets'/f'scan{n:03}'/'meta.json').read_text())
 (packet/'images.json').write_text(json.dumps({'scan':n,'base':base,'images':meta['images'],'dimensions':meta['dimensions']},indent=2))
 report.append({'scan':n,'original_boxes':len(r['second_boxes']),'boxes':len(boxes),'first_sha256':hashlib.sha256(fp.read_bytes()).hexdigest(),'boxes_sha256':hashlib.sha256(bp.read_bytes()).hexdigest()})
(w/'records/second_inputs_frozen.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report))
