from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import json
root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work');im=Image.open(root/'packets/145_scan012/page.jpg')
boxes={
 'cancelled_relation':[515,605,895,720],
 'cancelled_subgroups':[275,705,1610,830],
 'cancelled_image_formula':[510,825,985,935],
 'cancelled_deja_int_modulo':[260,950,1550,1080],
 'cancelled_multiplication':[260,1080,1610,1200],
 'cancelled_donnee':[265,1200,945,1320],
 'des_plus_jolis':[345,1395,825,1500],
 'sous_prefix':[1160,1330,1640,1480],
 's3_extension':[420,1495,580,1620],
 'aut_lac_insertion':[690,1430,1245,1605],
 'sigma_rho_and_struck_example':[1190,1590,1635,1725],
 'groupes_ramification':[285,1810,1640,1935],
 'canoniqt_isomorphes':[285,1920,1510,2050],
 'final_autom_insertion':[1000,2180,1658,2285],
 'final_classe_mod':[310,2265,1065,2351],
 'final_carre_insertion':[1045,2255,1658,2351],
 'manuscript_number_eleven':[25,2260,145,2351]
}
for name,box in boxes.items():
 c=ImageOps.autocontrast(im.crop(box).convert('RGB'),cutoff=.5)
 c=c.resize((2800,round(c.height*2800/c.width)),Image.Resampling.LANCZOS)
 c=c.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
 c.save(root/f'edition/crops/145_scan012_{name}.png')
(root/'edition/reader_reports/145_scan012_crop_boxes.json').write_text(json.dumps(boxes,indent=2))
