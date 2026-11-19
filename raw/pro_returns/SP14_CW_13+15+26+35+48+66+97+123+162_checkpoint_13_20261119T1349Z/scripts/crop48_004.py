import sys
sys.path.insert(0,'out/scripts');from work import crop
from PIL import Image
C=[('folio',(1459,65,1547,125),12),('top',(378,96,1133,202),5),('topmargin',(128,115,323,287),8),('oldtop',(917,110,1007,204),16),('lim1',(610,196,1031,286),7),('star',(399,381,1322,486),6),('starleft',(551,376,714,483),12),('starmargin',(138,380,330,479),10),('cancelmargin',(200,579,248,648),15),('limits2',(500,576,1208,674),6),('oldafterx',(787,580,827,652),18),('hom1',(450,748,1368,829),6),('local',(403,817,1559,915),5),('marginwave',(179,827,272,909),12),('hom2',(570,915,1346,998),7),('star2',(399,1083,1413,1178),6),('compare',(399,1218,1597,1340),4),('verif',(473,1284,698,1338),12),('laissee',(1034,1281,1165,1340),14),('bmargin',(35,1344,392,1494),7),('bhead',(435,1377,1408,1430),5),('s791',(398,1470,1554,1529),5),('s791b',(398,1532,1494,1599),5),('s791c',(398,1605,1518,1667),5),('s791d',(398,1660,1456,1723),5),('tout',(1374,1534,1493,1593),12),('phiold',(692,1603,736,1676),18),('connexe',(967,1666,1077,1723),14),('bottomdisplay',(538,1718,1237,1808),7),('lastprose',(398,1806,1627,1874),5),('consider',(1528,1813,1628,1873),14),('lastline',(398,1871,1507,2003),6),('catold',(602,1861,680,2006),14),('bottommargin',(116,1531,327,1992),7)]
for lab,box,sc in C:crop(48,4,lab,box,sc)
for name,deg in [('bmargin',-17),('local',-14)]:
 p='work/crops/H48-01_48_scan004_'+name+'.png'
 Image.open(p).rotate(deg,expand=True,fillcolor='white').save(p.replace('.png','_upright.png'))
 with open('out/crop_manifest.tsv','a') as f:f.write('H48-01_48_scan004_'+name+'_upright.png\t'+p+'\tfull\t1\t'+str(deg)+'\n')
