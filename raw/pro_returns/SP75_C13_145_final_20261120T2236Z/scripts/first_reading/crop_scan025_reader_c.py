from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

root = Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
img = Image.open(root / 'packets/145_scan025/page.jpg')
out = root / 'edition/crops'
items = [
    ('opening', [270,35,1655,242], 0, 'Complete opening two lines: M0863, gauche/pres, el/elt, alpha indices and hat Z; header11.'),
    ('action_insertion', [275,235,1645,485], 0, 'On passe de u a int(g) circle u; inserted gardant p et en; replacement gg_i.'),
    ('composition_first', [295,600,1615,820], 0, 'Both complete preliminary formula lines and all four tiny inverse-exponent states; ou and donc.'),
    ('formula23', [240,810,1265,1018], 0, 'Entire (23), donc/dou, both tiny inverse-exponent states and cancelled overbrace annotation.'),
    ('extension_definition', [240,990,1630,1345], 0, 'Opening extension definition, all group hats, cancelled par le couple/groupe, M0864 and deleted couples.'),
    ('structure_via', [235,1250,1665,1685], 0, 'Systeme de g_i, explicitent, inserted via(21), complete structure a lacets phrase and later group hats.'),
    ('mapping_pi', [255,1695,1540,1845], 0, 'Cancelled E and hatted Pi; full gamma_i mapping and following et on aura.'),
    ('formula24', [260,1810,1585,2015], 0, 'Whole (24), baseline cancellation, inserted-and-cancelled expression, surviving inserted expression M0865 and its connector.'),
    ('cocycle', [250,1915,1665,2175], 0, 'Full cocycle statement: cancelled group replaced above, produit du groupe/opposé au groupe, final Pi case/hat and numeric exponent.'),
    ('margin_nb', [20,1250,370,2005], -47, 'Entire diagonal NB note, underline, group versus ensemble, complete system tuple and relation22.'),
    ('kernel_final', [25,2120,1680,2358], 0, 'Cancelled groupe, full final kernel sentence, all local Pi forms and final product M0866; footer24.'),
]
manifest = []
for name, box, rotation, purpose in items:
    path = out / f'145_scan025_{name}.png'
    if path.exists():
        raise RuntimeError(f'Refusing to remake {path}')
    im = ImageOps.autocontrast(img.crop(box), cutoff=0.5)
    if rotation:
        im = im.rotate(rotation, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    im = im.resize((2800, round(im.height * 2800 / im.width)), Image.Resampling.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=120, threshold=3))
    im.save(path)
    manifest.append({'name': name, 'crop': f'crops/{path.name}', 'box': box, 'rotation_degrees': rotation, 'purpose': purpose})
dest = root / 'edition/reader_reports/145_scan025_crop_boxes.json'
dest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(f'Saved {len(manifest)} crops and {dest}')
