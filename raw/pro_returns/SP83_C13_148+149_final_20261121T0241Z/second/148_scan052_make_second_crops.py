from pathlib import Path
import csv
import json
from PIL import Image, ImageOps, ImageFilter

BASE = Path('/workspace/scratch/f28c4f52d3ec')
PAGE = '148_scan052'
source = BASE/'source/SP83_C13_148+149_scans/148_scan052.jpg'
with (BASE/'result/second'/f'{PAGE}_boxes.tsv').open() as fh:
    boxes = list(csv.DictReader(fh, delimiter='\t'))
im = Image.open(source).convert('RGB')
manifest = {'page': PAGE, 'source': str(source), 'source_size': list(im.size),
            'mode': 'Independent blind second reading; no first-pass files consulted.',
            'transform': 'Exact supplied original-coordinate crop; RGB autocontrast; LANCZOS enlargement; UnsharpMask radius 1.2 percent 110 threshold 3; no rotation.',
            'crops': []}
for b in boxes:
    box = [int(b[k]) for k in ['x0','y0','x1','y1']]
    source_width = box[2]-box[0]
    width = 1100 if source_width < 100 else 2400 if source_width < 350 else 3300 if source_width < 650 else 3800 if source_width < 900 else 4200
    out = BASE/'result/crops'/f"{PAGE}_second_{b['box']}.png"
    if out.exists():
        raise FileExistsError(f'Preserve existing blind evidence: {out}')
    part = ImageOps.autocontrast(im.crop(box))
    height = round(part.height*width/part.width)
    part = part.resize((width,height), Image.Resampling.LANCZOS)
    part = part.filter(ImageFilter.UnsharpMask(radius=1.2,percent=110,threshold=3))
    part.save(out)
    manifest['crops'].append({'box': b['box'], 'kind': b['kind'], 'original_box': box,
                              'path': str(out), 'output_size': [width,height], 'viewed': False})
(BASE/'result/second'/f'{PAGE}_second_crop_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'page':PAGE,'count':len(boxes),'source_size':list(im.size),'max_png_bytes':max(Path(c['path']).stat().st_size for c in manifest['crops'])},indent=2))
