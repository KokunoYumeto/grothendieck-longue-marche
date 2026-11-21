"""Evidence inventory for assigned scan129; no other-page access."""
from pathlib import Path
import sys
from PIL import Image, ImageOps, ImageFilter

ROOT = Path('/workspace/scratch/0cab6a548abb')
SOURCE = ROOT / 'packets/149_scan129/full.jpg'
CROPS = {
 'p01': {'bbox': [855, 20, 920, 62], 'target': 'author number64', 'width': 1400},
 'p02': {'bbox': [150, 110, 1170, 260], 'target': 'whole formula34 including all four shafts and both end numerals'},
 'p03': {'bbox': [235, 315, 1625, 480], 'target': 'où, cancelled I(x), whole index-set and T definitions, punctuation'},
 'p04': {'bbox': [235, 570, 1650, 805], 'target': 'functions/fractions and plain versus underlined tilde O, with complete context'},
 'p05': {'bbox': [240, 800, 1220, 910], 'target': 'word after fonction, complete closure phrase and final K_x, M0163'},
 'p06': {'bbox': [240, 965, 1655, 1110], 'target': 'sur X insertion, est and on aura, M0164'},
 'p07': {'bbox': [240, 1050, 1665, 1210], 'target': 'pour S, hensélisé insertion and leader, du pt and whole eta expression, M0165'},
 'p08': {'bbox': [240, 1200, 1670, 1430], 'target': 'complete factorization and composed path, equality versus membership, shaft before U, induite'},
 'p09': {'bbox': [240, 1390, 1655, 1655], 'target': 'S/T factorization, T definition, l’image cancellation and l’hom replacement'},
 'p10': {'bbox': [240, 1620, 1520, 1775], 'target': 'plain L superscripts and complete cancelled contenue clause with un composé'},
 'p11': {'bbox': [200, 1765, 1180, 2040], 'target': 'whole formula35, both vertical relations, label and cancelled lower notation, M0166'},
 'p12': {'bbox': [255, 2020, 1670, 2335], 'target': 'complete final parenthesis, every group expression, dots and unfinished last clause'},
 'p13': {'bbox': [18, 2295, 105, 2342], 'target': 'thin lower foliation128', 'width': 1600},
 'p14': {'bbox': [235, 795, 1220, 930], 'target': 'contextual repair of p05: complete descender of the word after fonction and full closure phrase'},
 'p15': {'bbox': [240, 1575, 1535, 1790], 'target': 'contextual repair of p10: complete raised un composé and lower eta of the prose map'},
 'p16': {'bbox': [245, 1985, 1679, 2360], 'target': 'contextual repair of p12: complete upper exponent bars and lower/right paper-edge ending'},
 'p17': {'bbox': [150, 63, 1679, 285], 'target': 'previously uncropped opening line: au-dessus hyphen and complete context through formula34'},
 'p18': {'bbox': [235, 0, 1370, 112], 'target': 'contextual repair of p17: complete opening-line letter tops, including author64'},
}

def main():
 im = Image.open(SOURCE).convert('RGB')
 for name, item in CROPS.items():
  if len(sys.argv) > 1 and name not in sys.argv[1:]: continue
  dst = ROOT / f'edition/crops/149_scan129_{name}.png'
  if dst.exists(): raise FileExistsError(f'Refusing to overwrite inspected crop: {dst}')
  crop = ImageOps.autocontrast(im.crop(item['bbox']), cutoff=0.5)
  width = item.get('width', 3200)
  crop = crop.resize((width, round(crop.height*width/crop.width)), Image.Resampling.LANCZOS)
  crop = crop.filter(ImageFilter.UnsharpMask(radius=1, percent=110, threshold=4))
  crop.save(dst)
  print(f'{name}\t{item["bbox"]}\t{item["target"]}')

if __name__ == '__main__': main()
