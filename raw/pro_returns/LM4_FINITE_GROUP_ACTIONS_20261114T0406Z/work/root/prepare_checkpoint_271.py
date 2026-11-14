#!/usr/bin/env python3
"""Select the frozen271 evidence and complete its exact document-gate report."""
from pathlib import Path
from hashlib import sha256
import csv
import json

ROOT = Path(__file__).resolve().parents[2]
sha = lambda p: sha256(p.read_bytes()).hexdigest()
prior = json.loads((ROOT / 'work/root/checkpoint_270_extra_paths.json').read_text())
paths = {p for p in prior if not p.startswith('work/root/rendered/review_619_final/')}
paths.update('work/root/' + name for name in [
    'accept_f32.py', 'final_new_claim_acceptance_271.json', 'review_f32.txt',
    'replay_f32.py', 'integrate_271.py', 'integrate_271_stdout.json',
    'integration_271_source_changes.json', 'assemble_271_initial_stdout.json',
    'build_271_initial_stdout.txt', 'pdf_qa_271_initial_stdout.json',
    'prepare_review_625.py', 'prepare_review_625_stdout.json',
    'render_preparation_625_final.json', 'seal_root_visual_review_625.py',
    'root_visual_review_625.json', 'seal_render_review_625.py',
    'seal_render_review_625_stdout.json', 'render_review_625.json',
    'f29_typesetting_final_gate_625.json', 'f30_final_document_gate_625.json',
    'f31_final_document_gate_625.json', 'f32_final_document_gate_625.json',
    'research_update_271.md', 'initial_fixed_region_binding_checks.json',
    'new_j_and_c_peer_binding_checks.json',
    'review_compact_family_initial_fixed_region.txt',
    'review_actual_gt0_negative_transposition_centralizer.txt',
    'seal_initial_region_and_negative_transposition_reviews.py',
    'initial_fixed_region_continuation_acceptance.json',
    'negative_transposition_continuation_acceptance.json',
    'review_actual_marked_v4_cusp_endomorphism.txt',
    'seal_marked_v4_review.py', 'seal_marked_v4_review_stdout.json',
    'marked_v4_continuation_acceptance.json',
    'prepare_checkpoint_271.py', 'verify_package_271.py'])
for folder in [
    'work/root/f32_independent_replay', 'work/part_c/f32_independent_replay',
    'work/part_c/f32_replay_setup_notes', 'work/root/prior_270_snapshot',
    'work/root/negative_transposition_review_sources',
    'work/part_c/compact_family_initial_fixed_region_build',
    'work/part_c/initial_fixed_region_research']:
    for p in (ROOT / folder).rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc':
            paths.add(str(p.relative_to(ROOT)))
for pattern in ['review_f32.*', 'review_f32_body.txt', 'render_review_625.json', 'final_625_*']:
    for p in (ROOT / 'work/part_c').glob(pattern):
        if p.is_file(): paths.add(str(p.relative_to(ROOT)))
for suffix in ['.tex', '_report.txt', '_result.json']:
    paths.add('work/part_c/compact_family_initial_fixed_region' + suffix)
for stem in ['actual_gt0_negative_transposition_centralizer', 'actual_marked_v4_cusp_endomorphism']:
    for suffix in ['.txt', '_result.json']:
        paths.add('work/part_d_attack/' + stem + suffix)
paths.add('work/part_d_attack/marked_extension_primary_source_check.txt')
for stem in ['work/part_d_attack/review_compact_family_initial_fixed_region',
             'work/part_c/review_actual_gt0_negative_transposition_centralizer',
             'work/part_a/review_d_marked_v4_cusp_endomorphism']:
    for suffix in ['.txt', '.json']: paths.add(stem + suffix)
stem = 'work/part_a/f_nonproduct_first_character_one_images'
for suffix in ['.tex', '_results.json', '_report.txt', '_evidence_manifest.json', '_preservation.json']:
    paths.add(stem + suffix)
manifest = json.loads((ROOT / (stem + '_evidence_manifest.json')).read_text())
assert len(manifest['entries']) == 59

