#!/usr/bin/env python3
"""Finish and bind the root-selected scan019 record; leave every approval false."""
from pathlib import Path
from collections import Counter
import copy
import hashlib
import json
import re
import sys
sys.dont_write_bytecode=True
from scan019_prepare_sources import span, json_spans

BASE=Path('/workspace/scratch/94548b74fbe0')
OUT=BASE/'out/checks'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda name:json.loads((OUT/name).read_text())


def write(name,value):
    (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')


r=load('scan019_record_draft.json')
u=load('scan019_source_union.json')
x=load('scan019_source_crosswalk.json')
m=load('scan019_final_source_map.json')
root_audit=load('scan019_root_crop_audit.json')
current_audit=load('scan019_tex_assembly_audit_v02.json')
draft_path=OUT/'scan019_final_draft.tex'
draft=draft_path.read_text()
draft_sha=sha(draft_path)
map_sha=sha(OUT/'scan019_final_source_map.json')
journal_path='out/checks/scan019_main_decisions.md'
journal=(BASE/journal_path).read_text()
assert r['root_choices_applied_through_decision']=='L019-32'
assert sha(BASE/journal_path)=='852e9f96027690be7f821d3cfe2d9fb7cbb08705d74e395cb9fae7ea31d42621'
assert sha(OUT/'scan019_root_crop_audit.json')=='ad4e8986012aed32179cb61493a460db2facd612c5de92dffb33e0adb5618a49'
assert draft_sha==m['final_sha256']==m['draft_sha256_utf8']
assert set(m['attachments_by_decision'])=={d['id'] for d in r['decisions']}


def attachment(value):
    """Exact path correspondence for approve_page.py's out-root binding hook."""
    out=copy.deepcopy(value)
    assert value['path']=='out/checks/scan019_final_draft.tex'
    bind_path='checks/scan019_final_draft.tex'
    assert (BASE/value['path']).resolve()==(BASE/'out'/bind_path).resolve()
    out['source_map_original_path']=out['path']
    out['source_map_manifest']=out.get('manifest')
    out['source_map_sha256']=map_sha
    out['path']=bind_path
    return out


def exact_final(literal,occurrence=0,label=None):
    matches=list(re.finditer(re.escape(literal),draft))
    assert len(matches)>occurrence,(literal,occurrence)
    match=matches[occurrence]
    raw=span('out/checks/scan019_final_draft.tex',draft,match.start(),match.end())
    raw.update(manifest='out/checks/scan019_final_source_map.json',
        byte_start=len(draft[:match.start()].encode()),byte_end=len(draft[:match.end()].encode()),
        final_file_sha256=draft_sha,attachment_id=label or literal)
    return attachment(raw)


by={d['id']:d for d in r['decisions']}
for d in r['decisions']:
    d['final_source_attachment']=[attachment(a) for a in m['attachments_by_decision'][d['id']]]
    d['root_source_attachment_status']='Exact selected-source offsets bound; pending targeted source QA and root final approval.'
    d['count_status']='Exact root journal selection/count copied; no clerk ink decision; final approval pending.'
    d['main_approved']=False
for q in r['doubts']:
    d=by[q['decision_id']]
    q['final_source_attachment']=copy.deepcopy(d['final_source_attachment'])
    q['main_approved']=False

sec20_start=journal.index('## 20 ')
closure=span(journal_path,journal,sec20_start,len(journal),section=20)
inv_groups={i['source_inventory_id'].removeprefix('SRC019-INV-'):i for i in x['inventory_source_groups']}
group_map={g['id']:g for g in m['selected_groups']}

# source group, selected description, public kind, hand, related root IDs,
# ordinary source inventory attachment or selected graphical group.
specs=[
 ('TOP',r'D\unsure{é|è}m. par récurrence … les ens.','text','his hand',[1,2,3,4,5,6,7],'019.01',None),
 ('ROOT-G01','One qualified gray point above the initial side of the second card; the card word stays in its complete group.','drawing','undetermined hand',[3],None,'ROOT-G01'),
 ('PAIRED',r'U_{J,i}\cap\Sigma_i^+, U_{J,i}\cap\Sigma_i^-','display','his hand',[8],'019.02',None),
 ('FIRST-U',r'B_G01: complete first U with three entrance/body paths; cancelled-equality alternative retained.','drawing','his hand',[8],None,'B_G01'),
 ('BELOW-PAIRED',r"ont la forme précédente … \unsure{l'une|l'un} des deux.",'text','his hand',[9,10,11],'019.04',None),
 ('LOWER-MARKS','C_M01: one dark point and one qualified short pale lower-left trace beneath the word ending.','drawing','undetermined hand',[10,11],None,'C_M01'),
 ('PAR-HYP',r'Par hyp. de récurrence, \unsure{on a}','text','his hand',[12],'019.05',None),
 ('FIRST-EQUALITY',r'U_{J,i}=X\setminus … with selected footed join and overwritten lower-limit group.','display','his hand',[13,14,15],'019.06',None),
 ('FIRST-JOIN','A_G03: rounded bowl, long sloping foot, left supporting run and right retrace.','drawing','his hand',[13],None,'A_G03'),
 ('J-PREDECESSOR',r'C_M02: cancelled J/dotless-j predecessor before live K_0.','deletion','his hand',[14],'019.07',None),
 ('J-POINT',r'C_M02: one separate qualified high point over the predecessor.','drawing','undetermined hand',[15],None,None),
 ('OU','où','text','his hand',[],'019.08',None),
 ('BRACE',r'K_0\subset J; \Sigma_\alpha^+\in\pi_0(X\setminus E_\alpha); \widehat\Sigma_\alpha^+=\Sigma_\alpha^+\cup E_\alpha.','display','his hand',[16,17,18],'019.09',None),
 ('ROOT-G02','Complete literal main brace with interrupted upper runs, closed middle loop and hooked bottom.','drawing','his hand',[18],None,'ROOT-G02'),
 ('SIGMA-PREDECESSOR',r'\deleted{\Sigma_{\unsure{\alpha|0}}}K_0','deletion','his hand',[16],'019.10',None),
 ('BRACE-TRACE','C_M03: pale short upper segment and bowed descending path with lower-left return.','drawing','undetermined hand',[17],None,'C_M03'),
 ('ONA2',r'\unsure{On a|\deleted{O}On a|\deleted{On}On a} donc','text','his hand',[19],'019.11',None),
 ('ONA2-STATE','Possible cancelled O or On retained within the complete On a state alternatives.','deletion','his hand',[19],None,None),
 ('LOWER-EQUALITY',r'U=U_{J,i}\cap\Sigma_i^- = X\setminus(…); selected before-X point, join and endpoint pair.','display','his hand',[20,21,22],'019.12',None),
 ('SECOND-JOIN','A_G04: rounded bowl, extending foot and two retraces; local coprod/bigsqcup doubt retained.','drawing','his hand',[20],None,'A_G04'),
 ('X-POINT',r'C_M05: one qualified point immediately before X.','drawing','undetermined hand',[21],None,'C_M05'),
 ('ENDPOINT','C_M04: two detached offset dark points after/below the lower display parenthesis.','drawing','undetermined hand',[22],None,'C_M04'),
 ('SOIT','Soit, cancelled','deletion','his hand',[23],'019.13',None),
 ('LOWER-PROSE',r'Au \unsure{deuxième|deuxieme|dernier} =, dans la … soit K_1 cet ens., donc','text','his hand',[23,24,25,26,27,28,29],'019.14',None),
 ('SOMME',r'\deleted{\unsure{somme|réunion}}','deletion','his hand',[25],'019.15',None),
 ('CANCELLED-SIGMA',r'\deleted{$\Sigma$} after sur les','deletion','his hand',[],'019.16',None),
 ('FINAL-DISPLAY',r'U=X\setminus(\bigcup_{\alpha\in K_1}\widehat\Sigma_\alpha^+\cup\widehat\Sigma_i^+)','display','his hand',[],'019.17',None),
 ('ARCHIVE','18, retained only in the archive-sheet comment','text','undetermined hand',[30],None,None),
]
inventory=[]
for ordinal,(key,label,kind,hand,nums,old_id,graphic) in enumerate(specs,1):
    dids=[f'L019-{n:02d}' for n in nums]
    source_rows=copy.deepcopy(inv_groups[key]['source_rows']) if key in inv_groups else {}
    i=dict(sheet_kind='text',hand=hand,element=f'019.I{ordinal:02d}',kind=kind,
        position=inv_groups[key]['scope'] if key in inv_groups else label,
        first_words_or_objects=label,transcribed='yes',selected=True,main_approved=False,
        source_inventory_group=key,source_rows=source_rows,related_decision_ids=dids,
        root_decision_sources=[by[d]['root_evidence_source'] for d in dids],
        root_remainder_selection_source=closure,
        selection_status='Root-selected source content; approval pending.',
        hand_status='Selected source attribution, with locally undetermined marks kept explicit; approval pending.',
        final_source_attachment=[])
    if old_id:
        i['original_C_inventory_identity']=old_id
        i['final_source_attachment']=[attachment(a) for a in m['original_inventory_source_attachments'][old_id]]
    elif graphic:
        i['selected_source_group']=graphic
        i['final_source_attachment']=[attachment(a) for a in m['selected_graphic_inventory_source_attachments'][graphic]]
        i['selected_group_source']=copy.deepcopy(group_map[graphic]['source'])
    elif key=='ARCHIVE':
        i['final_source_attachment']=[attachment(a) for a in m['archive_inventory_source_attachment']]
    else:
        i['final_source_attachment']=[copy.deepcopy(a) for d in dids for a in by[d]['final_source_attachment']]
    if key=='J-POINT':
        i['final_source_attachment']=[attachment(a['final_source_attachment']) for a in group_map['C_M02']['literal_components']]
    if key=='J-PREDECESSOR':
        i['hand_scope']='The predecessor body is attributed to his hand; the separate high point has its own undetermined-hand inventory entry.'
    if key in ['TOP','BELOW-PAIRED','FIRST-EQUALITY','BRACE','LOWER-EQUALITY']:
        i['hand_scope']='Text and mathematical lettering: his hand. Adjacent marks with unresolved attribution have their own inventory entries.'
    if key=='LOWER-PROSE':
        i['attachment_scope']='The q descender is retained through the existing tels que word once under L019-29; there is no additional upright inventory object.'
    if key=='ARCHIVE':i['confidence']='high'
    inventory.append(i)
r['inventory']=inventory

# Original row identities remain exact; root outcomes are attached separately.
for row in r['C_source_rows']:
    number=int(row['source_id'].split('R')[-1])
    row['final_source_attachment']=[attachment(a) for a in m['original_C_doubt_attachments'][f'R{number:02d}']['final_source_attachment']]
    for part in row['source_parts']:
        part['final_source_attachment']=copy.deepcopy(row['final_source_attachment'])
        part['main_approved']=False
status=Counter(row['root_original_row_status'] for row in r['C_source_rows'])
assert dict(status)=={'resolved':3,'retained':9}
r['C_doubt_resolution_counts']=dict(actual_rows=12,primary_parts=12,
    original_rows=dict(status),resolved_primary_parts=3,retained_primary_parts=9,pending_primary_parts=0,
    resolved_source_rows=['C019-R01','C019-R07','C019-R08'],
    retained_source_rows=[row['source_id'] for row in r['C_source_rows'] if row['root_original_row_status']=='retained'],
    scope_note='Each original row is counted once. The R04 predecessor/high-point cluster has one root physical parent and one original part. Graphical preservation of first U/join leaves their original interpretation doubts retained.')
write('scan019_C_doubt_outcomes.json',dict(scan=19,
    original_catalog=dict(path='out/checks/scan019_C_doubt_catalog.json',sha256=sha(OUT/'scan019_C_doubt_catalog.json')),
    root_journal=r['root_journal'],counts=r['C_doubt_resolution_counts'],rows=r['C_source_rows'],main_adjudicated=False))

# Exact current-source coverage of the two agreed source-only loci outside the
# 32 public decisions, and complete raw row to decision/source correspondences.
locus_coverage=[]
for locus in x['loci']:
    ds=[d['id'] for d in r['decisions'] if d['source_locus_id']==locus['source_locus_id']]
    cov=dict(source_locus_id=locus['source_locus_id'],root_decision_ids=ds,
        original_reader_difference_ids={reader:[z['value']['id'] for z in locus['reader_difference_rows'][reader]] for reader in 'ABC'},
        selected=True,main_approved=False,final_source_attachment=[])
    if ds:
        cov['final_source_attachment']=[copy.deepcopy(a) for d in ds for a in by[d]['final_source_attachment']]
        cov['root_authorization']=[by[d]['root_evidence_source'] for d in ds]
    elif locus['source_locus_id']=='SRC019-E-INDEX':
        cov.update(selection_scope='Agreed E_alpha in the third brace condition; source-only coverage under root section20.',root_authorization=[closure],
            readers=locus['readers'],reader_provenance=locus['reader_provenance'],
            final_source_attachment=[exact_final(r'\widehat{\Sigma}_\alpha^+=\Sigma_\alpha^+\cup E_\alpha.',label='unchanged-E-index')])
    elif locus['source_locus_id']=='SRC019-FINAL-INDEX':
        cov.update(selection_scope='Agreed final display/lower limit and recorded physical-edge limitation; source-only coverage under root section20.',root_authorization=[closure],
            readers=locus['readers'],reader_provenance=locus['reader_provenance'],
            final_source_attachment=[attachment(a) for a in m['original_inventory_source_attachments']['019.17']])
    else:raise AssertionError(locus['source_locus_id'])
    locus_coverage.append(cov)
raw_coverage={reader:{} for reader in 'ABC'}
for reader,mapping in x['original_difference_row_crosswalk'].items():
    for original_id,loci in mapping.items():
        matching=[l for l in locus_coverage if l['source_locus_id'] in loci]
        raw_coverage[reader][original_id]=dict(source_loci=loci,
            root_decision_ids=sorted({d for l in matching for d in l['root_decision_ids']}),
            coverage=copy.deepcopy(matching))
doubt_coverage={reader:[] for reader in 'ABC'}
for reader in 'ABC':
    for raw in u['reader_sources'][reader]['raw_rows']['doubts']:
        ptr=raw['source']['pointer']
        ids=[d['id'] for d in r['decisions'] if any(z['source']['pointer']==ptr for z in d['reader_doubt_proposals'][reader])]
        assert ids,(reader,ptr)
        doubt_coverage[reader].append(dict(original_source=raw['source'],root_decision_ids=ids,
            selected_statuses=[dict(id=d,remaining_doubt=by[d]['remaining_doubt']) for d in ids]))
r['source_locus_coverage']=locus_coverage
r['original_reader_difference_coverage']=raw_coverage
r['original_reader_doubt_coverage']=doubt_coverage
r['complete_selected_source_blocks']=[dict(id=b['id'],final_source_attachment=attachment(b['final_source_attachment'])) for b in m['final_blocks']]
r['original_inventory_coverage']=dict(raw_rows=85,source_groups=26,selected_inventory_entries=28,
    all_original_identities_preserved=True,scope='The 26 original scope groups each retain their raw source inventory rows. Two further entries are the exact root-authored card-point and complete-brace sources. Component inventory does not create duplicate physical counts.')

abbr_sources={
    reader:copy.deepcopy(u['reader_sources'][reader]['raw_rows']['notation'][index])
    for reader,index in [('A',7),('B',8),('C',9)]}
r['abbreviations']=[]
for form,expansion,needle in [
    (r'D\unsure{é|è}m.','démonstration',r'D\unsure{é|è}m.'),
    ('hyp.','hypothèse','hyp.'),('ens.','ensemble','ens.'),('i.e.','id est','i.e.'),
    ('card','cardinal',r'\operatorname{card}')]:
    r['abbreviations'].append(dict(form=form,expansion=expansion,selected=True,
        scope='Probable expansion in the requested abbreviation table only; manuscript form remains unexpanded.',
        source_rows=copy.deepcopy(abbr_sources),root_authorization=closure,
        final_source_attachment=[exact_final(needle,label='abbreviation-'+form)],main_approved=False))

r['notes']="""The sheet continues Dém. par récurrence, gives the written cardinality cases and paired intersections, then the indexed complement expression, three brace conditions, the lower U equality, the restricted K1 prose and the final complement expression. There is no title, date or separate author page heading in the three independent returns. Archive 18 remains solely in its existing comment and inventory; root read the numeral at high confidence and retained undetermined hand.

The selected text retains the opening acute/grave accent doubt, compressed avec and both on a groups, l’une/l’un, the cancelled J/dotless-j predecessor with one separate high point, the cancelled Sigma’s alpha/zero loop, the complete live/O-only/On cancellation-state alternatives, the full deuxième/deuxieme/dernier alternatives, cancelled somme/réunion, and à/colon. ens., sommer and cet resolve original C R01/R07/R08. The other nine original C rows remain retained, with exactly twelve original rows and twelve primary parts. The first U and first footed join receive literal geometry while their original interpretation questions remain open. The second join prints the first primary without another qualifier, while its independently inspected coprod/bigsqcup alternative remains explicitly recorded.

The complete selected graphical sources are ROOT-G01, B_G01, C_M01, A_G03, C_M02, C_M03, ROOT-G02, C_M05, A_G04 and C_M04. Their exact source paths, origins, fixed rectangles, baselines, adjacent words and qualifications are bound to final character/byte offsets. The root-authored card group replaces the second card word once and leaves I=2 outside; its phantom-dot annotation is invisible support for one gray ellipse. The full brace replaces the ordinary brace once beside the existing conditions. Root’s four-command/three-visible-run description is preserved without recalculating geometry. C_M01 contains the word and both lower marks once; C_M02 contains the predecessor and one high point once, using the dotless-j alternative. C_M04 retains both endpoint points and its complete placement wrapper. Manual placements carry no rendered or metric validation.

Each mark retains its stated attribution and uncertainty. The card point, two lower word-end traces, predecessor high point, pale left-brace trace, before-X point and endpoint pair retain undetermined hand/role/surface origin. Root’s complete narrow upright crop resolves the previously cropped line as the existing q descender in tels que; that word appears once and there is no extra mark between cet and ens. A’s original report explicitly assigned the earlier crop’s entering descender to que; C-reader recorded a preceding-line descender without naming its word; B supplied no separate attachment statement. Those original distinctions remain in L019-29’s source fields.

The first-line 1 meets the physical right boundary. The selected text has no additional post-1 comma, while material beyond the surviving paper remains unassessed; L019-04 retains that boundary limitation. The last lower limit alpha in K1 and final parenthesis remain as all readers transcribe them; its lower strokes meet the physical bottom edge and no unseen continuation is supplied. The unchanged E_alpha, formulas, signs, hats, cancellations and other agreed words retain their complete-reader source coverage under root section20. H’s two note macros and its page label remain identified as apparatus; they create no invented manuscript prose. The header follows the consolidated scanpage convention, and B00/D00’s original administrative difference flags remain raw source data with zero root ink count.

S SA01-K81-06 retains its actual broad 015–022 scope, quoted proposals and source author’s no-scan-view statement. Each independent page reader reports that its quoted examples are absent here and that the nine local Sigma roofs are already represented in C/H. Root retains those hats without an S-driven addition. L019-31 has C0/H0 and high confidence solely for source identity/recorded coverage; the root viewed local crops and no whole page or supplied half. This coverage finding supplies no mathematical theorem, proof or computation check.

The root audit records eighteen distinct successful local crop inspections, each once. One earlier attempt to deliver the existing lower-join PNG returned only an output/context truncation error and no image; the identical file was subsequently delivered successfully once while its targets remained undecided. Three earlier B text calls failed before delivery during a transient executor disconnect and then succeeded after a narrow retry; this involved no image. Newly identified complete-brace and q-attachment targets received their separate bounded inspections after earlier context left them undecided, with the settled neighboring targets excluded. Original reader source-validation false positives and their bounded corrections remain in the frozen reports/audits. This clerk opened no image, made no crop, and performed no OCR, research, compilation, rendering, installation, mathematical theorem check or optional coordinate computation. Declared reader crop/resize arithmetic is retained from its actual source without rerun."""

r['source_counting_constraints']=[
    dict(parent='L019-10',children=['L019-11'],witnesses=['C','H'],scope='One C_M01 dark-point/pale-trace cluster. Pale component stays separately visible at zero duplicate count; the word reading L019-09 is its own lexical locus.'),
    dict(parent='L019-14',children=['L019-15'],witnesses=['C','H'],scope='One C_M02 predecessor/high-point cluster and one original C R04 part; high-point component has zero duplicate count.'),
    dict(parent='L019-22',components=['C_M04_fill_1','C_M04_fill_2'],witnesses=['C','H'],scope='Two endpoint fills form one root-selected point cluster.'),
    dict(parent='L019-25',witnesses=['H'],scope='One whole struck-word ill placeholder recovered with explicit alternatives.'),
    dict(parent='L019-27',witnesses=['H'],scope='One whole live sommer ill placeholder; separate from the struck-word locus.'),
    dict(parent='L019-03',scope='One gray ellipse; phantom-dot qualifier anchor is invisible support and adds no second point.'),
    dict(parent='L019-18',scope='One whole brace; root reports four draw commands in three visible runs. No duplicate generic brace or isolated loop.'),
    dict(parent='L019-29',count=False,scope='Existing q descender represented through que once; no extra mark.'),
    dict(parent='L019-31',count=False,scope='S source identity/recorded coverage only; existing C/H hats retained.'),
    dict(parent='L019-32',count=False,scope='Header convention; raw B00/D00 administrative flags remain unchanged in provenance.')]

r['root_ink_pass']=dict(successful_crop_views=root_audit['total_distinct'],whole_scan_views=0,supplied_half_views=0,
    failed_unseen_delivery_events=copy.deepcopy(root_audit['failed_image_deliveries']),
    source='out/checks/scan019_root_crop_audit.json',audit_sha256=sha(OUT/'scan019_root_crop_audit.json'),clerk_image_views=0)
r['processing_provenance'].update(root_processing_source=span('out/checks/scan019_root_processing.md',(OUT/'scan019_root_processing.md').read_text()),
    root_crop_audit=copy.deepcopy(root_audit),tex_assembly_current_audit=dict(path='out/checks/scan019_tex_assembly_audit_v02.json',sha256=sha(OUT/'scan019_tex_assembly_audit_v02.json'),value=current_audit),
    prior_assembly_audit=dict(path='out/checks/scan019_tex_assembly_audit_v01.json',sha256=sha(OUT/'scan019_tex_assembly_audit_v01.json')),
    reader_source_validation_history={reader:copy.deepcopy(source['source_audits']) for reader,source in u['reader_sources'].items()},
    clerk_binding_history=['The first binding invocation addressed the original-C attachment wrapper as a list and stopped before any output write. Its adapter was corrected to read the existing final_source_attachment list; selected TeX, map and audit bytes were unchanged.'],
    no_coordinate_or_mathematical_event_rerun=True)
r['selected_draft']=dict(path='checks/scan019_final_draft.tex',sha256=draft_sha)
r['selected_source_map']=dict(path='checks/scan019_final_source_map.json',sha256=map_sha)
r['source_attachment_path_correspondence']=dict(
    original_map_path='out/checks/scan019_final_draft.tex',original_map_base=str(BASE),
    record_path='checks/scan019_final_draft.tex',record_base=str(BASE/'out'),
    exact_absolute_target=str(draft_path),relation='Both explicit base/path concatenations resolve to this identical file. Offsets and excerpt bytes are unchanged. Raw map path and manifest are retained in each record attachment.')
r['S_public_audit']=[dict(decision_id='L019-31',S_id=by['L019-31']['S_id'],S_status=by['L019-31']['S_status'],confidence_scope=by['L019-31']['confidence_scope'])]
r['check_events']=[]
r['counts']=dict(status='Complete root-issued selections; final root approval pending.',
    C=sum(d['diff_C'] for d in r['decisions']),H=sum(d['diff_H'] for d in r['decisions']),
    by_witness_confidence={w:dict(Counter(d['confidence'] for d in r['decisions'] if d['diff_'+w])) for w in ['C','H']},
    remaining_doubt_loci=len(r['doubts']),inventory_elements=len(inventory),decision_rows=len(r['decisions']),
    root_ink_or_attachment_entries=30,source_audit_or_administrative_entries=2,check_events=0)
r['root_ink_decision_entries']=30
r['root_source_audit_entries']=2
r['pending_root_decision_ids']=[]
r['pending_root_confidence_ids']=[]
r['root_approved_decision_entries']=0
r['root_choices_applied_through_section']=20
r['root_approval_status']='All source/ink choices and exact selected-source attachments recorded; targeted QA and root final approval pending.'
r['source_attachment_status']='Bound to exact selected draft with preserved out-relative path correspondence; targeted QA and root approval pending.'
r['main_adjudicated']=False
r['mechanical_verification'].update(source_preparation_only=False,all_ink_choices_supplied_by_root=True,
    raw_difference_rows_preserved=61,raw_doubt_rows_preserved=45,raw_inventory_rows_preserved=85,
    raw_notation_rows_preserved=28,source_inventory_rows_mapped=True,source_primary_parts=12,original_C_rows=12,
    all_public_reader_maps_complete=True,root_confidence_metadata_complete=True,
    selected_draft_and_map_sha256_bound=True,final_targeted_source_QA='pending one targeted independent source pass')
write('scan019_record_draft.json',r)
f=load('scan019_source_fingerprints.json')
f.update(record_stage='Complete root-selected record and exact attachments; pending targeted QA/root approval.',
    selected_draft=dict(path='out/checks/scan019_final_draft.tex',sha256=draft_sha),
    selected_map=dict(path='out/checks/scan019_final_source_map.json',sha256=map_sha),
    prepared_files={name:dict(sha256=sha(OUT/name)) for name in [
        'scan019_record_draft.json','scan019_source_crosswalk.json','scan019_C_doubt_outcomes.json',
        'scan019_root_choices.json','scan019_tex_assembly_audit_v01.json','scan019_tex_assembly_audit_v02.json']},
    current_assembly_audit=dict(path='out/checks/scan019_tex_assembly_audit_v02.json',sha256=sha(OUT/'scan019_tex_assembly_audit_v02.json')),
    root_journal=r['root_journal'],root_crop_audit_sha256=sha(OUT/'scan019_root_crop_audit.json'),root_approval_flags=False)
write('scan019_source_fingerprints.json',f)
print(json.dumps(dict(record_sha256=sha(OUT/'scan019_record_draft.json'),draft_sha256=draft_sha,map_sha256=map_sha,
    audit_sha256=sha(OUT/'scan019_tex_assembly_audit_v02.json'),counts=r['counts'],C_doubt_outcomes=r['C_doubt_resolution_counts'],
    all_approval_flags_false=True),ensure_ascii=False))
