#!/usr/bin/env python3
"""Finalize root-selected metadata, leaving exact final attachments/approval pending."""
from pathlib import Path
from collections import Counter
import copy,hashlib,json,re
BASE=Path('/workspace/scratch/94548b74fbe0');OUT=BASE/'out/checks'
rp=OUT/'scan018_record_draft.json';r=json.loads(rp.read_text())
u=json.loads((OUT/'scan018_source_union.json').read_text())
audit=json.loads((OUT/'scan018_root_crop_audit.json').read_text())
root_instructions=[
 {'source':'Root task message after checkpoint14; copied by clerk',
  'text':'Raw checkpoint14 is complete; source writes released. Root journal now complete §§01–21, including all44 decisions, archive17 high confidence/undetermined hand, L018-26 high shape/state confidence clarification. Apply only those explicit choices/counts, build final 44-decision draft + doubts + selected inventory + notes/abbr/S rows. Preserve all originals, C14rows18primaryparts and final-U context. Explicit S public audit may be one page-level noncount row with S_id/status: all three readers found no matching quoted Sigma/U expression, no local repair made. Root personally saw overlapping local S glyphs but never whole/halves; note whole-page S coverage from independent readers. Add root nonexistent-image-filename failure and text-only comparison truncation/recovery provenance. Assemble counts, flag any missing root choice. Do not approve or commit. Coordinate exact source attachments with tex018 after draft ready.'},
 {'source':'Root S audit metadata instruction; copied by clerk',
  'text':'For the authorized S018-PAGE audit use confidence high solely for exact source-row identification/scope and the agreement of the three independently recorded reviews; explicitly say this is source-identity confidence, not a root whole-page ink judgment. Counts C0/H0; log_decision true, S_id SA01-K81-06, S_status no matching quoted expression established on this page / no current-witness correction inferred. This is row45, not a new ink locus or original C doubt. Root independent expectation from journal: C23/H29, 23 remaining local doubt rows (please flag mismatch without changing to match).'},
 {'source':'Root text-delivery provenance instruction; copied by clerk',
  'text':"Additional root text provenance: the pre-compaction attempted B aggregate text read yielded no content ('Output exceeded available model context'); after resumption B was fully read in bounded calls before any root image. Later aggregate pairwise-diff text output truncated only the middle A–C section; that complete A–C diff was then delivered separately before the first crop. No image delivery was involved in either text truncation."},
]
ipath=OUT/'scan018_clerk_root_instructions.json'
ipath.write_text(json.dumps(dict(scan=18,scope='Exact session instructions supplied by root; no invented timestamps.',instructions=root_instructions),ensure_ascii=False,indent=2)+'\n')
instruction_ref=dict(manifest='out/checks/scan018_clerk_root_instructions.json',pointer='/instructions/1',sha256=hashlib.sha256(ipath.read_bytes()).hexdigest())
by={d['id']:d for d in r['decisions'] if d['id'].startswith('L018-')}
assert len(by)==44 and all(d['root_ink_choice_applied'] for d in by.values())
assert all(d['confidence'] in ['high','medium','low'] for d in by.values())
r['resolved_or_unselected_doubt_history']=[copy.deepcopy(x) for x in r['doubts'] if not by[x['decision_id']]['remaining_doubt']]
r['doubts']=[x for x in r['doubts'] if by[x['decision_id']]['remaining_doubt']]
assert {x['decision_id'] for x in r['doubts']}=={d['id'] for d in by.values() if d['remaining_doubt']}
for q in r['doubts']:
    d=by[q['decision_id']]
    q.update(reading=d['final'],alternatives=d.get('alternatives',[]),confidence=d['confidence'],
        reason=d['evidence'],final_status='retained',main_approved=False,
        root_decision_section=d['root_decision_section'],crop=d.get('crop'))

