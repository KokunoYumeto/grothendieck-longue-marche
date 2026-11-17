"""Finish the preserved third-build record using the actual extracted page."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import fitz

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT/'records/checkpoint37_failed_third_overfull_build'
assert DEST.is_dir()
pdf = DEST/'LM4_SUCCESSOR_paper.pdf'
assert pdf.read_bytes() == (ROOT/'LM4_SUCCESSOR_paper.pdf').read_bytes()
doc = fitz.open(pdf)
page = 246
content = doc[page-1].get_text()
assert 'T(V )' in content and 'Canonical and remaining scope.' in content
render = DEST/f'overfull-page-{page:03d}.png'
assert not render.exists()
doc[page-1].get_pixmap(matrix=fitz.Matrix(2,2), alpha=False).save(render)
rows = []
for p in sorted(DEST.rglob('*')):
    if p.is_file():
        raw = p.read_bytes()
        rows.append({'path': str(p.relative_to(ROOT)), 'bytes': len(raw),
                     'sha256': hashlib.sha256(raw).hexdigest()})
record = {'recorded_at': datetime.now(timezone.utc).isoformat(), 'checkpoint': 37,
          'actual_session_id': 89194, 'actual_launch_chunk_id': '0195c1',
          'actual_exit_code': 1, 'actual_exit_observed_chunk_id': '1978dc',
          'actual_full_driver_read_chunk_id': '075bb3',
          'pass_directory': 'records/build_passes/20261117T153318037650Z',
          'failure': 'All TeX passes completed; wrapper rejected one26.55002pt overfull A.130 display at source line216.',
          'overfull_count': 1, 'maximum_overfull_pt': 26.55002, 'pages': len(doc),
          'actual_overflow_page_located_by_full_text_read_chunk': '9fb12f',
          'rendered_overflow_formula_pages': [page],
          'visual_approval': False,
          'preservation_helper_failed_attempt': {
              'source': 'code/preserve_checkpoint37_third_build_failure.py',
              'actual_exit_code': 1, 'actual_exit_observed_chunk_id': '331a0d',
              'scope': 'All file copies succeeded; page locator searched T(V) instead of extracted T(V ) and asserted before rendering/record writing. Source retained unchanged; no build rerun.'},
          'retained_files': rows}
with (ROOT/'records/checkpoint37_third_build_failure_observed.json').open('x') as stream:
    json.dump(record, stream, indent=2)
    stream.write('\n')
print(json.dumps({'record': 'records/checkpoint37_third_build_failure_observed.json',
                  'overflow_page': page, 'render': str(render.relative_to(ROOT)),
                  'preserved_files': len(rows), 'pages': len(doc)}))
