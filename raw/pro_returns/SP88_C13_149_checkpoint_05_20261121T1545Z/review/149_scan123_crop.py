"""One reproducible first-reading crop per hard place on scan123; no OCR."""
from pathlib import Path
import sys
from PIL import Image, ImageOps, ImageFilter

ROOT = Path('/workspace/scratch/0cab6a548abb')
SOURCE = ROOT / 'packets/149_scan123/full.jpg'
DEST = ROOT / 'edition/crops'
CROPS = {
    'p01': [292, 40, 1623, 280],
    'p02': [296, 292, 1500, 397],
    'p03': [311, 405, 1510, 547],
    'p04': [305, 538, 904, 624],
    'p05': [411, 608, 1544, 704],
    'p06': [310, 801, 1510, 932],
    'p07': [304, 902, 1555, 1045],
    'p08': [290, 1042, 1606, 1318],
    'p09': [392, 1330, 1660, 1546],
    'p10': [286, 1500, 1652, 1652],
    'p11': [294, 1595, 1650, 1845],
    'p12': [295, 1819, 1366, 1973],
    'p13': [378, 1950, 1525, 2138],
    'p14': [294, 2210, 1679, 2335],
    'p15': [18, 2304, 94, 2351],
    # Declared contextual repairs: original p08/p12 clipped target ascenders.
    # They supply complete target context, not a second reading of settled ink.
    'p16': [290, 1000, 1606, 1318],
    'p17': [295, 1770, 1366, 1973],
}

if __name__ == '__main__':
    source = Image.open(SOURCE).convert('RGB')
    DEST.mkdir(parents=True, exist_ok=True)
    selected = sys.argv[1:] or list(CROPS)
    for place in selected:
        bbox = CROPS[place]
        target = DEST / f'149_scan123_{place}.png'
        if target.exists():
            raise FileExistsError(f'Refusing to overwrite inspected crop: {target}')
        crop = ImageOps.autocontrast(source.crop(bbox), cutoff=0.5)
        width = 3000
        crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
        crop = crop.filter(ImageFilter.UnsharpMask(radius=1, percent=110, threshold=4))
        crop.save(target)
        print(place, bbox, target.name)
