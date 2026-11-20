"""Explicit main-reader approval, called only after visual adjudication."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,sys,subprocess
ED=Path(__file__).resolve().parents[1]; ROOT=ED.parent
scan=int(sys.argv[1]);stem=f'145_scan{scan:03d}'
report=ED/'reader_reports'/(stem+'_reviewed.json')
if not report.exists(): raise SystemExit('Main-reader reviewed report is required')
r=json.loads(report.read_text())
assert r.get('main_reader_reviewed') is True
assert r['scan']==scan
assert (ED/'pages'/(stem+'.tex')).is_file()
source=list(csv.DictReader((ROOT/'source/SP75_C13_145_texts/MARKS.tsv').open(),delimiter='\t'))
required=[m['id'] for m in source if int(m['scan'])==scan]
assert [d['id'] for d in r['decisions']]==required, (required,[d['id'] for d in r['decisions']])
for c in r['changes']:
    assert c['c_changed'] or c['h_changed'], c
    assert c['confidence'] in ['high','medium','low']
    assert c.get('crop') and (ED/c['crop']).exists(),c['id']
    assert len(c['box'])==4
for d in r['decisions']:
    assert d['decision'] in ['first','alternative','other','undecided']
    if d['decision']!='undecided': assert d.get('crop') and (ED/d['crop']).exists(),d['id']
for b in r['second_boxes']: assert len(b['coords'])==4
assert len({b['box'] for b in r['second_boxes']})==len(r['second_boxes'])
subprocess.run([sys.executable,str(ED/'scripts/build_edition.py')],check=True)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
crops={c['crop'] for c in r['changes'] if c.get('crop')}|{d['crop'] for d in r['decisions'] if d.get('crop')}
with (ED/'progress.log').open('a') as f:
    f.write(f"scan {scan:03d} done {now} cote 145: {r['lines_read']} lines read, {r.get('crop_count',len(list((ED/'crops').glob(stem+'*.png'))))} places cropped, {len(r['changes'])} rows\n")
print(stem+' finalized '+now)
