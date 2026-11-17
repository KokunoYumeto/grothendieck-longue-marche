"""Install the reviewed heading-only repair and retain prior source bindings."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--review', required=True)
parser.add_argument('--review-text', required=True)
args = parser.parse_args()

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def bind(rel):
    raw = (ROOT/rel).read_bytes()
    return {'path': rel, 'bytes': len(raw), 'sha256': digest(raw)}

manifest = json.loads((ROOT/'work_DE/A127_A129_proof_heading_repair37.json').read_text())
review_bytes = (ROOT/args.review).read_bytes()
review = json.loads(review_bytes)
assert str(review.get('result', review.get('status', ''))).startswith('PASS')
for row in manifest['proposals']:
    proposed = row['proposed']
    assert bind(proposed['path']) == proposed
    assert proposed['sha256'] in review_bytes.decode()
    original = (ROOT/row['original']['path']).read_bytes()
    assert digest(original) == row['original']['sha256']
    assert original == (ROOT/row['preserved']).read_bytes()

dest = ROOT/'records/checkpoint37_before_proof_heading_repair'
dest.mkdir(exist_ok=False)
binding_paths = ['records/checkpoint37_formal_source_copies.json',
                 'records/checkpoint37_root_formal_reviews.json',
                 'records/checkpoint37_independent_review_manifest.json']
loaded = {rel: json.loads((ROOT/rel).read_text()) for rel in binding_paths}
copies = loaded[binding_paths[0]]['copies']
for rel in binding_paths:
    target = dest/rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes((ROOT/rel).read_bytes())
changes = []
for repair in manifest['proposals']:
    old_rel = repair['original']['path']
    copy = next(row for row in copies if row['source'] == old_rel)
    assert copy['sha256'] == repair['original']['sha256']
    new_bytes = (ROOT/repair['proposed']['path']).read_bytes()
    for rel in (copy['source'], copy['target']):
        old_bytes = (ROOT/rel).read_bytes()
        assert digest(old_bytes) == copy['sha256']
        saved = dest/rel
        saved.parent.mkdir(parents=True, exist_ok=True)
        saved.write_bytes(old_bytes)
        (ROOT/rel).write_bytes(new_bytes)
    changes.append({'statement': copy['statement'], 'old_sha256': copy['sha256'],
                    'new_sha256': digest(new_bytes), 'bytes': len(new_bytes)})
    copy['sha256'] = digest(new_bytes)
stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
review_bindings = {rel: bind(rel)['sha256'] for rel in (args.review, args.review_text)}
loaded[binding_paths[0]]['heading_repair_at'] = stamp
loaded[binding_paths[0]]['comparison'] = 'All six integrated proofs match the reviewed owned sources; A.127/A.129 have only the separately retained proof-heading repair.'
loaded[binding_paths[1]]['copies'] = copies
loaded[binding_paths[1]]['independent_reviews'].update(review_bindings)
loaded[binding_paths[1]]['heading_repair_root_review'] = {
    'complete_final_sources_read_chunk_id': '686364',
    'complete_diffs_read_chunk_id': '17090d',
    'scope': 'Only proof-internal sectioning commands changed; every mathematical passage retained.',
    'recorded_at': stamp,
}
loaded[binding_paths[2]]['source_hashes'] = {row['source']: row['sha256'] for row in copies}
loaded[binding_paths[2]]['reviews'].update(review_bindings)
loaded[binding_paths[2]]['heading_repair_at'] = stamp
for rel, data in loaded.items():
    (ROOT/rel).write_text(json.dumps(data, indent=2)+'\n')
record = {'recorded_at': stamp, 'result': 'PASS_HEADING_ONLY_REPAIR_INSTALLED',
          'changes': changes, 'independent_review': bind(args.review),
          'root_full_source_read': '686364', 'root_full_diff_read': '17090d',
          'preserved_directory': str(dest.relative_to(ROOT)),
          'build_run_by_installer': False}
with (ROOT/'records/checkpoint37_proof_heading_repair_install.json').open('x') as stream:
    json.dump(record, stream, indent=2)
    stream.write('\n')
print(json.dumps(record, indent=2))
