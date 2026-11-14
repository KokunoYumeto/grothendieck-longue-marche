"""Independent original-word audit of the four-parameter continuation.

Three coefficient charts are checked separately: the generic four-parameter
X7-pivot chart, the deleted-first three-parameter X4-pivot chart, and its
r=1 essential-line chart. No producer or symbolic algebra package is
imported. All coefficient arithmetic is integral sparse Laurent arithmetic.
"""
from collections import Counter
from hashlib import sha256
from itertools import permutations
from pathlib import Path
import ast
import json


CHECKS = Counter()
ZERO = ()
ONE = {(): 1}
CHARACTERS = []
UNITS = {}


def configure(names, characters):
    global ZERO, ONE, CHARACTERS, UNITS
    ZERO = (0,)*len(names)
    ONE = {ZERO: 1}
    CHARACTERS = [tuple(x) for x in characters]
    UNITS = {name: {tuple(int(i==j) for i in range(len(names))): 1}
             for j,name in enumerate(names)}


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
    if isinstance(node, ast.Name) and node.id in UNITS:
        return UNITS[node.id]
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


def serial_matrix(a):
    return [[serialize(x) for x in row] for row in a]


def chart_specs():
    return [
        {'name':'four_parameter','stem':'affine_product_one_four_parameter_stage',
         'names':['r','s','t','u'],
         'characters':[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0],[-1,-1,-1,-1]],
         'pivot':6,'keep':[0,1,2,3,4,5],'core_dimension':3,
         'basis_key':'basis','inverse_key':'inverse_basis','block_key':'block_action_6',
         'basis':[['-r','-r*s','-r*s*t','1','-r*s*t*u','-r*s*t*u'],
                  ['1','0','0','0','0','0'],['0','1','0','0','0','0'],
                  ['0','0','1','0','0','0'],['0','0','0','0','1','0'],['0','0','0','0','0','1']],
         'inverse':[['0','1','0','0','0','0'],['0','0','1','0','0','0'],['0','0','0','1','0','0'],
                    ['1','r','r*s','r*s*t','r*s*t*u','r*s*t*u'],['0','0','0','0','1','0'],['0','0','0','0','0','1']],
         'scalar_core':{0:'r',7:'t'},
         'quotient_table':{0:['1','r','r'],2:['r*t','r*t/u','r**2*s*t**2*u'],
                           7:['1/t','t/u','r*s*t**2*u'],8:['1','1','1/t'],9:['1','r*s*t*u','1']}},
        {'name':'deleted_first_three_parameter','stem':'affine_product_one_deleted_first_stage',
         'names':['r','s','t'],
         'characters':[[1,0,0],[0,1,0],[0,0,1],[-1,-1,-1],[0,0,0],[0,0,0],[0,0,0]],
         'pivot':3,'keep':[0,1,2,4,5,6],'core_dimension':2,
         'basis_key':'basis','inverse_key':'inverse_basis','block_key':'block_action_6',
         'basis':[['-r','-r*s','1','-1','-1','-1'],['1','0','0','0','0','0'],['0','1','0','0','0','0'],
                  ['0','0','0','1','0','0'],['0','0','0','0','1','0'],['0','0','0','0','0','1']],
         'inverse':[['0','1','0','0','0','0'],['0','0','1','0','0','0'],['1','r','r*s','1','1','1'],
                    ['0','0','0','1','0','0'],['0','0','0','0','1','0'],['0','0','0','0','0','1']],
         'scalar_core':{0:'r',7:'t',8:'1',10:'1'},
         'quotient_table':{0:['1','r','r','r'],2:['r*t','r**2*s*t**2','r*t','r*t'],
                           7:['1/t','r*s*t**2','t','t'],8:['1','1','1/t','r*s*t'],10:['1','1/t','r*s*t','1']}},
        {'name':'deleted_first_two_parameter','stem':'affine_deleted_first_two_parameter_stage',
         'names':['s','t'],
         'characters':[[0,0],[1,0],[0,1],[-1,-1],[0,0],[0,0],[0,0]],
         'pivot':3,'keep':[0,1,2,4,5,6],'core_dimension':1,
         'basis_key':'flag_change','inverse_key':'flag_inverse','block_key':'action_flag_6',
         'basis':[['0','0','0','0','1','0'],['1','1','-1','-1','-1','-1'],['-1/s','0','0','0','0','0'],
                  ['0','0','0','1','0','0'],['0','0','1','0','0','0'],['0','0','0','0','0','1']],
         'inverse':[['0','0','-s','0','0','0'],['1','1','s','1','1','1'],['0','0','0','0','1','0'],
                    ['0','0','0','1','0','0'],['1','0','0','0','0','0'],['0','0','0','0','0','1']],
         'scalar_core':dict(enumerate(['1','1','t','1','s','1','1','t','1','s','1'])),
         'quotient_table':{}}
    ]


