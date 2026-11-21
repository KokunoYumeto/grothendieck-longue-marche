"""Context crops for still-open independent-audit differences b10 and b11."""
from pathlib import Path
from PIL import Image, ImageOps
ROOT=Path(__file__).resolve().parents[1]
source=Image.open(ROOT.parent/'source/SP88_C13_149_scans/149_scan106.jpg')
for name,box in [('b10_context',(1035,1350,1681,1555)),
                 ('b11_context',(235,1720,1681,1990))]:
    dest=ROOT/'crops'/f'149_scan106_audit_{name}.png'
    if dest.exists():raise FileExistsError(dest)
    crop=ImageOps.autocontrast(source.crop(box))
    crop=crop.resize((3200,round(crop.height*3200/crop.width)),Image.Resampling.LANCZOS)
    crop.save(dest)
    print(name,box)
