from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import json
root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
source=Image.open(root/'packets/145_scan026/page.jpg')
specs=[
    ('parameter_trials',[290,172,1325,292],3000,0),
    ('operations_groups',[288,286,1631,495],3000,0),
    ('conjugaison_trouve',[386,495,1634,706],3000,0),
    ('covariants',[395,712,1450,812],3000,0),
    ('covariance_formula',[370,842,1255,970],3000,0),
    ('struck_si',[278,966,1084,1059],3000,0),
    ('nb_oblique',[32,288,718,1180],3000,-35),
    ('footer25',[31,2271,115,2350],2000,0),
]
manifest=[]
for name,box,width,rotation in specs:
    crop=ImageOps.autocontrast(source.crop(box).convert('RGB'))
    if rotation:
        crop=crop.rotate(rotation,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    crop=crop.resize((width,round(width*crop.height/crop.width)),Image.Resampling.LANCZOS)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1.3,percent=90,threshold=3))
    rel=f'crops/145_scan026_{name}.png'
    crop.save(root/'edition'/rel)
    manifest.append(dict(name=name,crop=rel,box=box,width=width,rotation_degrees=rotation))
(root/'edition/reader_reports/145_scan026_crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(manifest,ensure_ascii=False))
