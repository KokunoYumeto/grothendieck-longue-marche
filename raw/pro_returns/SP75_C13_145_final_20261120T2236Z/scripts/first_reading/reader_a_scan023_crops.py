from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

root = Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
source = Image.open(root/'packets/145_scan023/page.jpg')
specs = [
    ('opening_header10', [255,26,1612,166], 3000, 0),
    ('quoted_name_gen', [229,257,1632,463], 3000, 0),
    ('system17', [276,473,842,704], 3000, 0),
    ('nb_mark', [1060,425,1280,532], 2200, 0),
    ('main_insertion_hom', [228,700,1637,1088], 3000, 0),
    ('kernel_decrits', [222,1066,1620,1300], 3000, 0),
    ('separator', [744,1350,924,1422], 2000, 0),
    ('margin_relations', [23,1312,220,1730], 2500, -45),
    ('revenons_designera', [244,1440,1645,1762], 3000, 0),
    ('extension_cancelled_exterieurs', [254,1740,1642,1942], 3000, 0),
    ('lacets_autext_pi', [253,1911,1630,2126], 3000, 0),
    ('diagram18', [239,2116,1245,2355], 3000, 0),
    ('footer22', [31,2276,126,2352], 2000, 0),
]
manifest=[]
for name, box, width, rotation in specs:
    crop=ImageOps.autocontrast(source.crop(box).convert('RGB'))
    if rotation:
        crop=crop.rotate(rotation, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    crop=crop.resize((width, round(crop.height*width/crop.width)), Image.Resampling.LANCZOS)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1.3, percent=90, threshold=3))
    rel=f'crops/145_scan023_{name}.png'
    crop.save(root/'edition'/rel)
    manifest.append({'name':name,'crop':rel,'box':box,'width':width,'rotation_degrees':rotation})
(root/'edition/reader_reports/145_scan023_crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(manifest,ensure_ascii=False,indent=2))
