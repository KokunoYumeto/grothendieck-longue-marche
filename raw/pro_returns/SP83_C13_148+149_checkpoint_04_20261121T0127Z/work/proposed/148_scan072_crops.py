from pathlib import Path
from PIL import Image,ImageOps,ImageFilter,ImageChops
import json

ROOT=Path('/workspace/scratch/f28c4f52d3ec'); PAGE='148_scan072'
source=ROOT/'source/SP83_C13_148+149_scans'/f'{PAGE}.jpg'
image=Image.open(source).convert('RGB')
assert image.size==(2359,1682)
specs=[
 ('title',[1607,123,2300,280],4.0,'Mandatory C/H word disagreement and full caption'),
 ('left_graph',[195,75,1730,1360],2.0,'Complete left drawing: all incidence, coloured contours, vertices and rays'),
 ('left_inner',[700,400,1088,1018],4.5,'Open doubled central pencil trace and closely spaced inner red shapes'),
 ('left_mark',[858,555,954,640],8.0,'Supplied C doubt M0950 and its local surroundings'),
 ('upper_left_ray',[198,198,308,298],8.0,'Open shape of the pointed upper-left ray endpoint'),
 ('right_graph',[1473,637,2154,1125],4.0,'Complete weighted graph and all handwritten numerical labels'),
 ('folio',[24,1616,86,1665],8.0,'Handwritten folio omitted by H')]
manifest=[]
for name,box,scale,reason in specs:
    crop=ImageOps.autocontrast(image.crop(box))
    crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1.2,percent=105,threshold=3))
    path=ROOT/'result/crops'/f'{PAGE}_{name}.png'
    crop.save(path)
    viewpath=path; identical=None
    if path.stat().st_size>6290000:
        viewpath=ROOT/'transport'/f'{PAGE}_{name}.webp'
        viewpath.parent.mkdir(exist_ok=True)
        crop.save(viewpath,format='WEBP',lossless=True,quality=100,method=6)
        assert ImageChops.difference(crop,Image.open(viewpath).convert('RGB')).getbbox() is None
        identical=True
    manifest.append(dict(name=name,crop=f'crops/{PAGE}_{name}.png',path=str(path),box=box,
        view_path=str(viewpath),png_bytes=path.stat().st_size,view_bytes=viewpath.stat().st_size,
        lossless_transport_identical=identical,viewed=False,reason=reason))
(ROOT/'proposed'/f'{PAGE}_crop_boxes.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(manifest,ensure_ascii=False))
