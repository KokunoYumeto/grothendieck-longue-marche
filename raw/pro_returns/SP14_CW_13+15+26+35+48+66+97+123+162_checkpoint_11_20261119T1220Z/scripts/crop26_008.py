import sys
sys.path.insert(0,'out/scripts');from work import crop,ROOT,OUT
from PIL import Image,ImageOps,ImageEnhance
for label,box,scale in [('corner',(29,29,143,111),9),('line1',(244,63,1213,145),5),('line2',(245,154,1548,300),4),('old3',(541,331,623,418),12),('line3',(260,323,1611,441),4),('lines45',(282,476,1628,642),4),('old4',(1234,490,1438,546),10),('lines678',(316,672,1606,898),4),('diagram',(287,937,1651,1584),3),('CtoH',(690,1055,797,1289),6),('appendix',(628,1688,1463,1779),5),('watermark',(660,321,864,2103),2)]:crop(26,8,label,box,scale)
p=ROOT/'work/crops/H26-01_26_scan008_watermark.png'
im=Image.open(p).rotate(270,expand=True,fillcolor='white');im=ImageOps.mirror(im);im=ImageEnhance.Contrast(im).enhance(3)
o=p.with_name('H26-01_26_scan008_watermark_upright.png');im.save(o)
with (OUT/'crop_manifest.tsv').open('a') as f:f.write(f'{o.name}\t{p}\twhole generated crop\t1\t270;mirror=True;contrast=3\n')

crop(26,8,'name',(445,167,668,228),10)
p=crop(26,8,'watermark_full',(650,200,900,2130),2)
im=ImageEnhance.Contrast(ImageOps.mirror(Image.open(p).rotate(270,expand=True))).enhance(3)
im.save(ROOT/'work/crops/H26-01_26_scan008_watermark_full_upright.png')

crop(26,8,'strayleft',(213,1405,254,1453),10)
crop(26,8,'straybottom',(331,1794,546,1870),6)

p=ROOT/'work/crops/H26-01_26_scan008_watermark_full.png'
ImageEnhance.Contrast(Image.open(p).rotate(90,expand=True)).enhance(3).save(p.with_name('H26-01_26_scan008_watermark_readable.png'))
