"""First-reading evidence for 149_scan003 only; boxes use original pixels."""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

root=Path('/workspace/scratch/f28c4f52d3ec')
page='149_scan003'
specs={
 'heading':([260,22,1225,155],3400),
 'profini':([790,218,1450,365],2800),
 'automorphisms':([280,650,1665,996],4200),
 'point':([280,970,1665,1110],4000),
 'variance':([285,1110,1665,1535],4200),
 'reconstitue':([280,1535,1640,1770],4000),
 'ensembles':([280,1870,1660,2202],4200),
 'folio':([20,2298,100,2350],1100),
}
im=Image.open(root/'source/SP83_C13_148+149_scans/149_scan003.jpg').convert('RGB')
records=[]
for name,(box,width) in specs.items():
    target=root/'result/crops'/f'{page}_{name}.png'
    if target.exists():raise FileExistsError(target)
    crop=ImageOps.autocontrast(im.crop(box))
    crop=crop.resize((width,round(width*crop.height/crop.width)),Image.Resampling.LANCZOS)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1.2,percent=110,threshold=3))
    crop.save(target)
    records.append({'place':name,'box':box,'path':str(target),'size':list(crop.size),
                    'bytes':target.stat().st_size})
(root/'proposed'/f'{page}_crop_manifest.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))
