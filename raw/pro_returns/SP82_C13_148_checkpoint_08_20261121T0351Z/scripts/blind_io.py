"""Prepare image-only blind inputs and crop their prescribed rectangles.

No recognition, proposed reading, or comparison occurs in this script.
The crop command opens only the copied source image and the public box list.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import shutil
import sys
from PIL import Image, ImageOps, ImageFilter

OUT = Path(__file__).resolve().parents[1]
ROOT = OUT.parents[1]
INPUTS = ROOT / 'work/blind_inputs'
DISPLAY = ROOT / 'work/blind_display'
SCANS = [21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,41,42,43,44,46,47]


def prepare():
    import assemble
    approved = assemble.approved()
    assert [int(p['scan']) for p in approved] == SCANS, 'All first readings must be approved.'
    progress = (OUT / 'progress.log').read_text()
    assert all(f'scan {n:03d} done ' in progress for n in SCANS)
    for n in SCANS:
        stem = f'148_scan{n:03d}'
        assert not (OUT / 'second' / f'{stem}_first.tsv').exists(), 'Never overwrite first readings.'
        assemble.second_files(n)
        dest = INPUTS / stem
        dest.mkdir(parents=True, exist_ok=False)
        shutil.copy2(ROOT / 'source/SP82_C13_148_scans' / f'{stem}.jpg', dest / 'scan.jpg')
        shutil.copy2(OUT / 'second' / f'{stem}_boxes.tsv', dest / 'boxes.tsv')
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (OUT / 'progress.log').open('a') as f:
        f.write(f'all24 first readings complete; all blind box lists and first readings written {now}; no blind reader has yet received a page\n')
    print('Prepared all24 image-only inputs after first-pass completion.')


def crop(n):
    stem = f'148_scan{n:03d}'
    packet = INPUTS / stem
    with (packet / 'boxes.tsv').open(newline='') as f:
        boxes = list(csv.DictReader(f, delimiter='\t'))
    im = Image.open(packet / 'scan.jpg')
    dest = OUT / 'crops/second' / stem
    display = DISPLAY / stem
    dest.mkdir(parents=True, exist_ok=True)
    display.mkdir(parents=True, exist_ok=True)
    manifest = []
    for b in boxes:
        name = b['box']
        assert all(c.isalnum() or c in '-_.' for c in name)
        rect = tuple(int(b[k]) for k in ('x0','y0','x1','y1'))
        assert 0 <= rect[0] < rect[2] <= im.width and 0 <= rect[1] < rect[3] <= im.height, (name, rect, im.size)
        evidence = dest / f'{name}.png'
        if not evidence.exists():
            im.crop(rect).save(evidence, optimize=True)
        proxy = display / f'{name}.jpg'
        if not proxy.exists():
            c = ImageOps.autocontrast(Image.open(evidence).convert('RGB'))
            w = min(2500, max(900, c.width * 2))
            c = c.resize((w, round(c.height*w/c.width)), Image.Resampling.LANCZOS)
            c = c.filter(ImageFilter.UnsharpMask(radius=1, percent=110, threshold=3))
            c.save(proxy, quality=96, subsampling=0)
        manifest.append({'box':name, 'kind':b['kind'], 'pixels':rect,
                         'evidence':str(evidence), 'display':str(proxy)})
    (OUT / 'second' / f'{stem}_crop_manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print(json.dumps(manifest, ensure_ascii=False))


def restore_inputs():
    """Recreate disposable image-only packets without touching first readings."""
    for n in SCANS:
        stem = f'148_scan{n:03d}'
        assert (OUT/'second'/f'{stem}_first.tsv').is_file()
        box_file = OUT/'second'/f'{stem}_boxes.tsv'
        assert box_file.is_file()
        packet = INPUTS/stem
        packet.mkdir(parents=True, exist_ok=True)
        if not (packet/'scan.jpg').exists():
            shutil.copy2(ROOT/'source/SP82_C13_148_scans'/f'{stem}.jpg',packet/'scan.jpg')
        if not (packet/'boxes.tsv').exists():
            shutil.copy2(box_file,packet/'boxes.tsv')
        else:
            assert (packet/'boxes.tsv').read_bytes()==box_file.read_bytes()
    print('Recreated disposable blind inputs; first readings unchanged.')


if __name__ == '__main__':
    if sys.argv[1] == 'prepare':
        prepare()
    elif sys.argv[1] == 'crop':
        crop(int(sys.argv[2]))
    elif sys.argv[1] == 'restore-inputs':
        restore_inputs()
    else:
        raise SystemExit('Use prepare, crop N, or restore-inputs.')
