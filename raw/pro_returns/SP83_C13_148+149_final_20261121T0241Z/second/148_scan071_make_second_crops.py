from pathlib import Path
import csv
import json
from PIL import Image, ImageOps, ImageFilter, ImageChops

BASE = Path(__file__).resolve().parents[2]
PAGE = '148_scan071'
SOURCE = BASE / 'source' / 'SP83_C13_148+149_scans' / f'{PAGE}.jpg'
BOXES = BASE / 'result' / 'second' / f'{PAGE}_boxes.tsv'
MANIFEST = BASE / 'result' / 'second' / f'{PAGE}_second_crop_manifest.json'
WIDTHS = {'B01':3000,'B02':3600,'B03':1800,'B04':3600,'B05':3600,'B06':3000,'B07':3200,'B08':3600,'B09':1200}
if MANIFEST.exists():
    raise RuntimeError('Refusing to overwrite existing current-page crop manifest')
with BOXES.open(encoding='utf-8', newline='') as handle:
    boxes = list(csv.DictReader(handle, delimiter='\t'))
manifest = {'page':PAGE,'source':str(SOURCE),'mode':'Independent blind second reading','crops':[]}
with Image.open(SOURCE) as original:
    manifest['source_size'] = list(original.size)
    for row in boxes:
        name = row['box']
        coordinates = [int(row[k]) for k in ('x0','y0','x1','y1')]
        target = BASE / 'result' / 'crops' / f'{PAGE}_second_{name}.png'
        if target.exists():
            raise RuntimeError(f'Refusing to overwrite {target}')
        crop = ImageOps.autocontrast(original.crop(coordinates).convert('RGB'))
        width = WIDTHS[name]
        height = round(crop.height * width / crop.width)
        crop = crop.resize((width,height), Image.Resampling.LANCZOS)
        crop = crop.filter(ImageFilter.UnsharpMask(radius=1.0,percent=80,threshold=3))
        crop.save(target)
        record = {'box':name,'kind':row['kind'],'original_box':coordinates,'path':str(target),'output_size':[width,height],'rotation_degrees':0,'transform':'Exact original-coordinate crop; RGB autocontrast; LANCZOS enlargement; UnsharpMask radius1.0 percent80 threshold3.','viewed':False,'display_path':str(target)}
        if target.stat().st_size > 5900000:
            display = BASE / 'transport' / f'{PAGE}_second_{name}.webp'
            if display.exists():
                raise RuntimeError(f'Refusing to overwrite {display}')
            display.parent.mkdir(exist_ok=True)
            crop.save(display,format='WEBP',lossless=True,method=4)
            with Image.open(display) as restored:
                assert restored.size == crop.size
                assert ImageChops.difference(crop,restored.convert('RGB')).getbbox() is None
            record.update({'display_path':str(display),'transport':'Lossless WebP at identical dimensions; decoded pixels verified identical. Display duplicate only.','transport_bytes':display.stat().st_size})
        manifest['crops'].append(record)
        print(json.dumps({'box':name,'png_bytes':target.stat().st_size,'output_size':[width,height],'display_path':record['display_path'],'display_bytes':Path(record['display_path']).stat().st_size}),flush=True)
MANIFEST.write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
