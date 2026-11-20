from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_065/R3')
p=out/'crop_manifest.json'
m=json.loads(p.read_text())
source=m[0]['source']; bbox=[280,845,865,1060]
c=ImageOps.autocontrast(Image.open(source).crop(bbox).convert('L'))
scale=2400/c.width
c=c.resize((2400,round(c.height*scale)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.2,percent=125,threshold=3))
target=out/'crops'/'17_comp_punctuation.jpg'
c.save(target,quality=95)
m.append({'path':str(target),'source':source,'bbox':bbox,'scale':scale,'rotation':0,'reason':'The abbreviation-ending punctuation at comp. was left open by the upper half and had not previously been cropped. Includes preceding C4 line.','transforms':'PIL grayscale, autocontrast (cutoff 0), LANCZOS to 2400 px width, UnsharpMask radius 1.2 / percent 125 / threshold 3; JPEG quality 95'})
p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
print(target)
