"""Choose a tool-display encoding; the evidence PNG is never altered or recropped."""
from pathlib import Path
from PIL import Image
import sys, json

root = Path(__file__).resolve().parents[2]
source = root / 'edition/crops' / sys.argv[1]
assert source.is_file() and source.suffix == '.png'
if source.stat().st_size <= 4_000_000:
    print(source)
else:
    preview = root / 'preview' / (source.stem + '.jpg')
    preview.parent.mkdir(exist_ok=True)
    if not preview.exists():
        im = Image.open(source).convert('RGB')
        im.save(preview, quality=96, subsampling=0)
        record = {'source': str(source.relative_to(root)),
                  'display': str(preview.relative_to(root)),
                  'size': list(im.size), 'quality': 96, 'subsampling': 0,
                  'purpose': 'Same-dimension display encoding only; original PNG retained.'}
        (root/'edition/work'/('display_'+source.stem+'.json')).write_text(
            json.dumps(record, indent=2)+'\n')
    print(preview)
