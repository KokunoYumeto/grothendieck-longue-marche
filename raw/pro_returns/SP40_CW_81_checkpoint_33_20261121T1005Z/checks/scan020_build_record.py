#!/usr/bin/env python3
"""Apply only explicit scan020 root choices to the source record draft."""
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
load=lambda name:json.loads((OUT/name).read_text())


def write(name,value):
    (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')


U=load('scan020_source_union.json')
X=load('scan020_source_crosswalk.json')
W=load('scan020_witness_sources.json')['witnesses']
CHOICES=load('scan020_root_choices.json')['choices']
SOURCES={l['source_locus_id']:l for l in X['loci']}
JP='out/checks/scan020_main_decisions.md'
J=(BASE/JP).read_text()


def root_source(did):
    match=re.search(r'^'+re.escape(did)+r'\b',J,re.M)
    assert match,did
    following=re.search(r'^L020-\d+\b|^## ',J[match.end():],re.M)
    end=match.end()+following.start() if following else len(J)
    while end>match.start() and J[end-1]=='\n':end-=1
    preceding=list(re.finditer(r'^## (\d+) [^\n]*',J[:match.start()],re.M))
    sec=preceding[-1]
    section=int(sec[1])
    crop=re.search(r'(?:Viewed|Previously inspected crop) `([^`]+)`',J[sec.start():match.start()])
    return span(JP,J,match.start(),end,section=section,source_sha256_utf8=sha(BASE/JP)),crop[1] if crop else None


decisions=[]
for selected in CHOICES:
    s=copy.deepcopy(SOURCES[selected['source']])
    ref,crop=root_source(selected['id'])
    count=f"C{selected['C']}/H{selected['H']}"
    assert count in ref['excerpt'],(selected['id'],count)
    assert selected['confidence'] in ref['excerpt'],(selected['id'],selected['confidence'])
    witness=copy.deepcopy(W[selected['source']])
    d=dict(id=selected['id'],location=s['location'],C=witness['C']['reading'],H=witness['H']['reading'],
        final=selected['final'],readers=copy.deepcopy(s['readers']),readers_report_only=copy.deepcopy(s['readers_report_only']),
        reader_proposals={r:[copy.deepcopy(v['value']) for v in s['reader_difference_rows'][r]] for r in 'ABC'},
        reader_provenance=copy.deepcopy(s['reader_provenance']),reader_doubt_proposals=copy.deepcopy(s['reader_doubt_rows']),
        reader_supplemental_sources=copy.deepcopy(s['reader_supplemental_sources']),report_silent_choices=copy.deepcopy(s['report_silent_choices']),
        reader_tex_scopes=copy.deepcopy(s['reader_tex_scopes']),reader_tex_choices=copy.deepcopy(s['reader_tex_choices']),
        source_locus_id=selected['source'],witness_provenance=witness,evidence=ref['excerpt'],
        confidence=selected['confidence'],kind=selected['kind'],diff_C=bool(selected['C']),diff_H=bool(selected['H']),
        marked_in_H=bool(witness['H']['marked_in_H']),marked_in_H_basis=witness['H']['marked_scope'],
        C_doubt_status=selected.get('C_doubt_status'),source_C_doubt_rows=copy.deepcopy(s['source_C_doubt_rows']),
        source_C_doubt_parts=copy.deepcopy(s['source_C_part_ids']),remaining_doubt=bool(selected['remaining_doubt']),
        alternatives=copy.deepcopy(selected['alternatives']),root_evidence_source=ref,root_decision_section=ref['section'],
        crop=crop,root_ink_choice_applied=selected.get('root_ink_choice_applied',True),
        root_source_audit_choice_applied=selected.get('root_source_audit_choice_applied',False),
        root_source_authorization_sha256=sha(BASE/JP),physical_count_parent=selected.get('physical_count_parent'),
        C_count_parent=selected.get('C_count_parent'),H_count_parent=selected.get('H_count_parent'),
        H_placeholder_parent=selected.get('H_placeholder_parent'),log_decision=True,main_approved=False,
        final_source_attachment=[],mathematical_consequence=None,count_status='Exact root-issued physical counts copied; final approval pending.')
    for k in ['selected_source_group','hand','boundary_limit','decision_scope','printed_qualifier','first_qualifier',
              'confidence_scope','qualification','selected_source_pending','S_id','S_status','source_scope']:
        if k in selected:d[k]=copy.deepcopy(selected[k])
    if d.get('S_id'):
        d['S_source']=copy.deepcopy(U['sources']['packets/020/S_rows.json'])
    assert set(d['readers'])==set('ABC')
    decisions.append(d)

original_rows=copy.deepcopy(U['C_doubt_crosswalk'])
for row in original_rows:
    statuses=[]
    dids=[]
    for part in row['source_parts']:
        ds=[d for d in decisions if part['part_id'] in d['source_C_doubt_parts']]
        values={d['C_doubt_status'] for d in ds if d['C_doubt_status'] is not None}
        assert len(values)<=1,(part['part_id'],values)
        part['original_source_decision_status']=part['decision_status']
        part['root_status']=next(iter(values)) if values else None
        part['root_decision_ids']=[d['id'] for d in ds]
        part['root_evidence_sources']=[copy.deepcopy(d['root_evidence_source']) for d in ds]
        part['main_approved']=False
        part['final_source_attachment']=[]
        statuses.append(part['root_status'] or 'pending')
        dids.extend(part['root_decision_ids'])
    row['root_decision_ids']=list(dict.fromkeys(dids))
    row['root_part_status_counts']=dict(Counter(statuses))
    row['root_original_row_status']=statuses[0] if len(set(statuses))==1 else ('pending' if 'pending' in statuses else 'mixed')
    row['final_source_attachment']=[]

doubts=[dict(decision_id=d['id'],location=d['location'],reading=d['final'],alternatives=copy.deepcopy(d['alternatives']),
    confidence=d['confidence'],reason=d['evidence'],crop=d['crop'],root_evidence_source=copy.deepcopy(d['root_evidence_source']),
    reader_doubt_proposals=copy.deepcopy(d['reader_doubt_proposals']),source_C_doubt_rows=copy.deepcopy(d['source_C_doubt_rows']),
    source_C_doubt_parts=copy.deepcopy(d['source_C_doubt_parts']),final_source_attachment=[],main_approved=False)
    for d in decisions if d['remaining_doubt']]
meta=json.loads((BASE/'packets/020/metadata.json').read_text())
actual_root_ids=re.findall(r'^L020-\d+\b',J,re.M)
assert len(actual_root_ids)==len(set(actual_root_ids))
part_status=Counter(p['root_status'] or 'pending' for row in original_rows for p in row['source_parts'])
r=dict(scan=20,folder=meta['folder'],their_page=meta['their_page'],hua_has=meta['hua_has'],filename=Path(meta['codex_file']).name,
    brief_version='v18',source_record_brief_version='v02',main_adjudicated=False,main_approved=False,
    released_readers=list('ABC'),pending_readers=[],decisions=decisions,doubts=doubts,inventory=[],
    candidate_inventory=copy.deepcopy(U['candidate_inventory']),inventory_source_groups=copy.deepcopy(X['inventory_source_groups']),
    notes='Root-selected source record in preparation. Each applied choice retains its exact root-journal span. Selected inventory, attributed mathematical-content notes, abbreviations and final attachments await the exact final draft/map.',
    abbreviations=[],check_events=[],C_source_rows=original_rows,
    reader_raw_rows={r:copy.deepcopy(v['raw_rows']) for r,v in U['reader_sources'].items()},
    reader_extra_source_fields={r:copy.deepcopy(v['extra_source_fields']) for r,v in U['reader_sources'].items()},
    source_union_manifest='out/checks/scan020_source_union.json',source_union_sha256=sha(OUT/'scan020_source_union.json'),
    source_crosswalk_manifest='out/checks/scan020_source_crosswalk.json',source_crosswalk_sha256=sha(OUT/'scan020_source_crosswalk.json'),
    witness_source_manifest='out/checks/scan020_witness_sources.json',witness_source_sha256=sha(OUT/'scan020_witness_sources.json'),
    root_journal=dict(path=JP,sha256=sha(BASE/JP)),root_choices_applied_through_decision=decisions[-1]['id'] if decisions else None,
    root_approval_status='Exact issued choices copied; current selected approval fields remain false.',
    source_attachment_status='Pending exact selected draft/map.',
    counts=dict(status='Root-issued choices copied; final selected inventory and attachments pending.',
        C=sum(d['diff_C'] for d in decisions),H=sum(d['diff_H'] for d in decisions),
        by_witness_confidence={w:dict(Counter(d['confidence'] for d in decisions if d['diff_'+w])) for w in 'CH'},
        remaining_doubt_loci=len(doubts),decision_rows=len(decisions)),
    C_doubt_resolution_counts=dict(actual_rows=11,primary_parts=13,
        original_rows=dict(Counter(row['root_original_row_status'] for row in original_rows)),
        resolved_primary_parts=part_status['resolved'],retained_primary_parts=part_status['retained'],pending_primary_parts=part_status['pending']),
    S_source_rows=copy.deepcopy(U['sources']['packets/020/S_rows.json']['value']),
    pending_root_decision_ids=[d for d in actual_root_ids if d not in {v['id'] for v in decisions}],
    pending_root_confidence_ids=[],
    processing_provenance=dict(clerk_source_only=True,clerk_image_views=0,optional_mathematical_or_coordinate_computations=0,
        source_offsets_hashes_and_record_bookkeeping_only=True,reader_operations_preserved_without_rerun=True,
        clerk_preparation_history=copy.deepcopy(U['clerk_preparation_history']),
        reader_source_validation_history={r:copy.deepcopy(v['source_audits']) for r,v in U['reader_sources'].items()}),
    mechanical_verification=dict(source_preparation_only=True,raw_difference_rows_preserved=81,raw_doubt_rows_preserved=39,
        raw_inventory_rows_preserved=121,raw_notation_rows_preserved=33,no_image_viewed_by_clerk=True,
        mathematical_theorem_checks=0,numerical_geometry_checks_by_clerk=0,final_targeted_source_QA='pending completed frozen bundle'))
write('scan020_record_draft.json',r)
print(json.dumps(dict(record='out/checks/scan020_record_draft.json',sha256=sha(OUT/'scan020_record_draft.json'),
    applied_through=r['root_choices_applied_through_decision'],counts=r['counts'],pending=r['pending_root_decision_ids'],
    current_selected_approval_flags=False),ensure_ascii=False))
