import sys
sys.path.insert(0,'out/scripts');from work import crop
for label,box,scale in [('top',(145,311,1638,729),2),('series',(147,739,1650,1134),2),('partition',(141,1133,1642,1418),2),('interpolation',(139,1410,1647,1626),2),('integrals',(137,1606,1633,1833),2),('foot',(135,1815,1620,2012),2),('header',(712,265,850,304),6),('xj',(425,387,557,436),7),('phi',(217,444,290,499),7),('prop',(1050,946,1157,1001),7),('greater',(1038,390,1107,435),7),('norms',(145,1081,1325,1138),3),('denominator',(473,1440,617,1508),6)]:crop(15,33,label,box,scale)
ref=crop(15,33,'reference',(760,939,1160,1004),6)
from PIL import Image,ImageEnhance
ImageEnhance.Contrast(Image.open(ref).convert('L')).enhance(2).save(ref.replace('.png','_contrast.png'))
