from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

root = Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
source = Image.open(root/'packets/145_scan013/page.jpg')
output = root/'edition/crops'
output.mkdir(parents=True, exist_ok=True)
places = [
    ('01_opening', [331,18,1649,91]),
    ('02_pas_de_carre', [211,73,618,140]),
    ('03_on_doit_le', [598,71,1121,171]),
    ('04_first_epsilon_insertion', [325,154,1677,284]),
    ('05_et_de_bar_and_definitions', [230,143,746,516]),
    ('06_on_deleted_inserted', [211,511,759,641]),
    ('07_ecrivant_au_lieu_de', [638,553,1430,645]),
    ('08_ss_je_ecris', [862,650,1671,754]),
    ('09_underbrace_scope', [453,941,1117,1061]),
    ('10_deleted_expansion', [551,1147,1336,1306]),
    ('11_inserted_struck_inverse', [879,1273,1128,1365]),
    ('12_aussi_multipliant', [880,1328,1645,1455]),
    ('13_deleted_annotated_relation', [416,1436,1165,1641]),
    ('14_ie_deleted_prefix', [214,1637,1155,1748]),
    ('15_margin_prends_alpha', [1232,1720,1615,1842]),
    ('16_rejected_product', [288,1870,1586,1991]),
    ('17_cancelled_factors_ok', [291,1980,1444,2097]),
    ('18_footer', [31,2277,113,2346]),
]
manifest = {}
for name, box in places:
    name = '145_scan013_' + name
    im = ImageOps.autocontrast(source.crop(box))
    w, h = im.size
    im = im.resize((2800, round(h*2800/w)), Image.Resampling.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=120, threshold=3))
    im.save(output/f'{name}.png')
    manifest[name]=box
(output/'145_scan013_crop_boxes.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(f'Saved {len(manifest)} scan013 crops and coordinate manifest.')
