from pathlib import Path
import json
from PIL import Image, ImageOps, ImageFilter

ROOT = Path('/workspace/scratch/94548b74fbe0')
DEST = ROOT / 'out/readers/020/A'
SOURCE = ROOT / 'source/SP40_CW_81_scans/J81-03_81_scan020.jpg'
targets = [
    ('01_first_ring', (1040, 55, 1405, 190), 'C row 1, first Pi_I superscript and neighbouring text'),
    ('02_second_ring', (610, 175, 1180, 285), 'C row 1, second Pi_J superscript and neighbouring word'),
    ('03_deux_clas', (710, 275, 1270, 375), 'C row 2, complete word after les and its endpoint'),
    ('04_paired_intersections', (555, 375, 1350, 520), 'C row 3, complete paired intersections, sigma index and local upper strokes'),
    ('05_cancelled_sigma', (275, 760, 750, 915), 'C row 4, complete cancelled Sigma-index group before U'),
    ('06_voisinage_E', (1170, 740, 1560, 870), 'C row 5, overwritten E, its index, adjoining de and et, punctuation'),
    ('07_nonempty_formulas', (270, 890, 1135, 1040), 'Two complete barred formulas with overwritten predecessors and endpoints'),
    ('08_voit_sait', (1180, 875, 1660, 990), 'C row 10, On verb donc'),
    ('09_cancelled_count_word', (1180, 1010, 1615, 1120), 'C row 6, est en and complete struck word'),
    ('10_parenthesis_opening', (1130, 1135, 1640, 1315), 'Complete ce qui acheve group, accent and q descender'),
    ('11_aussi_ainsi', (260, 1295, 640, 1445), 'C row 11, complete adverb and following la'),
    ('12_dem_par_recurrence', (645, 1290, 1620, 1430), 'C row 7, dem abbreviation and complete following par recurrence sur'),
    ('13_lemma_formula_insertion', (865, 1515, 1540, 1930), 'C rows 1 and 8, complete lemma ring/formula/brace/index and cancelled non vide insertion with guide'),
    ('14_membership_correction', (570, 1885, 1370, 2035), 'C row 9 and cancelled on a, complete Sigma membership expression'),
]
im = Image.open(SOURCE).convert('RGB')
manifest = []
for name, box, purpose in targets:
    crop = im.crop(box)
    scale = 3200 / crop.width
    crop = crop.resize((3200, round(crop.height * scale)), Image.Resampling.LANCZOS)
    crop = ImageOps.autocontrast(crop)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.2, percent=120, threshold=3))
    name = name + '.png'
    crop.save(DEST / name)
    manifest.append({'path': name, 'bbox': list(box), 'coordinate_origin': 'original full scan, upper left', 'rotation': 0, 'purpose': purpose, 'processing': 'PIL crop; LANCZOS to 3200 pixels wide; autocontrast; UnsharpMask(radius=1.2, percent=120, threshold=3)'})
(DEST / 'crop_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(f'Created {len(manifest)} planned local crops. No OCR, image comparison, rendering, or mathematical computation.')
