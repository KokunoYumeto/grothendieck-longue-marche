from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/006c0e32b2af/out/readers/scan075/A')
source=Path('/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/H37-01_37_scan075.jpg')
image=Image.open(source).convert('RGB')
items=[
 {'file':'A01_pencil_verb.jpg','bbox':[37,45,153,151],'rotation':-22,'reason':'C doubt in slanted pencil verb: letters and initial capital/lower-case.'},
 {'file':'A02_intro_K.jpg','bbox':[1124,958,1206,1030],'rotation':0,'reason':'C doubt: one retraced K stem or independent double stroke.'},
 {'file':'A03_il_initial.jpg','bbox':[1030,1040,1292,1106],'rotation':0,'reason':'New open locus after the underlined clause: low dotted il or capital Il.'},
 {'file':'A04_schema.jpg','bbox':[941,1118,1068,1185],'rotation':0,'reason':'C doubt: final letter and possible underlying correction in schéma.'},
 {'file':'A05_margin_points.jpg','bbox':[1517,1337,1575,1400],'rotation':0,'reason':'C doubt: two detached marks beside the diagram; inspect shapes and placement.'},
]
for i in items:
 im=image.crop(tuple(i['bbox']))
 if i['rotation']:
  im=im.rotate(i['rotation'],resample=Image.Resampling.BICUBIC,expand=True,fillcolor=(255,255,255))
 im=ImageOps.autocontrast(im,cutoff=0.5)
 width=2400
 im=im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS)
 im=im.filter(ImageFilter.UnsharpMask(radius=1.5,percent=110,threshold=3))
 im.save(root/i['file'],quality=95)
 i['processing']='RGB; rotate before resize when indicated (BICUBIC, white fill); autocontrast cutoff 0.5%; LANCZOS resize to width 2400; UnsharpMask(radius=1.5, percent=110, threshold=3); JPEG quality 95'
(root/'crop_manifest.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(items,ensure_ascii=False,indent=2))
