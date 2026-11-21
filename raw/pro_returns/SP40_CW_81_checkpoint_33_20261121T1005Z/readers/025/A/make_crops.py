from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import json
base=Path('out/readers/025/A')
source=Path('source/SP40_CW_81_scans/J81-03_81_scan025.jpg')
plan=[
('01_opening_sigma',(780,100,965,220),'C R01 overwritten predecessor, complete live Sigma head/index/minus'),
('02_opening_cap_E',(1000,88,1375,240),'C R02 overwritten relation and R03 E index; complete barred U and endpoint'),
('03_crossed_et_si',(1390,125,1668,225),'C/H crossed et si versus ainsi; live alors endpoint'),
('04_reduced_on_a',(270,250,470,335),'Reduced marks after alors, read as complete on a candidate'),
('05_union_hat_sigma',(805,240,1080,410),'C R04 complete big union and lower limit, plus adjacent hatted Sigma'),
('06_ou_condition',(1190,245,1525,340),'Reduced où and complete i in K subset I'),
('07_pi_edge_deletion',(1208,333,1670,425),'C R05 cancelled edge cluster; Sigma head plus pi and parentheses/punctuation'),
('08_crossed_U_Sigma',(1070,420,1380,525),'C R06 complete crossed U/Sigma cluster and live les/Sigma'),
('09_mut_disjoints',(1370,407,1670,511),'C R07 raised contraction ending/point and complete disjoints endpoint'),
('10_K_replacement',(850,465,1185,650),'Complete raised K setminus braced i, cancelled K and guide/crossing paths'),
('11_prose_sigma',(1210,530,1645,642),'Complete live Sigma plus and parenthetical membership/index/braces'),
('12_determines',(280,555,950,780),'C R08 full word/accent and preceding que descender plus sont'),
('13_signed_pair',(275,780,710,912),'Two independently inspected prose Sigma heads, indices and signs, i.e. and period'),
('14_final_sigma',(1120,870,1300,1025),'Last Sigma complete head, alpha and minus'),
('15_lower_points',(1540,1665,1645,1775),'Small two-point trace, local shape and hand/role uncertainty'),
]
im=Image.open(source)
items=[]
for name,bbox,purpose in plan:
 p=base/'crops'/f'{name}.png'
 assert not p.exists(),f'Never regenerate a viewed crop: {p}'
 c=ImageOps.autocontrast(im.crop(bbox))
 scale=2600/c.width
 c=c.resize((2600,round(c.height*scale)),Image.Resampling.LANCZOS)
 c=c.filter(ImageFilter.UnsharpMask(radius=1,percent=105,threshold=3))
 c.save(p)
 items.append({'path':str(p.relative_to(base)),'source':str(source),'bbox':bbox,'rotation':0,'purpose':purpose,'resize_width':2600,'processing':'PIL autocontrast; LANCZOS; UnsharpMask radius=1 percent=105 threshold=3','viewed':False})
(base/'crop_manifest.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
print(f'Created {len(items)} first and only tight-target crops')
