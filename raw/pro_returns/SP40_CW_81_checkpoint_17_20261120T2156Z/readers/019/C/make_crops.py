from pathlib import Path
import json
from PIL import Image, ImageOps, ImageFilter

ROOT = Path('/workspace/scratch/94548b74fbe0/out/readers/019/C')
SOURCE = Path('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-03_81_scan019.jpg')
PLAN = [
 ('01_top_edge', [1400,65,1692,164], 'First cardinality ending and page-edge punctuation'),
 ('02_avec', [252,258,790,358], 'Compressed word before card, original C row09'),
 ('03_ens_first_U', [250,488,1020,632], 'ens. and first-U entrance strokes, original C rows01 and10'),
 ('04_lune', [920,734,1550,840], 'l’une/l’un word ending, original C row11'),
 ('05_ona1', [1010,845,1290,947], 'Tiny words after recurrence, original C row02'),
 ('06_union1_index', [864,940,1194,1125], 'Large join and overwritten index, original C rows03 and04'),
 ('07_overwritten_K', [660,1168,975,1286], 'Brace-line predecessor and live K0, original C row12'),
 ('08_ona2', [268,1485,670,1593], 'Crowded lead-in before donc, original C row05 and H deletion'),
 ('09_union2', [710,1570,1085,1745], 'Second large join, lower limit and adjacent hats'),
 ('10_deuxieme', [415,1765,1025,1885], 'Au deuxième/dernier =, witness difference'),
 ('11_struck_somme', [1030,1760,1595,1880], 'Struck word following dans la, original C row06'),
 ('12_borner_sommer', [375,2010,1075,2108], 'Mark after borner and sommer, original C row07 and H placeholder'),
 ('13_cet', [420,2190,1068,2288], 'K1 cet ens., donc, original C row08'),
 ('14_lower_end_dots', [1400,1570,1668,1745], 'Detached dark marks after middle display right parenthesis'),
 ('15_bottom_edge', [600,2240,1505,2362], 'Last display including page-edge lower limit and terminal parenthesis'),
 ('16_pale_trace_brace', [430,1240,590,1345], 'Pale curved trace to the left of middle brace'),
]

im = Image.open(SOURCE)
manifest = []
for name, bbox, purpose in PLAN:
    path = ROOT / 'crops' / (name + '.png')
    crop = ImageOps.autocontrast(im.crop(tuple(bbox)))
    width = 2800
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.1, percent=120, threshold=3))
    crop.save(path)
    manifest.append({'path': 'crops/' + path.name, 'bbox': bbox, 'coordinate_origin': 'full scan upper-left, pixels', 'rotation': 0, 'purpose': purpose, 'output_size': list(crop.size), 'viewed': False, 'successful_views': 0, 'failed_unseen_deliveries': 0})
(ROOT / 'crops' / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
(ROOT / 'image_ledger.json').write_text(json.dumps({'start_utc': '2026-11-20 19:48:32 UTC', 'image_dimensions': {'whole': [1692,2362], 'a': [1692,1261], 'b': [1692,1261]}, 'half_coordinate_maps': {'a': 'x_full=x_a; y_full=y_a', 'b': 'x_full=x_b; y_full=y_b+1101; 1101=2362-1261'}, 'base_images': [{'name': 'J81-03_81_scan019.jpg', 'successful_views': 1, 'failed_unseen_deliveries': 0, 'order': 1}, {'name': 'J81-03_81_scan019_a.jpg', 'successful_views': 1, 'failed_unseen_deliveries': 0, 'order': 2}, {'name': 'J81-03_81_scan019_b.jpg', 'successful_views': 1, 'failed_unseen_deliveries': 0, 'order': 3}], 'crops': manifest}, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'created_crops': len(manifest), 'root': str(ROOT)}))
