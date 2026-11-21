from pathlib import Path
from PIL import Image,ImageOps
r=Path(__file__).resolve().parents[1];p=r/'crops/149_scan108_audit_b10_label.png'
if p.exists():raise RuntimeError('Already made')
box=(280,1430,445,1592)
with Image.open(r.parent/'source/SP88_C13_149_scans/149_scan108.jpg') as im:
 c=ImageOps.autocontrast(im.crop(box));c.resize((c.width*8,c.height*8),Image.Resampling.LANCZOS).save(p)
print(box)
