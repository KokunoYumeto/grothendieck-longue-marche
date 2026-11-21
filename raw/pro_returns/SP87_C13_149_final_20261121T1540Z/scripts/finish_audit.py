"""Record a completed visual adjudication; no inference or image reading occurs here."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import sys
import aggregate

WORK = Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work')
def rows(path):
    return list(csv.DictReader(path.open(), delimiter='\t'))

def finish(scan):
    page=f'149_scan{scan:03d}'
    second=WORK/'second'
    prior=json.loads((second/f'{page}_comparison_hashes.json').read_text())
    for which in ['first','second']:
        got=hashlib.sha256((second/f'{page}_{which}.tsv').read_bytes()).hexdigest()
        if got!=prior[which]:raise ValueError(f'{which} reading changed after comparison')
    comparisons=rows(second/f'{page}_comparison.tsv')
    decisions=rows(second/f'{page}_adjudications.tsv')
    if [r['box'] for r in comparisons]!=[r['box'] for r in decisions]:
        raise ValueError('Adjudications must cover every token-different box in order')
    for c,d in zip(comparisons,decisions):
        if c['first']!=d['first'] or c['second']!=d['second']:
            raise ValueError('Adjudication does not preserve both frozen readings')
        if d['changed'] not in ['yes','no'] or not d['evidence']:
            raise ValueError('Each adjudication needs an explicit outcome and evidence')
        if not (WORK/d['crop']).is_file():raise ValueError('Missing adjudication crop')
    progress=WORK/'progress.log'
    if f'scan {scan:03d} audited ' in progress.read_text():raise ValueError('Audit already recorded')
    aggregate.rebuild()
    stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    count=len(rows(second/f'{page}_boxes.tsv'))
    changed=sum(d['changed']=='yes' for d in decisions)
    line=f'scan {scan:03d} audited {stamp}: {count} boxes read, {len(decisions)} differences, {changed} changed'
    with progress.open('a') as f:f.write(line+'\n')
    print(line)

if __name__=='__main__':
    finish(int(sys.argv[1]))
