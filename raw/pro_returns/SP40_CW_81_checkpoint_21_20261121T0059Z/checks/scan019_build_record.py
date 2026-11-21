#!/usr/bin/env python3
"""Build scan019 record exclusively from root journal selections and source maps."""
from pathlib import Path
from collections import Counter
import copy
import hashlib
import json
import re
import sys
sys.dont_write_bytecode = True
from scan019_prepare_sources import span, json_spans

BASE = Path('/workspace/scratch/94548b74fbe0')
OUT = BASE / 'out/checks'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name):
    return json.loads((OUT / name).read_text())


def write(name, obj):
    (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')


UNION=load('scan019_source_union.json')
CROSS=load('scan019_source_crosswalk.json')
SOURCES={x['source_locus_id']:x for x in CROSS['loci']}
JOURNAL_PATH='out/checks/scan019_main_decisions.md'
JOURNAL=(BASE/JOURNAL_PATH).read_text()
WIT={w:(BASE/f'packets/019/{w}.tex').read_text() for w in ['C','H']}


def exact_witness(w,literal,description=None,occurrence=0):
    text=WIT[w]
    starts=[m.start() for m in re.finditer(re.escape(literal),text)]
    assert len(starts)>occurrence,(w,literal,occurrence)
    start=starts[occurrence]
    return dict(reading=description or literal,
        source=span(f'packets/019/{w}.tex',text,start,start+len(literal)),
        complete_inspected_source=span(f'packets/019/{w}.tex',text),
        marked_in_H=(w=='H' and (r'\uncertain' in literal or r'\ill{' in literal)))


def absence(w,literal,description):
    value=exact_witness(w,literal,description)
    value['absence_scope']='Absence of this separately represented local mark in the exact inspected complete witness source; surrounding wording is anchoring provenance.'
    return value


WITNESS={
 'SRC019-ACCENT':{w:exact_witness(w,'Dém.') for w in ['C','H']},
 'SRC019-LE':{'C':exact_witness('C','Le cas','Le'),'H':exact_witness('H','le cas','le')},
 'SRC019-CARD-POINT':{
   'C':absence('C',r'Le cas $\operatorname{card} I=2$','No separately represented point above the initial side of the second card.'),
   'H':absence('H',r'$\operatorname{card}I=2$','No separately represented point above the initial side of the second card.')},
 'SRC019-EDGE':{
   'C':absence('C',r'0,1$ Le','No post-1 comma represented at the first expression end.'),
   'H':exact_witness('H',r'0,1$, le','Post-1 comma represented.')},
 'SRC019-AVEC':{'C':exact_witness('C',r'\unsure{avec}'),
   'H':absence('H','Cas général\n'+r'$\operatorname{card}I\geq 3$','No word represented before card at this locus.')},
 'SRC019-INEQUALITY':{w:exact_witness(w,r'\geq') for w in ['C','H']},
 'SRC019-ENS':{'C':exact_witness('C',r'\unsure{ens.}'),'H':exact_witness('H','que les ens.','ens.')},
 'SRC019-U':{'C':exact_witness('C',r'\unsure{U|\deleted{=}U}'),'H':exact_witness('H',r'U_{J,i}\cap\Sigma_i^+',r'U; no separate literal entrance-path drawing.')},
 'SRC019-LUNE':{'C':exact_witness('C',r"\unsure{l'une|l'un}"),'H':exact_witness('H',"l'un des deux.","l'un")},
 'SRC019-LOWER-POINT':{
   'C':absence('C',r"\unsure{l'une|l'un} des deux.",'No separately represented dark point below the word ending.'),
   'H':absence('H',"l'un des deux.",'No separately represented dark point below the word ending.')},
 'SRC019-LOWER-TRACE':{
   'C':absence('C',r"\unsure{l'une|l'un} des deux.",'No separately represented pale lower-left trace below the word ending.'),
   'H':absence('H',"l'un des deux.",'No separately represented pale lower-left trace below the word ending.')},
 'SRC019-ONA1':{'C':exact_witness('C',r'\unsure{on a}'),'H':exact_witness('H','de récurrence, on a','on a')},
 'SRC019-JOIN1':{'C':exact_witness('C',r'\mathop{\unsure{\coprod|\bigsqcup}}'),
   'H':exact_witness('H',r'\coprod_{\alpha\in K_0}',r'\coprod')},
 'SRC019-J-PREDECESSOR':{'C':exact_witness('C',r'\deleted{\unsure{J}}K_0'),
   'H':absence('H',r'\coprod_{\alpha\in K_0}',r'K_0; no predecessor group represented.')},
 'SRC019-J-POINT':{'C':absence('C',r'\deleted{\unsure{J}}K_0','No separate high point represented over the cancelled predecessor.'),
   'H':absence('H',r'\coprod_{\alpha\in K_0}','No high point or predecessor represented at this lower-limit locus.')},
 'SRC019-SIGMA-PREDECESSOR':{'C':exact_witness('C',r'\deleted{\Sigma_{\unsure{\alpha|0}}}K_0'),
   'H':absence('H','\\begin{cases}\nK_0\\subset J',r'K_0; no Sigma predecessor represented.')},
 'SRC019-BRACE-TRACE':{
   'C':absence('C','où\n\\[\n\\left\\{\\begin{aligned}','No separately represented pale trace left of the brace.'),
   'H':absence('H','où\n\\[\n\\begin{cases}','No separately represented pale trace left of the brace.')},
 'SRC019-MAIN-BRACE':{
   'C':exact_witness('C',r'\left\{\begin{aligned}',r'Ordinary \left\{...\right. brace; no literal loop/interrupted-run geometry.'),
   'H':exact_witness('H',r'\begin{cases}',r'Ordinary cases brace; no literal loop/interrupted-run geometry.')},
 'SRC019-ONA2':{'C':exact_witness('C',r'\unsure{On a}'),
   'H':exact_witness('H',r'\struck{On} \uncertain{On a}')},
 'SRC019-JOIN2':{'C':exact_witness('C',r'\coprod_{\alpha\in K_0}',r'\coprod'),
   'H':exact_witness('H',r'\coprod_{\alpha\in K_0}',r'\coprod',occurrence=1)},
 'SRC019-PRE-X-POINT':{'C':absence('C',r'U=U_{J,i}\cap\Sigma_i^-=X\setminus','No separately represented point before the lower X.'),
   'H':absence('H',r'U = U_{J,i}\cap\Sigma_i^- = X\setminus','No separately represented point before the lower X.')},
 'SRC019-ENDPOINT':{
   'C':absence('C',r'\widehat{\Sigma}_i^+\right)','No detached endpoint-point pair represented after the lower display parenthesis.'),
   'H':absence('H',r'\widehat{\Sigma}_i^+\Bigr)','No detached endpoint-point pair represented after the lower display parenthesis.')},
 'SRC019-AU':{'C':exact_witness('C',r'\deleted{Soit} Au ','Au'),'H':exact_witness('H',r'\uncertain{Au}')},
 'SRC019-ORDINAL':{'C':exact_witness('C','deuxième'),'H':exact_witness('H',r'\uncertain{dernier}')},
 'SRC019-STRUCK-SOMME':{'C':exact_witness('C',r'\deleted{\unsure{somme|réunion}}'),
   'H':exact_witness('H',r'\struck{\ill{}}')},
 'SRC019-BORNER-SIGN':{'C':exact_witness('C','se borner à ','à'),'H':exact_witness('H','se borner : ',':')},
 'SRC019-SOMMER':{'C':exact_witness('C',r'\unsure{sommer}'),'H':exact_witness('H',r'\ill{} sur les',r'\ill{}')},
 'SRC019-CET':{'C':exact_witness('C',r'\unsure{cet}'),'H':exact_witness('H','cet ens., donc','cet')},
 'SRC019-Q-DESCENDER':{w:exact_witness(w,'tels que') for w in ['C','H']},
 'SRC019-ARCHIVE':{'C':exact_witness('C','% archive sheet number: 18'),
   'H':exact_witness('H',r'\page{18}',r'Editorial \page{18}; archive numeral retained as comment/inventory under the selected convention.')},
 'SRC019-CONVENTION':{'C':exact_witness('C','\\cotefile{81}\n\\scanpage{19}'),
   'H':exact_witness('H',r'\page{18}',r'\page{18}; no cotefile wrapper.')},
}
WITNESS['SRC019-S-AUDIT']={}
for w,text in WIT.items():
    roof_sources=[span(f'packets/019/{w}.tex',text,m.start(),m.end()) for m in re.finditer(re.escape(r'\widehat{\Sigma}'),text)]
    WITNESS['SRC019-S-AUDIT'][w]=dict(reading=r'Existing \widehat{\Sigma} occurrences retained; no current-witness correction selected from the broad S row.',
        source=span(f'packets/019/{w}.tex',text),local_roof_sources=roof_sources,
        marked_in_H=False,marked_scope='The exact local roof macros are unqualified; unrelated H word qualifiers do not mark these roofs.')

# Entries below transcribe only root-issued selections. The root paragraph is
# preserved exactly and must explicitly contain the specified C/H counts.
CHOICES=[
 dict(id='L019-01',source='SRC019-ACCENT',final=r'D\unsure{é|è}m.',confidence='low',C=1,H=0,
      kind='other',remaining_doubt=True,alternatives=['è']),
 dict(id='L019-02',source='SRC019-LE',final='Le',confidence='high',C=0,H=1,
      kind='misread word',remaining_doubt=False,alternatives=[]),
 dict(id='L019-03',source='SRC019-CARD-POINT',final='ROOT-G01: one locally qualified gray point above the initial side of the second card, retained with that card word.',
      confidence='low',C=1,H=1,kind='omission',remaining_doubt=True,alternatives=[],
      selected_source_group='ROOT-G01',hand='undetermined hand'),
 dict(id='L019-04',source='SRC019-EDGE',final='Extant 0,1 with no further printed comma; material beyond the physical edge remains unassessed.',
      confidence='low',C=0,H=1,kind='other',remaining_doubt=True,alternatives=[],boundary_limit=True),
 dict(id='L019-05',source='SRC019-AVEC',final=r'\unsure{avec}',confidence='low',C=0,H=1,
      kind='omission',remaining_doubt=True,alternatives=[],C_doubt_status='retained'),
 dict(id='L019-06',source='SRC019-INEQUALITY',final=r'\geqslant',confidence='high',C=0,H=0,
      kind='other',remaining_doubt=False,alternatives=[],decision_scope='source typography decision; no physical count'),
 dict(id='L019-07',source='SRC019-ENS',final='ens.',confidence='medium',C=1,H=0,
      kind='other',remaining_doubt=False,alternatives=[],C_doubt_status='resolved'),
 dict(id='L019-08',source='SRC019-U',final=r'Complete B_G01: qualified literal first U with three entrance/body paths and explicit \deleted{=}U alternative.',
      confidence='low',C=1,H=1,kind='drawing or diagram',remaining_doubt=True,
      alternatives=[r'\deleted{=}U'],C_doubt_status='retained',selected_source_group='B_G01',hand='his hand'),
 dict(id='L019-09',source='SRC019-LUNE',final=r"\unsure{l'une|l'un}",confidence='medium',C=0,H=1,
      kind='misread word',remaining_doubt=True,alternatives=["l'un"],C_doubt_status='retained',selected_source_group='C_M01'),
 dict(id='L019-10',source='SRC019-LOWER-POINT',final='C_M01: dark point below the word ending, in the complete locally qualified word/two-trace group.',
      confidence='medium',C=1,H=1,kind='omission',remaining_doubt=True,alternatives=[],
      selected_source_group='C_M01',hand='undetermined hand'),
 dict(id='L019-11',source='SRC019-LOWER-TRACE',final='C_M01: one short pale lower-left upright path, preserved once within the complete group.',
      confidence='low',C=0,H=0,kind='omission',remaining_doubt=True,alternatives=[],
      selected_source_group='C_M01',physical_count_parent='L019-10',H_count_parent='L019-10',hand='undetermined hand'),
 dict(id='L019-12',source='SRC019-ONA1',final=r'\unsure{on a}',confidence='low',C=0,H=0,
      kind='other',remaining_doubt=True,alternatives=[],C_doubt_status='retained'),
 dict(id='L019-13',source='SRC019-JOIN1',final=r'Complete A_G03: qualified literal first footed-join graphic; \coprod primary with \bigsqcup retained.',
      confidence='medium',C=1,H=1,kind='drawing or diagram',remaining_doubt=True,alternatives=[r'\bigsqcup'],
      C_doubt_status='retained',selected_source_group='A_G03',hand='his hand'),
 dict(id='L019-14',source='SRC019-J-PREDECESSOR',final=r'\overset{\unsure{\cdot}}{\deleted{\unsure{J|\jmath}}}K_0',
      confidence='low',C=1,H=1,kind='omission',remaining_doubt=True,alternatives=[r'\deleted{\jmath} with the separately retained high point'],
      C_doubt_status='retained',selected_source_group='C_M02',hand='his hand'),
 dict(id='L019-15',source='SRC019-J-POINT',final=r'C_M02: one qualified high \cdot over the cancelled J/dotless-j predecessor.',
      confidence='low',C=0,H=0,kind='omission',remaining_doubt=True,alternatives=[],
      selected_source_group='C_M02',physical_count_parent='L019-14',H_count_parent='L019-14',hand='undetermined hand'),
 dict(id='L019-16',source='SRC019-SIGMA-PREDECESSOR',final=r'\deleted{\Sigma_{\unsure{\alpha|0}}}K_0',
      confidence='medium',C=0,H=1,kind='omission',remaining_doubt=True,alternatives=[r'\Sigma_0'],
      C_doubt_status='retained',hand='his hand'),
 dict(id='L019-17',source='SRC019-BRACE-TRACE',final='Complete C_M03: qualified pale bowed trace with short separate upper segment and lower-left return, left of the brace.',
      confidence='low',C=1,H=1,kind='omission',remaining_doubt=True,alternatives=[],
      selected_source_group='C_M03',hand='undetermined hand'),
 dict(id='L019-18',source='SRC019-MAIN-BRACE',final='Complete ROOT-G02: literal main brace with interrupted upper runs, closed middle loop and hooked lower endpoint.',
      confidence='high',C=1,H=1,kind='drawing or diagram',remaining_doubt=False,alternatives=[],
      selected_source_group='ROOT-G02',hand='his hand',root_source_file='out/checks/scan019_root_brace.tex'),
 dict(id='L019-19',source='SRC019-ONA2',final=r'\unsure{On a|\deleted{O}On a|\deleted{On}On a}',
      confidence='low',C=0,H=1,kind='deletion state (struck given live or live given struck)',remaining_doubt=True,
      alternatives=[r'\deleted{O}On a',r'\deleted{On}On a'],C_doubt_status='retained',hand='his hand'),
 dict(id='L019-20',source='SRC019-JOIN2',final=r'Complete A_G04: literal second footed-join graphic, with \coprod primary and local \bigsqcup alternative retained in this record.',
      confidence='medium',C=1,H=1,kind='drawing or diagram',remaining_doubt=True,alternatives=[r'\bigsqcup'],
      selected_source_group='A_G04',hand='his hand',printed_qualifier=False,first_qualifier='L019-13'),
 dict(id='L019-21',source='SRC019-PRE-X-POINT',final=r'\unsure{\cdot}\, immediately before the lower X; role, hand and surface origin unresolved.',
      confidence='low',C=1,H=1,kind='omission',remaining_doubt=True,alternatives=[],
      selected_source_group='C_M05',hand='undetermined hand'),
 dict(id='L019-22',source='SRC019-ENDPOINT',final='Complete C_M04: one qualified two-point cluster, upper point right of the lower point, after/below the lower display parenthesis.',
      confidence='medium',C=1,H=1,kind='omission',remaining_doubt=True,alternatives=[],
      selected_source_group='C_M04',hand='undetermined hand'),
 dict(id='L019-23',source='SRC019-AU',final='Au',confidence='high',C=0,H=0,kind='other',remaining_doubt=False,alternatives=[],
      decision_scope='noncount source reading; H primary retained'),
 dict(id='L019-24',source='SRC019-ORDINAL',final=r'\unsure{deuxième|deuxieme|dernier}',
      confidence='low',C=1,H=1,kind='misread word',remaining_doubt=True,alternatives=['deuxieme','dernier'],hand='his hand'),
 dict(id='L019-25',source='SRC019-STRUCK-SOMME',final=r'\deleted{\unsure{somme|réunion}}',
      confidence='low',C=0,H=1,kind=r'readable ink left as \ill{}',remaining_doubt=True,alternatives=['réunion'],
      C_doubt_status='retained',hand='his hand'),
 dict(id='L019-26',source='SRC019-BORNER-SIGN',final=r'\unsure{à|:}',confidence='low',C=1,H=1,
      kind='misread symbol or index',remaining_doubt=True,alternatives=[':'],hand='his hand'),
 dict(id='L019-27',source='SRC019-SOMMER',final='sommer',confidence='medium',C=1,H=1,
      kind=r'readable ink left as \ill{}',remaining_doubt=False,alternatives=[],C_doubt_status='resolved',hand='his hand'),
 dict(id='L019-28',source='SRC019-CET',final='cet',confidence='medium',C=1,H=0,
      kind='other',remaining_doubt=False,alternatives=[],C_doubt_status='resolved',hand='his hand'),
 dict(id='L019-29',source='SRC019-Q-DESCENDER',final='The upright is the connected descender of the existing q in tels que; retain that word once.',
      confidence='high',C=0,H=0,kind='other',remaining_doubt=False,alternatives=[],hand='his hand',
      decision_scope='attachment decision; no additional glyph or physical count'),
 dict(id='L019-30',source='SRC019-ARCHIVE',final='% archive sheet number: 18',
      confidence='high',C=0,H=0,kind='other',remaining_doubt=False,alternatives=[],hand='undetermined hand',
      decision_scope='archive numeral in comment/inventory only'),
 dict(id='L019-31',source='SRC019-S-AUDIT',final='Retain the nine existing hatted Sigma occurrences; no matching quoted S example or current-witness repair is inferred from the broad row.',
      confidence='high',C=0,H=0,kind='other',remaining_doubt=False,alternatives=[],
      decision_scope='source identity and recorded coverage only; no new ink locus',
      confidence_scope='High solely for exact source identity and recorded coverage; no whole-page root ink inspection is asserted.'),
 dict(id='L019-32',source='SRC019-CONVENTION',final=r'\scanpage{19}; the repeated \cotefile{81} is omitted under the consolidated-file convention.',
      confidence='high',C=0,H=0,kind='other',remaining_doubt=False,alternatives=[],
      decision_scope='administrative convention; no physical ink difference',
      confidence_scope='High solely for the established file convention.'),
]


def root_source(id):
    match=re.search(r'^'+re.escape(id)+r'\b',JOURNAL,re.M)
    assert match,id
    following=re.search(r'^L019-\d+\b|^## ',JOURNAL[match.end():],re.M)
    end=match.end()+following.start() if following else len(JOURNAL)
    while end>match.start() and JOURNAL[end-1]=='\n':end-=1
    preceding=list(re.finditer(r'^## (\d+) [^\n]*',JOURNAL[:match.start()],re.M))
    sec=preceding[-1]
    section=int(sec.group(1))
    crop_match=re.search(r'(?:Viewed|Previously inspected crop) `([^`]+)`',JOURNAL[sec.start():match.start()])
    return span(JOURNAL_PATH,JOURNAL,match.start(),end,section=section),crop_match.group(1) if crop_match else None


decisions=[]
for selected in CHOICES:
    source=copy.deepcopy(SOURCES[selected['source']])
    root_ref,crop=root_source(selected['id'])
    explicit_count=f"C{selected['C']}/H{selected['H']}"
    assert explicit_count in root_ref['excerpt'],(selected['id'],explicit_count)
    witness=WITNESS[selected['source']]
    root_rows=source['source_C_doubt_rows']
    report_proposals={r:[copy.deepcopy(x['value']) for x in source['reader_difference_rows'][r]] for r in 'ABC'}
    d=dict(id=selected['id'],location=source['location'],C=witness['C']['reading'],H=witness['H']['reading'],
        final=selected['final'],readers=source['readers'],readers_report_only=source['readers_report_only'],
        reader_proposals=report_proposals,reader_provenance=source['reader_provenance'],
        reader_doubt_proposals=source['reader_doubt_rows'],reader_supplemental_sources=source['reader_supplemental_sources'],
        report_silent_choices=source['report_silent_choices'],reader_tex_scopes=source['reader_tex_scopes'],
        source_locus_id=source['source_locus_id'],witness_provenance=witness,
        evidence=root_ref['excerpt'] if selected['id']=='L019-18' else root_ref['excerpt'].split('\n\n')[0],
        confidence=selected['confidence'],kind=selected['kind'],
        diff_C=bool(selected['C']),diff_H=bool(selected['H']),marked_in_H=bool(witness['H']['marked_in_H']),
        marked_in_H_basis=witness['H'].get('marked_scope','Exact H source span: '+witness['H']['source']['excerpt']),
        C_doubt_status=selected.get('C_doubt_status'),source_C_doubt_rows=root_rows,
        source_C_doubt_parts=[x+'-1' for x in root_rows],remaining_doubt=selected['remaining_doubt'],
        alternatives=selected['alternatives'],root_evidence_source=root_ref,root_decision_section=root_ref['section'],
        crop=crop,root_ink_choice_applied=True,root_source_authorization_sha256=sha(BASE/JOURNAL_PATH),
        physical_count_parent=selected.get('physical_count_parent'),H_count_parent=selected.get('H_count_parent'),
        log_decision=True,main_approved=False,final_source_attachment=[],mathematical_consequence=None,
        count_status='Exact root journal counts copied; final approval pending.')
    for key in ['selected_source_group','hand','boundary_limit','decision_scope','root_source_file','printed_qualifier','first_qualifier','confidence_scope']:
        if key in selected:d[key]=selected[key]
    if selected.get('root_source_file'):
        root_path=selected['root_source_file']
        d['selected_root_source']=span(root_path,(BASE/root_path).read_text())
        d['selected_root_source_sha256']=sha(BASE/root_path)
        assert d['selected_root_source_sha256'] in root_ref['excerpt']
    if selected['id']=='L019-03':
        d['selected_source_addition']=load('scan019_root_source_additions.json')
        start=JOURNAL.index('## 04 ')
        end=JOURNAL.index('## 05 ',start)
        d['root_exact_source_acceptance']=span(JOURNAL_PATH,JOURNAL,start,end,section=4)
    if selected['id'] in ['L019-31','L019-32']:
        d['root_ink_choice_applied']=False
        d['root_source_audit_choice_applied']=True
    if selected['id']=='L019-31':
        d.update(S_id='SA01-K81-06',S_status='existing nine hats retained; no matching quoted example or current-witness repair inferred from the broad source row',
            S_source=copy.deepcopy(UNION['sources']['packets/019/S_rows.json']),
            source_scope='Whole-page coverage comes from the three independent readers; root inspected local crops only.')
        supplements=source['reader_supplemental_sources']
        d['readers']={
            'A':[supplements['A'][0]['value']['local_finding']],
            'B':[supplements['B'][0]['value'],supplements['B'][1]['value']['S_assessment']],
            'C':[supplements['C'][0]['value']['result']]}
    decisions.append(d)

cross_C=copy.deepcopy(UNION['C_doubt_crosswalk'])
for row in cross_C:
    attached=[d for d in decisions if row['source_id'] in d['source_C_doubt_rows']]
    row['root_decision_ids']=[d['id'] for d in attached]
    row['root_original_row_status']=attached[0]['C_doubt_status'] if attached else None
    for part in row['source_parts']:
        part['root_status']=row['root_original_row_status']
        part['main_approved']=False

meta=json.loads((BASE/'packets/019/metadata.json').read_text())
doubts=[dict(decision_id=d['id'],location=d['location'],reading=d['final'],alternatives=d['alternatives'],
    confidence=d['confidence'],reason=d['evidence'],crop=d['crop'],root_evidence_source=d['root_evidence_source'],
    reader_doubt_proposals=d['reader_doubt_proposals'],source_C_doubt_rows=d['source_C_doubt_rows'],
    final_source_attachment=[],main_approved=False) for d in decisions if d['remaining_doubt']]
record=dict(scan=19,folder=meta['folder'],their_page=meta['their_page'],hua_has=meta['hua_has'],
    filename=Path(meta['codex_file']).name,brief_version='v17',main_adjudicated=False,
    released_readers=list('ABC'),pending_readers=[],decisions=decisions,doubts=doubts,inventory=[],
    candidate_inventory=UNION['candidate_inventory'],inventory_source_groups=CROSS['inventory_source_groups'],
    notes='Root-selected record in preparation. Only explicitly issued journal selections are applied. Final inventory, page notes, abbreviation selections, S audit and selected-source attachments await the completed journal.',
    abbreviations=[],check_events=[],C_source_rows=cross_C,
    reader_raw_rows={r:x['raw_rows'] for r,x in UNION['reader_sources'].items()},
    source_union_manifest='out/checks/scan019_source_union.json',source_union_sha256=sha(OUT/'scan019_source_union.json'),
    source_crosswalk_manifest='out/checks/scan019_source_crosswalk.json',source_crosswalk_sha256=sha(OUT/'scan019_source_crosswalk.json'),
    root_journal=dict(path=JOURNAL_PATH,sha256=sha(BASE/JOURNAL_PATH)),
    root_choices_applied_through_decision=decisions[-1]['id'],
    root_approval_status='Pending complete root journal and final root approval; every approval flag remains false.',
    source_attachment_status='Pending completed root selections and exact selected draft/source map.',
    counts=dict(status='Partial root-issued decisions only; final count pending completed journal.',
        C=sum(d['diff_C'] for d in decisions),H=sum(d['diff_H'] for d in decisions),
        by_witness_confidence={w:dict(Counter(d['confidence'] for d in decisions if d['diff_'+w])) for w in ['C','H']},
        remaining_doubt_loci=len(doubts),decision_rows=len(decisions)),
    C_doubt_resolution_counts=dict(actual_rows=12,primary_parts=12,
        root_rows=dict(Counter(row['root_original_row_status'] or 'pending' for row in cross_C))),
    S_source_rows=UNION['sources']['packets/019/S_rows.json']['value'],
    processing_provenance=dict(root_source='out/checks/scan019_root_processing.md',
        clerk_source_only=True,clerk_image_views=0,optional_mathematical_or_coordinate_computations=0,
        source_offsets_hashes_and_record_bookkeeping_only=True,
        reader_operations_preserved_without_rerun=True),
    mechanical_verification=dict(source_preparation_only=True,raw_difference_rows_preserved=61,
        raw_doubt_rows_preserved=45,raw_inventory_rows_preserved=85,
        no_image_viewed_by_clerk=True,mathematical_theorem_checks=0,numerical_geometry_checks_by_clerk=0,
        final_targeted_source_QA='pending completed frozen bundle'))
write('scan019_record_draft.json',record)
write('scan019_root_choices.json',dict(scan=19,source_journal=record['root_journal'],
    scope='Exact root choices copied into implementation fields; no additional ink decisions.',choices=CHOICES,main_adjudicated=False))
print(json.dumps(dict(record='out/checks/scan019_record_draft.json',sha256=sha(OUT/'scan019_record_draft.json'),
    applied_through=decisions[-1]['id'],partial_counts=record['counts'],all_approval_flags_false=True),ensure_ascii=False))
