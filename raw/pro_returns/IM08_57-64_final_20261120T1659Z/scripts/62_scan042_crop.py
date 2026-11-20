from PIL import Image, ImageEnhance
from pathlib import Path
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/62_scan042.jpg')
print(im.size)
c=ImageEnhance.Contrast(im.crop((205,325,1630,440))).enhance(1.65)
c.resize((4275,345),Image.Resampling.LANCZOS).save(root/'crops/62_scan042_L807_two_bases.png')
