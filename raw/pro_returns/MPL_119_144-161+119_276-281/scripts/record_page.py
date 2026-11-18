"""Append a visually completed page's manual inventory and timestamp.

This performs no image recognition and makes no inference about completeness.
The root transcriber supplies every inventory entry after viewing the images.
"""
import csv
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_119_144-161+119_276-281'

def record(scan, sheet_kind, elements):
    page = ROOT / 'pages' / f'{PREFIX}_119_scan{scan:03d}.tex'
    if not page.exists():
        raise FileNotFoundError(page)
    with (ROOT / f'{PREFIX}_inventory.csv').open('a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for i, (kind, position, words) in enumerate(elements, 1):
            writer.writerow([119, scan, sheet_kind, f'{scan}-{i:02d}', kind, position, words, 'yes'])
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT / 'progress.log').open('a', encoding='utf-8') as f:
        f.write(f'119 scan {scan:03d} done {now}\n')
    print(f'119 scan {scan:03d} done {now}; {len(elements)} inventory elements')
