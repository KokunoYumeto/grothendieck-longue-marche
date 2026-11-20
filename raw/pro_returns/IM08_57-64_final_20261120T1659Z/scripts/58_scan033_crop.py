from PIL import Image, ImageEnhance
from pathlib import Path
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/58_scan033.jpg')
print(im.size)
c=ImageEnhance.Contrast(im.crop((320,1030,1660,1175))).enhance(1.6)
c.resize((4020,435),Image.Resampling.LANCZOS).save(root/'crops/58_scan033_H0481_voisinage.png')
for name,box,factor in [('58_scan033_H0481_line_end.png',(1510,1020,1665,1100),16),('58_scan033_H0481_line_start.png',(330,1105,900,1170),5)]:
    c=ImageEnhance.Contrast(im.crop(box)).enhance(1.6)
    c.resize((c.width*factor,c.height*factor),Image.Resampling.LANCZOS).save(root/'crops'/name)