# The source-provided inventory is unchanged under source_rows. These display
# labels describe root-selected content; they do not create further ink choices.
labels={
1:'cette dernière, si card J',2:'Ceci posé, on voit d’abord',3:'(unique)',
4:'B G01: one complete bent guide',5:'Lemme Toute classe de Pi',
6:'B G02: one underline and separate short left rule',7:'cancelled j primary; cancelled i/comma and live j alternatives',
8:'C’est presque une tautologie; worked-over Dire retained within its word; proof through OK',
9:'la',10:'qu’une',11:'C G03: two interrupted guide runs and one literal la cancellation',
12:'U_alpha/x de Pi_J with recurring circle/zero',13:'C G04 main insertion guide',
14:'C G04b: one qualified comma-like hook; punctuation/guide-return role open',
15:'Sigma predecessor within first corrected E_i',16:'B G04: qualified separate upper rule with right retrace over E_i',
17:'Sigma predecessor within corrected E_j/J',18:'choisi/choisie, cancelled',
19:'A G05.P1: one literal cancellation across choisi/choisie',20:'A G05.P2–P3: two qualified detached endpoint points',
21:'cancelled est before live est',22:'(soit Sigma_i^-)',23:'C G06: full insertion guide with right hook',
24:'deux, cancelled and uncertain',25:'card I=2, raised',26:'C G07a: one long cancellation path',
27:'C G07b: qualified lower hook; letter/guide attachment and hand open',
28:'cela / OK / et, cancelled; cela primary',29:'A G08: OK, live primary/cancelled alternative, rising stroke and period',
30:'A G08.P2: qualified faint gray spot, role/hand/surface origin open',31:'17, archive comment only'}
groups={4:('B','G01'),6:('B','G02'),11:('C','G03'),13:('C','G04'),14:('C','G04'),
16:('B','G04'),18:('A','G05'),19:('A','G05'),20:('A','G05'),23:('C','G06'),
24:('C','G07'),25:('C','G07'),26:('C','G07'),27:('C','G07'),29:('A','G08'),30:('A','G08')}
undetermined={14,16,20,27,29,30,31}
for inv in r['inventory']:
    n=int(inv['element'].split('I')[-1])
    inv.update(first_words_or_objects=labels[n],selected=True,transcribed='yes',
        selection_status='Root-selected content from completed journal; final approval pending.',
        hand='undetermined hand' if n in undetermined else 'his hand',
        hand_status='Selected-source attribution retained; exact uncertain scope stated locally; final approval pending.',
        kind_status='Selected representation; original source kinds remain in source_rows.',main_approved=False)
    inv['root_decision_sources']=[by[x]['root_evidence_source'] for x in inv['related_decision_ids'] if x in by]
    if n in groups:inv['selected_source_group']=dict(zip(['reader','group'],groups[n]))
    if n==29:inv['hand_scope']='The OK letters are attributed to his hand; the transverse stroke’s attribution/function remains unestablished in the selected source context.'
    if n==14:inv['hand_scope']='The complete guide and wording are retained; the detached/attached hook keeps its source uncertainty in hand and role.'
    if n==16:inv['hand_scope']='The corrected E_i is in the manuscript hand; exact hand/role of its separate upper stroke remains undetermined by root §10.'
    if n==31:
        journal=(OUT/'scan018_main_decisions.md').read_text();a=journal.index('## 20 ');b=journal.index('## 21 ')
        inv.update(confidence='high',root_decision_section=20,root_crop='crops/018/20_root_archive.png',
            root_decision_sources=[dict(manifest='out/checks/scan018_main_decisions.md',char_start=a,char_end=b,
             line_start=journal.count('\n',0,a)+1,line_end=journal.count('\n',0,b-1)+1,excerpt=journal[a:b],
             literal_sha256_utf8=hashlib.sha256(journal[a:b].encode()).hexdigest(),section=20)])

# Preserve the three exact original S review objects and public actual wording.
source_fields={'A':'S_audit','B':'S_witness_review','C':'S_witness'}
audits={x:u['reader_sources'][x]['extra_source_fields'][source_fields[x]] for x in 'ABC'}
readings={'A':[audits['A']['value']['scope']],
          'B':[audits['B']['value']['conclusion'],'page_examples_matched: []'],
          'C':[audits['C']['value']['local_disposition']]}
