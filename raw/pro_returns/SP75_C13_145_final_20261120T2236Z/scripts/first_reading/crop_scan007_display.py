from PIL import Image,ImageOps,ImageFilter
from pathlib import Path
import json
r=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
b=[291,2114,1222,2215]
im=ImageOps.autocontrast(Image.open(r/'packets/145_scan007/page.jpg').crop(b))
im=im.resize((2600,round(im.height*2600/im.width)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
im.save(r/'edition/crops/145_scan007_12_double_star_display.png')
p=r/'edition/crops/145_scan007_crop_boxes.json'
x=json.loads(p.read_text());x['145_scan007_12_double_star_display']=b;p.write_text(json.dumps(x,indent=2)+'\n')
