from pathlib import Path
from PIL import Image
import json,hashlib
root=Path('/workspace/scratch/f28c4f52d3ec');page='148_scan067'
source=root/'result/crops'/f'{page}_second_B07.png';im=Image.open(source)
manifest=[]
for name,rect in [('B07_top',(0,0,im.width,1320)),('B07_bottom',(0,1200,im.width,im.height))]:
 out=root/'result/crops'/f'{page}_second_{name}.png';tile=im.crop(rect);tile.save(out)
 manifest.append({'name':name,'source_canonical_crop':str(source.relative_to(root)),'rect_in_canonical_pixels':rect,'path':str(out.relative_to(root)),'dimensions':tile.size,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'viewed':False})
 print(name,tile.size,out.stat().st_size)
(root/'result/second'/f'{page}_second_dense_tile_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
