"""Assemble, validate, and document the completed deliverables before packaging."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import csv,hashlib,json,re
from assemble import build
from validate import validate
from freeze_transcription import run as verify_freeze

B=Path(__file__).resolve().parents[1];ROOT=B.parents[1]
assert not (B/'delivery_manifest.json').exists()
summary=build()
result=validate(final=True);assert not result['errors']
verify_freeze(verify=True)
reports=[json.loads(p.read_text()) for p in sorted((B/'reviews').glob('149_scan*.json'))]
assert len(reports)==23
rows=[x for r in reports for x in r['changes']]
for r in reports:
 assert len({x['id'] for x in r['changes']})==len(r['changes'])
 assert len({x['element'] for x in r['inventory']})==len(r['inventory'])
assert sum(len(r['inventory']) for r in reports)==270
assert sum(len(r['diff_coverage']) for r in reports)==534
assert sum(r['audit']['boxes'] for r in reports)==455
assert sum(r['audit']['differences'] for r in reports)==327
assert sum(r['audit']['changed_boxes'] for r in reports)==121
required=['SP86_C13_149_transcription.tex','SP86_C13_149_changes.md','SP86_C13_149_collation.tsv','decisions.tsv','SP86_C13_149_doubts.md','SP86_C13_149_inventory.csv','SP86_C13_149_notes.md','CHECK_EVENTS.tsv','SP86_C13_149_sheet_feedback.md','SP86_C13_149_hand_log.md','progress.log','notation.md','transcription_sha256_final.json']
assert all((B/name).is_file() for name in required)
with (B/'CHECK_EVENTS.tsv').open() as f:checks=list(csv.DictReader(f,delimiter='\t'))
assert [x['statement id'] for x in checks]==['N064_check_01','N072_check_01','N076_check_01','N078_check_01']
macro_counts=Counter()
control_words=set()
for r in reports:
 text=(B/'pages'/f"{r['page']}.tex").read_text()
 control_words.update(re.findall(r'\\([A-Za-z]+)',text))
 for name in ['unsure','illegible','deleted','inserted']:macro_counts[name]+=len(re.findall(r'\\'+name+r'\{',text))
assert 'midK' not in control_words
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
result['completed_utc']=stamp
(B/'validation_final.json').write_text(json.dumps(result,indent=2)+'\n')
manifest=dict(completed_utc=stamp,status='All requested reading, audit, reconciliation and final validation complete.',pages=[r['page'] for r in reports],counts=dict(page_files=23,supplied_C_H_difference_rows=534,material_decision_places=len(rows),against_C=sum(x['against_C'] for x in rows),against_H=sum(x['against_H'] for x in rows),confidence=dict(Counter(x['confidence'] for x in rows)),supplied_marks=74,mark_decisions=dict(Counter(x['decision'] for r in reports for x in r['decisions'])),independent_boxes=455,differing_boxes=327,changed_boxes=121,inventory_entries=270,doubt_entries=sum(len(r['doubts']) for r in reports),macro_occurrences=dict(macro_counts),mathematical_check_events=4),authoritative_transcription=['SP86_C13_149_transcription.tex','pages/149_scanNNN.tex'],final_hash_manifest='transcription_sha256_final.json',earlier_preserved_hash_manifest='transcription_sha256.json',hash_history='The earlier manifest was superseded only for the documented single TeX control-word delimiter correction on 075. The final 24 file hashes were verified unchanged after assembly.',serialization_record='serialization_corrections.json',required_deliverables=required,documentation=dict(first_reader_returns='readings/ (historical)',current_page_reviews='reviews/149_scanNNN.json',fixed_independent_readings_and_adjudications='second/',crop_evidence='crops/',QA_reports_and_application_journals='reviews/final_*',cross_page_notation='notation_crosscheck.json',workflow_scripts='scripts/',checkpoint_receipts='checkpoints.json'),counting_scope='Material decision places are counted once, can affect both witnesses, and include resolved C doubts. Added or widened unresolved doubt alone and documented same-ink wrapper correspondences are excluded. Counts are not measured error probabilities.',control_sequence_review=dict(method='Alphabetic control words inspected against the supplied preamble and its standard LaTeX, AMS, ulem and TikZ dependencies; no compilation performed.',control_words=sorted(control_words),joined_midK_corrected=True),source_images_and_attached_texts_in_archive=False,halves_in_archive=False,earlier_checkpoint_zips_in_archive=False)
(B/'delivery_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
state=json.loads((B/'run_state.json').read_text());state.update(phase='reading and all final checks complete; final archive preparation',final_validation_completed_utc=stamp,final_hash_manifest='transcription_sha256_final.json',audited=[r['page'] for r in reports])
for path in [B/'run_state.json',ROOT/'run_state.json']:path.write_text(json.dumps(state,indent=2)+'\n')
with (B/'progress.log').open('a') as f:
 f.write(f'final delivery checks completed {stamp}: 23 pages; 455 independent boxes; all 327 differences adjudicated; 121 boxes changed; 74 supplied marks; 534 supplied difference rows; 270 inventory entries; final 24 transcription hashes verified unchanged; preparing SP86_C13_149.zip\n')
print(json.dumps({'completed_utc':stamp,**summary,'audit_boxes':455,'audit_differences':327,'audit_changed':121,'inventory':270,'macros':dict(macro_counts),'confidence':manifest['counts']['confidence'],'marks':manifest['counts']['mark_decisions']},ensure_ascii=False))
