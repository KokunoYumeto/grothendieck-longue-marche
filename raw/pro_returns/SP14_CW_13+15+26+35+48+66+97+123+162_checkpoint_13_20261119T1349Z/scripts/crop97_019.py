import sys,io,contextlib
from PIL import Image
sys.path.insert(0,'out/scripts')
from work import crop,S,row,name,OUT
crops=[
('header',(784,78,1057,121),8),('topinsert',(902,113,1463,155),7),('oldetant',(963,119,1059,151),20),
('Dprime',(1168,149,1208,184),24),('fraction',(304,181,598,242),9),('lineI',(435,215,928,269),7),
('module',(1166,214,1349,265),10),('oldCela',(1344,270,1604,319),10),('oldqu1',(283,343,339,382),22),
('oldque',(633,344,722,383),22),('ouverte',(1299,306,1415,385),12),('mem1',(442,342,596,386),10),
('section',(805,394,1039,457),10),('restriction',(1231,396,1475,458),10),('map',(1211,468,1362,511),10),
('codinsert',(478,502,1120,578),6),('marginall',(27,698,258,1038),5),('bracket',(247,583,304,975),5),
('oldest',(285,663,360,703),20),('oldseul',(615,730,762,770),16),('oldcela2',(1328,725,1583,769),12),
('pour2',(1303,691,1445,763),10),('oldqu2',(284,792,337,830),24),('intersect',(1387,787,1479,833),14),
('idealOU',(729,845,787,912),20),('formOU',(1017,849,1124,907),16),('regulier',(1334,845,1526,901),12),
('Gamma',(288,915,488,966),12),('codim',(1341,1040,1603,1097),12),('dim',(283,1105,530,1165),12),
('xX1',(847,1087,998,1149),12),('refmargin',(120,1078,257,1184),12),('bigcancel',(1036,1086,1509,1148),10),
('artin',(450,1161,1034,1229),6),('oldg',(1431,1166,1467,1223),24),('X1',(499,1225,659,1282),12),
('notin',(482,1287,626,1343),14),('Ozero',(772,1295,962,1362),12),('cyc',(680,1353,1301,1434),6),
('sum',(836,1351,903,1405),20),('Z1dot',(812,1423,916,1473),16),('propold',(746,1476,1147,1559),9),
('Lapp',(1169,1477,1444,1552),10),('Dcyc',(1445,1484,1630,1543),12),('propUL',(287,1548,1309,1612),5),
('eqadd',(289,1670,813,1734),7),('Iprod',(1181,1671,1585,1739),9),('siinsert',(963,1719,1159,1798),12),
('A',(1003,1750,1139,1802),14),('X1low',(814,1730,955,1798),12),('length',(987,1807,1457,1864),7),
('plus',(284,1880,533,1924),10),('oldx',(828,1876,865,1924),26),('tquot',(1197,1874,1623,1925),8),
('oldresulte',(571,1948,764,1987),18),('subset',(1405,2005,1510,2048),16)]
with contextlib.redirect_stdout(io.StringIO()):
 for label,box,scale in crops:crop(97,19,label,box,scale)
r=row(97,19)
for label,box,scale,angle in [('marginupright',(27,698,258,1038),6,-35),('refupright',(120,1078,257,1184),10,-24)]:
 im=Image.open(S/(name(r)+'.jpg')).crop(box)
 im=im.resize((im.width*scale,im.height*scale)).rotate(angle,expand=True,fillcolor='white')
 p='work/crops/'+name(r)+'_'+label+'.png';im.save(p)
 with (OUT/'crop_manifest.tsv').open('a') as f:f.write('\t'.join(map(str,[p.split('/')[-1],S/(name(r)+'.jpg'),','.join(map(str,box)),scale,angle]))+'\n')
print(len(crops),'base crops and two rotations generated')
