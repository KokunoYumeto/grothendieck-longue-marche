from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

root = Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
source = root / 'packets/145_scan022/page.jpg'
out = root / 'edition/crops'
out.mkdir(parents=True, exist_ok=True)
items = [
    ('formula10', [210, 15, 1040, 375], 0, 'Entire system (10), all cancelled signs, disputed indices and exponents, and final punctuation; adjacent handwritten 9.'),
    ('upper_margin', [22, 181, 418, 850], -37, 'Complete slanted marginal addition, including ajouter/écrire, relations, generator count and punctuation.'),
    ('question', [240, 365, 1610, 680], 0, 'Complete three-line question after (10), including the final que non.'),
    ('path_negative', [240, 680, 1605, 995], 0, 'Quant à relever through également; dotted tau, path phrase and disputed negative/singular choice.'),
    ('demblee_prefere', [230, 980, 1620, 1230], 0, 'Naturels, d’emblée and je préfère considérer through sous-groupe d’isotropie.'),
    ('gamma_couples_display', [235, 1215, 1635, 1625], 0, 'Gamma identity and ornate group sign M0847, est formé, couples, cancelled On, and complete tilde-dot-sigma display.'),
    ('releves_hom', [240, 1620, 1600, 1945], 0, 'Qui sont relevés, lacet trivial en P, and On trouve un hom.'),
    ('formula11', [330, 1830, 1405, 2045], 0, 'Complete (11), both ornate group signs M0848–M0849, brace, map image and punctuation.'),
    ('formula12', [345, 2120, 1380, 2220], 0, 'Complete (12), plain arrow, unpointed sigma and ornate group sign M0850.'),
    ('lower_margin_footer', [20, 2200, 1450, 2358], 0, 'On pose display, lower marginal text and cancelled rho, dotted live rho equality, handwritten footer 21.'),
]
img = Image.open(source)
manifest = []
for name, box, rotation, purpose in items:
    dest = out / f'145_scan022_{name}.png'
    if dest.exists():
        raise RuntimeError(f'Refusing to remake existing crop: {dest}')
    cropped = ImageOps.autocontrast(img.crop(box), cutoff=0.5)
    if rotation:
        cropped = cropped.rotate(rotation, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    cropped = cropped.resize((2800, round(cropped.height * 2800 / cropped.width)), Image.Resampling.LANCZOS)
    cropped = cropped.filter(ImageFilter.UnsharpMask(radius=1.2, percent=120, threshold=3))
    cropped.save(dest)
    manifest.append({'name': name, 'crop': f'crops/{dest.name}', 'box': box, 'rotation_degrees': rotation, 'purpose': purpose})
target = root / 'edition/reader_reports/145_scan022_crop_boxes.json'
target.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(f'Saved {len(manifest)} crops and {target}')
