from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
ROOT = Path('/workspace/scratch/0cab6a548abb')
SOURCE = ROOT / 'packets/149_scan120/full.jpg'
BOXES = {
 'p01': (322, 62, 1500, 166),
 'p02': (312, 226, 1655, 470),
 'p03': (311, 405, 1604, 570),
 'p04': (300, 598, 1632, 790),
 'p05': (302, 744, 1580, 865),
 'p06': (281, 848, 1650, 1122),
 'p07': (270, 1030, 1620, 1319),
 'p08': (285, 1255, 1637, 1541),
 'p09': (20, 849, 387, 1322),
 'p10': (17, 1286, 454, 1813),
 'p11': (266, 1503, 1639, 1668),
 'p12': (251, 1646, 1650, 1915),
 'p13': (257, 1835, 1646, 2136),
 'p14': (251, 2097, 1624, 2320),
 'p15': (17, 2311, 104, 2355),
 'p16': (315, 592, 949, 737),
 'p17': (947, 596, 1620, 725),
 'p18': (20, 810, 470, 1322),
 'p19': (16, 1376, 453, 1702),
 'p20': (16, 1493, 410, 1808),
}
ROTATIONS = {'p09': -39, 'p10': -32, 'p18': -39, 'p19': -32, 'p20': -32}
def save_crop(key,box):
 target=ROOT/f'edition/crops/149_scan120_{key}.png'
 target.parent.mkdir(parents=True,exist_ok=True)
 if target.exists(): raise FileExistsError(target)
 with Image.open(SOURCE) as src:
  crop=ImageOps.autocontrast(src.crop(box).convert('L'),cutoff=1)
 if key in ROTATIONS:
  crop=crop.rotate(ROTATIONS[key],resample=Image.Resampling.BICUBIC,expand=True,fillcolor=255)
 width=max(1800,min(2600,crop.width*3))
 crop=crop.resize((width,round(crop.height*width/crop.width)),Image.Resampling.LANCZOS)
 crop=crop.filter(ImageFilter.UnsharpMask(radius=1.2,percent=125,threshold=2))
 crop.save(target)
if __name__=='__main__':
 for key,box in BOXES.items():
  save_crop(key,box)
  print(key,box,ROTATIONS.get(key,0))
