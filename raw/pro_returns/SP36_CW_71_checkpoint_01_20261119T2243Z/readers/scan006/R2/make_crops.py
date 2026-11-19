from pathlib import Path
from PIL import Image, ImageOps
import json

ROOT = Path('/workspace/scratch/17347c1714f0')
OUT = ROOT / 'out/readers/scan006/R2'
SRC = ROOT / 'source/SP36_CW_71_scans'

# One crop for each place left unsettled by the single viewing of each half.
# Angles use PIL's convention: a negative angle rotates clockwise.
SPECS = [
    ('01_script_x', 'a', (242, 68, 376, 165), 0, 2400, 'Opening script capital: calligraphic/script form'),
    ('02_first_de', 'a', (260, 192, 410, 272), 0, 2400, 'Opening first de: cancelled final letter'),
    ('03_second_de', 'a', (672, 198, 792, 270), 0, 2400, 'Opening second de: cancelled final letter'),
    ('04_sur', 'a', (969, 175, 1105, 278), 0, 2400, 'Opening parenthesis: sur or via'),
    ('05_cancelled_heading', 'a', (802, 326, 1524, 433), 0, 2800, 'Cancelled heading: L\u2019application naturelle'),
    ('06_cancelled_de', 'a', (819, 450, 947, 536), 0, 2400, 'Small cancelled word before the cancelled map'),
    ('07_overwritten_operator', 'a', (1161, 516, 1328, 650), 0, 2600, 'Operator overwritten by the coproduct in parentheses'),
    ('08_coproduct_suffix', 'a', (973, 694, 1250, 824), 0, 2800, 'Second row: parenthesized letter beneath the coproduct'),
    ('09_side_formula_gloss', 'a', (1350, 673, 1665, 895), 0, 2800, 'Side formula: first subscript, script subscript, parallel strokes, Im, arrow and gloss'),
    ('10_drawing_ticks', 'a', (187, 477, 531, 766), 0, 2800, 'Small transverse strokes on the three inner branches and all nearby labels'),
    ('11_imm', 'a', (431, 1090, 886, 1213), 0, 2800, 'Abbreviation before ferm\u00e9e'),
    ('12_inserted_superscripts', 'b', (918, 327, 1246, 431), 0, 2800, 'Raised marks and insertion bracket on the small U-prime replacement formula'),
    ('13_slanted_margin', 'b', (25, 385, 260, 713), -45, 2800, 'Slanted three-line verification note'),
    ('14_replaced_condition', 'b', (282, 503, 845, 673), 0, 3000, 'Inserted dotted K-star condition and cancelled original condition'),
    ('15_cancelled_parenthesis', 'b', (851, 487, 1294, 634), 0, 2800, 'Cancelled parenthesis, its raised final stroke and following quantifier'),
    ('16_sufficient_condition', 'b', (1185, 640, 1618, 766), 0, 3000, 'Scribbled K after il suffit que and the live word before K-prime'),
    ('17_page_number', 'b', (95, 1008, 205, 1139), 0, 2400, 'Own page numeral above the archival numeral'),
]

manifest = []
for name, half, box, angle, width, place in SPECS:
    source = SRC / f'J71-01_71_scan006_{half}.jpg'
    im = Image.open(source).convert('L').crop(box)
    im = ImageOps.autocontrast(im)
    if angle:
        im = im.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True, fillcolor=255)
    rotated_size = im.size
    scale = width / im.width
    height = round(im.height * scale)
    im = im.resize((width, height), Image.Resampling.LANCZOS)
    target = OUT / f'{name}.jpg'
    im.save(target, format='JPEG', quality=97, subsampling=0)
    manifest.append({
        'file': str(target), 'source': str(source), 'box': list(box),
        'rotation': angle, 'output_width': width, 'output_height': height,
        'scale': scale, 'rotated_dimensions': list(rotated_size),
        'processing': 'grayscale; autocontrast; rotation if nonzero; LANCZOS enlargement; JPEG quality 97; no sharpening',
        'place': place, 'observed': None,
    })
(OUT / 'crop_manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')
print(f'Created {len(manifest)} grayscale JPEG crops.')
