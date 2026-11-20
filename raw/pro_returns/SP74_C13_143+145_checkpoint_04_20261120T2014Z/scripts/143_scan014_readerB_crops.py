from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
root=Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
im=Image.open('/workspace/scratch/8f839dff4bf0/source/SP74_C13_143+145_scans/143_scan014.jpg')
items={
'les_appl':((470,413,672,522),2400),
'hom_ending':((1390,1285,1650,1392),2400),
'first_aut_map':((600,1390,1645,1537),3000),
'cancelled_peut_se':((900,1753,1215,1861),2400),
'lower_group_maps':((640,1950,1645,2165),3000),
'final_clause':((375,2160,1565,2250),3000),
'final_deduite':((370,2242,1050,2310),2800),
'final_envisagees':((1050,2235,1662,2314),2800),
}
for label,(box,w) in items.items():
    cr=ImageOps.autocontrast(ImageOps.grayscale(im.crop(box)))
    cr=cr.resize((w,round(cr.height*w/cr.width)),Image.Resampling.LANCZOS)
    cr=cr.filter(ImageFilter.UnsharpMask(radius=1.6,percent=145,threshold=2))
    cr.save(root/'crops'/f'143_scan014_readerB_{label}.png')
print(items)
