from pathlib import Path
import math
import json
import sys
from PIL import Image, ImageDraw

ROOT = Path('/workspace/scratch/0cab6a548abb')
PAGE = '149_scan117'
OUT = ROOT / 'edition' / 'second' / 'diagnostics'
OUT.mkdir(parents=True, exist_ok=True)

def starts(length, size, overlap):
    if length <= size:
        return [0]
    count = math.ceil((length-size)/(size-overlap)) + 1
    return [round(i * (length-size)/(count-1)) for i in range(count)]

manifest = []
for box in sys.argv[1:]:
    source = ROOT / 'edition' / 'crops' / f'{PAGE}_second_{box}.png'
    with Image.open(source) as im:
        width, height = min(1800, im.width), min(1500, im.height)
        for ri, top in enumerate(starts(im.height, height, 240), 1):
            for ci, left in enumerate(starts(im.width, width, 240), 1):
                # These panels are derived only from the saved enlarged crop;
                # this script does not open or crop the manuscript source.
                panel = im.crop((left, top, left+width, top+height))
                display = Image.new('RGB', (width, height+28), 'white')
                draw = ImageDraw.Draw(display)
                draw.text((8, 5), f'{box}, derivative panel r{ri} c{ci}; x={left}..{left+width}, y={top}..{top+height}; overlap retained', fill='black')
                display.paste(panel, (0, 28))
                dest = OUT / f'{PAGE}_{box}_r{ri}_c{ci}.png'
                display.save(dest)
                manifest.append({'box': box, 'file': str(dest), 'derivative_bbox': [left,top,left+width,top+height], 'row':ri, 'column':ci})
                print(dest)
(OUT / f'{PAGE}_panel_manifest.json').write_text(json.dumps(manifest, indent=2)+'\n', encoding='utf-8')
