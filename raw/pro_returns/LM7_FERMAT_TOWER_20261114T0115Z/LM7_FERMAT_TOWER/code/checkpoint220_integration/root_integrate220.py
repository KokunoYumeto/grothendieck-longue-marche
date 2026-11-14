#!/usr/bin/env python3
"""Integrate the fully audited E117 and D62 results, preserving exact evidence."""
from pathlib import Path
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
assert not (B / 'ledger/checkpoint220_integration.json').exists()

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

def verify(folder, name, expected):
    p = folder / 'ledger' / name
    assert sha(p) == expected, str(p)
    m = read(p)
    rows = m['files']
    if isinstance(rows, dict):
        rows = [dict(path=k, **v) for k, v in rows.items()]
    for row in rows + m.get('immutable_inputs', []):
        q = folder / row.get('path', row.get('file'))
        assert sha(q) == row['sha256'], str(q)
        if 'bytes' in row:
            assert q.stat().st_size == row['bytes'], str(q)
    return m

spec = [
    ('e117', 'research_e117', 'e_quartic_three_manifest.json',
     '73e6772cd5c31a6e609d42e80903c2f16ed5388124c8e7b760ff4af0e293287b',
     'E_quartic_three.tex', 'E.117', 'e_quartic_three'),
    ('d62', 'D62_EXPERIMENTS', 'd_self_wedge_actual_corrections_manifest.json',
     '66a05d0534733dc7f6002488f20b45644fefe10c6adae1ad4168497d0ad3c68c',
     'D_self_wedge_actual_corrections.tex', 'D.62', 'd_self_wedge_actual_corrections')]
for tag, folder, name, expected, *_ in spec:
    verify(R / folder, name, expected)
audits = {
    'root_e117_audit': ('f92d30ce69cd61895db7c40e752305f7123446dac94d90e40b8b79105972c8a8', 'PASS'),
    'bc_e117_focus': ('e9b3ecc7131dc7a23094583a24fe4f8cacfc083fa89665ca275df73afb3b7d7b', 'PASS_FOCUSED_PROOF'),
    'root_d62_audit': ('8fab8cd8a0f45c0d48757018c8c42ab7d1ad2bb7992052271e77daf55bdbad3b', 'PASS'),
    'a_d62_audit': ('ead83a2fb43dd33af546a7f3406c19b7073665623f326da82474840512ef09e0', 'PASS_FULL_PROOF_AND_SOURCES_WITH_INDEPENDENT_MAP_EXECUTION')}
for name, (expected, status) in audits.items():
    p = R / name / 'audit.json'
    assert sha(p) == expected and read(p)['status'] == status, name

# Preserve the last actual complete build, assembly, visual and package records.
for name in ['assemble.py', 'assemble.out', 'build_pdf.py', 'build_pdf.out',
             'latex_pass1.out', 'latex_pass2.out', 'latex_pass3.out', 'bibtex.out',
             'build_certificate.json', 'pdf_qa.out', 'package.py', 'package.out']:
    p = B / 'code' / name
    if p.exists():
        cp(p, Path('code/checkpoint218_before220') / name)
cp(B / 'LM7_FERMAT_TOWER_paper.tex', Path('code/checkpoint218_before220/paper_master.tex.md'))
for p in sorted((B / 'qa').glob('*')):
    if p.is_file() and (p.name.startswith(('contact_', 'detail218_', 'visual218_'))
                       or p.name in ['pdf_qa.json', 'visual_review.md']):
        cp(p, Path('qa/history/checkpoint218_before220') / p.name)

excluded = {'sources', 'source_images', 'primary_sources', 'vendor', '__pycache__'}
allowed = {'.py', '.gp', '.cpp', '.json', '.csv', '.out', '.err', '.md', '.npz',
           '.npy', '.bin', '.tex', '.bib', '.jpg', '.txt', '.patch', '.diff'}

