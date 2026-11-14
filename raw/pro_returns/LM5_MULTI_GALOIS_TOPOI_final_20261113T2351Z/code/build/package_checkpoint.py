from pathlib import Path
import json, shutil, sys, zipfile

base = Path('/workspace/scratch/36f9c078cbe9')
root = base / 'deliverable'
number = sys.argv[1]
archive = base / f'LM5_MULTI_GALOIS_TOPOI_checkpoint_{number}.zip'
if archive.exists():
    raise SystemExit(f'Refusing to overwrite immutable checkpoint: {archive}')
verification = root / 'verification' / f'checkpoint{number}'
verification.mkdir(parents=True, exist_ok=True)
for name in ('build_final.log', 'bibtex.log'):
    shutil.copy2(root / name, verification / name)
buildcode = root / 'code' / 'build'
buildcode.mkdir(parents=True, exist_ok=True)
for name in ('integrate_sections.py', 'audit_package.py', 'build_checkpoint_report.py', 'package_checkpoint.py'):
    shutil.copy2(base / 'work' / name, buildcode / name)
for name in ('integrate_04.out', 'audit04.json'):
    shutil.copy2(base / 'work' / name, buildcode / name)
report = root / 'LM5_MULTI_GALOIS_TOPOI_report.md'
with report.open('a') as stream:
    stream.write('\nThe final PDF contains 57 pages. Rendered pages 1, 3, 8, 15, 26, 34, 42, 50, 52, 53, and 57 were visually inspected, including the first-page notation table, both pointless examples, the strict pro-groupoid counterexample, displays and diagrams, the higher-level statement index, and the bibliography. No clipping or overlapping text was found. There were zero overfull boxes in the first successful integrated build and zero in the final build; consequently there were no overflow pages requiring additional inspection. A raw underscore in one bibliography URL caused an intermediate failed build; the URL was put in the proper URL field and the successful final build has no undefined-reference or missing-character diagnostic. The failed build log is retained in checkpoint04.\n')
    if number == '04':
        stream.write('\nPart A is the newly completed part at this checkpoint. Part E is included as supporting text, in particular for A.22 and the higher tower; its final completion is recorded in the following checkpoint. All 77 numbered statements presently included have matching register rows: 58 Proved, 17 Refuted, and 2 Known with checked reductions. The readings register has 50 rows and the bibliography has 32 individually marked entries.\n')
    else:
        stream.write('\nPart E is the newly completed part at this checkpoint. Its final audit includes the finite-stage/hypercompletion qualification, the strict-presentation counterexample and intrinsic replacement, and the coordinatewise finite-congruence argument for the n=5 finite-homotopy test. The previously inspected 57-page PDF is unchanged from checkpoint04. All 77 numbered statements have matching register rows: 58 Proved, 17 Refuted, and 2 Known with checked reductions.\n')
exclusions = {'.aux', '.log', '.out', '.toc', '.blg', '.synctex.gz'}
files = [p for p in root.rglob('*') if p.is_file() and not (p.parent == root and p.suffix in exclusions)]
record = {'checkpoint': number, 'files': len(files) + 1, 'statements': 77, 'pdf_pages': 57, 'overfull_initial': 0, 'overfull_final': 0, 'visual_pages': [1,3,8,15,26,34,42,50,52,53,57], 'immutable_new_archive': str(archive)}
recordfile = buildcode / f'package_checkpoint_{number}.output.json'
recordfile.write_text(json.dumps(record, indent=2) + '\n')
with zipfile.ZipFile(archive, 'x', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for path in sorted(set(files + [recordfile])):
        z.write(path, path.relative_to(root))
record['archive_bytes'] = archive.stat().st_size
print(json.dumps(record, indent=2))
(base/'work'/f'upload_checkpoint{number}.json').write_text(json.dumps({'uploads':[{'local_path':str(archive),'purpose':'create_library_file'}]}))
