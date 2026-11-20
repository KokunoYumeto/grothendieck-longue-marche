from pathlib import Path
from PIL import Image
import csv,sys
root=Path(__file__).resolve().parents[2];n=int(sys.argv[1]);tag=f'{n:03}'
p=root/'source/SP70_C13_142_texts'
for f in [f'pages/142_scan{tag}.tex',f'hua/hua_142_scan{tag}.tex']:
 print('\nFILE '+f+'\n'+(p/f).read_text())
for r in csv.DictReader((p/'MARKS.tsv').open(),delimiter='\t'):
 if int(r['scan'])==n:print(r['id'],r['the mark as written'],r['the LaTeX around it'])
im=Image.open(root/f'source/SP70_C13_142_scans/142_scan{tag}.jpg');w,h=im.size
for name,box in [('top',(0,0,w,round(h*.55))),('bottom',(0,round(h*.45),w,h))]:
 dest=root/f'views/{tag}_{name}.png'
 if not dest.exists():im.crop(box).save(dest)
print('DIMENSIONS',w,h)