def mapped_owned(p, folder, tag):
    rel = p.relative_to(folder)
    if any(x in excluded for x in rel.parts) or p.suffix not in allowed:
        return None
    if rel.parts[0] == 'sections':
        return rel
    if rel.parts[0] == 'ledger':
        if p.name.endswith('_coverage.json') and isinstance(read(p), dict):
            return Path('ledger') / (tag + '_staging') / p.name
        return rel
    if rel.parts[0] == 'qa' and p.suffix in {'.jpg', '.json', '.md'}:
        return Path('qa') / (tag + '_author') / Path(*rel.parts[1:])
    out = Path('code') / (tag + '_bundle') / rel
    if p.suffix in {'.tex', '.bib', '.patch', '.diff'}:
        out = out.with_name(out.name + '.md')
    elif p.name.endswith('.source.txt'):
        out = out.with_name(out.name[:-11] + '.py')
    elif p.suffix == '.txt':
        out = out.with_name(out.name + '.md')
    if out.suffix in {'.py', '.gp'} and not p.with_suffix('.out').exists() and not p.with_name(p.stem + '_gp.out').exists():
        out = out.with_name(out.name + '.md')
    return out

for tag, folder, *_ in spec:
    folder = R / folder
    for p in sorted(folder.rglob('*')):
        if p.is_file():
            dest = mapped_owned(p, folder, tag)
            if dest is not None:
                cp(p, dest)
    # Active result/report/peer ledgers will receive root's integration record.
    # Keep the exact author versions as independently hashable archive members.
    for p in sorted((folder / 'ledger').glob('*')):
        if p.is_file() and (p.name.endswith(('_results.json', '_report.md', '_peer.json'))):
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
    for f in ['audit.json', 'audit.md', 'verification.json']:
        p = folder / f
        if p.exists():
            cp(p, Path('ledger') / (name + '_' + f))
for p in sorted((R / 'root_integrate220_history').rglob('*')):
    if p.is_file():
        cp(p, Path('code/checkpoint220_integration/history') / p.relative_to(R / 'root_integrate220_history'))

details = {
    'E.117': 'E.117 evaluates the actual integral and rational three-primary quartic class-two image and every fibre. The finite-S section coordinates are Z3^13 x (Z3^78 plus C3^10). The unrestricted image retains all 55 peripheral cups and the actual mixed correction, with its unclosed support denominator, exact divisibility and decay conditions. The central fibres have free rank 66, ten C3 factors and the stated twelve restricted Tate/CM factors. Actual division fields, integral action comparisons, source pullback maps and Chebotarev fields are proved. Original E.23 beyond this exact class-two coefficient stage remains active.',
    'D.62': 'D.62 uses actual source-involution and infinite-cusp words to cancel all 26 projective self-wedge classes left by D.61. The exact cusp wrap t^36 is retained and its extra commutator is killed by the displayed cusp-annihilating projector. The Y action is Int(b_t,Y) alpha61,Y, its homology is T61, and the literal D.57 and W_h maps are retained. The lift adds 6656 central coordinates and 28 coinvariants. The specified residual is 325120-dimensional with 534 coinvariants; its actual boundary and full profinite source realization remain active.'}
