import sys
sys.path.insert(0,'out/scripts');from work import crop
from PIL import Image
C=[('chap',(55,57,331,157),7),('title1',(407,67,950,183),5),('oldtitle',(943,46,1484,188),6),('s1',(320,344,1520,482),4),('s2',(330,493,1365,583),5),('s45',(318,744,1662,955),4),('margin',(43,637,203,978),5),('s6',(340,947,1299,1040),7),('b',(126,1029,980,1149),5),('s7',(329,1169,1310,1338),5),('s8',(332,1339,1523,1450),5),('s9',(369,1471,747,1560),8),('s10',(161,1564,1443,1697),5),('cartier',(139,1711,881,1884),6),('c',(150,1862,1561,1994),5),('s12',(213,1983,1337,2084),5)]
for label,box,scale in C:crop(48,3,label,box,scale)
p='work/crops/H48-01_48_scan003_margin.png';im=Image.open(p);im.rotate(-25,expand=True,fillcolor='white').save('work/crops/H48-01_48_scan003_margin_upright.png')
with open('out/crop_manifest.tsv','a') as f:f.write('H48-01_48_scan003_margin_upright.png\tH48-01_48_scan003_margin.png\tfull\t1\t-25\n')
