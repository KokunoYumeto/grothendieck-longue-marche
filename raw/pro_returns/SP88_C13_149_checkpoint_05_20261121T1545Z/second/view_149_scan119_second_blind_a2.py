from pathlib import Path
from PIL import Image, ImageEnhance

root = Path('/workspace/scratch/0cab6a548abb/edition/crops')
for box in ('b01', 'b02'):
    src = root / f'149_scan119_second_{box}.png'
    dest = root / f'149_scan119_second_{box}_view1500.png'
    with Image.open(src) as canonical:
        resized = canonical.resize((1500, round(canonical.height * 1500 / canonical.width)), Image.Resampling.LANCZOS)
        resized.save(dest)
        print(dest.name, canonical.size, resized.size)

panels = {
    'b01': [(0, 0, 2758, 840), (0, 740, 2758, 1600), (0, 1480, 2758, 2286)],
    'b02': [(0, 0, 3322, 860), (0, 780, 3322, 1640), (0, 1560, 3322, 2360)],
}
for box, bounds in panels.items():
    with Image.open(root / f'149_scan119_second_{box}.png') as canonical:
        for i, bbox in enumerate(bounds, 1):
            panel = canonical.crop(bbox)
            panel = panel.resize((2000, round(panel.height * 2000 / panel.width)), Image.Resampling.LANCZOS)
            dest = root / f'149_scan119_second_{box}_panel{i}.png'
            panel.save(dest)
            print(dest.name, bbox, panel.size)

details = {
    'b01_topright': ('b01', (1700, 20, 2650, 300)),
    'b01_line2': ('b01', (70, 265, 2380, 610)),
    'b01_middle': ('b01', (0, 715, 2758, 1330)),
    'b01_bottom': ('b01', (0, 1260, 2758, 2286)),
    'b01_quotedwords': ('b01', (30, 720, 1700, 930)),
    'b01_functor': ('b01', (1910, 690, 2758, 960)),
    'b01_geomsymbol': ('b01', (490, 235, 830, 590)),
    'b01_insertion': ('b01', (780, 1010, 2190, 1360)),
    'b01_cancelledfield': ('b01', (0, 1410, 480, 1740)),
    'b01_deletedwords': ('b01', (0, 1890, 1080, 2130)),
    'b02_label': ('b02', (470, 100, 760, 370)),
    'b02_surjectif': ('b02', (2790, 90, 3310, 380)),
    'b02_closure': ('b02', (1810, 410, 3322, 1160)),
    'b02_kummer': ('b02', (430, 1110, 3322, 1375)),
    'b02_lower': ('b02', (0, 1410, 3322, 2360)),
    'b02_lowerwords': ('b02', (470, 1410, 3322, 1850)),
    'b02_lowerinsertion': ('b02', (1910, 1670, 3220, 1910)),
    'b02_bottomformula': ('b02', (930, 1840, 3322, 2360)),
    'b02_marginbottom': ('b02', (0, 850, 1100, 1440)),
    'b02_margintop': ('b02', (100, 160, 1300, 950)),
}
for suffix, (box, bbox) in details.items():
    with Image.open(root / f'149_scan119_second_{box}.png') as canonical:
        detail = canonical.crop(bbox)
        if detail.width > 1800:
            detail = detail.resize((1800, round(detail.height * 1800 / detail.width)), Image.Resampling.LANCZOS)
        detail = ImageEnhance.Contrast(detail).enhance(1.6)
        dest = root / f'149_scan119_second_{suffix}_detail.png'
        detail.save(dest)
        print(dest.name, bbox, detail.size)

with Image.open(root / '149_scan119_second_b02.png') as canonical:
    bbox = (0, 120, 1310, 1470)
    margin = canonical.crop(bbox)
    margin = margin.rotate(-26, Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    margin = ImageEnhance.Contrast(margin).enhance(1.6)
    margin = margin.resize((1350, round(margin.height * 1350 / margin.width)), Image.Resampling.LANCZOS)
    margin.save(root / '149_scan119_second_b02_margin_rot26.png')
    print('b02_margin_rot26', bbox, margin.size, 'rotation=-26')
