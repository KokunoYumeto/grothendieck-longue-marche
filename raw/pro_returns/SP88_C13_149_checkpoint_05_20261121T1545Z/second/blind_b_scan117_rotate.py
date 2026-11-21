"""Display derivatives of an existing crop; no new source-image crop."""
from pathlib import Path
from PIL import Image
import json

base = Path('/workspace/scratch/0cab6a548abb')
src = base / 'edition/crops/149_scan117_second_b03.png'
out = base / 'edition/second/diagnostics'
im = Image.open(src)
ov = im.resize((1800, round(im.height * 1800 / im.width)), Image.Resampling.LANCZOS)
ov.save(out / '149_scan117_b03_overview.png')
rot = im.rotate(-29, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
rot.save(out / '149_scan117_b03_rot29.png')
rot.resize((1800, round(rot.height * 1800 / rot.width)), Image.Resampling.LANCZOS).save(out / '149_scan117_b03_rot29_overview.png')
(out / '149_scan117_rotation_manifest.json').write_text(json.dumps({
    'input_saved_crop':str(src), 'source_image_recropped':False,
    'rotation_degrees_pillow':-29, 'rotated_dimensions':rot.size,
    'outputs':['149_scan117_b03_overview.png','149_scan117_b03_rot29.png','149_scan117_b03_rot29_overview.png']
}, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print('Created two overviews and one rotated derivative', rot.size)
