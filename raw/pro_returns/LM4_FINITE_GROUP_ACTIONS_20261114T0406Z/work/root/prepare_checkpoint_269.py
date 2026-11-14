#!/usr/bin/env python3
"""Select complete frozen checkpoint evidence and finalize the reviewed-PDF report."""
from pathlib import Path
from hashlib import sha256
import json

ROOT=Path(__file__).resolve().parents[2]
prior=json.loads((ROOT/'work/root/checkpoint_267_extra_paths.json').read_text())
paths={p for p in prior if not p.startswith('work/root/rendered/review_600_final/')}
paths.update('work/root/'+name for name in [
 'accept_f29.py','accept_f30.py','final_new_claim_acceptance_268.json','final_new_claim_acceptance_269.json',
 'integrate_268.py','integrate_269.py','integration_268_source_changes.json','integration_269_source_changes.json',
 'assemble_268_stdout.json','assemble_268_typography_stdout.json','assemble_269_stdout.json',
 'build_268_initial_stdout.txt','build_268_initial_overflow.log','build_268_final_stdout.txt','build_269_initial_stdout.txt',
 'overflow_268_initial.json','pdf_qa_268_stdout.json','pdf_qa_269_initial_stdout.json',
 'prepare_review_608.py','prepare_review_611.py','render_preparation_608_final.json','render_preparation_611_final.json',
 'seal_root_visual_review_608.py','seal_root_visual_review_611.py','root_visual_review_608.json','root_visual_review_611.json',
 'seal_render_review_608.py','seal_render_review_611.py','render_review_608.json','render_review_611.json',
 'f29_typesetting_repair.json','f29_typesetting_final_gate_608.json','f29_typesetting_final_gate_611.json','f30_final_document_gate_611.json',
 'research_update_268.md','research_update_269.md','review_f29.txt','review_f30.txt',
 'replay_f29_new_verifiers.py','replay_f30_independent_audit.py','review_compact_family_displacement_graph.txt',
 'review_finite_pants_diagram_gl3_2.txt','review_actual_transporter_single_parameter_reduction.txt',
 'replay_actual_transporter_reduction.py','seal_actual_transporter_review_269.py','actual_transporter_acceptance_269.json',
 'integrate_transporter_report_269.py','transporter_report_integration_269.json',
 'prepare_checkpoint_269.py','verify_package_269.py','preserve_267_pdf.py',
])
for folder in [
 'work/root/f29_independent_replay','work/root/f30_independent_replay',
 'work/part_c/f29_independent_replay','work/part_c/f30_independent_replay',
 'work/root/four_parameter_r1_exploration','work/root/finite_pants_gl3_replay',
 'work/root/actual_transporter_independent_replay','work/part_c/actual_transporter_independent_replay',
 'work/root/prior_267_snapshot','work/root/prior_268_snapshot',
 'work/part_c/compact_family_displacement_graph_build',
]:
 for path in (ROOT/folder).rglob('*'):
  if path.is_file() and '__pycache__' not in path.parts and path.suffix!='.pyc':
   paths.add(str(path.relative_to(ROOT)))
for pattern in ['review_f29.*','review_f30.*','render_review_608.json','render_review_611.json',
                'final_608_*','final_611_*','review_actual_transporter_single_parameter_reduction.*']:
 for path in (ROOT/'work/part_c').glob(pattern):
  if path.is_file():paths.add(str(path.relative_to(ROOT)))
for name in ['compact_family_displacement_graph.tex','compact_family_displacement_graph_report.txt','compact_family_displacement_graph_result.json']:
 paths.add('work/part_c/'+name)
for name in ['review_compact_family_displacement_graph.txt','review_compact_family_displacement_graph.json',
 'finite_pants_diagram_gl3_2.txt','finite_pants_diagram_gl3_2_result.json',
 'section_bound_exact_limit.txt','section_bound_exact_limit_result.json',
 'actual_transporter_single_parameter_reduction.txt','actual_transporter_single_parameter_reduction_result.json',
 'finite_generation_primary_source_check.txt','zalesskii_2024_metadata_read_scope.txt',
 'zalesskii_2024_metadata_read_scope.json','zalesskii_2024_prosoluble_reference.bib']:
 paths.add('work/part_d_attack/'+name)
for stem in ['finite_pants_diagram_gl3_2','section_bound_insufficiency_base','actual_transporter_homology_probe','actual_transporter_reduction']:
 for suffix in ['.py','_output.json','_stdout.txt']:
  path='work/part_d_attack/code/'+stem+suffix
  assert (ROOT/path).is_file(),path
  paths.add(path)
for stem in ['f_four_parameter_product_one_images','f_product_one_first_scalar_field_images']:
 for suffix in ['.tex','_results.json','_report.txt','_evidence_manifest.json']:
  paths.add('work/part_a/'+stem+suffix)
 # The packager separately validates and routes every manifest entry.
 manifest=json.loads((ROOT/'work/part_a'/f'{stem}_evidence_manifest.json').read_text())
 for entry in manifest['entries']:
  source=Path(entry['path']);source=source if source.is_absolute() else ROOT/source
  relative=source.relative_to(ROOT)
  if len(relative.parts)>2 and relative.parts[1] in ['part_a','part_b','part_c'] and relative.parts[2]=='code':
   continue
  paths.add(str(relative))
