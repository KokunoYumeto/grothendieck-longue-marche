#!/usr/bin/env python3
"""Copy only E119's mathematical sources, rebuild, and compare every output.

Usage: python code/e_lower_fiftythree_replay.py --gp /absolute/path/gp
No expected output or BIN object is copied into the reconstruction tree.
The complete decoded PARI objects are compared; no component is excluded.
"""
from pathlib import Path
import argparse, hashlib, json, shutil, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]
P = argparse.ArgumentParser()
P.add_argument('--gp', required=True)
P.add_argument('--destination')
A = P.parse_args()
GP = str(Path(A.gp).resolve())
DEST = Path(A.destination).resolve() if A.destination else ROOT/'audit'/'author_replay'
assert not DEST.exists(), 'Use a new destination; previous actual executions are retained.'
FRESH = DEST/'fresh'
for name in ('code', 'inputs'):
    (FRESH/name).mkdir(parents=True)
names = [
    'e53_horizontal_base','e53_genus_kummer','e53_six_character_witness',
    'e53_horizontal_norm_matrix','e53_genus_transition','e53_local_genus_maps',
    'e53_positional_horizontal_norm','e53_positional_genus_transition']
deps = ['e116_small_inert_units', 'e116_prime_columns']
sources = [Path('code/e_lower_fiftythree.py')]
sources += [Path('code')/(n+'.gp') for n in names]
sources += [Path('inputs')/(n+'.gp') for n in deps]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
for rel in sources:
    shutil.copy2(ROOT/rel, FRESH/rel)
command = [sys.executable, str(FRESH/'code/e_lower_fiftythree.py'), '--gp', GP]
run = subprocess.run(command, cwd=FRESH/'code', stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)
(FRESH/'code/e_lower_fiftythree.out').write_bytes(run.stdout)
assert run.returncode == 0, (run.returncode, run.stdout.decode()[-3000:])
text_files = [Path('code/e_lower_fiftythree.out'), Path('code/e_lower_fiftythree.json')]
text_files += [Path('code')/(n+'.out') for n in names]
text_files += [Path('inputs')/(n+'.out') for n in deps]
text_checks = {}
for rel in text_files:
    x, y = ROOT/rel, FRESH/rel
    assert x.read_bytes() == y.read_bytes(), str(rel)
    text_checks[str(rel)] = {'sha256': sha(x), 'bytes': x.stat().st_size,
                            'byte_identical': True}
binary_files = sorted([p.relative_to(ROOT) for sub in ('code','inputs')
                       for p in (ROOT/sub).glob('*.bin')])
lines = ['default(parisizemax,1000000000);', 'allocatemem(256000000);']
binary_checks = {}
for rel in binary_files:
    x, y = ROOT/rel, FRESH/rel
    assert y.is_file(), str(rel)
    lines += ['a=read('+json.dumps(str(x))+');',
              'b=read('+json.dumps(str(y))+');',
              'if(!(a===b),error('+json.dumps('Complete GEN mismatch: '+str(rel))+'));',
              'print('+json.dumps('PASS complete GEN: '+str(rel))+');']
    binary_checks[str(rel)] = {'author_sha256': sha(x), 'replay_sha256': sha(y),
                               'raw_bytes_identical': x.read_bytes() == y.read_bytes()}
lines += ['print("PASS all complete PARI objects");', 'quit(0);']
gp_source = DEST/'compare_binary.gp'
gp_source.write_text('\n'.join(lines)+'\n')
check = subprocess.run([GP,'-q','-f',str(gp_source)], cwd=DEST,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(DEST/'compare_binary.out').write_bytes(check.stdout)
(DEST/'compare_binary.err').write_bytes(check.stderr)
assert check.returncode == 0 and b'PASS all complete PARI objects' in check.stdout
errors = [s for s in check.stderr.decode().splitlines() if '***' in s and
          not (s.strip().startswith('***   Warning: new stack size = ') or
               s.strip().startswith('***   Warning: new maximum stack size = '))]
assert not errors, errors
for item in binary_checks.values():
    item['complete_decoded_GEN_identical'] = True
result = {'statement':'E.119', 'status':'PASS', 'GP_stages':10,
          'source_copy_only':True, 'rebuild_exit_code':run.returncode,
          'text_outputs':text_checks, 'binary_objects':binary_checks,
          'source_sha256':{str(r):sha(ROOT/r) for r in sources},
          'excluded_fields':[], 'excluded_binary_components':[],
          'binary_comparison_exit_code':check.returncode,
          'scope':'Independent author reconstruction from copied sources; complete text and decoded-object comparison. This is not a peer proof audit.'}
data = json.dumps(result,indent=2)+'\n'
(DEST/'replay.json').write_text(data)
(ROOT/'code/e_lower_fiftythree_replay.json').write_text(data)
print(data,end='')
