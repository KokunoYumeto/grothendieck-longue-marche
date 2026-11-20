from pathlib import Path
from PIL import Image, ImageEnhance
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/64_scan103.jpg')
print(im.size)
for name,box,factor in [
 ('64_scan103_L813_multiplication_text.png',(270,535,1330,650),3),
 ('64_scan103_L813_canonical_map.png',(1230,1188,1530,1455),8),
 ('64_scan103_L813_kernel.png',(595,1800,1160,1920),5)
]:
 c=ImageEnhance.Contrast(im.crop(box)).enhance(1.5)
 c.resize((c.width*factor,c.height*factor),Image.Resampling.LANCZOS).save(root/'crops'/name)
