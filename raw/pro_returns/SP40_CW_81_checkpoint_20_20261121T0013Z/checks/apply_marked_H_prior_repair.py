"""Apply root-reviewed MH-P01 to its two source-metadata fields only."""
from pathlib import Path
from datetime import datetime, timezone
import copy
import hashlib
import json

BASE = Path(__file__).resolve().parents[2]
OUT = BASE / 'out'
audit_path = OUT / 'checks/marked_H_prior_source_audit.json'
receipt_path = OUT / 'checks/marked_H_prior_applied.json'
assert not receipt_path.exists()
digest = lambda b: hashlib.sha256(b).hexdigest()
assert digest(audit_path.read_bytes()) == '16c7fa5d1c3a74ca90c23b4e4171e599b22639189d41e247d191324a8f42b7be'
proposal = json.loads(audit_path.read_text())['proposals'][0]
assert proposal['audit_id'] == 'MH-P01' and proposal['decision_id'] == '017-D04b'
record_path = BASE / proposal['record_path']
before_bytes = record_path.read_bytes()
assert digest(before_bytes) == proposal['record_sha256']
record = json.loads(before_bytes)
encode = lambda value: (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode()
assert encode(record) == before_bytes
index = int(proposal['record_pointer'].split('/')[-1])
decision = record['decisions'][index]
assert decision['id'] == proposal['decision_id']
for key, value in proposal['prior_fields_exact'].items():
    assert decision[key] == value
assert decision['H_count_parent'] == proposal['existing_count_parent_exact']
page_path = OUT / 'pages' / record['filename']
page_sha = digest(page_path.read_bytes())
for key, value in proposal['proposed_fields'].items():
    decision[key] = value
after_bytes = encode(record)
inverse = copy.deepcopy(record)
inverse['decisions'][index].update(proposal['prior_fields_exact'])
assert encode(inverse) == before_bytes
when = datetime.now(timezone.utc).isoformat()
receipt = {
    'audit_id': 'MH-P01',
    'root_approved_utc': when,
    'root_review_scope': 'Root read the exact local H span, existing decision fields, complete proposal and supplied macro definitions; two source-metadata fields only.',
    'audit': {'path': str(audit_path.relative_to(OUT)), 'sha256': digest(audit_path.read_bytes())},
    'record': str(record_path.relative_to(OUT)),
    'before_sha256': digest(before_bytes),
    'after_sha256': digest(after_bytes),
    'field_patches': [
        {'pointer': proposal['record_pointer'] + '/' + key,
         'before': proposal['prior_fields_exact'][key], 'after': value}
        for key, value in proposal['proposed_fields'].items()
    ],
    'inverse_restores_original_record_bytes': True,
    'page': str(page_path.relative_to(OUT)),
    'page_sha256_unchanged': page_sha,
    'ink_count_reading_and_count_parent_fields_changed': False,
    'new_image_views': 0,
    'mathematical_check_events': 0,
    'source_evidence': proposal['H_sources'],
}
record_path.write_bytes(after_bytes)
assert digest(page_path.read_bytes()) == page_sha
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
with (OUT / 'progress.log').open('a') as log:
    log.write('source metadata repair MH-P01 approved/applied ' + when + '; scan017/017-D04b local H doubt flag and scope only; exact two-field inverse retained; page, counts and H parent unchanged\n')
print(json.dumps({'applied': True, 'record': receipt['record'], 'before_sha256': receipt['before_sha256'], 'after_sha256': receipt['after_sha256'], 'page_sha256_unchanged': page_sha, 'receipt': str(receipt_path)}, ensure_ascii=False))
