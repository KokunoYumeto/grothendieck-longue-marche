from pathlib import Path
from PIL import Image

BASE = Path('/workspace/scratch/8f839dff4bf0')
WORK = BASE / 'SP74_C13_143+145_work'
box = (1005, 1360, 1673, 1525)
out = WORK / 'crops/143_scan021_auditC_morphism_set.png'
assert not out.exists(), 'This one permitted crop already exists; do not recrop.'
with Image.open(BASE / 'source/SP74_C13_143+145_scans/143_scan021.jpg') as image:
    crop = image.crop(box)
    crop.resize((crop.width * 4, crop.height * 4), Image.Resampling.LANCZOS).save(out)
print({'crop': str(out), 'native_box': box, 'scale': 4})
