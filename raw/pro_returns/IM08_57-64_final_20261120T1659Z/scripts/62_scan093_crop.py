from pathlib import Path
from PIL import Image, ImageEnhance
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/62_scan093.jpg')
print(im.size)
for name,box,factor in [
 ('62_scan093_L828_values_and_invariants.png',(330,1538,1660,1835),2),
 ('62_scan093_L828_ratios.png',(325,1822,1660,1963),2),
 ('62_scan093_L828_J_order.png',(1160,1425,1665,1570),5)
]:
 c=ImageEnhance.Contrast(im.crop(box)).enhance(1.5)
 c.resize((c.width*factor,c.height*factor),Image.Resampling.LANCZOS).save(root/'crops'/name)
