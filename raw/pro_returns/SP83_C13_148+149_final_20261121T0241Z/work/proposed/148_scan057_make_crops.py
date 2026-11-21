"""Page-local evidence transforms; no OCR or full-page rescaling."""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter

ROOT = Path('/workspace/scratch/f28c4f52d3ec')
PAGE = '148_scan057'
SPECS = {
    'opening': ([310, 25, 1603, 188], 3800),
    'torseurs': ([320, 289, 1618, 589], 3900),
    'first_formula': ([319, 592, 923, 745], 3200),
    'first_formula_full': ([319, 575, 923, 745], 3200),
    'contraction': ([320, 733, 1620, 831], 3700),
    'partial': ([315, 838, 1565, 1070], 3800),
    'extension': ([318, 1070, 1635, 1300], 3800),
    'multiple': ([313, 1284, 1668, 1623], 3900),
    'strengthening': ([315, 1625, 1650, 1850], 3800),
    'singular': ([315, 1850, 1630, 2160], 3900),
    'singular_full': ([315, 1815, 1630, 2185], 3900),
    'final': ([315, 2150, 1580, 2340], 3700),
    'folio': ([41, 2244, 135, 2335], 1100),
}

def make(names=None):
    source = Image.open(ROOT / 'source/SP83_C13_148+149_scans/148_scan057.jpg').convert('RGB')
    for name in (SPECS if names is None else names):
        box, width = SPECS[name]
        crop = ImageOps.autocontrast(source.crop(box))
        crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
        crop = crop.filter(ImageFilter.UnsharpMask(radius=1.2, percent=115, threshold=3))
        crop.save(ROOT / 'result/crops' / f'{PAGE}_{name}.png')

if __name__ == '__main__':
    make()
