"""Record an image-only assignment after all first readings are committed."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import sys

WORK = Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work')
EXPECTED = set(range(79,99)) | {100,101,102}

def assign(scan, reader):
    done = {int(p.stem[-3:]) for p in (WORK/'pages').glob('149_scan*.tex')}
    if done != EXPECTED:
        raise ValueError('Every first-pass page must be committed before the blind stage')
    assignments = list(csv.DictReader((WORK/'review/reader_assignments.tsv').open(), delimiter='\t'))
    first = {int(r['scan']): r['first_reader'] for r in assignments}
    if reader not in {'reader_a','reader_b','reader_c'} or reader == first[scan]:
        raise ValueError('Choose a different first-pass reader for this leaf')
    target = WORK/'review/second_assignments.tsv'
    prior = list(csv.DictReader(target.open(), delimiter='\t')) if target.exists() else []
    if any(int(r['scan']) == scan for r in prior):
        raise ValueError('This leaf already has a blind reader')
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with target.open('a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['scan','first_reader','blind_reader','assigned_utc'], delimiter='\t')
        if not prior:
            writer.writeheader()
        writer.writerow({'scan':scan,'first_reader':first[scan],'blind_reader':reader,'assigned_utc':stamp})
    with (WORK/'progress.log').open('a') as f:
        f.write(f'scan {scan:03d} blind assigned {stamp}: {reader}, first reader {first[scan]}\n')
    print(f'{scan:03d}: {reader}; image and anonymous boxes only')

if __name__ == '__main__':
    assign(int(sys.argv[1]), sys.argv[2])
