from pathlib import Path
from PIL import Image
import json

OUT = Path('/workspace/scratch/17347c1714f0/out/readers/scan003/R3')
SOURCE = Path('/workspace/scratch/17347c1714f0/source/SP36_CW_71_scans/J71-01_71_scan003_a.jpg')
# Each crop is made once, after the whole scan and both supplied halves
# have been viewed once. No OCR or text-recognition operation is used.
JOBS = [
    ('01_borde.png', (655, 42, 988, 140), 0, 'First verbal row: terminal letter of borde/bordes/bords'),
    ('02_overmarks.png', (202, 134, 555, 221), 0, 'Three worked-over signs above the double-primed Gamma entries'),
    ('03_boundary_notation.png', (205, 239, 567, 310), 0, 'First occurrence of recurrent boundary glyph, partial/delta'),
    ('04_endpoint_set.png', (303, 323, 522, 416), 0, 'First member of the two-letter endpoint set'),
    ('05_initial_identity_index.png', (711, 423, 988, 509), 0, 'Initial digit of first union identity with adjacent comparison indices'),
    ('06_primed_identity_index.png', (1033, 432, 1192, 503), 0, 'First single-primed Gamma subscript in first union identity'),
    ('07_identity_right_ends.png', (1209, 424, 1497, 667), 0, 'Terminal boundary glyph in second identity, with adjacent same-glyph comparisons'),
    ('08_drawing.png', (141, 554, 433, 949), -90, 'Sideways drawing: outer subscript and two endpoint marks in small loop'),
    ('09_beside_drawing.png', (444, 729, 666, 833), 0, 'Worked-over superscript and second double-primed Gamma subscript beside drawing'),
    ('10_detached_mark.png', (193, 1055, 322, 1155), 0, 'Detached mark before the final U,C,V list'),
]

im = Image.open(SOURCE)
logs = []
for name, box, rotation, place in JOBS:
    crop = im.crop(box)
    if rotation:
        crop = crop.rotate(rotation, expand=True)
    scale = 2800 / crop.width
    crop = crop.resize((2800, round(crop.height * scale)), Image.Resampling.LANCZOS)
    path = OUT / name
    crop.save(path)
    logs.append({'file': str(path), 'source': str(SOURCE), 'box': list(box),
                 'rotation': rotation, 'output_width': 2800, 'scale': scale,
                 'place': place, 'processing': 'PIL crop, optional quarter-turn rotation, LANCZOS enlargement only'})
(OUT / 'crop_log.json').write_text(json.dumps(logs, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(logs, ensure_ascii=False, indent=2))
