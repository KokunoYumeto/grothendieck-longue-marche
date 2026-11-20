from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/94548b74fbe0')
out=root/'out/readers/016/C'
im=Image.open(root/'source/SP40_CW_81_scans/J81-02_81_scan016.jpg')
items=[
 ('c18_point_below_avec.png',[257,1034,494,1160],'Detached point below/right of avec, with that word as context.'),
 ('c19_point_above_second_closure.png',[686,1814,976,1959],'Detached point above the second nonempty-intersection formula, with que and formula context.')
]
manifest=json.loads((out/'crop_manifest.json').read_text())
for name,bbox,purpose in items:
    part=ImageOps.autocontrast(im.crop(tuple(bbox)))
    part=part.resize((2600,round(part.height*2600/part.width)),Image.Resampling.LANCZOS)
    part=part.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
    part.save(out/name)
    manifest.append({'path':name,'bbox':bbox,'rotation':0,'purpose':purpose})
(out/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Created two new-locus crops; no previously cropped locus was recropped.')
