#!/usr/bin/env python3
"""Bind the complete scan020 selected record to its frozen draft/map."""
from pathlib import Path
from collections import Counter
import copy
import hashlib
import json
import re
import sys
sys.dont_write_bytecode=True
from scan020_prepare_sources import span

BASE=Path('/workspace/scratch/94548b74fbe0')
OUT=BASE/'out/checks'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda n:json.loads((OUT/n).read_text())


def write(name,value):
    (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')


r=load('scan020_record_draft.json')
u=load('scan020_source_union.json')
x=load('scan020_source_crosswalk.json')
m=load('scan020_final_source_map.json')
root_audit=load('scan020_root_crop_audit.json')
assembly_audit=load('scan020_assembly_audit.json')
draft_path=OUT/'scan020_final_draft.tex'
draft=draft_path.read_text()
draft_sha=sha(draft_path)
map_sha=sha(OUT/'scan020_final_source_map.json')
JP='out/checks/scan020_main_decisions.md'
J=(BASE/JP).read_text()
assert draft_sha==m['draft_sha256_utf8']==m['final_sha256']==m['final_sha256_utf8']
assert sha(BASE/JP)==m['root_journal']['sha256']==r['root_journal']['sha256']
assert set(m['attachments_by_decision'])=={d['id'] for d in r['decisions']}
assert len(r['decisions'])==42 and len(r['doubts'])==19


def attachment(a):
    out=copy.deepcopy(a)
    assert a['path']=='checks/scan020_final_draft.tex'
    assert a['workspace_path']=='out/checks/scan020_final_draft.tex'
    assert (BASE/a['workspace_path']).resolve()==(BASE/'out'/a['path']).resolve()
    assert draft[a['char_start']:a['char_end']]==a['excerpt']
    assert a['draft_sha256_utf8']==draft_sha
    out['source_map_original_path']=a['workspace_path']
    out['source_map_manifest']=a.get('workspace_manifest_path')
    out['source_map_sha256']=map_sha
    return out


def attachments(values):
    return [attachment(a) for a in values]


def section(n):
    at=J.index(f'## {n:02d} ')
    end=J.find('\n## ',at+1)
    return span(JP,J,at,len(J) if end<0 else end,section=n,source_sha256_utf8=sha(BASE/JP))


def exact_final(literal,label,occurrence=0):
    ms=list(re.finditer(re.escape(literal),draft))
    assert len(ms)>occurrence,(literal,occurrence)
    found=ms[occurrence]
    a=span('checks/scan020_final_draft.tex',draft,found.start(),found.end())
    a.update(workspace_path='out/checks/scan020_final_draft.tex',manifest='checks/scan020_final_source_map.json',
        workspace_manifest_path='out/checks/scan020_final_source_map.json',draft_sha256_utf8=draft_sha,
        final_file_sha256=draft_sha,byte_start=len(draft[:found.start()].encode()),byte_end=len(draft[:found.end()].encode()),
        attachment_id=label,body_sha256=hashlib.sha256(literal.encode()).hexdigest())
    return attachment(a)


by={d['id']:d for d in r['decisions']}
source_by={s['source_locus_id']:s for s in x['loci']}
groups={g['id']:g for g in m['selected_groups']}
for d in r['decisions']:
    d['final_source_attachment']=attachments(m['attachments_by_decision'][d['id']])
    d['root_source_attachment_status']='Exact selected-source offsets bound; root final approval remains pending.'
    d['main_approved']=False
    d['count_status']='Exact root-issued physical-cluster count; raw reader proposals retained separately.'
    if d.get('selected_source_group'):
        g=groups[d['selected_source_group']]
        d['selected_group_source']=copy.deepcopy(g['source'])
        d['selected_group_final_attachment']=attachment(g['final_source_attachment'])
        d['selected_group_source_pieces']=copy.deepcopy(g['exact_source_pieces'])
        d['literal_graphical_components']=copy.deepcopy(g['literal_components'])
    s=source_by[d['source_locus_id']]
    if s.get('aggregate_source_locus_ids'):
        d['aggregate_source_locus_ids']=copy.deepcopy(s['aggregate_source_locus_ids'])
        d['aggregate_reader_source_scopes']=copy.deepcopy(s['component_scopes'])
for q in r['doubts']:
    q['final_source_attachment']=copy.deepcopy(by[q['decision_id']]['final_source_attachment'])
    q['main_approved']=False

remainder_auth=copy.deepcopy(by['L020-42']['root_evidence_source'])
inventory_auth=section(21)
inv_groups={g['source_inventory_id'].removeprefix('SRC020-INV-'):g for g in x['inventory_source_groups']}
# Every raw inventory group remains one selected scope; three root whole-glyph
# drawing entries are added under the explicit section21 grouping authority.
specs=[
 ('TOP','Opening prose through qualified clas/deux and separate point','text',[1,2,3,4,5],None),
 ('PI-PREDECESSOR','Pi beneath opening U','deletion',[3],None),
 ('PAIRED','Both paired intersections with complete root Sigma groups','display',[6,7,8],None),
 ('PAIR-INDEX','Qualified old-J-plus-i / j / i index state','deletion',[6],'R020-G01'),
 ('ROOT-POSITIVE-SIGMA','Complete first positive Sigma/index/plus and qualified short-head role','drawing',[6,7],'R020-G01'),
 ('ROOT-NEGATIVE-SIGMA','Complete negative Sigma/index/minus and locally retained short-head role','drawing',[8],'R020-G02'),
 ('UPPER-PROSE','qui sont non vides … U est un voisinage de corrected E, et','text',[9,10,11,12,13,14],None),
 ('CANCELLED-SIGMA','Complete cancelled Sigma j/i, short head, index point and two crossings','deletion',[9,10],'R020-G03'),
 ('VOISINAGE-POINT','One qualified gray rounded point after voisinage','drawing',[11],'A020-G02'),
 ('E-PREDECESSOR','Sigma beneath voisinage E','deletion',[13],None),
 ('NONEMPTY','Two nonemptiness formulas, both long rules, corrected letters and endpoints','display',[15,16,17,18,19,20],None),
 ('ROOT-BAR1-SIGMA','Complete first positive Sigma, its short head and already-present long outer rule','drawing',[16,17],'R020-G04'),
 ('BAR1-E-PREDECESSOR','Sigma beneath first nonemptiness E_i','deletion',[15],None),
 ('BAR2-SIGMA-PREDECESSOR','E beneath second barred Sigma','deletion',[18],None),
 ('BAR2-E-PREDECESSOR','Sigma beneath second nonemptiness E_i','deletion',[19],None),
 ('COUNT','On sait donc … written count and qualified parenthesis','text',[21,22,23,24,25,26,27,42],None),
 ('COUNT-WORD','Cancelled tout/est with both literal crossings and interrupted initial flecks','deletion',[23],'R020-G05'),
 ('LA-POINT','One qualified detached triangular point after la','drawing',[25],'A020-G04'),
 ('LEMMA-PROSE','Underlined Lemme and the complete selected lemma prose','text',[28,33,34,35,36,37,42],None),
 ('LEMMA-FORMULA','X setminus union expression, resolved old-I/K limit, parenthesized body and upper label','display',[29,30,31,32],'B_G03'),
 ('UNION','Literal union bowl, upper-right loop and pale lower retrace','drawing',[29],None),
 ('UNION-INDEX','Resolved I beneath K in alpha-in-I/K limit','deletion',[30],None),
 ('HAT-LABEL','Inserted hatted Sigma_alpha-plus above the brace','insertion',[32],None),
 ('BRACE','Complete stepped upper brace, closed left loop and dark retrace','drawing',[31],None),
 ('NONVIDE','Inserted and cancelled non vide, including its literal pointed crossing return','insertion',[33],None),
 ('GUIDE','Separate complete curved insertion guide; adjoining words retained in its containing group','drawing',[34],None),
 ('MARGIN','Two-line slanted K est ne empty / si I ne empty','margin note',[38],'C_MARGIN'),
 ('ONA','Cancelled on a','deletion',[35],None),
 ('MEMBERSHIP','One qualified literal relation and invisible complete-state annotation','drawing',[36],'R020-G06'),
 ('MEMBERSHIP-E','Qualified E / Sigma-predecessor-plus-E state inside pi_0 argument','deletion',[37],None),
 ('FINAL','Final quantified hatted condition and parenthesized unhatted relation','display',[42],None),
 ('ARCHIVE','19, archive numeral preserved only as a comment','text',[39],None),
]
inventory=[]
for num,(key,label,kind,dnums,graphic) in enumerate(specs,1):
    dids=[f'L020-{n:02d}' for n in dnums]
    raw=copy.deepcopy(inv_groups[key]['source_rows']) if key in inv_groups else {w:[] for w in ['witness C','A','B','C']}
    item=dict(sheet_kind='text',hand='undetermined hand' if key in ['VOISINAGE-POINT','LA-POINT','ARCHIVE'] else 'his hand',
        element=f'020.I{num:02d}',kind=kind,position=inv_groups[key]['scope'] if key in inv_groups else label,
        first_words_or_objects=label,transcribed='yes',selected=True,main_approved=False,source_inventory_group=key,
        source_rows=raw,related_decision_ids=dids,root_decision_sources=[copy.deepcopy(by[d]['root_evidence_source']) for d in dids],
        root_remainder_selection_source=remainder_auth,root_inventory_authorization=inventory_auth,
        selection_status='Root-selected source content; complete approval remains pending.',
        hand_status='Root-selected attribution; undetermined point/archive hands stay explicit.',final_source_attachment=[])
    if key in inv_groups:
        item['final_source_attachment']=attachments(m['attachments_by_inventory_source_group']['SRC020-INV-'+key])
        item['original_C_inventory_identities']=[z['value']['element'] for z in raw['witness C']]
    if graphic:
        item['selected_source_group']=graphic
        item['selected_group_source']=copy.deepcopy(groups[graphic]['source'])
        item['complete_group_attachment']=attachment(groups[graphic]['final_source_attachment'])
        if key.startswith('ROOT-') or key in ['CANCELLED-SIGMA','VOISINAGE-POINT','COUNT-WORD','LA-POINT','MARGIN','MEMBERSHIP']:
            item['final_source_attachment']=attachments(m['selected_graphic_inventory_source_attachments'][graphic])
    if key=='CANCELLED-SIGMA':
        item['component_attachments']=[dict(component='short upper head within the existing complete cluster',
            decision_id='L020-10',final_source_attachment=attachment(groups['R020-G03']['literal_components'][0]['final_source_attachment']))]
    if key in ['TOP','PAIRED','UPPER-PROSE','NONEMPTY','COUNT','LEMMA-PROSE']:
        item['hand_scope']='Manuscript text and mathematical lettering: his hand. The selected small gray and triangular points have their own undetermined-hand entries.'
    if key in ['PAIR-INDEX','MEMBERSHIP-E']:
        item['state_scope']='The selected source retains a complete-state qualifier; this inventory entry does not assert the doubtful predecessor as resolved.'
    inventory.append(item)
assert len(inventory)==32
inventory_by={item['source_inventory_group']:item for item in inventory}
path_owner={'R020-G01':'ROOT-POSITIVE-SIGMA','R020-G02':'ROOT-NEGATIVE-SIGMA',
    'R020-G03':'CANCELLED-SIGMA','A020-G02':'VOISINAGE-POINT','R020-G04':'ROOT-BAR1-SIGMA',
    'R020-G05':'COUNT-WORD','A020-G04':'LA-POINT','R020-G06':'MEMBERSHIP'}
ownership=[]
for group in m['selected_groups']:
    for ordinal,component in enumerate(group['literal_components']):
        key=('UNION' if ordinal<3 else 'BRACE') if group['id']=='B_G03' else (
            ('NONVIDE' if ordinal==0 else 'GUIDE') if group['id']=='C_G03--G04' else path_owner[group['id']])
        owner=inventory_by[key]
        owner.setdefault('owned_literal_component_ids',[]).append(component['id'])
        ownership.append(dict(component_id=component['id'],group_id=group['id'],inventory_element=owner['element'],
            source_inventory_group=key,final_source_attachment=attachment(component['final_source_attachment']),
            exact_source_pieces=copy.deepcopy(component['exact_source_pieces']),
            scope='Unique selected-path inventory ownership; broader group/context attachments are references to this same final occurrence.'))
assert len({v['component_id'] for v in ownership})==assembly_audit['literal_draw_fill_commands']
r['selected_literal_path_ownership']=ownership
r['inventory']=inventory

for row in r['C_source_rows']:
    row['final_source_attachment']=attachments(m['original_C_doubt_attachments'][row['source_id']]['final_source_attachment'])
    for part in row['source_parts']:
        part['final_source_attachment']=attachments(m['original_C_doubt_part_attachments'][part['part_id']]['final_source_attachment'])
        part['main_approved']=False
        assert part['decision_status']==part['original_source_decision_status']=='pending ink adjudication'
row_status=Counter(row['root_original_row_status'] for row in r['C_source_rows'])
part_status=Counter(part['root_status'] for row in r['C_source_rows'] for part in row['source_parts'])
assert dict(row_status)=={'retained':9,'resolved':2}
assert dict(part_status)=={'retained':11,'resolved':2}
r['C_doubt_resolution_counts']=dict(actual_rows=11,primary_parts=13,original_rows=dict(row_status),
    resolved_primary_parts=2,retained_primary_parts=11,pending_primary_parts=0,
    resolved_source_rows=['C020-R08','C020-R10'],retained_source_rows=[row['source_id'] for row in r['C_source_rows'] if row['root_original_row_status']=='retained'],
    scope_note='R01 retains all three separately recorded parts. Every original row/part preserves its raw pending decision_status separately from the root outcome.')
write('scan020_C_doubt_outcomes.json',dict(scan=20,original_catalog=u['canonical_C_catalog'],root_journal=r['root_journal'],
    counts=r['C_doubt_resolution_counts'],rows=r['C_source_rows'],main_adjudicated=False))

locus_coverage=[]
aggregate=set(source_by['SRC020-AGREED-REMAINDER']['aggregate_source_locus_ids'])
for locus in x['loci']:
    dids=[d['id'] for d in r['decisions'] if d['source_locus_id']==locus['source_locus_id']]
    if not dids and locus['source_locus_id'] in aggregate:dids=['L020-42']
    assert dids,locus['source_locus_id']
    locus_coverage.append(dict(source_locus_id=locus['source_locus_id'],root_decision_ids=dids,
        original_reader_difference_ids={q:[z['value']['id'] for z in locus['reader_difference_rows'][q]] for q in 'ABC'},
        selected=True,main_approved=False,readers=copy.deepcopy(locus['readers']),reader_provenance=copy.deepcopy(locus['reader_provenance']),
        root_authorization=[copy.deepcopy(by[d]['root_evidence_source']) for d in dids],
        final_source_attachment=attachments(m['attachments_by_source_locus'][locus['source_locus_id']])))
cover_by={l['source_locus_id']:l for l in locus_coverage}
r['source_locus_coverage']=locus_coverage
r['original_reader_difference_coverage']={q:{rid:dict(source_loci=keys,
    root_decision_ids=sorted({d for key in keys for d in cover_by[key]['root_decision_ids']}),
    coverage=[copy.deepcopy(cover_by[key]) for key in keys]) for rid,keys in rows.items()} for q,rows in x['original_difference_row_crosswalk'].items()}
r['original_reader_doubt_coverage']={q:[dict(original_source=raw['source'],
    source_loci=x['original_doubt_row_crosswalk'][q][raw['source']['pointer']],
    root_decision_ids=sorted({d for key in x['original_doubt_row_crosswalk'][q][raw['source']['pointer']] for d in cover_by[key]['root_decision_ids']}))
    for raw in u['reader_sources'][q]['raw_rows']['doubts']] for q in 'ABC'}
r['complete_selected_source_blocks']=[dict(id=b['id'],final_source_attachment=attachment(b['final_source_attachment'])) for b in m['final_blocks']]
r['selected_graphical_groups']=copy.deepcopy(m['selected_groups'])
r['original_inventory_coverage']=dict(raw_rows=121,reader_rows=100,actual_C_rows=21,source_groups=29,selected_inventory_entries=32,
    all_original_identities_preserved=True,
    original_C_attachments={key:attachments(v) for key,v in m['original_inventory_source_attachments'].items()},
    scope='All 121 original inventory rows remain in their exact 29 source groups. Root section21 adds three whole-Sigma drawing entries; cancelled-head component remains attached within the existing cancelled-Sigma entry.')

r['abbreviations']=[
    dict(form='clas.',expansion='classes',scope='Probable expansion for the qualified primary only; deux remains the complete alternative word.',
         final_source_attachment=attachments(m['attachments_by_source_locus']['SRC020-CLAS-WORD'])+attachments(m['attachments_by_source_locus']['SRC020-CLAS-POINT'])),
    dict(form='nb',expansion='nombre',scope='Both written occurrences remain unexpanded.',
         final_source_attachment=attachments(m['attachments_by_source_locus']['SRC020-NB1'])+attachments(m['attachments_by_source_locus']['SRC020-NB2'])),
    dict(form='card',expansion='cardinal',scope='Written lowercase card remains unexpanded.',final_source_attachment=attachments(m['attachments_by_source_locus']['SRC020-CARD'])),
    dict(form=r'\unsure{dèm.|dém.|dem.}',expansion='démonstration',scope='Conventional probable expansion authorized by root section21; the sheet does not write it out. All selected accent/no-accent alternatives remain literal.',
         final_source_attachment=attachments(m['attachments_by_source_locus']['SRC020-DEM'])),
]
for entry in r['abbreviations']:
    entry.update(root_authorization=inventory_auth,selected=True,main_approved=False)

content=copy.deepcopy(m['attributed_content_note'])
r['attributed_content_note']=content
def source_label(a):return f"{a['path']} characters [{a['char_start']},{a['char_end']})"
content_paragraphs=[e['text']+' Exact selected source: '+ '; '.join(source_label(a) for a in e['source_attachments'])+'.' for e in content['entries']]
r['notes']='\n\n'.join(content_paragraphs+[
    'The actual C Doubtful readings table has eleven rows and thirteen parts. Root resolves C020-R08 (old I under K) and C020-R10 (sait); nine rows remain retained, including all three C020-R01 rings. Nineteen local doubts remain: eleven retained original C parts, four locally unresolved short-head roles, two isolated-point roles, par/p, and the lower E/Sigma-predecessor state. Exact source identities and original flags are retained in the record; the notation and slip sections retain their own source categories.',
    'The selected complete sources are R020-G01 through R020-G06, A020-G02, A020-G04, modified B_G03, C_G03--G04 and C_MARGIN. Every selected path, node, wrapper, local source declaration and adjacent word boundary has an exact final attachment. The first positive Sigma carries the recurring short-head-role qualifier; the later three local role doubts remain explicit in the record. The grey point after voisinage and the triangular point after la retain undetermined hand/role/origin; neither point-only group duplicates its neighboring words. The cancelled Sigma owns one physical cluster and one H ill placeholder; its short-head component adds no duplicate count. The cancelled count word and on a each own their own H placeholder. These are manual graphical approximations described by root in '+source_label(section(19))+'.',
    'B_G03 retains the three union paths, three brace paths, resolved old-I/K limit and one upper hatted label. Root selected annotation placement at L020-32 as its own H difference although H describes that label in apparatus. C_G03--G04 owns partie, non vide, de I and the comma, with et outside; its cancellation and curved guide are separately recorded components. R020-G06 keeps the three literal relation paths and invisible complete-state annotation once. The two long closure rules remain present; L020-16 and L020-20 carry their exact S identities and zero current-witness counts.',
    'The S summary at L020-41 preserves SA01-K81-06, SA01-29, the recorded 81/15–22 range and the author’s no-scan-view statement. Its quoted index-1/i.e. examples, strict-inclusion chain and U_s example are reported absent by the three complete independent readings. Local ink confirmations and the source-only coverage record retain separate flags and journal spans. The scan-header convention and twelve agreed remainder scopes are authorized in '+source_label(section(20))+'. The four probable expansions appear only in the separate table under '+source_label(inventory_auth)+'.',
    'The root crop audit records eighteen distinct successful local inspections and one earlier failed unseen delivery of the exact B12 PNG, followed by its single successful retry. Root viewed no whole scan or supplied half. The independently recorded reader processing and source-validation histories remain literal provenance. The assembly audit records source-span/identity/delimiter checks and manual-source attachment checks. No compilation, rendering, OCR, web research, optional coordinate computation or mathematical proof check was performed by this clerk; check_events remains empty.'
])

r['source_counting_constraints']=[
    dict(parent='L020-06',children=['L020-07'],witnesses=['H'],scope='One positive Sigma/index graphic cluster in R020-G01; H counted at06, C new upper run counted at07.'),
    dict(parent='L020-09',children=['L020-10'],witnesses=['C','H'],H_placeholder='H020-ILL-01',scope='One complete cancelled Sigma/index/state/crossing group; head component has zero duplicate count.'),
    dict(parent='L020-17',components=['L020-16'],witnesses=['C','H'],scope='R020-G04 prints long outer rule and short head once; existing long rule at16 has C0/H0, new literal short head at17 has C1/H1.'),
    dict(parent='L020-23',H_placeholder='H020-ILL-02',scope='One cancelled-word/crossing cluster; interrupted initial flecks are source components of the selected second crossing.'),
    dict(parent='L020-35',H_placeholder='H020-ILL-03',scope='One complete cancelled on a placeholder recovery.'),
    dict(parent='L020-11',scope='One A020-G02 point; neighboring words remain outside its group.'),
    dict(parent='L020-25',scope='One A020-G04 point; la remains outside its group.'),
    dict(parent='B_G03',decisions=['L020-29','L020-30','L020-31','L020-32'],scope='One complete source group with distinct union, limit, brace and annotation-placement count loci; nodes and paths appear once.'),
    dict(parent='C_G03--G04',decisions=['L020-33','L020-34'],scope='One complete word-bearing source group; cancellation/phrase and guide are separate physical count loci.'),
    dict(parent='L020-36',scope='One relation/state/drawing cluster; invisible full-state candidates are editorial support, not extra occurrences.'),
    dict(parent='L020-20',count=False,scope='Existing second long overbar confirmed with S identity; C0/H0.'),
    dict(parents=['L020-40','L020-41','L020-42'],count=False,scope='Source-only convention, S coverage and remainder selections, each C0/H0.')]
r['root_ink_pass']=dict(successful_crop_views=root_audit['total_distinct'],whole_scan_views=0,supplied_half_views=0,
    failed_unseen_delivery_events=copy.deepcopy(root_audit['failed_image_deliveries']),source='out/checks/scan020_root_crop_audit.json',
    audit_sha256=sha(OUT/'scan020_root_crop_audit.json'),clerk_image_views=0)
r['processing_provenance'].update(root_processing_source=span('out/checks/scan020_root_processing.md',(OUT/'scan020_root_processing.md').read_text()),
    root_crop_audit=copy.deepcopy(root_audit),tex_assembly_current_audit=dict(path='out/checks/scan020_assembly_audit.json',
        sha256=sha(OUT/'scan020_assembly_audit.json'),value=assembly_audit),
    original_assembly_audit_hashes=[m['assembly_audit']],source_assembly_provenance=copy.deepcopy(m['processing_provenance']),
    no_coordinate_or_mathematical_event_rerun=True)
r['selected_draft']=dict(path='checks/scan020_final_draft.tex',workspace_path='out/checks/scan020_final_draft.tex',sha256=draft_sha)
r['selected_source_map']=dict(path='checks/scan020_final_source_map.json',workspace_path='out/checks/scan020_final_source_map.json',sha256=map_sha)
r['source_attachment_path_correspondence']=dict(record_path='checks/scan020_final_draft.tex',record_base=str(BASE/'out'),
    original_map_path='out/checks/scan020_final_draft.tex',original_map_base=str(BASE),exact_absolute_target=str(draft_path),
    relation='Both declared base/path concatenations resolve to the identical selected file; exact offsets and bytes are preserved.')
r['S_public_audit']=[dict(decision_id=d['id'],S_id=d['S_id'],S_status=d['S_status'],root_ink_choice_applied=d['root_ink_choice_applied'],
    root_source_audit_choice_applied=d['root_source_audit_choice_applied']) for d in r['decisions'] if d.get('S_id')]
r['counts']=dict(status='Complete root-selected readings and exact attachments; final root approval pending.',C=17,H=29,
    by_witness_confidence={w:dict(Counter(d['confidence'] for d in r['decisions'] if d['diff_'+w])) for w in 'CH'},
    remaining_doubt_loci=19,inventory_elements=32,decision_rows=42,root_ink_entries=39,source_audit_entries=3,check_events=0)
assert sum(d['diff_C'] for d in r['decisions'])==17 and sum(d['diff_H'] for d in r['decisions'])==29
r.update(root_ink_decision_entries=39,root_source_audit_entries=3,pending_root_decision_ids=[],pending_root_confidence_ids=[],
    root_approved_decision_entries=0,root_choices_applied_through_section=21,
    root_approval_status='All source/ink choices, inventory, doubts and exact attachments recorded; final root approval pending.',
    source_attachment_status='Bound to frozen selected draft/map; final independent source audit and root approval pending.',
    main_adjudicated=False,main_approved=False)
r['mechanical_verification'].update(source_preparation_only=False,all_ink_choices_supplied_by_root=True,all_public_reader_maps_complete=True,
    root_confidence_metadata_complete=True,selected_draft_and_map_sha256_bound=True,source_inventory_rows_mapped=True,
    original_C_rows=11,source_primary_parts=13,final_targeted_source_QA='pending one independent frozen-bundle source pass')
write('scan020_record_draft.json',r)
f=load('scan020_source_fingerprints.json')
f.update(record_stage='Complete selected record frozen for independent source audit and root review.',
    selected_draft=dict(path='out/checks/scan020_final_draft.tex',sha256=draft_sha),selected_map=dict(path='out/checks/scan020_final_source_map.json',sha256=map_sha),
    prepared_files={name:dict(sha256=sha(OUT/name)) for name in ['scan020_record_draft.json','scan020_source_crosswalk.json','scan020_C_doubt_outcomes.json','scan020_root_choices.json','scan020_assembly_audit.json','scan020_attributed_content_note.json']},
    current_assembly_audit=dict(path='out/checks/scan020_assembly_audit.json',sha256=sha(OUT/'scan020_assembly_audit.json')),
    root_journal=r['root_journal'],root_crop_audit_sha256=sha(OUT/'scan020_root_crop_audit.json'),root_approval_flags=False)
write('scan020_source_fingerprints.json',f)
print(json.dumps(dict(record_sha256=sha(OUT/'scan020_record_draft.json'),draft_sha256=draft_sha,map_sha256=map_sha,
    audit_sha256=sha(OUT/'scan020_assembly_audit.json'),counts=r['counts'],C_doubt_outcomes=r['C_doubt_resolution_counts'],
    current_selected_approval_flags=False),ensure_ascii=False))
