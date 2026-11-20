"""Commit an adjudicated scan, rebuild cumulative deliverables, then log completion."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,csv,subprocess
p=argparse.ArgumentParser();p.add_argument('scan',type=int);a=p.parse_args()
r=Path(__file__).resolve().parents[1];n=a.scan
order=[2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
record=r/'records'/f'scan{n:03d}.json'
d=json.loads(record.read_text())
assert d['scan']==n and d.get('main_adjudicated') is True
for prev in order[:order.index(n)]:
    assert f'scan {prev:03d} done ' in (r/'progress.log').read_text(),f'Previous scan {prev} not complete'
for role in ['A','B','C']:
    rr=r/'readers'/f'{n:03d}'/role
    assert (rr/'report.json').is_file() and (rr/'reading.tex').is_file(),f'Reader {role} missing'
page=r/'pages'/d['filename']
assert page.is_file()
validation_path=r/'scripts/validate.py'
validation_ns={'__file__':str(validation_path)}
exec(validation_path.read_text().split('records=')[0],validation_ns)
source_result=validation_ns['check_tex'](page)
assert not source_result['errors'],source_result
if d.get('root_page_text_exact') is not None:
    assert page.read_text()==d['root_page_text_exact'],'Page changed after root approval'
assert len({x['id'] for x in d['decisions']})==len(d['decisions'])
for item in d['doubts']:
    assert all(k in item for k in ('location','reading','confidence'))
for item in d.get('abbreviations',[]):
    assert all(k in item for k in ('form','expansion'))
assert all(i['transcribed']=='yes' for i in d['inventory'])
for item in d['decisions']:
    assert set(item['readers'])=={'A','B','C'},item['id']
    if d['hua_has']!='text':assert not item.get('diff_H'),item['id']
subprocess.run(['python',str(r/'scripts/build_records.py')],check=True)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (r/'progress.log').open('a') as f:f.write(f'scan {n:03d} done {now}\n')
print(f'scan {n:03d} committed {now}')
