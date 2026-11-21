from pathlib import Path
import argparse
import csv
import json
import shutil

ROOT = Path('/workspace/scratch/d12e26a9cd50')
SOURCE = ROOT / 'source'
OUTPUT = ROOT / 'SP93_C13_151_work'
WORK = ROOT / 'reading_work'

def prepare(scan):
    scan = f'{int(scan):03d}'
    name = f'151_scan{scan}'
    packet = WORK / 'packets' / name
    packet.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE / 'SP93_C13_151_texts/pages' / f'{name}.tex', packet / 'C.tex')
    h = SOURCE / 'SP93_C13_151_texts/hua' / f'hua_{name}.tex'
    if h.exists():
        shutil.copyfile(h, packet / 'H.tex')
    else:
        (packet / 'H_ABSENT.txt').write_text('There is no witness H for this scan.\n')
    shutil.copyfile(SOURCE / 'SP93_C13_151_texts/PREAMBLE.tex', packet / 'PREAMBLE.tex')
    shutil.copyfile(OUTPUT / 'notation_current.md', packet / 'notation.md')
    with (SOURCE / 'SP93_C13_151_texts/MARKS.tsv').open(newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        marks = [r for r in reader if int(r['scan']) == int(scan)]
        fields = reader.fieldnames
    with (packet / 'MARKS.tsv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fields, delimiter='\t')
        writer.writeheader()
        writer.writerows(marks)
    with (SOURCE / 'SP93_C13_151_C_H_differences.tsv').open(newline='') as f:
        # Source TSV is literal tab-separated text: TikZ quote characters are
        # manuscript/witness data, not CSV quoting. Every physical row has five fields.
        reader = csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
        diffs = [dict(id=f'D{i:04d}', **r) for i, r in enumerate(reader, 1) if r['page'] == name]
        fields = ['id'] + reader.fieldnames
    with (packet / 'differences.tsv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fields, delimiter='\t')
        writer.writeheader()
        writer.writerows(diffs)
    image = SOURCE / 'SP93_C13_151_scans' / f'{name}.jpg'
    (packet / 'image_path.txt').write_text(str(image) + '\n')
    print(json.dumps({'scan': scan, 'packet': str(packet), 'image': str(image), 'marks': len(marks), 'difference_rows': len(diffs)}))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('scans', nargs='+')
    for n in parser.parse_args().scans:
        prepare(n)
