from pathlib import Path
from PIL import Image, ImageEnhance
root=Path('/workspace/scratch/b0d3bc83132a/IM08_work')
im=Image.open(root/'source/IM08_57-64_scans/62_scan070.jpg')
print(im.size)
for name,box,factor in [
 ('62_scan070_L823_cn_equation.png',(240,1278,1450,1402),3),
 ('62_scan070_L823_target_sign.png',(548,1286,820,1377),10),
 ('62_scan070_L823_moduli.png',(180,1690,1358,1900),3),
 ('62_scan070_L823_dn_identity.png',(1015,1048,1455,1162),6)
]:
 c=ImageEnhance.Contrast(im.crop(box)).enhance(1.5)
 c.resize((c.width*factor,c.height*factor),Image.Resampling.LANCZOS).save(root/'crops'/name)
for name,box,factor in [
 ('62_scan070_L823_plus_comparison.png',(235,1052,920,1145),5),
 ('62_scan070_L823_factorized_plus.png',(1188,1308,1280,1386),20)
]:
 c=ImageEnhance.Contrast(im.crop(box)).enhance(1.5)
 c.resize((c.width*factor,c.height*factor),Image.Resampling.LANCZOS).save(root/'crops'/name)
