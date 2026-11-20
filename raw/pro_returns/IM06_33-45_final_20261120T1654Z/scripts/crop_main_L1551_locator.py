from pathlib import Path
from PIL import Image, ImageEnhance

root=Path(__file__).resolve().parents[1]
im=Image.open(root/'source/IM06_33-45_scans/34_scan046.jpg')
box=(570,935,1535,1110)
crop=im.crop(box)
crop=ImageEnhance.Contrast(crop).enhance(1.25)
crop=crop.resize((2600,round(crop.height*2600/crop.width)),Image.Resampling.LANCZOS)
crop.save(root/'crops/34_scan046_L1551_duality_locator.png')