for tag, folder, name, expected, section, ident, stem in spec:
    rel = Path('ledger') / (stem + '_results.json')
    rows = json.loads(get(rel))
    assert len(rows) == 1 and rows[0]['id'] == ident
    rows[0]['notes'] += ' ' + details[ident]
    rows[0]['where_proved'] = rows[0]['where_proved'].replace('code/', f'code/{tag}_bundle/code/').replace('audit/d62_author_rebuild/', 'code/d62_bundle/audit/d62_author_rebuild/')
    if ident == 'E.117':
        rows[0]['manuscript_passages'] = 'Section 51.16; folios 733v--736v; scans 172--178; equations 371--379; Part E(c),(d), follow-up 4'
        rows[0]['notes'] += ' Complete root proof/source audit and full copied arithmetic replay PASS; five whole text/source files are byte-identical with no exclusions, and the entire decoded PARI object is equal. The independent BC proof review has its explicitly limited scope.'
    else:
        rows[0]['notes'] = rows[0]['notes'].replace('Root/peer audit pending.', 'Complete root proof/source audit and four-stage copied replay PASS. Complete JSON/stdout comparisons exclude only elapsed_seconds. Independent peer proof review and separately written dense Hermitian/F2 and integral Magnus checks PASS with their exact retained scope.')
    put(rel, enc(rows), 'Record completed review scope, exact archive paths and original-task state.')
    rel = Path('ledger') / (stem + '_report.md')
    before = get(rel).decode()
    after = before
    if ident == 'E.117':
        old = "Root's complete proof and independent replay review is pending at this author freeze."
        assert after.count(old) == 1
        after = after.replace(old, "The exact author-freeze report is preserved under code/e117_bundle/author_freeze. Root has now completed the entire proof/source audit and copied-source replay, with PASS; its full records are attached. The focused BC audit retains its stated scope.")
    else:
        after += '\n\nThe complete root audit and fresh four-stage copied-source replay have now passed. The separate independent peer proof review and its independently written dense Hermitian/F2 and integral Magnus program have also passed. Their complete records retain the exact source, output and comparison scopes.\n'
    after += '\n## Integrated original-task scope\n\n' + details[ident] + '\n'
    put(rel, after, 'Integrate completed root/peer review without changing historical author records.')
    amendments.append({'file': str(rel), 'before_sha256': digest(before.encode()), 'after_sha256': digest(after.encode()), 'kind': 'Completed review and current task state'})

rel = Path('ledger/e_quartic_three_peer.json')
peer = json.loads(get(rel))
peer['author_freeze_status'] = peer['status']
peer['status'] = 'PASS_FOCUSED_PROOF; complete root proof/source/replay audit PASS'
peer['root_audit'] = {'path': 'code/root_e117_audit/audit.json', 'sha256': audits['root_e117_audit'][0], 'scope': 'Entire frozen proof, source/dependency ledgers, fresh copied arithmetic replay, complete text comparisons and full decoded binary equality; see the exact audit.'}
put(rel, enc(peer), 'Add completed root review while retaining the exact independent peer scope.')

rel = Path('LM7_FERMAT_TOWER_paper.tex')
t = get(rel).decode()
for marker, addition in [(r'\input{sections/D_remaining_projective_rows.tex}', r'\input{sections/D_self_wedge_actual_corrections.tex}'),
                         (r'\input{sections/E_inert_lower_factors.tex}', r'\input{sections/E_quartic_three.tex}')]:
    assert t.count(marker) == 1 and addition not in t
    t = t.replace(marker, marker + '\n' + addition)
put(rel, t, 'Register the two fully audited proof sections.')

rel = Path('sections/E.tex')
t = get(rel).decode()
a = t.index(r'\begin{statement}{E.23}')
z = t.index(r'\end{statement}', a)
new = r'''
E.117 completes the integral and rational three-primary quartic
class-two image and every fibre. Its exact finite-$S$ coordinates
are $\mathbb Z_3^{13}\times(\mathbb Z_3^{78}\oplus(\mathbb Z/3)^{10})$.
The unrestricted image is evaluated by all fifty-five peripheral
cups and the actual restricted mixed correction, retaining its
support denominator, integral inverse and decay conditions.
The complete global central fibre has free rank $66$, ten
order-three factors and the twelve displayed restricted Tate/CM
factors. The integral Johnson comparison, full arithmetic-source
pullback and unbounded local Kummer orders are proved in that
statement. The cubic intrinsic class-three map, later quartic
quotients, remaining coefficient primes, lower positional norm
factors and full metabelian/marked source preimages remain active.
'''
put(rel, t[:z] + new + t[z:], 'Update E23 with the evaluated three-primary stage and exact remaining targets.')

