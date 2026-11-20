"""Commit all first readings and neutral box lists before blind reading starts."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json
from build_reports import ROOT, ORDER, second_prepare

manifest=ROOT/'second/FIRST_READING_SHA256.tsv'
if manifest.exists():
    raise SystemExit('Blind inputs have already been committed; do not overwrite them.')
for n in ORDER:
    report=ROOT/'adjudicated'/f'147_scan{n:03d}.json'
    if not report.exists() or not json.loads(report.read_text()).get('main_reader_reviewed'):
        raise SystemExit(f'All first readings must be approved before this phase: missing {n:03d}.')
for n in ORDER:
    second_prepare(n)
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
rows=[]
for n in ORDER:
    for suffix in ('boxes.tsv','first.tsv'):
        p=ROOT/'second'/f'147_scan{n:03d}_{suffix}'
        rows.append({'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
with manifest.open('w',newline='') as f:
    writer=csv.DictWriter(f,['path','sha256'],delimiter='\t');writer.writeheader();writer.writerows(rows)
with (ROOT/'progress.log').open('a') as f:
    f.write(f'blind first readings committed {stamp}: {len(ORDER)} pages; {len(rows)} input files; neutral box identifiers and kinds\n')
    for row in rows:f.write(f'BLIND-INPUT-SHA-256 {row["path"]} {row["sha256"]}\n')
print(f'Committed {len(rows)} blind input files at {stamp}')
