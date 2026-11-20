from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json

base = Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
im = Image.open(base/'packets/145_scan003/page.jpg')
specs = [
 ('opening', [165,40,1300,162], 0, 2800),
 ('margin_u_l0', [1060,30,1533,475], -45, 2600),
 ('margin_et_pas', [33,649,210,826], -45, 2300),
 ('margin_beta_gamma', [30,1003,356,1496], -60, 2800),
 ('avec_definition', [266,1110,1130,1250], 0, 2600),
 ('second_relation_rewrite', [315,1318,985,1475], 0, 2700),
 ('peut_se_recrire', [278,1370,1505,1610], 0, 2900),
 ('remplace_en', [293,1863,590,1952], 0, 2300),
 ('en_lui_appliquant', [315,1870,1048,2001], 0, 2800),
 ('final_formula', [441,1911,1455,2057], 0, 3000),
 ('final_corrections', [309,2006,1455,2203], 0, 3000),
]
saved = []
for name, box, angle, width in specs:
    crop = ImageOps.autocontrast(im.crop(box).convert('RGB'))
    if angle:
        crop = crop.rotate(angle, Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))
    rel = f'crops/145_scan003_{name}.png'
    crop.save(base/'edition'/rel)
    saved.append({'name': name, 'box':box, 'crop':rel, 'rotation':angle})
(base/'edition/reader_reports/145_scan003_crop_manifest.json').write_text(json.dumps(saved, indent=2)+'\n')
print(json.dumps(saved, indent=2))
