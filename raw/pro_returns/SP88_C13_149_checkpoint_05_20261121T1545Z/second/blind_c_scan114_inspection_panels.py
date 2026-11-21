from PIL import Image
from pathlib import Path
import sys,json
root=Path('/workspace/scratch/0cab6a548abb')
box=sys.argv[1]
mode=sys.argv[2] if len(sys.argv)>2 else 'halves'
p=root/f'edition/crops/149_scan114_second_{box}.png'
im=Image.open(p)
if mode=='halves':
    mid=im.width//2
    out=Image.new(im.mode, (im.width-mid,2*im.height+40),'white')
    out.paste(im.crop((0,0,mid,im.height)),(0,0))
    out.paste(im.crop((mid,0,im.width,im.height)),(0,im.height+40))
    detail={'derived_from':str(p),'layout':'left half above right half, no overlap, 40px white gap','split_x_pixels':mid,'rotation_degrees':0}
elif mode.startswith('rotate'):
    angle=float(mode[6:])
    out=im.rotate(angle,expand=True,fillcolor='white',resample=Image.Resampling.BICUBIC)
    detail={'derived_from':str(p),'layout':'rotated saved crop','rotation_degrees':angle}
else:
    raise ValueError(mode)
q=root/f'edition/crops/149_scan114_second_{box}_{mode}.png'
out.save(q)
detail['file']=str(q)
log=root/'edition/second/blind_c_scan114_inspection_records.json'
r=json.loads(log.read_text()) if log.exists() else []
r.append(detail)
log.write_text(json.dumps(r,indent=2),encoding='utf8')
print(q)
