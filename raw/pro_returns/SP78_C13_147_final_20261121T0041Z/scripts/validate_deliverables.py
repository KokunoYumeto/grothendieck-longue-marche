#!/usr/bin/env python3
"""Structural checks only: no OCR, rendering, compilation or textual inference."""
from pathlib import Path
import csv,json,re,sys
from build_deliverables import clean, evidence
root=Path(__file__).resolve().parents[1]
scans=[54,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,72,73,74,75,76,77,78,79]
complete='--complete' in sys.argv
report_paths=sorted((root/'reviewed').glob('*.json'))
report_list=[json.loads(p.read_text()) for p in report_paths]
reports={int(p.stem[-3:]):r for p,r in zip(report_paths,report_list)}
issues=[]
def issue(s):issues.append(s)

def compare_table(name, fields, expected_rows, delimiter='\t'):
    """Compare parsed cells, including row order/count, using builder schemas."""
    path=root/name
    if not path.is_file():
        issue(f'Missing deliverable {name}')
        return
    try:
        with path.open(newline='') as f:
            reader=csv.reader(f,delimiter=delimiter,strict=True)
            header=next(reader,None)
            actual_rows=list(reader)
    except (OSError,csv.Error) as exc:
        issue(f'{name}: cannot read generated table: {exc}')
        return
    if header!=fields:
        issue(f'{name}: header does not match builder schema')
    if len(actual_rows)!=len(expected_rows):
        issue(f'{name}: row count {len(actual_rows)} does not match reviewed metadata {len(expected_rows)}')
    differing=[]
    for i,(actual,expected) in enumerate(zip(actual_rows,expected_rows),1):
        if actual==expected:
            continue
        changed=[fields[j] if j<len(fields) else f'extra cell {j+1}'
                 for j in range(max(len(actual),len(expected)))
                 if (actual[j] if j<len(actual) else None)!=(expected[j] if j<len(expected) else None)]
        labels=[f'{key}={expected[fields.index(key)]}'
                for key in ['id','scan','element','our_scan'] if key in fields]
        differing.append(f'row {i} ({", ".join(labels)}): {", ".join(changed)}')
    if differing:
        examples='; '.join(differing[:4])
        issue(f'{name}: {len(differing)} row(s) differ from reviewed metadata; {examples}')

if complete and set(reports)!=set(scans):issue(f'Approved scans mismatch: {sorted(reports)}')
for n,r in sorted(reports.items()):
    name=f'147_scan{n:03}';p=root/'pages'/f'{name}.tex'
    if not p.exists():issue(f'{name}: missing page');continue
    s=p.read_text()
    if not re.search(r'\\scanpage\{'+str(n)+r'\}',s):issue(f'{name}: wrong/missing scanpage')
    depth=0
    for c in re.sub(r'\\[{}%]|%[^\n]*','',s):
        if c=='{':depth+=1
        elif c=='}':depth-=1
        if depth<0:break
    if depth:issue(f'{name}: unbalanced curly braces {depth}')
    for c in r.get('changes',[]):
        if not (c.get('against_C') or c.get('against_H')):issue(f'{name}: no witness difference at {c.get("id")}')
        if not c.get('crop') or not (root/'crops'/Path(c['crop']).name).is_file():issue(f'{name}: missing change crop {c.get("id")}')
        if len(c.get('box',[]))!=4:issue(f'{name}: missing box {c.get("id")}')
    ids=[d['id'] for d in r.get('decisions',[])]
    if len(ids)!=len(set(ids)):issue(f'{name}: duplicate mark decision')
    for d in r.get('decisions',[]):
        if d['decision']!='undecided' and ('(' not in d.get('crop','') or '.png' not in d.get('crop','')):issue(f'{name}: resolved mark without a crop {d["id"]}')
    for row in r.get('inventory',[]):
        if row.get('transcribed')!='yes':issue(f'{name}: untranscribed inventory element {row.get("element")}')
    for suffix in ['boxes','first']+(['second'] if complete else []):
        if not (root/'second'/f'{name}_{suffix}.tsv').exists():issue(f'{name}: missing {suffix} reading')
    if complete and not r.get('audit_complete'):issue(f'{name}: audit not approved')
combined=root/'SP78_C13_147_transcription.tex'
page_files=sorted((root/'pages').glob('147_scan*.tex'))
if complete and [p.name for p in page_files]!=[f'147_scan{n:03}.tex' for n in scans]:
    issue('Page file coverage/order does not match the complete scan scope')
if not combined.is_file():
    issue('Missing deliverable SP78_C13_147_transcription.tex')
else:
    # The builder assembles every matching page file in filename order.
    target='\\cotefile{147}\n\n'+'\n\n'.join(p.read_text().rstrip() for p in page_files)+'\n'
    if combined.read_text()!=target:issue('Combined fragment does not match page files')

# Reproduce only the builder's deterministic table projections, not its writes.
decision_fields=['id','cote','scan','decision','reading','what the ink shows','crop','confidence']
decision_rows=[{**d,'what the ink shows':d.get('ink',d.get('what the ink shows',''))}
               for r in report_list for d in r.get('decisions',[])]
decision_rows.sort(key=lambda d:int(re.sub(r'\D','',d['id'])))
compare_table('decisions.tsv',decision_fields,
              [[clean(d.get(k,'')) for k in decision_fields] for d in decision_rows])

inventory_fields=['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']
inventory_rows=[row for r in report_list for row in r.get('inventory',[])]
# Unlike write_tsv, the builder's CSV writer preserves tabs and line breaks.
compare_table('SP78_C13_147_inventory.csv',inventory_fields,
              [['' if row.get(k,'') is None else str(row.get(k,'')) for k in inventory_fields]
               for row in inventory_rows],delimiter=',')

collation_fields=['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']
collation_rows=[]
for r in report_list:
    n=r['scan']
    for c in r.get('changes',[]):
        if c.get('against_H'):
            collation_rows.append(dict(folder=147,their_page=n-1,our_scan=n,line=c['place'],
                their_reading=c['H'],codex_reading=c['C'],final_reading=c['final'],
                scan_shows=evidence(c),kind=c.get('kind','other'),
                marked_in_H='yes' if c.get('marked_in_H') else 'no',confidence=c['confidence']))
compare_table('SP78_C13_147_collation.tsv',collation_fields,
              [[clean(row.get(k,'')) for k in collation_fields] for row in collation_rows])

if complete:
    expected=list(csv.DictReader((root.parent/'input/SP78_C13_147_texts/MARKS.tsv').open(),delimiter='\t'))
    if (root/'decisions.tsv').is_file():
        actual=list(csv.DictReader((root/'decisions.tsv').open(),delimiter='\t'))
        if [r['id'] for r in expected]!=[r.get('id') for r in actual]:issue('decisions.tsv does not reproduce all MARKS IDs in input order')
    for f in ['SP78_C13_147_changes.md','SP78_C13_147_collation.tsv','SP78_C13_147_doubts.md','SP78_C13_147_inventory.csv','SP78_C13_147_notes.md','SP78_C13_147_sheet_feedback.md','SP78_C13_147_hand_log.md','CHECK_EVENTS.tsv','progress.log']:
        if not (root/f).is_file():issue(f'Missing deliverable {f}')
pending_audits=[n for n,r in sorted(reports.items()) if not r.get('audit_complete')]
result={'approved_pages':len(reports),'complete_check':complete,'pending_audits':pending_audits,'issues':issues}
print(json.dumps(result,ensure_ascii=False,indent=2))
sys.exit(1 if issues else 0)
