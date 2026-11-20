"""Reader B, scan005: original-image crops only; no recognition."""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
ROOT=Path('/workspace/scratch/ddf8babdc42e')
SOURCE=ROOT/'source/SP115_CW_156-7_scans/H156-01_156-7_scan005.jpg'
SPECS={
 'page_number':([775,10,843,75],0),
 'M_heading':([323,61,1100,221],0),
 'left_note':([37,109,520,490],0),
 'right_note':([1215,60,1670,360],0),
 'L_heading':([323,270,1030,402],0),
 'L_definition':([900,245,1670,480],0),
 'axiom_intro':([262,545,1665,739],0),
 'at1':([275,730,1580,815],0),
 'at2':([275,803,1625,995],0),
 'margin_at1':([21,670,295,898],-34),
 'margin_at2':([20,805,465,1265],-37),
 'scholie':([402,1005,1667,1270],0),
 'conditions_ab':([705,1255,1655,1383],0),
 'condition_c':([705,1370,1655,1465],0),
 'margin_c':([120,1300,637,1610],-27),
 'ou_un':([620,1435,1660,1540],0),
 'b_prime':([690,1515,1660,1655],0),
 'a_prime':([695,1630,1540,1805],0),
 'left_arrow':([615,1480,815,1690],0),
 'relation':([413,1810,1645,1990],0),
 'reconstitution':([430,1970,1660,2153],0),
 'properties':([805,2140,1630,2325],0),
}
def main():
 im=Image.open(SOURCE);manifest={}
 for name,(box,angle) in SPECS.items():
  crop=ImageOps.autocontrast(im.crop(box),cutoff=0.4)
  if angle: crop=crop.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
  width=2800
  crop=crop.resize((width,round(crop.height*width/crop.width)),Image.Resampling.LANCZOS)
  crop=crop.filter(ImageFilter.UnsharpMask(radius=1.3,percent=120,threshold=3))
  out=ROOT/f'out/crops/scan005_{name}.png';crop.save(out)
  manifest[name]=dict(path=str(out.relative_to(ROOT)),source=str(SOURCE.relative_to(ROOT)),box=box,original_dimensions=[1684,2361],rotate=angle,rotation_resampler='Pillow BICUBIC' if angle else None,rotation_expand=True if angle else None,rotation_fill='white' if angle else None,autocontrast_cutoff_percent=0.4,output_width=width,resize_resampler='Pillow LANCZOS',unsharp_mask={'radius':1.3,'percent':120,'threshold':3})
 (ROOT/'out/review/scan005_crop_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
 print(f'Created {len(manifest)} crops, with exact original boxes and transform metadata.')
if __name__=='__main__':main()
