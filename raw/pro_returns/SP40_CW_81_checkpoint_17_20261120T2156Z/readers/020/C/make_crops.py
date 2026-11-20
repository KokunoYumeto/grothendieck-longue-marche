from pathlib import Path
import json
from PIL import Image, ImageOps, ImageFilter

base = Path('/workspace/scratch/94548b74fbe0')
out = base / 'out/readers/020/C'
source = Image.open(base / 'source/SP40_CW_81_scans/J81-03_81_scan020.jpg')
plan = json.loads((out / 'crop_plan.json').read_text())
for item in plan:
    im = source.crop(tuple(item['bbox']))
    if item['rotation']:
        im = im.rotate(item['rotation'], resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    im = ImageOps.autocontrast(im)
    width = 2600
    im = im.resize((width, round(im.height * width / im.width)), Image.Resampling.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.0, percent=100, threshold=3))
    im.save(out / item['path'])
print(f'Created {len(plan)} planned local crops; source dimensions {source.size}.')
