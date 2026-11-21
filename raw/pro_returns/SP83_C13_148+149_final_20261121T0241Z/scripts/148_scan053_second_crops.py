from pathlib import Path
import csv,json
from PIL import Image,ImageOps,ImageFilter
root=Path('/workspace/scratch/f28c4f52d3ec')
rows=list(csv.DictReader((root/'result/second/148_scan053_boxes.tsv').open(),delimiter='\t'))
scales={'B01':12,'B02':10,'B03':4.5,'B04':7,'B05':5.5,'B06':5,'B07':5,'B08':5,'B09':9,'B10':7,'B11':8,'B12':6,'B13':5.5,'B14':4.2,'B15':2.7,'B16':3.8,'B17':4.5,'B18':2.7,'B19':3.1,'B20':4.5,'B21':10,'B22':2.4,'B23':2.4,'B24':2,'B25':2}
rot={'B22':-43,'B23':-43,'B24':-43,'B25':-47}
manifest=[]
with Image.open(root/'source/SP83_C13_148+149_scans/148_scan053.jpg') as im:
 for row in rows:
  bid=row['box'];box=tuple(int(row[k]) for k in ('x0','y0','x1','y1'))
  cut=ImageOps.autocontrast(im.crop(box));f=scales[bid]
  cut=cut.resize((round(cut.width*f),round(cut.height*f)),Image.Resampling.LANCZOS)
  if bid in rot:cut=cut.rotate(rot[bid],Image.Resampling.BICUBIC,expand=True,fillcolor='white')
  cut=cut.filter(ImageFilter.UnsharpMask(radius=1.3,percent=110,threshold=3))
  out=root/f'result/crops/148_scan053_second_{bid}.png';cut.save(out)
  manifest.append({'box':bid,'original_box':box,'scale':f,'rotation':rot.get(bid,0),'path':str(out),'size':cut.size,'bytes':out.stat().st_size})
(root/'result/second/148_scan053_second_crop_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
for m in manifest:print(m['box'],m['size'],m['bytes'])
