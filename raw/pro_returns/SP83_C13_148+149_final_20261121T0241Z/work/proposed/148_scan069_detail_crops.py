from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
root=Path('/workspace/scratch/f28c4f52d3ec'); page='148_scan069'
im=Image.open(root/'source/SP83_C13_148+149_scans/148_scan069.jpg').convert('RGB')
side=root/'proposed'/f'{page}_crop_boxes.json'
records=json.loads(side.read_text())
for record in records: record['viewed']=True
for name,box,parent,reason in [
    ('black_chevrons',[1238,418,1311,547],'upper_right','Unresolved count and shape of the black overdraw beside the upper-right perimeter edge.'),
    ('left_fan',[730,360,930,550],'whole_graph','Unresolved directions, pen gaps and joins in the tightly packed upper-left red fan.')
]:
    path=root/'result/crops'/f'{page}_{name}.png'
    region=ImageOps.autocontrast(im.crop(box))
    scale=min(8,3000/region.width)
    region=region.resize((round(region.width*scale),round(region.height*scale)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(1.2,105,3))
    region.save(path)
    assert path.stat().st_size<6_290_000
    records.append(dict(name=name,crop=f'crops/{path.name}',path=str(path),box=box,
        view_path=str(path),png_bytes=path.stat().st_size,view_bytes=path.stat().st_size,
        lossless_transport_identical=None,viewed=False,extends=parent,reason=reason))
side.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('Two unresolved detail crops saved; nine crop files total.')
