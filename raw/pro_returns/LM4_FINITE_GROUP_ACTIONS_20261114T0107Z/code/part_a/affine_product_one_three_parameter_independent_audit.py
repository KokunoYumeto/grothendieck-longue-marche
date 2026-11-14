"""Independent integral Laurent audit of the actual three-parameter source.

No producer or algebra package is imported. Nineteen original F23 braid
words are evaluated using generic affine multiplication over the three-
variable integral Laurent ring. The exact principal quotient, invariant
2-dimensional submodule, diagonal quotient characters and actual seed
comparison maps are verified without a finite-field sample.
"""
from collections import Counter
from hashlib import sha256
from itertools import permutations
from pathlib import Path
import ast
import json


CHECKS = Counter()
ZERO = (0, 0, 0)
ONE = {ZERO: 1}
R = {(1, 0, 0): 1}
S = {(0, 1, 0): 1}
T = {(0, 0, 1): 1}
CHARACTERS = [(1, 0, 0), (0, 1, 0), (0, 0, 1), ZERO, ZERO, ZERO, (-1, -1, -1)]


def check(test, category):
    assert test, category
    CHECKS[category] += 1


def add(p, q):
    result = dict(p)
    for exponent, c in q.items():
        value = result.get(exponent, 0) + c
        if value:
            result[exponent] = value
        else:
            result.pop(exponent, None)
    return result


def negative(p):
    return {e: -c for e, c in p.items()}


def shift(p, exponent):
    return {tuple(x+y for x,y in zip(e,exponent)): c for e,c in p.items()}


def mul(p, q):
    result = {}
    for e,c in p.items():
        for f,d in q.items():
            result = add(result, {tuple(x+y for x,y in zip(e,f)): c*d})
    return result


def power(p, n):
    if n < 0:
        check(len(p) == 1, 'only_monomial_denominators')
        exponent, c = next(iter(p.items()))
        check(c in [-1, 1], 'only_signed_unit_denominators')
        return {tuple(e*n for e in exponent): -1 if c == -1 and n % 2 else 1}
    result = ONE
    for _ in range(n):
        result = mul(result, p)
    return result


