from pathlib import Path
import json
from PIL import Image, ImageOps, ImageFilter

ROOT = Path('/workspace/scratch/006c0e32b2af/out/readers/scan074/A')
SOURCE = Path('/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/B37-04_37_scan074.jpg')
OPEN_PLACES = [
    ('074_A_01_disol_edge.jpg', (1058, 305, 1218, 356), 'Clipped last glyph after diso; compare C l/n/u with H supplied ns.'),
    ('074_A_02_preferable_overtype.jpg', (410, 385, 626, 426), 'Overtyped letters in préférable: live letters, upper accents, and readable underprints.'),
    ('074_A_03_apres_edge.jpg', (1083, 421, 1218, 462), 'Visible portion of terminal s in après versus H supplied s.'),
    ('074_A_04_lower_curve.jpg', (1094, 1494, 1178, 1558), 'Isolated lower-right curve: actual contour and uncertain writing operation.'),
]

manifest = []
with Image.open(SOURCE) as original:
    for filename, bbox, reason in OPEN_PLACES:
        cropped = original.crop(bbox)
        cropped = ImageOps.autocontrast(cropped, cutoff=0.3)
        target_width = 2600
        target_height = round(cropped.height * target_width / cropped.width)
        cropped = cropped.resize((target_width, target_height), Image.Resampling.LANCZOS)
        cropped = cropped.filter(ImageFilter.UnsharpMask(radius=1, percent=80, threshold=2))
        cropped.save(ROOT / filename, quality=96, subsampling=0)
        manifest.append({
            'file': str(ROOT / filename),
            'bbox': list(bbox),
            'rotation': 0,
            'reason': reason,
            'processing': 'RGB autocontrast cutoff 0.3%; LANCZOS resize to 2600 px wide; unsharp mask radius 1, percent 80, threshold 2; JPEG quality 96.'
        })
(ROOT / 'crop_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print('Saved four crops and crop_manifest.json.')
