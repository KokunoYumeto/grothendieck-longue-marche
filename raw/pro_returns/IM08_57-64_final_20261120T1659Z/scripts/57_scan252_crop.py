from PIL import Image, ImageEnhance
from pathlib import Path
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/57_scan252.jpg')
print(im.size)
for name,box,factor in [('57_scan252_L648_sequence.png',(750,235,1320,350),5),('57_scan252_L648_cohomology.png',(720,440,1510,600),4)]:
    c=ImageEnhance.Contrast(im.crop(box)).enhance(1.8)
    c.resize((c.width*factor,c.height*factor),Image.Resampling.LANCZOS).save(root/'crops'/name)
