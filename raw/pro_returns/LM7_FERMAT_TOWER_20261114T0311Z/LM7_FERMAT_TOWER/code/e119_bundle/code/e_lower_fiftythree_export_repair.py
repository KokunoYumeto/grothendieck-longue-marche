#!/usr/bin/env python3
"""Preserve frozen E119 and repair only exact ambient-map serialization.

This rechecks the changed Python certificate from unchanged GP records.
It does not repeat any number-field or BNF computation.
"""
from pathlib import Path
import hashlib, json, shutil, subprocess, sys
import sympy as S

ROOT = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest = ROOT / 'ledger/e_lower_fiftythree_manifest.json'
old = json.loads(manifest.read_text())
assert sha(manifest) == '79d424d7f19195b64260847b54544206615d0ed4c3f1011e8f88dc4392d6831d'
assert sha(ROOT / 'sections/E_lower_fiftythree.tex') == '25d9250dabab99ca3848525d608ed6968323cdc58400f75b8d074a90d79759c0'
for rel, v in old['files'].items():
    assert sha(ROOT / rel) == v['sha256'], rel
snap = ROOT.parent / 'research_e119_pre_rational_export'
assert not snap.exists()
shutil.copytree(ROOT, snap, ignore=shutil.ignore_patterns(
    '__pycache__', 'e_lower_fiftythree_export_repair.py',
    'e_lower_fiftythree_export_repair.out'))
archive = ROOT / 'audit/pre_rational_export/full_tree'
archive.parent.mkdir(parents=True)
shutil.move(snap, archive)
main = ROOT / 'code/e_lower_fiftythree.py'
src = main.read_text()
olddef = 'def ints(m):return [[int(v) for v in m.row(i)] for i in range(m.rows)]'
newdef = """def ints(m):
    assert all(S.denom(v)==1 for v in m), 'nonintegral matrix passed to integer serializer'
    encoded=[[int(v) for v in m.row(i)] for i in range(m.rows)]
    assert S.Matrix(encoded)==m
    return encoded

def rationals(m):
    encoded=[[str(S.Rational(v)) for v in m.row(i)] for i in range(m.rows)]
    decoded=S.Matrix([[S.Rational(v) for v in row] for row in encoded])
    assert decoded==m, 'rational matrix export failed exact round trip'
    return encoded"""
assert src.count(olddef) == 1
src = src.replace(olddef, newdef)
oldforward = "'kernel_lattice':ints(K),'forward':ints(KU*K.inv()),"
newforward = "'kernel_lattice':ints(K),'forward':rationals(KU*K.inv()),"
assert src.count(oldforward) == 1
main.write_text(src.replace(oldforward, newforward))
run = subprocess.run([sys.executable, str(main)], cwd=ROOT / 'code',
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
(ROOT / 'code/e_lower_fiftythree.out').write_bytes(run.stdout)
assert run.returncode == 0, (run.returncode, run.stdout.decode()[-3000:])
new = json.loads((ROOT / 'code/e_lower_fiftythree.json').read_text())
previous = json.loads((archive / 'code/e_lower_fiftythree.json').read_text())
changed = []
for key in ['B2_genus', 'L2_genus']:
    rows = new[key]['forward']
    M = S.Matrix([[S.Rational(v) for v in row] for row in rows])
    I = S.Matrix(new[key]['inverse'])
    assert M * I == I * M == S.eye(M.rows)
    entries = []
    for i in range(M.rows):
        for j in range(M.cols):
            if S.denom(M[i, j]) != 1:
                entries.append({'row_zero_based': i, 'column_zero_based': j,
                                'exact': str(M[i, j]),
                                'old_integer': previous[key]['forward'][i][j]})
            else:
                assert int(M[i, j]) == previous[key]['forward'][i][j]
    assert len(entries) == (8 if key == 'B2_genus' else 4)
    changed.append({'key': key + '.forward', 'exact_rational_entries': entries,
                    'full_ambient_inverse_verified': True})
    previous[key]['forward'] = rows
assert new == previous, 'Additional certificate-field changes are forbidden'

# Fresh checker-only replay from the literal unchanged GP stdout and sources.
fresh = ROOT / 'audit/rational_export_replay/fresh'
for sub in ['code', 'inputs']:
    (fresh / sub).mkdir(parents=True)
needed = [Path('code/e_lower_fiftythree.py')]
needed += [Path(rel) for rel in old['files']
           if (rel.startswith('code/') or rel.startswith('inputs/'))
           and '/' not in rel.split('/', 1)[1]
           and rel.endswith(('.gp', '.out'))
           and not rel.startswith('code/e_lower_fiftythree')]
for rel in needed:
    shutil.copy2(ROOT / rel, fresh / rel)
replay = subprocess.run([sys.executable, str(fresh / 'code/e_lower_fiftythree.py')],
                        cwd=fresh / 'code', stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
(fresh / 'code/e_lower_fiftythree.out').write_bytes(replay.stdout)
assert replay.returncode == 0, (replay.returncode, replay.stdout.decode()[-3000:])
assert replay.stdout == run.stdout
assert ((fresh / 'code/e_lower_fiftythree.json').read_bytes()
        == (ROOT / 'code/e_lower_fiftythree.json').read_bytes())

# Every arithmetic source, output and full serialized object stays byte fixed.
arithmetic = []
for rel, v in old['files'].items():
    if ((rel.startswith('code/') or rel.startswith('inputs/'))
            and '/' not in rel.split('/', 1)[1]
            and rel.endswith(('.gp', '.out', '.bin'))
            and not rel.startswith('code/e_lower_fiftythree')):
        assert sha(ROOT / rel) == v['sha256'], rel
        arithmetic.append({'path': rel, 'sha256': v['sha256']})
info = {
    'statement': 'E.119', 'status': 'PASS',
    'scope': 'Exact JSON serialization amendment and fresh checker-only replay; no new GP/BNF computation.',
    'preserved_complete_frozen_tree': 'audit/pre_rational_export/full_tree',
    'old_manifest_sha256': sha(archive / 'ledger/e_lower_fiftythree_manifest.json'),
    'old_main_sha256': sha(archive / 'code/e_lower_fiftythree.py'),
    'new_main_sha256': sha(main),
    'old_JSON_sha256': sha(archive / 'code/e_lower_fiftythree.json'),
    'new_JSON_sha256': sha(ROOT / 'code/e_lower_fiftythree.json'),
    'unchanged_proof_sha256': sha(ROOT / 'sections/E_lower_fiftythree.tex'),
    'changed_fields': changed,
    'all_other_JSON_fields_identical': True,
    'integer_serializer': 'Every call asserts denominator1 and exact decode equality.',
    'rational_serializer': 'Canonical rational strings, decoded entrywise with exact Rational equality.',
    'fresh_checker_replay': {
        'exit_code': replay.returncode,
        'stdout_byte_identical': True, 'JSON_byte_identical': True,
        'source_and_cached_records': len(needed)},
    'unchanged_arithmetic_files': arithmetic,
    'excluded_fields': []}
text = json.dumps(info, indent=2) + '\n'
(ROOT / 'ledger/e_lower_fiftythree_rational_export_amendment.json').write_text(text)
print(text, end='')
