from pathlib import Path
from PIL import Image, ImageEnhance
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/62_scan081.jpg')
print(im.size)
for name,box,factor in [
 ('62_scan081_L824_series.png',(360,966,1308,1100),3),
 ('62_scan081_L824_coefficient.png',(605,976,762,1087),16)
]:
 c=ImageEnhance.Contrast(im.crop(box)).enhance(1.5)
 c.resize((c.width*factor,c.height*factor),Image.Resampling.LANCZOS).save(root/'crops'/name)
