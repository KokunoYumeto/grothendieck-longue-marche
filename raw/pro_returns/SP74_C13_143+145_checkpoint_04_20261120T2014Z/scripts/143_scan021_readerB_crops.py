from PIL import Image,ImageOps,ImageFilter
from pathlib import Path
root=Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
im=Image.open('/workspace/scratch/8f839dff4bf0/source/SP74_C13_143+145_scans/143_scan021.jpg')
items={
'cancelled_fibres':((930,270,1640,433),3000),
'live_groupoid_glyphs':((468,1093,1175,1310),3000),
'components_restart':((339,1525,1455,1748),3200),
'centralise_assumption':((329,1865,1660,2085),3200),
'final_tail':((340,2087,1650,2345),3200),
}
for label,(box,w) in items.items():
    cr=ImageOps.autocontrast(ImageOps.grayscale(im.crop(box)))
    cr=cr.resize((w,round(cr.height*w/cr.width)),Image.Resampling.LANCZOS)
    cr=cr.filter(ImageFilter.UnsharpMask(radius=1.6,percent=145,threshold=2))
    cr.save(root/'crops'/f'143_scan021_readerB_{label}.png')
print(items)
