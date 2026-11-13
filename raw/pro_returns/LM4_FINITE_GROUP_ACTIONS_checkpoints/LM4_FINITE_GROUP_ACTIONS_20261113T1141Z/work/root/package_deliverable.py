#!/usr/bin/env python3
"""Package the exact paper, registries, computations and reproducible inputs.

The package retains the INCOMPLETE marker while any obligation remains open.
It never assigns mathematical status from a successful build or computation.
"""
from pathlib import Path
import ast, csv, hashlib, json, shutil, subprocess, sys, zipfile

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'deliverable'
PREFIX = 'LM4_FINITE_GROUP_ACTIONS'
STAGE = ROOT / 'work' / 'package_staging'
MARKER = STAGE / '.lm4_package_owned'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def copy(source, dest):
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, dest)

# A PDF inspection certifies one exact byte sequence, not an earlier build.
assembly=json.loads((OUT/'assembly_check.json').read_text())
for name,expected in assembly.get('source_input_sha256',{}).items():
    if sha(ROOT/name)!=expected:
        raise RuntimeError('Assembly input changed after assembly: '+name)
pdf_hash = sha(OUT / (PREFIX + '_paper.pdf'))
build = json.loads((OUT/'build_artifact.json').read_text())
if not build['success'] or build['pdf_sha256'] != pdf_hash:
    raise RuntimeError('The current PDF has no successful matching build')
for name, expected in build['source_sha256'].items():
    if sha(OUT/name) != expected:
        raise RuntimeError('Source changed after the PDF build: '+name)
for name in ['pdf_qa.json', 'render_review.json']:
    review = json.loads((OUT / name).read_text())
    if review.get('sha256') != pdf_hash:
        raise RuntimeError('Stale or missing exact-PDF review: ' + name)
if json.loads((OUT / 'pdf_qa.json').read_text())['overfull_greater_than_2pt']:
    raise RuntimeError('The current PDF has an overfull box exceeding 2pt')

if STAGE.exists():
    if not MARKER.exists():
        raise RuntimeError('Refusing to replace an unmarked staging directory')
    shutil.rmtree(STAGE)
STAGE.mkdir(parents=True)
MARKER.write_text('Private staging directory owned by package_deliverable.py\n')

# Retain every mathematical program, exact output and finite presentation cache.
for part in ['part_a', 'part_b', 'part_c']:
    for p in sorted((ROOT / 'work' / part / 'code').rglob('*')):
        if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc':
            copy(p, STAGE / 'code' / part / p.relative_to(ROOT / 'work' / part / 'code'))
for name in ['catalogue_higher_genus.py', 'finite_checks.py', 'finite_checks.json',
             'finite_checks_stdout.txt', 'higher_genus_stdout.txt',
             'haran_pair_counts.py', 'haran_pair_counts_output.json',
             'haran_pair_counts_stdout.txt']:
    copy(ROOT / 'work' / 'root' / name, STAGE / 'code' / 'root' / name)
for folder in ['research_data', 'higher_genus_output']:
    shutil.copytree(ROOT / 'work' / 'root' / folder, STAGE / 'code' / 'root' / folder)

# The active source fragments and metadata suffice to reproduce the assembly.
tree = ast.parse((ROOT / 'work' / 'root' / 'assemble.py').read_text())
inputs = set()
for node in tree.body:
    if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id in
                                          ['FRAGMENTS', 'METADATA', 'BIBS'] for t in node.targets):
        inputs.update(ast.literal_eval(node.value))
inputs.add('work/root/prelude.tex')
for part in ['part_a', 'part_b', 'part_c', 'root']:
    p = ROOT / 'work' / part / 'readings.json'
    if p.exists(): inputs.add(str(p.relative_to(ROOT)))
inputs.add('work/part_c/b_extra_readings.json')
for name in ['assemble.py', 'build_pdf.py', 'make_report.py', 'pdf_qa.py',
             'package_deliverable.py']:
    inputs.add('work/root/' + name)
for part in ['part_a', 'part_b', 'part_c']:
    for p in (ROOT / 'work' / part).glob('*report*.md'):
        inputs.add(str(p.relative_to(ROOT)))