S=dict(id='S018-PAGE',location='Page-level S source identity and coverage audit',
    C='Current C Sigma/U expressions; no page-specific repair supplied from S',
    H='Current H Sigma/U expressions; no page-specific repair supplied from S',
    final='No matching quoted S Sigma/U expression established by the three independently recorded full-page reviews; no current-witness correction inferred.',
    readers=readings,readers_report_only={x:[] for x in 'ABC'},
    reader_proposals={x:[] for x in 'ABC'},reader_audit_proposals=audits,
    reader_provenance={x:[audits[x]['source']] for x in 'ABC'},
    source_scope='Whole-page S coverage is supplied by the independent readers. Root inspected overlapping local glyphs in its 20 crops and viewed neither whole page nor supplied halves.',
    S_id='SA01-K81-06',S_status='no matching quoted expression established on this page / no current-witness correction inferred',
    S_item='SA01-29',S_source=dict(manifest='packets/018/S_rows.json',pointer='/rows/0',value=u['sources']['packets/018/S_rows.json']['value']['rows'][0]),
    confidence='high',confidence_scope='Source-identity confidence only: exact row identity/scope and agreement of the three recorded reviews. This does not assert root whole-page ink judgment.',
    kind='other',marked_in_H=False,diff_C=False,diff_H=False,C_doubt_status=None,
    source_C_doubt_parts=[],source_C_doubt_rows=[],physical_count_parent=None,H_count_parent=None,
    log_decision=True,decision_scope='source audit; no additional ink locus or original C doubt',
    evidence='S SA01-K81-06 spans scans015–022, and its recorded author viewed no scan. The three independent page returns identify no matching quoted Sigma/U expression. Root selected no page repair from that broad range. The first corrected E_i upper stroke remains the independent retained C018-R14 doubt. High confidence here concerns source identity and recorded scope only.',
    root_source_authorization=instruction_ref,root_source_audit_choice_applied=True,root_ink_choice_applied=False,
    main_approved=False,count_status='Root-authorized noncount source audit; final approval pending.',final_source_attachment=[])
r['decisions']=[d for d in r['decisions'] if d['id']!='S018-PAGE']+[S]
r['S_public_candidates']=[]
r['S_public_audit']=[dict(decision_id='S018-PAGE',S_id=S['S_id'],S_status=S['S_status'],confidence_scope=S['confidence_scope'])]

part_status=[p['root_status'] for row in r['C_source_rows'] for p in row['source_parts']]
assert len(part_status)==18 and all(s in ['resolved','retained'] for s in part_status)
row_counts=Counter()
for row in r['C_source_rows']:
    states={p['root_status'] for p in row['source_parts']}
    status=next(iter(states)) if len(states)==1 else 'mixed'
    row['root_original_row_status']=status;row_counts[status]+=1
    if row['source_id']=='C018-R08':
        row['additional_inspected_recurrence'].update(root_status='retained',root_decision_id='L018-40',root_decision_section=19,
            final_scope='Context recurrence retained without adding to original source-row or 18-primary-part counts.')
r['C_doubt_resolution_counts']=dict(actual_rows=14,primary_parts=18,
    original_rows=dict(row_counts),resolved_primary_parts=part_status.count('resolved'),
    retained_primary_parts=part_status.count('retained'),pending_primary_parts=0,
    additional_context_recurrence='L018-40 final U alpha/x retained; no extra original C part/count.',
    scope_note='R09 has two resolved predecessors and a retained index. R14 retains the original upper-rule attachment question despite secure stroke presence. All actual reader original maps remain verbatim.')
for a in r['abbreviations']:
    a['selected']=True;a['scope']='Probable expansion in abbreviation table only; form remains unexpanded in transcription.'
