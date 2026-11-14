#!/usr/bin/env python3
"""Integrate final frozen E121 and D64 proofs with their complete evidence."""
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
assert not (B / 'ledger/checkpoint224_integration.json').exists()
with (B / 'LM7_FERMAT_TOWER_results.csv').open() as f:
    assert len(list(csv.DictReader(f))) == 222

def put(rel, data, reason):
    p = B / rel
    pending[p] = data.encode() if isinstance(data, str) else data
    reasons[p] = reason

def get(rel):
    p = B / rel
    return pending[p] if p in pending else p.read_bytes()

def cp(src, rel):
    p = B / rel
    data = src.read_bytes()
    if p.exists():
        assert p.read_bytes() == data, str(rel)
    else:
        if p in pending:
            assert pending[p] == data, str(rel)
        put(rel, data, 'Exact frozen source, actual output or review evidence.')
    mapping.append({'source': str(src.relative_to(R)), 'archive': str(rel), 'sha256': digest(data)})

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
    ('e121', 'research_e119_continuation', 'e_fiftythree_normalizer_manifest.json',
     'de04c68da8e09240a36074cd7dfb3d943d0759811cf6e842fe871b1e24625b1d',
     'E_fiftythree_normalizer.tex', 'E.121', 'e_fiftythree_normalizer'),
    ('d64', 'D64_EXPERIMENTS', 'd_compact_isometry_source_manifest.json',
     'f83f88aa73247f28783661a5823f2ad08fb4479302ce61cf4d184f741e1fb357',
     'D_compact_isometry_source.tex', 'D.64', 'd_compact_isometry_source'),
]
manifests = {tag: verify(R / folder, name, expected)
             for tag, folder, name, expected, *_ in spec}
audits = {
    'root_e121_audit': ('b17e76956f0a73fdc00b3ee39cdfcf423ac432076c277eceb11509ea1331a895', 'PASS_ROOT_FULL_PROOF_SOURCES_REPLAY_AND_TYPING_DELTA'),
    'd_e121_audit': ('98b8f53046da0db039c9017cd4f9f285f99f16aa295b5308ddf4fbf61cfc01a5', 'PASS_FULL_PROOF_SOURCE_AND_INDEPENDENT_MARKED_MAP_IDEAL_CHECKS'),
    'root_d64_audit': ('c41294f9282ec0b1cb07f51a72ec80ab212ce05ade6efd5a7da90251a5518a1b', 'PASS_ROOT_FULL_PROOF_SOURCES_AND_REPLAY'),
    'bc_d64_audit': ('e3c6a86f67f37bd8793d9824cb3ff3e09b96c4e4b1bed317a870319b0fe28552', 'PASS'),
}
for name, (expected, status) in audits.items():
    p = R / name / 'audit.json'
    d = read(p)
    assert sha(p) == expected and d.get('status', d.get('result')) == status, name

for name in ['assemble.py', 'assemble.out', 'build_pdf.py', 'build_pdf.out',
             'latex_pass1.out', 'latex_pass2.out', 'latex_pass3.out', 'bibtex.out',
             'build_certificate.json', 'pdf_qa.out', 'package.py', 'package.out']:
    p = B / 'code' / name
    if p.exists():
        cp(p, Path('code/checkpoint222_before224') / name)
cp(B / 'LM7_FERMAT_TOWER_paper.tex', Path('code/checkpoint222_before224/paper_master.tex.md'))
for p in sorted((B / 'qa').glob('*')):
    if p.is_file() and (p.name.startswith(('contact_', 'detail222_', 'visual222_'))
                       or p.name in ['pdf_qa.json', 'visual_review.md']):
        cp(p, Path('qa/history/checkpoint222_before224') / p.name)

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
    source_stdout = p.with_name(p.name[:-11] + '.out') if p.name.endswith('.source.txt') else p.with_suffix('.out')
    if out.suffix in {'.py', '.gp'} and not p.with_suffix('.out').exists() and not p.with_name(p.stem + '_gp.out').exists() and not source_stdout.exists():
        out = out.with_name(out.name + '.md')
    return out

