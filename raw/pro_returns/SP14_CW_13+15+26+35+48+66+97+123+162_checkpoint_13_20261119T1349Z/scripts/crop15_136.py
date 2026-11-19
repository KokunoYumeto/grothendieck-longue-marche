import sys
sys.path.insert(0,'out/scripts');from work import crop
for label,box,scale in [('margin',(1534,115,1590,166),10),('headings',(310,270,525,438),5),('candidates',(448,524,836,652),4),('names',(525,909,724,1200),4),('request',(383,759,1336,808),4),('suggestion',(363,1312,1101,1406),4),('date',(1244,139,1368,186),6),('dots',(1247,589,1290,893),4)]:crop(15,136,label,box,scale)
