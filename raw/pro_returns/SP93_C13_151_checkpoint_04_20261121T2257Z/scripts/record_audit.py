"""Record explicit main-reader adjudications after a blind comparison.

This does not decide any ink reading. The supplied audit JSON must contain one
decision for every differing box, with final reading, crop evidence and an
explicit changed flag. First and second reading TSVs are never modified.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, csv, hashlib, json
from assemble import commit

ROOT=Path('/workspace/scratch/d12e26a9cd50')
OUT=ROOT/'SP93_C13_151_work'

def rows(path):
    with path.open(newline='') as f:
        return list(csv.DictReader(f,delimiter='\t'))

def main(scan):
    scan=f'{int(scan):03d}'; name=f'151_scan{scan}'
    comparison=rows(OUT/'second'/f'{name}_comparison.tsv')
    boxes={x['box']:[int(x[k]) for k in ['x0','y0','x1','y1']] for x in rows(OUT/'second'/f'{name}_boxes.tsv')}
    decisions=json.loads((OUT/'reviews'/f'{name}_audit.json').read_text())
    wanted=[x for x in comparison if x['same_tokens']=='no']
    if [x['box'] for x in decisions] != [x['box'] for x in wanted]:
        raise ValueError('Every differing box must have one ordered adjudication.')
    for d,c in zip(decisions,wanted):
        if not isinstance(d.get('changed'),bool) or not d.get('evidence') or not d.get('final'):
            raise ValueError('Missing explicit decision, evidence, or changed flag.')
        d['first']=c['first'];d['second']=c['second'];d['pixel_box']=boxes[d['box']]
        if not d.get('crop') or not (OUT/d['crop']).is_file():
            raise ValueError('Every adjudication requires an existing viewed crop.')
    p=OUT/'reports'/f'{name}.json';report=json.loads(p.read_text())
    if report.get('second_audit_complete'):
        raise ValueError('Page audit already recorded; do not silently overwrite its event.')
    report['second_adjudications']=decisions
    report['second_audit_complete']=True
    report['first_reading_sha256']=hashlib.sha256((OUT/'second'/f'{name}_first.tsv').read_bytes()).hexdigest()
    report['second_reading_sha256']=hashlib.sha256((OUT/'second'/f'{name}_second.tsv').read_bytes()).hexdigest()
    p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    commit(scan,preserve_first=True)
    stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (OUT/'progress.log').open('a') as f:
        f.write(f'scan {scan} audited {stamp}: {len(comparison)} boxes read, {len(wanted)} differences, {sum(d["changed"] for d in decisions)} changed\n')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('scan');main(p.parse_args().scan)
