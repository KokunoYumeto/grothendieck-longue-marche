from PIL import Image, ImageEnhance
from pathlib import Path
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/62_scan028.jpg')
print(im.size)
for name,box,factor in [('62_scan028_L804_target_subscript.png',(670,2025,825,2135),16),('62_scan028_L804_top_S3_comparison.png',(775,185,905,280),19)]:
    c=ImageEnhance.Contrast(im.crop(box)).enhance(1.65)
    c.resize((c.width*factor,c.height*factor),Image.Resampling.LANCZOS).save(root/'crops'/name)
