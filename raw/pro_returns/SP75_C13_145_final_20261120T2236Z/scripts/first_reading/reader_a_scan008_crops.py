from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json

base=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
im=Image.open(base/'packets/145_scan008/page.jpg')
specs=[
 ('opening_words',[232,43,1615,152],0,3000),
 ('conjugating_factor',[717,245,1301,398],0,2700),
 ('deleted_les',[204,410,618,504],0,2500),
 ('system_third_line',[479,723,1681,970],0,3000),
 ('margin_nb',[21,640,444,1048],-29,2800),
 ('last_two_displays',[434,1689,1390,1907],0,3000),
 ('final_references',[572,1904,970,2009],0,2600),
 ('suffit_barred_m',[938,2003,1660,2110],0,2700),
 ('valeur_aux_deux_mb',[206,2104,1470,2228],0,3000),
]
saved=[]
for name,box,angle,width in specs:
    crop=ImageOps.autocontrast(im.crop(box).convert('RGB'))
    if angle: crop=crop.rotate(angle,Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    crop=crop.resize((width,round(crop.height*width/crop.width)),Image.Resampling.LANCZOS)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1.2,percent=110,threshold=3))
    rel=f'crops/145_scan008_{name}.png'
    crop.save(base/'edition'/rel)
    saved.append({'name':name,'box':box,'crop':rel,'rotation':angle})
(base/'edition/reader_reports/145_scan008_crop_manifest.json').write_text(json.dumps(saved,indent=2)+'\n')
print(json.dumps(saved,indent=2))
