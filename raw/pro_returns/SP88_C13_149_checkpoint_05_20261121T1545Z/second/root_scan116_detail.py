from pathlib import Path
from PIL import Image
r=Path(__file__).resolve().parents[1];p=r/'second/diagnostics/149_scan116_b03_leftmark.png';assert not p.exists();im=Image.open(r/'crops/149_scan116_second_b03.png');box=(0,570,240,840);c=im.crop(box);c.resize((c.width*3,c.height*3),Image.Resampling.LANCZOS).save(p)
