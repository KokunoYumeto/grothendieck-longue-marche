"""Retained record of smaller display copies; canonical evidence remains unchanged.

These copies were generated after the PNG transport rejected pencil_map.
They have not been inspected. Lossless transport will be preferred if available.
"""
from pathlib import Path
from PIL import Image

root = Path('/workspace/scratch/f28c4f52d3ec')
destdir = root / 'proposed/148_scan067_views'
destdir.mkdir(exist_ok=True)
for name in ['pencil_map', 'pants', 'loops', 'triangle1', 'triangle2', 'triangle3', 'sphere', 'counts']:
    src = root / 'result/crops' / f'148_scan067_{name}.png'
    im = Image.open(src)
    if max(im.size) > 2600:
        im.thumbnail((2600, 2600), Image.Resampling.LANCZOS)
    target = destdir / f'{name}.png'
    if target.exists():
        raise FileExistsError(target)
    im.save(target)
    print(name, src.stat().st_size, im.size, flush=True)
