from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
r=Path('/workspace/scratch/8f839dff4bf0')
w=r/'SP74_C13_143+145_work'
s=Image.open(r/'source/SP74_C13_143+145_scans/143_scan034.jpg')
boxes={
 'delta-u-statement':[1150,1320,1630,1405],
 'u-m-statement':[1200,1220,1635,1310],
 'first-arithmetic':[165,755,405,925]
}
for name,box in boxes.items():
 im=ImageOps.autocontrast(s.crop(box).transpose(Image.Transpose.ROTATE_180))
 im=im.resize((3000,round(im.height*3000/im.width)),Image.Resampling.LANCZOS)
 im=im.filter(ImageFilter.UnsharpMask(radius=1.6,percent=155,threshold=3))
 im.save(w/'crops'/f'143_scan034_readerC_{name}.png')
print(boxes)
