"""Reproduce reader B's scan003 crops. No recognition is used."""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
ROOT=Path('/workspace/scratch/ddf8babdc42e')
SOURCE=ROOT/'source/SP115_CW_156-7_scans/H156-01_156-7_scan003.jpg'
SPECS={
 'context':([235,55,750,172],0),
 'lieu_point':([248,734,1662,1013],0),
 'margin':([15,645,1005,1845],-45),
 'lieux_etant':([260,1190,1570,1315],0),
 'figure_insertions':([265,1300,1545,1570],0),
 'ensembliste_ecrivons':([470,1650,1550,1825],0),
 'mulomb_first':([275,1818,1550,1918],0),
 'support_est':([275,1905,1155,2015],0),
 'mulomb_permet':([550,2054,1635,2160],0),
 'reconstituer_deletion_support':([270,2150,1635,2317],0),
 'ou_simplicite':([260,1015,835,1208],0),
}
def main():
 im=Image.open(SOURCE)
 for name,(box,angle) in SPECS.items():
  crop=ImageOps.autocontrast(im.crop(box),cutoff=0.4)
  if angle:
   crop=crop.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
  width=3000 if angle else 2800
  crop=crop.resize((width,round(crop.height*width/crop.width)),Image.Resampling.LANCZOS)
  crop=crop.filter(ImageFilter.UnsharpMask(radius=1.3,percent=120,threshold=3))
  if name=='margin':
   crop=crop.crop((0,790,2850,1680))
   crop=crop.resize((2800,round(crop.height*2800/crop.width)),Image.Resampling.LANCZOS)
  crop.save(ROOT/f'out/crops/scan003_{name}.png')
if __name__=='__main__': main()
