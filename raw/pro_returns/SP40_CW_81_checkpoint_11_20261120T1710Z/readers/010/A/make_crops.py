from pathlib import Path
import json
from PIL import Image, ImageOps, ImageFilter
BASE=Path(__file__).resolve().parent
SOURCE=BASE.parents[3]/'source/SP40_CW_81_scans/J81-01_81_scan010.jpg'
with Image.open(SOURCE) as source:
    for rec in json.loads((BASE/'crop_plan.json').read_text()):
        crop=source.crop(rec['bbox'])
        crop=ImageOps.autocontrast(crop)
        w,h=crop.size
        crop=crop.resize((2800,round(h*2800/w)),Image.Resampling.LANCZOS)
        crop=crop.filter(ImageFilter.UnsharpMask(radius=1,percent=110,threshold=3))
        crop.save(BASE/rec['path'])
