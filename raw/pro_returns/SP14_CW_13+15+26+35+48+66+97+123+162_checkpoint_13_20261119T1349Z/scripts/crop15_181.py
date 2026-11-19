import sys
sys.path.insert(0,'out/scripts');from work import crop,ROOT,OUT
from PIL import Image
p=crop(15,181,'list',(472,1699,1573,2292),3)
o=ROOT/'work/crops/B15-01_15_scan181_list_upright.png';Image.open(p).rotate(180,expand=True).save(o)
with (OUT/'crop_manifest.tsv').open('a') as f:f.write(f'{o.name}\t{p}\twhole generated crop\t1\t180\n')
