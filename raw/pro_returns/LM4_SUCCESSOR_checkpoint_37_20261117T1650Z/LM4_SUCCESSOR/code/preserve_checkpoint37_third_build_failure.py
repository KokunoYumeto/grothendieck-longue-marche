"""Preserve the completed TeX output rejected for one overfull display."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import fitz

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT/'records/checkpoint37_failed_third_overfull_build'
DEST.mkdir(exist_ok=False)
names = ['records/checkpoint37_build_driver.out', 'records/checkpoint37_build_driver.err',
         'LM4_SUCCESSOR_paper.tex', 'LM4_SUCCESSOR_paper.pdf', 'LM4_SUCCESSOR_paper.log',
         'LM4_SUCCESSOR_paper.aux', 'LM4_SUCCESSOR_paper.toc', 'LM4_SUCCESSOR_paper.out',
         'LM4_SUCCESSOR_paper.bbl', 'LM4_SUCCESSOR_paper.blg',
         'work_A/A130_GT0_two_strand_fixed_group_proposed.tex',
         'sections/a_gt0_two_strand_fixed_group.tex',
         'records/checkpoint37_formal_source_copies.json',
         'records/checkpoint37_root_formal_reviews.json',
         'records/checkpoint37_independent_review_manifest.json']
names += [str(p.relative_to(ROOT)) for p in sorted((ROOT/'records/build_passes/20261117T153318037650Z').rglob('*')) if p.is_file()]
rows = []
for rel in names:
    src = ROOT/rel
    if not src.exists():
        rows.append({'path': rel, 'exists': False})
        continue
    raw = src.read_bytes()
    dst = DEST/rel
    if dst.suffix in {'.aux', '.toc', '.bbl', '.blg'}:
        dst = dst.with_name(dst.name+'.retained.txt')
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(raw)
    rows.append({'path': rel, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
                 'retained_as': str(dst.relative_to(ROOT))})
doc = fitz.open(ROOT/'LM4_SUCCESSOR_paper.pdf')
hits = [i+1 for i,p in enumerate(doc) if 'T(V)' in p.get_text() and 240 <= i+1 <= 250]
assert hits, 'Locate the actual overflow formula before rendering it.'
rendered = []
for n in hits:
    path = DEST/f'overfull-page-{n:03d}.png'
    doc[n-1].get_pixmap(matrix=fitz.Matrix(2,2), alpha=False).save(path)
    rendered.append({'page': n, 'path': str(path.relative_to(ROOT)),
                     'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
record = {'recorded_at': datetime.now(timezone.utc).isoformat(), 'checkpoint': 37,
          'actual_session_id': 89194, 'actual_launch_chunk_id': '0195c1',
          'actual_exit_code': 1, 'actual_exit_observed_chunk_id': '1978dc',
          'actual_full_driver_read_chunk_id': '075bb3',
          'pass_directory': 'records/build_passes/20261117T153318037650Z',
          'failure': 'All TeX passes completed; build wrapper rejected one26.55002pt overfull A.130 display at source line216.',
          'overfull_count': 1, 'maximum_overfull_pt': 26.55002,
          'pages': len(doc), 'rendered_overflow_formula_pages': rendered,
          'visual_approval': False, 'retained_files': rows}
with (ROOT/'records/checkpoint37_third_build_failure_observed.json').open('x') as stream:
    json.dump(record, stream, indent=2)
    stream.write('\n')
print(json.dumps({k:v for k,v in record.items() if k!='retained_files'}, indent=2))
