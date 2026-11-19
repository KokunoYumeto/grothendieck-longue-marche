import sys
sys.path.insert(0,'out/scripts');from work import crop,ROOT,OUT
from PIL import Image,ImageOps
for label,box in [('wm_initials',(690,70,982,460)),('wm_word1',(690,460,982,1120)),('wm_word2',(690,1120,982,1890))]:
 p=crop(26,9,label,box,2)
 im=Image.open(p).rotate(90,expand=True).convert('L').point(lambda v:max(0,min(255,int((v-190)*255/65))))
 for suf,v in [('r90',im),('r90mirror',ImageOps.mirror(im))]:
  o=ROOT/f'work/crops/H26-01_26_scan009_{label}_{suf}.png';v.save(o)
  with (OUT/'crop_manifest.tsv').open('a') as f:f.write(f'{o.name}\t{p}\twhole crop\t1\t90;gray levels 190-255;mirror={suf=="r90mirror"}\n')
