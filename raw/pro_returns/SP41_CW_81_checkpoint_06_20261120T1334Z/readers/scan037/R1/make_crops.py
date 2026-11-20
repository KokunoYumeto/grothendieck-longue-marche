from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
from datetime import datetime, timezone
import json
root=Path('/workspace/scratch/811dda00717a')
src=root/'source/SP41_CW_81_scans/J81-05_81_scan037.jpg'
out=root/'work/readers/scan037/R1/crops'
items=[
('01_heading',[220,35,410,165],0),
('02_slanted_note',[18,150,530,991],-45),
('03_second_inclusion',[835,735,1150,840],0),
('04_cancelled_pair',[270,825,715,945],0),
('05_rewritten_sigma',[1310,820,1597,944],0),
('06_bare_sigma',[1165,1025,1566,1132],0),
('07_revised_proof',[285,1375,1610,1630],0),
('08_definition_heading_pi',[293,1650,1044,1765],0),
('09_strict_word',[1200,1650,1576,1762],0),
('10_inserted_phrase_les',[584,1720,1320,1870],0),
('11_distincts_suffix',[1115,1840,1578,1970],0),
('12_bottom_display',[291,2240,1668,2350],0),
]
records=[]
with Image.open(src) as full:
    for name,box,rot in items:
        im=full.crop(tuple(box))
        trim=None
        if rot:
            im=im.rotate(rot,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
            mask=im.convert('L').point(lambda v:255 if v<150 else 0)
            bound=mask.getbbox()
            trim=[max(0,bound[0]-20),max(0,bound[1]-20),min(im.width,bound[2]+20),min(im.height,bound[3]+20)]
            im=im.crop(trim)
        im=ImageOps.autocontrast(im)
        im=im.resize((3000,round(im.height*3000/im.width)),Image.Resampling.LANCZOS)
        im=im.filter(ImageFilter.UnsharpMask(radius=1.0,percent=120,threshold=3))
        target=out/(name+'.png')
        im.save(target)
        records.append({'source':str(src),'target':str(target),'bbox':box,'rotation_degrees':rot,'rotated_trim_box':trim,'width':3000,'height':im.height,'enhancement':['autocontrast','LANCZOS','UnsharpMask(radius=1.0,percent=120,threshold=3)'],'UTC':datetime.now(timezone.utc).isoformat()})
(out/'crop_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(records,ensure_ascii=False,indent=2))
