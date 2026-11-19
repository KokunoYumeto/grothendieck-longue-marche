import sys
sys.path.insert(0,'out/scripts');from work import crop,ROOT,OUT
from PIL import Image,ImageOps,ImageEnhance
for label,box,scale in [('heading',(292,207,1346,382),4),('partout',(318,400,1534,525),4),('quote',(324,536,1484,647),5),('bottomwords',(223,768,1436,1020),4),('formula',(971,813,1548,1086),6),('old',(968,913,1110,995),10),('super0',(1157,900,1210,957),12),('arrows',(1215,917,1308,986),12),('punct',(753,886,835,967),10),('watermark',(778,109,1072,2085),2)]:crop(26,7,label,box,scale)
for base,angle,flip in [('heading',-2,False),('partout',-3,False),('quote',-3,False),('bottomwords',-2,False),('watermark',90,True)]:
 p=ROOT/'work/crops'/f'H26-01_26_scan007_{base}.png';im=Image.open(p).rotate(angle,expand=True,fillcolor='white')
 if flip:im=ImageOps.mirror(im);im=ImageEnhance.Contrast(im).enhance(3)
 o=p.with_name(p.stem+'_upright.png');im.save(o)
 with (OUT/'crop_manifest.tsv').open('a') as f:f.write(f'{o.name}\t{p}\twhole generated crop\t1\t{angle};mirror={flip};contrast={3 if flip else 1}\n')

crop(26,7,'cpct',(706,547,934,631),10)
p=ROOT/'work/crops/H26-01_26_scan007_watermark_upright.png'
Image.open(p).rotate(180,expand=True).save(p.with_name('H26-01_26_scan007_watermark_readable.png'))
