import sys
from PIL import Image
sys.path.insert(0,'out/scripts');from work import crop,OUT
items=[('heading',(163,43,1642,211),2),('opening',(205,203,1652,374),2),('clauses',(296,364,1651,538),2),('item1',(210,540,1649,1009),2),('item1b',(218,995,1650,1247),2),('connected',(220,1226,1648,1556),2),('item2',(211,1504,1648,1950),2),('bottom',(215,1920,1651,2136),2)]
for label,box,scale in items:crop(13,51,label,box,scale)
for label,box,scale,angle in [('margin_upright',(20,1778,254,2002),4,-17),('pair_upright',(214,1691,1649,1910),2.5,-5),('item1_insert_upright',(480,660,1133,747),3,-5)]:
 p=crop(13,51,label,box,scale)
 Image.open(p).rotate(angle,expand=True,fillcolor='white').save(p)
 with (OUT/'crop_manifest.tsv').open('a') as f:f.write(p.split('/')[-1]+'\trotation after crop\t'+','.join(map(str,box))+'\t'+str(scale)+'\t'+str(angle)+'\n')
