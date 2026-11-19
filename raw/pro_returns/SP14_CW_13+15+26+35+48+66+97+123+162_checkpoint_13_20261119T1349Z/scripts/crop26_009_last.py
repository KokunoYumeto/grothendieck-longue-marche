import sys
sys.path.insert(0,'out/scripts');from work import crop,ROOT,OUT
from PIL import Image,ImageEnhance
for label,box,scale in [('left_number',(42,1694,119,1784),10),('bottom_innerhom',(330,2070,456,2140),10),('bottom_right_sub',(1536,2036,1602,2108),10),('prepicoldsub',(748,1170,828,1258),10),('watermark_letters',(764,130,923,1060),3),('watermark_end',(764,1050,923,1620),3),('gammaend',(460,1057,544,1126),10),('productoldword',(584,921,685,1031),8)]:crop(26,9,label,box,scale)
for label in ['watermark_letters','watermark_end']:
 p=ROOT/f'work/crops/H26-01_26_scan009_{label}.png'
 for deg in [90,270]:
  im=ImageEnhance.Contrast(Image.open(p).rotate(deg,expand=True)).enhance(2);o=p.with_name(p.stem+f'_rot{deg}.png');im.save(o)
  with (OUT/'crop_manifest.tsv').open('a') as f:f.write(f'{o.name}\t{p}\twhole crop\t1\t{deg};contrast=2\n')
