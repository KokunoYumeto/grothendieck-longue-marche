from PIL import Image, ImageEnhance
from pathlib import Path
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/59_scan013.jpg')
print(im.size)
for name,box,factor in [('59_scan013_L673_nb_line.png',(310,865,1650,1010),3),('59_scan013_L673_ppcm.png',(625,910,810,995),14)]:
    c=ImageEnhance.Contrast(im.crop(box)).enhance(1.75)
    c.resize((c.width*factor,c.height*factor),Image.Resampling.LANCZOS).save(root/'crops'/name)
