from pathlib import Path
from PIL import Image, ImageOps, ImageFilter, ImageChops
import json

root = Path('/workspace/scratch/f28c4f52d3ec')
page = '148_scan069'
im = Image.open(root/'source/SP83_C13_148+149_scans/148_scan069.jpg').convert('RGB')
places = [
    ('whole_graph', [380,75,1560,1250]),
    ('upper_labels', [825,285,1040,409]),
    ('left_label', [675,430,785,536]),
    ('inner_labels', [846,463,1105,663]),
    ('upper_right', [1080,300,1355,662]),
    ('lower_graph', [664,657,1323,1052]),
    ('folio', [22,1612,68,1666]),
]
records = []
for name, box in places:
    path = root/'result/crops'/f'{page}_{name}.png'
    region = ImageOps.autocontrast(im.crop(box))
    scale = max(3,min(8,3000/region.width))
    region = region.resize((round(region.width*scale),round(region.height*scale)),Image.Resampling.LANCZOS)
    region = region.filter(ImageFilter.UnsharpMask(1.2,105,3))
    region.save(path)
    view_path = path
    verified = None
    if path.stat().st_size > 6_290_000:
        view_path = root/'transport'/f'{page}_{name}.webp'
        view_path.parent.mkdir(exist_ok=True)
        region.save(view_path,format='WEBP',lossless=True,method=6)
        with Image.open(view_path) as decoded:
            assert decoded.size == region.size
            assert ImageChops.difference(region,decoded.convert('RGB')).getbbox() is None
        verified = True
    records.append(dict(name=name,crop=f'crops/{path.name}',path=str(path),box=box,
        view_path=str(view_path),png_bytes=path.stat().st_size,view_bytes=view_path.stat().st_size,
        lossless_transport_identical=verified,viewed=False))
(root/'proposed'/f'{page}_crop_boxes.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{k:r[k] for k in ('name','box','png_bytes','view_path','view_bytes')} for r in records],indent=2))
