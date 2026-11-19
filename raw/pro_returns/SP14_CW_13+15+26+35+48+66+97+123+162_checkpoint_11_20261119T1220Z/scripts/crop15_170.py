import sys
sys.path.insert(0,'out/scripts');from work import crop
for label,box,scale in [('title',(419,15,1556,156),3),('examiner',(235,123,707,217),4),('zero',(129,203,1607,293),3),('one',(14,270,1620,399),3),('two',(121,381,1170,470),3),('three',(15,488,1643,614),3),('four',(76,619,1650,996),3),('five_nine',(36,987,1456,1399),3),('margin',(633,1554,1532,1891),3),('fibres',(642,19,809,113),7),('title_end',(1342,19,1552,106),7),('associees',(506,218,719,273),7),('definie',(873,284,1069,343),7),('places',(1341,275,1624,373),6),('Pb',(1371,494,1440,572),8),('motivique',(1440,511,1643,586),7),('parties',(562,574,699,614),9),('val',(792,555,874,602),9),('coh',(572,822,670,882),8),('trans',(1136,776,1292,826),8),('pr',(1302,775,1400,828),8),('reseau',(1400,822,1540,871),8),('mes',(662,1008,761,1057),9),('autres',(782,1006,931,1048),8),('anciens',(1019,985,1299,1046),7),('structures',(603,1145,812,1206),8),('seven',(149,1211,219,1315),8),('RR',(1035,554,1091,614),9),('ZZ',(1177,1174,1268,1245),9),('Riemann_q',(990,1281,1089,1352),9),('eclatements',(890,1734,1122,1795),8)]:crop(15,170,label,box,scale)
for label,box,scale in [('one_du',(516,285,623,334),8),('one_groupe',(646,281,836,345),7),('four_des',(443,638,559,687),8),('four_gps',(582,629,748,701),8),('four_fond',(761,615,1051,702),7),('fonction',(281,1049,535,1130),7),('insert4',(388,987,552,1066),8),('conditions_de',(979,253,1038,294),9),('dans1',(428,830,517,878),8),('dans2',(447,941,553,991),8),('margin_ou',(1161,1721,1486,1802),6)]:crop(15,170,label,box,scale)
from PIL import Image
from pathlib import Path
from work import OUT,ROOT
for base,angle in [('margin',-2.3),('zero',-1.2)]:
 p=ROOT/'work/crops'/f'B15-01_15_scan170_{base}.png';o=p.with_name(p.stem+'_upright.png');Image.open(p).rotate(angle,expand=True,fillcolor='white').save(o)
 with (OUT/'crop_manifest.tsv').open('a') as f:f.write(f'{o.name}\t{p}\twhole generated crop\t1\t{angle}\n')
for label,box,scale in [('trans_full',(1128,767,1318,827),8),('other_places',(1400,770,1655,829),6),('groupe_underline',(465,337,693,402),7),('title_underline',(438,26,647,104),7),('OK1',(20,308,71,369),8),('OK3',(22,524,73,577),8),('OK7',(42,1155,96,1210),8),('star4',(87,651,121,687),10)]:crop(15,170,label,box,scale)

for base,angle in [('OK1',-25),('OK3',-12),('OK7',-18)]:
 p=ROOT/'work/crops'/f'B15-01_15_scan170_{base}.png';o=p.with_name(p.stem+'_upright.png');Image.open(p).rotate(angle,expand=True,fillcolor='white').save(o)
 with (OUT/'crop_manifest.tsv').open('a') as f:f.write(f'{o.name}\t{p}\twhole generated crop\t1\t{angle}\n')
