import sys
sys.path.insert(0,'out/scripts');from work import crop
for label,box,scale in [('corollary',(136,275,1628,602),2),('routes',(143,592,1649,931),2),('definition',(146,935,1662,1314),2),('theorem',(153,1317,1659,1680),2),('primitives',(152,1701,1688,2040),2),('header',(717,218,860,268),5),('gamma',(446,640,509,693),7),('gamma_sub',(1042,646,1113,698),7),('def_accent',(150,944,281,996),7),('th_accents',(154,1319,341,1380),6),('number',(156,1705,220,1761),7),('edge',(1575,1952,1694,2014),7),('point',(1564,1077,1672,1126),6),('Alors',(1353,383,1551,441),5)]:crop(15,31,label,box,scale)
crop(15,31,'last_point',(1543,1060,1704,1140),7)
edge=crop(15,31,'edge_full',(1556,1938,1704,2032),8)
from PIL import Image,ImageEnhance
ImageEnhance.Contrast(Image.open(edge).convert('L')).enhance(2.5).save(edge.replace('.png','_contrast.png'))