def verify_chart(specification, braid_data, folder, universal_hash):
    configure(specification['names'],specification['characters'])
    symbolic_path=folder/(specification['stem']+'_output.json')
    symbolic=json.loads(symbolic_path.read_text())
    check(symbolic['source_sha256']==universal_hash,'universal_input_binding')
    code=folder/(specification['stem']+'.py')
    check(symbolic['producer_sha256']==sha256(code.read_bytes()).hexdigest(),'symbolic_producer_binding')
    basis=parse_matrix(specification['basis']);inverse_basis=parse_matrix(specification['inverse'])
    check(matrix_mul(basis,inverse_basis)==identity(6),'independent_basis_inverse')
    check(matrix_mul(inverse_basis,basis)==identity(6),'independent_inverse_basis')
    check(basis==parse_matrix(symbolic[specification['basis_key']]),'producer_basis')
    check(inverse_basis==parse_matrix(symbolic[specification['inverse_key']]),'producer_inverse_basis')
    delta=[[add({e:1},negative(ONE))] for e in CHARACTERS]
    section=[[{} for _ in range(6)] for _ in range(7)]
    for j,i in enumerate(specification['keep']):section[i][j]=ONE
    section_basis=matrix_mul(section,basis);dimension=specification['core_dimension']
    core_lift=[row[:dimension] for row in section_basis]
    old=[x for x in braid_data['records'] if x['index']<11]
    seeds=[x for x in braid_data['records'] if x['index']>=11 and int(x['label'].split('_')[2])==-1]
    check(len(old)==11 and len(seeds)==8,'nineteen_actual_words')
    blocks=[];cores=[];actual=[]
    for word,shown in zip(old,symbolic['source_records']):
        check(word['index']==shown['index'] and word['label']==shown['label'],'actual_index_and_label')
        u,action=literal_braid(word['negative_braid'])
        check(action==parse_matrix(shown['action_7']),'literal_action_seven')
        check(matrix_mul(action,delta)==delta,'principal_vector_fixed')
        block=parse_matrix(shown[specification['block_key']])
        quotient=parse_matrix(shown['action_H1_6'])
        check(quotient==matrix_mul(matrix_mul(basis,block),inverse_basis),'literal_full_quotient_binding')
        lhs=matrix_mul(action,section_basis);rhs=matrix_mul(section_basis,block)
        pivot=specification['pivot']
        check(scalar_mul(delta[pivot][0],matrix_sub(lhs,rhs))==matrix_mul(delta,[lhs[pivot]]),
              'actual_principal_quotient_identity')
        for i in range(dimension,6):
            for j in range(6):
                if i!=j:check(not block[i][j],'actual_diagonal_quotient_coordinates')
        core=[row[:dimension] for row in block[:dimension]]
        for e in core:
            for p in e:check(all(isinstance(c,int) for c in p.values()),'integral_core_coefficients')
        actual.append(action);blocks.append(block);cores.append(core)
    for index,scalar in specification['scalar_core'].items():
        check(cores[index]==scalar_mul(parse(scalar),identity(dimension)),'actual_scalar_core_operator')
    comparison=[]
    for index,values in specification['quotient_table'].items():
        entries=[blocks[index][i][i] for i in range(dimension,6)]
        check(entries==[parse(x) for x in values],'actual_quotient_comparison_table')
        comparison.append({'source_index_zero_based':index,'source_label':old[index]['label'],'values':values})
    seed_records=[];seed_rows={}
    for word in seeds:
        u,_=literal_braid(word['negative_braid'])
        check(matrix_mul([u[1]],delta)==[[add({u[0]:1},negative(ONE))]],'literal_seed_fundamental_identity')
        seed_rows[word['index']]=u[1]
        values=matrix_mul([u[1]],core_lift)
        seed_records.append({'index':word['index'],'label':word['label'],'scalar':serialize({u[0]:1}),
                             'core_values':serial_matrix(values)})
        matching=[q for q in symbolic.get('seed_records',[]) if q['index']==word['index']]
        if matching:
            record=matching[0]
            if 'core_values' in record:check(values==parse_matrix(record['core_values']),'producer_seed_values')
            if 'socle_value' in record:check(values==[[parse(record['socle_value'])]],'producer_socle_seed_value')
    extra={}
    if specification['name']=='four_parameter':
        annihilators=[]
        for index,scalar in [(8,'r*s*t'),(9,'1/(t*u)')]:
            first=matrix_sub(cores[index],identity(3))
            second=matrix_sub(cores[index],scalar_mul(parse(scalar),identity(3)))
            product=matrix_mul(matrix_mul(first,first),second)
            check(all(not p for row in product for p in row),'actual_integral_core_annihilator')
            annihilators.append({'source_index':index,'polynomial':'(z-1)^2*(z-'+scalar+')'})
        extra['core_annihilators']=annihilators
    if specification['name']=='deleted_first_two_parameter':
        selected=[1,2,5,7,9];rows=[]
        for index in selected:
            comm=matrix_sub(matrix_mul(blocks[4],blocks[index]),matrix_mul(blocks[index],blocks[4]))
            check(all(not p for row in comm[1:] for p in row) and not comm[0][0],
                  'actual_commutator_image_and_kernel')
            rows.append(comm[0][1:])
        shown_h=parse_matrix([
            ['0','0','0','(s*t+1)*(s*t+s-1)','-1/t**2'],
            ['0','0','1','-(t+1)','0'],
            ['0','s/t','-1/t**2','0','0'],
            ['(t+1)*(s*t-t+1)/(s*t**3)','0','s','0','0'],
            ['-(s-1)/(s*t**2)','0','0','-(s-1)','0']])
        check(rows==scalar_mul(parse('(s-1)*(t-1)'),shown_h),
              'displayed_deleted_first_commutator_rows')
        det=determinant(rows);expected=parse('(s-1)**6*(t-1)**6*(t+1)/t**6')
        check(det==expected,'deleted_first_essential_line_determinant')
        chosen=seed_rows[13]
        check(next(x for x in seed_records if x['index']==13)['scalar']==serialize(parse('1/(s*t)')),
              'chosen_actual_seed_scalar')
        value=matrix_mul([chosen],core_lift)
        check(value==[[parse('s*t-1')]],'chosen_actual_seed_line_value')
        check(matrix_sub(matrix_mul(actual[2],core_lift),scalar_mul(parse('t'),core_lift))
              ==scalar_mul(parse('s*t**2'),delta),
              'displayed_source_two_principal_correction')
        kappa=matrix_mul([chosen],matrix_sub(actual[2],identity(7)))
        next_kappa=matrix_mul(kappa,actual[2])
        check(matrix_mul(kappa,delta)==[[{}]],'chosen_kappa_character_one_cohomology')
        check(matrix_mul(kappa,core_lift)==[[parse('1-s*t')]],'chosen_kappa_line_value')
        check(matrix_mul(next_kappa,core_lift)==[[parse('t*(1-s*t)')]],'chosen_source_kappa_line_value')
        extra={'commutator_anchor':4,'commutator_other_indices':selected,'commutator_rows':serial_matrix(rows),
               'determinant':serialize(det),'determinant_formula':'(s-1)^6*(t-1)^6*(t+1)/t^6',
               'seed_index':13,'seed_label':'cross_0_-1_1','evaluation_source_index':2,
               'kappa_row':serial_matrix(kappa),'source_kappa_row':serial_matrix(next_kappa),
               'kappa_value':'1-s*t','source_kappa_value':'t*(1-s*t)'}
    return {'name':specification['name'],'coefficient_variables':specification['names'],
            'character_exponents':specification['characters'],'principal_pivot_original_index':specification['pivot']+1,
            'quotient_original_indices':[i+1 for i in specification['keep']],
            'symbolic_input':str(symbolic_path),'symbolic_sha256':sha256(symbolic_path.read_bytes()).hexdigest(),
            'symbolic_producer':str(code),'symbolic_producer_sha256':sha256(code.read_bytes()).hexdigest(),
            'core_dimension':dimension,'source_words':11,'seed_words':8,'comparison_table':comparison,
            'seed_records':seed_records,'extra':extra}


