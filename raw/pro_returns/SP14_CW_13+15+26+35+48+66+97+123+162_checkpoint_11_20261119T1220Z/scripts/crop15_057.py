import sys
sys.path.insert(0,'out/scripts');from work import ROOT,OUT,S,name,row
from PIL import Image
r=row(15,57);src=S/(name(r)+'.jpg');im=Image.open(src);w,h=im.size
def cr(label,box,scale=2):
 x0,y0,x1,y1=box;ob=(w-x1,h-y1,w-x0,h-y0)
 a=im.crop(ob).rotate(180);a=a.resize((int(a.width*scale),int(a.height*scale)))
 target=ROOT/'work/crops'/f'{name(r)}_{label}.png';a.save(target)
 with (OUT/'crop_manifest.tsv').open('a') as f:f.write('\t'.join(map(str,[target.name,src,','.join(map(str,ob)),scale,180]))+'\n')
 print(target)
for label,box,scale in [('upright',(0,0,w,h),1),('upright_a',(0,0,w,1160),1),('upright_b',(0,1000,w,h),1),('top',(155,274,1623,490),2),('prop4a',(155,517,1644,888),2),('prop4b',(154,906,1658,1093),2),('proof',(151,1102,1604,1412),2),('definition',(152,1425,1628,1814),2),('bottom',(149,1825,1550,2019),2),('gamma',(729,411,779,468),8),('c',(985,645,1024,682),9),('K',(1099,1436,1128,1476),10),('E',(665,1504,696,1543),10),('section4',(155,524,191,562),9),('accent',(155,1424,271,1477),7),('ordinal',(996,334,1048,384),8),('header',(710,231,826,272),7)]:cr(label,box,scale)
