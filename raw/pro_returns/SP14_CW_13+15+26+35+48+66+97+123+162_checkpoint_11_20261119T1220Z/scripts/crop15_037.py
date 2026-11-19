import sys
sys.path.insert(0,'out/scripts');from work import crop
for label,box,scale in [('headings',(154,296,1589,676),2),('proposition',(154,691,1646,1237),2),('proof1',(156,1248,1657,1675),2),('proof2',(154,1680,1688,2053),2),('header',(723,241,864,286),6),('number',(155,513,207,561),7),('title_dot',(671,513,795,562),7),('section_punct',(377,569,492,622),7),('old_g',(1282,878,1439,950),6),('dash',(769,1060,926,1103),7),('rule',(172,756,509,804),5)]:crop(15,37,label,box,scale)