for optional in ['work/root/review_c52.txt', 'work/part_c/review_c52.txt', 'work/part_b/review_c53.txt', 'work/part_c/review_c51.txt', 'work/part_c/c50_independent_rerun_stdout.txt', 'work/part_c/f9_independent_rerun_stdout.txt', 'work/root/review_c50_f9.txt', 'work/part_c/review_c50.txt', 'work/part_c/review_f9.txt', 'work/part_a/review_d58.md', 'work/part_a/d58_audit_stdout.txt', 'work/root/review_d58.txt', 'work/part_c/review_c49.txt', 'work/root/review_c49.txt', 'work/root/review_c47_d56_d57.txt', 'work/part_c/review_c47.txt', 'work/part_c/review_c48.txt', 'work/part_c/review_d56.txt', 'work/part_c/review_d57.txt', 'work/root/review_c43_c44_c45.txt', 'work/root/review_d53_d54_d55.txt', 'work/part_a/review_d53.md', 'work/part_a/d53_audit_stdout.txt', 'work/part_a/review_d54_d55.md', 'work/part_a/d54_d55_audit_stdout.txt', 'work/part_c/review_c43_c46.txt', 'work/part_a/pants_recognition_centralizer_audit.md', 'work/part_c/review_c42.txt', 'work/part_c/review_c42_rerun.txt', 'work/part_a/review_d52.md', 'work/part_a/d52_audit_stdout.txt', 'work/root/review_d52.txt', 'work/part_c/d51_incidence_audit.txt', 'work/part_a/a5_cross_refinement_auxiliary.tex', 'work/part_a/a5_cross_refinement_auxiliary_results.json', 'work/part_b/c_scope_audit.md', 'work/part_b/c12_auxiliary_audit.md', 'work/part_c/d22_independent_audit.tex', 'work/part_c/review_c37.txt', 'work/part_c/review_d45.txt', 'work/part_a/review_d43.md', 'work/root/review_c38_d45_d46.txt', 'work/part_c/review_c39.txt', 'work/part_c/review_c40.txt', 'work/part_c/review_c41.txt', 'work/part_c/review_f8.txt', 'work/part_b/review_f8.txt', 'work/root/review_f8_rerun_stdout.txt', 'work/root/research_updates_20261113.md', 'work/part_a/review_d50.md', 'work/part_a/review_d51.md', 'work/root/review_d51.txt', 'work/part_b/review_d50.txt', 'work/part_c/review_d47.txt', 'work/part_c/review_d49.txt', 'work/root/review_d47_rerun_stdout.txt', 'work/root/review_c39_d47_d48_d49.txt']:
    if (ROOT / optional).exists(): inputs.add(optional)
for name in sorted(inputs):
    if (ROOT / name).exists(): copy(ROOT / name, STAGE / name)

for name in [PREFIX + '_paper.tex', PREFIX + '_paper.pdf', PREFIX + '_references.bib',
             PREFIX + '_results.csv', PREFIX + '_readings.csv', PREFIX + '_report.md']:
    copy(OUT / name, STAGE / name)
for name in ['assembly_check.json', 'build_commands.json', 'build_artifact.json', 'pdf_qa.json', 'render_review.json',
             PREFIX + '_paper.log', PREFIX + '_paper.bbl', PREFIX + '_paper.blg',
             'build_stage_1_stdout.txt', 'build_stage_2_stdout.txt',
             'build_stage_3_stdout.txt', 'build_stage_4_stdout.txt']:
    p = OUT / name
    if p.exists(): copy(p, STAGE / 'verification' / name)
for name in ['overflow_initial.json', 'overflow_second.json',
             'overflow_204_page.json', 'overflow_261_page.json', 'render_review_211.json', 'render_review_222.json', 'render_review_232.json', 'render_review_238.json', 'render_review_240.json', 'render_review_247.json', 'render_review_261.json', 'render_review_290.json', 'render_review_293.json', 'render_review_300.json', 'build_initial_success.log', 'build_second_overflow.log']:
    p = ROOT / 'work' / 'root' / name
    if p.exists(): copy(p, STAGE / 'verification' / name)

required = json.loads((STAGE / 'code/part_b/low_complexity_catalogue_required_paths.json').read_text())
missing = [p for p in required['required_for_assembler'] if not (STAGE / p).is_file()]
if missing: raise RuntimeError('Missing catalogue inputs: ' + repr(missing))
before = {p: sha(STAGE / p) for p in required['generated_outputs']}
proc = subprocess.run([sys.executable, str(STAGE / 'code/part_b/assemble_low_complexity_catalogues.py')],
                      cwd=STAGE, capture_output=True, text=True)
(STAGE / 'verification' / 'package_catalogue_stdout.txt').write_text(proc.stdout + proc.stderr)
if proc.returncode: raise RuntimeError('Packaged catalogue validation failed')
after = {p: sha(STAGE / p) for p in required['generated_outputs']}
if before != after: raise RuntimeError('Packaged catalogue output changed')

stats = {}
for row in csv.DictReader((OUT / (PREFIX + '_results.csv')).open()):
    stats[row['status']] = stats.get(row['status'], 0) + 1
