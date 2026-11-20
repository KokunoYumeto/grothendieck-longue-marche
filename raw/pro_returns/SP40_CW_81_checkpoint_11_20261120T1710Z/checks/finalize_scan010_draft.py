"""Enter only root-supplied crop decisions in the mechanical draft; no images."""
from pathlib import Path
import json,hashlib,copy,runpy,datetime
R=Path('/workspace/scratch/94548b74fbe0')
ns=runpy.run_path(str(R/'out/checks/assemble_scan010_draft.py'))
p=R/'out/checks/scan010_record_draft.json';r=json.loads(p.read_text())
u=json.loads((R/'out/checks/scan010_root_decisions_received.json').read_text())
rootpath='out/pages/J81-01_81_scan010.tex';roottex=(R/rootpath).read_text()
extract=ns['extract']
short_C={
'01':r'\unsure{\bullet|\circ}',
'02':'Uniformly dark projecting path from (1328,433) toward (1341,329); detached blob drawn; source origin doubt.',
'03':'Left angular foot trace; source faint-strokes / other-surface qualification.',
'04':'Right angular foot trace; source faint-strokes / other-surface qualification.',
'05':r'\deleted{<disk and diagonal strokes>}; source state: diagonal cancellation / hatching.',
'06':r'\unsure{\bullet|\circ}; no separately drawn projecting hook.',
'07':'Two short straight paths: (1018,28)--(1025,29) and (1037,27)--(1046,26).',
'08':'Existing main pale curl; source origin/role doubt.',
'09':'Existing pair of tiny right-middle flecks; source origin/role doubt.',
'10':r'\bullet','11':r'\bullet',
'12':'No detached point at this position.',
'13':'Several small detached fragments and two dots omitted.',
'14':'No higher slanted pale trace.',
'15':'No pale interior diagonal.',
'16':'No separate short dash below the angular shape.',
'17':'Continuous pale segment beginning (1568,905).',
'18':'No independently drawn fleck at this position.',
'19':'No pale curve at this position.',
'20':'No pale diagonal trace in this space.',
'21':'Pale irregular far-right patch omitted.',
'22':'Pale horizontal trace begins at (276,827).',
'23':'No short downward tip at about x490.',
'24':'No pale vertical trace at about x490.',
'25':'No pale descending trace at this position.',
'26':'No detached gray spot at this position.',
'27':'No gray patch at this position.',
'28':'No separate short mark near (1165,877).'
}
for d in r['decisions']:
 n=d['id'][-2:];patch=copy.deepcopy(u['decisions'][d['id']]);d.update(patch)
 d['C']=short_C[n];d['root_decided']=True;d['main_approval_pending']=True;d['main_counting_decision_pending']=False
 d['root_decision_source']='out/checks/scan010_root_decisions_received.json; exact root messages retained'
 d['root_final_tex_excerpts']=extract(roottex,n)
 d['root_page_source']=rootpath
 if n in ['01','10','11']:d['kind']='misread symbol or index'
 if n=='28':
  d['kind']='omission';d['log_decision']=True
  d['qualification']+=' The new mark has no reader report row; all three proposed TeX files omit a separate path.'
 if 'confidence_source' in d:d['confidence_source']=d['confidence_source'].replace('numeric label','confidence label')
 assert d['final'] and d['evidence'] and d['confidence'] in ['high','medium','low'] and isinstance(d['diff_C'],bool),d['id']
 # Original compound rows retain exact provenance, but candidate crops below are local.
 local={
 '02':{'A':'crop_04_middle_final_disk.png','B':'c05_middle_final_disk.png','C':'04_middle_final_disk.png'},
 '03':{'A':'crop_05_left_foot_trace.png','B':'c06_lower_graph_and_left_angular.png','C':'05_left_angular_trace_and_graph.png'},
 '04':{'A':'crop_06_right_foot_trace.png','B':'c07_right_angular.png','C':'06_right_angular_trace.png'},
 '07':{'A':'crop_07_upper_detached_marks.png','B':'c08_upper_edge_marks.png','C':'07_upper_edge_traces.png'},
 '08':{'A':'crop_08_pale_right_trace.png','B':'c09_right_pale_marks.png','C':'08_right_middle_pale_marks.png'},
 '09':{'A':'crop_09_right_flecks.png','B':'c10_right_flecks.png','C':'09_right_middle_flecks.png'}}
 if n in local:d['candidate_crop_references']=[f'out/readers/010/{role}/{file}' for role,file in local[n].items()]
