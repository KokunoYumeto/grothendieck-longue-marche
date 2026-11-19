import sys
sys.path.insert(0,'out/scripts');from work import ROOT,OUT,S,name,row
from PIL import Image
r=row(15,51);src=S/(name(r)+'.jpg');im=Image.open(src);w,h=im.size
def cr(label,box,scale=2):
 x0,y0,x1,y1=box;ob=(w-x1,h-y1,w-x0,h-y0)
 a=im.crop(ob).rotate(180);a=a.resize((int(a.width*scale),int(a.height*scale)))
 target=ROOT/'work/crops'/f'{name(r)}_{label}.png';a.save(target)
 with (OUT/'crop_manifest.tsv').open('a') as f:f.write('\t'.join(map(str,[target.name,src,','.join(map(str,ob)),scale,180]))+'\n')
 print(target)
for label,box,scale in [('upright',(0,0,w,h),1),('upright_a',(0,0,w,1164),1),('upright_b',(0,1004,w,h),1),('formula1',(175,225,1654,427),2),('bounds',(132,424,1616,824),2),('bound2',(192,812,1393,1030),2),('corollary',(134,1030,1636,1355),2),('proof',(143,1354,1629,1810),2),('zero',(141,1829,1622,2080),2),('M',(1157,613,1197,654),9),('smile',(1077,786,1159,842),8),('E',(328,1629,372,1676),9),('K',(899,1829,934,1871),9),('colon',(1419,355,1476,397),8),('header',(664,226,793,258),7)]:cr(label,box,scale)
