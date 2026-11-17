"""Bind the actual complete root and independent rereads after the layout repair."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]
sha = lambda rel: hashlib.sha256((root / rel).read_bytes()).hexdigest()
old_sha = '3977034db5a4bf8ad203033fd9826d040504f96b76097631ca340152aaeb1644'
new_sha = '004e81c5893dc47c85b803f466a3f417132cf108903819d2272904931d44cd8c'
source = 'work_DE/B151_one_sided_family_extension_proposed.tex'
target = 'sections/b_one_sided_family_extension.tex'
assert sha(source) == sha(target) == new_sha
review_paths = ['work_A/review_B151_layout_final31.md',
                'work_A/review_B151_layout_final31.json']
independent = json.loads((root / review_paths[1]).read_text())
assert independent['status'] == 'PASS_COMPLETE_FINAL_SOURCE_REREAD'
assert independent['sha256'] == new_sha
assert not independent['mathematical_changes']
assert independent['review_sha256'] == sha(review_paths[0])
for rel in ['records/checkpoint31_root_formal_reviews.json',
            'records/checkpoint31_formal_source_copies.json']:
    path = root / rel
    prior = root / 'records/pdf_qa/checkpoint31_before_B151_layout' / rel
    assert path.read_bytes() == prior.read_bytes()
    record = json.loads(path.read_text())
    row = next(x for x in record['copies'] if x['statement'] == 'B.151')
    assert row['sha256'] == old_sha
    row['sha256'] = new_sha
    row['root_entire_final_source_read'] = True
    row['layout_only_rereview'] = review_paths
    record['layout_repair_reviewed_at'] = datetime.now(timezone.utc).isoformat()
    if 'independent_reviews' in record:
        record['independent_reviews'].update({p: sha(p) for p in review_paths})
        record['root_review_scope'] += ' The entire B151 source was then reread after the two actual overflow repairs; A independently reread the complete final source at its new exact hash. The failed combined build and all previous source/review bytes are preserved.'
        record['no_private_build_or_render_at_review'] = False
        record['build_scope_at_final_rereview'] = 'Actual combined build only; one failed layout pass and one successful corrected combined build. No component build.'
    path.write_text(json.dumps(record, indent=2)+'\n')
print('PASS: complete final B151 rereads bound; both final copy registers agree; prior bytes preserved.')
