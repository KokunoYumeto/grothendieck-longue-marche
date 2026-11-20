from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import csv, json

base = Path('/workspace/scratch/ddf8babdc42e')
stem = 'H156-01_156-7_scan009'
source = base/'source/SP115_CW_156-7_scans'/f'{stem}.jpg'
boxfile = base/'out/second'/f'{stem}_boxes.tsv'
with boxfile.open(newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f, delimiter='\t'))
assert len(rows) == 31
im = Image.open(source).convert('RGB')
rotations = {'B007': -40, 'B022': -39, 'B024': -45, 'B026': -45}
manifest = {'scan': 'scan009', 'source': str(source), 'source_dimensions': list(im.size), 'operation_order': ['exact crop', 'autocontrast', 'rotation if specified', 'LANCZOS resize', 'UnsharpMask'], 'crops': []}
for row in rows:
    box = [int(row[k]) for k in ('x0','y0','x1','y1')]
    out = base/'out/crops'/f"second_scan009_{row['box']}.png"
    assert not out.exists(), f'Refusing to replace {out}'
    crop = ImageOps.autocontrast(im.crop(box), cutoff=.4)
    angle = rotations.get(row['box'], 0)
    if angle:
        crop = crop.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    width = 2800
    if crop.height/crop.width > 2.5:
        width = round(2800*crop.width/crop.height)
    height = round(crop.height*width/crop.width)
    crop = crop.resize((width,height), Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.1, percent=100, threshold=3))
    crop.save(out)
    manifest['crops'].append({'box':row['box'], 'kind':row['kind'], 'original_box':box, 'rotation_degrees_Pillow':angle, 'rotation_resampling':'BICUBIC', 'rotation_expand':True if angle else False, 'rotation_fill':'white' if angle else None, 'autocontrast_cutoff':.4, 'resize_resampling':'LANCZOS', 'output_size':[width,height], 'sharpen':{'method':'UnsharpMask','radius':1.1,'percent':100,'threshold':3}, 'path':str(out)})
(base/'out/second'/f'{stem}_crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'new_crops':len(rows),'source_dimensions':im.size,'rotations':rotations,'narrow_graphic_long_edge_limit':2800}))
