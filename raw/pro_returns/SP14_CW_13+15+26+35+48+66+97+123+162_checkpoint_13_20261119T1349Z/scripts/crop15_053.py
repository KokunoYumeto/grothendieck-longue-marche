import sys
sys.path.insert(0,'out/scripts');from work import ROOT,OUT,S,name,row
from PIL import Image
r=row(15,53);src=S/(name(r)+'.jpg');im=Image.open(src);w,h=im.size
def cr(label,box,scale=2):
 x0,y0,x1,y1=box;ob=(w-x1,h-y1,w-x0,h-y0)
 a=im.crop(ob).rotate(180);a=a.resize((int(a.width*scale),int(a.height*scale)))
 target=ROOT/'work/crops'/f'{name(r)}_{label}.png';a.save(target)
 with (OUT/'crop_manifest.tsv').open('a') as f:f.write('\t'.join(map(str,[target.name,src,','.join(map(str,ob)),scale,180]))+'\n')
 print(target)
for label,box,scale in [('upright',(0,0,w,h),1),('upright_a',(0,0,w,1160),1),('upright_b',(0,1000,w,h),1),('top',(158,264,1645,614),2),('series',(145,616,1611,1002),2),('prop',(164,1021,1645,1314),2),('eq6',(166,1306,1643,1423),2),('bottom1',(166,1414,1608,1651),2),('bottom2',(166,1670,1645,1921),2),('c',(768,268,811,302),9),('accent',(1215,258,1354,309),7),('K',(1506,574,1549,611),9),('R',(1134,695,1193,742),8),('prime',(1434,1414,1470,1445),10),('Po',(1000,1178,1055,1235),7),('header',(714,210,849,249),7),('bound',(150,625,303,697),6)]:cr(label,box,scale)

cr('ap',(1100,1340,1166,1403),8)
cr('general_comma',(322,746,377,794),9)
