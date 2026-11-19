import sys
sys.path.insert(0,'out/scripts');from work import ROOT,OUT,S,name,row
from PIL import Image
r=row(15,55);src=S/(name(r)+'.jpg');im=Image.open(src);w,h=im.size
def cr(label,box,scale=2):
 x0,y0,x1,y1=box;ob=(w-x1,h-y1,w-x0,h-y0)
 a=im.crop(ob).rotate(180);a=a.resize((int(a.width*scale),int(a.height*scale)))
 target=ROOT/'work/crops'/f'{name(r)}_{label}.png';a.save(target)
 with (OUT/'crop_manifest.tsv').open('a') as f:f.write('\t'.join(map(str,[target.name,src,','.join(map(str,ob)),scale,180]))+'\n')
 print(target)
for label,box,scale in [('upright',(0,0,w,h),1),('upright_a',(0,0,w,1160),1),('upright_b',(0,1000,w,h),1),('prop6',(199,279,1662,689),2),('bis1',(204,700,1664,1061),2),('bis2',(204,1072,1687,1266),2),('proof',(212,1288,1618,1610),2),('ending',(210,1617,1603,2001),2),('K',(1166,410,1198,443),10),('E',(780,816,811,850),10),('M',(684,1380,718,1408),10),('slash',(910,1152,956,1193),9),('edge',(1512,1210,1709,1270),6),('s',(343,1356,380,1395),10),('dot',(1427,1493,1469,1521),10),('header',(775,237,910,271),7)]:cr(label,box,scale)

cr('s_comparison',(212,1352,429,1402),6)