for tag, folder_name, *_ in spec:
    folder = R / folder_name
    for p in sorted(folder.rglob('*')):
        if p.is_file():
            dest = mapped_owned(p, folder, tag)
            if dest is not None:
                cp(p, dest)
    for row in manifest_rows(manifests[tag]):
        p = folder / row.get('path', row.get('file'))
        dest = mapped_owned(p, folder, tag)
        assert dest is not None and digest(get(dest)) == row['sha256'], str(p)
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
    'E.121': 'E.121 evaluates the full next positional53 S-class groups A(B2)=C9+C3^3 and A(L2)=C9^2. Exact normalizer/trace nilpotence removes the B projection kernel, and the positive horizontal connecting class gives the L kernel <3u>. All actual ideal norms, extensions, capitulation groups, cyclic-nine and normal-closure Artin maps are computed. The three completed unit norm quotients are C3^6,C3,C3 and their kernels are C3+Z3^18,C3+Z3^6,C3+Z3^22, with actual Hilbert90 divisor maps and explicit choice-dependent product isomorphisms. This closes the E119 next-layer projection questions. Later positional norm systems and the unrestricted intrinsic section set remain active through E46 and the stated exact source comparisons.',
    'D.64': 'D.64 uses marked compact isometries and actual source-involution words to lift a further1930-dimensional central quotient with14 coinvariants, retaining both D57 branches, all16 framings, the full W_h maps and literal source conjugators. The lower homology action is T64=T63+A1m1+A4m4 with its exact crossed-homomorphism and cusp-inner comparison. Universal equivariant retractions retain eight additional compact coordinates. The final proof cancels the moving component after the new source words through the actual R50 intersection Lstar2 lifts. The exact residual J64 has specified dimension282230. Fourteen uncovered compact-test coordinates keep their test scope; the full residual arithmetic boundary and full profinite source realization remain active.',
}
review_notes = {
    'E.121': 'Root completed the full original proof and713-line mathematical-source review and five-stage copied-source arithmetic replay: all seven entire text outputs are byte-identical and all seven whole decoded PARI objects equal, with no exclusions. The original128-file freeze and root executions are preserved. The final264-file freeze adds two proof-only morphism clarifications; all computations remain unchanged. Root separately executed an independent exhaustive finite-map verifier. The independent peer read the entire573-line final proof and checked all rational genus maps,26244 normal-closure products,12 marked S-prime images,14 complete principal ideal identities and732 HNF columns using its own programs.',
    'D.64': 'Root completed the entire755-line amended proof and1248-line source review and six complete copied-source/input replays. All complete JSON/stdout files agree excluding only elapsed_seconds, and every execution returns0 with empty stderr. The complete original freeze and necessary post-word moving repair are retained with unchanged computational files. The independent peer read the full proof and separately reconstructed marked integral pairings, both branches, all548 retraction coefficients,576 source-basis wedges and the integral involution/full36-term cusp identities.',
}
for tag, folder, name, expected, section, ident, stem in spec:
    rel = Path('ledger') / (stem + '_results.json')
    before = get(rel)
    rows = json.loads(before)
    assert len(rows) == 1 and rows[0]['id'] == ident
    if isinstance(rows[0]['notes'], list):
        rows[0]['notes'] = ' '.join(rows[0]['notes'])
    rows[0]['notes'] += ' ' + details[ident] + ' ' + review_notes[ident]
    rows[0]['where_proved'] = rows[0]['where_proved'].replace('code/', f'code/{tag}_bundle/code/')
    if isinstance(rows[0]['manuscript_passages'], list):
        rows[0]['manuscript_passages'] = '; '.join(rows[0]['manuscript_passages'])
    after = enc(rows)
    put(rel, after, 'Record completed root/peer reviews and exact archive paths.')
    amendments.append({'file': str(rel), 'before_sha256': digest(before), 'after_sha256': digest(after.encode()), 'author_freeze': str(Path('code') / (tag + '_bundle/author_freeze/ledger') / rel.name)})
    rel = Path('ledger') / (stem + '_report.md')
    before = get(rel)
    after = before.decode() + '\n\n## Completed integration reviews\n\n' + review_notes[ident] + '\n\n## Integrated original-task scope\n\n' + details[ident] + '\n'
    put(rel, after, 'Append completed review and task scope; exact author report retained.')
    amendments.append({'file': str(rel), 'before_sha256': digest(before), 'after_sha256': digest(after.encode()), 'author_freeze': str(Path('code') / (tag + '_bundle/author_freeze/ledger') / rel.name)})

rel = Path('LM7_FERMAT_TOWER_paper.tex')
t = get(rel).decode()
for marker, addition in [(r'\input{sections/D_compact_orthogonal_cross.tex}', r'\input{sections/D_compact_isometry_source.tex}'),
                         (r'\input{sections/E_lower_fiftythree.tex}', r'\input{sections/E_fiftythree_normalizer.tex}')]:
    assert t.count(marker) == 1 and addition not in t
    t = t.replace(marker, marker + '\n' + addition)
put(rel, t, 'Register both fully audited proofs.')

