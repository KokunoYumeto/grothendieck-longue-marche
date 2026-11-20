#!/usr/bin/env python3
"""Bind assembler's exact source spans to the root-selected pending record."""
from pathlib import Path
import copy,hashlib,json
BASE=Path('/workspace/scratch/94548b74fbe0');OUT=BASE/'out/checks'
rp=OUT/'scan018_record_draft.json';mp=OUT/'scan018_final_source_map.json';dp=OUT/'scan018_final_draft.tex'
r=json.loads(rp.read_text());m=json.loads(mp.read_text());draft=dp.read_text()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
mhash=sha(mp);dhash=sha(dp);assert dhash==m['draft_sha256_utf8']
prior=sha(rp);blocks={b['id']:(i,b) for i,b in enumerate(m['blocks'])}
def convert(item,pointer):
    d=item['draft'];a=d['character_start'];b=d['character_end_exclusive']
    assert draft[a:b]==d['literal_tex']
    assert hashlib.sha256(draft[a:b].encode()).hexdigest()==d['literal_sha256_utf8']
    ids=item.get('block_ids') or [item['block_id']]
    return dict(manifest='out/checks/scan018_final_draft.tex',path='checks/scan018_final_draft.tex',
        char_start=a,char_end=b,line_start=d['covering_lines_inclusive'][0],line_end=d['covering_lines_inclusive'][1],
        offset_convention=d['offset_convention'],excerpt=d['literal_tex'],literal_sha256_utf8=d['literal_sha256_utf8'],
        draft_sha256_utf8=dhash,group_anchor=ids,scope=item.get('note') or 'Exact selected source span.',
        assembly_map=dict(manifest='out/checks/scan018_final_source_map.json',pointer=pointer,sha256=mhash),
        selected_block_sources=[dict(block_id=i,source=blocks[i][1]['source'],
            manifest='out/checks/scan018_final_source_map.json',pointer='/blocks/'+str(blocks[i][0])) for i in ids],
        root_decision_sources=[x for i in ids for x in blocks[i][1].get('root_decision_sources',[])])
totals={}
for key,array,keyfield,targetfield in [
    ('decision_coverage','decisions','decision_id','id'),
    ('inventory_coverage','inventory','inventory_id','element'),
    ('doubt_coverage','doubts','decision_id','decision_id')]:
    targets={x[targetfield]:x for x in r[array]};assert set(targets)=={x[keyfield] for x in m[key]}
    total=0
    for i,x in enumerate(m[key]):
        t=targets[x[keyfield]]
        t['final_source_attachment']=[convert(v,f'/{key}/{i}/final_source_attachments/{j}') for j,v in enumerate(x['final_source_attachments'])]
        t['selected_source_map_entry']=dict(manifest='out/checks/scan018_final_source_map.json',pointer=f'/{key}/{i}',sha256=mhash)
        t['root_source_attachment_status']='Exact assembler source span bound; root final approval pending.'
        t['main_approved']=False;total+=len(t['final_source_attachment'])
    totals[array]=total
for row in r['C_source_rows']:
    for part in row['source_parts']:
        matching=[d for d in r['decisions'] if part['part_id'] in d.get('source_C_doubt_parts',[])]
        part['final_source_attachments']=[dict(decision_id=d['id'],attachments=d['final_source_attachment']) for d in matching]
    if row['source_id']=='C018-R08':
        d=next(d for d in r['decisions'] if d['id']=='L018-40')
        row['additional_inspected_recurrence']['final_source_attachments']=d['final_source_attachment']
r['assembler_original_C_scope']=m['original_C_doubt_row_coverage']
r['recurring_glyph_source_scope']=m['recurring_glyph_source_scope']
r['root_combination_edits']=m['root_combination_edits']
r['root_selected_source']='checks/scan018_final_draft.tex';r['root_selected_source_sha256']=dhash
r['source_attachment_map']='checks/scan018_final_source_map.json';r['source_attachment_map_sha256']=mhash
r['source_attachment_status']='Complete exact selected-source attachments bound; single targeted final QA and root approval pending.'
r['final_source_missing_attachments']={k:[x.get('id',x.get('element',x.get('decision_id'))) for x in r[k] if not x['final_source_attachment']] for k in ['decisions','inventory','doubts']}
r['source_binding_provenance']=dict(prior_record_sha256=prior,draft_sha256_utf8=dhash,map_sha256=mhash,
    scope='Exact literal/offset binding only; no ink, geometry or rendering checks.',assembler_audit='out/checks/scan018_tex_assembly_audit.json',
    assembler_audit_sha256=sha(OUT/'scan018_tex_assembly_audit.json'))
r['mechanical_verification'].update(selected_draft_sha256=dhash,selected_map_sha256=mhash,
    final_decision_attachment_entries=totals['decisions'],final_inventory_attachment_entries=totals['inventory'],
    final_doubt_attachment_entries=totals['doubts'],assembler_literal_span_checks_only=True,
    final_source_attachment_review='Bound; awaiting the single targeted independent QA pass.')
assert r['main_adjudicated'] is False and all(d['main_approved'] is False for d in r['decisions'])
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
fp=OUT/'scan018_source_fingerprints.json';f=json.loads(fp.read_text())
for p in ['scan018_record_draft.json','scan018_final_source_map.json','scan018_final_draft.tex','scan018_tex_assembly_audit.json']:
    f['prepared_files'][p]=dict(sha256=sha(OUT/p))
f['selected_draft']=dict(path='out/checks/scan018_final_draft.tex',sha256=dhash)
f['selected_map']=dict(path='out/checks/scan018_final_source_map.json',sha256=mhash)
f['record_stage']='Frozen for one targeted source audit; all root approval flags false.'
fp.write_text(json.dumps(f,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(record_sha256=sha(rp),draft_sha256=dhash,map_sha256=mhash,
    attachment_entries=totals,counts=r['counts'],approvals=False),ensure_ascii=False))
