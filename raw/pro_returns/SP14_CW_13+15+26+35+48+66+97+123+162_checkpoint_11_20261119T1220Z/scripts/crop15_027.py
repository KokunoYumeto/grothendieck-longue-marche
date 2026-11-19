import sys
sys.path.insert(0,'out/scripts');from work import crop
for label,box,scale in [('header',(743,239,878,292),5),('top',(145,286,1648,554),2),('route',(147,549,1638,834),2),('primitives',(146,853,1654,1241),2),('principle',(307,1261,1665,1654),2),('compatibility',(308,1658,1646,2014),2),('old_word',(1534,1053,1669,1115),6),('index',(661,1661,742,1716),6),('defined',(742,1668,1063,1711),4),('finally',(1375,1949,1574,1996),4)]:crop(15,27,label,box,scale)
