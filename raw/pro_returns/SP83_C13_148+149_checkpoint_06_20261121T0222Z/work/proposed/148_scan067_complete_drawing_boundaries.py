"""Complete two unresolved diagram boundaries; preserve all earlier versions."""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

root = Path('/workspace/scratch/f28c4f52d3ec')
im = Image.open(root / 'source/SP83_C13_148+149_scans/148_scan067.jpg').convert('RGB')
for name, box, width in [
    ('pencil_map_full', (1360, 0, 2873, 1370), 3800),
    ('triangle1_full', (583, 1472, 1350, 2100), 3500),
]:
    target = root / 'result/crops' / f'148_scan067_{name}.png'
    if target.exists():
        raise FileExistsError(target)
    crop = ImageOps.autocontrast(im.crop(box))
    crop = crop.resize((width, round(width * crop.height / crop.width)), Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))
    crop.save(target)
    # Transport only: same dimensions, no new source crop, canonical PNG retained.
    transport = root / 'transport' / f'148_scan067_{name}_q98.jpg'
    if transport.exists():
        raise FileExistsError(transport)
    crop.save(transport, quality=98, subsampling=0)
    record = {'name': name, 'box': list(box), 'canonical': str(target), 'transport': str(transport),
              'dimensions': list(crop.size), 'transport_method': 'JPEG quality98, subsampling0; no resize or crop',
              'bytes': transport.stat().st_size}
    with (root / 'proposed/148_scan067_boundary_transport.jsonl').open('a') as stream:
        stream.write(json.dumps(record) + '\n')
    print(record, flush=True)
