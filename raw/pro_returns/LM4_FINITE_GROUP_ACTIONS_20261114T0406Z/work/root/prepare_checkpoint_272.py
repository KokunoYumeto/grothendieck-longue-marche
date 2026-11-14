#!/usr/bin/env python3
"""Select the exact272 evidence and complete its final document report."""
from pathlib import Path
from hashlib import sha256
import csv,json

ROOT=Path(__file__).resolve().parents[2]
sha=lambda p:sha256(p.read_bytes()).hexdigest()
prior=json.loads((ROOT/'work/root/checkpoint_271_extra_paths.json').read_text())
paths={p for p in prior if not p.startswith('work/root/rendered/review_625_final/')}
new_root=[
 'accept_f33.py','accept_f33_stdout.json','final_new_claim_acceptance_272.json',
 'review_f33.txt','integrate_272.py','integrate_272_stdout.json',
 'integration_272_source_changes.json','assemble_272_initial_stdout.json',
 'build_272_initial_stdout.txt','pdf_qa_272_initial_stdout.json',
 'prepare_review_629.py','prepare_review_629_stdout.json',
 'render_preparation_629_final.json','seal_root_visual_review_629.py',
 'seal_root_visual_review_629_stdout.json','root_visual_review_629.json',
 'seal_render_review_629.py','seal_render_review_629_stdout.json','render_review_629.json',
 'f29_typesetting_final_gate_629.json','f30_final_document_gate_629.json',
 'f31_final_document_gate_629.json','f32_final_document_gate_629.json',
 'f33_final_document_gate_629.json','research_update_272.md',
 'prepare_checkpoint_272.py','verify_package_272.py',
 'nonproduct_research_review_snapshot.txt','review_compact_family_finite_overlap_carriers.txt',
 'seal_finite_overlap_carrier_review.py','seal_finite_overlap_carrier_review_stdout.json']
paths.update('work/root/'+x for x in new_root)
accepted=[
 'orbit_track_component','order_three_candidate','four_order_three','cyclic_carrier',
 'hr_minus_one_uw_one','haran_c2_c3','disjoint_trace_carrier','canonical_transporter',
 'finite_overlap_carrier','crossed_hr_minus_one']
acceptance_names=['work/root/'+x+'_continuation_acceptance.json' for x in accepted]
paths.update(acceptance_names)
for folder in ['work/root/prior_271_snapshot','work/root/f33_independent_replay',
               'work/part_c/f33_peer_replay']:
    for p in (ROOT/folder).rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc':
            paths.add(str(p.relative_to(ROOT)))
for pattern in ['review_f33.*','review_f33_body.txt','review_f33_binding_audit.json',
                'render_review_629*','final_629_*']:
    for p in (ROOT/'work/part_c').glob(pattern):
        if p.is_file():paths.add(str(p.relative_to(ROOT)))
for pattern in ['nonproduct_*.py','nonproduct_*.json','nonproduct_*.txt',
                'check_nonproduct_*.py','check_nonproduct_*.json','check_nonproduct_*.txt',
                'seal_*_review_stdout.json','seal_*_reviews_stdout.json',
                'replay_*_stdout.json']:
    for p in (ROOT/'work/root').glob(pattern):
        if p.is_file():paths.add(str(p.relative_to(ROOT)))
for name in ['work/part_a/f_nonproduct_minimal_kernel_to_sign_pair.txt',
             'work/part_d_attack/actual_cyclic_orbit_comparison_working.txt',
             'work/part_d_attack/actual_cyclic_orbit_comparison_working_result.json',
             'work/part_d_attack/cyclic_orbit_primary_search_scope.txt',
             'work/part_d_attack/haran_closed_subgroups_1987_reference.bib']:
    paths.add(name)
stem='work/part_a/f_quadratic_sign_pair_restriction'
for suffix in ['.tex','_results.json','_report.txt','_evidence_manifest.json','_preservation.json']:
    paths.add(stem+suffix)
manifest=json.loads((ROOT/(stem+'_evidence_manifest.json')).read_text())
assert len(manifest['entries'])==69

old_routes=json.loads((ROOT/'work/root/checkpoint_271_historical_binding_routes.json').read_text())['entries']
historical_routes={(r['original_path'],r['sha256']):r for r in old_routes}
historical={
 '6eb08722ef726aaa8894facf55915238861d7981c9d86d63cdc62e6e7dc47a97':('work/root/prior_269_snapshot/paper.pdf',4139349,611),
 '4546799ef3198a11c19a7b7a81e3d9a20aca2016c9f97633826fd971ffc02175':('work/root/prior_270_snapshot/paper.pdf',4194159,619),
 '9d80a79e439f1928b2b7096cf9a6d5ec5ac1e01638b119c4872bf394ef635364':('work/root/prior_271_snapshot/paper.pdf',4233896,625)}
def add_bound_paths(value):
    if isinstance(value,dict):
        if {'path','bytes','sha256'}<=set(value):
            p=Path(value['path']);p=p if p.is_absolute() else ROOT/p
            p.relative_to(ROOT);assert p.is_file(),str(p)
            if p.stat().st_size!=value['bytes'] or sha(p)!=value['sha256']:
                assert str(p.relative_to(ROOT))=='deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf',value
                route,size,pages=historical[value['sha256']];assert value['bytes']==size
                p=ROOT/route
                historical_routes[(value['path'],value['sha256'])]={
                 'original_path':value['path'],'archive_path':route,'bytes':size,
                 'sha256':value['sha256'],
                 'exact_map':f'The historical then-current PDF is the identical archived published{pages}-page byte sequence; the current629 PDF has its separate binding.'}
            assert p.stat().st_size==value['bytes'] and sha(p)==value['sha256'],str(p)
            paths.add(str(p.relative_to(ROOT)))
        for child in value.values():add_bound_paths(child)
    elif isinstance(value,list):
        for child in value:add_bound_paths(child)
