from pathlib import Path
from PIL import Image, ImageEnhance
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/64_scan064.jpg')
print(im.size)
for name,box,factor in [
 ('64_scan064_L811_equation_and_roots.png',(790,785,1610,917),4),
 ('64_scan064_L811_radicand.png',(1390,788,1558,878),15)
]:
 c=ImageEnhance.Contrast(im.crop(box)).enhance(1.5)
 c.resize((c.width*factor,c.height*factor),Image.Resampling.LANCZOS).save(root/'crops'/name)
