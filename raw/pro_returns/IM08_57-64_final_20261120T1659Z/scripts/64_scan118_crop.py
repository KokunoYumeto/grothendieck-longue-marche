from pathlib import Path
from PIL import Image, ImageEnhance
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/64_scan118.jpg')
print(im.size)
for name,box,factor in [
 ('64_scan118_L815_margin_sign.png',(18,125,488,255),6),
 ('64_scan118_L815_bracket_sign.png',(1250,132,1665,264),7)
]:
 c=ImageEnhance.Contrast(im.crop(box)).enhance(1.5)
 c.resize((c.width*factor,c.height*factor),Image.Resampling.LANCZOS).save(root/'crops'/name)
