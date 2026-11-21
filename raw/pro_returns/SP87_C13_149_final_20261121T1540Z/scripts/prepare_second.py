"""Prepare image-only blind-reading crops, never loading a witness or first reading."""
from pathlib import Path
import csv
import json
import sys
from PIL import Image, ImageOps, ImageFilter

ROOT = Path('/workspace/scratch/b8c6ff258063')
WORK = ROOT/'SP87_C13_149_work'

def prepare(scan, rotations=None):
    rotations = rotations or {}
    page = f'149_scan{scan:03d}'
    source = ROOT/'source/SP87_C13_149_scans'/f'{page}.jpg'
    boxes_path = WORK/'second'/f'{page}_boxes.tsv'
    boxes = list(csv.DictReader(boxes_path.open(), delimiter='\t'))
    targets = [WORK/'crops'/f'second_{page}_{b["box"]}.png' for b in boxes]
    if any(p.exists() for p in targets):
        raise SystemExit('Second crops already exist; inspect those, do not recrop.')
    im = Image.open(source)
    manifest = []
    for b, target in zip(boxes, targets):
        box = tuple(int(b[k]) for k in ('x0','y0','x1','y1'))
        crop = ImageOps.autocontrast(im.crop(box))
        width = 2200
        crop = crop.resize((width, max(1, round(crop.height*width/crop.width))), Image.Resampling.LANCZOS)
        crop = crop.filter(ImageFilter.UnsharpMask(radius=1.1, percent=115, threshold=2))
        angle = float(rotations.get(b['box'], 0))
        if angle:
            crop = crop.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
        crop.save(target)
        manifest.append({'box':b['box'],'kind':b['kind'],'coordinates':box,'crop':str(target),'rotation_degrees':angle})
    output = WORK/'second'/f'{page}_crop_manifest.json'
    output.write_text(json.dumps(manifest, indent=2)+'\n')
    print(json.dumps({'page':page,'image':str(source),'boxes':str(boxes_path),'manifest':str(output),'count':len(boxes)}))

if __name__ == '__main__':
    prepare(int(sys.argv[1]), json.loads(sys.argv[2]) if len(sys.argv)>2 else {})
