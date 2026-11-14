#!/usr/bin/env python3
"""Integrate frozen, fully audited E119 and D63 with every owned certificate."""
from pathlib import Path
import csv
import hashlib
import json
import shutil

R = Path(__file__).resolve().parent
B = R / 'LM7_FERMAT_TOWER'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
digest = lambda b: hashlib.sha256(b).hexdigest()
enc = lambda x: json.dumps(x, indent=2, ensure_ascii=False) + '\n'
read = lambda p: json.loads(p.read_text())
pending, reasons, mapping, amendments = {}, {}, [], []
assert not (B / 'ledger/checkpoint222_integration.json').exists()
with (B / 'LM7_FERMAT_TOWER_results.csv').open() as f:
    assert len(list(csv.DictReader(f))) == 220

def put(rel, data, reason):
    p = B / rel
    pending[p] = data.encode() if isinstance(data, str) else data
    reasons[p] = reason

def get(rel):
    p = B / rel
    return pending[p] if p in pending else p.read_bytes()

def cp(src, rel):
    p = B / rel
    if p.exists():
        assert p.read_bytes() == src.read_bytes(), str(rel)
    else:
        put(rel, src.read_bytes(), 'Exact owned source, actual output or review evidence.')
    mapping.append({'source': str(src.relative_to(R)), 'archive': str(rel), 'sha256': sha(src)})

def manifest_rows(m):
    rows = m.get('files', m.get('owned_files'))
    if isinstance(rows, dict):
        rows = [dict(path=k, **v) for k, v in rows.items()]
    return rows + m.get('immutable_inputs', [])

def verify(folder, name, expected):
    p = folder / 'ledger' / name
    assert sha(p) == expected, str(p)
    m = read(p)
    for row in manifest_rows(m):
        q = folder / row.get('path', row.get('file'))
        assert sha(q) == row['sha256'], str(q)
        if 'bytes' in row:
            assert q.stat().st_size == row['bytes'], str(q)
    return m

spec = [
    ('e119', 'research_e119', 'e_lower_fiftythree_manifest.json',
    '67657642ad1f77f73b23a0147b82f717eedb5e9c1165bba0fad5e39a16d082e1',
     'E_lower_fiftythree.tex', 'E.119', 'e_lower_fiftythree'),
    ('d63', 'D63_EXPERIMENTS', 'd_compact_orthogonal_cross_manifest.json',
     '91bace632be9d7fbad254e749e73b3c83e14165cd22bfaa847cc18c53a407786',
     'D_compact_orthogonal_cross.tex', 'D.63', 'd_compact_orthogonal_cross')]
manifests = {tag: verify(R / folder, name, expected)
             for tag, folder, name, expected, *_ in spec}
audits = {
    'root_e119_audit': ('47a38d22fa7be8b0ae579060bd0b56365d943b07c6b8c5c5be5dce0a1f2a4184', 'PASS_FULL_PROOF_SOURCES_AND_ROOT_REPLAY'),
    'root_e119_delta_audit': ('c484eee0a7deb0f15efa22aed00a46d4ae6aa93cd6dbe95a9f3ccf775b6345e4', 'PASS_EXACT_SERIALIZATION_AMENDMENT_AND_FRESH_CHECKER'),
    'd_e119_audit': ('c11b8d69304beb368b606eccba09e6ff65fff64a3d5f996c9800b8e9c6e1f92c', 'PASS'),
    'root_d63_audit': ('860386597a3e954b45fc311e351ab14f360590b828a13798811657a93fe9fd61', 'PASS_FULL_PROOF_SOURCES_AND_ROOT_REPLAY'),
    'bc_d63_audit': ('51c25b4865320f60cf89c4d9e8ee2925080e781843c2f6a46942629fd6581bbb', 'PASS')}
for name, (expected, status) in audits.items():
    p = R / name / 'audit.json'
    assert sha(p) == expected and read(p)['status'] == status, name

# These are the last actual complete build and visual/package records.
for name in ['assemble.py', 'assemble.out', 'build_pdf.py', 'build_pdf.out',
             'latex_pass1.out', 'latex_pass2.out', 'latex_pass3.out', 'bibtex.out',
             'build_certificate.json', 'pdf_qa.out', 'package.py', 'package.out']:
    p = B / 'code' / name
    if p.exists():
        cp(p, Path('code/checkpoint220_before222') / name)
cp(B / 'LM7_FERMAT_TOWER_paper.tex', Path('code/checkpoint220_before222/paper_master.tex.md'))
for p in sorted((B / 'qa').glob('*')):
    if p.is_file() and (p.name.startswith(('contact_', 'detail220_', 'visual220_'))
                       or p.name in ['pdf_qa.json', 'visual_review.md']):
        cp(p, Path('qa/history/checkpoint220_before222') / p.name)