r['notes']="""The sheet continues the cardinality passage, defines U_{J,i}, gives an underlined Lemme with a separate short left rule, and records a prose argument with several raised additions and cancellations. Lemme is the local heading. No date or independent manuscript page heading is supplied by the three complete readings. Archive 17 is retained only in the existing comment and inventory, with high numeral confidence and undetermined hand (root §20).

The selected page preserves the local spellings and alternatives: rècurrence/récurrence, des/de, upper composante/composant, the lemma sign’s cancelled j/i/comma and live-j candidates, both circle/zero occurrences, both local alpha/x U readings, the second E index j/J, cancelled choisi/choisie, lower composant/composante, three separately recorded lower accent loci, cancelled deux, cancelled cela/OK/et, â/à, and final OK’s live/cancelled state. Repeated ring and U signs carry the printed qualifier at their first occurrence, while the later inspected doubts remain in the record. The root-authorized combined lower word is l'\\unsure{é|e}l\\unsure{ê|é}ment; the bottom cancelled candidate is \\deleted{\\unsure{cela|OK|et}}. Each combination is tied to its exact original sources and root journal (§§15,18).

The first corrected E_i keeps its recovered Sigma predecessor and a separate literal upper stroke. The original C018-R14 attachment/earlier-stroke question remains retained: visible stroke presence does not settle that question. C018-R09 independently records the predecessors and second E index. The final-U recurrence remains context to original R08; all fourteen original C rows and eighteen primary parts remain intact. The written que il and pi_0(X\\setminus\\Sigma_i) remain without a grammatical or mathematical repair. H’s sic note is editorial apparatus and supplies no additional manuscript occurrence.

Complete selected graphical groups are B G01/G02, C G03/G04, B G04, A G05, C G06/G07 and A G08. Their ordinary words, fixed origins, baselines, qualifications, path bodies and invisible state annotations are retained as selected. Each visible stroke occurs once. The point pair, lower hook, first-E upper stroke, final-OK diagonal and faint edge spot retain their stated local uncertainties. Manual drawing declarations supply no rendered, metric or alignment validation.

S SA01-K81-06 is recorded with its actual range and source author’s no-scan-view statement. All three independent whole-page returns found no matching quoted Sigma/U expression; no current-witness repair is inferred from that range. Root personally saw overlapping local glyphs in its crops but viewed neither the whole page nor supplied halves. S018-PAGE has high source-identity/scope confidence only, C0/H0, and adds no ink locus or original C doubt.

Root inspected twenty distinct local crops once each. One attempted A filename did not exist, delivered no image and was corrected to the existing manifest filename before the single successful view. A pre-compaction B aggregate text request returned no content; B was then fully read in bounded calls before any root image. A later pairwise-diff aggregate truncated the middle A–C text section, which was delivered completely in a separate call before the first crop. Neither text event involved an image delivery. The exact failed attempt and source instructions remain in provenance. Reader crop-offset/resize arithmetic is preserved from the original reports without rerunning it. No mathematical computation, proof check, OCR, research, compiler, renderer, installation or optional geometry calculation was performed by this source clerk. Reading the author’s final OK supplies no proof endorsement."""
r['check_events']=[]
r['root_ink_pass']=dict(successful_crop_views=20,unsuccessful_unseen_delivery_attempts=audit['unsuccessful_unseen_delivery_attempts'],
    whole_scan_views=0,supplied_half_views=0,source='out/checks/scan018_root_crop_audit.json',clerk_image_views=0,
    audit_sha256=hashlib.sha256((OUT/'scan018_root_crop_audit.json').read_bytes()).hexdigest())
r['processing_provenance']=dict(
    root_instructions='out/checks/scan018_clerk_root_instructions.json',
    reader_processing_provenance={x:u['reader_sources'][x]['extra_source_fields']['processing_provenance'] for x in 'ABC'},
    root_text_delivery_events=[
        dict(event='Attempted aggregate B text read',outcome='No content: Output exceeded available model context',recovery='Complete B read in bounded calls after resumption and before any root image',image_delivery=False),
        dict(event='Aggregate pairwise source-diff text delivery',outcome='Middle A–C section truncated',recovery='Complete A–C diff delivered separately before the first root crop',image_delivery=False)],
    root_image_delivery_failure=audit['unsuccessful_unseen_delivery_attempts'],
    finite_processing_scope='Reader-reported fixed crop and resize operations/half-coordinate conversions are copied without rerun. Source-offset/hash/count checks only by clerk; no image-content or metric calculation.',
    clerk_scope='No images opened, crops made, OCR, compiler, renderer, install, research, delegation or optional mathematical/geometric work.')
