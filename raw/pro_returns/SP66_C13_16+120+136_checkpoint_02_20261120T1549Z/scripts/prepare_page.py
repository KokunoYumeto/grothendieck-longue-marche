"""Prepare native-resolution overlapping halves and print the supplied witnesses; no OCR."""
from pathlib import Path
import sys,csv
from PIL import Image
root=Path(__file__).resolve().parents[2];key=sys.argv[1]
p=root/'source/SP66_C13_16+120+136_scans'/(key+'.jpg')
im=Image.open(p);w,h=im.size
boxes=[(0,0,w,int(h*.55)),(0,int(h*.45),w,h)] if h>=w else [(0,0,int(w*.55),h),(int(w*.45),0,w,h)]
for label,b in zip(['top','bottom'],boxes):
 out=root/'views'/(key+'_'+label+'.png')
 if out.exists():raise RuntimeError('Half already prepared: '+str(out))
 im.crop(b).save(out)
print('DIMENSIONS',im.size,'HALF BOXES',boxes)
t=root/'source/SP66_C13_16+120+136_texts'
print('WITNESS C\n'+(t/'pages'/(key+'.tex')).read_text())
hp=t/'hua'/('hua_'+key+'.tex')
print('WITNESS H\n'+(hp.read_text() if hp.exists() else '[No witness H for this page]'))
cote,scan=key.split('_scan')
for x in csv.DictReader((t/'MARKS.tsv').open(),delimiter='\t'):
 if x['cote']==cote and int(x['scan'])==int(scan):print(x['id'],x['the mark as written'])
