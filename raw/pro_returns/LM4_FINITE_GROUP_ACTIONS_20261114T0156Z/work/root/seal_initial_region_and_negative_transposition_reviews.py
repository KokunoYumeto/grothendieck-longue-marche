#!/usr/bin/env python3
"""Seal two fully read mathematical reviews and preserve the published PDF."""
from pathlib import Path
import hashlib
import json
import shutil
from datetime import datetime, timezone

ROOT = Path('/workspace/scratch/64cb59721884')

def binding(path):
    p = ROOT / path
    data = p.read_bytes()
    return {'path': str(p.relative_to(ROOT)), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}

def read_json(path):
    return json.loads((ROOT / path).read_text())

def verify_tree(value, found):
    if isinstance(value, dict):
        if isinstance(value.get('path'), str) and 'sha256' in value:
            got = binding(value['path'])
            assert got['sha256'] == value['sha256'], value['path']
            if 'bytes' in value:
                assert got['bytes'] == value['bytes'], value['path']
            found[got['path']] = got
        for item in value.values():
            verify_tree(item, found)
    elif isinstance(value, list):
        for item in value:
            verify_tree(item, found)

def write_new(path, value):
    p = ROOT / path
    assert not p.exists(), path
    p.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')

cmeta = 'work/part_c/compact_family_initial_fixed_region_result.json'
cpeer = 'work/part_d_attack/review_compact_family_initial_fixed_region.json'
jmeta = 'work/part_d_attack/actual_gt0_negative_transposition_centralizer_result.json'
jpeer = 'work/part_c/review_actual_gt0_negative_transposition_centralizer.json'
cm = read_json(cmeta)
before_path = cm['build']['before']['path']
source_path = cm['source']['path']
before = (ROOT / before_path).read_bytes()
source = (ROOT / source_path).read_bytes()
forward = before
for edit in cm['build']['exact_edits']:
    old, new = edit['old'].encode(), edit['new'].encode()
    assert forward.count(old) == 1
    forward = forward.replace(old, new, 1)
assert forward == source
inverse = source
for edit in reversed(cm['build']['exact_edits']):
    old, new = edit['old'].encode(), edit['new'].encode()
    assert inverse.count(new) == 1
    inverse = inverse.replace(new, old, 1)
assert inverse == before
ps = cm['primary_source_check']
registered = (ROOT / ps['registered_record']['path']).read_bytes()
standalone = (ROOT / ps['standalone_record']['path']).read_bytes()
assert registered.count(b'A_Yagasaki2000') == 1
assert standalone.count(b'C_Yagasaki2000') == 1
assert registered.replace(b'A_Yagasaki2000', b'C_Yagasaki2000', 1) == standalone
assert standalone.replace(b'C_Yagasaki2000', b'A_Yagasaki2000', 1) == registered

pdf_path = 'deliverable/LM4_FINITE_GROUP_ACTIONS_paper.pdf'
pdf = binding(pdf_path)
assert pdf['bytes'] == 4194159
assert pdf['sha256'] == '4546799ef3198a11c19a7b7a81e3d9a20aca2016c9f97633826fd971ffc02175'
review_path = 'work/root/render_review_619.json'
assert binding(review_path)['sha256'] == '798efaa2f4066f49f18437bed1e3efb015945b6920562f635c0acb2f0cfc2235'
snapshot = ROOT / 'work/root/prior_270_snapshot'
snapshot.mkdir(exist_ok=True)
for src, name in [(pdf_path, 'paper.pdf'), (review_path, 'render_review.json')]:
    target = snapshot / name
    if target.exists():
        assert target.read_bytes() == (ROOT / src).read_bytes()
    else:
        shutil.copy2(ROOT / src, target)
snap_record = {
    'checkpoint': 270, 'published_library_version': 30, 'pdf_pages': 619,
    'original_pdf': pdf, 'archived_pdf': binding('work/root/prior_270_snapshot/paper.pdf'),
    'original_review': binding(review_path),
    'archived_review': binding('work/root/prior_270_snapshot/render_review.json'),
    'whole_pdf_and_review_byte_identity': True,
}
write_new('work/root/prior_270_snapshot/binding.json', snap_record)

