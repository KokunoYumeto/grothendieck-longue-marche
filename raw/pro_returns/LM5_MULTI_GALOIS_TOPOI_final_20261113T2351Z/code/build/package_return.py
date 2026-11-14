"""Create a new immutable checkpoint or final ZIP from the audited deliverable."""
from pathlib import Path
from collections import Counter
import csv, hashlib, json, re, shutil, sys, zipfile

BASE = Path('/workspace/scratch/36f9c078cbe9')
ROOT = BASE / 'deliverable'
mode = sys.argv[1]
assert mode in {'checkpoint_06', 'final'}
archive = BASE / f'LM5_MULTI_GALOIS_TOPOI_{mode}.zip'
if archive.exists():
    raise SystemExit(f'Refusing to overwrite immutable archive: {archive.name}')
qa = json.loads((ROOT / 'verification/current_qa.json').read_text())
assert qa['overfull_above_2pt'] == 0 and qa['undefined_diagnostics'] == 0
assert qa['visual_pages'], 'No visual inspection recorded'
report = (ROOT / 'LM5_MULTI_GALOIS_TOPOI_report.md').read_text()
assert report.startswith('INCOMPLETE\n\n| Prompt item')
assert 'F.44' in report and 'F.45' in report
rows = list(csv.DictReader((ROOT / 'LM5_MULTI_GALOIS_TOPOI_results.csv').open()))
code = ROOT / 'code/build'
code.mkdir(parents=True, exist_ok=True)
for name in ['integrate_sections.py', 'audit_package.py', 'build_checkpoint_report.py',
             'build_full_report.py', 'package_checkpoint.py', 'package_return.py', 'rebuild_paper.py', 'render_qa.py']:
    shutil.copy2(BASE / 'work' / name, code / name)
for name in ['integrate_06.out', 'audit_06.json', 'build_full_report_06.out', 'rebuild_06.out', 'render_qa_06.out',
             'build_full_report_final.out', 'audit_final.json', 'package_checkpoint_06.out']:
    p = BASE / 'work' / name
    if p.exists():
        shutil.copy2(p, code / name)
before = ROOT / 'verification/before_fixes'
before.mkdir(parents=True, exist_ok=True)
for p in ROOT.glob('build_f*.log'):
    if p.name != 'build_final.log':
        shutil.copy2(p, before / p.name)
if mode == 'final':
    history = ROOT / 'history'
    history.mkdir(exist_ok=True)
    for number in range(1, 7):
        p = BASE / f'LM5_MULTI_GALOIS_TOPOI_checkpoint_{number:02d}.zip'
        assert p.exists(), p
        shutil.copy2(p, history / p.name)
    (history / 'README.md').write_text(
        '# Immutable research checkpoints\n\n'
        '01: Part D. 02: B and D. 03: B, C and D. 04: completion of A, with E included. '
        '05: completion of E. 06: integrated F and its explicitly unresolved obligations.\n\n'
        'The current root files and sections supersede these drafts. Every earlier file and passage is retained '
        'inside its original archive. The integrated report identifies substantive supersessions and corrections.\n')
record = {'archive_name': archive.name, 'mode': mode, 'statements': len(rows),
          'status_counts': dict(Counter(r['status'] for r in rows)), 'pdf_pages': qa['pdf_pages'],
          'visual_pages': qa['visual_pages'], 'overfull_above_2pt': 0,
          'immutable_creation': True,
          'checkpoint_archives_preserved': list(range(1, 7)) if mode == 'final' else []}
recordfile = code / f'package_{mode}_output.json'
recordfile.write_text(json.dumps(record, indent=2) + '\n')
excluded = {'.aux', '.log', '.out', '.toc', '.blg', '.synctex.gz'}
files = [p for p in ROOT.rglob('*') if p.is_file()
         and not (p.parent == ROOT and p.suffix in excluded)
         and p.name != 'MANIFEST_SHA256.json']
manifest = [{'path': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size,
             'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(files)]
manifestfile = ROOT / 'MANIFEST_SHA256.json'
manifestfile.write_text(json.dumps(manifest, indent=2) + '\n')
with zipfile.ZipFile(archive, 'x', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for p in sorted(files + [manifestfile]):
        z.write(p, p.relative_to(ROOT))
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert len(z.namelist()) == len(files) + 1
    for item in manifest:
        assert hashlib.sha256(z.read(item['path'])).hexdigest() == item['sha256']
record['archive_bytes'] = archive.stat().st_size
record['archive_sha256'] = hashlib.sha256(archive.read_bytes()).hexdigest()
record['archive_members'] = len(files) + 1
print(json.dumps(record, indent=2))
(BASE / 'work' / f'upload_{mode}.json').write_text(json.dumps(
    {'uploads': [{'local_path': str(archive), 'purpose': 'create_library_file'}]}))
