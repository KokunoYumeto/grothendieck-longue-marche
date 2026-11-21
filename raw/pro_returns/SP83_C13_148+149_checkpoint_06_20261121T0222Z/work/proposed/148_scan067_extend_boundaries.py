from pathlib import Path
from PIL import Image, ImageOps, ImageFilter

root = Path('/workspace/scratch/f28c4f52d3ec')
source = root / 'source/SP83_C13_148+149_scans/148_scan067.jpg'
specs = {
    'opening_full': ((183, 0, 1080, 530), 3800),
    'card_title_full': ((1190, 0, 2945, 245), 4400),
    'cancelled_def_full': ((1190, 193, 2746, 634), 4500),
    'edge_condition_full': ((1410, 498, 2210, 730), 3900),
}
im = Image.open(source).convert('RGB')
for name, (box, width) in specs.items():
    target = root / 'result/crops' / f'148_scan067_{name}.png'
    if target.exists():
        raise FileExistsError(target)
    cropped = ImageOps.autocontrast(im.crop(box))
    cropped = cropped.resize((width, round(width * cropped.height / cropped.width)), Image.Resampling.LANCZOS)
    cropped = cropped.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))
    cropped.save(target)
    print(name, list(box), flush=True)
