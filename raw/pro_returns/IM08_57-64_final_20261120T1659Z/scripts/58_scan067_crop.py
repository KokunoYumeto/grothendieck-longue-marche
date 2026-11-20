from PIL import Image, ImageEnhance
from pathlib import Path
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/58_scan067.jpg')
print(im.size)
for name,box,factor in [('58_scan067_L663_pic_map.png',(690,1255,1420,1375),4),('58_scan067_L663_factorial_margin.png',(35,1310,330,1545),8),('58_scan067_H0490_diagram_margin.png',(35,555,220,715),12),('58_scan067_H0490_deleted_section.png',(295,1425,1660,1630),3)]:
    c=ImageEnhance.Contrast(im.crop(box)).enhance(1.7)
    c.resize((c.width*factor,c.height*factor),Image.Resampling.LANCZOS).save(root/'crops'/name)
