import sys
sys.path.insert(0,'out/scripts');from work import crop,ROOT,OUT
from PIL import Image
for label,box,scale in [('quadr',(434,507,611,580),13),('lef',(969,499,1081,579),12),('exist',(947,802,1145,881),12),('etend',(1243,807,1363,875),13),('cohend',(1521,803,1662,895),12),('xixth',(259,908,335,982),14),('xxiend',(1497,1122,1672,1204),12),('picapost',(335,673,417,728),14),('bottomdot',(684,1693,754,1766),12)]:crop(35,3,label,box,scale)
p=crop(35,3,'return_upright_source',(1334,23,1608,118),10)
o=ROOT/'work/crops/H35-01_35_scan003_return_upright.png';Image.open(p).rotate(-8,expand=True,fillcolor='white').save(o)
with (OUT/'crop_manifest.tsv').open('a') as f:f.write(f'{o.name}\t{p}\twhole crop\t1\t-8\n')