rel = Path('sections/E_quartic_five_cohomology.tex')
before = get(rel).decode()
old = 'groups; the mixed obstruction deciding the image of the full\nquartic abelian section space is retained in E.23.'
new = 'groups. E.115 evaluates the mixed obstruction deciding the image\nof the full quartic abelian section space with these coefficients.'
assert before.count(old) == 1
after = before.replace(old, new)
put(rel, after, 'Replace an obsolete forward status by the exact later E115 result.')
amendments.append({'file': str(rel), 'before_sha256': digest(before.encode()), 'after_sha256': digest(after.encode()), 'kind': 'Update forward status; no formula or fibre coordinate changed'})

rel = Path('sections/D.tex')
t = get(rel).decode()
old = 'The four actual involution-cover divided norms still leave\ntwenty-six named self-wedge classes; their arithmetic boundary\nand the full profinite source realization remain active.'
assert t.count(old) == 2
t = t.replace(old, 'At the D.61 stage the four actual involution-cover divided norms\nleave twenty-six named self-wedge classes. D.62 evaluates their\narithmetic correction by the actual source words below.')
new = r'''
D.62 cancels all twenty-six projective self-wedge classes by
actual source-involution and infinite-cusp correcting words.
The full cusp wrap is retained; its extra commutator is killed
by the specified projector. The literal comparison on $Y$ is
$\operatorname{Int}(b_{t,Y})\alpha_{61,Y}$, with unchanged
homology $T_{61}$ and retained D.57 and $\mathcal W_h$ maps.
The new lift retains $6656$ further central coordinates and
twenty-eight coinvariants. Its specified residual has dimension
$325\,120$ and $534$ coinvariants. The arithmetic boundary on
this residual and the full profinite source realization remain
the active original questions.
'''
for ident in ['D.13', 'D.19']:
    a = t.index(r'\begin{statement}{' + ident + '}')
    z = t.index(r'\end{statement}', a)
    t = t[:z] + new + t[z:]
put(rel, t, 'Record the actual D62 source-word lift and precise remaining boundary.')

for name in ['d_results.json', 'd_coverage.json']:
    rel = Path('ledger') / name
    rows = json.loads(get(rel))
    for row in rows:
        if name == 'd_results.json' and row['id'] in ['D.13', 'D.19']:
            row['depends_on'].append('D.62')
            row['notes'] += ' ' + details['D.62']
        if name == 'd_coverage.json' and row['task'] in ['D.e', 'D.afterLM2.1']:
            row['statement_ids'].append('D.62')
            row['outcome'] += ' ' + details['D.62']
            row['remaining_step'] = 'Evaluate the actual residual J62 arithmetic boundary on the specified 325120-dimensional module with 534 coinvariants, then the remaining full profinite source realization.'
    put(rel, enc(rows), 'Synchronize the original D result rows and task inventory.')

rel = Path('code/assemble.py')
t = get(rel).decode()
needle = '\ne_rows = []\n'
assert t.count(needle) == 1
t = t.replace(needle, "\ne_deps['E.23'].append('E.117')\ne_notes['E.23'] += " + repr(' ' + details['E.117']) + '\n' + needle)
needle = "(LEDGER/'e_coverage.json').write_text(json.dumps(e_coverage,ensure_ascii=False,indent=2)+'\\n')"
assert t.count(needle) == 1
block = ("for row in e_coverage:\n    if row['task'] in ('E.c','E.d','E.follow-up-4'):\n"
         "        row['statement_ids'].extend(x for x in ('E.117',) if x not in row['statement_ids'])\n"
         "    if row['task'] in ('E.d','E.follow-up-4'):\n        row['outcome'] += " + repr('; ' + details['E.117']) + '\n'
         "        row['remaining_step'] = " + repr('Evaluate the cubic intrinsic class-three map, later quartic quotients and remaining coefficient primes, lower positional norm factors, and full intrinsic metabelian/marked source preimages.') + '\n')