for x in r['actual_C_doubt_map']:x['root_status']='retained'
# Source-identified uncertainty loci remain explicit. A crop shared by distinct objects
# never contributes a doubt from one of those objects to another.
r['doubts']=[]
for d in r['decisions']:
 if not d['source_doubts']:continue
 n=d['id'][-2:]
 direct={'01':(r'\circ',[r'\bullet']),'05':('diagonal cancellation',['hatching']),'06':(r'\bullet',[r'\circ']),'10':(r'\circ',[r'\bullet']),'11':(r'\bullet',[r'\circ'])}
 if n in direct:reading,alts=direct[n];conf=d['confidence'];scope='reading / state qualification'
 else:
  reading=d['final'];alts=[]
  for s in d['source_doubts']:
   for a in s['doubt_exact'].get('alternatives',[]):
    if a not in alts:alts.append(a)
  conf='low';scope='unresolved origin, role, or faint continuation; geometric confidence is recorded in the decision'
 reason=d['evidence']+' '+d.get('qualification','')
 r['doubts'].append({'decision_id':d['id'],'location':d['location'],'reading':reading,'alternatives':alts,'confidence':conf,'confidence_scope':scope,'reason':reason.strip(),'origin':'source local doubt retained after root crop decision','crop':d['crop'],'source_doubts':d['source_doubts']})
r.pop('proposed_doubts',None)
for i in r['inventory']:
 i['transcribed']='yes';i['root_page_source']=rootpath
 i['coverage_note']='Exact original inventory rows and source IDs are preserved; this item names the local object in the consolidated page.'
 if i['element']=='010.I47':
  i['first_words_or_objects']='disk with four continuous major interior runs and two adjoining thickened segments'
  i['coverage_note']='Root corrected inventory wording after own crop02; all four major runs already occur in witness C and all reader TeX. This wording correction adds no C transcription-difference locus.'
 if i['element'] in ['010.I75','010.I76']:
  i['coverage_note']='Existing faint path occurs in witness C and all reader TeX; this merged inventory makes its coverage explicit within the original disk inventory item. No new transcription difference.'
 if i['element']=='010.I77':
  i['coverage_note']='Root-only omission D28; a separately drawn short mark near (1165,877) is absent from C and all three reader proposals. No source report/inventory row is invented.'
  i['root_crop']='out/crops/010/root_02_final_lower_disk.png'
