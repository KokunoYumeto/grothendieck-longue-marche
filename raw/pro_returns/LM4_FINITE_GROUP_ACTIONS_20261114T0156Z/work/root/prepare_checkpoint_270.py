#!/usr/bin/env python3
"""Select frozen270 evidence and write its completed document-gate report."""
from pathlib import Path
from hashlib import sha256
import json

ROOT=Path(__file__).resolve().parents[2]
prior=json.loads((ROOT/'work/root/checkpoint_269_extra_paths.json').read_text())
paths={p for p in prior if not p.startswith('work/root/rendered/review_611_final/')}
paths.update('work/root/'+name for name in [
    'accept_f31.py','final_new_claim_acceptance_270.json','integrate_270.py',
    'integration_270_source_changes.json','assemble_270_stdout.json',
    'assemble_270_typography_stdout.json','build_270_initial_stdout.txt',
    'build_270_initial_overflow.log','build_270_final_stdout.txt',
    'pdf_qa_270_initial_stdout.json','pdf_qa_270_final_stdout.json',
    'prepare_review_619.py','prepare_review_619_stdout.json',
    'render_preparation_619_final.json','seal_root_visual_review_619.py',
    'root_visual_review_619.json','seal_render_review_619.py','render_review_619.json',
    'f31_typesetting_repair.json','f29_typesetting_final_gate_619.json',
    'f30_final_document_gate_619.json','f31_final_document_gate_619.json',
    'research_update_270.md','review_f31.txt','replay_f31_independent_audit.py',
    'replay_f31_independent_audit_stdout.json',
    'seal_continuation_reviews_270.py','actual_class_two_acceptance_270.json',
    'filled_carriers_acceptance_270.json','review_compact_family_filled_carriers.txt',
    'review_actual_transporter_class_two_and_gt0.txt','replay_actual_class_two.py',
    'review_actual_norm_branches_and_odd_local_coefficients.txt',
    'replay_actual_odd_local_midpoint.py','replay_actual_odd_local_midpoint_stdout.json',
    'seal_norm_branch_review_270.py','norm_branch_acceptance_270.json',
    'integrate_norm_branch_report_270.py','norm_branch_report_integration_270.json',
    'prepare_checkpoint_270.py','verify_package_270.py',
])
for folder in [
    'work/root/f31_independent_replay','work/part_c/f31_independent_replay',
    'work/root/actual_class_two_independent_replay',
    'work/part_c/actual_transporter_class_two_peer_review',
    'work/root/actual_odd_local_midpoint_independent_replay',
    'work/root/prior_269_snapshot',
    'work/part_c/compact_family_filled_carriers_and_expansions_build',
]:
    for p in (ROOT/folder).rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc':
            paths.add(str(p.relative_to(ROOT)))
for pattern in ['review_f31.*','f31_peer_review_body.txt','render_review_619.json','final_619_*']:
    for p in (ROOT/'work/part_c').glob(pattern):
        if p.is_file():paths.add(str(p.relative_to(ROOT)))
for suffix in ['.tex','_report.txt','_result.json']:
    paths.add('work/part_c/compact_family_filled_carriers_and_expansions'+suffix)
for stem in ['actual_transporter_class_two_and_gt0','actual_norm_branches_and_odd_local_coefficients']:
    for suffix in ['.txt','_result.json']:
        paths.add('work/part_d_attack/'+stem+suffix)
for suffix in ['.txt','.json']:
    paths.add('work/part_d_attack/review_compact_family_filled_carriers'+suffix)
for stem in ['actual_transporter_class_two','actual_odd_local_midpoint']:
    for suffix in ['.py','_output.json','_stdout.txt']:
        paths.add('work/part_d_attack/code/'+stem+suffix)
stem='work/part_a/f_full_product_one_affine_images'
for suffix in ['.tex','_results.json','_report.txt','_evidence_manifest.json']:
    paths.add(stem+suffix)
