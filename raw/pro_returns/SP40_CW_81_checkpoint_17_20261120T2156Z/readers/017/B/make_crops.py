from pathlib import Path
from PIL import Image, ImageOps
import json

BASE = Path('/workspace/scratch/94548b74fbe0')
OUT = BASE / 'out/readers/017/B'
SOURCE = BASE / 'source/SP40_CW_81_scans/J81-02_81_scan017.jpg'
im = Image.open(SOURCE)
# Coordinates are manually chosen full-scan pixels, origin upper left.
# No image matching, OCR, geometry fitting, or numerical mathematical checks.
specs = [
    ('crop01_top_correction.png', [1035,178,1665,336], 0, 5, 'First cancelled expression, raised on ait, and si/ou parenthesis'),
    ('crop02_trouve.png', [270,319,950,442], 0, 4, 'Cancelled Alors on trouve que, including the long final descender'),
    ('crop03_equation_endpoints.png', [780,408,1200,595], 0, 6, 'Upper equality right-hand endpoints and detached point'),
    ('crop04_join.png', [700,738,1240,850], 0, 5, 'First join in the third equality with surrounding terms'),
    ('crop05_margin.png', [20,936,323,1318], -42, 5, 'Entire slanted margin note, including corrected first member'),
    ('crop06_cancelled_definie.png', [411,1260,879,1395], 0, 6, 'Cancelled wording after X and live continuation'),
    ('crop07_corrected_E.png', [1258,1264,1598,1386], 0, 7, 'Overwritten predecessor of E_j and following parenthesis'),
    ('crop08_intersection.png', [307,1404,813,1500], 0, 5, 'Overwritten opening and state of intersection'),
    ('crop09_ternaires.png', [947,1345,1246,1478], 0, 8, 'Raised ternaires Pi_j and its complete V-shaped guide'),
    ('crop10_isolated_sign.png', [1071,1507,1447,1616], 0, 7, 'Later E_j, isolated cancelled form, and complete parenthesis'),
    ('crop11_first_union.png', [690,1844,995,1983], 0, 8, 'First large union, its limits, and the detached left point'),
    ('crop12_inserted_Pi.png', [552,1963,972,2096], 0, 6, 'Raised Pi_J upper ring and long curved insertion guide'),
    ('crop13_middle_union.png', [1002,1955,1641,2112], 0, 4, 'Middle complement union, transverse top stroke, and intersection'),
    ('crop14_binary_Pi.png', [1092,2062,1567,2220], 0, 6, 'Binary-partition upper ring, inserted parenthesis and curved guide'),
    ('crop15_U_subscript.png', [307,2140,581,2321], 0, 9, 'Inserted U_J, overwritten subscript, and complete guide into sur X'),
    ('crop16_final_words.png', [1115,2209,1652,2340], 0, 5, 'Final Pi_j, parenthetical quantified letter, punctuation, and Pour'),
]
records = []
for name, box, rotation, scale, purpose in specs:
    crop = ImageOps.autocontrast(im.crop(box).convert('RGB'))
    if rotation:
        crop = crop.rotate(rotation, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    unscaled = crop.size
    crop = crop.resize((crop.width * scale, crop.height * scale), Image.Resampling.LANCZOS)
    crop.save(OUT / name)
    records.append({'path': name, 'bbox': box, 'coordinate_system': 'full scan, upper-left origin; right and lower crop bounds exclusive', 'rotation': rotation, 'scale': scale, 'rotated_unscaled_size': list(unscaled), 'output_size': list(crop.size), 'purpose': purpose, 'operations': ['RGB conversion','autocontrast'] + (['BICUBIC rotation, expanded white canvas'] if rotation else []) + ['integer-scale LANCZOS resize','PNG save']})
(OUT / 'crop_manifest.json').write_text(json.dumps({'source': str(SOURCE), 'source_size': list(im.size), 'halves': {'a': [1685,1261], 'b': [1685,1262], 'b_full_scan_y_offset': 1101, 'offset_calculation': '2363 - 1262 = 1101; no pixel alignment calculation'}, 'crops': records}, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'crop_count': len(records), 'source_size': list(im.size), 'paths': [r['path'] for r in records]}, ensure_ascii=False))
