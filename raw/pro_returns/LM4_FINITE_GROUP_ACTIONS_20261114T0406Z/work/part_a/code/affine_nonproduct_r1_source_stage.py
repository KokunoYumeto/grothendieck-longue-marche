"""Exact r=1 general-character boundary/X1 source-module chart."""
from hashlib import sha256
from pathlib import Path
import json
import runpy


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    source = folder/'affine_nonproduct_boundary_quotient_stage_output.json'
    helper = folder/'affine_four_parameter_extension_independent_audit.py'
    products = folder/'affine_full_product_one_independent_audit.py'
    data = json.loads(source.read_text())
    arithmetic, sparse = runpy.run_path(str(helper)), runpy.run_path(str(products))
    names = ['s', 't', 'u', 'v', 'w', 'z']
    characters = [[0]*6]+[[int(i == j) for i in range(6)] for j in range(6)]
    arithmetic['configure'](names, characters)
    parse, pm = arithmetic['parse'], arithmetic['parse_matrix']
    mm, add, eye, scale = [sparse[name] for name in ['mm', 'plus', 'eye', 'scale']]
    one = parse('1')
    h = parse('s*t*u*v*w*z')
    parse.__globals__['UNITS']['h'] = h
    basis_text = [['-s', '-s*t', '-s*t*u', '-s*t*u*v', '-s*t*u*v*w', '1'],
                  ['1', '0', '0', '0', '0', '0'], ['0', '1', '0', '0', '0', '0'],
                  ['0', '0', '1', '0', '0', '0'], ['0', '0', '0', '1', '0', '0'],
                  ['0', '0', '0', '0', '1', '0']]
    inverse_text = [['0', '1', '0', '0', '0', '0'], ['0', '0', '1', '0', '0', '0'],
                    ['0', '0', '0', '1', '0', '0'], ['0', '0', '0', '0', '1', '0'],
                    ['0', '0', '0', '0', '0', '1'],
                    ['1', 's', 's*t', 's*t*u', 's*t*u*v', 's*t*u*v*w']]
    basis, inverse = pm(basis_text), pm(inverse_text)
    assert mm(basis, inverse) == eye(6, one) and mm(inverse, basis) == eye(6, one)
    character_table = ['1', '1/u**2', '1/t', '1/v**2', '1/w**2', '1/z**2',
                       '1', 't/h', '1', '1', '1']

    def specialize(poly):
        answer = {}
        for coefficient, exponent in poly:
            answer = add(answer, {tuple(exponent[1:]): coefficient})
        return answer

    records = []
    for old in data['records']:
        index = old['index']
        matrix = [[specialize(poly) for poly in row] for row in old['boundary_quotient_matrix_6']]
        block = mm(mm(inverse, matrix), basis)
        assert all(not entry for entry in block[5][:5]), ('invariant_X1_kernel', index)
        assert block[5][5] == parse(character_table[index]), ('actual_X1_character', index)
        core = [row[:5] for row in block[:5]]
        if index == 0:
            assert core == scale(parse('1/h'), eye(5, one))
        records.append({'index': index, 'label': old['label'],
                        'block_matrix_6': arithmetic['serial_matrix'](block),
                        'core_matrix_5': arithmetic['serial_matrix'](core),
                        'X1_quotient_character': character_table[index]})
    result = {'status': 'EXACT_R1_GENERAL_CHARACTER_X1_KERNEL_SOURCE_DATA',
              'producer_sha256': sha256(script.read_bytes()).hexdigest(),
              'inputs': {str(path): sha256(path.read_bytes()).hexdigest() for path in [source, helper, products]},
              'variables': names, 'characters': characters,
              'basis': basis_text, 'inverse_basis': inverse_text,
              'boundary_product': 'h=s*t*u*v*w*z', 'records': records,
              'scope': 'Actual five-dimensional X1-evaluation kernel and its one-dimensional quotient on r=1,h!=1, via the explicitly proved boundary principal quotient. Source0 is exactly h^-1 I5 on the kernel. No general-character affine equality is asserted.'}
    output = script.with_name('affine_nonproduct_r1_source_stage_output.json')
    output.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print(json.dumps({'status': result['status'], 'source_records': len(records),
                      'quotient_characters': character_table,
                      'output_sha256': sha256(output.read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
