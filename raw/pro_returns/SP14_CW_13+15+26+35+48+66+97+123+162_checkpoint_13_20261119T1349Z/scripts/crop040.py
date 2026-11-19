import sys
from PIL import Image
sys.path.insert(0,'out/scripts');from work import crop,OUT
for label,box in [('heading',(150,25,1635,170)),('paragraph',(228,243,1635,577)),('factorization',(240,500,1210,780)),('torsor',(260,725,1658,1135)),('cancelled',(255,1140,1630,1570)),('replacement',(263,1415,1570,1900)),('end',(270,1830,1635,2135))]:crop(13,40,label,box,2)
for label,box,angle in [('side_upright',(22,225,280,497),-34),('cancelled_upright',(255,1140,1630,1570),-4),('bottom_upright',(270,1830,1635,2135),-4)]:
 p=crop(13,40,label,box,2);Image.open(p).rotate(angle,expand=True,fillcolor='white').save(p)
 with (OUT/'crop_manifest.tsv').open('a') as f:f.write(p.split('/')[-1]+'\trotation after crop\t'+str(box)+'\t2\t'+str(angle)+'\n')
