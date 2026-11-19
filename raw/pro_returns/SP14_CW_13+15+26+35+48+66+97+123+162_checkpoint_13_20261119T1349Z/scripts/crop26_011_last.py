import sys
sys.path.insert(0,'out/scripts');from work import crop,ROOT,OUT
from PIL import Image
crop(26,11,'eend2',(1365,844,1664,920),8)
for label,box,deg in [('fibre2',(132,1070,254,1156),-24),('rediger2',(208,1081,362,1192),-24),('nmfull',(24,1020,384,1232),-24)]:
 p=crop(26,11,label,box,8);o=ROOT/'work/crops'/f'H26-01_26_scan011_{label}_upright.png';Image.open(p).rotate(deg,expand=True,fillcolor='white').save(o)
 with (OUT/'crop_manifest.tsv').open('a') as f:f.write(f'{o.name}\t{p}\twhole crop\t1\t{deg}\n')
