from PIL import Image, ImageEnhance
from pathlib import Path
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/62_scan046.jpg')
print(im.size)
c=ImageEnhance.Contrast(im.crop((250,385,1400,485))).enhance(1.7)
c.resize((3450,300),Image.Resampling.LANCZOS).save(root/'crops/62_scan046_L808_normal_integral.png')
