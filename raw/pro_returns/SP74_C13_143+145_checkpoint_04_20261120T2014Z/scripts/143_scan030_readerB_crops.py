from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
root=Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
im=Image.open('/workspace/scratch/8f839dff4bf0/source/SP74_C13_143+145_scans/143_scan030.jpg').convert('RGB')
items={
 'opening_clause':((715,56,1626,150),3000,0),
 'upper_exception':((23,45,273,293),2600,0),
 'diagram_upper_row':((384,357,1585,488),3200,0),
 'diagram_left_link':((570,470,859,718),2800,0),
 'diagram_right':((896,485,1681,796),3200,0),
 'invariance':((333,747,1493,1047),3200,0),
 'margin_normalizer':((17,577,646,1186),3200,-35),
 'cancelled_a':((495,1097,974,1178),2600,0),
 'quotient':((362,1548,1553,1848),3200,0),
 'margin_exception':((13,1168,511,1850),3200,-42),
 'margin_prudence':((15,1583,511,2348),3200,-42),
 'example_cela':((1094,1879,1621,1983),2600,0),
 'example_formula':((347,2111,1214,2245),3200,0),
}
for label,(box,width,angle) in items.items():
    cr=ImageOps.autocontrast(im.crop(box))
    if angle:
        cr=cr.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    cr=cr.resize((width,round(cr.height*width/cr.width)),Image.Resampling.LANCZOS)
    cr=cr.filter(ImageFilter.UnsharpMask(radius=1.6,percent=145,threshold=2))
    path=root/'crops'/f'143_scan030_readerB_{label}.png'
    cr.save(path)
    print(f'{path.name}: {box}, rotation {angle}')
