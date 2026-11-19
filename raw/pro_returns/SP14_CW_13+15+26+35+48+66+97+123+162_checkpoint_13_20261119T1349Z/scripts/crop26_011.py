import sys
sys.path.insert(0,'out/scripts');from work import crop,ROOT,OUT
from PIL import Image,ImageEnhance,ImageOps
for label,box,scale in [('heading',(186,88,810,185),5),('a',(229,210,1680,311),4),('b1',(250,347,1255,423),5),('b2',(318,422,1248,501),5),('rightnotes',(1265,347,1650,535),5),('leftrefs',(28,207,279,652),4),('c',(250,511,1551,623),4),('de',(230,698,1680,950),4),('dmath',(1031,712,1286,804),8),('mumford1',(38,671,377,835),5),('f1',(278,915,1670,1024),4),('f2',(478,1021,1637,1115),4),('f3',(675,1127,1290,1274),5),('mumnames',(20,940,388,1266),5),('fbracket',(220,937,278,1226),5),('g',(279,1264,1100,1377),5),('seventeen',(35,1223,276,1325),6),('h',(279,1381,1505,1497),5),('pbmal',(36,1368,221,1517),6),('i1',(300,1580,1630,1669),4),('i2',(494,1660,1659,1768),5),('ileft',(42,1639,353,1822),5),('j',(279,1872,1520,1989),5),('watermark',(681,20,849,2146),2)]:crop(26,11,label,box,scale)
for label,deg in [('mumford1',-17),('mumnames',-29),('pbmal',-24),('ileft',-17)]:
 p=ROOT/f'work/crops/H26-01_26_scan011_{label}.png';o=p.with_name(p.stem+'_upright.png');Image.open(p).rotate(deg,expand=True,fillcolor='white').save(o)
 with (OUT/'crop_manifest.tsv').open('a') as f:f.write(f'{o.name}\t{p}\twhole crop\t1\t{deg}\n')
p=ROOT/'work/crops/H26-01_26_scan011_watermark.png'
for label,im in [('r90',Image.open(p).rotate(90,expand=True)),('r90mirror',ImageOps.mirror(Image.open(p).rotate(90,expand=True)))]:
 o=p.with_name(p.stem+'_'+label+'.png');ImageEnhance.Contrast(im).enhance(2).save(o)
 with (OUT/'crop_manifest.tsv').open('a') as f:f.write(f'{o.name}\t{p}\twhole crop\t1\t90;mirror={label=="r90mirror"};contrast=2\n')