excluded = {'sources', 'source_images', 'primary_sources', 'vendor', '__pycache__'}
allowed = {'.py', '.gp', '.cpp', '.json', '.csv', '.out', '.err', '.md', '.npz',
           '.npy', '.bin', '.tex', '.bib', '.jpg', '.png', '.pdf', '.aux', '.log',
           '.txt', '.patch', '.diff'}

def mapped_owned(p, folder, tag):
    rel = p.relative_to(folder)
    if any(x in excluded for x in rel.parts) or p.suffix not in allowed:
        return None
    if rel.parts[0] == 'sections' and len(rel.parts) == 2:
        return rel
    if rel.parts[0] == 'ledger':
        if p.name.endswith('_coverage.json') and isinstance(read(p), dict):
            return Path('ledger') / (tag + '_staging') / p.name
        return rel
    if rel.parts[0] == 'qa':
        out = Path('qa') / (tag + '_author') / Path(*rel.parts[1:])
    else:
        out = Path('code') / (tag + '_bundle') / rel
    if p.suffix in {'.tex', '.bib', '.patch', '.diff'}:
        out = out.with_name(out.name + '.md')
    elif p.name == 'proof.source.txt':
        out = out.with_name('proof.tex.md')
    elif p.name.endswith('.source.txt'):
        out = out.with_name(out.name[:-11] + '.py')
    elif p.suffix == '.txt':
        out = out.with_name(out.name + '.md')
    source_txt_stdout = p.with_name(p.name[:-11] + '.out') if p.name.endswith('.source.txt') else p.with_suffix('.out')
    if out.suffix in {'.py', '.gp'} and not p.with_suffix('.out').exists() and not p.with_name(p.stem + '_gp.out').exists() and not source_txt_stdout.exists():
        out = out.with_name(out.name + '.md')
    return out

for tag, folder_name, *_ in spec:
    folder = R / folder_name
    for p in sorted(folder.rglob('*')):
        if p.is_file():
            dest = mapped_owned(p, folder, tag)
            if dest is not None:
                cp(p, dest)
    # Every frozen owned file and immutable dependency has an exact archive copy.
    for row in manifest_rows(manifests[tag]):
        p = folder / row.get('path', row.get('file'))
        dest = mapped_owned(p, folder, tag)
        assert dest is not None, str(p)
        assert digest(get(dest)) == row['sha256'], str(p)
    for p in sorted((folder / 'ledger').glob('*')):
        if p.is_file() and p.name.endswith(('_results.json', '_report.md', '_peer.json')):
            cp(p, Path('code') / (tag + '_bundle') / 'author_freeze/ledger' / p.name)

for name in audits:
    folder = R / name
    for p in sorted(folder.rglob('*')):
        if not p.is_file() or any(x in excluded for x in p.relative_to(folder).parts) or p.suffix not in allowed:
            continue
        rel = Path('code') / name / p.relative_to(folder)
        if p.suffix in {'.tex', '.bib', '.txt', '.patch', '.diff'}:
            rel = rel.with_name(rel.name + '.md')
        if p.suffix in {'.py', '.gp'} and not p.with_suffix('.out').exists() and not p.with_name(p.stem + '_gp.out').exists():
            rel = rel.with_name(rel.name + '.md')
        cp(p, rel)
    for f in ['audit.json', 'audit.md', 'verification.json', 'replay.json']:
        p = folder / f
        if p.exists():
            cp(p, Path('ledger') / (name + '_' + f))

details = {
    'E.119': 'E.119 evaluates the first lower positional53 S-class groups as A(B1)=A(L1)=C3^2 and their full ordinary three-class groups as C9+C3^2 and C9+C3. The literal S-Hilbert field, complete S-unit bases, horizontal norm/extension maps and every completed norm fibre are proved with independent class generation and unit saturation. At the next stage the exact genus/decomposition maps give A(B2)/(sigma-1)A(B2)=C9+C3^3 and A(L2)/(sigma-1)A(L2)=C9+C3, with full Smith inverses, norm, projected extension and necessary capitulation lines. The completed S-unit norm indices are exactly 3^5 times the actual B capitulation order and 3 times the actual L order. The full upper groups, their actual normalizer actions, capitulation and later lower positional factors remain active; E46 supplies the exact root-cubing norm map back to H.',
    'D.63': 'D.63 constructs the integral graph E to M-perp, the affine lift inside L and the actual peripheral derivation. It retains every earlier central projector kernel and all D.57/W_h data while adding 40960 central coordinates and 52 coinvariants. Its exact lower action is Int(b_t,Y) beta_Y, beta_Y=(A0 eta) alpha62,Y, with homology T63=(1-e)T61(1-e)+e. The residual J63 has specified dimension 284160 and 482 coinvariants, compact norm rank 6 and kernel 476. Its actual arithmetic boundary and the full profinite source realization remain active.'}
