from pathlib import Path
from PIL import Image,ImageOps,ImageFilter,ImageChops
import csv,json,hashlib
root=Path('/workspace/scratch/f28c4f52d3ec');page='148_scan072'
source=root/'source/SP83_C13_148+149_scans'/f'{page}.jpg';im=Image.open(source).convert('RGB')
rows=list(csv.DictReader((root/'result/second'/f'{page}_boxes.tsv').open(),delimiter='\t'))
manifest={'page':page,'reader':'reader_c','source':str(source.relative_to(root)),'source_size':im.size,'original_directly_viewed_once':True,'transforms':'Exact crop, RGB autocontrast, LANCZOS enlargement, UnsharpMask radius1.1 percent105 threshold3; no OCR.','crops':[],'helpers':[]}
for row,scale in zip(rows,[2.0,10]):
 rect=tuple(int(row[k]) for k in ['x0','y0','x1','y1'])
 c=ImageOps.autocontrast(im.crop(rect)).resize((round((rect[2]-rect[0])*scale),round((rect[3]-rect[1])*scale)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.1,percent=105,threshold=3))
 out=root/'result/crops'/f'{page}_second_{row["box"]}.png';c.save(out)
 item={'box':row['box'],'kind':row['kind'],'source_rect':rect,'scale':scale,'path':str(out.relative_to(root)),'dimensions':c.size,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'viewed':False}
 if out.stat().st_size>6200000:
  transport=root/'transport'/f'{page}_second_{row["box"]}.webp';transport.parent.mkdir(exist_ok=True)
  c.save(transport,format='WEBP',lossless=True,quality=100,method=4)
  assert ImageChops.difference(c,Image.open(transport).convert('RGB')).getbbox() is None
  item.update({'transport_path':str(transport.relative_to(root)),'transport_pixel_identical':True,'transport_bytes':transport.stat().st_size})
 manifest['crops'].append(item);print(row['box'],c.size,out.stat().st_size,item.get('transport_bytes',''),flush=True)
for name,rect,scale in [('B01_caption',(1590,100,2300,290),4),('B01_numbers',(1460,620,2170,1140),3.5),('B01_contours_top',(195,75,1325,700),2.5),('B01_contours_bottom',(300,600,1460,1360),2.4)]:
 c=ImageOps.autocontrast(im.crop(rect)).resize((round((rect[2]-rect[0])*scale),round((rect[3]-rect[1])*scale)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.1,percent=105,threshold=3))
 out=root/'result/crops'/f'{page}_second_{name}.png';c.save(out)
 item={'name':name,'parent_box':'B01','source_rect':rect,'scale':scale,'path':str(out.relative_to(root)),'dimensions':c.size,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'viewed':False}
 manifest['helpers'].append(item);print(name,c.size,out.stat().st_size,flush=True)
(root/'result/second'/f'{page}_second_crop_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
