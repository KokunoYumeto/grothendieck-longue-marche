import sys
sys.path.insert(0,'out/scripts');from work import crop
for label,box,scale in [('header',(698,225,841,272),5),('proposition',(123,268,1638,656),2),('lemma',(124,659,1638,844),2),('proof1',(123,849,1647,1207),2),('proof2',(123,1194,1647,1638),2),('routes',(121,1638,1635,2050),2),('Or',(471,970,558,1044),6),('lemma_rule',(886,739,1142,792),5),('a_insert',(361,1965,434,2022),7),('th',(1568,1993,1644,2047),7),('barB',(722,985,763,1040),7)]:crop(15,29,label,box,scale)
