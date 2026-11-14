#!/usr/bin/env python3
"""Replay the unchanged actual standard-quotient and chain-cover certificate."""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT/'work/root/actual_transporter_independent_replay'
DEST.mkdir(exist_ok=True)
expected = {
    'work/part_d_attack/actual_transporter_single_parameter_reduction.txt': '7ba862392788a46b4fa92563ae0c5cea293897fd8d39ac9d27a17e2ab6826b49',
    'work/part_d_attack/actual_transporter_single_parameter_reduction_result.json': 'cc281bb8abf4e351971891dc881106143449491d81abef5ce33d10cde632d4bf',
    'work/part_d_attack/code/actual_transporter_reduction.py': 'a0507439a6132be28aca56fb4c4d5d7316fb2fa103c8c181664acbcb970c3c2b',
    'work/part_d_attack/code/actual_transporter_reduction_output.json': '43f8ceef3d62899e624a99b3699fcc17256c9dae49f8599d6c45a43c5b52b92d',
    'work/part_d_attack/code/actual_transporter_reduction_stdout.txt': '43f8ceef3d62899e624a99b3699fcc17256c9dae49f8599d6c45a43c5b52b92d',
}

def bind(path):
    p = Path(path)
    p = p if p.is_absolute() else ROOT/p
    return {'path': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size,
            'sha256': sha256(p.read_bytes()).hexdigest()}

for path, digest in expected.items():
    assert bind(path)['sha256'] == digest, path
metadata = json.loads((ROOT/'work/part_d_attack/actual_transporter_single_parameter_reduction_result.json').read_text())
for entry in metadata['files']+metadata['dependency_bindings']:
    actual = bind(entry['path'])
    assert actual['bytes'] == entry['bytes'] and actual['sha256'] == entry['sha256'], entry['path']
source = ROOT/'work/part_d_attack/code/actual_transporter_reduction.py'
program = DEST/source.name
shutil.copyfile(source, program)
assert source.read_bytes() == program.read_bytes()
stdout = DEST/'stdout.txt'
stderr = DEST/'stderr.txt'
with stdout.open('wb') as out, stderr.open('wb') as err:
    proc = subprocess.run([sys.executable, str(program)], cwd=DEST, stdout=out, stderr=err)
assert proc.returncode == 0 and not stderr.read_bytes()
original = source.with_name('actual_transporter_reduction_output.json')
replay = program.with_name(original.name)
assert replay.read_bytes() == original.read_bytes() == stdout.read_bytes()
d = json.loads(replay.read_text())
assert d['status'] == 'PASS' and d['assertion_count'] == len(d['checks']) == 24
assert all(c['passed'] for c in d['checks'])
assert d['base_B_unit_residues'] == [1,11,19,29,31,41,49,59]
assert d['base_T_unit_residues'] == [1,19,41,59]
assert d['refined_B_unit_residues'] == [1,19,41,59,61,79,101,119]
assert d['refined_T_unit_residues'] == [1,41,79,119]
assert sorted({m % 60 for m in d['refined_B_unit_residues']}) == d['base_T_unit_residues']
assert d['base_total_order'] == 480 and d['base_parity_order'] == 240
assert d['refined_parity_group_order'] == 60*2**61
assert d['base_parity_exponent'] == 30 and d['refined_parity_exponent'] == 60
assert len(d['tree_edges']) == 59 and len(d['tree_chains_hex']) == 60
assert len(d['Schreier_cycle_basis_hex']) == 61
for row in d['base_rows']:
    assert row['B_conjugator_count_in_A5_times_C2_squared'] in [0,20]
    assert row['B_conjugator_count_in_A5_times_C2_squared'] == 4*len(row['A5_conjugator_indices'])
for row in d['refined_rows']:
    assert len(row['one_chain_per_solution_coset']) == row['solution_coset_count']
    assert row['solution_coset_count']*row['solutions_per_base_coset'] == (40960 if row['B_nonempty'] else 0)
for path, digest in expected.items():
    assert bind(path)['sha256'] == digest, path
result = {
    'status': 'PASS', 'exit_code': proc.returncode, 'named_checks': 24,
    'originals_unchanged': [bind(p) for p in expected],
    'dependencies_verified': [bind(e['path']) for e in metadata['dependency_bindings']],
    'original': bind(original), 'replay': bind(replay),
    'stdout': bind(stdout), 'stderr': bind(stderr), 'program': bind(program),
    'runner': bind(Path(__file__)), 'raw_output_byte_identical': True,
    'stdout_raw_byte_identical': True,
    'base_rows_checked': len(d['base_rows']), 'refined_rows_checked': len(d['refined_rows']),
    'all_retained_chain_witnesses_substituted_by_the_replayed_program': True,
    'exact_coarse_and_refined_residue_sets_verified': True,
    'scope': 'The actual standard P3 quotient and its mod-two homology refinement. The original general D74 transporter parameter nonemptiness remains unresolved.'
}
(DEST/'comparison.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'status': 'PASS', 'checks': 24, 'raw_output_byte_identical': True,
                  'base_rows': len(d['base_rows']), 'refined_rows': len(d['refined_rows']),
                  'comparison': str((DEST/'comparison.json').relative_to(ROOT))}, indent=2))
