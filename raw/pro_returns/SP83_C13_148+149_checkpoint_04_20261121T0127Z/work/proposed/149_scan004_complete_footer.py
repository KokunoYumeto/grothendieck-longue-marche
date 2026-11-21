from pathlib import Path
import json
from PIL import Image, ImageOps, ImageFilter

BASE = Path('/workspace/scratch/f28c4f52d3ec')
SOURCE = BASE / 'source/SP83_C13_148+149_scans/149_scan004.jpg'
DEST = BASE / 'result/crops/149_scan004_footer_full.png'
BOX = [280, 2140, 1678, 2345]
WIDTH = 4200
if DEST.exists():
    raise FileExistsError(f'Preserve previous evidence: {DEST}')
im = Image.open(SOURCE).convert('RGB')
part = ImageOps.autocontrast(im.crop(BOX))
height = round(part.height * WIDTH / part.width)
part = part.resize((WIDTH, height), Image.Resampling.LANCZOS)
part = part.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))
part.save(DEST)
record = {'page': '149_scan004', 'source': str(SOURCE), 'name': 'footer_full',
          'path': str(DEST), 'box': BOX, 'output_size': [WIDTH, height],
          'replaces_for_complete_boundary': 'result/crops/149_scan004_footer.png',
          'prior_file_preserved': True,
          'reason': 'Complete the upper ascenders of the final two prose lines (especially ferme) and include the full right source edge. This completes an unresolved boundary; the old crop remains unchanged.',
          'transform': 'RGB; autocontrast; LANCZOS resize; UnsharpMask radius 1.2, percent 110, threshold 3; no rotation',
          'viewed': False}
(BASE/'proposed/149_scan004_boundary_manifest.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
manifest_path = BASE/'proposed/149_scan004_crop_manifest.json'
manifest = json.loads(manifest_path.read_text())
for crop in manifest['crops']:
    crop['viewed'] = True
    crop['viewed_by'] = 'reader_b through tools.view_image; each successfully displayed once'
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
print(str(DEST))