def main():
    CHECKS.clear();producer=Path(__file__).resolve();folder=producer.parent
    braid_path=folder/'full_cross_source_stage/marginal_braids.json'
    universal_path=folder/'affine_obstruction_stage_output.json'
    braid_data=json.loads(braid_path.read_text());universal_hash=sha256(universal_path.read_bytes()).hexdigest()
    charts=[verify_chart(specification,braid_data,folder,universal_hash) for specification in chart_specs()]
    result={'status':'PASS_THREE_CHART_FOUR_PARAMETER_LITERAL_WORD_AUDIT',
            'producer_sha256':sha256(producer.read_bytes()).hexdigest(),
            'base_inputs':{str(braid_path):sha256(braid_path.read_bytes()).hexdigest(),str(universal_path):universal_hash},
            'charts':charts,'checks':dict(CHECKS),'check_total':sum(CHECKS.values()),
            'independence':'No producer or algebra-package import. Every chart reconstructs all original words independently with generic affine multiplication over its specified integral Laurent ring. Basis and quotient identities are checked with exact principal-pivot denominator clearing.',
            'scope':'The three specified actual charts and their coefficient identities only. The separate r=1,c!=1 quotient-extension proof is maintained by root and must be combined through its exact maps before a four-parameter image statement is registered.'}
    output=producer.with_name('affine_four_parameter_extension_independent_audit_output.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'checks':result['check_total'],
                      'charts':[{'name':c['name'],'pivot':c['principal_pivot_original_index'],'core_dimension':c['core_dimension']} for c in charts],
                      'literal_source_word_evaluations':33,'literal_seed_word_evaluations':24,
                      'output_sha256':sha256(output.read_bytes()).hexdigest()},indent=2))


if __name__=='__main__':main()


