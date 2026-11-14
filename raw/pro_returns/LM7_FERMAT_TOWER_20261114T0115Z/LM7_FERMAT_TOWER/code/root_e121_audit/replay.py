#!/usr/bin/env python3
"""Root replay of the frozen E121 sources and their exact E119 inputs."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent / 'research_e119_continuation'
GP = HERE.parent / 'research_e52/vendor/pari-2.19.0/gp'
parser = argparse.ArgumentParser()
parser.add_argument('--manifest', required=True)
parser.add_argument('--manifest-sha256', required=True)
parser.add_argument('--proof-sha256', required=True)
args = parser.parse_args()
manifest_path = AUTHOR / args.manifest
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(manifest_path) == args.manifest_sha256
proof = AUTHOR / 'sections/E_fiftythree_normalizer.tex'
assert sha(proof) == args.proof_sha256
manifest = json.loads(manifest_path.read_text())

def frozen_check():
    assert sha(manifest_path) == args.manifest_sha256
    for name, record in manifest['files'].items():
        path = AUTHOR / name
        assert sha(path) == record['sha256'], name
        if 'bytes' in record:
            assert path.stat().st_size == record['bytes'], name

frozen_check()
fresh = HERE / 'fresh'
assert not fresh.exists()
(fresh / 'code').mkdir(parents=True)
shutil.copytree(AUTHOR / 'inputs', fresh / 'inputs')
names = ['e53_order_nine_genus', 'e53_normalizer_actions',
         'e53_horizontal_upper_norm', 'e53_horizontal_upper_extension',
         'e53_cyclic_nine_comparison']
sources = ['code/' + n + '.gp' for n in names] + ['code/e53_normalizer_module.py']
for name in sources:
    shutil.copy2(AUTHOR / name, fresh / name)
    assert sha(AUTHOR / name) == sha(fresh / name)
input_manifest = json.loads((fresh / 'inputs/manifest.json').read_text())
for item in input_manifest['files']:
    assert sha(fresh / item['path']) == item['sha256']
    assert sha(HERE.parent / item['source']) == item['sha256']
assert not list((fresh / 'code').glob('*.out'))
assert not list((fresh / 'code').glob('*.bin'))

stage_runs = []
for name in names:
    command = [str(GP), '-q', '-f', name + '.gp']
    run = subprocess.run(command, cwd=fresh / 'code', stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    (fresh / 'code' / (name + '.out')).write_bytes(run.stdout)
    assert run.returncode == 0, (name, run.returncode)
    lines = run.stdout.decode().splitlines()
    bad = [s for s in lines if '***' in s and not (
        s.strip().startswith('***   Warning: new stack size = ') or
        s.strip().startswith('***   Warning: new maximum stack size = '))]
    assert not bad, (name, bad)
    records = [json.loads(s) for s in lines if s.startswith('{')]
    assert records[-1].get('status') == 'PASS'
    stage_runs.append({'source':name+'.gp','exit_code':run.returncode,
                       'stderr_policy':'Merged with stdout, matching the author driver.',
                       'output_sha256':sha(fresh/'code'/(name+'.out'))})
    print('PASS fresh GP stage: ' + name, flush=True)

command = [sys.executable, str(fresh / 'code/e53_normalizer_module.py')]
run = subprocess.run(command, cwd=fresh / 'code', stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
(fresh / 'code/e53_normalizer_module.out').write_bytes(run.stdout)
(fresh / 'code/e53_normalizer_module.err').write_bytes(run.stderr)
assert run.returncode == 0, (run.returncode, run.stderr.decode())
assert json.loads(run.stdout)['status'] == 'PASS'
text_names = ['code/'+n+'.out' for n in names] + [
    'code/e53_normalizer_module.out', 'code/e53_normalizer_module.json']
text_checks = {}
for name in text_names:
    a, b = AUTHOR/name, fresh/name
    assert a.read_bytes() == b.read_bytes(), name
    text_checks[name] = {'sha256':sha(a),'bytes':a.stat().st_size,
                         'byte_identical':True}

binary_names = sorted('code/'+p.name for p in (fresh/'code').glob('*.bin'))
assert len(binary_names) == 7
lines = ['default(parisizemax,2000000000);', 'allocatemem(256000000);']
binary_checks = {}
for name in binary_names:
    a, b = AUTHOR/name, fresh/name
    lines += ['a=read('+json.dumps(str(a))+');',
              'b=read('+json.dumps(str(b))+');',
              'if(!(a===b),error('+json.dumps('Complete GEN mismatch: '+name)+'));',
              'print('+json.dumps('PASS complete GEN: '+name)+');']
    binary_checks[name] = {'author_sha256':sha(a),'root_sha256':sha(b),
                          'raw_bytes_identical':a.read_bytes()==b.read_bytes()}
lines += ['print("PASS all complete PARI objects");', 'quit(0);']
(HERE/'compare_binary.gp').write_text('\n'.join(lines)+'\n')
comparison = subprocess.run([str(GP),'-q','-f',str(HERE/'compare_binary.gp')],
                            cwd=HERE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
(HERE/'compare_binary.out').write_bytes(comparison.stdout)
(HERE/'compare_binary.err').write_bytes(comparison.stderr)
assert comparison.returncode == 0
assert b'PASS all complete PARI objects' in comparison.stdout
bad = [s for s in comparison.stderr.decode().splitlines() if '***' in s and not (
    s.strip() == '*** allocatemem: Warning: increasing stack size to 256000000.' or
    s.strip().startswith('***   Warning: new stack size = ') or
    s.strip().startswith('***   Warning: new maximum stack size = '))]
assert not bad, bad
for item in binary_checks.values():
    item['whole_decoded_GEN_identical'] = True
frozen_check()
result = {'statement':'E.121','status':'PASS_ROOT_FIVE_STAGE_REPLAY',
          'manifest_sha256':sha(manifest_path),'proof_sha256':sha(proof),
          'frozen_files_before_and_after':len(manifest['files']),
          'stages':stage_runs,'mathematical_source_hashes':{
              n:sha(AUTHOR/n) for n in sources},
          'input_manifest':input_manifest,'text_outputs':text_checks,
          'binary_objects':binary_checks,'python_exit_code':run.returncode,
          'python_stderr_bytes':len(run.stderr),
          'binary_comparison_exit_code':comparison.returncode,
          'excluded_fields':[],'excluded_binary_components':[],
          'scope':'Five new GP stages and the exact Python checker freshly executed from copied sources and immutable E119 inputs. The earlier E119 BNF certifications were not repeated. Every complete new text output and every complete decoded binary object was compared.'}
(HERE/'replay.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
