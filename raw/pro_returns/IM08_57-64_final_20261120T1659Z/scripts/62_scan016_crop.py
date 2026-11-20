from PIL import Image, ImageEnhance
from pathlib import Path
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/62_scan016.jpg')
print(im.size)
for name,box,factor in [('62_scan016_L798_opening.png',(270,60,1170,220),3),('62_scan016_L798_folio.png',(30,2045,150,2140),20)]:
    c=ImageEnhance.Contrast(im.crop(box)).enhance(1.65)
    c.resize((c.width*factor,c.height*factor),Image.Resampling.LANCZOS).save(root/'crops'/name)