r['inventory_only_corrections']=u['inventory_only_corrections']
r['unchanged_audit'].append({'location':'Final lower disk, four major interior runs','witness_C':'Four existing commands: (1012,924)...(1070,770); (1011,808)...(1156,788); (1101,764)...(1174,881); (1109,967)...(1172,823).','reader_agreement':'These four major runs occur in all three reader TeX sources. C-reader inventory says four; witness C/A/B inventory says three.','diff_C':False,'diff_H':False,'C_doubt_status':None,'inventory_element':'010.I47','root_crop':'out/crops/010/root_02_final_lower_disk.png','confidence':'high','note':'Inventory-only wording correction. New separate short mark near (1165,877) is D28 and is counted there once.'})
r['main_adjudicated']=False;r['main_approved_utc']=None
r['draft_status']='Complete root crop decisions entered; awaits root review and commit.'
r['assembly_revision']='complete mechanical draft with root-supplied decisions; no pending decision cells'
r['root_page_text_exact']=roottex
rootnotes='out/checks/scan010_main_decisions.md'
r['root_adjudication_notes_exact']=(R/rootnotes).read_text() if (R/rootnotes).exists() else '\n\n'.join(u['messages_exact'])
r['root_messages_exact']=u['messages_exact']
r['root_crop_accounting']=u['counts']
r['notes']='Three graphic rows contain nine upper, seven middle, and five lower disk/oval drawings, with twelve small graph groups, grouping braces, two encircling ovals, five OK labels, ou with drawn parentheses, and one heavy question mark. Archive numeral 9 remains only in its TeX comment. Root retained all five original C doubt-table rows, preserving their nine local subloci and the exact source reader choices. The final lower disk inventory now records four major interior runs already drawn in C and all proposals; the separately omitted short mark discovered there is D28. Unlettered residual marks retain undetermined hand/role. All reading and check evidence concerns the supplied page; check_events is empty.'
r['workflow_note']='A/B/C independent returns are preserved exactly. Mechanical assembly opened no image and made no ink decision. Root reported 15 distinct successful reader-crop views plus two own crop views (17 successful distinct crops); one context-truncated B05 output attempt preceded the successful retry and is not counted as a seen image. Root-supplied crop choices populate all 28 decisions. Final page text was read only for exact-source correspondence; no compiler or mathematical check was run by this assembly.'
r['counts'].update({'decision_loci':28,'C_difference_loci':24,'H_difference_loci':0,'actual_C_doubt_loci':5,'actual_C_doubt_source_rows':5,'actual_C_doubt_local_subloci':9,'actual_C_doubts_retained':5,'actual_C_doubts_resolved':0,'remaining_doubt_or_graphic_uncertainty_loci':len(r['doubts']),'inventory_elements':len(r['inventory']),'check_events':0,'high_C_difference_loci':sum(d['diff_C'] and d['confidence']=='high' for d in r['decisions']),'medium_C_difference_loci':sum(d['diff_C'] and d['confidence']=='medium' for d in r['decisions']),'low_C_difference_loci':sum(d['diff_C'] and d['confidence']=='low' for d in r['decisions']),'root_unique_successful_crops':17})
r['counting_policy']='Twenty-eight physical decision loci, including root-only D28. D03/D04/D08/D09 retain C without a difference; the other 24 loci differ from C. D05 counts the removal of the spurious visible generic horizontal rule once; its cancellation/hatching doubt remains. The upper seventh graph fill/hook share D06; the paired upper-edge shapes share D07. Compound source rows are preserved once each in source-row counts, with explicit local mappings. Phantom repetitions and comments create no additional loci. The final lower disk four-run inventory correction has diff_C=false; the separate newly observed mark is D28 only. H desc produces no H text-collation rows.'
r['approval_followups']=[]
r['source_coverage_checks']={'all_report_rows_mapped':all(x['decision_ids'] for xs in r['source_row_coverage'].values() for x in xs),'source_report_row_total':sum(len(xs) for xs in r['source_row_coverage'].values()),'all_reader_doubt_rows_mapped':all(x['decision_ids'] for xs in r['source_doubt_coverage'].values() for x in xs),'source_reader_doubt_row_total':sum(len(xs) for xs in r['source_doubt_coverage'].values()),'all_source_inventory_rows_mapped':all(x['merged_element_ids'] for xs in r['inventory_coverage'].values() for x in xs),'source_inventory_rows_including_witness_C':sum(len(xs) for xs in r['inventory_coverage'].values()),'all_reader_tex_opcodes_mapped_or_editorial':all(x['mapped'] for xs in r['reader_tex_difference_coverage'].values() for x in xs),'reader_tex_non_equal_opcodes':sum(len(xs) for xs in r['reader_tex_difference_coverage'].values()),'root_D28_path_present':'(1166,875)--(1165,879)' in roottex,'source_checks_only':True}
for path in [rootpath,rootnotes,'out/checks/scan010_root_decisions_received.json','out/crops/010/manifest.json']:
 if (R/path).exists():r['source_fingerprints'][path]={'sha256':hashlib.sha256((R/path).read_bytes()).hexdigest(),'bytes':(R/path).stat().st_size}
