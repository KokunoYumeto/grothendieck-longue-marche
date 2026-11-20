from pathlib import Path
import json
from PIL import Image, ImageOps, ImageFilter
root=Path(__file__).parent
source=Path('/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/H37-01_37_scan075.jpg')
image=Image.open(source).convert('RGB')
items=json.loads((root/'open_loci.json').read_text())
for item in items:
    crop=image.crop(tuple(item['bbox']))
    if item['rotation']:
        crop=crop.rotate(item['rotation'], resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    crop=ImageOps.autocontrast(crop, cutoff=0.3)
    crop=crop.resize((2400,round(crop.height*2400/crop.width)),Image.Resampling.LANCZOS)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1, percent=70, threshold=3))
    item['file']=str(root/('B_scan075_'+item['id']+'.jpg'))
    item['processing']='RGB; rotate with BICUBIC if nonzero; autocontrast cutoff 0.3%; LANCZOS resize to 2400 px width; UnsharpMask radius 1, percent 70, threshold 3; JPEG quality 96.'
    crop.save(item['file'],quality=96)
(root/'crop_manifest.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
