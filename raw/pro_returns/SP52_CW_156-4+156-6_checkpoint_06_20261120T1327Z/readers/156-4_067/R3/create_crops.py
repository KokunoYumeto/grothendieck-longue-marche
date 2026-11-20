from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json

OUT = Path(__file__).parent
SOURCE = Path('/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan067.jpg')
places = [
 ('01_top_left', (430,105,940,303), 0, 'Top two operator spellings; family and M alphabets, primes.'),
 ('02_top_right', (1150,20,1668,273), 0, 'Both disjoint endings, relation to Phi, inserted inclusion and closing strokes.'),
 ('03_top_inserted_row', (825,270,1665,390), 0, 'Inserted third equality and its enclosure/leader; operator spelling.'),
 ('04_cancelled_block', (280,390,1660,615), 0, 'Cancelled prose and three formula groups, including separate phi and corrected subscript.'),
 ('05_left_note', (35,685,475,925), -17, 'Slanted left note, final word and linking arrow.'),
 ('06_braced_display', (435,680,1210,850), 0, 'Barred F, double arrow and low point before family F.'),
 ('07_right_note', (1070,600,1668,950), 0, 'Right NB, Stable ending, underline and enclosure/connecting line.'),
 ('08_double_prime_definitions', (505,860,1565,1095), 0, 'Both cosup/cosupp and supp spellings; def accents.'),
 ('09_on_a', (280,1110,1100,1240), 0, 'Short word after On a and inclusion.'),
 ('10_sup_passage', (770,1110,1650,1310), 0, 'Sup/Supp, following punctuation, and passage a/colon une.'),
 ('11_contient_sous_figure', (285,1240,800,1445), 0, 'Cancelled contient Phi and live singular sous-figure.'),
 ('12_union', (815,1290,1580,1445), 0, 'Overwritten M before barred Phi, bars and dotted i indices, comma before alors.'),
 ('13_lower_cosup_display', (290,1450,1655,1680), 0, 'Both lower equations, corrected subscript, pre-X deletion and tt.'),
 ('14_ramene_section', (310,1650,1655,1850), 0, 'ramene/revenu and separate section/question mark.'),
 ('15_first_saturee', (305,1790,1635,2040), 0, 'Heading underline, raised family F0, overwritten M and parenthetical p. r. a.'),
 ('16_second_saturee', (300,2010,1655,2260), 0, 'Second saturee, inserted M0, support/cosupport, mutuellement and terminal par cancellation.'),
]
im = Image.open(SOURCE)
records = []
for name, bbox, rotation, reason in places:
    crop = im.crop(bbox)
    if rotation:
        crop = crop.rotate(rotation, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    scale = 2600 / crop.width
    crop = crop.resize((2600, round(crop.height*scale)), Image.Resampling.LANCZOS)
    crop = ImageOps.autocontrast(crop).filter(ImageFilter.UnsharpMask(radius=1.3, percent=120, threshold=3))
    path = OUT / 'crops' / (name+'.jpg')
    crop.save(path, quality=94, subsampling=0)
    records.append(dict(path=str(path), source=str(SOURCE), bbox=list(bbox), scale=scale, rotation=rotation, reason=reason))
(OUT/'crop_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([dict(path=x['path'],bbox=x['bbox'],scale=x['scale'],rotation=x['rotation']) for x in records],indent=2))