for tag, folder, name, expected, section, ident, stem in spec:
    rel = Path('ledger') / (stem + '_results.json')
    rows = json.loads(get(rel))
    assert len(rows) == 1 and rows[0]['id'] == ident
    if isinstance(rows[0]['notes'], list):
        rows[0]['notes'] = ' '.join(rows[0]['notes'])
    rows[0]['notes'] += ' ' + details[ident]
    rows[0]['where_proved'] = rows[0]['where_proved'].replace('code/', f'code/{tag}_bundle/code/')
    rows[0]['manuscript_passages'] = '; '.join(rows[0]['manuscript_passages'])
    if ident == 'E.119':
        rows[0]['notes'] += ' Root full proof/source audit and source-only ten-stage arithmetic replay PASS, with all twelve whole decoded PARI objects equal and zero exclusions. The later exact rational-serialization amendment retains all ten unchanged GP sources/outputs; root reran the corrected checker on those root-generated outputs and compared its entire stdout/JSON byte for byte. The original and amended runs and the independent peer full proof/source and finite-map checks are attached with exact scopes.'
    else:
        rows[0]['notes'] += ' Root full proof/source audit and four complete fresh copied-source replays PASS; every entire JSON/stdout agrees excluding only elapsed_seconds. Independent peer full proof/source audit and separately written Hom/Sylow/cross-action/norm checks PASS, including 245760 cross columns and 245760 relation columns.'
    put(rel, enc(rows), 'Record complete reviews, exact archive paths and original-task scope.')
    rel = Path('ledger') / (stem + '_report.md')
    before = get(rel).decode()
    after = before
    if ident == 'E.119':
        old = 'Root reports complete proof/source review and full source-only ten-stage replay PASS; D reports full proof/source and independent map review.'
        assert after.count(old) == 1
        after = after.replace(old, 'The exact author-freeze report remains preserved under code/e119_bundle/author_freeze. Root completed the full proof/source audit and ten-stage arithmetic replay, comparing all twelve text outputs and all twelve entire decoded PARI objects. After the exact rational-serialization amendment, root independently reran the corrected checker on its own previously generated arithmetic outputs; the complete corrected stdout and JSON agree byte for byte. All ten GP sources and outputs remain unchanged. The separate independent peer proof/source and finite-map audit has also passed, with its own exact execution scope.')
    else:
        after += '\n\nRoot has now completed the full 620-line proof and 617-line source audit and four complete copied-source/input replays. Every full JSON and stdout agrees after excluding only elapsed_seconds. The independent peer has completed the full proof/source review and separately reconstructed all Hom, Sylow and cross norm maps. These records are attached separately from the exact author freeze.\n'
    after += '\n## Integrated original-task scope\n\n' + details[ident] + '\n'
    put(rel, after, 'Add completed review and exact task scope while preserving author freeze.')
    amendments.append({'file': str(rel), 'before_sha256': digest(before.encode()), 'after_sha256': digest(after.encode()), 'kind': 'Completed root and independent peer review'})

rel = Path('LM7_FERMAT_TOWER_paper.tex')
t = get(rel).decode()
for marker, addition in [(r'\input{sections/D_self_wedge_actual_corrections.tex}', r'\input{sections/D_compact_orthogonal_cross.tex}'),
                         (r'\input{sections/E_quartic_three.tex}', r'\input{sections/E_lower_fiftythree.tex}')]:
    assert t.count(marker) == 1 and addition not in t
    t = t.replace(marker, marker + '\n' + addition)
put(rel, t, 'Register both fully audited proofs.')

