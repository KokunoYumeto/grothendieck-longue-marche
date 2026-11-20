from pathlib import Path
import json
from PIL import Image, ImageOps

root = Path('/workspace/scratch/94548b74fbe0')
dest = root / 'out/readers/017/C'
source = root / 'source/SP40_CW_81_scans/J81-02_81_scan017.jpg'
box = (300, 1135, 855, 1250)
with Image.open(source) as im:
    part = ImageOps.autocontrast(im.crop(box).convert('RGB'))
    result = part.resize((2220, 460), Image.Resampling.LANCZOS)
    result.save(dest / 'crop14_considerons.png')
entry = {'path': 'crop14_considerons.png', 'source': str(source), 'bbox': list(box), 'coordinate_origin': 'full scan, top-left; right/bottom exclusive', 'rotation': 0, 'rotation_resampling': None, 'autocontrast': True, 'sharpening': False, 'scale': 4, 'pre_resize_size': [555, 115], 'output_size': [2220, 460], 'purpose': 'Unresolved accent presence in Considérons, with complete word and following la.'}
log = json.loads((dest / 'crop_log.json').read_text())
log.append(entry)
(dest / 'crop_log.json').write_text(json.dumps(log, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(entry, ensure_ascii=False))
