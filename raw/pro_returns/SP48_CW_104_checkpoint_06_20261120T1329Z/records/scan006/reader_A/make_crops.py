from pathlib import Path
from PIL import Image, ImageOps
import json

OUT = Path(__file__).parent
SRC = Path('/workspace/scratch/7178efd1cfac/source/SP48_CW_104_scans/H104-01_104_scan006.jpg')
specs = [
 ('01_typed_strip', [100,60,455,1450], -90, 3000),
 ('02_top_symbols', [635,35,1245,213], 0, 2800),
 ('03_upper_map_words', [1070,250,1690,540], 0, 2800),
 ('04_margin_diagram', [2095,240,2345,890], 90, 3000),
 ('05_margin_equality', [2130,1015,2290,1215], 90, 2400),
 ('06_xy_array', [1708,692,2112,990], 0, 2500),
 ('07_middle_words', [588,718,1577,897], 0, 3200),
 ('08_corrected_map_label', [566,893,837,1014], 0, 2400),
 ('09_subset_definition', [1435,1034,1970,1277], 0, 3000),
 ('10_canceled_opening', [868,1030,1435,1150], 0, 2800),
 ('11_canceled_soit', [645,1243,1096,1329], 0, 2600),
 ('12_considérons', [582,1301,1565,1425], 0, 3200),
 ('13_F_chain', [773,1431,1190,1529], 0, 2600),
 ('14_pi_formula', [1035,1522,2140,1649], 0, 3500),
 ('15_curved_arrow', [1848,1224,2115,1424], 0, 2400),
]
im = Image.open(SRC)
records = []
for name, box, angle, width in specs:
    crop = im.crop(box)
    if angle:
        crop = crop.rotate(angle, expand=True)
    crop = ImageOps.autocontrast(crop, cutoff=0)
    height = round(crop.height * width / crop.width)
    crop = crop.resize((width, height), Image.Resampling.LANCZOS)
    dst = OUT / 'crops' / (name + '.png')
    crop.save(dst)
    records.append({'file': str(dst.relative_to(OUT)), 'source': str(SRC), 'bbox': box, 'rotation_degrees_ccw': angle, 'autocontrast_cutoff': 0, 'resampling': 'LANCZOS', 'sharpening': 'none', 'output_size': [width,height]})
(OUT / 'crop_processing.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'crops':len(records),'dimensions':im.size,'output':str(OUT)}))
