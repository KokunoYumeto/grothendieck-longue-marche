from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import csv,json,hashlib
root=Path('/workspace/scratch/f28c4f52d3ec'); page='148_scan061'
source=root/'source/SP83_C13_148+149_scans'/f'{page}.jpg'
rows=list(csv.DictReader((root/'result/second'/f'{page}_boxes.tsv').open(encoding='utf-8'),delimiter='\t'))
scales=[3.4,3.0,3.0,3.1,7,3,5,3.1,3.2,5.0,3.1,5.5,3.1,4.5,3.1,5,4,12]
angles=[0,0,0,0,-30,0,-28,0,0,-34,0,-33,0,-38,0,-42,0,0]
im=Image.open(source).convert('RGB')
manifest={'page':page,'source':str(source.relative_to(root)),'source_size':im.size,'reader':'reader_c','phase':'blind second reading','original_directly_viewed':True,'transforms':'exact original rectangle; RGB autocontrast; LANCZOS enlargement; optional BICUBIC rotation with expanded white field; UnsharpMask radius1.3 percent110 threshold3; no OCR','crops':[]}
for row,scale,angle in zip(rows,scales,angles):
 rect=tuple(int(row[k]) for k in ['x0','y0','x1','y1'])
 crop=ImageOps.autocontrast(im.crop(rect))
 crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS)
 if angle:crop=crop.rotate(angle,Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 crop=crop.filter(ImageFilter.UnsharpMask(radius=1.3,percent=110,threshold=3))
 out=root/'result/crops'/f'{page}_second_{row["box"]}.png'
 crop.save(out)
 manifest['crops'].append({'box':row['box'],'kind':row['kind'],'rect':rect,'scale':scale,'rotation_degrees':angle,'path':str(out.relative_to(root)),'dimensions':crop.size,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'viewed':False})
 print(row['box'],crop.size,out.stat().st_size)
(root/'result/second'/f'{page}_second_crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Created all',len(rows),'canonical crops.')
