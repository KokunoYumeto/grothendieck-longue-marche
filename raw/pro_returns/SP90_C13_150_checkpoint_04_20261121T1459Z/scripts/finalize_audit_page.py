"""Log a manually adjudicated image-only second reading, without choosing ink.

Before running, the editor must inspect every differing crop, fill every
comparison decision, update the page and all affected records, and write an
explicit audit_review field to the page's editorial JSON.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, csv, json, subprocess, sys

ROOT=Path(__file__).resolve().parents[1]

def main():
    p=argparse.ArgumentParser();p.add_argument('scan',type=int);p.add_argument('--changed',type=int,required=True);a=p.parse_args()
    stem=f'150_scan{a.scan:03}'
    meta=ROOT/'editor'/f'{stem}.json';d=json.loads(meta.read_text())
    if not d.get('audit_review'):raise RuntimeError('Explicit visual audit review required')
    log=ROOT/'progress.log'
    if f'scan {a.scan:03} audited ' in log.read_text():raise RuntimeError('Audit already logged')
    with (ROOT/'second'/f'{stem}_comparison.tsv').open(newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
    diffs=[r for r in rows if r['different']=='yes']
    for r in diffs:
        for k in ('adjudicated_reading','decision','evidence','crop'):
            if not r.get(k):raise RuntimeError(f'Unadjudicated {r["box"]}: {k}')
        if not (ROOT/'crops'/r['crop']).is_file():raise RuntimeError('Missing audit crop '+r['crop'])
    if not 0<=a.changed<=len(diffs):raise RuntimeError('Changed count must be between zero and difference count')
    subprocess.run([sys.executable,str(ROOT/'scripts/freeze_first_readings.py'),'--verify'],check=True,capture_output=True,text=True)
    build=subprocess.run([sys.executable,str(ROOT/'scripts/build_records.py')],check=True,capture_output=True,text=True)
    check=subprocess.run([sys.executable,str(ROOT/'scripts/check_edition.py')],capture_output=True,text=True)
    if check.returncode:raise RuntimeError(check.stdout+check.stderr)
    stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    d['audited_at']=stamp;d['audit_counts']={'boxes':len(rows),'differences':len(diffs),'changed':a.changed}
    meta.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    with log.open('a') as f:f.write(f'scan {a.scan:03} audited {stamp}: {len(rows)} boxes read, {len(diffs)} differences, {a.changed} changed\n')
    print(json.dumps({'scan':a.scan,'utc':stamp,**d['audit_counts'],'cumulative':json.loads(build.stdout)},indent=2))

if __name__=='__main__':main()
