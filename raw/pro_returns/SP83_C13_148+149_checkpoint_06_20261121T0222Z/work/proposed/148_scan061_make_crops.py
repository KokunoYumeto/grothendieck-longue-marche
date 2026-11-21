"""Evidence crops for this page only; boxes use original scan coordinates."""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter

ROOT = Path('/workspace/scratch/f28c4f52d3ec')
PAGE = '148_scan061'
SPECS = {
    'heading': ([248,22,1430,155],3400,0),
    'zero_insert': ([320,135,1265,219],3600,0),
    'item1_circles': ([386,230,1560,366],3900,0),
    'item1_replace': ([386,338,1643,602],3900,0),
    'margin1': ([50,228,319,523],2000,-29),
    'item2_title': ([312,555,1515,644],3900,0),
    'item2_body': ([391,611,1663,1019],3900,0),
    'margin2': ([14,482,434,1063],3100,-30),
    'item3_title': ([312,1008,1640,1165],3900,0),
    'item3_formula': ([393,1136,1625,1389],3900,0),
    'margin3': ([24,984,409,1392],2400,-31),
    'items45': ([270,1388,1617,1673],3900,0),
    'margin45': ([18,1380,319,1772],2300,-34),
    'item6': ([312,1657,1618,1807],3900,0),
    'margin6': ([20,1642,418,2098],2600,-39),
    'item7': ([315,1796,1668,2025],3900,0),
    'item7_product': ([388,2011,742,2140],2000,0),
    'margin7': ([20,1907,413,2300],2500,-42),
    'footnote': ([1005,2010,1671,2338],3500,0),
    'folio': ([22,2294,88,2349],1100,0),
    # Boundary completion only; retain the initial clipped versions above.
    'item1_circles_full': ([300,158,1645,389],3900,0),
    'item1_replace_full': ([386,312,1643,602],3900,0),
    'item2_full': ([290,520,1663,1040],3900,0),
    'zero_insert_full': ([300,108,1660,232],4000,0),
}

def make(names=None):
    source = Image.open(ROOT/'source/SP83_C13_148+149_scans/148_scan061.jpg').convert('RGB')
    for name in (SPECS if names is None else names):
        box,width,angle = SPECS[name]
        output = ImageOps.autocontrast(source.crop(box))
        if angle:
            output = output.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
        output = output.resize((width,round(output.height*width/output.width)),Image.Resampling.LANCZOS)
        output = output.filter(ImageFilter.UnsharpMask(radius=1.2,percent=115,threshold=3))
        path=ROOT/'result/crops'/f'{PAGE}_{name}.png'
        if path.exists():
            raise FileExistsError(f'Preserve the existing crop and use a new suffix: {path}')
        output.save(path)

if __name__ == '__main__':
    make()
