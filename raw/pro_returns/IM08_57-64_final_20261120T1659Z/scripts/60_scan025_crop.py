from PIL import Image, ImageEnhance
from pathlib import Path
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/60_scan025.jpg')
print(im.size)
for name,box,factor in [('60_scan025_L664_boxed_shift.png',(110,1060,1090,1260),3),('60_scan025_L664_sign_margin.png',(1200,1090,1620,1255),6)]:
    c=ImageEnhance.Contrast(im.crop(box)).enhance(1.65)
    c.resize((c.width*factor,c.height*factor),Image.Resampling.LANCZOS).save(root/'crops'/name)
