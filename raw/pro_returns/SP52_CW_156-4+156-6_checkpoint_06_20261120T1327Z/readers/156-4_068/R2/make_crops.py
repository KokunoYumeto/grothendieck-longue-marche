from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

OUT = Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_068/R2')
SRC = Path('/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans')
specs = [
 ('01_cancelled_opening', 'a', [280,35,1240,220], 'Cancelled first line and unfinished quotation; next line included.'),
 ('02_minimale', 'a', [315,205,680,475], 'Internal letters of minimale; surrounding text lines included.'),
 ('03_celles_telles', 'a', [690,205,1200,465], 'First letter of celles/telles in the parenthesis; surrounding text included.'),
 ('04_cancelled_sappelle', 'a', [480,300,930,565], 'Cancelled s\u2019appelle and final short word; preceding and following context included.'),
 ('05_cosup_point', 'a', [320,725,1330,1025], 'Separate low mark and local spelling of cosup/p; surrounding line included.'),
 ('06_bijection', 'a', [325,800,690,1125], 'Raised letter and complete bijection word; adjacent line context included.'),
 ('07_saturees_ending', 'a', [1180,805,1670,1125], 'Terminal strokes of satur\u00e9es after parties; surrounding text included.'),
 ('08_sur', 'a', [315,1010,705,1230], 'Small word before elles; following line included.'),
 ('09_m0_insertion', 'b', [200,200,630,445], 'Inserted M0 and its separate oblique leader, with prior text line.'),
 ('10_ou_deleted_de', 'b', [625,235,1055,430], 'Accent or stroke above ou, cancelled de, and F0; prior line included.'),
 ('11_cancelled_on_definit', 'b', [1300,205,1665,500], 'Cancelled On d\u00e9finit group at right edge; prior and subsequent context included.'),
 ('12_cancelled_application', 'b', [300,405,1380,585], 'Entire cancelled L\u2019application line including last d/e group; following line included.'),
 ('13_desidentifie', 'b', [315,430,1150,645], 'Long verb, Sigma and short de/\u00e0; surrounding line included.'),
 ('14_cancelled_letter_ses_deux', 'b', [1020,410,1590,635], 'Cancelled capital before ses deux; surrounding line included.'),
 ('15_realisations', 'b', [300,475,990,740], 'R\u00e9alisations and opening parenthesis, with surrounding lines.'),
 ('16_partie_first_p', 'b', [985,480,1440,725], 'Partie(s), first power-set P and whole following M parentheses; adjacent line context.'),
 ('17_second_p', 'b', [315,550,690,800], 'Second power-set P and complete parentheses; surrounding lines included.'),
 ('18_anti_revision', 'b', [935,770,1550,1035], 'Entire anti compound, overlapping correction, and d\u2019; previous and following lines included.'),
]
manifest = []
for name, half, bbox, reason in specs:
    source = SRC / f'J156-4-09_156-4_scan068_{half}.jpg'
    im = Image.open(source).crop(bbox)
    scale = 2400 / im.width
    im = ImageOps.autocontrast(im).resize((2400, round(im.height * scale)), Image.Resampling.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))
    path = OUT / 'crops' / f'{name}.jpg'
    im.save(path, quality=94, subsampling=0)
    manifest.append(dict(path=str(path), source=str(source), bbox=bbox, scale=scale, rotation=0, reason=reason, transformations=['PIL autocontrast', 'PIL LANCZOS resize to 2400 px width', 'PIL UnsharpMask radius=1.2 percent=110 threshold=3', 'JPEG quality=94 subsampling=0']))
(OUT / 'crop_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(f'Created {len(manifest)} own crops; none has yet been viewed.')