def integer_literal(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return node.value
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -integer_literal(node.operand)
    raise ValueError('Noninteger exponent')


def parse_node(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return {ZERO: node.value} if node.value else {}
    if isinstance(node, ast.Name) and node.id in ['r', 's', 't']:
        return {'r': R, 's': S, 't': T}[node.id]
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return negative(parse_node(node.operand))
    if isinstance(node, ast.BinOp):
        left = parse_node(node.left)
        if isinstance(node.op, ast.Pow):
            return power(left, integer_literal(node.right))
        right = parse_node(node.right)
        if isinstance(node.op, ast.Add):
            return add(left, right)
        if isinstance(node.op, ast.Sub):
            return add(left, negative(right))
        if isinstance(node.op, ast.Mult):
            return mul(left, right)
        if isinstance(node.op, ast.Div):
            return mul(left, power(right, -1))
    raise ValueError('Unsupported Laurent syntax')


def parse(text):
    return parse_node(ast.parse(text, mode='eval').body)


def parse_matrix(rows):
    return [[parse(x) for x in row] for row in rows]


def identity(n):
    return [[ONE if i == j else {} for j in range(n)] for i in range(n)]


def matrix_mul(a, b):
    answer = [[{} for _ in b[0]] for _ in a]
    for i, row in enumerate(a):
        for k, x in enumerate(row):
            if x:
                for j, y in enumerate(b[k]):
                    if y:
                        answer[i][j] = add(answer[i][j], mul(x, y))
    return answer


def matrix_sub(a, b):
    return [[add(x, negative(y)) for x, y in zip(row, old)]
            for row, old in zip(a, b)]


def scalar_mul(p, a):
    return [[mul(p, x) for x in row] for row in a]


def group_mul(g, h):
    a, x = g
    b, y = h
    return tuple(x+y for x,y in zip(a,b)), [add(xx, shift(yy, a)) for xx, yy in zip(x, y)]


def group_inv(g):
    a, x = g
    ai = tuple(-e for e in a)
    return ai, [negative(shift(xx, ai)) for xx in x]


def group_conj(g, h):
    return group_mul(group_mul(g, h), group_inv(g))


def group_product(elements):
    answer = (ZERO, [{} for _ in range(7)])
    for element in elements:
        answer = group_mul(answer, element)
    return answer


def literal_braid(word):
    unit = (ZERO, [{} for _ in range(7)])
    x = [(e, row) for e, row in zip(CHARACTERS, identity(7))] + [unit]
    c = [unit] * 8
    labels = list(range(8))
    initial_boundary = group_product(x)
    for crossing in word:
        j = abs(crossing)-1
        a, b = x[j:j+2]
        ca, cb = c[j:j+2]
        if crossing > 0:
            x[j:j+2] = [group_conj(a, b), a]
            c[j:j+2] = [group_mul(a, cb), ca]
        else:
            bi = group_inv(b)
            x[j:j+2] = [b, group_conj(bi, a)]
            c[j:j+2] = [cb, group_mul(bi, ca)]
        labels[j], labels[j+1] = labels[j+1], labels[j]
    check(labels == list(range(8)), 'literal_pure_braid')
    check(x[-1] == unit, 'erased_meridian')
    check([g[0] for g in x[:-1]] == CHARACTERS, 'literal_character_preserved')
    check(group_product(x) == initial_boundary, 'literal_boundary_product_fixed')
    u = group_inv(c[-1])
    action = [group_conj(u, g)[1] for g in x[:-1]]
    return u, action


def determinant(a):
    n = len(a)
    result = {}
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        term = ONE if inversions % 2 == 0 else negative(ONE)
        for i, j in enumerate(perm):
            term = mul(term, a[i][j])
        result = add(result, term)
    return result


def serialize(p):
    return [[c, list(e)] for e, c in sorted(p.items())]


def main():
    CHECKS.clear()
    producer=Path(__file__).resolve()
    folder=producer.parent
    paths={'braids':folder/'full_cross_source_stage/marginal_braids.json',
           'symbolic':folder/'affine_product_one_three_parameter_stage_output.json',
           'universal':folder/'affine_obstruction_stage_output.json'}
    hashes={name:sha256(path.read_bytes()).hexdigest() for name,path in paths.items()}
    braid_data=json.loads(paths['braids'].read_text())
    symbolic=json.loads(paths['symbolic'].read_text())
    check(symbolic['source_sha256']==hashes['universal'],'universal_input_binding')
    old=[x for x in braid_data['records'] if x['index']<11]
    seeds=[x for x in braid_data['records'] if x['index']>=11 and int(x['label'].split('_')[2])==-1]
    check(len(old)==11 and len(seeds)==8,'nineteen_actual_words')
    delta=[[add({e:1},negative(ONE))] for e in CHARACTERS]
    section=identity(6)+[[{} for _ in range(6)]]
    basis=parse_matrix([
        ['-r','-r*s','1','-r*s*t','-r*s*t','-r*s*t'],
        ['1','0','0','0','0','0'],
        ['0','1','0','0','0','0'],
        ['0','0','0','1','0','0'],
        ['0','0','0','0','1','0'],
        ['0','0','0','0','0','1']])
    inverse_basis=parse_matrix([
        ['0','1','0','0','0','0'],
        ['0','0','1','0','0','0'],
        ['1','r','r*s','r*s*t','r*s*t','r*s*t'],
        ['0','0','0','1','0','0'],
        ['0','0','0','0','1','0'],
        ['0','0','0','0','0','1']])
    check(matrix_mul(basis,inverse_basis)==identity(6),'basis_inverse')
    check(matrix_mul(inverse_basis,basis)==identity(6),'inverse_basis')
    check(basis==parse_matrix(symbolic['basis']),'producer_basis')
    check(inverse_basis==parse_matrix(symbolic['inverse_basis']),'producer_inverse_basis')
    kernel_section=[row[:2] for row in basis]
    kernel_projection=inverse_basis[:2]
    check(matrix_mul(kernel_projection,kernel_section)==identity(2),'kernel_coordinate_inverse')
    section_basis=matrix_mul(section,basis)
    section_kernel=matrix_mul(section,kernel_section)
    boundary=parse_matrix([['1','r','r*s','r*s*t','r*s*t','r*s*t','r*s*t']])
    check(matrix_mul(boundary,delta)==[[{}]],'boundary_kills_principals')
    actual=[];blocks=[];cores=[];labels=[]
    for braid,shown in zip(old,symbolic['source_records']):
        check(braid['index']==shown['index'],'actual_source_index')
        u,action=literal_braid(braid['negative_braid'])
        check(action==parse_matrix(shown['action_7']),'literal_action_7')
        check(matrix_mul(action,delta)==delta,'principal_vector_fixed')
        check(matrix_mul(boundary,action)==scalar_mul({u[0]:1},boundary),'actual_boundary_quotient')
        block=parse_matrix(shown['block_action_6'])
        lhs=matrix_mul(action,section_basis)
        rhs=matrix_mul(section_basis,block)
        check(scalar_mul(delta[6][0],matrix_sub(lhs,rhs))==matrix_mul(delta,[lhs[6]]),
              'actual_principal_quotient_identity')
        core=[row[:2] for row in block[:2]]
        check(core==parse_matrix(shown['core_matrix']),'producer_core_matrix')
        correction=parse_matrix(shown['principal_correction_row'])
        check(matrix_sub(matrix_mul(action,section_kernel),matrix_mul(section_kernel,core))==matrix_mul(delta,correction),
              'actual_core_principal_correction')
        for i in range(2,6):
            for j in range(6):
                if i!=j: check(not block[i][j],'actual_diagonal_four_quotients')
        actual.append(action);blocks.append(block);cores.append(core);labels.append(braid['label'])
    for index,scalar in [(0,R),(7,T),(8,ONE),(9,ONE)]:
        check(cores[index]==scalar_mul(scalar,identity(2)),'actual_scalar_core_operator')
    expected_quotients={
        0:['1','r','r','r'],
        7:['1/t','t','t','r*s*t**2'],
        8:['1','r*s*t','1','1/t'],
        9:['1','1/t','r*s*t','1']}
    comparison_table=[]
    for index,values in expected_quotients.items():
        diagonal=[blocks[index][j][j] for j in range(2,6)]
        check(diagonal==[parse(x) for x in values],'actual_four_quotient_comparison_table')
        comparison_table.append({'source_index_zero_based':index,'source_label':labels[index],
                                 'quotient_values':values})
    check(blocks[2][2][2]==parse('r*t'),'boundary_source_two_scalar')
    seed_values=[];chosen=None
    symbolic_seeds={x['index']:x for x in symbolic['seed_records']}
    for braid in seeds:
        u,_=literal_braid(braid['negative_braid'])
        row=matrix_mul([u[1]],section_kernel)
        check(row==parse_matrix(symbolic_seeds[braid['index']]['core_value_row']),'actual_seed_core_values')
        seed_values.append({'index':braid['index'],'label':braid['label'],
                            'scalar':serialize({u[0]:1}),'row':[[serialize(x) for x in row[0]]]})
        if braid['index']==25:
            check(braid['label']=='cross_4_-1_1','chosen_actual_seed_label')
            check({u[0]:1}==parse('1/(r*s*t)'),'chosen_actual_seed_scalar')
            check(row==parse_matrix([['r*s*t-1','0']]),'chosen_actual_seed_core_row')
            chosen=u[1]
    check(chosen is not None,'chosen_seed_exists')
    evals=[]
    for i in [2,7]:
        row=matrix_mul([chosen],matrix_sub(actual[i],identity(7)))
        check(matrix_mul(row,delta)==[[{}]],'actual_character_one_cohomology_evaluation')
        core_row=matrix_mul(row,section_kernel)
        expected=['1-r*s*t','0'] if i==2 else ['0','s*(r*s*t-1)']
        check(core_row==parse_matrix([expected]),'explicit_two_core_evaluations')
        evals.append(core_row[0])
    eval_det=determinant(evals)
    check(eval_det==parse('-s*(r*s*t-1)**2'),'actual_core_evaluation_determinant')
    result={'status':'PASS_INTEGRAL_THREE_PARAMETER_SOURCE_COMPARISON_AUDIT',
            'producer_sha256':sha256(producer.read_bytes()).hexdigest(),
            'inputs':{str(paths[name]):hashes[name] for name in paths},
            'source_words':11,'seed_words':8,
            'core_scalar_sources_zero_based':{'0':'r*I2','7':'t*I2','8':'I2','9':'I2'},
            'comparison_table':comparison_table,'boundary_source_two_scalar':'r*t',
            'seed_values':seed_values,'core_evaluation_words':['B_2(u_25)*u_25^-1','B_7(u_25)*u_25^-1'],
            'core_evaluation_matrix':[[serialize(x) for x in row] for row in evals],
            'core_evaluation_determinant':serialize(eval_det),
            'checks':dict(CHECKS),'check_total':sum(CHECKS.values()),
            'scope':'The exact source identities and comparison table on the three-parameter locus. Each index is the original zero-based F23 index and its label is recorded. No representation-theoretic consequence is asserted by this verifier alone.',
            'independence':'No producer or algebra-package imports. Generic integral Laurent affine multiplication reconstructs the original words, independently of the producer specialization and symbolic simplification.'}
    output=producer.with_name('affine_product_one_three_parameter_independent_audit_output.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'checks':result['check_total'],
                      'comparison_table':comparison_table,'boundary_source_two_scalar':'r*t',
                      'core_evaluation_determinant':'-s*(r*s*t-1)^2',
                      'output_sha256':sha256(output.read_bytes()).hexdigest()},indent=2))


if __name__=='__main__':
    main()


