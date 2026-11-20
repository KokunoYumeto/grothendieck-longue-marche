from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

ROOT = Path('/workspace/scratch/94548b74fbe0/out/readers/003/C')
SOURCE = Path('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-01_81_scan003.jpg')
SPECS = [
    ('01_title_insertion.png', [180, 14, 1005, 150], 0, 2800, 'Inserted orientée and its attachment within the heading'),
    ('02_title_category.png', [1010, 70, 1680, 210], 0, 2600, 'Terminal of isotopique(s) and cat. punctuation'),
    ('03_morphism.png', [180, 165, 1150, 280], 0, 3000, 'Morphism noun, horizontal sign, target C and spécial'),
    ('04_zero_value.png', [1200, 405, 1745, 520], 0, 2600, 'Overwritten f(0) value with f(1) and f(infinity) context'),
    ('05_critical_conditions.png', [440, 490, 1510, 665], 0, 3200, 'avec insertion, overwritten memberships and cancelled finite value set'),
    ('06_ramification.png', [1270, 580, 1775, 705], 0, 2600, 'en z/en un z and final punctuation in ramification parenthesis'),
    ('07_respectivement.png', [1015, 905, 1390, 1010], 0, 2500, 'Abbreviated resp raised terminal'),
    ('08_oblique_note.png', [15, 930, 430, 1355], -40, 3000, 'Complete oblique normalization note'),
    ('09_fraction_cancel.png', [195, 1210, 715, 1375], 0, 2600, 'Cancelled Q(z) beside P prime numerator'),
    ('10_nb_cancel_word.png', [215, 1635, 665, 1740], 0, 2500, 'Cancelled au/ou after P(z)=Q(z)'),
    ('11_question_insert.png', [390, 1860, 1245, 2030], 0, 3000, 'd’où/donc and insertion avec/donc P prime = Q prime with final hook'),
    ('12_cancelled_start.png', [215, 2040, 665, 2130], 0, 2600, 'Cancelled first attempt before Prenons'),
    ('13_example_opening.png', [235, 2085, 1555, 2185], 0, 3200, 'Q(T)=1 and cond superscript ns'),
    ('14_degree_and_factor.png', [590, 2125, 1380, 2250], 0, 3000, 'Consequence insertion and P(T)=T P_0(T) overwritten letters'),
    ('15_example_ending.png', [220, 2315, 1515, 2455], 0, 3200, 'certes and cancelled P(T)=T squared at bottom edge'),
    ('16_sideways_note.png', [16, 1480, 244, 2450], -90, 3800, 'Sideways calculation, first three baselines and beginning of continuation'),
    ('17_sideways_continuation.png', [195, 1740, 300, 2450], -90, 3400, 'Lowest two sideways baselines, beyond the baseline clipped in crop 16'),
    ('18_condition_punctuation.png', [1370, 915, 1775, 1020], 0, 2700, 'Punctuation between the three f values in the degree parenthesis'),
    ('19_nb_insertion_punctuation.png', [420, 1485, 850, 1580], 0, 2600, 'Semicolon and trailing punctuation in inserted pour P(z);Q(z) nonzero'),
]

im = Image.open(SOURCE)
records = []
for name, bbox, rotation, width, purpose in SPECS:
    out = im.crop(tuple(bbox))
    if rotation:
        out = out.rotate(rotation, expand=True, resample=Image.Resampling.BICUBIC, fillcolor='white')
    out = ImageOps.autocontrast(out)
    out = out.resize((width, round(out.height * width / out.width)), Image.Resampling.LANCZOS)
    out = out.filter(ImageFilter.UnsharpMask(radius=1.1, percent=120, threshold=3))
    out.save(ROOT / name)
    records.append({'path': name, 'bbox': bbox, 'rotation': rotation, 'purpose': purpose})
(ROOT / 'crop_index.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(records, ensure_ascii=False))