old_routes = json.loads((ROOT / 'work/root/checkpoint_270_historical_binding_routes.json').read_text())['entries']
historical_routes = {(r['original_path'], r['sha256']): r for r in old_routes}
historical = {
    '6eb08722ef726aaa8894facf55915238861d7981c9d86d63cdc62e6e7dc47a97':
        ('work/root/prior_269_snapshot/paper.pdf', 4139349, 611),
    '4546799ef3198a11c19a7b7a81e3d9a20aca2016c9f97633826fd971ffc02175':
        ('work/root/prior_270_snapshot/paper.pdf', 4194159, 619)}

def add_path(p):
    relative = p.relative_to(ROOT)
    parts = relative.parts
    if not (len(parts) > 3 and parts[0] == 'work' and
            parts[1] in ['part_a', 'part_b', 'part_c', 'part_d_attack'] and parts[2] == 'code'):
        paths.add(str(relative))

def add_bound_paths(value):
    if isinstance(value, dict):
        if all(k in value for k in ['path', 'bytes', 'sha256']):
            p = Path(value['path'])
            p = p if p.is_absolute() else ROOT / p
            assert p.is_file(), str(p)
            if p.stat().st_size != value['bytes'] or sha(p) != value['sha256']:
                assert str(p.relative_to(ROOT)) == 'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf', value
                route, size, pages = historical[value['sha256']]
                assert value['bytes'] == size
                p = ROOT / route
                historical_routes[(value['path'], value['sha256'])] = {
                    'original_path': value['path'], 'archive_path': route,
                    'bytes': size, 'sha256': value['sha256'],
                    'exact_map': f'The historical current-PDF identity is the exact preserved published {pages}-page PDF; the current625 PDF has its separate binding.'}
            assert p.stat().st_size == value['bytes'] and sha(p) == value['sha256'], str(p)
            add_path(p)
        for child in value.values(): add_bound_paths(child)
    elif isinstance(value, list):
        for child in value: add_bound_paths(child)

add_bound_paths(manifest)
for name in [
    'work/root/final_new_claim_acceptance_271.json', 'work/part_c/review_f32.json',
    'work/part_c/render_review_625.json',
    'work/root/initial_fixed_region_continuation_acceptance.json',
    'work/root/negative_transposition_continuation_acceptance.json',
    'work/root/marked_v4_continuation_acceptance.json',
    'work/root/prior_270_snapshot/binding.json']:
    add_bound_paths(json.loads((ROOT / name).read_text()))
review = json.loads((ROOT / 'work/root/render_review_625.json').read_text())
assert review['sha256'] == '9d80a79e439f1928b2b7096cf9a6d5ec5ac1e01638b119c4872bf394ef635364'
assert review['actually_viewed_count'] == 102 and not review['issues']
for item in review['rendered_images']:
    p = Path(item['path'])
    paths.add(str((p if p.is_absolute() else ROOT / p).relative_to(ROOT)))
route_name = 'work/root/checkpoint_271_historical_binding_routes.json'
route_entries = sorted(historical_routes.values(), key=lambda r: (r['sha256'], r['original_path']))
assert {r['sha256'] for r in route_entries} == set(historical)
(ROOT / route_name).write_text(json.dumps({'status': 'PASS_EXACT_HISTORICAL_BYTES',
                                        'entries': route_entries}, indent=2) + '\n')
paths.add(route_name)
paths = {p for p in paths if not p.startswith('work/root/rendered/review_619_final/')}
out_name = 'work/root/checkpoint_271_extra_paths.json'
record_name = 'work/root/checkpoint_271_preparation.json'
paths.update([out_name, record_name])
missing = [p for p in paths if not (ROOT / p).is_file() and p not in [out_name, record_name]]
assert not missing, missing
out = ROOT / out_name
out.write_text(json.dumps(sorted(paths), indent=2) + '\n')

