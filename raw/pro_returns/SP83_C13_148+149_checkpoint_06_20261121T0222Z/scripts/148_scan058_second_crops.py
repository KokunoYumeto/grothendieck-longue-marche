from pathlib import Path
import csv,json,hashlib
from PIL import Image,ImageOps,ImageFilter
root=Path('/workspace/scratch/f28c4f52d3ec')
page='148_scan058'
source=root/'source/SP83_C13_148+149_scans'/f'{page}.jpg'
boxes=list(csv.DictReader((root/'result/second'/f'{page}_boxes.tsv').open(encoding='utf-8'),delimiter='\t'))
scales=[12,10,7,8,7,8,6,3,4,5,3,7,7,5,6,4,6,11]
im=Image.open(source).convert('RGB')
manifest={'page':page,'source':str(source.relative_to(root)),'source_size':im.size,'original_viewed':True,'reader':'reader_c','phase':'blind second reading','transforms':'exact crop, RGB autocontrast, LANCZOS enlargement, UnsharpMask(radius=1.3,percent=110,threshold=3); no OCR','crops':[]}
for row,scale in zip(boxes,scales):
 rect=tuple(int(row[n]) for n in ['x0','y0','x1','y1'])
 crop=ImageOps.autocontrast(im.crop(rect))
 crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS)
 crop=crop.filter(ImageFilter.UnsharpMask(radius=1.3,percent=110,threshold=3))
 out=root/'result/crops'/f'{page}_second_{row["box"]}.png'
 crop.save(out)
 manifest['crops'].append({'box':row['box'],'kind':row['kind'],'rect':rect,'scale':scale,'rotation':0,'path':str(out.relative_to(root)),'dimensions':crop.size,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'viewed':False})
(root/'result/second'/f'{page}_second_crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Created',len(manifest['crops']),'exact canonical crops')
for crop in manifest['crops']:
 print(crop['box'],crop['dimensions'],crop['bytes'])
