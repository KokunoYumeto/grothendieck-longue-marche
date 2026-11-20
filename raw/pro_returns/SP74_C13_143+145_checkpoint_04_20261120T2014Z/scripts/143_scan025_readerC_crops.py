from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
root=Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
src=Image.open('/workspace/scratch/8f839dff4bf0/source/SP74_C13_143+145_scans/143_scan025.jpg')
boxes={
'margin-note':(25,548,424,1014),
'partition-family':(472,478,1315,588),
'tprime-condition':(1322,656,1580,772),
'object-set-mark':(1437,942,1655,1068),
'first-deletion-on':(1437,1206,1655,1325),
'second-deletion-suppose':(350,1373,847,1487),
'family-index':(986,1545,1657,1703),
'operations-plural':(458,1709,861,1825),
'compatibility-dots':(880,1920,1115,2032),
}
for name,box in boxes.items():
 im=ImageOps.autocontrast(src.crop(box).convert('RGB'))
 if name=='margin-note':im=im.rotate(-8,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 width=2800 if name=='margin-note' else 3000
 im=im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS)
 im=im.filter(ImageFilter.UnsharpMask(radius=1.6,percent=155,threshold=3))
 path=root/'crops'/('143_scan025_readerC_'+name+'.png')
 im.save(path)
 print(name,list(box),'rotation -8 degrees' if name=='margin-note' else '')
