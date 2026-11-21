"""Apply only the finite, root-reviewed reporting corrections after scan026 commits.

All original target bytes are preserved. Each transformation has its recorded
exact inverse. No page or combined-transcription file is modified here.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import copy
import hashlib
import json

BASE = Path(__file__).resolve().parents[2]
OUT = BASE / 'out'
CHECKS = OUT / 'checks'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encode(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode()


def exact(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))


def read(name):
    return json.loads((CHECKS / name).read_text())


def patch(value, operations):
    result = copy.deepcopy(value)
    for operation in operations:
        keys = [k.replace('~1', '/').replace('~0', '~')
                for k in operation['path'].split('/')[1:]]
        parent = result
        for key in keys[:-1]:
            parent = parent[int(key)] if isinstance(parent, list) else parent[key]
        key = int(keys[-1]) if isinstance(parent, list) else keys[-1]
        op = operation['op']
        if op == 'test':
            assert exact(parent[key]) == exact(operation['value']), operation['path']
        elif op == 'replace':
            assert isinstance(parent, list) or key in parent
            parent[key] = copy.deepcopy(operation['value'])
        elif op == 'add':
            if isinstance(parent, list):
                parent.insert(key, copy.deepcopy(operation['value']))
            else:
                assert key not in parent
                parent[key] = copy.deepcopy(operation['value'])
        elif op == 'remove':
            del parent[key]
        else:
            raise AssertionError(op)
    return result


def replacements(text, changes):
    for change in changes:
        assert text.count(change['old_text']) == change['expected_occurrences']
        text = text.replace(change['old_text'], change['new_text'])
    return text


parser = argparse.ArgumentParser()
parser.add_argument('--apply', action='store_true')
args = parser.parse_args()
plans = []


def add_plan(path, before_sha, after_sha, forward, inverse, proposal):
    source = BASE / path
    before = source.read_bytes()
    assert digest(before) == before_sha, path
    after = forward(before)
    assert digest(after) == after_sha, path
    assert inverse(after) == before, path
    plans.append(dict(path=path, before=before, after=after,
                      before_sha256=before_sha, after_sha256=after_sha,
                      proposal=proposal))


for name in ['final_readiness026_scan017_event_proposal.json',
             'final_readiness026_workflow_selector_proposal.json']:
    proposal = read(name)
    add_plan(proposal['target'], proposal['expected_before_sha256'],
             proposal['proposed_after_sha256'],
             lambda b, p=proposal: encode(patch(json.loads(b), p['forward_json_patch'])),
             lambda b, p=proposal: encode(patch(json.loads(b), p['inverse_json_patch'])), name)

name = 'notation_NREV01_NREV02_public_report_proposal_v01.json'
proposal = read(name)
for item in proposal['record_patches']:
    add_plan(item['path'], item['before_sha256_utf8'], item['proposed_after_sha256_utf8'],
             lambda b, p=item: encode(patch(json.loads(b), p['forward_json_patch'])),
             lambda b, p=item: encode(patch(json.loads(b), p['inverse_json_patch'])), name)

name = 'final_readiness026_validator_status_proposal.json'
proposal = read(name)
rule = proposal['exact_rule_data']
assert digest((BASE / rule['path']).read_bytes()) == rule['sha256']
add_plan(proposal['target'], proposal['expected_before_sha256'],
         proposal['proposed_after_sha256'],
         lambda b: replacements(b.decode(), proposal['forward_replacements']).encode(),
         lambda b: replacements(b.decode(), proposal['inverse_replacements']).encode(), name)
assert plans[-1]['after'] == (BASE / proposal['complete_proposed_source']['path']).read_bytes()

name = 'wf_root_crop_counts_through025_proposal/forward.patch.json'
proposal = read(name)
reverse = read('wf_root_crop_counts_through025_proposal/inverse.patch.json')
add_plan(proposal['target'], proposal['expected_file_sha256'],
         proposal['result_file_sha256'],
         lambda b: replacements(b.decode(), [proposal]).encode(),
         lambda b: replacements(b.decode(), [reverse]).encode(), name)

assert len(plans) == 6 and len({p['path'] for p in plans}) == 6
page_hashes = {str(p.relative_to(BASE)): digest(p.read_bytes())
               for p in sorted((OUT / 'pages').glob('*.tex'))}
wf = read('scan026_root_wf_extension_review_v01.json')
assert wf['approved_source_reporting_extension'] is True
assert digest((CHECKS / 'scan026_source_wf_through026_evidence_proposal_v01.json').read_bytes()) == wf['new_complete_evidence_sha256']

proof = dict(utc=datetime.now(timezone.utc).isoformat(), applied=args.apply,
             targets=[{k: v for k, v in p.items() if k not in ('before', 'after')}
                      for p in plans],
             all_exact_forward_and_inverse_checks_passed=True,
             page_hashes=page_hashes,
             wf026_review='checks/scan026_root_wf_extension_review_v01.json',
             wf026_complete_evidence='checks/scan026_source_wf_through026_evidence_proposal_v01.json')

if args.apply:
    assert 'scan 026 done ' in (OUT / 'progress.log').read_text()
    assert len(page_hashes) == 24
    target = CHECKS / 'final_readiness026_root_application.json'
    backups = CHECKS / 'final_readiness026_root_before_application'
    assert not target.exists() and not backups.exists()
    backups.mkdir()
    for i, item in enumerate(plans):
        backup = backups / (f'{i:02d}_' + Path(item['path']).name)
        backup.write_bytes(item['before'])
        assert backup.read_bytes() == item['before']
    for item in plans:
        path = BASE / item['path']
        assert path.read_bytes() == item['before']
        path.write_bytes(item['after'])
        assert digest(path.read_bytes()) == item['after_sha256']
    assert all(digest((BASE / path).read_bytes()) == value
               for path, value in page_hashes.items())
    target.write_bytes(encode(proof))
    with (OUT / 'progress.log').open('a') as stream:
        stream.write(proof['utc'] + ' final reporting corrections applied with exact inverse recovery; all 24 page files unchanged.\n')
else:
    target = CHECKS / 'final_readiness026_root_preflight.json'
    assert not target.exists()
    target.write_bytes(encode(proof))
print(json.dumps({'applied': args.apply, 'targets': len(plans),
                  'pages_unchanged': len(page_hashes), 'proof': str(target)}))