rel = Path('sections/E.tex')
t = get(rel).decode()
a = t.index(r'\begin{statement}{E.23}')
z = t.index(r'\end{statement}', a)
new = r'''
E.119 evaluates the first lower positional-$53$ fields:
$A(B_1)=A(L_1)=(\mathbb Z/3)^2$, with full ordinary
three-class groups $\mathbb Z/9\oplus(\mathbb Z/3)^2$
and $\mathbb Z/9\oplus\mathbb Z/3$ respectively.
Its literal $S$-Hilbert field, complete $S$-unit bases and
horizontal norm and extension maps have explicit inverse
coordinates. At the next layer its actual genus and decomposition
maps identify the two $\sigma$-coinvariant quotients as
$\mathbb Z/9\oplus(\mathbb Z/3)^3$ and
$\mathbb Z/9\oplus\mathbb Z/3$.
The full upper groups retain the exact projection kernels
$(\sigma-1)A_2$; their normalizer actions, actual capitulation
and later lower positional factors remain active.
The completed $S$-unit norm indices are exactly $3^5|K_B|$
and $3|K_L|$ for the two displayed actual capitulation kernels.
Every comparison with $H$ uses E.46's literal root-cubing norm
map. These finite transitions leave the original intrinsic,
higher-stage and unrestricted positional questions on this list.
'''
put(rel, t[:z] + new + t[z:], 'Record the actual positional53 finite stage and its retained full kernels.')

rel = Path('sections/D.tex')
t = get(rel).decode()
new = r'''
D.63 orthogonalizes the actual compact projective summands
through its explicit integral graph and lifts them inside the
retained source kernel. The actual peripheral derivation gives
$T_{63}=(1-e)T_{61}(1-e)+e$ and the exact lower action
$\operatorname{Int}(b_{t,Y})\beta_Y$, retaining the complete
D.57 and $\mathcal W_h$ maps and all old projector kernels.
The new lift adds $40\,960$ central coordinates and fifty-two
coinvariants. Its specified remaining kernel $\mathcal J_{63}$
has dimension $284\,160$ and $482$ coinvariants; its compact
norm has rank six and kernel dimension $476$.
The arithmetic boundary on this literal residual and the
full profinite source realization remain the original active
questions.
'''
for ident in ['D.13', 'D.19']:
    a = t.index(r'\begin{statement}{' + ident + '}')
    z = t.index(r'\end{statement}', a)
    t = t[:z] + new + t[z:]
put(rel, t, 'Record the D63 actual source lift and latest exact residual.')

for name in ['d_results.json', 'd_coverage.json']:
    rel = Path('ledger') / name
    rows = json.loads(get(rel))
    for row in rows:
        if name == 'd_results.json' and row['id'] in ['D.13', 'D.19']:
            row['depends_on'].append('D.63')
            row['notes'] += ' ' + details['D.63']
        if name == 'd_coverage.json' and row['task'] in ['D.e', 'D.afterLM2.1']:
            row['statement_ids'].append('D.63')
            row['outcome'] += ' ' + details['D.63']
            row['remaining_step'] = 'Evaluate the actual residual J63 arithmetic boundary on the specified 284160-dimensional module with 482 coinvariants, compact norm rank 6 and kernel 476, then the remaining full profinite source realization.'
    put(rel, enc(rows), 'Synchronize original D result rows and all33-task coverage.')

rel = Path('code/assemble.py')
t = get(rel).decode()
needle = '\ne_rows = []\n'
assert t.count(needle) == 1
t = t.replace(needle, "\ne_deps['E.23'].append('E.119')\ne_notes['E.23'] += " + repr(' ' + details['E.119']) + '\n' + needle)
needle = "(LEDGER/'e_coverage.json').write_text(json.dumps(e_coverage,ensure_ascii=False,indent=2)+'\\n')"
assert t.count(needle) == 1
block = ("for row in e_coverage:\n    if row['task'] in ('E.c','E.d','E.follow-up-4'):\n"
         "        row['statement_ids'].extend(x for x in ('E.119',) if x not in row['statement_ids'])\n"
         "    if row['task'] in ('E.d','E.follow-up-4'):\n        row['outcome'] += " + repr('; ' + details['E.119']) + '\n'
         "        row['remaining_step'] = " + repr('Evaluate the cubic intrinsic class-three map, later quartic quotients and remaining coefficient primes; the actual positional53 upper class groups, normalizer actions, capitulation and later lower norm factors; and full intrinsic metabelian/marked source preimages.') + '\n')
t = t.replace(needle, block + needle)
put(rel, t, 'Synchronize generated E23 and original E coverage rows.')

rel = Path('ledger/d_original_source_recheck.md')
t = get(rel).decode()
t += '\n\nRetrieval family turn1031 searched the exact Ihara PartI title with Cambridge/PDF and Coleman with the official MSJ domain. It returned the author bibliography, RIMS1997 catalogue, NDL Coleman metadata and separate later citing works, without a readable requested original. Retrieval family turn1055 again searched exact PartI and Coleman title/pagination with exhausted hosts excluded. It returned the same CERN metadata, author bibliography, volume catalogue and separate later works, without an original proof. No new requested original was opened or obtained, and no verification label changed.\n'
put(rel, t, 'Record actual additional original-source searches with unchanged proof-verification status.')

