from pathlib import Path
from PIL import Image, ImageOps
r=Path(__file__).resolve().parents[1]
p=r/'crops/149_scan113_audit_b03_context.png'
assert not p.exists()
box=(930,0,1600,225)
im=Image.open(r.parent/'source/SP88_C13_149_scans/149_scan113.jpg')
c=ImageOps.autocontrast(im.crop(box));c=c.resize((c.width*3,c.height*3),Image.Resampling.LANCZOS);c.save(p)
