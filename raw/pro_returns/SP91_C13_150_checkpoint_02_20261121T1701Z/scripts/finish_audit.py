"""Record an audit only after the main reader's image adjudications and edits.

No transcription is inferred or changed by this script. The main reader writes
the adjudication table and updates the page and substantive comparison record.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, subprocess, sys

ROOT=Path(__file__).resolve().parents[1]
def now():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
for scan in sys.argv[1:]:
    s=f'{int(scan):03}';stem='150_scan'+s
    rp=ROOT/'records'/f'{stem}.json';r=json.loads(rp.read_text())
    assert not r.get('audited'), 'Audit already recorded: '+s
    comparison=json.loads((ROOT/'second'/f'{stem}_comparison.json').read_text())
    with (ROOT/'second'/f'{stem}_adjudication.tsv').open() as f:
        adjudications=list(csv.DictReader(f,delimiter='\t'))
    differences=[x for x in comparison if x['different']]
    assert [x['box'] for x in differences]==[x['box'] for x in adjudications]
    changed=set()
    for d,a in zip(differences,adjudications):
        assert a['first']==d['first'] and a['second']==d['second'], (s,a['box'],'reading altered in adjudication')
        assert a['final'] and a['evidence'] and a['box_pixels']
        assert a['changed'] in ['yes','no'] and a['confidence'] in ['high','medium','low']
        assert (ROOT/a['crop']).exists()
        if a['changed']=='yes':
            ids=[i.strip() for i in a['change_ids'].split(';') if i.strip()]
            assert ids,(s,a['box'],'changed place needs its record ID')
            changed.update(ids)
    r['audit_adjudications']=adjudications
    r['audited']=True;r['audited_at']=now()
    r['audit_summary']={'boxes':len(comparison),'differences':len(differences),'changed_places':len(changed),'change_ids':sorted(changed)}
    rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    subprocess.run([sys.executable,str(ROOT/'scripts/build_outputs.py'),'build'],check=True)
    with (ROOT/'progress.log').open('a') as f:
        f.write(f'scan {s} audited {now()}: {len(comparison)} boxes read, {len(differences)} differences, {len(changed)} changed\n')
    print(json.dumps({'scan':s,**r['audit_summary']}))
