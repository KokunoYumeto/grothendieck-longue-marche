import sys
sys.path.insert(0,'out/scripts');from work import crop,ROOT,OUT
from PIL import Image,ImageEnhance
for label,box,scale in [('headaccent',(194,89,473,151),10),('aend',(1275,209,1666,303),8),('hilbert',(325,348,638,411),9),('chapold',(87,442,226,540),9),('eend',(1350,803,1638,875),9),('parenth',(1264,930,1670,1023),7),('a_f',(479,1022,566,1110),9),('nec',(862,1184,1073,1256),9),('hgroup',(1249,1396,1499,1484),10),('iold',(495,1668,566,1757),10),('jend',(1425,1903,1537,1967),8)]:crop(26,11,label,box,scale)
for label,box,scale,deg in [('mumtight',(48,691,302,824),7,-17),('names',(32,947,359,1179),7,-24),('fibre',(79,1119,386,1238),8,-24),('rediger',(66,1184,285,1302),8,-24),('chapoldrot',(87,442,226,540),9,-4)]:
 p=crop(26,11,label,box,scale); im=Image.open(p); o=ROOT/'work/crops'/(Image.open(p).filename.split('/')[-1].replace('.png','_upright.png')); im.rotate(deg,expand=True,fillcolor='white').save(o)
 with (OUT/'crop_manifest.tsv').open('a') as f:f.write(f'{o.name}\t{p}\twhole crop\t1\t{deg}\n')
p=ROOT/'work/crops/H26-01_26_scan011_watermark.png';im=Image.open(p).rotate(270,expand=True)
for label,box in [('wmleft',(0,0,1600,336)),('wmright',(2600,0,4252,336)),('wmcentre',(1300,0,2900,336))]:
 o=ROOT/'work/crops'/f'H26-01_26_scan011_{label}.png';ImageEnhance.Contrast(im.crop(box)).enhance(1.3).save(o)
 with (OUT/'crop_manifest.tsv').open('a') as f:f.write(f'{o.name}\t{p}\trotate270 then {box}\t1\t270;contrast1.3\n')
