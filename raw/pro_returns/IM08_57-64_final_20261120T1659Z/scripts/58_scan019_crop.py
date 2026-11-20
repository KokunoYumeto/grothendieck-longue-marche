from PIL import Image, ImageEnhance
from pathlib import Path
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/58_scan019.jpg')
print(im.size)
for name,box,factor in [('58_scan019_L668_map.png',(1070,335,1520,425),6),('58_scan019_L668_pi1_comparison.png',(1100,610,1300,715),12)]:
    c=ImageEnhance.Contrast(im.crop(box)).enhance(1.75)
    c.resize((c.width*factor,c.height*factor),Image.Resampling.LANCZOS).save(root/'crops'/name)
