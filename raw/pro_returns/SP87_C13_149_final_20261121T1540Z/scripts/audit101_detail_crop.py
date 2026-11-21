from PIL import Image,ImageOps,ImageFilter
from pathlib import Path
import json
w=Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work');box=(1025,1340,1275,1470)
p=w.parent/'source/SP87_C13_149_scans/149_scan101.jpg'
im=Image.open(p).crop(box)
im=ImageOps.autocontrast(im).resize((2200,1144),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1,percent=110,threshold=3))
im.save(w/'crops/audit_149_scan101_infinity_word.png')
(w/'review/audit101_detail_crop.json').write_text(json.dumps({'source':str(p),'box':box,'crop':'crops/audit_149_scan101_infinity_word.png','purpose':'Second-reading root adjudication: distinguish the tiny two-lobed form after l-apostrophe; B012 whole-span crop insufficiently magnifies it.','operations':'autocontrast; LANCZOS to2200px; light UnsharpMask'},indent=2)+'\n')
