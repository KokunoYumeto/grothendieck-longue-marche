"""Root approval of scan015 after 26 completed, distinct ink crops.

The page bytes are the already-reviewed selected draft. This script binds the
record to those bytes; it performs no further image or mathematical operation.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import hashlib
import json

BASE = Path(__file__).resolve().parents[2]
OUT = BASE / 'out'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

r = json.loads((OUT / 'checks/scan015_record_draft.json').read_text())
f = json.loads((OUT / 'checks/scan015_reader_fingerprints.json').read_text())
for key, value in f['files'].items():
    assert sha(BASE / value['path']) == value['sha256'], key
for role in 'ABC':
    reader = json.loads((OUT / 'readers/015' / role / 'report.json').read_text())
    assert all(reader[k] for k in ('full_image_viewed', 'halves_viewed', 'complete_visual_read'))
    assert not reader.get('check_events')

audit_path = OUT / 'checks/scan015_root_crop_audit.json'
audit = json.loads(audit_path.read_text())
assert audit['total_distinct'] == 26
assert len({x['path'] for x in audit['viewed_once']}) == 26
assert not audit['whole_or_halves_seen_by_root']
assert not audit['failed_unseen_attempts']
for item in audit['viewed_once']:
    item['sha256'] = sha(OUT / item['path'])
    item['successful_display_count'] = 1

source_audit = OUT / 'checks/scan015_source_audit.md'
assert source_audit.is_file()
assert not r['pending_root_decision_ids']
assert len(r['decisions']) == 96 and len(r['doubts']) == 27
assert len(r['inventory']) == 66
assert all(item['transcribed'] == 'yes' for item in r['inventory'])
assert not r['check_events']
assert "\\'ouvert" not in next(x['reading'] for x in r['doubts'] if x['decision_id'] == '015-P09')
assert 'undetermined hand' in next(x['hand'] for x in r['inventory'] if x['element'] == '015-I64')

draft = OUT / 'checks/scan015_final_draft.tex'
page_bytes = draft.read_bytes()
page = page_bytes.decode('utf-8')
page_sha = sha(draft)
assert page_sha == '943c29ba8517a981cd502b0d8c39eccb587f7ec09a1c6ef4d0854580a1f80017'
page_ref = 'pages/' + r['filename']
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def finalize_attachments(value):
    if isinstance(value, dict):
        if value.get('path') == 'checks/scan015_final_draft.tex' and 'char_start' in value:
            start, end = value['char_start'], value['char_end']
            assert 0 <= start < end <= len(page)
            value['source_manifest'] = value.pop('manifest', 'root.final_draft.tex')
            value.update(path=page_ref, sha256=page_sha,
                         body_sha256=hashlib.sha256(page[start:end].encode()).hexdigest())
        for child in value.values():
            finalize_attachments(child)
    elif isinstance(value, list):
        for child in value:
            finalize_attachments(child)

finalize_attachments(r)
for d in r['decisions']:
    d['main_approved'] = True
    assert set(d['readers']) == {'A', 'B', 'C'}
for item in r['inventory']:
    item['hand_status'] = 'root approved; qualified or mixed attribution remains explicit'

r.update(main_adjudicated=True, main_approved_utc=now,
         root_page_text_exact=page, root_actions_pending=[],
         reader_fingerprints=f,
         root_crop_audit='checks/scan015_root_crop_audit.json',
         root_source_audit='checks/scan015_source_audit.md',
         final_page=dict(path=page_ref, sha256=page_sha,
                         selected_draft='checks/scan015_final_draft.tex',
                         relation='byte-for-byte identical; character offsets preserved'),
         source_attachment_status='Root approved; final-page attachments use exact selected-draft offsets.')
r['counts'] = dict(C=sum(bool(d['diff_C']) for d in r['decisions']),
                   H=sum(bool(d['diff_H']) for d in r['decisions']),
                   decision_loci=len(r['decisions']), remaining_doubt_loci=len(r['doubts']),
                   inventory_elements=len(r['inventory']), check_events=0)
assert r['counts']['C'] == 30 and r['counts']['H'] == 49

(OUT / page_ref).write_bytes(page_bytes)
(OUT / 'records/scan015.json').write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + '\n')
approval = dict(scan=15, approved_utc=now, page=page_ref, sha256=page_sha,
                counts=r['counts'], root_crops=26,
                C_confidence=dict(Counter(d['confidence'] for d in r['decisions'] if d['diff_C'])),
                H_confidence=dict(Counter(d['confidence'] for d in r['decisions'] if d['diff_H'])),
                validation_scope='Previously reviewed source assembly; commit script supplies required structural gate.',
                source_audit_sha256=sha(source_audit))
(OUT / 'checks/scan015_root_approval.json').write_text(json.dumps(approval, ensure_ascii=False, indent=2) + '\n')
with (OUT / 'progress.log').open('a') as stream:
    stream.write('scan015 root approval ' + now + '; 26 distinct crops; byte-exact selected draft; no mathematical checks or compilation\n')
print(json.dumps(approval, ensure_ascii=False))
