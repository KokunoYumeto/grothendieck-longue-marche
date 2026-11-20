from pathlib import Path
from PIL import Image, ImageEnhance
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/64_scan025.jpg')
print(im.size)
for name,box,factor in [
 ('64_scan025_L809_clause.png',(395,1550,1260,1730),3),
 ('64_scan025_L809_deletions.png',(590,1615,970,1715),7)
]:
 c=ImageEnhance.Contrast(im.crop(box)).enhance(1.5)
 c.resize((c.width*factor,c.height*factor),Image.Resampling.LANCZOS).save(root/'crops'/name)
