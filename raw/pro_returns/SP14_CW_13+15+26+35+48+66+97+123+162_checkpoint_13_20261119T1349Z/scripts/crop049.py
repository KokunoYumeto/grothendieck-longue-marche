import sys
from PIL import Image
sys.path.insert(0,'out/scripts');from work import crop,OUT
items=[('top',(241,45,1642,258),2,0),('equiv',(257,263,1656,532),2,0),('stabilizer',(252,511,1658,816),2,0),('proposition',(252,771,1655,1104),2,0),('cancelbottom',(257,1016,1654,1328),2,0),('item5',(239,1336,1654,1777),1.8,0),('last',(278,1755,1654,2134),1.9,0),('margin_prop',(14,850,289,1003),3,0),('margin_NB',(14,1072,216,1275),3,0),('margin_elliptic',(21,1324,281,1474),3,-20),('bar1',(762,267,815,310),6,0),('label',(286,378,344,421),5,0),('T_J',(950,389,1001,460),5,0),('le',(1053,398,1122,443),5,0),('old_decl',(1120,380,1378,432),4,0),('old_gx',(803,472,952,518),4,0),('old_inverse',(988,447,1028,489),6,0),('old_stabG',(1486,493,1544,550),5,0),('old_on',(1152,606,1279,645),4,0),('insert_V',(1509,552,1560,603),6,0),('R_member',(631,681,811,739),5,0),('old_C',(796,674,916,723),5,0),('R_hat',(427,749,467,791),6,0),('old_la',(416,793,464,837),5,0),('old_quelle',(1175,742,1366,782),5,0),('old_R',(986,782,1045,823),5,0),('old_containsR',(864,898,932,977),5,0),('old_ceci',(611,1037,724,1083),5,0),('old_leword',(784,1003,886,1082),5,0),('tt',(1262,1002,1341,1044),5,0),('equal_s',(357,1176,405,1210),6,0),('calM',(548,1622,617,1679),5,0),('disj',(1367,1926,1569,1985),4,0),('modeste',(1042,2002,1269,2043),5,0),('estim',(354,2049,596,2134),4,0)]
for label,box,scale,angle in items:
 p=crop(13,49,label,box,scale)
 if angle:
  Image.open(p).rotate(angle,expand=True,fillcolor='white').save(p)
  with (OUT/'crop_manifest.tsv').open('a') as f:f.write(p.split('/')[-1]+'\trotation after crop\t'+str(box)+'\t'+str(scale)+'\t'+str(angle)+'\n')
