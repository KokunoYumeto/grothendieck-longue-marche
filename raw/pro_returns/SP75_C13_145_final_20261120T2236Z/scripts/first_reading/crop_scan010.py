from PIL import Image,ImageOps,ImageFilter
from pathlib import Path
import json
r=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
im=Image.open(r/'packets/145_scan010/page.jpg')
bs={
'145_scan010_01_opening':[300,70,607,145],
'145_scan010_02_margin_upper':[22,111,335,560],
'145_scan010_03_margin_middle':[20,245,642,933],
'145_scan010_04_margin_final':[25,862,301,1177],
'145_scan010_05_condition':[280,321,1564,421],
'145_scan010_06_si_replacement':[277,410,1440,535],
'145_scan010_07_dependent':[939,1180,1629,1308],
'145_scan010_08_autom_ext_first':[349,1298,813,1418],
'145_scan010_09_choice_son':[223,1398,1155,1518],
'145_scan010_10_travaille':[594,1848,1267,1970],
'145_scan010_11_autom_ext_last':[799,1941,1285,2062],
'145_scan010_12_donc_insertion':[866,2089,1522,2240],
'145_scan010_13_footer':[28,2260,86,2341],
}
rot={'145_scan010_02_margin_upper':-36,'145_scan010_03_margin_middle':-39,'145_scan010_04_margin_final':-40}
for n,b in bs.items():
 x=ImageOps.autocontrast(im.crop(b))
 if n in rot:x=x.rotate(rot[n],expand=True,fillcolor='white')
 w=2800 if n.endswith('margin_middle') else 2600
 x=x.resize((w,round(x.height*w/x.width)),Image.Resampling.LANCZOS)
 x=x.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
 x.save(r/'edition/crops'/(n+'.png'))
(r/'edition/crops/145_scan010_crop_boxes.json').write_text(json.dumps(bs,indent=2)+'\n')
print(len(bs))
