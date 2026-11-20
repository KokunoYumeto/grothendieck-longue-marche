from pathlib import Path
from PIL import Image
import csv,json,sys
ROOT=Path('/workspace/scratch/615b60ecbb6e')
OUT=ROOT/'SP73_C13_142+143_work'
SRC=ROOT/'source'
page=sys.argv[1]
cote,scan=page.split('_scan')
p=SRC/'SP73_C13_142+143_scans'/f'{page}.jpg'
im=Image.open(p); w,h=im.size
if h>=w:
    boxes={'top':(0,0,w,round(h*.55)),'bottom':(0,round(h*.45),w,h)}
else:
    boxes={'left':(0,0,round(w*.55),h),'right':(round(w*.45),0,w,h)}
for label,box in boxes.items():
    dst=ROOT/'halves'/f'{page}_{label}.png'
    if not dst.exists(): im.crop(box).save(dst)
marks=list(csv.DictReader((SRC/'SP73_C13_142+143_texts/MARKS.tsv').open(),delimiter='\t'))
marks=[m for m in marks if m['cote']==cote and int(m['scan'])==int(scan)]
packet=OUT/'state'/f'{page}_packet.json'
packet.write_text(json.dumps({'page':page,'cote':cote,'scan':int(scan),'image':str(p),'image_size':[w,h], 'halves':{k:{'path':str(ROOT/'halves'/f'{page}_{k}.png'),'box':v} for k,v in boxes.items()},'witness_c':str(SRC/'SP73_C13_142+143_texts/pages'/f'{page}.tex'),'witness_h':str(SRC/'SP73_C13_142+143_texts/hua'/f'hua_{page}.tex') if (SRC/'SP73_C13_142+143_texts/hua'/f'hua_{page}.tex').exists() else None,'marks':marks,'notation':(OUT/'state/notation.md').read_text()},ensure_ascii=False,indent=2))
print(packet)
