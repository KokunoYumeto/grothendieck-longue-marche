from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
root = Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
im = Image.open('/workspace/scratch/8f839dff4bf0/source/SP74_C13_143+145_scans/143_scan024.jpg')
items = {
    'opening_attachment': ((700, 90, 1662, 421), 3000),
    'cancelled_adjective': ((590, 224, 859, 289), 2800),
    'codomain_and_action': ((883, 553, 1658, 927), 3000),
    'object_set': ((282, 930, 1585, 1167), 3200),
    'injection': ((571, 1274, 1254, 1460), 3000),
    'mais_and_bracket': ((517, 1740, 1470, 1878), 3000),
    'family_and_bitorsors': ((295, 1986, 1457, 2196), 3200),
}
for label, (box, width) in items.items():
    cr = ImageOps.autocontrast(ImageOps.grayscale(im.crop(box)))
    cr = cr.resize((width, round(cr.height * width / cr.width)), Image.Resampling.LANCZOS)
    cr = cr.filter(ImageFilter.UnsharpMask(radius=1.6, percent=145, threshold=2))
    path = root / 'crops' / f'143_scan024_readerB_{label}.png'
    cr.save(path)
    print(f'{path.name}: {box}')
