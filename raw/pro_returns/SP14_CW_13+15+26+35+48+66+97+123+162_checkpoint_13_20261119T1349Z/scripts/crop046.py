import sys
from PIL import Image,ImageEnhance,ImageOps
sys.path.insert(0,'out/scripts');from work import crop,OUT
for label,box,scale,angle in [('heading',(130,50,1380,187),2,0),('opening',(50,222,1630,545),1.7,0),('diagram',(475,535,1655,785),2,0),('first',(140,795,1610,1185),1.8,0),('filtration',(188,1180,1600,1550),1.8,0),('last',(195,1540,1650,2025),1.8,0),('margin1',(18,695,282,927),2.5,-39),('marginQ',(18,1068,190,1715),2.5,-53),('margin2',(24,1807,205,2010),3,-57),('heading_mark',(133,70,174,118),5,0),('geom',(1048,264,1185,324),4,0),('point',(1230,257,1297,346),4,0),('regardera',(166,522,385,580),4,0),('gloss',(540,425,873,487),3,0),('diagram_label',(994,538,1105,600),4,0),('y',(946,831,983,883),5,0),('old_fonct',(1148,800,1384,881),4,0),('A',(1403,798,1445,854),5,0),('complexifie',(621,1350,898,1421),3,0),('bigraduation',(1250,1453,1510,1527),3,0),('last_B',(1030,1940,1138,2010),5,0),('last_Q',(1196,1958,1273,2011),5,0),('last_Hdg',(1420,1970,1481,2016),5,0)]:
 p=crop(13,46,label,box,scale)
 if angle:
  Image.open(p).rotate(angle,expand=True,fillcolor='white').save(p)
  with (OUT/'crop_manifest.tsv').open('a') as f:f.write(p.split('/')[-1]+'\trotation after crop\t'+str(box)+'\t'+str(scale)+'\t'+str(angle)+'\n')