t = t.replace(needle, block + needle)
put(rel, t, 'Synchronize the generated E result and original task coverage rows.')

rel = Path('ledger/d_original_source_recheck.md')
t = get(rel).decode()
t += '\n## Subsequent exact-title public-source passes\n\nRetrieval family turn1021 used the exact Coleman1989 title and DOI, and the Ihara RIMS Part I identifiers. It returned the previously reached CiNii/NDL metadata and separate later sources. Retrieval family turn1022 excluded previously exhausted hosts and returned the author bibliography, the later Tilouine exposition, Hain--Matsumoto2003, and other citing papers. A separate Coleman1986 torsion paper and a later Yoshida paper have different titles and were not substituted for the requested originals. No requested Ihara1986, Coleman1989 or Ihara1999 Part I original proof became readable. Their original-source labels remain unchanged.\n'
put(rel, t, 'Record the actual unsuccessful original-source searches without upgrading their status.')

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
t += '\n\n## E117 and D62\n\nE117 retains both arithmetic programs, all three exact inputs and every actual failure/replay record in code/e117_bundle. The full arithmetic reconstruction accepts --gp /absolute/path/to/gp. Root executed fresh copied sources and inputs: five complete source/text files agree byte for byte, with no excluded fields; the entire deserialized PARI GEN including both complete BNF objects agrees. Raw binary differences and the exact decoding comparison are retained.\n\nD62 retains its four-stage computations and immutable inputs in code/d62_bundle. Root executed each stage in a separate copied directory. Whole JSON and stdout agree after excluding only elapsed_seconds, with empty stderr and unchanged source/input hashes. The independent peer program in code/a_d62_audit uses separate dense Hermitian/F2 and integral Magnus implementations and retains its complete actual results.\n\nThe original author result/report/peer ledgers remain byte-exact under each bundle\'s author_freeze/ledger. Active ledgers additionally record the completed root audits. All proof, source reading, fresh execution and visual scopes are specified in the attached records. The E117 focused peer review does not claim a full support audit or a fresh arithmetic execution. The original D.13, D.19 and E.23 questions remain active.\n'
put(rel, t, 'Document exact reconstruction and independent audit scopes.')
put(Path('ledger/checkpoint220_amendments.json'), enc({'status': 'PASS', 'amendments': amendments}), 'Record exact editorial and completed-review changes.')

changes = []
for p, data in pending.items():
    old = sha(p) if p.exists() else None
    if p.exists() and p.read_bytes() != data:
        if p.parent == B / 'sections':
            h = B / 'sections/history/checkpoint218_before220' / p.name
            h.parent.mkdir(parents=True, exist_ok=True)
            assert not h.exists()
            shutil.copy2(p, h)
        elif p.parent == B / 'ledger':
            h = B / 'code/checkpoint218_before220/ledger' / p.name
            if h.suffix == '.bib':
                h = h.with_name(h.name + '.md')
            h.parent.mkdir(parents=True, exist_ok=True)
            assert not h.exists()
            shutil.copy2(p, h)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data)
    changes.append({'path': str(p.relative_to(B)), 'before_sha256': old, 'after_sha256': sha(p), 'reason': reasons[p]})
record = {'status': 'PASS', 'added_statements': [x[5] for x in spec], 'expected_statement_count': 220,
          'original_task_rows': 33, 'original_open_statements': ['D.13', 'D.19', 'E.23'],
          'frozen_to_archive_mapping': mapping, 'changes': changes,
          'build_status': 'Assembly and subsequent complete LuaLaTeX build and actual visual review follow.'}
(B / 'ledger/checkpoint220_integration.json').write_text(enc(record))
print(enc({'status': 'PASS', 'added_statements': record['added_statements'], 'expected_statement_count': 220,
           'changed_files': len(changes), 'preserved_mappings': len(mapping), 'amendments': len(amendments)}))
