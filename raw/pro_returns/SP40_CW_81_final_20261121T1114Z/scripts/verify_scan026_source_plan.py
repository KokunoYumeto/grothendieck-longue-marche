"""Replay one finite source-splice plan, preserving original bytes and offsets.

This reads source text only. It opens no images and makes no ink decisions.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json

p = argparse.ArgumentParser()
p.add_argument('plan')
p.add_argument('proposal')
p.add_argument('audit')
a = p.parse_args()
BASE = Path(__file__).resolve().parents[2]
cache = {}

def read(path):
    path = Path(path)
    if not path.is_absolute():
        path = BASE/path
    assert path.suffix.lower() not in {'.jpg', '.jpeg', '.png', '.pdf', '.zip'}
    if path not in cache:
        cache[path] = path.read_bytes()
    return cache[path]

def sha(data):
    return hashlib.sha256(data).hexdigest()

def verify_span(ref):
    raw = read(ref['path'])
    assert sha(raw) == ref['sha256']
    text = raw.decode('utf-8')
    value = text[ref['char_start']:ref['char_end']]
    assert value == ref['literal']
    assert sha(value.encode()) == ref['body_sha256']
    if 'utf8_byte_start' in ref:
        assert raw[ref['utf8_byte_start']:ref['utf8_byte_end']] == value.encode()
    return value

plan = json.loads(read(a.plan))
original_bytes = read(plan['base']['path'])
assert sha(original_bytes) == plan['base']['sha256']
original = original_bytes.decode('utf-8')
fragments, inverse_splices, reviewed = [], [], []
oldpos = newpos = 0
for edit in sorted(plan['edits'], key=lambda x:x['base_char_start']):
    start, end = edit['base_char_start'], edit['base_char_end']
    assert oldpos <= start <= end
    assert original[start:end] == edit['before']
    replacement = ''
    for piece in edit['replacement_pieces']:
        replacement += verify_span(piece['source']) if 'source' in piece else piece['literal']
        for ref in piece.get('root_authority_refs', []):
            verify_span(ref)
    for ref in edit.get('root_authority_refs', []):
        verify_span(ref)
    prefix = original[oldpos:start]
    fragments.extend([prefix, replacement])
    new_start = newpos + len(prefix)
    new_end = new_start + len(replacement)
    inverse_splices.append((new_start, new_end, edit['before']))
    reviewed.append({'edit_id':edit['edit_id'], 'old_range':[start,end],
                     'new_range':[new_start,new_end],
                     'before_sha256':sha(edit['before'].encode()),
                     'after_sha256':sha(replacement.encode())})
    oldpos, newpos = end, new_end
fragments.append(original[oldpos:])
selected = ''.join(fragments)
proposal_bytes = read(a.proposal)
assert selected.encode() == proposal_bytes
restored = selected
for start, end, old in reversed(inverse_splices):
    restored = restored[:start] + old + restored[end:]
assert restored.encode() == original_bytes
assert all(path.read_bytes() == value for path,value in cache.items())
audit = {'verified_utc':datetime.now(timezone.utc).isoformat(), 'author':'/root',
         'plan_path':a.plan, 'plan_sha256':sha(read(a.plan)),
         'original_sha256':sha(original_bytes), 'proposal_sha256':sha(proposal_bytes),
         'literal_splices':reviewed, 'forward_exact':True, 'inverse_exact':True,
         'all_bound_source_and_authority_spans_exact':True,
         'all_inputs_unchanged':True, 'image_views':0,
         'source_review_status':'Review coverage is separately recorded by root; this script supplies exact source mapping only.'}
out = Path(a.audit)
if not out.is_absolute():
    out = BASE/out
assert not out.exists()
out.write_text(json.dumps(audit, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'audit':str(out), 'splices':len(reviewed),
                  'proposal_sha256':sha(proposal_bytes),
                  'forward_exact':True, 'inverse_exact':True}))