now = datetime.now(timezone.utc).isoformat()
definitions = [
    {
        'name': 'initial_fixed_region', 'author_metadata': cmeta,
        'peer_metadata': cpeer,
        'root_report': 'work/root/review_compact_family_initial_fixed_region.txt',
        'peer_report': 'work/part_d_attack/review_compact_family_initial_fixed_region.txt',
        'source': source_path,
        'source_lines_read': 397,
        'root_source_checks': {
            'complete_primary_tex_theorems_1_1_and_2_1_read': True,
            'actually_viewed_primary_printed_pages': [1, 2],
            'actual_view_groups': [[1, 2]],
            'primary_images': ps['images'],
            'five_edit_whole_file_forward_and_inverse_bytes_equal': True,
            'single_bib_header_whole_entry_forward_and_inverse_bytes_equal': True,
        },
        'accepted_scope': 'Finite original-topology common lifted fixed region, exact all-sheet labels, common tails and compatible finite nested stages.',
        'retained_target': 'Original-tail control of accumulated correction sizes for an exhaustion and the infinite deformation.',
    },
    {
        'name': 'negative_transposition', 'author_metadata': jmeta,
        'peer_metadata': jpeer,
        'root_report': 'work/root/review_actual_gt0_negative_transposition_centralizer.txt',
        'peer_report': 'work/part_c/review_actual_gt0_negative_transposition_centralizer.txt',
        'source': 'work/part_d_attack/actual_gt0_negative_transposition_centralizer.txt',
        'source_lines_read': 283,
        'root_source_checks': {
            'D74_reopened_lines': [110, 590],
            'complete_primary_brown_theorem_2_and_following_use_read': True,
            'brown_primary_url': 'https://mat.unb.br/~pz/arquivos/Claus3.pdf',
            'brown_retrieval_ref': 'turn1275view0',
            'actually_viewed_haran_printed_pages': [9, 10],
            'actual_view_groups': [[9, 10]],
            'primary_images': read_json('work/root/negative_transposition_review_sources/render_bindings.json')['images'],
            'haran_definition_proposition_2_2_and_proof_read': True,
        },
        'accepted_scope': 'Full original C_F(J)=1, one section class, real projectivity, unique cusp g and full continuous transporter coordinates.',
        'retained_target': 'Original T nonemptiness, full unit a-b, image and original cusp alignments.',
    },
]
sealed = []
for row in definitions:
    found = {}
    for key in ('author_metadata', 'peer_metadata'):
        verify_tree(read_json(row[key]), found)
        found[row[key]] = binding(row[key])
    for key in ('root_report', 'peer_report', 'source'):
        found[row[key]] = binding(row[key])
    verify_tree(row['root_source_checks'], found)
    result = {
        'status': 'ACCEPTED_UNNUMBERED_CONTINUATION_ROOT_AND_PEER_PASS',
        'sealed_at_utc': now, 'numbered_claim_registered': False,
        'published_checkpoint_modified': False,
        'root_full_source_read': True, 'root_full_author_report_or_metadata_read': True,
        'root_full_peer_report_read': True, 'mathematical_corrections_requested': [],
        **row, 'binding_count': len(found),
        'bindings': [found[p] for p in sorted(found)],
        'sealed_by': binding('work/root/seal_initial_region_and_negative_transposition_reviews.py'),
        'published_pdf_preserved': binding('work/root/prior_270_snapshot/binding.json'),
    }
    target = f"work/root/{row['name']}_continuation_acceptance.json"
    write_new(target, result)
    sealed.append(binding(target))
print(json.dumps({'status': 'PASS', 'acceptances': sealed,
                  'snapshot': binding('work/root/prior_270_snapshot/binding.json')}, indent=2))
