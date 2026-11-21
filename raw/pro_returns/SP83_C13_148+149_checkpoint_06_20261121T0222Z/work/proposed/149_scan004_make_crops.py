from pathlib import Path
import json
from PIL import Image, ImageOps, ImageFilter

BASE = Path('/workspace/scratch/f28c4f52d3ec')
PAGE = '149_scan004'
SOURCE = BASE / 'source/SP83_C13_148+149_scans/149_scan004.jpg'
PLACES = [
    ('opening', [280, 65, 1625, 360], 4000, 'Opening Spec map, Topos capitalization, and complete opening prose'),
    ('formula1', [275, 370, 995, 475], 3300, 'Whole first displayed formula including handwritten (1), shaft, and target superscript'),
    ('formula2', [260, 580, 1230, 700], 3700, 'Whole second displayed formula including handwritten (2), arrow, target superscript, and point'),
    ('closure', [275, 725, 1665, 1080], 4200, 'Cancelled cloture and closing parenthesis; whole closure phrase and raised K-bar-prime'),
    ('definition', [280, 1080, 1640, 1325], 4200, 'Whole inline Pi expression and closure definition, associated word/on, raised alg and sep state'),
    ('groups', [280, 1335, 1630, 1665], 4000, 'Complete corresponding-points prose including de/des groupes'),
    ('formula3', [275, 1695, 1240, 1850], 3700, 'Whole third displayed formula including handwritten (3), shaft and both target superscripts'),
    ('restriction', [280, 1810, 1640, 2180], 4200, 'Complete reconstruction sentence, accent in reconstituer and quote forms'),
    ('footer', [280, 2180, 1665, 2345], 4200, 'Marginal 1-like mark and whole final two lines with reference (3) and E index'),
    ('folio', [20, 2305, 105, 2358], 1100, 'Pale lower folio 3'),
]

image = Image.open(SOURCE).convert('RGB')
assert image.size == (1678, 2366)
manifest = {'page': PAGE, 'source': str(SOURCE), 'source_size': list(image.size),
            'transform': 'RGB; autocontrast; LANCZOS resize; UnsharpMask radius 1.2, percent 110, threshold 3; no rotation',
            'view_protocol': 'Original displayed once; half1 displayed once; half2 displayed once. Evidence crops are not second-pass crops.',
            'crops': []}
for name, box, width, purpose in PLACES:
    dest = BASE / 'result/crops' / f'{PAGE}_{name}.png'
    if dest.exists():
        raise FileExistsError(f'Preserve existing evidence: {dest}')
    crop = ImageOps.autocontrast(image.crop(box))
    height = round(crop.height * width / crop.width)
    crop = crop.resize((width, height), Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))
    crop.save(dest)
    manifest['crops'].append({'place': name, 'box': box, 'path': str(dest),
                              'output_size': [width, height], 'purpose': purpose, 'viewed': False})
(BASE / 'proposed' / f'{PAGE}_crop_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'page': PAGE, 'places': len(PLACES), 'manifest': str(BASE/'proposed'/f'{PAGE}_crop_manifest.json'),
                  'files': [{'place': c['place'], 'bytes': Path(c['path']).stat().st_size} for c in manifest['crops']]}, indent=2))
