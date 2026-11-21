from pathlib import Path
from PIL import Image, ImageOps
import json

ROOT = Path(__file__).resolve().parent
SOURCE = Path('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-03_81_scan026.jpg')
plan = json.loads((ROOT / 'crop_plan.json').read_text())
im = Image.open(SOURCE).convert('RGB')
records = []
for target in plan['targets']:
    crop = im.crop(tuple(target['bbox']))
    original_size = list(crop.size)
    crop = ImageOps.autocontrast(crop, cutoff=0)
    if target['rotation']:
        crop = crop.rotate(target['rotation'], resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    rotated_size = list(crop.size)
    width = 2800
    height = round(crop.height * width / crop.width)
    crop = crop.resize((width, height), Image.Resampling.LANCZOS)
    relative = 'crops/' + target['id'] + '.png'
    crop.save(ROOT / relative)
    records.append(dict(target, path=relative, source=str(SOURCE), input_size=list(im.size), original_crop_size=original_size,
                        autocontrast={'cutoff':0}, rotation_resampler='BICUBIC' if target['rotation'] else None,
                        rotate_expand=bool(target['rotation']), rotated_size=rotated_size,
                        enlargement_resampler='LANCZOS', output_size=[width,height], sharpen=False))
(ROOT / 'crop_audit.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
print('Created', len(records), 'planned local crops; no displays performed by this script.')
