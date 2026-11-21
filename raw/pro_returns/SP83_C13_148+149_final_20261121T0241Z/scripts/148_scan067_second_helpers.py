from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import json,hashlib
root=Path('/workspace/scratch/f28c4f52d3ec');page='148_scan067'
im=Image.open(root/'source/SP83_C13_148+149_scans'/f'{page}.jpg').convert('RGB')
items=[
('B01_end',(183,330,1080,510),4),
('B02_orientation',(1250,0,2120,125),4),
('B02_end',(2100,95,2945,245),4),
('B03_upper',(1190,193,2746,400),3.5),
('B03_lower',(1190,390,2746,634),3),
('B06_upper',(1480,705,2370,900),3.5),
('B06_lower',(1480,885,2370,1058),3.5),
('B08_caption',(210,1680,505,1810),6),
('B09_pale',(1580,1274,2207,1578),4),
('B13_labels',(1660,1590,2020,1845),6),
('B14_words',(2570,1268,2981,1369),5),
('B16_bottom',(1950,1940,2972,2160),3.5),
('B16_caption_top',(2300,1817,2972,1970),4),
]
manifest=[]
for name,rect,scale in items:
 crop=ImageOps.autocontrast(im.crop(rect)).resize((round((rect[2]-rect[0])*scale),round((rect[3]-rect[1])*scale)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.1,percent=110,threshold=3))
 out=root/'result/crops'/f'{page}_second_{name}.png';crop.save(out)
 manifest.append({'name':name,'parent_box':name[:3],'source_rect':rect,'scale':scale,'path':str(out.relative_to(root)),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'viewed':False})
 print(name,crop.size,out.stat().st_size)
(root/'result/second'/f'{page}_second_helper_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
