"""Prepare an image-only rereading packet after all first readings are committed."""
from pathlib import Path
import csv, hashlib, json, shutil, sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent
SCANS = list(range(108,118)) + list(range(119,132))
scan = int(sys.argv[1])
reader = sys.argv[2]
assert scan in SCANS
assignments_path = ROOT/'review/assignments.json'
assignments = json.loads(assignments_path.read_text())
assert assignments['first'][str(scan)] != reader, 'The blind reader must differ from the first reader.'
assert all((ROOT/'review'/f'147_scan{s}_reviewed.json').exists() and (ROOT/'pages'/f'147_scan{s}.tex').exists() for s in SCANS), 'All 23 first readings must be committed before any blind reading.'
snapshot = ROOT/'second/first_readings_frozen.json'
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
if not snapshot.exists():
    files = [ROOT/'second'/f'147_scan{s}_{suffix}.tsv' for s in SCANS for suffix in ('boxes','first')]
    snapshot.write_text(json.dumps({'utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'sha256':{str(p.relative_to(ROOT)):digest(p) for p in files}}, indent=2)+'\n')
else:
    record = json.loads(snapshot.read_text())
    assert all(digest(ROOT/p)==h for p,h in record['sha256'].items()), 'A frozen first reading or box list changed.'
stem = f'147_scan{scan}'
packet = BASE/'blind_packets'/stem
packet.mkdir(parents=True, exist_ok=True)
shutil.copy2(BASE/'source/SP80_C13_147_scans'/f'{stem}.jpg', packet/'page.jpg')
shutil.copy2(ROOT/'second'/f'{stem}_boxes.tsv', packet/'boxes.tsv')
shutil.copy2(ROOT/'scripts/blind_reader_rules.md', packet/'rules.md')
assignments['second'][str(scan)] = reader
assignments_path.write_text(json.dumps(assignments,indent=2)+'\n')
print(packet)
