#!/usr/bin/env python3
"""Rebuild expendable native halves and page-only packets from supplied inputs.
No text recognition is performed. Existing halves are never regenerated.
Run after extracting the original attachment ONCE to ../source.
"""
from pathlib import Path
import csv,json,shutil
from PIL import Image
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent;PREFIX='SP74_C13_143+145'
SRC=BASE/'source';TXT=SRC/(PREFIX+'_texts');SCANS=SRC/(PREFIX+'_scans')
HALVES=BASE/'halves';PACKETS=BASE/'reader_packets'
HALVES.mkdir(exist_ok=True);PACKETS.mkdir(exist_ok=True)
marks=list(csv.DictReader((TXT/'MARKS.tsv').open(),delimiter='\t'))
diffs=list(csv.DictReader((SRC/(PREFIX+'_C_H_differences.tsv')).open(),delimiter='\t'))
preamble=(TXT/'PREAMBLE.tex').read_text()
for page in json.loads((ROOT/'page_order.json').read_text()):
 key=page['key'];impath=SCANS/(key+'.jpg');im=Image.open(impath);w,h=im.size
 boxes=[[0,0,w,round(h*.55)],[0,round(h*.45),w,h]] if h>=w else [[0,0,round(w*.55),h],[round(w*.45),0,w,h]]
 halves=[]
 for n,box in enumerate(boxes,1):
  p=HALVES/f'{key}_half{n}.png'
  if not p.exists():im.crop(box).save(p)
  halves.append(str(p))
 hp=TXT/'hua'/f'hua_{key}.tex'
 d=dict(page,image=str(impath),halves=halves,half_boxes=boxes,witness_C=(TXT/'pages'/(key+'.tex')).read_text(),witness_H=hp.read_text() if hp.exists() else None,preamble=preamble,marks=[m for m in marks if m['cote']==page['cote'] and int(m['scan'])==page['scan']],differences=[x for x in diffs if x['page']==key])
 (PACKETS/(key+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2))
for p in (ROOT/'workflow').glob('*.md'):shutil.copyfile(p,PACKETS/p.name)
print('Native halves retained or recreated; 24 page-only packets written.')
