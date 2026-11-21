"""Complete clipped letter bounds; preserve all original evidence crops."""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

root=Path('/workspace/scratch/f28c4f52d3ec')
specs={
 'automorphisms_full':([280,650,1665,1025],4200),
 'variance_full':([285,1085,1665,1560],4200),
 'reconstitue_full':([280,1495,1640,1785],4000),
}
im=Image.open(root/'source/SP83_C13_148+149_scans/149_scan003.jpg').convert('RGB')
rows=[]
for name,(box,width) in specs.items():
    target=root/'result/crops'/f'149_scan003_{name}.png'
    if target.exists():raise FileExistsError(target)
    crop=ImageOps.autocontrast(im.crop(box))
    crop=crop.resize((width,round(width*crop.height/crop.width)),Image.Resampling.LANCZOS)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1.2,percent=110,threshold=3))
    crop.save(target)
    rows.append({'place':name,'box':box,'path':str(target),'size':list(crop.size)})
(root/'proposed/149_scan003_boundary_manifest.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))
