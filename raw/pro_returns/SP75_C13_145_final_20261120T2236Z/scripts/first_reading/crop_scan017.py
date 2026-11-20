from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
source=Image.open(root/'packets/145_scan017/page.jpg')
out=root/'edition/crops'
places=[
 ('01_initial_deletion',[632,135,1049,202]),
 ('02_first_tuple',[233,218,836,300]),
 ('03_path_l_slash',[195,302,732,397]),
 ('04_product_insertion',[350,386,996,508]),
 ('05_quotation_marks',[246,478,1640,588]),
 ('06_gauche_underline',[1336,570,1651,661]),
 ('07_etale_inserted_u',[261,745,861,879]),
 ('08_fibre_map',[1107,825,1648,942]),
 ('09_sigma_lists',[526,1052,1287,1156]),
 ('10_sigma_i_lambda_insertion',[740,1128,1638,1263]),
 ('11_bar_p_sigma',[245,1280,1064,1379]),
 ('12_lunique_celui_des',[1113,1232,1570,1350]),
 ('13_stable_fixed_points',[931,1325,1566,1449]),
 ('14_symmetry_formula',[245,1452,1240,1572]),
 ('15_au_plan_fixant',[258,1559,1115,1660]),
 ('16_zero_one_ou_infty',[1129,1533,1515,1621]),
 ('17_ne_passant_gamma_insertion',[1245,1618,1665,1752]),
 ('18_pas_au_designant',[246,1735,1610,1848]),
 ('19_autour_des',[869,1830,1378,1936]),
 ('20_quarts',[252,2044,850,2152]),
 ('21_repeated_numbers',[844,1942,1085,2045]),
 ('22_numbered_relation',[491,2120,1012,2217]),
 ('23_question_on_peut',[240,2184,1584,2290]),
 ('24_footer',[28,2274,102,2345]),
]
manifest={}
for stem, box in places:
    name='145_scan017_'+stem
    im=ImageOps.autocontrast(source.crop(box))
    w,h=im.size
    im=im.resize((2800,round(h*2800/w)),Image.Resampling.LANCZOS)
    im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
    im.save(out/f'{name}.png')
    manifest[name]=box
(out/'145_scan017_crop_boxes.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
