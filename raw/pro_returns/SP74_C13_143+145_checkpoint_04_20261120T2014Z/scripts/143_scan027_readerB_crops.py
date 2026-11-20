from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
root = Path('/workspace/scratch/8f839dff4bf0/SP74_C13_143+145_work')
im = Image.open('/workspace/scratch/8f839dff4bf0/source/SP74_C13_143+145_scans/143_scan027.jpg')
items = {
    'opening_symbols': ((983, 45, 1600, 274), 3000),
    'second_set': ((312, 282, 934, 392), 2800),
    'opening_close': ((320, 393, 1612, 613), 3200),
    'heading_revisions': ((430, 844, 1528, 1101), 3200),
    'punctured_family': ((349, 1280, 1405, 1446), 3200),
    'les_schemas': ((1000, 1541, 1510, 1655), 2800),
    'isom_and_article': ((350, 1660, 1170, 1787), 3000),
    'rank_and_sections': ((349, 1780, 1505, 1909), 3200),
    'dimension_condition': ((837, 1985, 1564, 2111), 3000),
    'en_fait_revision': ((363, 2104, 1345, 2240), 3000),
    'first_classifying_group': ((388, 2210, 911, 2316), 2800),
    'last_classifying_insertion': ((943, 2140, 1513, 2319), 2800),
}
for label, (box, width) in items.items():
    cr = ImageOps.autocontrast(ImageOps.grayscale(im.crop(box)))
    cr = cr.resize((width, round(cr.height * width / cr.width)), Image.Resampling.LANCZOS)
    cr = cr.filter(ImageFilter.UnsharpMask(radius=1.6, percent=145, threshold=2))
    path = root / 'crops' / f'143_scan027_readerB_{label}.png'
    cr.save(path)
    print(f'{path.name}: {box}')