rel = Path('sections/E.tex')
t = get(rel).decode()
a = t.index(r'\begin{statement}{E.23}')
z = t.index(r'\end{statement}', a)
new = r'''
E.121 evaluates the entire next positional-$53$ groups left
by E.119: $A(B_2)=C_9\oplus C_3^3$ and $A(L_2)=C_9^2$.
Its actual normalizer and trace argument proves
$(\sigma-1)A(B_2)=0$, while the positive connecting class
gives $(\sigma-1)A(L_2)=\langle3u\rangle$.
Every vertical and horizontal norm, extension and capitulation
map is evaluated, together with the cyclic-nine quotient and
the Artin character of the literal normal closure.
The three completed unit norm quotients are $C_3^6,C_3,C_3$;
the kernel types are $C_3\oplus\mathbb Z_3^{18}$,
$C_3\oplus\mathbb Z_3^6$ and
$C_3\oplus\mathbb Z_3^{22}$, through the stated actual
Hilbert90 maps and product isomorphisms with specified choices.
Thus the preceding E.119 upper-layer questions are settled
by E.121. Later positional norm systems, the remaining
intrinsic class-three and higher maps, and the unrestricted
section set remain active through their exact comparison maps.
'''
put(rel, t[:z] + new + t[z:], 'Record the full evaluated positional53 transition and its remaining scope.')

rel = Path('sections/D.tex')
t = get(rel).decode()
new = r'''
The successive residual descriptions above refer to their
numbered stages. D.64 extends the actual action through the
onto quotient $\Phi_{64}$ of $\mathcal J_{63}$ of dimension
$1930$, with fourteen coinvariants. Marked compact isometries
and actual source-involution words give
$T_{64}=T_{63}+A_1m_1+A_4m_4$ and its literal lower-action
comparison, retaining both D.57 branches, all sixteen framings,
the full $\mathcal W_h$ maps and source conjugators.
Its post-word moving correction uses the actual
$R_{50}\cap L_{*,2}$ source lifts before the final augmentation.
The exact remaining kernel $\mathcal J_{64}=\ker\Phi_{64}$
has specified dimension $282\,230$.
The fourteen uncovered compact-test coordinates retain
their test scope; the entire residual arithmetic boundary
and the full profinite source realization remain active.
'''
for ident in ['D.13', 'D.19']:
    a = t.index(r'\begin{statement}{' + ident + '}')
    z = t.index(r'\end{statement}', a)
    t = t[:z] + new + t[z:]
put(rel, t, 'Record the D64 source lift, exact retained maps and current residual.')

for name in ['d_results.json', 'd_coverage.json']:
    rel = Path('ledger') / name
    rows = json.loads(get(rel))
    for row in rows:
        if name == 'd_results.json' and row['id'] in ['D.13', 'D.19']:
            assert 'D.64' not in row['depends_on']
            row['depends_on'].append('D.64')
            row['notes'] += ' ' + details['D.64']
        if name == 'd_coverage.json' and row['task'] in ['D.e', 'D.afterLM2.1']:
            row['statement_ids'].append('D.64')
            row['outcome'] += ' ' + details['D.64']
            row['remaining_step'] = 'Evaluate the actual arithmetic boundary on J64, with specified residual dimension282230 and exact full-source inverse image, and then the remaining full profinite source realization. The14 uncovered compact-test coordinates have no asserted identification with the coinvariants of J64.'
    put(rel, enc(rows), 'Synchronize original D result and task rows.')

rel = Path('code/assemble.py')
t = get(rel).decode()
needle = '\ne_rows = []\n'
assert t.count(needle) == 1
t = t.replace(needle, "\ne_deps['E.23'].append('E.121')\ne_notes['E.23'] += " + repr(' ' + details['E.121']) + '\n' + needle)
needle = "(LEDGER/'e_coverage.json').write_text(json.dumps(e_coverage,ensure_ascii=False,indent=2)+'\\n')"
assert t.count(needle) == 1
block = ("for row in e_coverage:\n    if row['task'] in ('E.c','E.d','E.follow-up-4'):\n"
         "        row['statement_ids'].extend(x for x in ('E.121',) if x not in row['statement_ids'])\n"
         "    if row['task'] in ('E.d','E.follow-up-4'):\n        row['outcome'] += " + repr('; ' + details['E.121']) + '\n'
         "        row['remaining_step'] = " + repr('Evaluate the cubic intrinsic class-three and subsequent maps, later quartic quotients and remaining coefficient primes; later positional53 norm systems; and full intrinsic metabelian/marked source preimages. E121 has evaluated the entire positional53 level-two class and unit transition.') + '\n')
t = t.replace(needle, block + needle)
put(rel, t, 'Synchronize generated E23 and the33 original-task coverage rows.')

rel = Path('ledger/d_original_source_recheck.md')
put(rel, get(rel).decode() + '\n\n' + (R / 'root_pending222/source_recheck.md').read_text(),
    'Record additional actual requested-original source retrievals without changing verification labels.')

