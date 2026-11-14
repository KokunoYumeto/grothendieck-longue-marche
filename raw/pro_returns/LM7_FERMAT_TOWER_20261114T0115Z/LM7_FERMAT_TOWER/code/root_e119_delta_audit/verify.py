#!/usr/bin/env python3
"""Audit the exact export amendment and rerun its checker on root-generated data."""
from pathlib import Path
from fractions import Fraction
import copy
import difflib
import hashlib
import json
import shutil
import subprocess
import sys
import sympy as S

here = Path(__file__).resolve().parent
root = here.parent
author = root / 'research_e119'
oldroot = root / 'root_e119_audit'
preserved = author / 'audit/pre_rational_export/full_tree'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read = lambda p: json.loads(p.read_text())
encode = lambda x: json.dumps(x, indent=2) + '\n'

mp = author / 'ledger/e_lower_fiftythree_manifest.json'
assert sha(mp) == '67657642ad1f77f73b23a0147b82f717eedb5e9c1165bba0fad5e39a16d082e1'
manifest = read(mp)
assert len(manifest['files']) == 415
for name, value in manifest['files'].items():
    p = author / name
    assert sha(p) == value['sha256'] and p.stat().st_size == value['bytes'], name
oldmp = preserved / 'ledger/e_lower_fiftythree_manifest.json'
assert sha(oldmp) == '79d424d7f19195b64260847b54544206615d0ed4c3f1011e8f88dc4392d6831d'
oldmanifest = read(oldmp)
for name, value in oldmanifest['files'].items():
    p = preserved / name
    assert sha(p) == value['sha256'] and p.stat().st_size == value['bytes'], name
proof = author / 'sections/E_lower_fiftythree.tex'
assert sha(proof) == '25d9250dabab99ca3848525d608ed6968323cdc58400f75b8d074a90d79759c0'
assert proof.read_bytes() == (preserved / 'sections/E_lower_fiftythree.tex').read_bytes()
rp = oldroot / 'replay.json'
assert sha(rp) == 'eaf49401274fb5ff58303ec72522076953ce98a61d3eda62e0a6ad8098bd07fe'
replay = read(rp)
assert replay['status'] == 'PASS_ROOT_FROZEN_SOURCE_REPLAY'
assert replay['GP_stages'] == 10 and replay['main_exit_code'] == 0
assert replay['excluded_fields'] == replay['excluded_binary_components'] == []

source = author / 'code/e_lower_fiftythree.py'
assert sha(source) == '2ed1ecc3da4b09a6b731337da15615d30157aee7e40697d2a7b1058807656fff'
original_source = oldroot / 'fresh/code/e_lower_fiftythree.py'
assert sha(original_source) == replay['source_sha256']['code/e_lower_fiftythree.py']
source_diff = ''.join(difflib.unified_diff(original_source.read_text().splitlines(True),
                                       source.read_text().splitlines(True),
                                       fromfile='root_original_replayed_source',
                                       tofile='corrected_frozen_author_source'))
(here / 'source_amendment.diff.md').write_text(source_diff)

fresh = here / 'fresh'
assert not fresh.exists()
(fresh / 'code').mkdir(parents=True)
(fresh / 'inputs').mkdir()
shutil.copy2(source, fresh / 'code/e_lower_fiftythree.py')
gp_sources = []
gp_outputs = []
for name, value in replay['source_sha256'].items():
    if not name.endswith('.gp'):
        continue
    assert sha(author / name) == sha(oldroot / 'fresh' / name) == value, name
    shutil.copy2(author / name, fresh / name)
    gp_sources.append({'path': name, 'sha256': value})
for name, value in replay['text_outputs'].items():
    if name in ['code/e_lower_fiftythree.out', 'code/e_lower_fiftythree.json']:
        continue
    assert name.endswith('.out')
    assert sha(author / name) == sha(oldroot / 'fresh' / name) == value['sha256'], name
    shutil.copy2(oldroot / 'fresh' / name, fresh / name)
    gp_outputs.append({'path': name, 'sha256': value['sha256'], 'source': 'root original ten-stage arithmetic reconstruction'})
