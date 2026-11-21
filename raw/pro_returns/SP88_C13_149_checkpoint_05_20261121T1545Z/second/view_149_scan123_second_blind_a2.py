from pathlib import Path
from PIL import Image, ImageEnhance

cropdir = Path('/workspace/scratch/0cab6a548abb/edition/crops')
panels = {
    'b01': [(0, 0, 2782, 930), (0, 830, 2782, 1760), (0, 1660, 2782, 2556)],
    'b02': [(0, 0, 2782, 760), (0, 680, 2782, 1440), (0, 1360, 2782, 2028)],
}
for box, bounds in panels.items():
    with Image.open(cropdir / f'149_scan123_second_{box}.png') as canonical:
        full = canonical.resize((1500, round(canonical.height * 1500 / canonical.width)), Image.Resampling.LANCZOS)
        full.save(cropdir / f'149_scan123_second_{box}_view1500.png')
        print(box, 'whole view', full.size)
        for index, bbox in enumerate(bounds, 1):
            panel = canonical.crop(bbox)
            panel = panel.resize((2000, round(panel.height * 2000 / panel.width)), Image.Resampling.LANCZOS)
            panel.save(cropdir / f'149_scan123_second_{box}_panel{index}.png')
            print(box, index, bbox, panel.size)
