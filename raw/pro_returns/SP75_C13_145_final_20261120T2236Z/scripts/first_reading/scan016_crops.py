from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import json
r=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
source=Image.open(r/'packets/145_scan016/page.jpg').convert('RGB')
boxes={
'profinis':[230,65,480,175],
'plural_groupoides':[220,165,1645,365],
'on_pourra':[1090,260,1425,360],
'initial_pi_formula':[500,390,1170,620],
'dotted_rho':[210,820,900,945],
'struck_qui':[205,940,725,1035],
'aut_complexes_sigmas':[355,1190,1080,1340],
'echangent_fixent':[1200,1190,1660,1335],
'struck_sur':[195,1340,510,1435],
'sont_resp':[215,1410,500,1520],
'rotations_symetries':[515,1395,760,1505],
'struck_axes':[1245,1395,1375,1505],
'oblique_margin':[15,1200,420,2130],
'au_plan':[780,1590,1420,1685],
'ornamental_s_pair':[890,1660,1330,1880],
'dotted_sigmas_semicolon':[600,1865,1555,2000],
'dotted_tau_extension_label':[205,1970,1515,2095],
'extension_notation':[210,2055,1480,2195],
'final_extension_display':[520,2200,1290,2348],
'manuscript_number_fifteen':[25,2265,105,2345]
}
for name,box in boxes.items():
 im=ImageOps.autocontrast(source.crop(box),cutoff=.5)
 if name=='oblique_margin':im=im.rotate(-45,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 w=3000 if name=='oblique_margin' else 2800
 im=im.resize((w,round(im.height*w/im.width)),Image.Resampling.LANCZOS)
 im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
 im.save(r/'edition/crops'/f'145_scan016_{name}.png')
(r/'edition/reader_reports/145_scan016_crop_boxes.json').write_text(json.dumps(boxes,indent=2)+'\n')
print('Saved twenty scan016 crops; oblique_margin rotated clockwise 45 degrees. Original boxes recorded.')
