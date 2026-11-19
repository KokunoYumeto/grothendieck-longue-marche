import sys
sys.path.insert(0,'out/scripts');from work import crop,ROOT,OUT
from PIL import Image,ImageEnhance
for label,box,scale in [('divsuffixes',(125,260,1080,371),3),('prepic_old1',(1125,1170,1380,1270),8),('prepic_old2',(1370,1160,1676,1290),8),('prepic_liveH',(1095,1090,1570,1188),6),('prepicprime_oldsign',(1125,1320,1240,1400),10),('oldhom_start2',(770,1740,1080,1875),5),('oldhom_end',(1330,1850,1435,1960),8),('lower_index',(211,2070,350,2151),10),('lower_right_end',(1530,2000,1678,2110),10),('left_mark',(105,1577,241,1780),7),('homprod_oldX',(230,1665,312,1735),10),('watermark_bottom',(740,400,940,2080),2)]:crop(26,9,label,box,scale)
p=ROOT/'work/crops/H26-01_26_scan009_watermark_bottom.png';im=ImageEnhance.Contrast(Image.open(p).rotate(90,expand=True)).enhance(2);o=p.with_name(p.stem+'_upright.png');im.save(o)
with (OUT/'crop_manifest.tsv').open('a') as f:f.write(f'{o.name}\t{p}\twhole crop\t1\t90;contrast=2\n')