assert len(gp_sources) == len(gp_outputs) == 10
binary_records = []
for name, value in replay['binary_objects'].items():
    assert value['complete_decoded_GEN_identical']
    assert sha(author / name) == value['author_sha256'], name
    assert sha(oldroot / 'fresh' / name) == value['replay_sha256'], name
    binary_records.append({'path': name, 'current_author_sha256': sha(author / name),
                           'original_root_sha256': sha(oldroot / 'fresh' / name),
                           'previous_complete_decoded_equality_preserved_by_unchanged_bytes': True})
assert len(binary_records) == 12

cmd = [sys.executable, str(fresh / 'code/e_lower_fiftythree.py')]
run = subprocess.run(cmd, cwd=fresh, capture_output=True)
(fresh / 'code/e_lower_fiftythree.out').write_bytes(run.stdout)
(fresh / 'code/e_lower_fiftythree.err').write_bytes(run.stderr)
assert run.returncode == 0 and not run.stderr, (run.returncode, run.stderr.decode())
assert run.stdout == (author / 'code/e_lower_fiftythree.out').read_bytes()
assert (fresh / 'code/e_lower_fiftythree.json').read_bytes() == (author / 'code/e_lower_fiftythree.json').read_bytes()
assert sha(author / 'code/e_lower_fiftythree.json') == '53848b5a42a6b7a0968e355e4f9f042071599e4e087bcb391cd0ad3fa0703d8a'
assert sha(fresh / 'code/e_lower_fiftythree.py') == sha(source)
for item in gp_sources + gp_outputs:
    assert sha(fresh / item['path']) == item['sha256'], item['path']

before = read(oldroot / 'fresh/code/e_lower_fiftythree.json')
after = read(fresh / 'code/e_lower_fiftythree.json')
adjusted = copy.deepcopy(before)
cases = []
for key, stem, typename, expected_count in [
        ('B2_genus', 'e53_genus_transition', 'next_genus_presentation', 8),
        ('L2_genus', 'e53_positional_genus_transition', 'positional_genus_transition', 4)]:
    rows = [json.loads(x) for x in (fresh / 'code' / (stem + '.out')).read_text().splitlines() if x.startswith('{')]
    row = next(x for x in rows if x['type'] == typename)
    K = S.Matrix(row['kernel_lattice'])
    U = S.Matrix(row['kernel_smith_left'])
    D = S.Matrix(row['kernel_smith_diagonal'])
    encoded = after[key]['forward']
    assert all(isinstance(v, str) for line in encoded for v in line)
    fractions = [[Fraction(v) for v in line] for line in encoded]
    decoded = S.Matrix([[S.Rational(v.numerator, v.denominator) for v in line] for line in fractions])
    inverse = S.Matrix(after[key]['inverse'])
    assert decoded * K == U
    assert K * U.inv() == inverse
    assert decoded * inverse == inverse * decoded == S.eye(K.rows)
    differences = []
    for i in range(K.rows):
        for j in range(K.cols):
            v = decoded[i,j]
            old = before[key]['forward'][i][j]
            if v != old:
                assert S.denom(v) == 3 and D[i,i] == 1
                differences.append({'row': i, 'column': j, 'before': old,
                                    'after': str(v), 'Smith_modulus': int(D[i,i])})
            elif D[i,i] != 1:
                assert S.denom(v) == 1
    assert len(differences) == expected_count
    adjusted[key]['forward'] = after[key]['forward']
    cases.append({'key': key, 'exact_ambient_inverse_compositions': True,
                  'kernel_lattice_restriction_equals_integral_Smith_left_matrix': True,
                  'all_nontrivial_Smith_rows_unchanged': True,
                  'changed_rational_entries': differences})
assert adjusted == after
for name, value in manifest['files'].items():
    assert sha(author / name) == value['sha256'], name

