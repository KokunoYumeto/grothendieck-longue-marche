from PIL import Image, ImageEnhance
from pathlib import Path
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/62_scan004.jpg')
print(im.size)
c=ImageEnhance.Contrast(im.crop((1120,1245,1660,1350))).enhance(1.75)
c.resize((3240,630),Image.Resampling.LANCZOS).save(root/'crops/62_scan004_H0506_parenthesis.png')
