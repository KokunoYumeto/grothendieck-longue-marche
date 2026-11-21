from pathlib import Path
from PIL import Image
r=Path(__file__).resolve().parents[1]/'crops'
p=r/'149_scan109_second_b17_root_rotated.png'
if p.exists():raise RuntimeError('Already made')
with Image.open(r/'149_scan109_second_b17.png') as im:im.rotate(-40,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white').save(p)
