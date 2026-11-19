import sys
from PIL import Image
sys.path.insert(0,'out/scripts');from work import crop,OUT
for label,box,scale in [('text',(208,37,1644,282),2),('Alg',(1470,72,1555,138),5),('conjuguant',(266,226,539,291),5),('insert',(539,90,701,138),5)]:crop(13,52,label,box,scale)
p=crop(13,52,'watermark',(615,0,1050,2152),1.5)
Image.open(p).convert('L').point(lambda v:max(0,min(255,(v-210)*255/40))).rotate(90,expand=True,fillcolor='white').save(p)
with (OUT/'crop_manifest.tsv').open('a') as f:f.write(p.split('/')[-1]+'\tgrayscale levels 210–250 rotation\t615,0,1050,2152\t1.5\t90\n')
