from PIL import Image, ImageEnhance
from pathlib import Path
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/58_scan003.jpg')
print(im.size)
for name,box,factor in [('58_scan003_L666_hypothesis.png',(285,330,1655,755),3),('58_scan003_L666_reduction.png',(390,1400,1570,1785),3)]:
    c=ImageEnhance.Contrast(im.crop(box)).enhance(1.6)
    c.resize((c.width*factor,c.height*factor),Image.Resampling.LANCZOS).save(root/'crops'/name)
