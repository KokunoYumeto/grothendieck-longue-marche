#!/usr/bin/env python3
"""Seal the fully read marked-V4 root and independent mathematical reviews."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json

ROOT = Path(__file__).resolve().parents[2]
expected = {
    'work/part_d_attack/actual_marked_v4_cusp_endomorphism.txt': '73306d3916270d346467aeafa42593d77e20a539eb53b1d2d6bd172a95eaa2cf',
    'work/part_d_attack/actual_marked_v4_cusp_endomorphism_result.json': 'cee4322346c91e3d68f92ad4939f0e1b7cff93250abb6cb656b08a52750161bb',
    'work/root/review_actual_marked_v4_cusp_endomorphism.txt': '5933c1c72434b65f2b9d3cc763d8aa1e3a74d958a00fb745b86e7637e68b6230',
    'work/part_a/review_d_marked_v4_cusp_endomorphism.txt': 'b5d67d416882b8a72c58e50da161a5403fb6f7f576478fec750baa70fa8fbda1',
    'work/part_a/review_d_marked_v4_cusp_endomorphism.json': 'd34b9b9a1354bfceff6c250efb65d722ed6ccb7488423bc5710d5362c6aa2625',
}
def bind(name):
    p = Path(name)
    p = p if p.is_absolute() else ROOT/p
    b = p.read_bytes()
    return {'path': str(p.relative_to(ROOT)), 'bytes': len(b), 'sha256': sha256(b).hexdigest()}
def read(name):
    return json.loads((ROOT/name).read_text())
found = {}
def verify(value):
    if isinstance(value, dict):
        if isinstance(value.get('path'), str) and 'sha256' in value:
            got = bind(value['path'])
            assert got['sha256'] == value['sha256'], value['path']
            if 'bytes' in value:
                assert got['bytes'] == value['bytes'], value['path']
            found[got['path']] = got
        for child in value.values():
            verify(child)
    elif isinstance(value, list):
        for child in value:
            verify(child)
for name, digest in expected.items():
    got = bind(name)
    assert got['sha256'] == digest, name
    found[name] = got
for name in ['work/part_d_attack/actual_marked_v4_cusp_endomorphism_result.json',
             'work/part_a/review_d_marked_v4_cusp_endomorphism.json',
             'work/root/negative_transposition_continuation_acceptance.json']:
    verify(read(name))
peer = read('work/part_a/review_d_marked_v4_cusp_endomorphism.json')
assert peer['status'] == 'PASS_FULL_INDEPENDENT_MATHEMATICAL_PEER_REVIEW'
assert not peer['corrections_requested']
assert peer['author_and_dependencies_unchanged']
record = {
    'status': 'ACCEPTED_UNNUMBERED_CONTINUATION_ROOT_AND_PEER_PASS',
    'sealed_at_utc': datetime.now(timezone.utc).isoformat(),
    'numbered_claim_registered': False, 'root_full_source_lines_read': 256,
    'root_full_author_metadata_read': True, 'root_full_primary_comparison_note_lines_read': 40,
    'root_full_peer_report_lines_read': 228,
    'mathematical_corrections_requested': [],
    'accepted_scope': 'The exact marked V4 and positive coproduct maps, unique original conjugators, subgroup-image equivalences, original F determinant and cusp value, both beta equivariances and reflection transports.',
    'retained_target': 'The full unit a-b, actual eta image, original two cusp alignments and nonempty original norm set.',
    'new_external_source_opening_claimed': False,
    'new_numerical_replay_claimed': False,
    'binding_count': len(found), 'bindings': [found[p] for p in sorted(found)],
    'sealed_by': bind('work/root/seal_marked_v4_review.py'),
}
out = ROOT/'work/root/marked_v4_continuation_acceptance.json'
assert not out.exists()
out.write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps({'status': 'PASS', 'acceptance': bind(out)}, indent=2))
