from PIL import Image, ImageEnhance
from pathlib import Path
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/62_scan062.jpg')
print(im.size)
for name,box,factor in [('62_scan062_L832_relation_and_comparison.png',(625,800,1585,935),3),('62_scan062_L832_target_index.png',(1165,830,1365,935),13)]:
    c=ImageEnhance.Contrast(im.crop(box)).enhance(1.55)
    c.resize((c.width*factor,c.height*factor),Image.Resampling.LANCZOS).save(root/'crops'/name)
