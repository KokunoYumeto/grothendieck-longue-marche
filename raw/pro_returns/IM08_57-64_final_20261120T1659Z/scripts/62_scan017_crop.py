from PIL import Image, ImageEnhance
from pathlib import Path
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/62_scan017.jpg')
print(im.size)
for name,box,factor in [('62_scan017_L797_matrices.png',(600,1770,1640,1920),3),('62_scan017_L797_affine_group.png',(370,1910,1645,2010),3)]:
    c=ImageEnhance.Contrast(im.crop(box)).enhance(1.7)
    c.resize((c.width*factor,c.height*factor),Image.Resampling.LANCZOS).save(root/'crops'/name)
