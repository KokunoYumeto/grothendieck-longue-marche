from pathlib import Path
import json
from PIL import Image, ImageOps, ImageFilter

root = Path('/workspace/scratch/006c0e32b2af/out/readers/scan086/B')
source = Path('/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/B37-04_37_scan086.jpg')
specs = [
    ('B086_01_s4_lower_mark.jpg', [1137, 317, 1274, 374], 'Explicit C doubt: small mark below/right of the period in the section 4 heading.'),
    ('B086_02_53_under_d.jpg', [572, 967, 713, 1018], 'Explicit C doubt: older character beneath live d in de, entry 5.3.'),
    ('B086_03_55_under_f.jpg', [709, 1122, 832, 1171], 'Explicit C doubt: older character beneath live f in valuatifs, entry 5.5.'),
    ('B086_04_610_under_i.jpg', [613, 1859, 785, 1911], 'Explicit C doubt: older character beneath live i in schématique, entry 6.10.'),
    ('B086_05_610_punctuation.jpg', [971, 1860, 1125, 1911], 'Explicit C doubt: punctuation after schéma, entry 6.10.'),
    ('B086_06_vertical_trace.jpg', [774, 384, 850, 482], 'New open locus: vertical trace between section 4 heading leaders and entry 4.1 leaders; determine material or graphic status.'),
    ('B086_07_detached_pair.jpg', [1374, 1496, 1443, 1552], 'New open locus: two small dark points above entry 6.3 leaders; determine material or graphic status.'),
]
im = Image.open(source).convert('RGB')
records = []
for name, bbox, reason in specs:
    crop = im.crop(bbox)
    size = (2400, round(crop.height * 2400 / crop.width))
    crop = crop.resize(size, Image.Resampling.LANCZOS)
    crop = ImageOps.autocontrast(crop, cutoff=0)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))
    crop.save(root / name, quality=96, subsampling=0)
    records.append({'file': name, 'source': str(source), 'bbox': bbox, 'rotation': 0,
                    'reason': reason, 'processing': {'mode': 'RGB', 'resize': size,
                    'resampling': 'LANCZOS', 'autocontrast_cutoff': 0,
                    'unsharp_mask': {'radius': 1.2, 'percent': 110, 'threshold': 3},
                    'jpeg_quality': 96, 'jpeg_subsampling': 0},
                    'requested_deliveries': 0, 'actual_visual_views': 0})
(root / 'crop_processing.json').write_text(json.dumps(records, indent=2) + '\n')