for p in list(pending):
    if p.suffix == '.gp' and p.with_suffix('.out') not in pending and not p.with_suffix('.out').exists():
        alt = p.with_name(p.stem + '_gp.out')
        assert alt in pending or alt.exists(), str(p)
        put(p.with_suffix('.out').relative_to(B), get(alt.relative_to(B)), 'Byte-identical alias of actual GP stdout.')
for p in pending:
    if p.suffix in {'.py', '.gp'}:
        assert p.with_suffix('.out') in pending or p.with_suffix('.out').exists(), str(p)

rel = Path('code/README.md')
put(rel, get(rel).decode() + '''

## E121 and D64

E121 is retained in code/e121_bundle with the complete128-file original
freeze,264-file final freeze, exact two-paragraph proof amendment, every
mathematical source, actual attempt and complete arithmetic output. Root
ran all five new GP stages and the exact checker from copied sources and
nine immutable E119 inputs. Seven complete text outputs agree byte for
byte; all seven whole decoded PARI objects agree, with no exclusions.
The raw serialized BIN bytes differ and their exact hashes are recorded.
The proof amendment changes no mathematical computation. The completed
kernel map and inverse, choice ambiguity and actual norm-lift rule are
explicit. Root's separate finite-map verifier imports no author code or
outputs. The independent peer checks full rational genus maps,26244
normal-closure products,12 marked primes,14 principal ideal identities,
732 actual HNF columns, seven units and all28 local characters. Its
interrupted direct-power attempt and earlier successful counter/guard
versions are preserved with their actual outputs and precise scopes.

D64 is retained in code/d64_bundle with the complete original freeze and
the necessary post-word moving-component repair. All25 original code,
input and output files remain unchanged. Root read the full755-line
proof and1248-line mathematical source, then freshly ran all six complete
programs on their exact inputs. Complete JSON and stdout match after
excluding only elapsed_seconds. The separate peer reconstructs marked
integral pairings, all branches/framings, isometries,548 full retraction
coefficients,576 source-basis wedges and full36-term cusp identities.

Exact author ledgers remain in each bundle's author_freeze/ledger.
The active ledgers add the completed reviews and original-task scope.
Every frozen-to-archive mapping points to bytes with its stated hash;
active editorial amendments are recorded separately. All original
D13,D19,E23 questions and the three D.a original-source access gaps remain
active. The integrated paper has its own subsequent visual review.
''', 'Document complete evidence, exact changes and ongoing original-task scope.')

# Map every frozen row to an exact archive copy, including amended ledgers.
for item in mapping:
    if digest(get(Path(item['archive']))) != item['sha256']:
        amendment = next(a for a in amendments if a['file'] == item['archive'])
        assert amendment['before_sha256'] == item['sha256']
        item['active_editorial_path'] = item['archive']
        item['archive'] = amendment['author_freeze']
    assert digest(get(Path(item['archive']))) == item['sha256'], item
put(Path('ledger/checkpoint224_amendments.json'), enc({'status': 'PASS', 'amendments': amendments}),
    'Record exact active-ledger amendments and unchanged frozen copies.')

for tag, folder, name, expected, *_ in spec:
    verify(R / folder, name, expected)
changes = []
for p, data in pending.items():
    old = sha(p) if p.exists() else None
    if p.exists() and p.read_bytes() != data:
        if p.parent == B / 'sections':
            h = B / 'sections/history/checkpoint222_before224' / p.name
            h.parent.mkdir(parents=True, exist_ok=True)
            assert not h.exists()
            shutil.copy2(p, h)
        elif p.parent == B / 'ledger':
            h = B / 'code/checkpoint222_before224/ledger' / p.name
            if h.suffix == '.bib':
                h = h.with_name(h.name + '.md')
            h.parent.mkdir(parents=True, exist_ok=True)
            assert not h.exists()
            shutil.copy2(p, h)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data)
    changes.append({'path': str(p.relative_to(B)), 'before_sha256': old,
                    'after_sha256': sha(p), 'reason': reasons[p]})
record = {'status': 'PASS', 'added_statements': [x[5] for x in spec],
          'expected_statement_count': 224, 'original_task_rows': 33,
          'original_open_statements': ['D.13', 'D.19', 'E.23'],
          'frozen_to_archive_mapping': mapping, 'changes': changes,
          'active_ledger_amendments': amendments,
          'build_status': 'Assembly, full LuaLaTeX build and actual integrated visual review follow.'}
(B / 'ledger/checkpoint224_integration.json').write_text(enc(record))
print(enc({'status': 'PASS', 'added_statements': record['added_statements'],
           'expected_statement_count': 224, 'mapped_frozen_files': len(mapping),
           'written_files': len(changes), 'original_task_rows': 33,
           'all_frozen_mappings_match_actual_archive_bytes': True}), end='')
