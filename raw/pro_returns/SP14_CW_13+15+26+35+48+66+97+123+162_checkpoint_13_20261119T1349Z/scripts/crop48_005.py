import sys
sys.path.insert(0,'out/scripts')
from work import crop
from PIL import Image
C=[('title',(378,80,1654,170),6),('titlefinal',(1371,80,1654,169),12),('dlabel',(183,47,338,189),8),('elabel',(204,252,315,376),9),('extension',(382,244,1618,355),6),('chevalley',(674,337,1109,393),9),('firstdots',(402,187,426,262),12),('seconddashes',(402,358,430,467),12),('torseurs',(328,432,1138,596),7),('thirdlabel',(207,477,319,599),10),('nimporte',(1201,470,1500,539),10),('isotriv',(847,539,1598,638),8),('isotrivend',(1495,546,1598,625),15),('neron',(384,664,965,753),10),('lastlabel',(181,658,314,806),10),('paragraph',(555,824,1656,926),7),('carre',(1391,826,1659,893),12),('refs',(219,1074,704,1382),7)]
for lab,box,sc in C:crop(48,5,lab,box,sc)
