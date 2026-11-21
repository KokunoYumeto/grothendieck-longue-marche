#!/usr/bin/env python3
"""Apply copied root choices to the pending record without granting approval."""
from pathlib import Path
import hashlib,json,re
BASE=Path('/workspace/scratch/94548b74fbe0');OUT=BASE/'out/checks'
rp=OUT/'scan018_record_draft.json'
r=json.loads(rp.read_text());choices=json.loads((OUT/'scan018_root_choices.json').read_text())['choices']
jpath='out/checks/scan018_main_decisions.md';journal=(BASE/jpath).read_text()
heads=list(re.finditer(r'^## (\d+)\s+—[^\n]*',journal,re.M));sections={}
for i,h in enumerate(heads):
    end=heads[i+1].start() if i+1<len(heads) else len(journal)
    lit=journal[h.start():end]
    sections[int(h.group(1))]=dict(manifest=jpath,char_start=h.start(),char_end=end,
        line_start=journal.count('\n',0,h.start())+1,line_end=journal.count('\n',0,end-1)+1,
        offset_convention='zero-based Unicode code points; end exclusive',
        excerpt=lit,literal_sha256_utf8=hashlib.sha256(lit.encode()).hexdigest(),
        section=int(h.group(1)),heading=h.group())
byid={d['id']:d for d in r['decisions']};parts={}
for c in choices:
    d=byid[c['id']];source=sections[c['root_section']]
    assert c['id'] in source['excerpt'],(c['id'],'root section lacks locus identity')
    for k,v in c.items():
        if k not in ['id','root_section','source_C_part_statuses']:d[k]=v
    d.update(root_decision_log=jpath,root_decision_section=c['root_section'],
        root_evidence_source=source,evidence=source['excerpt'],root_ink_choice_applied=True,
        main_approved=False,confidence_status='root selected; final approval pending' if c.get('confidence') else 'pending root confidence',
        count_status='root selected physical-count outcome; final approval pending')
    extra=[sections[x] for x in c.get('root_clarification_sections',[])]
    if extra:
        d['root_source_only_corrections']=extra
        d['evidence']=source['excerpt']+'\n'+'\n'.join(x['excerpt'] for x in extra)
    crop=re.findall(r'Viewed `([^`]+)` once',source['excerpt'])
    if crop:d['crop']=crop[0];d['root_crop_paths']=crop
    for p,status in c.get('source_C_part_statuses',{}).items():parts[p]=dict(status=status,decision_id=c['id'],root_section=c['root_section'])
    for doubt in r['doubts']:
        if doubt['decision_id']==c['id']:
            doubt['final_status']='retained' if c.get('remaining_doubt') else 'resolved'
            doubt['reading']=c['final'];doubt['confidence']=c['confidence'];doubt['reason']=source['excerpt']
            doubt['root_evidence_source']=source;doubt['main_approved']=False
            if 'alternatives' in c:doubt['alternatives']=c['alternatives']
for row in r['C_source_rows']:
    for p in row['source_parts']:
        if p['part_id'] in parts:
            x=parts[p['part_id']];p['root_status']=x['status'];p['root_status_source']=x;p['main_approved']=False
r['main_adjudicated']=False
r['root_approval_status']='All approvals pending root final review and commit gate.'
r['root_choices_applied_through_section']=max([n for c in choices for n in [c['root_section']]+c.get('root_clarification_sections',[])],default=0)
r['root_sections_present']=len(sections)
r['root_approved_decision_entries']=0
r['pending_root_decision_ids']=[d['id'] for d in r['decisions'] if not d['root_ink_choice_applied']]
r['pending_root_confidence_ids']=[d['id'] for d in r['decisions'] if d['root_ink_choice_applied'] and d.get('confidence') is None]
r['root_choice_manifest']='out/checks/scan018_root_choices.json'
r['counts']['status']='Partial root selections recorded; final totals pending completion.'
r['counts']['partial_root_selected']={w:sum(int(c.get('diff_'+w,False)) for c in choices) for w in ['C','H']}
r['root_selected_primary_parts']=parts
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
fpath=OUT/'scan018_source_fingerprints.json';f=json.loads(fpath.read_text())
for p in ['scan018_record_draft.json','scan018_root_choices.json']:
    f['prepared_files'][p]=dict(sha256=hashlib.sha256((OUT/p).read_bytes()).hexdigest())
f['record_stage']='root ink selections being applied; all approvals false'
fpath.write_text(json.dumps(f,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(root_sections_applied=sorted({c['root_section'] for c in choices}),
    choices_applied=len(choices),pending_loci=len(r['pending_root_decision_ids']),root_approval_flags=False)))
