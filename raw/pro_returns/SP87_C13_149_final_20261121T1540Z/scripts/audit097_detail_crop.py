from PIL import Image,ImageEnhance,ImageFilter
from pathlib import Path
import json
w=Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work');box=(1280,2140,1570,2340)
im=Image.open(w.parent/'source/SP87_C13_149_scans/149_scan097.jpg').crop(box)
im=im.resize((1800,round(im.height*1800/im.width)),Image.Resampling.LANCZOS)
im=ImageEnhance.Contrast(im).enhance(1.25).filter(ImageFilter.UnsharpMask(radius=1.5,percent=115,threshold=3))
im.save(w/'crops/audit_149_scan097_final_insertion.png')
(w/'review/149_scan097_additional_crop_manifest.json').write_text(json.dumps({'source':'149_scan097.jpg','coordinates':box,'crop':'crops/audit_149_scan097_final_insertion.png','reason':'Anonymous B020 clips the top of the raised replacement; include complete ascenders and terminal numeral.','stage':'root adjudication after blind TSV saved'},indent=2)+'\n')
