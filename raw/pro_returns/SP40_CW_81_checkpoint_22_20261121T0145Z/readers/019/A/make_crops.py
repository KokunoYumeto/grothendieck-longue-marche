"""One planned enlargement per unresolved locus; no OCR or image comparisons."""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

base = Path(__file__).parent
source = Path('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-03_81_scan019.jpg')
plans = [
    ('01_top_endpoint', [1400,65,1692,175], 'First-line 0,1 ending and punctuation at physical edge', []),
    ('02_avec', [250,255,800,355], 'Detached compressed word before card I >= 3', ['R09']),
    ('03_first_u', [550,505,1015,640], 'First U entrance and possible cancelled equality, plus index and signs', ['R10']),
    ('04_lune', [930,735,1555,850], 'l’une / l’un and terminal punctuation with full adjoining words', ['R11']),
    ('05_ona_recurrence', [720,850,1290,950], 'End of récurrence and very small on a', ['R02']),
    ('06_first_union', [490,935,1205,1135], 'First large union form and overwritten lower index', ['R03','R04']),
    ('07_brace_predecessor', [595,1160,980,1290], 'Sigma predecessor and lower index beneath K0', ['R12']),
    ('08_brace_e_index', [680,1360,1270,1480], 'Small final E index on third brace line', []),
    ('09_ona_donc', [250,1480,675,1595], 'Overwritten opening On and following a before donc', ['R05']),
    ('10_ordinal', [260,1765,1045,1875], 'Struck Soit, Au, ordinal and equality punctuation', []),
    ('11_struck_word', [1210,1755,1605,1880], 'Struck word after dans la with complete endpoints', ['R06']),
    ('12_borner_sommer', [345,1990,1120,2110], 'borner, à / colon and sommer', ['R07']),
    ('13_cet', [250,2195,1090,2290], 'soit K1 cet ens., donc', ['R08']),
    ('14_final_display', [595,2240,1520,2362], 'Final display and clipped union lower index at page foot', []),
]
im = Image.open(source)
manifest = []
for name, bbox, purpose, rows in plans:
    crop = ImageOps.autocontrast(im.crop(tuple(bbox)))
    width = 2800
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.1, percent=120, threshold=3))
    rel = f'crops/{name}.png'
    crop.save(base / rel)
    manifest.append({'path': rel, 'bbox': bbox, 'rotation': 0, 'purpose': purpose,
                     'C_source_rows': rows, 'source': str(source),
                     'coordinates': 'original full-scan pixels, upper-left origin',
                     'output_size': list(crop.size), 'viewed': False})
(base / 'crops' / 'manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+'\n')
print(json.dumps({'created': len(manifest), 'source_size': list(im.size), 'output_directory': str(base/'crops')}))
