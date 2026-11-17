"""Retain the actually observed second checkpoint-37 TeX failure before repair."""
from pathlib import Path
import datetime
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'records/checkpoint37_failed_second_tex_build'
DEST.mkdir(exist_ok=False)
names = [
    'records/checkpoint37_build_driver.out',
    'records/checkpoint37_build_driver.err',
    'LM4_SUCCESSOR_paper.tex',
    'LM4_SUCCESSOR_paper.pdf',
    'LM4_SUCCESSOR_paper.log',
    'LM4_SUCCESSOR_paper.aux',
    'LM4_SUCCESSOR_paper.toc',
    'LM4_SUCCESSOR_paper.out',
    'LM4_SUCCESSOR_paper.bbl',
    'LM4_SUCCESSOR_paper.blg',
    'work_DE/A127_elliptic_brunnian_cyclic_involution_proposed.tex',
    'sections/a_elliptic_brunnian_cyclic_involution.tex',
]
rows = []
for rel in names:
    src = ROOT / rel
    if not src.exists():
        rows.append({'path': rel, 'exists': False})
        continue
    raw = src.read_bytes()
    dst = DEST / rel
    if dst.suffix in {'.aux', '.toc', '.bbl', '.blg'}:
        dst = dst.with_name(dst.name + '.retained.txt')
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(raw)
    rows.append({'path': rel, 'exists': True, 'bytes': len(raw),
                 'sha256': hashlib.sha256(raw).hexdigest(),
                 'retained_as': str(dst.relative_to(ROOT))})
pass_dir = ROOT / 'records/build_passes/20261117T152507291536Z'
for src in sorted(pass_dir.rglob('*')):
    if not src.is_file():
        continue
    raw = src.read_bytes()
    dst = DEST / src.relative_to(ROOT)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    rows.append({'path': str(src.relative_to(ROOT)), 'exists': True,
                 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
                 'retained_as': str(dst.relative_to(ROOT))})
record = {
    'checkpoint': 37,
    'recorded_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'actual_command': 'python code/build_paper.py --env records/tex_recovery32/env.json > records/checkpoint37_build_driver.out 2> records/checkpoint37_build_driver.err',
    'actual_session_id': 79648,
    'actual_launch_chunk_id': '55ad01',
    'actual_exit_code': 1,
    'actual_exit_observed_chunk_id': 'e4d48f',
    'actual_full_driver_read_chunk_ids': ['67cae1', '1c1bf9'],
    'pass_directory': str(pass_dir.relative_to(ROOT)),
    'failure': 'LuaLaTeX: Improper \\prevdepth at A.127 line 81, paragraph A.127.2; no output PDF produced.',
    'diagnosis_at_recording': 'Not yet determined; no proof change inferred.',
    'retained_files': rows,
}
out = ROOT / 'records/checkpoint37_second_build_failure_observed.json'
with out.open('x', encoding='utf-8') as fh:
    json.dump(record, fh, indent=2)
    fh.write('\n')
print(json.dumps({'record': str(out.relative_to(ROOT)), 'files': len(rows),
                  'actual_build_exit_code': 1, 'preservation': 'complete'}))
