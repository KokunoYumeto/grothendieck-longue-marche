from pathlib import Path
from PIL import Image, ImageOps
import json

BASE = Path('/workspace/scratch/94548b74fbe0')
OUT = BASE / 'out/readers/017/B'
im = Image.open(BASE / 'source/SP40_CW_81_scans/J81-02_81_scan017.jpg')
specs = [
    ('crop17_considérons.png', [313,1138,745,1243], 6, 'Accent and complete word Considérons'),
    ('crop18_definies.png', [536,1511,982,1619], 6, 'Local accent and ending of définies before par les'),
    ('crop19_lower_definie.png', [1080,1740,1452,1845], 7, 'Local accent and ending of définie in lower prose'),
]
manifest = json.loads((OUT / 'crop_manifest.json').read_text(encoding='utf-8'))
for name, box, scale, purpose in specs:
    crop = ImageOps.autocontrast(im.crop(box).convert('RGB'))
    unscaled = crop.size
    crop = crop.resize((crop.width * scale, crop.height * scale), Image.Resampling.LANCZOS)
    crop.save(OUT / name)
    manifest['crops'].append({'path': name, 'bbox': box, 'coordinate_system': 'full scan, upper-left origin; right and lower crop bounds exclusive', 'rotation': 0, 'scale': scale, 'rotated_unscaled_size': list(unscaled), 'output_size': list(crop.size), 'purpose': purpose, 'operations': ['RGB conversion','autocontrast','integer-scale LANCZOS resize','PNG save']})
(OUT / 'crop_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'new_crop_count': len(specs), 'total_crop_count': len(manifest['crops']), 'paths': [s[0] for s in specs]}, ensure_ascii=False))
