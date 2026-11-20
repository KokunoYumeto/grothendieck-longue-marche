from pathlib import Path
from PIL import Image, ImageEnhance
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/62_scan096.jpg')
print(im.size)
for name,box,factor in [
 ('62_scan096_L831_dn_formula.png',(405,817,1120,1007),4),
 ('62_scan096_L831_preceding_formulas.png',(408,526,1055,815),4)
]:
 c=ImageEnhance.Contrast(im.crop(box)).enhance(1.5)
 c.resize((c.width*factor,c.height*factor),Image.Resampling.LANCZOS).save(root/'crops'/name)
