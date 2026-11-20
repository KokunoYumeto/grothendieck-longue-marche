from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from pathlib import Path
root=Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
im=Image.open('/workspace/scratch/8f839dff4bf0/source/SP74_C13_143+145_scans/143_scan009.jpg')
items={
'formula25':((375,150,1605,325),3000),
'interline_stabilizer':((1095,405,1665,505),2600),
'cancelled_block26':((240,750,1672,1015),3200),
'divi_ending':((1055,1120,1460,1225),2400),
'under_inclusion':((470,1545,875,1710),2600),
'subgroup_abbreviation':((455,1975,1650,2080),3000),
}
for label,(box,w) in items.items():
    cr=ImageOps.autocontrast(ImageOps.grayscale(im.crop(box)))
    cr=cr.resize((w,round(cr.height*w/cr.width)),Image.Resampling.LANCZOS)
    cr=cr.filter(ImageFilter.UnsharpMask(radius=1.6,percent=145,threshold=2))
    cr.save(root/'crops'/f'143_scan009_readerB_{label}.png')
print(items)