for p in list(pending):
    if p.suffix == '.gp' and p.with_suffix('.out') not in pending and not p.with_suffix('.out').exists():
        alt = p.with_name(p.stem + '_gp.out')
        assert alt in pending or alt.exists(), str(p)
        put(p.with_suffix('.out').relative_to(B), get(alt.relative_to(B)), 'Byte-identical alias of actual GP stdout.')
for p in pending:
    if p.suffix in {'.py', '.gp'}:
        assert p.with_suffix('.out') in pending or p.with_suffix('.out').exists(), str(p)

rel = Path('code/README.md')
t = get(rel).decode()
t += '''

## E119 and D63

E119 is retained under code/e119_bundle with all eleven mathematical input
sources, twelve complete text outputs, twelve full PARI objects, actual failed
runs and both original author replays. Its full mathematical reconstruction
accepts --gp /absolute/path/to/gp and starts from source-only empty temporary
directories. Root repeated all ten GP stages and compared all twelve complete
text outputs and all twelve entire decoded GEN objects, with no exclusions.
The exact original record remains under code/root_e119_audit.

The later exact-rational export amendment changes twelve ambient Smith-map
entries in modulus-one rows. All other JSON fields, all GP sources/outputs,
all BIN objects and the proof remain unchanged. The entire old author tree
and both old peer runs are preserved. Root read the exact source diff and ran
the corrected complete checker on its own arithmetic outputs in a fresh
directory. Its entire stdout/JSON agrees byte for byte with the amended
author output; both ambient inverse compositions and every changed entry
were independently checked. These new records are in code/root_e119_delta_audit.
The independent peer full proof/source and finite-map audit was also rerun
against all 415 amended manifest entries and retains its exact scope.

D63 is retained under code/d63_bundle with all four mathematical programs,
every actual failed/intermediate attempt, all immutable matrix inputs and
all author replay outputs. Root independently executed each complete program
in a fresh copied directory. Every whole JSON and stdout agrees after
excluding only elapsed_seconds, with all source/input hashes unchanged and
empty stderr. The independently written peer standard-library verifier
reconstructs the Hom systems, full unordered Sylow norms and all 245760
cross-action columns and all 245760 relation columns from the frozen matrices.

The exact frozen author ledgers remain under each bundle's author_freeze/ledger;
active ledgers additionally record the completed root and peer reviews.
Both standalone author PDFs and their owned QA artifacts are retained.
Integrated visual review is recorded separately after the new complete build.
Original D.13, D.19 and E.23 and the three requested-original D.a verification
gaps remain active.
'''
put(rel, t, 'Document full reconstruction, actual errors and precisely separated review scopes.')
put(Path('ledger/checkpoint222_amendments.json'), enc({'status': 'PASS', 'amendments': amendments}), 'Record exact completed-review editorial amendments.')

# Recheck every frozen source immediately before the first mutation of the main tree.
for tag, folder, name, expected, *_ in spec:
    verify(R / folder, name, expected)
changes = []
for p, data in pending.items():
    old = sha(p) if p.exists() else None
    if p.exists() and p.read_bytes() != data:
        if p.parent == B / 'sections':
            h = B / 'sections/history/checkpoint220_before222' / p.name
            h.parent.mkdir(parents=True, exist_ok=True)
            assert not h.exists()
            shutil.copy2(p, h)
        elif p.parent == B / 'ledger':
            h = B / 'code/checkpoint220_before222/ledger' / p.name
            if h.suffix == '.bib':
                h = h.with_name(h.name + '.md')
            h.parent.mkdir(parents=True, exist_ok=True)
            assert not h.exists()
            shutil.copy2(p, h)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data)
    changes.append({'path': str(p.relative_to(B)), 'before_sha256': old, 'after_sha256': sha(p), 'reason': reasons[p]})
record = {'status': 'PASS', 'added_statements': [x[5] for x in spec], 'expected_statement_count': 222,
          'original_task_rows': 33, 'original_open_statements': ['D.13', 'D.19', 'E.23'],
          'frozen_to_archive_mapping': mapping, 'changes': changes,
          'build_status': 'Assembly, complete LuaLaTeX build and actual integrated visual review follow.'}
(B / 'ledger/checkpoint222_integration.json').write_text(enc(record))
print(enc({'status': 'PASS', 'added_statements': record['added_statements'], 'expected_statement_count': 222,
           'changed_files': len(changes), 'preserved_mappings': len(mapping), 'amendments': len(amendments)}))
