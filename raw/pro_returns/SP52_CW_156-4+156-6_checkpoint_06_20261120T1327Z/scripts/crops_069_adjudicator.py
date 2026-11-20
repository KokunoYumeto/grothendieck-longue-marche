from pathlib import Path
from PIL import Image,ImageOps,ImageEnhance
import json,sys
O=Path(__file__).resolve().parents[1];K='156-4_069'
src=Path(json.loads((O.parent/'page_packets'/K/'metadata.json').read_text())['images'][0])
dest=O/'crops'/K;dest.mkdir(parents=True,exist_ok=True)
spec=[('a01_involution',(300,775,1670,1085),0,'Separate involution sentence, substantially unread in H and outside the returned crops already viewed.'),
 ('a02_margin_ne_vois',(300,650,720,1135),-48,'Still-open rightward/upward tail after marginal je: existing reader crops clip its full continuation. No absence inferred from their boundaries.')]
selected=sys.argv[1] if len(sys.argv)>1 else 'a01_involution'
im=Image.open(src);mp=dest/'manifest.json';manifest=json.loads(mp.read_text()) if mp.exists() else []
for name,bbox,rot,reason in spec:
 if name!=selected:continue
 p=dest/(name+'.jpg')
 if p.exists():raise SystemExit('Do not recreate an existing crop: '+str(p))
 c=im.crop(bbox)
 if rot:c=c.rotate(rot,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 c=ImageOps.autocontrast(c);scale=2500/c.width
 c=c.resize((2500,round(c.height*scale)),Image.Resampling.LANCZOS)
 c=ImageEnhance.Sharpness(c).enhance(1.12);c.save(p,quality=94)
 manifest.append(dict(path=str(p.relative_to(O)),source=str(src),bbox=bbox,scale=scale,rotation=rot,reason=reason,transformations=['crop','BICUBIC rotation, expand and white fill where nonzero','autocontrast','LANCZOS 2500 px across','sharpness 1.12','JPEG quality 94']))
(dest/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Created one new unframed target; not counted viewed by this script.')
