from pathlib import Path
import csv, json
from PIL import Image, ImageOps, ImageFilter
root=Path('/workspace/scratch/f28c4f52d3ec')
source=root/'source/SP83_C13_148+149_scans/148_scan049.jpg'
rows=list(csv.DictReader((root/'result/second/148_scan049_boxes.tsv').open(),delimiter='\t'))
scales={'B01':9,'B02':4,'B03':3.5,'B04':4,'B05':2.5,'B06':3,'B07':2.5,'B08':5,'B09':2.8,'B10':4.5,'B11':4.5,'B12':2.6,'B13':10}
rotations={'B05':-43}
with Image.open(source) as original:
 manifest=[]
 for row in rows:
  bid=row['box']; box=tuple(int(row[k]) for k in ('x0','y0','x1','y1'))
  im=ImageOps.autocontrast(original.crop(box))
  f=scales[bid]; im=im.resize((round(im.width*f),round(im.height*f)),Image.Resampling.LANCZOS)
  if bid in rotations:
   im=im.rotate(rotations[bid],Image.Resampling.BICUBIC,expand=True,fillcolor='white')
  im=im.filter(ImageFilter.UnsharpMask(radius=1.3,percent=110,threshold=3))
  out=root/f'result/crops/148_scan049_second_{bid}.png'
  im.save(out)
  manifest.append({'box':bid,'original_box':box,'scale':f,'rotation':rotations.get(bid,0),'path':str(out),'size':im.size,'bytes':out.stat().st_size})
(root/'result/second/148_scan049_second_crop_manifest.json').write_text(json.dumps(manifest,indent=2))
for m in manifest:
 print(m['box'],m['size'],m['bytes'],m['path'])