rows = list(csv.DictReader((ROOT / 'deliverable/LM4_FINITE_GROUP_ACTIONS_results.csv').open()))
assert len(rows) == len({r['id'] for r in rows}) == 271
report = ROOT / 'work/root/research_update_271.md'
old = report.read_bytes()
text = old.decode()
marker = 'FINAL_VERIFICATION_271_PENDING'
assert text.count(marker) == 1
pdf = ROOT / 'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf'
tex = ROOT / 'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.tex'
completion = f'''The final 271-claim document completed all four LuaLaTeX/BibTeX stages successfully. It has **625 pages**, **{pdf.stat().st_size:,} bytes** and PDF SHA-256 `{sha(pdf)}`. The TeX SHA-256 is `{sha(tex)}`. The bibliography retains 88 records and 77 cited/printed entries; the manuscript reading register retains 36 entries.

The complete final build has **zero overfull boxes**, missing-character warnings, undefined citations/references or fatal errors. F.32 required no typography repair. The complete assembled F.29, F.30, F.31 and F.32 fragments passed full forward and inverse byte comparisons with their frozen sources. F.29 retains its single recorded row break, F.31 its single recorded discretionary break, and the other two retain only the exact manuscript-passage insertion. Every frozen mathematical proof remains unchanged.

The final visual gate covers **102 selected pages**. Root freshly viewed pages611--614, including every new covector, auxiliary polynomial, determinant and the separation argument. Peer freshly viewed pages609,610,615,616,617,621,622,625, covering both ends of F.32, its shared F.31 page, the exact kernel/trace conclusion and five bibliography samples. All seven F.32 pages were actually viewed. The other **90 entire PNG files** are byte-for-byte equal to previously viewed images in the sealed619 review. Both reviewers checked complete bytes, sizes, hashes and prior-view membership. The exact619-page PDF and its sealed review are retained so the independent archive verifier can reproduce every carry directly. The combined final review SHA-256 is `{sha(ROOT / 'work/root/render_review_625.json')}`.

The complete 1,995-line final LuaLaTeX log, 48-line BibTeX log, all four stage outputs and both build records were independently read and preserved. Root checked the exact diagnostic and file bindings. The first-pass label-rerun notice is resolved in stages3 and4, whose entire outputs agree byte for byte. The inherited opening-table underfull line, font-loader fallback followed by T1 Latin Modern, two informational microtype notices and Tukia number-without-volume notice have their precise recorded scope. The first-page notation concordance and every historical overflow passage remain in the selected images.

The archive gate validates all **400 evidence routes** from F.23--F.32 against their frozen manifests, including all59 F.32 entries. It retains the full mathematical reviews, both isolated 1,088-check replays, the peer's independent 86-check actual-TeX parser, and all three newly accepted unnumbered continuations with their exact primary-source and review evidence. Historical bindings to the then-current611 and619 PDFs have explicit routes to those identical archived byte strings; the frozen metadata is preserved verbatim. The finite catalogue assembler runs from the packaged layout using all44 required inputs, with all eight outputs required to agree byte for byte. The independent ZIP verifier checks every member, all271 unique claim rows, the39-obligation table, all400 evidence routes, all102 final image bindings, all90 re-rendered carries, all four current document gates and every bound file in the new acceptances.

The report continues to begin with `INCOMPLETE`, immediately followed by the complete39-obligation table. The remaining original surface deformation, original transporter nonemptiness, affine characters with both first character and total product different from one, full marginal inclusions and interaction source-membership targets stay explicit. F.32 is the only new numbered claim in this checkpoint. Other included exploratory programs retain their stated scope.
'''
report.write_text(text.replace(marker, completion.rstrip()))
record = {
    'status': 'PASS_EVIDENCE_SELECTION_AND_FINAL_DOCUMENT_REPORT', 'paths': len(paths),
    'final_pngs': 102, 'prior619_pngs_replaced_by_exact_prior_pdf_and_review': 96,
    'report_old_sha256': sha256(old).hexdigest(), 'report_new_sha256': sha(report),
    'extra_paths_sha256': sha(out), 'historical_pdf_binding_routes': route_entries}
(ROOT / record_name).write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