review = '''# Root E.119 exact export-amendment audit

**PASS.** The original full root proof/source audit and ten-stage source-only arithmetic replay remain retained unchanged in `root_e119_audit`. The 745-line proof and every GP source, arithmetic stdout and author BIN object remain byte-identical. Root read the entire source amendment: it strengthens the integer-matrix serializer with integrality and decode assertions, adds a rational-string encoder with exact decoding, and uses that encoder for the two ambient Smith forward maps.

The preserved pre-amendment tree contains all 191 original manifested files with their exact byte counts and hashes. The amended manifest contains 415 files; root checked every current entry before and after execution. The proof hash is unchanged.

Root executed the corrected complete Python checker in a fresh copied directory using the ten GP outputs produced by root's original arithmetic reconstruction, together with their unchanged ten GP sources. The actual exit code is zero and stderr is empty. Its entire stdout and JSON are byte-identical to the corrected frozen author outputs, without exclusions. This is a fresh checker execution on root-generated arithmetic data. No additional GP execution or BNF certification is claimed.

Root separately decoded every forward entry through exact rational numerator and denominator values. Multiplication by the actual kernel lattice gives the integral Smith left matrix; both full ambient compositions with the retained inverse are identity. Eight B2 entries and four L2 entries change from the truncated integers to the exact denominator-three values. Each lies in a Smith row of modulus one. The projection of each affected row to its finite Smith factor is therefore zero; all nontrivial finite-coordinate rows, norm and extension maps remain exactly unchanged. Every other complete JSON field agrees with the original root output.

All twelve current author BIN hashes and all twelve original root BIN hashes match the prior full-decoding comparison record. The previously executed equality of every complete decoded PARI object is consequently retained with no component omitted. Raw serializations continue to have their separately recorded unequal byte hashes.

The author additionally supplies its independently executed exact-export verification and fresh checker-only replay. The peer's earlier certificate serialization has its own preserved original record and exact amendment. Their actual scopes are retained separately. This amendment changes saved ambient coordinates; it adds no mathematical claim and assigns no value to the remaining upper class kernels or capitulation subgroups.
'''
(here / 'audit.md').write_text(review)
record = {'statement': 'E.119', 'status': 'PASS_EXACT_SERIALIZATION_AMENDMENT_AND_FRESH_CHECKER',
          'proof_sha256': sha(proof), 'current_manifest_sha256': sha(mp),
          'current_manifest_files_verified': len(manifest['files']),
          'original_manifest_sha256': sha(oldmp), 'preserved_original_files_verified': len(oldmanifest['files']),
          'original_root_full_replay_sha256': sha(rp),
          'amended_source_sha256': sha(source), 'source_diff_sha256': sha(here / 'source_amendment.diff.md'),
          'actual_command': cmd, 'actual_exit_code': run.returncode, 'stderr_bytes': len(run.stderr),
          'complete_stdout_and_JSON_byte_identical': True, 'excluded_fields': [],
          'current_JSON_sha256': sha(author / 'code/e_lower_fiftythree.json'),
          'unchanged_GP_sources': gp_sources, 'root_generated_GP_outputs': gp_outputs,
          'unchanged_complete_binary_comparison_evidence': binary_records,
          'exact_ambient_matrix_cases': cases, 'all_other_JSON_fields_identical': True,
          'all_current_frozen_files_unchanged_after_execution': True,
          'new_GP_execution_claimed': False, 'new_BNF_certification_claimed': False,
          'full_proof_audit_reused_unchanged': 'root_e119_audit/audit.json',
          'audit_md_sha256': sha(here / 'audit.md')}
(here / 'audit.json').write_text(encode(record))
print(encode({'status': record['status'], 'audit_json_sha256': sha(here / 'audit.json'),
              'audit_md_sha256': sha(here / 'audit.md'), 'frozen_files_verified': len(manifest['files']),
              'corrected_full_stdout_and_JSON_byte_identical': True,
              'exact_fractional_entries': sum(len(x['changed_rational_entries']) for x in cases)}))
