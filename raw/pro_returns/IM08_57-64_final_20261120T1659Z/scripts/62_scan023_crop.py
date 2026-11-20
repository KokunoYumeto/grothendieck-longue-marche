from PIL import Image, ImageEnhance
from pathlib import Path
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/62_scan023.jpg')
print(im.size)
c=ImageEnhance.Contrast(im.crop((485,1355,1125,1525))).enhance(1.7)
c.resize((2560,680),Image.Resampling.LANCZOS).save(root/'crops/62_scan023_L803_intermediate_and_final.png')
