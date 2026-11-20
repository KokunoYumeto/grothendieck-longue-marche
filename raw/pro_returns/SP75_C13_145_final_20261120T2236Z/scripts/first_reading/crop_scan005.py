from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
src=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work/packets/145_scan005/page.jpg')
out=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work/edition/crops')
img=Image.open(src)
boxes={
'145_scan005_01_title':[255,75,1535,263],
'145_scan005_02_margin_extension':[20,130,250,445],
'145_scan005_03_margin_sign':[22,445,77,510],
'145_scan005_04_endomorphism_symbol':[840,527,1105,626],
'145_scan005_05_same_relation':[240,700,575,795],
'145_scan005_06_autom_abbreviation':[1360,685,1642,794],
'145_scan005_07_donc_struck':[195,1128,828,1249],
'145_scan005_08_inner_insertion':[1070,1230,1655,1376],
'145_scan005_09_exchange_same_sorte':[208,1410,1130,1550],
'145_scan005_10_group_symbol':[885,1775,1380,1940],
'145_scan005_11_proposal':[780,1920,1580,2036],
'145_scan005_12_lacets_caractere':[200,2005,1660,2200],
'145_scan005_13_symmetric_positive':[1000,2180,1380,2305],
}
for name,box in boxes.items():
 im=ImageOps.autocontrast(img.crop(box))
 if name.endswith('margin_extension'): im=im.rotate(-38,expand=True,fillcolor='white')
 w=2400
 im=im.resize((w,round(im.height*w/im.width)),Image.Resampling.LANCZOS)
 im=im.filter(ImageFilter.UnsharpMask(radius=1.25,percent=110,threshold=3))
 im.save(out/(name+'.png'))
(out/'145_scan005_crop_boxes.json').write_text(json.dumps(boxes,indent=2)+'\n')
print(f'Created {len(boxes)} crops')
