import sys
sys.path.insert(0,'out/scripts');from work import crop,ROOT,OUT
from PIL import Image,ImageEnhance
for label,box,scale in [('heading',(1145,25,1585,158),4),('quot',(119,57,1139,154),4),('hilb',(124,166,1545,273),4),('div',(124,253,1088,380),5),('hom',(126,398,1384,492),4),('isom',(125,508,1109,608),5),('aut',(132,625,1036,723),5),('imm',(130,740,1217,842),4),('prod',(117,846,1457,1056),4),('gammas',(42,1054,544,1145),6),('prepic',(143,1091,1677,1291),4),('prepicprime',(121,1305,1634,1463),4),('pic',(174,1472,1668,1596),4),('contraL',(239,1579,455,1646),8),('contraR',(958,1585,1136,1651),8),('homprod',(125,1630,1506,1735),4),('Vprod',(126,1754,704,1878),5),('boxV',(1075,1730,1678,1985),4),('oldhom',(189,1811,1402,1982),4),('bottomleft',(195,1990,1087,2145),4),('bottomright',(1127,1990,1678,2146),5),('watermark',(710,22,940,2142),2)]:crop(26,9,label,box,scale)
p=ROOT/'work/crops/H26-01_26_scan009_watermark.png'
im=ImageEnhance.Contrast(Image.open(p).rotate(90,expand=True)).enhance(3)
o=p.with_name('H26-01_26_scan009_watermark_upright.png');im.save(o)
with (OUT/'crop_manifest.tsv').open('a') as f:f.write(f'{o.name}\t{p}\twhole generated crop\t1\t90;contrast=3\n')

for label,box,scale in [('isom_tight',(560,511,665,571),12),('gamma1',(103,1060,212,1126),10),('gamma2',(277,1057,394,1121),10),('prodoldindex',(155,945,207,997),12),('divold',(188,278,246,357),12)]:crop(26,9,label,box,scale)