review=json.loads((ROOT/'work/root/render_review_611.json').read_text())
assert review['sha256']=='6eb08722ef726aaa8894facf55915238861d7981c9d86d63cdc62e6e7dc47a97'
assert review['actually_viewed_count']==88 and not review['issues']
for item in review['rendered_images']:
 path=Path(item['path']);path=path if path.is_absolute() else ROOT/path
 paths.add(str(path.relative_to(ROOT)))
paths.add('work/root/rendered/f29_initial_overflow_page596.png')
# Include the peer audit/replay builders recorded by the sealed review files.
for name in ['work/part_c/review_f29.json','work/part_c/review_f30.json',
             'work/part_c/review_actual_transporter_single_parameter_reduction.json',
             'work/part_c/render_review_611.json']:
 data=json.loads((ROOT/name).read_text())
 for key in ['record_builder','review_writer','peer_replay_runner']:
  value=data.get(key)
  if isinstance(value,dict) and isinstance(value.get('path'),str):
   path=Path(value['path']);path=path if path.is_absolute() else ROOT/path
   assert path.is_file()
   paths.add(str(path.relative_to(ROOT)))
paths.add('work/root/checkpoint_269_extra_paths.json')
missing=[p for p in paths if not (ROOT/p).is_file() and p!='work/root/checkpoint_269_extra_paths.json']
assert not missing,missing
out=ROOT/'work/root/checkpoint_269_extra_paths.json'
out.write_text(json.dumps(sorted(paths),indent=2)+'\n')

report=ROOT/'work/root/research_update_269.md'
text=report.read_text()
marker='FINAL_VERIFICATION_269_PENDING'
assert text.count(marker)==1
completion='''The final 269-claim document completed all four LuaLaTeX/BibTeX stages successfully. It has **611 pages**, **4,139,349 bytes** and PDF SHA-256 `6eb08722ef726aaa8894facf55915238861d7981c9d86d63cdc62e6e7dc47a97`. The TeX SHA-256 is `83bcd3703562c8d753390e4ad33d3248bd1068ffed92856d2158349b2ef65bd2`. Its 88 bibliography records retain 77 used/printed references; the reading register has 36 entries.

The final visual gate covers **88 selected pages**. Root freshly viewed all four F.30 pages, 598--601, and peer freshly viewed the five changed bibliography samples, 602, 603, 607, 608 and 611. The other 79 full PNG files are byte-for-byte equal to images in the sealed 608-page review. Both reviewers independently checked their complete bytes, sizes, hashes and prior-view membership. The exact prior PDF and review are retained so these image comparisons remain reproducible. The final combined review SHA-256 is `a6025bedd581aee6e46b67d367707d7cf7808faef06f7f4b002d47cfb94647cf`.

The full final 1,967-line LuaLaTeX log, 48-line BibTeX log, all four stage outputs and both build records were independently read and preserved. There are **zero overfull boxes**, missing-character warnings, undefined citations/references, fatal errors or final LaTeX/package/font warnings. Stage 1's label-rerun request is resolved; stages 3 and 4 have byte-identical stdout and no rerun request. The inherited underfull opening-table line, font-loader fallback followed by T1 Latin Modern, two informational microtype notices and the Tukia number-without-volume bibliographic notice are recorded with their precise scope.

The complete assembled F.29 fragment equals its frozen proof through the one recorded reversible gathered-row break and the exact manuscript-passage insertion; the inverse comparison recovers the entire source. Its repaired F.29.25 page is an exact whole-image carry from the actual 608-page view. F.30 needs no typography repair: the complete forward and inverse passage-insertion comparison also recovers its frozen proof, and every one of its four final pages was actually viewed. Separate final document gates bind these facts to the 611-page PDF. All historical overflow passages and the first-page notation concordance remain in the bound selection.

The archive selection retains all F.23--F.30 manifest inputs through explicit original-path-to-archive-path routes, including the 63 F.29 and 37 F.30 entries, the two new proofs' complete mathematical reviews and isolated replays, the accepted surface displacement-graph note, the GL3(F2) finite diagram, the actual transporter reduction and homology-cover certificate, and the verified source-scope notes. The exact finite catalogue assembler is run from the packaged layout with its 44 required inputs and its eight accepted outputs compared byte for byte. The independent archive verifier checks every member against the size/SHA-256 manifest, the complete registry, all 287 evidence routes, the exact PDF gates and all 88 final PNGs; its source is included for reproduction.

The complete report continues to begin with `INCOMPLETE`, immediately followed by the 39-obligation table. The new affine locus and exact transporter reduction retain the unresolved general product-one character, controlled noncompact deformation and original realization obligations. Broader ongoing exploratory code, where retained, keeps its separate scope and adds no numbered result.
'''
old=report.read_bytes()
report.write_text(text.replace(marker,completion.rstrip()))
record={'status':'PASS_EVIDENCE_SELECTION_AND_FINAL_DOCUMENT_REPORT',
 'paths':len(paths),'final_pngs':88,'older_600_pngs_replaced_by_exact_prior_pdf_and_review':74,
 'report_old_sha256':sha256(old).hexdigest(),'report_new_sha256':sha256(report.read_bytes()).hexdigest(),
 'extra_paths_sha256':sha256(out.read_bytes()).hexdigest()}
(ROOT/'work/root/checkpoint_269_preparation.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