manifest=json.loads((ROOT/(stem+'_evidence_manifest.json')).read_text())
assert len(manifest['entries'])==54
for entry in manifest['entries']:
    p=Path(entry['path']);p=p if p.is_absolute() else ROOT/p
    relative=p.relative_to(ROOT)
    if len(relative.parts)>2 and relative.parts[1] in ['part_a','part_b','part_c','part_d_attack'] and relative.parts[2]=='code':
        continue
    paths.add(str(relative))

# Include the complete exact binding closures of the new peer and root gates.
# One earlier acceptance bound the then-current611 PDF at the deliverable path.
# Resolve that exact historical byte identity to the preserved611 snapshot.
historical_routes=[]
def add_bound_paths(value):
    if isinstance(value,dict):
        if all(k in value for k in ['path','bytes','sha256']):
            p=Path(value['path']);p=p if p.is_absolute() else ROOT/p
            assert p.is_file(),str(p)
            if p.stat().st_size!=value['bytes'] or sha256(p.read_bytes()).hexdigest()!=value['sha256']:
                assert str(p.relative_to(ROOT))=='deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf'
                assert value['bytes']==4139349 and value['sha256']=='6eb08722ef726aaa8894facf55915238861d7981c9d86d63cdc62e6e7dc47a97'
                p=ROOT/'work/root/prior_269_snapshot/paper.pdf'
                historical_routes.append({'original_path':value['path'],
                    'archive_path':str(p.relative_to(ROOT)),'bytes':value['bytes'],
                    'sha256':value['sha256'],
                    'exact_map':'The historical current-PDF identity is the exact preserved published269 PDF; the current619 PDF has its separate binding.'})
            assert p.stat().st_size==value['bytes'],str(p)
            assert sha256(p.read_bytes()).hexdigest()==value['sha256'],str(p)
            relative=p.relative_to(ROOT)
            if not (len(relative.parts)>2 and relative.parts[0]=='work' and relative.parts[1] in ['part_a','part_b','part_c','part_d_attack'] and relative.parts[2]=='code'):
                paths.add(str(relative))
        for child in value.values():add_bound_paths(child)
    elif isinstance(value,list):
        for child in value:add_bound_paths(child)

for name in ['work/part_c/review_f31.json','work/part_c/render_review_619.json',
             'work/root/norm_branch_acceptance_270.json',
             'work/root/actual_class_two_acceptance_270.json',
             'work/root/filled_carriers_acceptance_270.json']:
    add_bound_paths(json.loads((ROOT/name).read_text()))
review=json.loads((ROOT/'work/root/render_review_619.json').read_text())
assert review['sha256']=='4546799ef3198a11c19a7b7a81e3d9a20aca2016c9f97633826fd971ffc02175'
assert review['actually_viewed_count']==96 and not review['issues']
for item in review['rendered_images']:
    p=Path(item['path']);p=p if p.is_absolute() else ROOT/p
    paths.add(str(p.relative_to(ROOT)))
paths.add('work/root/rendered/f31_initial_overflow_page603.png')
assert len(historical_routes)==1
route_name='work/root/checkpoint_270_historical_binding_routes.json'
(ROOT/route_name).write_text(json.dumps({'status':'PASS_EXACT_HISTORICAL_BYTES','entries':historical_routes},indent=2)+'\n')
paths.add(route_name)
# Prior PNGs are reproducible from the retained exact prior PDF. Keep their
# sealed review and PDF while replacing old final-image files by the new set.
paths={p for p in paths if not p.startswith('work/root/rendered/review_611_final/')}
out_name='work/root/checkpoint_270_extra_paths.json'
paths.add(out_name)
missing=[p for p in paths if not (ROOT/p).is_file() and p!=out_name]
assert not missing,missing
out=ROOT/out_name
out.write_text(json.dumps(sorted(paths),indent=2)+'\n')

