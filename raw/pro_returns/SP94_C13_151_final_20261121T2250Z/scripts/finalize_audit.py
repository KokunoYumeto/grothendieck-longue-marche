"""Record a completed, manually adjudicated blind reading.

This script does not decide readings or edit transcription text. The main
reader must first inspect each disputed crop, edit the page/report as needed,
and fill every comparison decision and evidence field.
"""
from pathlib import Path
import csv, json, sys
from compile_records import WORK, now, compile_all

page = sys.argv[1]
with (WORK/'second'/(page+'_comparison.tsv')).open() as f:
    rows = list(csv.DictReader(f, delimiter='\t'))
assert rows
for row in rows:
    assert row['decision'] not in ('', 'PENDING'), (page, row['box'])
    assert row['changed'] in ('yes', 'no'), (page, row['box'])
    if row['same_tokens'] == 'no':
        assert row['evidence'].strip(), (page, row['box'], 'missing visual adjudication')
        crop = WORK/'crops'/('second_'+page+'_'+row['box']+'.jpg')
        assert crop.exists(), str(crop)

stamp = now()
summary = dict(boxes=len(rows), differences=sum(r['same_tokens']=='no' for r in rows),
               changed=sum(r['changed']=='yes' for r in rows), completed_utc=stamp)
rp = WORK/'reports'/(page+'.json')
report = json.loads(rp.read_text())
report['audit_summary'] = summary
rp.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
sp = WORK/'run_state.json'
state = json.loads(sp.read_text())
assert page in state['completed'] and page not in state['audited'], page
state['audited'].append(page)
sp.write_text(json.dumps(state, indent=2)+'\n')
with (WORK/'progress.log').open('a') as f:
    f.write(f"scan {report['scan']:03d} audited {stamp}: {summary['boxes']} boxes read, {summary['differences']} differences, {summary['changed']} changed\n")
print(json.dumps(dict(page=page, **summary, aggregate=compile_all())))
