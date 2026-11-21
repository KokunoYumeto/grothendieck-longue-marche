from pathlib import Path
import csv,json
from PIL import Image, ImageOps, ImageFilter
root=Path('/workspace/scratch/f28c4f52d3ec')
rows=list(csv.DictReader((root/'result/second/148_scan051_boxes.tsv').open(),delimiter='\t'))
scales={'B01':9,'B02':2.7,'B03':2.7,'B04':2.7,'B05':2.6,'B06':2.6,'B07':5,'B08':6,'B09':4,'B10':4,'B11':4,'B12':10}
manifest=[]
with Image.open(root/'source/SP83_C13_148+149_scans/148_scan051.jpg') as im:
 for row in rows:
  bid=row['box'];box=tuple(int(row[k]) for k in ('x0','y0','x1','y1'))
  cut=ImageOps.autocontrast(im.crop(box));f=scales[bid]
  cut=cut.resize((round(cut.width*f),round(cut.height*f)),Image.Resampling.LANCZOS)
  cut=cut.filter(ImageFilter.UnsharpMask(radius=1.3,percent=110,threshold=3))
  out=root/f'result/crops/148_scan051_second_{bid}.png';cut.save(out)
  manifest.append({'box':bid,'original_box':box,'scale':f,'rotation':0,'path':str(out),'size':cut.size,'bytes':out.stat().st_size})
(root/'result/second/148_scan051_second_crop_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
for m in manifest:print(m['box'],m['size'],m['bytes'])
