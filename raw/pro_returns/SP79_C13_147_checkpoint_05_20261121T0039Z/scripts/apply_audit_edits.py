"""Apply explicit main-reader edits after visual blind adjudication.

Input JSON supplies scan, exact page replacements, selected apparatus updates,
and additions. This tool makes no reading decisions. Committed first and second
readings and report second_boxes are never changed.
"""
import json, sys
from build_reports import ROOT
from integrity import atomic_write, verify_first, verify_comparison

payload=json.load(sys.stdin)
n=int(payload['scan']);stem=f'147_scan{n:03d}'
verify_first();verify_comparison(n)
page_path=ROOT/'pages'/f'{stem}.tex'
report_path=ROOT/'adjudicated'/f'{stem}.json'
page=page_path.read_text();report=json.loads(report_path.read_text())
if report.get('audit_completed'):
    raise SystemExit('Do not alter a completed audit through this helper.')
for edit in payload.get('page_replacements',[]):
    old,new=edit['old'],edit['new']
    if not old or page.count(old)!=edit['count']:
        raise ValueError(f'Exact page replacement count failed: {old!r}')
    page=page.replace(old,new)
for collection,key in [('changes','id'),('decisions','id')]:
    for update in payload.get(collection+'_updates',[]):
        matches=[x for x in report[collection] if x[key]==update[key]]
        if len(matches)!=1:raise ValueError(f'Expected one {collection} entry: {update[key]}')
        target=matches[0]
        for field,expected in update.get('expect',{}).items():
            if target.get(field)!=expected:raise ValueError(f'Unexpected old {collection}.{field}')
        # Witness quotations are supplied evidence and must not be rewritten.
        if collection=='changes' and set(update['fields'])&{'C','H'}:
            raise ValueError('Do not overwrite witness quotations in a reading update.')
        target.update(update['fields'])
    additions=payload.get(collection+'_add',[])
    existing={x[key] for x in report.get(collection,[])}
    for addition in additions:
        if addition[key] in existing:raise ValueError('Duplicate apparatus identifier')
        report.setdefault(collection,[]).append(addition);existing.add(addition[key])
remove=payload.get('doubts_remove',[])
for place in remove:
    if sum(d['place']==place for d in report.get('doubts',[]))!=1:
        raise ValueError(f'Expected exactly one doubt to remove: {place}')
report['doubts']=[d for d in report.get('doubts',[]) if d['place'] not in remove]
report['doubts'].extend(payload.get('doubts_add',[]))
for collection in ['notes','notation','hand_log','check_events']:
    report.setdefault(collection,[]).extend(payload.get(collection+'_add',[]))
atomic_write(page_path,page.encode())
atomic_write(report_path,(json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode())
print(f'Applied explicit page/apparatus edits for {stem}; audit approval still required.')
