from pathlib import Path
import json,csv,hashlib,datetime
R=Path(__file__).resolve().parents[1]
manifest=R/'second/INITIAL_FROZEN_SHA256.json'
if manifest.exists():raise SystemExit('Refusing to overwrite frozen initial readings')
records=[]
for n in range(2,10):
 stem=f'H156-01_156-7_scan{n:03d}'
 page=R/'pages'/f'{stem}.tex';jp=R/'review'/f'scan{n:03d}_final.json'
 boxes=R/'second'/f'{stem}_boxes.tsv';first=R/'second'/f'{stem}_first.tsv'
 for p in [page,jp,boxes,first]:
  if not p.exists():raise SystemExit('Missing initial artifact '+str(p))
 with boxes.open(newline='') as f:bs=list(csv.DictReader(f,delimiter='\t'))
 with first.open(newline='') as f:fs=list(csv.DictReader(f,delimiter='\t'))
 assert [b['box'] for b in bs]==[b['box'] for b in fs]
 assert len({b['box'] for b in bs})==len(bs)
 d=json.loads(jp.read_text());old=d.get('second_boxes',[]);extras={b.get('box'):b for b in old}
 d['second_boxes']=[]
 for b,f in zip(bs,fs):
  x=dict(extras.get(b['box'],{}));x.update(b);x['reading']=f['reading']
  for k in ['x0','y0','x1','y1']:x[k]=int(x[k])
  assert x['x0']<x['x1'] and x['y0']<x['y1']
  d['second_boxes'].append(x)
 jp.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
 records.append({'scan':n,'boxes':len(bs),'files':[{'path':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [page,boxes,first]]})
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
manifest.write_text(json.dumps({'frozen_utc':now,'rule':'The first TSVs and neutral box TSVs were complete before any blind assignment; they are immutable. Page hashes record their initial state, not the eventual corrected final state.','pages':records},ensure_ascii=False,indent=2)+'\n')
with (R/'progress.log').open('a') as f:f.write('initial blind packets frozen '+now+': all8 pages; '+str(sum(x['boxes'] for x in records))+' boxes; exact LaTeX first readings; SHA256 manifest in second/INITIAL_FROZEN_SHA256.json\n')
print(now,[(x['scan'],x['boxes']) for x in records])