state = 'INCOMPLETE' if stats.get('Open') else 'See the obligation register'
readme = f'''# {PREFIX}

**{state}**

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority claimed.

The paper and its report retain every unresolved obligation. A successful
computation or PDF build does not change the mathematical status of a claim.
The report begins with the complete 39-obligation register.

## Main files

- `{PREFIX}_paper.pdf` and `{PREFIX}_paper.tex`: the self-contained paper.
- `{PREFIX}_results.csv`: one row for each numbered statement.
- `{PREFIX}_readings.csv`: doubtful manuscript readings and mathematical evidence.
- `{PREFIX}_references.bib`: source metadata and individual verification notes.
- `{PREFIX}_report.md`: proof, source, computation and remaining-obligation record.
- `manifest.csv`: exact size and SHA-256 hash of every other packaged file.

Registered statuses: {', '.join(f'{k}={v}' for k,v in sorted(stats.items()))}.

## Complete finite-action index

Start with `code/part_b/low_complexity_catalogue_README.md` and
`code/part_b/low_complexity_catalogue_index.csv`. They route all 16 types,
882 mapping-class subgroup rows and 889 injective realization rows to their
exact section certificates. The exceptional realization fibers are retained.
All paths in the index are relative to this ZIP root.

The master assembler can be rerun from this directory:

```sh
python code/part_b/assemble_low_complexity_catalogues.py
```

Every required input is included. Packaging itself reruns this command and
compares all eight generated outputs byte for byte with the accepted outputs.

## Computation layout

`code/part_a`, `code/part_b`, `code/part_c`, and `code/root` contain every
mathematical program, its captured outputs, the finite presentation caches,
and the original machine-readable genus-two/genus-three census inputs.
The latter include their source attribution and hash verification. Individual
programs write their outputs beside themselves; invoke each by its file path.
Python 3.12 was used. The finite-presentation enumerators use SymPy; accepted exact checks also use
the Python standard library and the included modules. The explicitly marked
seven-point braid exploration uses NumPy and numerical crossing extraction;
it supplies no asserted relation or injectivity proof. Accepted certificates
use exact integer, rational, finite-field, permutation or free-word operations.
Every infinite assertion has its separate proof; exploratory files retain
their stated scope and are not promoted by inclusion in this archive.

## Paper build and source assembly

With LuaLaTeX and BibTeX installed, the root paper builds directly:

```sh
lualatex -interaction=nonstopmode -halt-on-error {PREFIX}_paper.tex
bibtex {PREFIX}_paper
lualatex -interaction=nonstopmode -halt-on-error {PREFIX}_paper.tex
lualatex -interaction=nonstopmode -halt-on-error {PREFIX}_paper.tex
```

The active modular sources and metadata are retained under `work/`.
Running `python work/root/assemble.py` regenerates the paper and registers
under a newly created `deliverable/` directory. The supplied
`work/root/build_pdf.py --full` configures writable TeX caches for the Linux
environment used here; an ordinary TeX installation can use the four commands
above instead. `pdf_qa.py` needs PyMuPDF and renders pages for visual review.
Its rendered images alone do not certify that they have been viewed.

`verification/` retains build logs, the assembly audit, PDF checks, visual
review records when present, and the packaged catalogue execution record.
'''
(STAGE / 'README.md').write_text(readme)

# Captured interpreter caches are irrelevant and excluded from the ZIP.
for cache in STAGE.rglob('__pycache__'):
    shutil.rmtree(cache)
MARKER.unlink()
files = sorted(p for p in STAGE.rglob('*') if p.is_file())
summary = {
    'status': state, 'claims_by_status': stats,
    'catalogue_required_inputs': len(required['required_for_assembler']),
    'missing_catalogue_inputs': missing,
    'catalogue_outputs_byte_identical': before == after,
    'catalogue_output_count': len(before),
    'payload_file_count_before_manifest_and_summary': len(files),
    'uncompressed_payload_bytes_before_manifest_and_summary': sum(p.stat().st_size for p in files),
    'excluded': ['__pycache__', '*.pyc'],
}
(OUT / 'package_manifest_summary.json').write_text(json.dumps(summary, indent=2) + '\n')
copy(OUT / 'package_manifest_summary.json', STAGE / 'verification/package_manifest_summary.json')
# Incorporate the successful package-layout check in the report before hashing.
report = subprocess.run([sys.executable, str(ROOT / 'work/root/make_report.py')],
                        cwd=ROOT, capture_output=True, text=True)
if report.returncode:
    raise RuntimeError('Report regeneration failed: ' + report.stderr)
copy(OUT / (PREFIX + '_report.md'), STAGE / (PREFIX + '_report.md'))
with (STAGE / 'manifest.csv').open('w', newline='') as f:
    w = csv.writer(f); w.writerow(['path', 'bytes', 'sha256'])
    for p in sorted(STAGE.rglob('*')):
        if p.is_file() and p.name != 'manifest.csv':
            w.writerow([str(p.relative_to(STAGE)), p.stat().st_size, sha(p)])
archive = OUT / (PREFIX + '.zip')
with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for p in sorted(STAGE.rglob('*')):
        if p.is_file(): z.write(p, str(p.relative_to(STAGE)))
with zipfile.ZipFile(archive) as z:
    bad = z.testzip()
    if bad: raise RuntimeError('ZIP CRC failed at ' + bad)
    entries = len(z.namelist())
MARKER.write_text('Private staging directory owned by package_deliverable.py\n')
verification = {'archive': archive.name, 'bytes': archive.stat().st_size,
                'sha256': sha(archive), 'entries': entries, 'crc_error': bad,
                **summary}
(OUT / 'package_zip_verification.json').write_text(json.dumps(verification, indent=2) + '\n')
print(json.dumps(verification, indent=2))
