from pathlib import Path
from PIL import Image, ImageEnhance
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/62_scan090.jpg')
print(im.size)
for name,box,factor in [
 ('62_scan090_L827_three_formulas.png',(520,866,1355,1217),3),
 ('62_scan090_L827_coefficient.png',(535,1103,696,1202),16)
]:
 c=ImageEnhance.Contrast(im.crop(box)).enhance(1.5)
 c.resize((c.width*factor,c.height*factor),Image.Resampling.LANCZOS).save(root/'crops'/name)