r['assembly_timestamp_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
assert sum(d['diff_C'] for d in r['decisions'])==24
assert all(d['H'] is None and d['diff_H'] is False for d in r['decisions'])
assert all(d['final'] is not None and d['evidence'] is not None and d['confidence'] is not None for d in r['decisions'])
assert r['source_coverage_checks']['root_D28_path_present']
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
# Compact review map; full exact source text remains in the JSON/proposals.
md=['# Scan 010 — source and inventory coverage','', 'Complete draft: root supplied all 28 local decisions; `main_adjudicated=false` awaits root review/commit. There are **24 C differences**, **0 H differences**, **5 original C doubt rows retained**, **20 remaining local doubt records**, and **77 merged inventory elements**. H is `desc`; it contributes no text-collation rows.','', 'All 66 report rows (A 19, B 25, C-reader 22), all 33 reader doubt rows, all 249 inventory source rows including witness C, and all 34 non-equal reader-TeX opcodes are mapped. Exact choices, IDs, rows, reports, TeX, audits, and fingerprints are retained in the JSON.','', '## Local decision / source-row map','','| Decision | Local identity | A report rows | B report rows | C-reader report rows | C source-doubt row | C diff |','| --- | --- | --- | --- | --- | --- | --- |']
for d in r['decisions']:md.append('| '+' | '.join([d['id'],d['location'],*[', '.join(d['reader_provenance'][role]['source_row_ids']) or 'no local row; TeX absence retained' for role in 'ABC'],str(d['C_doubt_source_row'] or '—'),'yes' if d['diff_C'] else 'no'])+' |')
md+=['','## Original C doubt rows','','| Source row | Explicit local identities | Status |','| --- | --- | --- |']
for d in r['actual_C_doubt_map']:md.append('| '+str(d['source_row'])+' | '+', '.join(d['decision_ids'])+' | retained; source row counted once |')
md+=['','Row 2 covers only the final-middle projecting trace/blob and the two principal foot traces. Row 5 covers only the upper pair, existing right curl, and right flecks. New local spots, strokes, and graph endpoints keep their own identities. Shared crop references do not transfer doubts between neighboring marks.','', '## Inventory coverage','','| Merged ID | Object / local identity | Witness C IDs | A IDs | B IDs | C-reader IDs |','| --- | --- | --- | --- | --- | --- |']
for i in r['inventory']:md.append('| '+' | '.join([i['element'],i['position']+' — '+i['first_words_or_objects'],*[', '.join(i['source_element_ids'][role]) or '—' for role in ['witness_C','A','B','C']]])+' |')
md+=['','The two enclosing ovals, braces, five OK labels, ou and both parentheses, question mark, twelve graph groups, all disk drawings, isolated flecks, faint residual paths, and archive 9 comment are explicitly covered. I75/I76 make two existing faint paths explicit without changing transcription. I77 is root-only D28. Unknown residual marks have `undetermined hand`; the archive numeral retains the readers’ `another unnamed hand`.','', '## Counting and source discrepancies','','D05 counts one physical change for removal of the generic horizontal rule while retaining cancellation/hatching uncertainty. Its invisible phantom copy creates no duplicate drawing count. D06 groups the middle vertex and projecting hook; D07 groups the two upper-edge refinements. D28 has no invented reader report row.','', 'The final lower disk has four major runs already drawn in C/A/B/C-reader. Witness C/A/B inventory says “three strokes with two bold segments at an angle”; C-reader says “disk with four strokes and two adjoining thickened segments”. Root confirmed four in own crop02. This is an inventory-only correction with diff_C=false; the separate newly observed short mark near (1165,877) is counted only as D28.','', 'D10 exact primary choices: A/C-reader `\\circ|\\bullet`, B `\\bullet|\\circ`; root chose A/C-reader. D11: A `\\circ|\\bullet`, B/C-reader `\\bullet|\\circ`; root chose B/C-reader. A’s lower-second-disk source lacks the outer unsure wrapper, which B/C-reader and root include. D15 preserves the shorter root-supported course with an in-place unsure wrapper; B’s longer proposed continuation remains recorded in provenance. D22 includes the half-read faint extension and root’s interrupted gray-patch refinement.','', 'Root reports 15 distinct successful reader crops plus 2 own crops, total 17. One failed context-truncated B05 output attempt was followed by a successful retry and is excluded from seen-image counts. Check events remain empty.','']
(R/'out/checks/scan010_mapping.md').write_text('\n'.join(md))
print(json.dumps({'complete_draft':str(p),'counts':r['counts'],'coverage':r['source_coverage_checks'],'main_adjudicated':r['main_adjudicated']},ensure_ascii=False))
