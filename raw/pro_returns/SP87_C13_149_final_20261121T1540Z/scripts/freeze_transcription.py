"""Freeze or verify the final page bytes after all visual audits are complete."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import csv
import hashlib

WORK = Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work')
SCANS = list(range(79, 99)) + [100, 101, 102]


def stamp():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verify', action='store_true')
    args = parser.parse_args()
    record = WORK/'review/frozen_hashes.tsv'
    progress = WORK/'progress.log'
    if args.verify:
        rows = list(csv.DictReader(record.open(), delimiter='\t'))
        for row in rows:
            if digest(WORK/row['path']) != row['sha256']:
                raise SystemExit('Frozen transcription changed: '+row['path'])
        with progress.open('a') as f:
            f.write(f'frozen hashes verified unchanged {stamp()}: {len(rows)} files\n')
        print(f'All {len(rows)} frozen hashes are unchanged.')
        return
    if record.exists():
        raise SystemExit('The transcription was already frozen; use --verify.')
    log = progress.read_text()
    for scan in SCANS:
        if f'scan {scan:03d} audited ' not in log:
            raise SystemExit(f'Scan {scan:03d} has not completed its blind audit.')
    paths = [WORK/'pages'/f'149_scan{s:03d}.tex' for s in SCANS]
    paths.append(WORK/'SP87_C13_149_transcription.tex')
    rows = [{'path':p.relative_to(WORK).as_posix(),'sha256':digest(p)} for p in paths]
    with record.open('x', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['path','sha256'], delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)
    with progress.open('a') as f:
        f.write(f'transcription frozen {stamp()}\n')
        for row in rows:
            f.write(f'SHA-256 {row["sha256"]} {row["path"]}\n')
    print(f'Frozen {len(rows)} files.')


if __name__ == '__main__':
    main()
