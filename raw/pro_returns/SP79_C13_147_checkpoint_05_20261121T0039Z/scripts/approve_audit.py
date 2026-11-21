"""Record a main-reader blind adjudication; never infer or edit source readings."""
from datetime import datetime, timezone
import csv, hashlib, json, sys
from build_reports import ROOT, build
from integrity import verify_first, verify_comparison, verify_views

n=int(sys.argv[1]);stem=f'147_scan{n:03d}'
report_path=ROOT/'adjudicated'/f'{stem}.json'
r=json.loads(report_path.read_text())
if r.get('audit_completed'):raise SystemExit('Audit already approved; do not append a duplicate event.')
verify_first()
cmp=verify_comparison(n)
review=json.loads((ROOT/'second'/f'{stem}_adjudication.json').read_text())
verify_views(n,review['second_reader'])
assert review['second_reader']!=r['reader'],'Blind reader must differ from the first reader'
expected={x['box']:x for x in cmp['items']}
decisions=review['decisions']
assert len(decisions)==len({d['box'] for d in decisions})
assert {d['box'] for d in decisions}==set(expected),'Every differing box must be adjudicated'
for d in decisions:
    item=expected[d['box']]
    assert d['first']==item['first'] and d['second']==item['second'],'Preserve both committed readings verbatim'
    assert isinstance(d['changed'],bool) and d['ink'] and d['final']
    assert (ROOT/d['crop']).exists(),'Every adjudication requires a viewed crop'
    # A box can contain several distinct disagreements.  Explicit operation
    # coverage prevents a decision on one word from standing for the rest.
    covered=[]
    for resolution in d['token_resolutions']:
        assert resolution['decision'] and resolution['ink']
        covered.extend(resolution['operations'])
    assert sorted(covered)==list(range(len(item['token_differences']))), 'Every token operation must be adjudicated exactly once'
token_rows=[]
for d in decisions:
    item=expected[d['box']]
    for resolution in d['token_resolutions']:
        for op_index in resolution['operations']:
            op=item['token_differences'][op_index]
            token_rows.append({'box':d['box'],'operation_index':op_index,
                'first_tokens':json.dumps(op['first_tokens'],ensure_ascii=False),
                'second_tokens':json.dumps(op['second_tokens'],ensure_ascii=False),
                'decision':resolution['decision'],'ink':resolution['ink'],
                'crop':d['crop']})
with (ROOT/'second'/f'{stem}_token_adjudication.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,['box','operation_index','first_tokens','second_tokens','decision','ink','crop'],delimiter='\t')
    w.writeheader();w.writerows(token_rows)
r['audit_decisions']=decisions
r['second_reader']=review['second_reader']
r['audit_completed']=True
r['audited_at']=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
if review.get('notes'):r.setdefault('notes',[]).extend(review['notes'])
report_path.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
build()
changed=sum(d['changed'] for d in decisions)
with (ROOT/'progress.log').open('a') as f:
    f.write(f'scan {n:03d} audited {r["audited_at"]}: {cmp["boxes"]} boxes read, {cmp["differences"]} differences, {changed} changed\n')
print(f'Approved blind audit {n:03d}: {cmp["boxes"]} boxes, {cmp["differences"]} differing boxes, {changed} changed boxes')