r['source_counting_constraints']=[
    dict(parent='L018-16',witnesses=['C','H'],children=['L018-17'],scope='Main guide carries C1/H1; hook is a logged zero-count component.'),
    dict(parent='L018-35',witnesses=['H'],children=['L018-36','L018-37'],scope='Whole old-word/raised-card correction counted once in H. Lower hook has its separate C1 at L018-37.'),
    dict(parent='L018-41',witnesses=['C','H'],children=['L018-42'],scope='Whole final-OK state/path cluster counted once; high shape-confidence component is zero count.'),
    dict(parent='L018-27',witnesses=['C','H'],components=['A:G05.P2','A:G05.P3'],scope='Two point fills are one physical point cluster, counted once per witness.'),
    dict(loci=['L018-19','L018-20'],scope='Root explicitly selected separate H predecessor and spatially separate upper-stroke loci; C-reader shared-H proposal remains raw provenance.'),
    dict(loci=['L018-25','L018-26'],scope='Same C chosen-word primary/doubt retained; literal agreed cancellation adds no change count. H lexical difference remains qualified at L018-25.'),
    dict(parent='L018-13',scope='Interrupted guide counted once; already agreed la cancellation adds no count.'),
    dict(parent='L018-10',scope='Underline emphasis already agrees with H; left-rule discrepancy supplies H count.'),
    dict(parent='S018-PAGE',witnesses=['C','H'],count=False,scope='Source-identity audit only.')]
counts={w:sum(bool(d['diff_'+w]) for d in r['decisions']) for w in ['C','H']}
r['counts']=dict(status='Root choices copied and counted; final approval pending.',**counts,
    by_witness_confidence={w:dict(Counter(d['confidence'] for d in r['decisions'] if d['diff_'+w])) for w in ['C','H']},
    remaining_doubt_loci=len(r['doubts']),inventory_elements=len(r['inventory']),decision_rows=len(r['decisions']),
    ink_decision_loci=44,page_source_audit_rows=1,check_events=0)
r['root_ink_decision_entries']=44;r['root_source_audit_entries']=1
r['pending_root_decision_ids']=[];r['pending_root_confidence_ids']=[]
r['root_approved_decision_entries']=0;r['main_adjudicated']=False
r['root_choices_applied_through_section']=21
r['root_approval_status']='All source/ink choices recorded; all approval flags remain false for root final review.'
r['source_attachment_status']='Selected-source draft/map attachments pending assembler binding.'
r['mechanical_verification'].update(all_ink_choices_supplied_by_root=True,raw_difference_rows_preserved=115,
    raw_doubt_rows_preserved=49,raw_inventory_rows_preserved=99,source_inventory_rows_mapped=True,
    source_primary_parts=18,original_C_rows=14,root_confidence_metadata_complete=True,
    final_source_attachment_review='pending single targeted QA pass after bundle freeze')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
fpath=OUT/'scan018_source_fingerprints.json';f=json.loads(fpath.read_text())
for p in ['scan018_record_draft.json','scan018_root_choices.json','scan018_clerk_root_instructions.json']:
    f['prepared_files'][p]=dict(sha256=hashlib.sha256((OUT/p).read_bytes()).hexdigest())
f['record_stage']='All root choices applied; final selected-source attachments pending; no approval.'
fpath.write_text(json.dumps(f,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(counts=r['counts'],C_doubt_resolution_counts=r['C_doubt_resolution_counts'],
    all_approval_flags_false=True,record_sha256=hashlib.sha256(rp.read_bytes()).hexdigest()),ensure_ascii=False))