add_bound_paths(manifest)
for name in acceptance_names+[
 'work/root/final_new_claim_acceptance_272.json','work/part_c/review_f33.json',
 'work/part_c/review_f33_binding_audit.json','work/part_c/render_review_629.json',
 'work/root/prior_271_snapshot/binding.json']:
    add_bound_paths(json.loads((ROOT/name).read_text()))
review=json.loads((ROOT/'work/root/render_review_629.json').read_text())
assert review['sha256']=='693902ed60a12a9ef5d26160d56cac7b96b9ff9cde034b4f02f9b41231b2871d'
assert review['actually_viewed_count']==106 and not review['issues']
for item in review['rendered_images']:
    p=Path(item['path']);paths.add(str((p if p.is_absolute() else ROOT/p).relative_to(ROOT)))
route_name='work/root/checkpoint_272_historical_binding_routes.json'
route_entries=sorted(historical_routes.values(),key=lambda r:(r['sha256'],r['original_path']))
assert {r['sha256'] for r in route_entries}==set(historical)
(ROOT/route_name).write_text(json.dumps({'status':'PASS_EXACT_HISTORICAL_BYTES',
 'scope':'Copied earlier route descriptions retain their creation-date scope; the new current document is629 pages.',
 'entries':route_entries},indent=2)+'\n')
paths.add(route_name)
paths={p for p in paths if not p.startswith('work/root/rendered/review_625_final/')}
out_name='work/root/checkpoint_272_extra_paths.json'
record_name='work/root/checkpoint_272_preparation.json'
paths.update([out_name,record_name])
missing=[p for p in paths if not (ROOT/p).is_file() and p not in [out_name,record_name]]
assert not missing,missing
out=ROOT/out_name;assert not out.exists();out.write_text(json.dumps(sorted(paths),indent=2)+'\n')

rows=list(csv.DictReader((ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_results.csv').open()))
assert len(rows)==len({r['id'] for r in rows})==272
report=ROOT/'work/root/research_update_272.md';old=report.read_bytes();text=old.decode()
marker='FINAL_VERIFICATION_272_PENDING';assert text.count(marker)==1
pdf=ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf'
tex=ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.tex'
completion=f'''The final 272-claim document completed all four LuaLaTeX/BibTeX stages successfully. It has **629 pages**, **{pdf.stat().st_size:,} bytes** and PDF SHA-256 `{sha(pdf)}`. The TeX SHA-256 is `{sha(tex)}`. The bibliography contains89 records, including the new verified Haran entry, and77 cited/printed entries; the manuscript reading register retains36 entries.

The complete final build has **zero overfull boxes**, missing-character warnings, undefined citations/references or fatal errors. F.33 required no typography repair. All five complete assembled fragments F.29--F.33 passed forward and inverse byte comparisons against their frozen sources: the two previous recorded typography repairs are retained exactly, and F.30, F.32 and F.33 have only their exact manuscript-passage insertion. No frozen mathematical proof changed.

The visual gate covers **106 selected pages**. Root freshly viewed pages617--618, including the full gauge and inverse, exhaustive chart table, all50 pivots, terminal block and paired-coordinate inverse. Peer freshly viewed pages615,616,619,620,621,625,626,629, including the changed end of F.32, both ends of F.33 and five bibliography samples. All four F.33 pages were actually viewed. The other **96 entire PNG files** are byte-for-byte equal to previously viewed images in the sealed625 review, with complete size, hash, byte and prior-view membership checks. The exact625-page PDF and its review are preserved for independent reproduction of each carry. The combined current review SHA-256 is `{sha(ROOT/'work/root/render_review_629.json')}`.

The complete final LuaLaTeX log, BibTeX log, all four stage outputs and both build records were independently read and preserved. Root checked the diagnostic and exact-file bindings. The final diagnostic record retains the precise scope of the inherited underfull opening-table line, the initial font-loader fallback followed by Latin Modern, informational microtype notices and the Tukia number-without-volume bibliography notice. All four stages exit zero. The initial label-rerun notice is resolved in the final two byte-identical stage outputs. The notation concordance and all historical overflow passages remain in the current selected-image coverage.

The archive gate checks all **469 evidence routes** from F.23--F.33, including the69 new F.33 entries, and preserves the full root and peer mathematical and program reviews. The complete new mathematical acceptance and all ten accepted post271 continuations retain their exact bound files. The historical current-PDF bindings have explicit routes to the identical archived611-,619- and625-page byte strings. The independent archive verifier checks every member,272 unique claim rows, the39-obligation table, all469 routes, all106 image bindings, all96 carries re-rendered from the archived625 PDF, five current document gates and every bound file in the new acceptances. The packaged finite catalogue assembler uses all44 required inputs and reproduces all eight accepted outputs byte for byte.

The report still begins with `INCOMPLETE`, immediately followed by the complete39-obligation table. F.33 is the only new numbered claim in this checkpoint. The retained exploratory and pending-review files have the exact scopes described above; their presence does not register a further theorem or complete an unresolved original obligation.
'''
report.write_text(text.replace(marker,completion.rstrip()))
record={
 'status':'PASS_EVIDENCE_SELECTION_AND_FINAL_DOCUMENT_REPORT','paths':len(paths),
 'final_pngs':106,'prior625_pngs_replaced_by_exact_prior_pdf_and_review':102,
 'accepted_post271_continuations':len(accepted),
 'report_old_sha256':sha256(old).hexdigest(),'report_new_sha256':sha(report),
 'extra_paths_sha256':sha(out),'historical_pdf_binding_routes':route_entries}
(ROOT/record_name).write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
