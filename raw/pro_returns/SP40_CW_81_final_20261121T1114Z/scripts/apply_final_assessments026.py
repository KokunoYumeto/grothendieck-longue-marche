#!/usr/bin/env python3
"""Apply the four root-reviewed assessment text operations, with exact inverses."""
import csv
import hashlib
import io
import json
from datetime import datetime, timezone
from pathlib import Path


def sha(data):
    return hashlib.sha256(data).hexdigest()


def literal(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':')).encode()


delta_path = Path('out/checks/scan026_source_final_assessment_delta_v01.json')
assert sha(delta_path.read_bytes()) == '83526534e66e0ca582514a6787713503841722ce758ac0208893c4dd1fe02ead'
delta = json.loads(delta_path.read_bytes())
claims_path = Path(delta['claim_map'])
claims = json.loads(claims_path.read_bytes())
assert len(claims) == 42
proof_path = Path('out/checks/scan026_root_final_assessment_application.json')
assert not proof_path.exists()
page_before = {str(p): sha(p.read_bytes()) for p in sorted(Path('out/pages').glob('*.tex'))}
assert len(page_before) == 24
combined = Path('out/SP40_CW_81_transcription.tex')
combined_before = sha(combined.read_bytes())
cache = {}
bindings = []
for claim in claims:
    for ref in claim['authority_refs']:
        path = ref['path']
        raw = cache.setdefault(path, Path(path).read_bytes())
        assert sha(raw) == ref['file_sha256'], path
        if 'json_pointer' in ref:
            val = json.loads(raw)
            pointer = ref['json_pointer']
            for part in pointer.split('/')[1:]:
                key = part.replace('~1', '/').replace('~0', '~')
                val = val[int(key)] if isinstance(val, list) else val[key]
            assert type(val).__name__ == ref['type'], (path, pointer)
            assert sha(literal(val)) == ref['ordered_value_sha256'], (path, pointer)
        elif 'char_start' in ref:
            fragment = raw.decode()[ref['char_start']:ref['char_end']].encode()
            assert fragment == raw[ref['utf8_byte_start']:ref['utf8_byte_end']]
            assert sha(fragment) == ref['literal_sha256'], path
        else:
            assert 'CSV_data_record_count' in ref
            assert len(list(csv.DictReader(io.StringIO(raw.decode())))) == ref['CSV_data_record_count']
        bindings.append({'claim_id': claim['claim_id'], 'reference': ref})
    for ref in claim['proposed_occurrences']:
        raw = Path(ref['path']).read_bytes()
        text = raw.decode()[ref['char_start']:ref['char_end']]
        assert text == claim['text'], claim['claim_id']
        assert text.encode() == raw[ref['utf8_byte_start']:ref['utf8_byte_end']]
        assert sha(text.encode()) == ref['literal_sha256']

prepared = []
for doc in delta['documents']:
    baseline = Path(doc['baseline_path']).read_bytes()
    target = Path(doc['target_path'])
    assert baseline == target.read_bytes()
    assert sha(baseline) == doc['baseline_sha256']
    proposed = Path(doc['proposed_path']).read_bytes()
    assert sha(proposed) == doc['proposed_sha256']
    result = baseline.decode()
    for operation in sorted(doc['operations'], key=lambda o: o['old_char_start'], reverse=True):
        a, b = operation['old_char_start'], operation['old_char_end']
        assert result[a:b] == operation['before']
        result = result[:a] + operation['after'] + result[b:]
    assert result.encode() == proposed
    inverse = result
    for operation in sorted(doc['operations'], key=lambda o: o['new_char_start'], reverse=True):
        a, b = operation['new_char_start'], operation['new_char_end']
        assert inverse[a:b] == operation['after']
        inverse = inverse[:a] + operation['before'] + inverse[b:]
    assert inverse.encode() == baseline
    prepared.append((target, proposed))

for m in delta['brief_morphisms']:
    before = Path(m['before_path']).read_bytes()
    after = Path(m['after_path']).read_bytes()
    assert sha(before) == m['before_sha256'] and sha(after) == m['after_sha256']
    h1, body1 = before.split(b'\n', 1)
    h2, body2 = after.split(b'\n', 1)
    assert h1.decode() == m['old_first_line'] and h2.decode() == m['new_first_line']
    assert body1 == body2 and len(body1) == m['common_body_bytes']
    assert sha(body1) == m['common_body_sha256']
    assert h2 + b'\n' + body1 == after and h1 + b'\n' + body2 == before

for target, proposed in prepared:
    target.write_bytes(proposed)
assert page_before == {str(p): sha(p.read_bytes()) for p in sorted(Path('out/pages').glob('*.tex'))}
assert combined_before == sha(combined.read_bytes())
proof = {
    'root_review': 'Accepted after complete review of all new wording, four exact operations, 42 sentence authority bindings, both full brief diffs, and the full forward/inverse proof. Earlier historical assessment text had already been read completely.',
    'applied_utc': datetime.now(timezone.utc).isoformat(),
    'delta_sha256': sha(delta_path.read_bytes()),
    'claims_sha256': sha(claims_path.read_bytes()),
    'authority_reference_count': len(bindings),
    'all_exact_authority_references_and_proposed_occurrences_verified': True,
    'both_document_forward_and_inverse_bytes_exact': True,
    'both_header_only_brief_forward_and_inverse_bytes_exact': True,
    'documents': [{k: d[k] for k in ['target_path', 'baseline_path', 'baseline_sha256', 'proposed_sha256']} for d in delta['documents']],
    'all_24_page_hashes_unchanged': page_before,
    'combined_sha256_unchanged': combined_before,
    'images_opened': 0,
    'new_ink_decisions': 0,
    'new_mathematical_proof_claims': 0,
}
proof_path.write_text(json.dumps(proof, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(proof, ensure_ascii=False, indent=2))
