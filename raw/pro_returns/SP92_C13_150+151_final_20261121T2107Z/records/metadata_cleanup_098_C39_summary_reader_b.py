"""Apply root's explicit correction of the new C39 H-summary, not a historical witness."""
from pathlib import Path
import copy
import hashlib
import json
from datetime import datetime, timezone

W = Path('/workspace/scratch/d7279cb02214/SP92_C13_150+151_work')
record_path = W / 'records/150_scan098.json'
log_path = W / 'records/metadata_cleanup_096_098_reader_b.json'
before_bytes = record_path.read_bytes()
before = json.loads(before_bytes)
after = copy.deepcopy(before)
log = json.loads(log_path.read_text())
sha = lambda value: hashlib.sha256(value).hexdigest()
assert 'authorized_followup' not in log
c39 = next(i for i, row in enumerate(after['changes']) if row['id'] == 'C39')
d0774 = next(i for i, row in enumerate(after['diff_coverage']) if row['diff_id'] == 'D0774')
old_h = after['changes'][c39]['H']
assert old_h == 'Underbrace below V_J intersection X_L*'
new_h = 'Lower annotation described in a note; no bracket encoded'
after['changes'][c39]['H'] = new_h
assert after['changes'][c39]['against_H'] is True
old_reason = after['diff_coverage'][d0774]['reason']
assert 'shared brace encoding' in old_reason
new_reason = (
    'The lower V_J^{X_L^*} is encoded beneath the formula in C and quoted in H’s following note; '
    'that formula and the vertical comparison agree. C39 records the audited square-ended bracket: '
    'C encoded a brace, while H described the lower annotation in a note without encoding a bracket.'
)
after['diff_coverage'][d0774]['reason'] = new_reason
expected = copy.deepcopy(before)
expected['changes'][c39]['H'] = new_h
expected['diff_coverage'][d0774]['reason'] = new_reason
assert after == expected
assert all(sha((W / relative).read_bytes()) == digest
           for relative, digest in log['unchanged_input_hashes'].items())
assert record_path.read_bytes() == before_bytes
encoded = json.dumps(after, ensure_ascii=False, indent=2) + '\n'
assert json.loads(encoded) == after
temp = record_path.with_suffix('.metadata_cleanup.tmp')
assert not temp.exists()
temp.write_text(encoded, encoding='utf-8')
temp.replace(record_path)
assert json.loads(record_path.read_text()) == after

authorization = (
    'Root explicitly authorized correction of the new 098 C39 H summary to '
    '"Lower annotation described in a note; no bracket encoded", with against_H=true retained. '
    'This is a current audit-summary correction, not an edit to historical witness material.'
)
followup_edits = [
    {'page':'150_scan098', 'path':f'changes/{c39}/H', 'before':old_h, 'after':new_h,
     'reason':authorization, 'audit_boxes':['B03']},
    {'page':'150_scan098', 'path':f'diff_coverage/{d0774}/reason', 'before':old_reason, 'after':new_reason,
     'reason':'Remove the resulting implication that H encoded a brace.', 'audit_boxes':['B03']},
]
log['edits'].extend(followup_edits)
log['field_edit_count'] += 2
log['edits_by_page']['150_scan098'] += 2
log['authorized_followup'] = {
    'completed_utc':datetime.now(timezone.utc).isoformat(),
    'authorization':authorization,
    'changed_fields_only':[item['path'] for item in followup_edits],
    'against_H_retained_true':True,
    'all_other_record_values_unchanged_in_followup':True,
    'record_hash_before_followup':sha(before_bytes),
    'record_hash_after_followup':sha(record_path.read_bytes()),
}
log['checks'].pop('witness_fields_unchanged')
log['checks']['historical_witness_fields_unchanged'] = True
log['checks']['only_authorized_new_C39_H_summary_corrected'] = True
log['record_hashes']['150_scan098']['after'] = sha(record_path.read_bytes())
log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
assert all(sha((W / relative).read_bytes()) == digest
           for relative, digest in log['unchanged_input_hashes'].items())
print(json.dumps({'total_field_edits':log['field_edit_count'],'by_page':log['edits_by_page'],
                  'C39_H':new_h,'against_H':after['changes'][c39]['against_H'],
                  'protected_checks':'passed'},ensure_ascii=False))
