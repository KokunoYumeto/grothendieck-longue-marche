from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json

OUT = Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_072/R2')
SOURCE = Path('/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan072.jpg')
specs = [
 ('01_repeat_marks', [1060,175,1625,365], 0, 'Two adjacent repetition signs after quand; following la.'),
 ('02_en_forme', [280,275,980,465], 0, 'Opening definition en forme and any final punctuation.'),
 ('03_definition_capital_orders', [810,458,1395,675], 0, 'Overworked initial C, family F and two order signs.'),
 ('04_tout_satisfait', [760,565,1668,770], 0, 'Live/deleted state of tout and lettering of satisfait/satisfont.'),
 ('05_pleine_leader', [1190,370,1650,555], 0, 'Bracketed pleine, underline and distinct insertion leader.'),
 ('06_quelc', [1220,715,1668,905], 0, 'Abbreviation after sup and its punctuation.'),
 ('07_correspond', [440,845,1668,1025], 0, 'Line-broken s’en corre-spond and insertion attachment.'),
 ('08_mappings_bar', [530,905,1560,1110], 0, 'Both added correspondence signs, M prime and bar over F.'),
 ('09_oblique_sup_note', [27,860,525,1415], -44, 'Complete oblique arbitrary/finite sup note and local cancellation.'),
 ('10_b_correction', [530,1200,1510,1510], 0, 'Curved mark after M, deleted clause and full raised qu’on va formuler.'),
 ('11_c_note', [1030,1355,1670,1635], 0, 'Instruction, circled c, fixed subdivision, mapping, cancellations and pointer.'),
 ('12_diagram_qualifier', [1180,1655,1590,1820], 0, 'Preposition and family glyph to right of first C6 diagram.'),
 ('13_symetrique_note', [25,1625,325,1900], -44, 'Oblique symétrique en note and intersecting vertical rule.'),
 ('14_a_line_ending', [1230,1860,1640,1995], 0, 'H, family glyph and final avec/ou in C6(a).'),
 ('15_b_note', [1140,1940,1668,2240], 0, 'Complete C6(b) marginal text, worked letters, terminal G and double rule.'),
 ('16_bottom_lines', [285,2220,1668,2359], 0, 'Final two body lines, underlines and struck ending at sheet edge.'),
 ('17_lower_slanted_note', [28,2140,410,2359], -28, 'Full slanted sur la sous-figure G de F and its placement.'),
 ('18_first_diagram_points', [480,1560,950,1895], 0, 'Previously uninspected detached marks left of the first diagram; check the diagram geometry with the adjoining Soit line.'),
]
im=Image.open(SOURCE)
records=[]
for name,bbox,rotation,reason in specs:
    crop=ImageOps.autocontrast(im.crop(bbox), cutoff=0)
    if rotation:
        crop=crop.rotate(rotation, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    scale=2500/crop.width
    crop=crop.resize((2500, round(crop.height*scale)), Image.Resampling.LANCZOS)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))
    path=OUT/'crops'/f'{name}.jpg'
    crop.save(path, quality=94, subsampling=0)
    records.append(dict(path=str(path),source=str(SOURCE),bbox=bbox,scale=scale,rotation=rotation,reason=reason,transformations='Autocontrast cutoff 0; rotate with BICUBIC and white expansion; resize to 2500 px across with LANCZOS; UnsharpMask radius 1.2 percent 110 threshold 3; JPEG quality 94.'))
(OUT/'crops_metadata.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(f'Created {len(records)} crops from the assigned whole image.')
