from PIL import Image,ImageOps,ImageFilter
from pathlib import Path
import json
r=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
im=Image.open(r/'packets/145_scan007/page.jpg')
bs={
'145_scan007_01_indexed_pi':[929,80,1092,162],
'145_scan007_02_autom_signature':[275,383,1520,585],
'145_scan007_03_group_mod_autom':[239,783,1137,885],
'145_scan007_04_group_formula':[936,867,1405,980],
'145_scan007_05_aux_autom':[1260,1133,1565,1240],
'145_scan007_06_normalise_insertion':[210,1264,1630,1467],
'145_scan007_07_deleted_un_L0':[812,1440,1577,1587],
'145_scan007_08_composition':[776,1570,1482,1675],
'145_scan007_09_multiplier_insertion':[710,1638,1645,1800],
'145_scan007_10_tel_que_colon':[546,2010,928,2122],
'145_scan007_11_final_line_footer':[33,2202,1630,2337]
}
for n,b in bs.items():
 x=ImageOps.autocontrast(im.crop(b))
 w=2600
 x=x.resize((w,round(x.height*w/x.width)),Image.Resampling.LANCZOS)
 x=x.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
 x.save(r/'edition/crops'/(n+'.png'))
(r/'edition/crops/145_scan007_crop_boxes.json').write_text(json.dumps(bs,indent=2)+'\n')
print(len(bs))
