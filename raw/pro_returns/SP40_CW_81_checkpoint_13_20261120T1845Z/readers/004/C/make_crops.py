from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
root=Path('/workspace/scratch/94548b74fbe0/out/readers/004/C')
src=Image.open('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-01_81_scan004.jpg')
specs=[
 ('01_top_parenthesis.png',(695,205,1005,355),0,'First eta/gamma and the following brace-like stroke'),
 ('02_xf_equality.png',(145,930,790,1070),0,'Equality versus triple bar after xf_1; complete short line'),
 ('03_cancelled_xf.png',(125,1060,310,1177),0,'Locally struck isolated xf_1'),
 ('04_last_cross_term.png',(930,1210,1260,1430),0,'Cancellation of e_i f_1 and sign of annotation below it'),
 ('05_upside_down_note.png',(475,1395,1100,1595),180,'Entire two-line upside-down note including bounds and unfinished f_i f_1='),
 ('06_upside_down_struck.png',(935,1590,1105,1730),180,'Separate upside-down cancelled product e_1 f_d'),
 ('07_bottom_delta.png',(55,1575,390,1735),0,'Locally struck first delta formula and its terminal character'),
 ('08_right_cancelled_a.png',(1410,412,1865,535),0,'Cancelled predecessor between first case minus and eta'),
 ('09_right_one_alpha.png',(1740,499,2335,615),0,'Sign between 1 and alpha in second case'),
 ('10_right_struck_factor.png',(1350,665,1755,811),0,'Cancelled factor between f_1 e_1 and equals in underlined line'),
 ('11_right_struck_prefix.png',(1350,827,1855,998),0,'Cancelled prefix beside lower cases brace'),
 ('12_right_second_case.png',(1703,914,2375,1020),0,'Second case: eta subscript and following e_1/a_1, locally crossed product'),
 ('13_final_initials.png',(1990,1450,2350,1590),0,'Small initials after signed delta-eta result')
]
manifest=[]
for name,box,rotation,purpose in specs:
 im=src.crop(box)
 if rotation:
  im=im.rotate(rotation,expand=True)
 im=ImageOps.autocontrast(im)
 width=2800
 im=im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS)
 im=im.filter(ImageFilter.UnsharpMask(radius=1.0,percent=110,threshold=3))
 im.save(root/name)
 manifest.append({'path':name,'bbox':list(box),'rotation':rotation,'purpose':purpose})
(root/'crops_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Created',len(manifest),'tight crops in',root)
