from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/94548b74fbe0/out/readers/013/C')
im=Image.open('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-02_81_scan013.jpg')
manifest=json.loads((root/'crops_manifest.json').read_text())
for stem,bbox,purpose,width in [
 ('c29_decouverte_accent',[100,690,336,762],'Accent presence/direction and word Découverte left open by half a',2596),
 ('c30_B_faint_arrow',[497,937,552,1067],'Complete pale arrow before second live subdivision; shaft origin and head',660)
]:
 c=ImageOps.autocontrast(im.crop(bbox)); scale=width/c.width
 c=c.resize((width,round(c.height*scale)),Image.Resampling.LANCZOS)
 c=c.filter(ImageFilter.UnsharpMask(radius=1.5,percent=110,threshold=3))
 p=root/(stem+'.png'); c.save(p)
 manifest.append(dict(path=p.name,bbox=bbox,coordinate_system='original full scan; upper-left origin; pixels',rotation=0,purpose=purpose,output_size=list(c.size),viewed=False))
(root/'crops_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Two final previously uninspected loci cropped; total',len(manifest))
