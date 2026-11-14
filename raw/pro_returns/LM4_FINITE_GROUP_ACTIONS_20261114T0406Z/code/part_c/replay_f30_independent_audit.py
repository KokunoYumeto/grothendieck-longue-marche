#!/usr/bin/env python3
"""Exact peer replay of F30's three-original-word Laurent certificate."""
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import json
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
AUTHOR = ROOT/'work/part_a/code'
DEST = ROOT/'work/part_c/f30_independent_replay'


def bind(path):
    data = path.read_bytes()
    return {'path':str(path.relative_to(ROOT)), 'bytes':len(data),
            'sha256':sha256(data).hexdigest()}


def main():
    proof = ROOT/'work/part_a/f_product_one_first_scalar_field_images.tex'
    assert bind(proof)['sha256'] == '1703a98c06269ec8ad73cdd5e420f7213ba620e06a6dcc104905447566a613f5'
    stem = 'affine_product_one_first_scalar_field_independent_audit'
    names = [stem+'.py','affine_four_parameter_extension_independent_audit.py',
             'affine_product_one_first_scalar_field_stage.py',
             'affine_product_one_first_scalar_field_stage_output.json',
             'affine_obstruction_stage_output.json',
             'full_cross_source_stage/marginal_braids.json']
    originals = {name:bind(AUTHOR/name) for name in names}
    original_output = AUTHOR/(stem+'_output.json')
    original_binding = bind(original_output)
    DEST.mkdir(parents=True,exist_ok=False)
    copies = []
    for name in names:
        target = DEST/name
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(AUTHOR/name,target)
        assert target.read_bytes() == (AUTHOR/name).read_bytes()
        copies.append({'original':originals[name],'copy':bind(target)})
    stdout,stderr = DEST/'stdout.txt',DEST/'stderr.txt'
    with stdout.open('wb') as out, stderr.open('wb') as err:
        run = subprocess.run([sys.executable,str(DEST/(stem+'.py'))],cwd=ROOT,
                             stdout=out,stderr=err,check=False)
    assert run.returncode == 0 and stderr.read_bytes() == b''
    output = DEST/(stem+'_output.json')
    raw = json.loads(output.read_text())
    assert raw['check_total'] == sum(raw['checks'].values()) == 45
    assert [entry['index'] for entry in raw['source_records']] == [0,2,7]
    assert [entry['label'] for entry in raw['source_records']] == ['old0','old_1_1','old_-1_1']
    assert [entry['boundary_character'] for entry in raw['source_records']] == ['1','r*t','1/t']
    assert raw['source_records'][0]['core_scalar'] == 'r'
    transported = deepcopy(raw)
    path_map = {}
    transported_inputs = {}
    for path,digest in raw['inputs'].items():
        local = Path(path)
        original = AUTHOR/local.relative_to(DEST)
        assert local.read_bytes() == original.read_bytes()
        assert sha256(local.read_bytes()).hexdigest() == digest
        path_map[path] = str(original)
        transported_inputs[str(original)] = digest
    assert len(path_map) == len(set(path_map.values())) == 5
    transported['inputs'] = transported_inputs
    transported_path = DEST/'path_transport_output.json'
    transported_path.write_text(json.dumps(transported,indent=2)+'\n')
    assert transported_path.read_bytes() == original_output.read_bytes()
    for name in names:
        assert bind(AUTHOR/name) == originals[name]
    assert bind(original_output) == original_binding
    result = {'status':'PASS','checks':45,'exit_code':run.returncode,
              'original':original_binding,'replay':bind(output),
              'raw_byte_identical':output.read_bytes()==original_output.read_bytes(),
              'exact_five_input_path_bijection':path_map,
              'path_transported_output_byte_identical':True,
              'path_transported_output':bind(transported_path),
              'copied_inputs':copies,'all_original_inputs_unchanged_after_replay':True,
              'proof':bind(proof),'stdout':bind(stdout),'stderr':bind(stderr),
              'runner':bind(Path(__file__).resolve()),
              'scope':'Unchanged independent verifier, original sources0,2,7, exact X1-pivot principal correction and five-dimensional scalar-core identity; no symbolic producer or universal F24 certificate rerun.'}
    comparison = DEST/'comparison.json'
    comparison.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','checks':45,'comparison':bind(comparison)},indent=2))


if __name__ == '__main__':
    main()
