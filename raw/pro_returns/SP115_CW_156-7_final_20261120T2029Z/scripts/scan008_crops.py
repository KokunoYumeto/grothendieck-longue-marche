from pathlib import Path
import json
from PIL import Image, ImageOps, ImageFilter

ROOT = Path('/workspace/scratch/ddf8babdc42e')
SOURCE = ROOT / 'source/SP115_CW_156-7_scans/H156-01_156-7_scan008.jpg'
SPECS = [
    ('opening_insertion', (1040, 190, 1640, 350), 0, 2800),
    ('des_ending', (1080, 415, 1585, 505), 0, 2600),
    ('facultatifs_quotes', (1090, 330, 1530, 438), 0, 2600),
    ('disjoints', (255, 745, 790, 825), 0, 2600),
    ('definition_formula', (510, 770, 1450, 905), 0, 3000),
    ('ailleurs', (1250, 900, 1650, 990), 0, 2600),
    ('universal_formula', (515, 985, 1440, 1085), 0, 3000),
    ('interpretation', (255, 1085, 1610, 1170), 0, 3000),
    ('M_formula', (535, 1200, 1660, 1407), 0, 3000),
    ('NB', (860, 1365, 1670, 1630), 0, 3000),
    ('slanted_margin', (20, 1460, 630, 1980), -36, 3000),
    ('At_heading', (230, 1625, 1585, 1742), 0, 3000),
    ('At_K', (280, 1720, 1055, 1840), 0, 2800),
    ('At_supposons', (1060, 1698, 1580, 1840), 0, 2600),
    ('At_display', (285, 1815, 1540, 1945), 0, 3000),
    ('At_conclusion', (300, 1925, 1390, 2045), 0, 3000),
    ('Cor_formula', (470, 2025, 1555, 2175), 0, 3000),
    ('Cor_final', (565, 2150, 1510, 2305), 0, 3000),
]

im = Image.open(SOURCE)
manifest = {'scan': '008', 'source': str(SOURCE), 'source_size': list(im.size), 'crops': [],
            'window_corrections_before_decision': {
                'definition_formula': 'Top extended from 790 to 770 because the raised label ascender touched the initial crop edge.',
                'M_formula': 'Top extended from 1220 to 1200 to include the complete upper brace.',
                'NB': 'Top extended from 1380 to 1365 to include the complete raised précédents insertion.'}}
for name, box, angle, width in SPECS:
    out = ROOT / 'out/crops' / f'scan008_{name}.png'
    crop = ImageOps.autocontrast(im.crop(box), cutoff=0.4)
    if angle:
        crop = crop.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.3, percent=120, threshold=3))
    out.parent.mkdir(parents=True, exist_ok=True)
    crop.save(out)
    manifest['crops'].append({
        'name': name, 'file': str(out), 'box': list(box),
        'rotation_degrees_Pillow': angle, 'rotation_resample': 'BICUBIC',
        'rotation_expand': True, 'rotation_fillcolor': 'white',
        'output_width': width, 'output_size': list(crop.size),
        'resize_resample': 'LANCZOS', 'autocontrast_cutoff': 0.4,
        'unsharp_mask': {'radius': 1.3, 'percent': 120, 'threshold': 3},
        'operation_order': ['crop original', 'autocontrast', 'rotate if nonzero', 'resize', 'unsharp mask']
    })
manifest_path = ROOT / 'out/review/scan008_crop_manifest.json'
manifest_path.parent.mkdir(parents=True, exist_ok=True)
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(f'{len(SPECS)} crops; {manifest_path}')
