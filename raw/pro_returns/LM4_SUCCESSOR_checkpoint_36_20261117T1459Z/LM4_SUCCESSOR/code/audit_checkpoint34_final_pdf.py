"""Audit entire final build logs and bind the corrected A109 source reviews."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import hashlib, json, re

root = Path(__file__).resolve().parents[1]
read = lambda rel: json.loads((root / rel).read_text())
sha = lambda rel: hashlib.sha256((root / rel).read_bytes()).hexdigest()
now = lambda: datetime.now(timezone.utc).isoformat()
m = read('records/checkpoint34_metrics.json')
render = read('records/pdf_qa/checkpoint34_final/render_manifest.json')
assert sha('LM4_SUCCESSOR_paper.pdf') == m['pdf_sha256'] == render['pdf_sha256']
assert m['pages'] == render['page_count'] == 646
passes = root / 'records/build_passes/20261117T122219410067Z'
assert passes.is_dir()
audits = []
for path in [root / 'LM4_SUCCESSOR_paper.log', *sorted(passes.glob('build*.log'))]:
    content = path.read_text()
    warnings = [line for line in content.splitlines()
                if re.search(r'\bwarning\b', line, re.I)
                and not line.startswith(('Package:', 'File:'))]
    issues = [line for line in content.splitlines()
              if re.search(r'overfull|undefined|missing character|^!|fatal error|rerun to get', line, re.I)]
    audits.append(dict(path=str(path.relative_to(root)), bytes=path.stat().st_size,
                       sha256=sha(path.relative_to(root)), warnings=warnings, issues=issues,
                       underfull_notices=re.findall(r'^.*Underfull.*$', content, re.M),
                       overfull=re.findall(r'^.*Overfull.*$', content, re.M),
                       complete_file_scanned=True))
final = [audits[0], next(a for a in audits if a['path'].endswith('/build_stabilize_0.log'))]
assert all(not a['warnings'] and not a['issues'] for a in final)
assert Counter(final[0]['underfull_notices']) == Counter(final[1]['underfull_notices'])
baseline = read('records/checkpoint33_visual_review.json')['final_log_and_stdout_audits'][0]['underfull_notices']
old_log = (root / 'records/pdf_qa/checkpoint34_first_layout/LM4_SUCCESSOR_paper.log').read_text()
first_overfull = re.findall(r'^.*Overfull.*$', old_log, re.M)
assert len(first_overfull) == 1 and '17.66902pt' in first_overfull[0]
assert not any(a['overfull'] for a in audits)
assert not (root / 'records/checkpoint34_corrected_build_driver.err').read_bytes()
record = dict(recorded_at=now(), result='PASS_FINAL_LOGS', final_pdf_sha256=m['pdf_sha256'],
              final_build_directory=str(passes.relative_to(root)),
              final_log_and_stdout_audits=final, all_final_build_pass_audits=audits,
              previous_overfull_count=0, first34_overfull_count=1,
              first34_overfull_notices=first_overfull, corrected_first_pass_overfull_count=0,
              final_overfull_count=0, final_underfull_count=len(final[0]['underfull_notices']),
              underfull_identical_to_checkpoint33=Counter(baseline) == Counter(final[0]['underfull_notices']),
              added_underfull_notices=list((Counter(final[0]['underfull_notices'])-Counter(baseline)).elements()),
              removed_underfull_notices=list((Counter(baseline)-Counter(final[0]['underfull_notices'])).elements()),
              scope='Every byte of all corrected build stdout files and the final engine log was scanned case-insensitively. Transient earlier-pass references are retained in their own audits. Final engine and stabilized stdout are clean. Actual image observations are separately recorded.')
target = root / 'records/checkpoint34_final_pdf_audit.json'
assert not target.exists()
target.write_text(json.dumps(record, indent=2)+'\n')

layout = read('records/checkpoint34_layout_correction.json')
layout_review = read('work_CE/review_A109_final_layout_diff34.json')
assert layout_review['result'] == 'PASS' and layout_review['whole_diff_read']
assert sha(layout['source']) == sha(layout['target']) == layout['after_sha256']
assert layout_review['current_source']['sha256'] == layout['after_sha256']
assert sha('records/checkpoint34_A109_layout.diff') == layout_review['exact_diff']['sha256']
extra = {rel: sha(rel) for rel in ['work_CE/review_A109_final_layout_diff34.txt',
                                  'work_CE/review_A109_final_layout_diff34.json']}
for rel in ['records/checkpoint34_independent_review_manifest.json',
            'records/checkpoint34_root_formal_reviews.json',
            'records/checkpoint34_formal_source_copies.json']:
    path = root / rel
    backup = root / 'records/pdf_qa/checkpoint34_first_layout' / rel
    assert backup.read_bytes() == path.read_bytes(), 'Preserve exact preceding record first.'
    data = read(rel)
    if 'source_hashes' in data:
        assert data['source_hashes'][layout['source']] == layout['before_sha256']
        data['source_hashes'][layout['source']] = layout['after_sha256']
        data['reviews'].update(extra)
    if 'copies' in data:
        rows = [row for row in data['copies'] if row['statement'] == 'A.109']
        assert len(rows) == 1 and rows[0]['sha256'] == layout['before_sha256']
        rows[0]['sha256'] = layout['after_sha256']
    if 'independent_reviews' in data:
        data['independent_reviews'].update(extra)
    data['layout_binding_update'] = dict(recorded_at=now(),
        prior_record=str(backup.relative_to(root)), prior_record_sha256=sha(backup.relative_to(root)),
        source_before=layout['before_sha256'], source_after=layout['after_sha256'],
        correction_record_sha256=sha('records/checkpoint34_layout_correction.json'),
        independent_reviews=extra,
        scope='Root read the complete two-line layout diff and independent binding. Only the provenance paragraph receives a local footnotesize ragged-right group; all mathematics and paths unchanged.')
    path.write_text(json.dumps(data, indent=2)+'\n')
print(json.dumps({key: record[key] for key in ['result','final_pdf_sha256','first34_overfull_count',
    'final_overfull_count','final_underfull_count','underfull_identical_to_checkpoint33',
    'added_underfull_notices','removed_underfull_notices']}, indent=2))
