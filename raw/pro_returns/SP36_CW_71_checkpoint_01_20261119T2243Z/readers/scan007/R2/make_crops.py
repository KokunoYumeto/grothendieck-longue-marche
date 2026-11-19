from pathlib import Path
from PIL import Image, ImageOps
import json
root=Path('/workspace/scratch/17347c1714f0/out/readers/scan007/R2')
src=Path('/workspace/scratch/17347c1714f0/source/SP36_CW_71_scans')
specs=[
 ('01_sigma_script.jpg','a',(342,715,590,825),2800,'First standalone Sigma and script X'),
 ('02_main_indices.jpg','a',(457,856,1292,982),3200,'First main object crowded end-index and neighbouring subscript'),
 ('03_overwritten_delta.jpg','a',(1290,848,1530,976),2800,'Third main object initial overwritten triangular mark'),
 ('04_cancelled_suffix.jpg','a',(495,1055,756,1174),2800,'Cancelled suffix after intermediate Sigma(X)'),
 ('05_bottom_relation.jpg','b',(1011,118,1667,241),3200,'Bottom main relation and compressed rightmost index'),
 ('06_lower_top_indices.jpg','b',(857,423,995,628),2800,'Two upper X indices in lower column and link'),
 ('07_lower_cancelled_index.jpg','b',(379,891,708,1001),2800,'Cancelled suffix after lower Sigma subscript'),
 ('08_lower_final_index_hook.jpg','b',(884,696,1031,1007),2800,'Lower final index and vertical hook connector'),
 ('09_lower_cancelled_arrow.jpg','b',(420,992,572,1236),2800,'Crossed lowest vertical arrow and Sigma d prime'),
 ('10_pi_D.jpg','b',(1175,622,1580,755),2800,'Right equality first sign and right-hand D')
]
metadata=[]
for name,half,box,width,place in specs:
 source=src/f'J71-01_71_scan007_{half}.jpg'
 im=Image.open(source).convert('L').crop(box)
 im=ImageOps.autocontrast(im)
 scale=width/im.width
 im=im.resize((width,round(im.height*scale)),Image.Resampling.LANCZOS)
 out=root/name
 im.save(out,quality=97)
 metadata.append({'file':str(out),'source':str(source),'box':list(box),'rotation':0,'scale':scale,'output_width':width,'processing':'grayscale; crop; autocontrast; LANCZOS enlargement; JPEG quality 97','place':place,'observed':''})
(root/'crop_log.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
print('Saved',len(metadata),'crops and reproducible script.')
