"""Evidence for page148_scan067 only. Original-coordinate boxes; retain all versions."""
from pathlib import Path
from PIL import Image,ImageOps,ImageFilter

ROOT=Path('/workspace/scratch/f28c4f52d3ec')
PAGE='148_scan067'
SPECS={
 'opening':([183,18,1080,486],3800,0),
 'card_title':([1190,18,2945,213],4400,0),
 'cancelled_def':([1190,204,2746,592],4500,0),
 'edge_condition':([1420,551,2150,716],3900,0),
 'torsors':([1480,705,2370,1058],4000,0),
 'pencil_map':([1360,153,2873,1355],3800,0),
 'pants':([419,495,1451,1439],3800,0),
 'loops':([105,1278,561,2001],2500,0),
 'algebra_main':([1306,1274,2207,1578],4200,0),
 'algebra_pencil':([1235,1517,1715,1732],3300,0),
 'triangle1':([583,1472,1315,2100],3500,0),
 'triangle2':([1235,1706,1737,2170],3300,0),
 'triangle3':([1633,1528,2051,1845],3500,0),
 'nb':([2270,1268,2981,1369],4000,0),
 'sphere':([2077,1342,2809,1954],3800,0),
 'counts':([1950,1817,2972,2160],4300,0),
 'folio':([102,2101,212,2208],1100,0),
}

def make(names=None):
 image=Image.open(ROOT/'source/SP83_C13_148+149_scans/148_scan067.jpg').convert('RGB')
 for name in SPECS if names is None else names:
  box,width,angle=SPECS[name]
  out=ImageOps.autocontrast(image.crop(box))
  if angle:out=out.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
  out=out.resize((width,round(out.height*width/out.width)),Image.Resampling.LANCZOS)
  out=out.filter(ImageFilter.UnsharpMask(radius=1.2,percent=110,threshold=3))
  path=ROOT/'result/crops'/f'{PAGE}_{name}.png'
  if path.exists():raise FileExistsError('Preserve existing evidence; use a new suffix: '+str(path))
  out.save(path)
  print(name,box,flush=True)

if __name__=='__main__':make()
