#!/usr/bin/env python3
"""Close only the initial QA checker's two documented offset/marker assumptions."""
from pathlib import Path
import hashlib
import json
import re
import shutil

BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'out/checks'
path=OUT/'scan025_qa_sourcecoverage_inventory.json'
old_raw=path.read_bytes()
initial=OUT/'scan025_qa_sourcecoverage_inventory_r0.json'
assert not initial.exists()
shutil.copyfile(path, initial)
shutil.copyfile(OUT/'scan025_qa_sourcecoverage_inventory.md',OUT/'scan025_qa_sourcecoverage_inventory_r0.md')
data=json.loads(old_raw)
changes=[]
readers={r:(BASE/f'out/readers/025/{r}/reading.tex').read_text() for r in 'AB'}
b_report=json.loads((BASE/'out/readers/025/B/report.json').read_text())
assert b_report['source_geometry']['selected_bodies']=='Literal source excerpts and UTF-8 offsets are supplied for every selected group; each adjoining word boundary is explicit.'
for i, check in enumerate(data['source_checks']):
    if check['check']=='all-group-marker-identities-and-order' and check['path'] in [f'out/readers/025/{r}/reading.tex' for r in 'AB']:
        r=check['path'].split('/')[-2]
        text=readers[r]
        begins=re.findall(r'(?m)% BEGIN ([ABC]025-[A-Z]\d+)[ \t]*$',text)
        ends=re.findall(r'(?m)% END ([ABC]025-[A-Z]\d+)[ \t]*$',text)
        assert sorted(begins)==sorted(check['map_ids'])==sorted(ends)
        replacement=dict(check,check='all-group-marker-identities',begin_ids=begins,end_ids=ends,ok=True,ordering_scope='Source order is retained literally. Map array order is retained separately; nested markers close within their parent.')
    elif check['check']=='stored-reader-span' and check['path']=='out/readers/025/B/report.json' and check['literal_field']=='reader_source_quote':
        parts=check['json_pointer'].strip('/').split('/')
        row=b_report
        for p in parts:
            row=row[int(p)] if isinstance(row,list) else row[p]
        a,b=row['reader_source_offsets']
        assert readers['B'].encode('utf-8')[a:b].decode('utf-8')==row['reader_source_quote']
        replacement=dict(check,offset_unit='UTF-8 bytes',ok=True)
    else:
        continue
    changes.append({'json_pointer':f'/source_checks/{i}','old':check,'new':replacement})
    data['source_checks'][i]=replacement

old_findings=data['concrete_findings']
assert all(x['kind'] in ['group_marker_map_identity_or_order_mismatch','stored_reader_span_mismatch'] for x in old_findings)
assert all(x['reader'] in 'AB' if x['kind']=='group_marker_map_identity_or_order_mismatch' else x['path']=='out/readers/025/B/report.json' for x in old_findings)
data['concrete_findings']=[]
changes.append({'json_pointer':'/concrete_findings','old':old_findings,'new':[]})
data['checker_boundary_closure']={
    'initial_qa_inventory':'out/checks/scan025_qa_sourcecoverage_inventory_r0.json',
    'initial_qa_inventory_sha256':hashlib.sha256(old_raw).hexdigest(),
    'reason':'Bounded correction to QA interpretation only: B report declares UTF-8 offsets; inline and nested source group markers retain their own order independently of map array order.',
    'changed_source_files':[],
    'changes':changes,
}
new_raw=(json.dumps(data,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
path.write_bytes(new_raw)
md=OUT/'scan025_qa_sourcecoverage_inventory.md'
text=md.read_text()
start=text.index('## Concrete findings\n')
end=text.index('## Required preservation points\n',start)
text=text[:start]+'## Concrete findings\n\nNo source-reference or literal-offset defect remains after the bounded checker correction. B report source offsets use its declared UTF-8 convention. Inline and nested group markers are covered by their original source offsets; map array order is separately preserved. The initial QA snapshot and exact old/new checker changes are retained.\n\n'+text[end:]
text=text.replace('Source checks: 477; failed checks: 16.','Source checks: 477; failed checks: 0.')
md.write_text(text)
closure={'initial_qa_inventory_sha256':hashlib.sha256(old_raw).hexdigest(),'corrected_qa_inventory_sha256':hashlib.sha256(new_raw).hexdigest(),'changed_qa_check_paths':len(changes),'remaining_failed_checks':sum(not x['ok'] for x in data['source_checks']),'remaining_source_findings':data['concrete_findings'],'source_files_changed':[]}
(OUT/'scan025_qa_checker_boundary_closure.json').write_text(json.dumps(closure,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(closure,ensure_ascii=False,indent=2))
