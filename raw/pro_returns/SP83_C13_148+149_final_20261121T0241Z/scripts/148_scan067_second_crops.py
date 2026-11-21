from pathlib import Path
from PIL import Image,ImageOps,ImageFilter,ImageChops
import csv,json,hashlib
root=Path('/workspace/scratch/f28c4f52d3ec');page='148_scan067'
source=root/'source/SP83_C13_148+149_scans'/f'{page}.jpg'
rows=list(csv.DictReader((root/'result/second'/f'{page}_boxes.tsv').open(encoding='utf-8'),delimiter='\t'))
scales=[3.2,2.5,2.6,3.0,4.0,3.5,1.8,4.0,3.5,5.0,3.5,4.0,5.0,4.0,3.6,3.5,8.0]
im=Image.open(source).convert('RGB')
manifest={'page':page,'reader':'reader_c','phase':'blind second reading','source':str(source.relative_to(root)),'source_size':im.size,'original_directly_viewed':True,'transforms':'Exact original rectangles; RGB autocontrast; LANCZOS enlargement; UnsharpMask radius1.2 percent105 threshold3. No OCR. Oversized PNGs may have a pixel-identical lossless WebP transport copy.','crops':[]}
transport=root/'transport';transport.mkdir(exist_ok=True)
for row,scale in zip(rows,scales):
 rect=tuple(int(row[k]) for k in ['x0','y0','x1','y1'])
 crop=ImageOps.autocontrast(im.crop(rect)).resize((round((rect[2]-rect[0])*scale),round((rect[3]-rect[1])*scale)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.2,percent=105,threshold=3))
 out=root/'result/crops'/f'{page}_second_{row["box"]}.png';crop.save(out)
 item={'box':row['box'],'kind':row['kind'],'rect':rect,'scale':scale,'path':str(out.relative_to(root)),'dimensions':crop.size,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'viewed':False}
 if out.stat().st_size>6400000:
  webp=transport/f'{page}_second_{row["box"]}.webp'
  crop.save(webp,format='WEBP',lossless=True,quality=100,method=4)
  decoded=Image.open(webp).convert('RGB')
  assert decoded.size==crop.size and ImageChops.difference(crop,decoded).getbbox() is None
  item.update({'transport_path':str(webp.relative_to(root)),'transport_bytes':webp.stat().st_size,'transport_pixel_identical':True})
 manifest['crops'].append(item)
 print(row['box'],crop.size,out.stat().st_size,item.get('transport_bytes',''),flush=True)
(root/'result/second'/f'{page}_second_crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Complete',len(rows),flush=True)
