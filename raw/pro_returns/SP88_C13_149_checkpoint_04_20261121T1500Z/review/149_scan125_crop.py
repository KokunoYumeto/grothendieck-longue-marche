"""Single-pass evidence crops for assigned manuscript scan 125 only."""
from pathlib import Path
import sys
from PIL import Image, ImageOps, ImageFilter

ROOT = Path('/workspace/scratch/0cab6a548abb')
SOURCE = ROOT / 'packets/149_scan125/full.jpg'
CROPS = {
    'p01': {'bbox': [300, 80, 945, 180], 'target': 'initial rait and following context'},
    'p02': {'bbox': [310, 175, 1635, 265], 'target': 'first construire with complete text line'},
    'p03': {'bbox': [320, 275, 1580, 405], 'target': 'E_L sur E_K and written pts'},
    'p04': {'bbox': [310, 410, 1445, 660], 'target': 'dim 0 and both quotation marks around variété de Riemann'},
    'p05': {'bbox': [310, 680, 1635, 795], 'target': 'Composant and following sous-extension'},
    'p06': {'bbox': [305, 795, 1630, 935], 'target': 'whole L_1 superscript expression and degree context, M0140'},
    'p07': {'bbox': [310, 940, 1490, 1065], 'target': 'hom punctuation and complete E_L to E_L1 map'},
    'p08': {'bbox': [305, 1075, 1620, 1355], 'target': 'second construire and germes de insertion with attachment'},
    'p09': {'bbox': [300, 1360, 1635, 1505], 'target': 'le fait intéressant sera and E_K'},
    'p10': {'bbox': [300, 1490, 1585, 1665], 'target': 'en insertion, its leader, and trouve pas plus'},
    'p11': {'bbox': [300, 1785, 1640, 1945], 'target': 'both quote pairs around places and complete adjacent expression'},
    'p12': {'bbox': [20, 1630, 510, 2045], 'target': 'whole slanted marginal note', 'rotation': -29},
    'p13': {'bbox': [875, 30, 960, 85], 'target': 'author page number 62', 'width': 1600},
    'p14': {'bbox': [20, 2295, 105, 2345], 'target': 'thin lower foliation 124', 'width': 1600},
    'p15': {'bbox': [295, 1355, 1640, 1665], 'target': 'declared contextual repair of p09: complete E_K and two main lines, including en insertion', 'repairs': 'p09'},
}

def main():
    im = Image.open(SOURCE).convert('RGB')
    for name, spec in CROPS.items():
        if sys.argv[1:] and name not in sys.argv[1:]:
            continue
        dst = ROOT / f'edition/crops/149_scan125_{name}.png'
        if dst.exists():
            raise FileExistsError(f'Refusing to overwrite inspected crop: {dst}')
        crop = ImageOps.autocontrast(im.crop(spec['bbox']), cutoff=0.5)
        if spec.get('rotation'):
            crop = crop.rotate(spec['rotation'], Image.Resampling.BICUBIC,
                               expand=True, fillcolor='white')
        width = spec.get('width', 2800)
        crop = crop.resize((width, round(crop.height * width / crop.width)),
                           Image.Resampling.LANCZOS)
        crop = crop.filter(ImageFilter.UnsharpMask(radius=1, percent=110, threshold=4))
        crop.save(dst)
        print(f'{name}\t{spec["bbox"]}\t{spec["target"]}')

if __name__ == '__main__':
    main()
