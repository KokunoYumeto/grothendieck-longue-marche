from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import json,hashlib
root=Path('/workspace/scratch/f28c4f52d3ec');p='148_scan067'
im=Image.open(root/'source/SP83_C13_148+149_scans'/f'{p}.jpg').convert('RGB')
items=[('B03_right_words',(2290,245,2746,395),6),('B03_replacement',(1570,358,2490,455),4.5),('B08_caption_full',(320,1680,561,1810),6)]
m=[]
for name,rect,s in items:
 c=ImageOps.autocontrast(im.crop(rect)).resize((round((rect[2]-rect[0])*s),round((rect[3]-rect[1])*s)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1,percent=105,threshold=3))
 f=root/'result/crops'/f'{p}_second_{name}.png';c.save(f)
 m.append({'name':name,'parent_box':name[:3],'source_rect':rect,'scale':s,'path':str(f.relative_to(root)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'viewed':False})
 print(name,c.size)
(root/'result/second'/f'{p}_second_final_helper_manifest.json').write_text(json.dumps(m,indent=2)+'\n')
