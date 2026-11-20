from PIL import Image,ImageOps,ImageFilter
from pathlib import Path
root=Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
im=Image.open('/workspace/scratch/8f839dff4bf0/source/SP74_C13_143+145_scans/143_scan016.jpg')
items={
'first_isom_display':((375,138,1662,400),3200),
'hom_tors_prose':((840,515,1647,605),2800),
'cancelled_comme':((315,635,538,726),2400),
'cancelled_les_operations':((294,909,675,1018),2600),
'action_diagram':((420,1505,1665,1862),3200),
'bitorseur_definition':((650,1935,1665,2061),3000),
'final_isom_pair':((545,2154,1280,2357),2800),
}
for label,(box,w) in items.items():
    cr=ImageOps.autocontrast(ImageOps.grayscale(im.crop(box)))
    cr=cr.resize((w,round(cr.height*w/cr.width)),Image.Resampling.LANCZOS)
    cr=cr.filter(ImageFilter.UnsharpMask(radius=1.6,percent=145,threshold=2))
    cr.save(root/'crops'/f'143_scan016_readerB_{label}.png')
print(items)
