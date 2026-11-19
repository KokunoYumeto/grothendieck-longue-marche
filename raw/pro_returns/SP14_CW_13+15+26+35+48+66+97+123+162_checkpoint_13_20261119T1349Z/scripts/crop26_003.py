import sys
sys.path.insert(0,'out/scripts');from work import crop
for label,box,scale in [('A',(198,124,1330,234),3),('one_two',(163,276,1615,516),3),('three_five',(167,483,1653,749),3),('six',(171,757,1429,886),4),('B',(178,888,1535,1101),3),('old',(177,1090,1509,1274),3),('seven',(178,1290,1267,1394),3),('nine_ten',(178,1366,1647,1684),3),('eleven',(159,1613,1610,1834),3),('last',(160,1821,1655,2130),3),('twoold',(343,393,1597,444),4),('oldsch',(1218,464,1427,522),6),('appl4',(909,559,1655,675),5),('note5',(1241,658,1617,759),6),('dedes6',(601,761,689,816),8),('evt',(424,815,507,876),8),('oldmorph',(780,847,1001,885),8),('diverses',(744,1091,984,1136),7),('old7',(179,1139,263,1269),7),('rep7',(365,1297,848,1386),5),('tang',(1008,1360,1648,1467),5),('note10',(1287,1532,1656,1647),6),('margin11',(392,1604,898,1753),5),('prod',(1348,1667,1608,1787),6),('num11',(158,1701,371,1842),6),('num8',(156,1834,271,1954),6),('last12',(355,1870,1586,2021),5),('last13',(354,2023,1655,2134),5)]:crop(26,3,label,box,scale)
from PIL import Image
from work import ROOT,OUT
for base,ang in [('margin11',-10),('note10',-3),('last13',-1.2)]:
 p=ROOT/'work/crops'/f'H26-01_26_scan003_{base}.png';o=p.with_name(p.stem+'_upright.png');Image.open(p).rotate(ang,expand=True,fillcolor='white').save(o)
 with (OUT/'crop_manifest.tsv').open('a') as f:f.write(f'{o.name}\t{p}\twhole generated crop\t1\t{ang}\n')

# Additional decision crops inspected before the page commit.
for label,box,scale in [('oldheadingnum',(170,1020,282,1108),7),('margin11full',(385,1600,915,1800),5),('schemasend',(755,753,925,819),7),('gen5',(1465,680,1625,759),7),('elementaires',(725,1663,1287,1814),5),('old7line',(177,1128,1509,1284),4),('article10',(975,1490,1134,1566),7),('article11',(1089,1655,1314,1750),7),('last13tail',(1014,2047,1656,2141),6),('ths',(920,2020,1070,2082),8),('last12end',(1430,1870,1622,1970),7),('oldarticle',(651,1100,871,1210),7),('tenarticlewide',(800,1448,1310,1534),5),('tenarticle',(813,1515,945,1609),7)]:crop(26,3,label,box,scale)
p=ROOT/'work/crops/H26-01_26_scan003_margin11full.png';o=p.with_name(p.stem+'_upright.png');Image.open(p).rotate(-10,expand=True,fillcolor='white').save(o)
with (OUT/'crop_manifest.tsv').open('a') as f:f.write(f'{o.name}\t{p}\twhole generated crop\t1\t-10\n')
