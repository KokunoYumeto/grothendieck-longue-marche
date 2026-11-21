"""Single saved evidence crop per assigned scan128 target cluster."""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter

ROOT = Path('/workspace/scratch/0cab6a548abb')
SOURCE = ROOT / 'packets/149_scan128/full.jpg'
CROPS = {
    'p01': {'bbox': [330, 305, 1620, 545], 'target': 'deuxième, partie and the b) insertion with leader'},
    'p02': {'bbox': [335, 590, 1550, 738], 'target': 'complete first E_L to E_U expression and both shaft ends'},
    'p03': {'bbox': [325, 738, 1640, 870], 'target': 'complete next E_L and E_K expressions with following prose'},
    'p04': {'bbox': [315, 850, 1590, 1095], 'target': 'Delta_V insertion, relative pi expression, I_V and dash'},
    'p05': {'bbox': [310, 1070, 1670, 1335], 'target': 'qui on le devine, jouera un rôle analogue and groupe-bout, with complete context'},
    'p06': {'bbox': [290, 1320, 1550, 1450], 'target': 'V distinctes and complete question line'},
    'p07': {'bbox': [285, 1445, 905, 1595], 'target': 'whole final Delta/Lambda_V expression, distinctes and question mark, M0160'},
    'p08': {'bbox': [285, 1765, 1645, 2075], 'target': 'both D= and D_i(i in I) insertions, full component/divisor context and both X-U forms'},
    'p09': {'bbox': [290, 2055, 1565, 2265], 'target': 'x in supp D, hensélisé insertion and complete tilde O_x / O_X,x expressions, M0161'},
    'p10': {'bbox': [290, 2220, 1610, 2340], 'target': 'final decorated U_x, entire image inverse line and On a, M0162'},
    'p11': {'bbox': [18, 2295, 100, 2342], 'target': 'thin lower foliation 127', 'width': 1600},
}

def main():
    im = Image.open(SOURCE).convert('RGB')
    for name, spec in CROPS.items():
        dst = ROOT / f'edition/crops/149_scan128_{name}.png'
        if dst.exists():
            raise FileExistsError(f'Refusing to overwrite inspected crop: {dst}')
        crop = ImageOps.autocontrast(im.crop(spec['bbox']), cutoff=0.5)
        width = spec.get('width', 3000)
        crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
        crop = crop.filter(ImageFilter.UnsharpMask(radius=1, percent=110, threshold=4))
        crop.save(dst)
        print(f'{name}\t{spec["bbox"]}\t{spec["target"]}')

if __name__ == '__main__':
    main()
