from pathlib import Path
import math
import sys
from PIL import Image, ImageDraw

ROOT = Path('/workspace/scratch/0cab6a548abb')
PAGE = '149_scan111'
OUT = ROOT / 'edition' / 'second' / 'diagnostics'
OUT.mkdir(parents=True, exist_ok=True)

# These are diagnostic display panels from an already saved crop. This script
# never opens or recrops the source manuscript image.
for box in sys.argv[1:]:
    source = ROOT / 'edition' / 'crops' / f'{PAGE}_second_{box}.png'
    with Image.open(source) as im:
        panel_width = min(1500, im.width)
        n = max(1, math.ceil(im.width / 1300))
        offsets = [round(i * (im.width - panel_width) / (n - 1)) if n > 1 else 0 for i in range(n)]
        header = 28
        panel_height = im.height + header
        wrapped = Image.new('RGB', (panel_width, n * panel_height), 'white')
        draw = ImageDraw.Draw(wrapped)
        for i, left in enumerate(offsets):
            # Cropping only the enlarged derivative preserves the one original
            # coordinate crop per assigned box.
            panel = im.crop((left, 0, left + panel_width, im.height))
            top = i * panel_height
            draw.text((8, top + 5), f'{box}, panel {i + 1}/{n}, derivative x={left}..{left + panel_width}; overlapping panels', fill='black')
            wrapped.paste(panel, (0, top + header))
        dest = OUT / f'{PAGE}_{box}_wrapped.png'
        wrapped.save(dest)
        print(dest)
