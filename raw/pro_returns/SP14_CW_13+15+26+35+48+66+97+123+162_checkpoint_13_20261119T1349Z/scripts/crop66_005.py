import sys
sys.path.insert(0,'out/scripts')
from work import crop,ROOT,OUT,row,name
from PIL import Image
specs=[('topmarks',(18,40,228,234),6),('circle25',(213,96,322,187),13),('line1',(401,108,1640,188),5),('equiv1',(1226,127,1393,190),18),('line2',(318,183,1672,279),5),('pb',(970,182,1348,275),13),('alb',(550,282,887,348),13),('line3',(317,280,1669,355),5),('line4',(322,357,1659,445),5),('equivalent',(324,361,595,444),13),('equivalence',(1217,357,1640,438),12),('line5',(313,444,1644,539),5),('bracket',(277,268,330,530),12),('twentysix',(398,548,1682,628),5),('relative',(952,549,1162,625),16),('twentyseven',(407,632,1682,720),5),('adeles',(408,639,554,714),17),('dim',(940,635,1059,711),17),('locales',(341,738,554,806),15),('twentyeight1',(425,785,1671,890),5),('twentyeight2',(314,879,1667,1004),5),('preschemas',(317,917,554,1004),13),('z',(1033,884,1113,945),20),('end',(320,1015,589,1087),14)]
for n,b,s in specs:crop(66,5,n,b,s)
p=crop(66,5,'margin',(33,285,291,470),9)
im=Image.open(p).rotate(-39,expand=True,fillcolor='white')
target=ROOT/'work/crops'/f'{name(row(66,5))}_margin_upright.png'
im.save(target)
with (OUT/'crop_manifest.tsv').open('a') as f:f.write(f'{target.name}\t{p}\trotation\t9\t-39\n')
print(target)
