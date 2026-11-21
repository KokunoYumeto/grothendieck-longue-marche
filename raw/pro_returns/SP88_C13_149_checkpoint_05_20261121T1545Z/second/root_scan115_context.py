from pathlib import Path
from PIL import Image,ImageOps
r=Path(__file__).resolve().parents[1];p=r/'crops/149_scan115_audit_b09_accent.png';assert not p.exists();box=(1250,1480,1660,1750)
c=ImageOps.autocontrast(Image.open(r.parent/'source/SP88_C13_149_scans/149_scan115.jpg').crop(box));c.resize((c.width*4,c.height*4),Image.Resampling.LANCZOS).save(p)
