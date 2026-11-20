"""Prepare one isolated page packet after its predecessor is committed; never opens images."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, json, re, shutil
ap=argparse.ArgumentParser()
ap.add_argument('scan',type=int)
ap.add_argument('brief',help='Existing brief filename in briefs/')
a=ap.parse_args()
out=Path(__file__).resolve().parents[1]
if not 3<=a.scan<=17:raise ValueError('Sequential continuation scans are 003–017')
progress=(out/'progress.log').read_text()
if f'scan {a.scan-1:03d} done ' not in progress:raise RuntimeError('Previous page is not committed')
if f'scan {a.scan:03d} done ' in progress:raise RuntimeError('This page is already committed')
brief=out/'briefs'/a.brief
if not brief.is_file():raise FileNotFoundError(brief)
packet=out.parent/f'reader_inputs/scan{a.scan:03d}'
p=packet/'C_context.md';removed=[];kept=[]
for line in p.read_text().splitlines():
    m=re.match(r'^\|\s*(\d+)(?=\D|$)',line)
    if m and int(m.group(1))!=a.scan:removed.append(line)
    else:kept.append(line)
if removed:p.write_text('\n'.join(kept)+'\n')
snapshot=out/f'briefs/notation_before_scan{a.scan:03d}.md'
if snapshot.exists():raise RuntimeError('Notation snapshot already exists; do not overwrite a reader input')
shutil.copyfile(out/'notation.md',snapshot)
record=out/f'records/scan{a.scan:03d}';record.mkdir(parents=True,exist_ok=True)
(record/'packet_check.json').write_text(json.dumps({'scan':a.scan,'brief':a.brief,'excluded_primary_other_scan_rows':removed,'packet_files':sorted(x.name for x in packet.iterdir()),'prior_page_committed':True},ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (out/'progress.log').open('a') as f:f.write(f'scan {a.scan:03d} packet and notation snapshot prepared {now}; brief={a.brief}\n')
print(json.dumps({'scan':a.scan,'removed_rows':removed,'brief':str(brief),'notation':str(snapshot),'packet':str(packet)},ensure_ascii=False))