report=ROOT/'work/root/research_update_270.md'
old=report.read_bytes();text=old.decode()
marker='FINAL_VERIFICATION_270_PENDING'
assert text.count(marker)==1
pdf=ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf'
tex=ROOT/'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.tex'
review_hash=sha256((ROOT/'work/root/render_review_619.json').read_bytes()).hexdigest()
completion=f'''The final 270-claim document completed all four LuaLaTeX/BibTeX stages successfully. It has **619 pages**, **{pdf.stat().st_size:,} bytes** and PDF SHA-256 `{sha256(pdf.read_bytes()).hexdigest()}`. The TeX SHA-256 is `{sha256(tex.read_bytes()).hexdigest()}`. The bibliography retains 88 records and 77 cited/printed entries; the manuscript reading register retains 36 entries.

The initial build had exactly one overfull box, 2.14531 points, in the inline negative-crossing tuple on page603. Root actually viewed that page. The exact assembly-only repair inserts one discretionary break at its coordinate separator; every mathematical token, tuple order and frozen proof byte remains unchanged. The complete inverse text map recovers the entire frozen source. The corrected final build has **zero overfull boxes**, missing-character warnings, undefined citations/references or fatal errors. The immutable initial repair record and separate final document gate are both retained.

The final visual gate covers **96 selected pages**. Root freshly viewed pages602--605, including the corrected crossing formula and all eight displayed moving rows. Peer freshly viewed pages601,606--611,615,616,619, covering the immediately preceding changed page, the rest of F.31 and five changed reference samples. The other **82 entire PNG files** are byte-for-byte equal to previously viewed images in the sealed611 review. Both reviewers checked the complete bytes, sizes, hashes and prior-view membership. The exact611-page PDF is retained, and the independent archive verifier reproduces all82 carried PNGs directly from it. The final combined review SHA-256 is `{review_hash}`.

The complete final LuaLaTeX and BibTeX logs, all four stage outputs and both build records were independently read and preserved. The root checked the exact diagnostic and file bindings. The resolved first-pass rerun request, inherited opening-table underfull line, font-loader fallback with T1 Latin Modern, informational microtype notices and existing Tukia number-without-volume notice retain their precise recorded scope. The final stage3 and stage4 outputs agree byte for byte. No mathematical claim derives its status from the successful build.

The complete assembled F.29, F.30 and F.31 fragments each passed the forward and inverse source comparison. F.29 retains its previously recorded single row-break map; F.30 retains only the exact manuscript-passage insertion; F.31 has that passage insertion and the single discretionary-break token. Separate gates bind all three comparisons and the fresh/carry page evidence to this exact final PDF. The first-page notation concordance and every historical overflow passage remain in the selected images.

All **341 evidence routes** from F.23--F.31 are validated against their frozen manifests, including all54 F.31 entries. The archive includes the full mathematical reviews and both isolated replays, accepted class-two and norm-branch transporter continuations, and the accepted finite filled-carrier operations with their standalone visual evidence. Mathematical programs and outputs from Part D are also copied under `code/part_d_attack`; selected original paths are retained for literal frozen-review bindings. The finite catalogue assembler is run from the packaged layout using all44 required inputs, and all eight outputs must agree byte for byte. The independent verifier checks every ZIP member against its manifest, all270 unique claim rows, the39-obligation table, all341 evidence routes, all96 final image bindings and the exact document gates.

The report continues to begin with `INCOMPLETE`, immediately followed by the complete39-obligation table. The outstanding original surface deformation, original transporter nonemptiness, general affine characters with `chi(P0)!=1`, full marginal inclusions and interaction source-membership targets remain explicit. Newly included research code retains its stated scope and adds no numbered result beyond F.31.
'''
report.write_text(text.replace(marker,completion.rstrip()))
record={'status':'PASS_EVIDENCE_SELECTION_AND_FINAL_DOCUMENT_REPORT',
    'paths':len(paths),'final_pngs':96,'prior611_pngs_replaced_by_exact_prior_pdf_and_review':88,
    'report_old_sha256':sha256(old).hexdigest(),'report_new_sha256':sha256(report.read_bytes()).hexdigest(),
    'extra_paths_sha256':sha256(out.read_bytes()).hexdigest(),
    'historical_pdf_binding_routes':historical_routes}
(ROOT/'work/root/checkpoint_270_preparation.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
