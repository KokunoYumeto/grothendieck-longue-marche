"""Independent actual-word audit of the general nonproduct source identities.

Only Python's standard library is used.  No producer/helper arithmetic is
imported.  All computations below are in a seven-variable integer Laurent
ring, including every full matrix annihilator.
"""
from pathlib import Path
from hashlib import sha256
from collections import Counter
import ast
import json
import sys

sys.setrecursionlimit(30000)
DIM = 7
ZERO = (0,)*DIM
UNITS = [tuple(int(i == j) for i in range(DIM)) for j in range(DIM)]
ONE = {ZERO: 1}
CHECKS = Counter()


def check(condition, name):
    if not condition:
        raise AssertionError(name)
    CHECKS[name] += 1


def plus(*polynomials):
    result = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            result[exponent] = result.get(exponent, 0)+coefficient
    return {e: c for e, c in result.items() if c}


def neg(polynomial):
    return {e: -c for e, c in polynomial.items()}


def shift(polynomial, exponent, coefficient=1):
    return {tuple(a+b for a, b in zip(e, exponent)): coefficient*c
            for e, c in polynomial.items()}


def times(left, right):
    if not left or not right:
        return {}
    if len(left) == 1:
        (e, c), = left.items()
        return shift(right, e, c)
    if len(right) == 1:
        (e, c), = right.items()
        return shift(left, e, c)
    answer = {}
    for e, c in left.items():
        for f, d in right.items():
            key = tuple(a+b for a, b in zip(e, f))
            answer[key] = answer.get(key, 0)+c*d
    return {e: c for e, c in answer.items() if c}


def power(polynomial, degree):
    if degree < 0:
        check(len(polynomial) == 1, 'Laurent_inverse_is_one_monomial')
        (exponent, coefficient), = polynomial.items()
        check(coefficient in (-1, 1), 'Laurent_inverse_has_unit_integer_coefficient')
        return {tuple(degree*a for a in exponent): coefficient**(-degree)}
    answer = ONE
    while degree:
        if degree & 1:
            answer = times(answer, polynomial)
        polynomial = times(polynomial, polynomial)
        degree >>= 1
    return answer


def integer(node):
    if isinstance(node, ast.Constant) and type(node.value) is int:
        return node.value
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -integer(node.operand)
    raise ValueError('Noninteger exponent')


def parse(text, names=None):
    if names is None:
        names = {name: {UNITS[i]: 1} for i, name in enumerate(['r','h','t','u','v','w','z'])}
        names['s'] = {(-1,1,-1,-1,-1,-1,-1): 1}
    def visit(node):
        if isinstance(node, ast.Constant) and type(node.value) is int:
            return {} if node.value == 0 else {ZERO: node.value}
        if isinstance(node, ast.Name):
            return names[node.id]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return neg(visit(node.operand))
        if isinstance(node, ast.BinOp):
            if isinstance(node.op, ast.Pow):
                return power(visit(node.left), integer(node.right))
            left, right = visit(node.left), visit(node.right)
            if isinstance(node.op, ast.Add):
                return plus(left, right)
            if isinstance(node.op, ast.Sub):
                return plus(left, neg(right))
            if isinstance(node.op, ast.Mult):
                return times(left, right)
            if isinstance(node.op, ast.Div):
                return times(left, power(right, -1))
        raise ValueError(ast.dump(node))
    return visit(ast.parse(text, mode='eval').body)


def unpack(serial):
    answer = {}
    for coefficient, exponent in serial:
        e = tuple(exponent)
        check(type(coefficient) is int and coefficient != 0 and len(e) == DIM,
              'serialized_nonzero_integer_Laurent_term')
        check(e not in answer, 'serialized_distinct_monomials')
        answer[e] = coefficient
    return answer


def unpack_matrix(serial):
    return [[unpack(entry) for entry in row] for row in serial]


def monomial_map(poly, images):
    answer = {}
    for exponent, coefficient in poly.items():
        e = [0]*DIM
        c = coefficient
        for degree, (sign, image) in zip(exponent, images):
            c *= sign**abs(degree)
            e = [a+degree*b for a, b in zip(e, image)]
        key = tuple(e)
        answer[key] = answer.get(key, 0)+c
    return {e: c for e, c in answer.items() if c}


H_IMAGES = [(1, UNITS[i]) for i in range(DIM)]
H_IMAGES[1] = (1, (-1,1,-1,-1,-1,-1,-1))
ORIGINAL_IMAGES = [(1, UNITS[i]) for i in range(DIM)]
ORIGINAL_IMAGES[1] = (1, (1,1,1,1,1,1,1))


def to_h(poly):
    return monomial_map(poly, H_IMAGES)


def from_h(poly):
    return monomial_map(poly, ORIGINAL_IMAGES)


def specialize(poly, substitutions):
    images = [(1, UNITS[i]) for i in range(DIM)]
    for index, value in substitutions.items():
        check(len(value) == 1, 'specialization_is_explicit_unit_monomial')
        (exponent, coefficient), = value.items()
        check(coefficient in (-1, 1), 'specialization_unit_sign')
        images[index] = (coefficient, exponent)
    return monomial_map(poly, images)


def eye(size):
    return [[ONE if i == j else {} for j in range(size)] for i in range(size)]


def mm(left, right):
    assert len(left[0]) == len(right)
    return [[plus(*(times(left[i][k], right[k][j])
                    for k in range(len(right)) if left[i][k] and right[k][j]))
             for j in range(len(right[0]))] for i in range(len(left))]


def scale(value, matrix):
    return [[times(value, entry) for entry in row] for row in matrix]


def matrix_plus(left, right):
    return [[plus(x, y) for x, y in zip(a, b)] for a, b in zip(left, right)]


def matrix_minus(left, right):
    return matrix_plus(left, scale({ZERO: -1}, right))


def shifted(matrix, value):
    return matrix_minus(matrix, scale(value, eye(len(matrix))))


def matrix_check(left, right, name):
    check(len(left) == len(right) and all(len(a) == len(b) for a, b in zip(left, right)),
          name+'_dimensions')
    for i, (a, b) in enumerate(zip(left, right)):
        for j, (x, y) in enumerate(zip(a, b)):
            check(x == y, name+'_entry_%d_%d'%(i,j))


def group_product(left, right):
    a, da = left
    b, db = right
    return tuple(x+y for x, y in zip(a, b)), [plus(x, shift(y, a)) for x, y in zip(da, db)]


def group_inverse(value):
    a, da = value
    b = tuple(-x for x in a)
    return b, [shift(x, b, -1) for x in da]


def literal_braid(word):
    identity = (ZERO, [{} for _ in range(DIM)])
    meridians = [(UNITS[i], [ONE if i == j else {} for j in range(DIM)]) for i in range(DIM)]+[identity]
    conjugators = [identity for _ in range(DIM+1)]
    labels = list(range(DIM+1))
    for letter in word:
        i = abs(letter)-1
        check(0 <= i < DIM, 'literal_eight_strand_letter')
        x, y = meridians[i], meridians[i+1]
        cx, cy = conjugators[i], conjugators[i+1]
        if letter > 0:
            meridians[i:i+2] = [group_product(group_product(x,y),group_inverse(x)), x]
            conjugators[i:i+2] = [group_product(x,cy), cx]
        else:
            meridians[i:i+2] = [y, group_product(group_product(group_inverse(y),x),y)]
            conjugators[i:i+2] = [cy, group_product(group_inverse(y),cx)]
        labels[i], labels[i+1] = labels[i+1], labels[i]
    check(labels == list(range(DIM+1)), 'literal_pure_label_permutation')
    check([x[0] for x in meridians] == UNITS+[ZERO], 'literal_original_characters_preserved')
    check(meridians[-1] == identity, 'literal_erased_eighth_meridian')
    decoration = group_inverse(conjugators[-1])
    action = [group_product(group_product(decoration,x),group_inverse(decoration))[1]
              for x in meridians[:DIM]]
    pure = [x[1] for x in meridians[:DIM]]
    return decoration, action, pure


def parsed_row(strings):
    return [parse(x) for x in strings]


def parsed_column(strings):
    return [[parse(x)] for x in strings]


def polynomial_product(matrix, roots, name):
    result = eye(len(matrix))
    counts = []
    for i, root in enumerate(roots):
        result = mm(result, shifted(matrix, parse(root)))
        counts.append(sum(len(p) for row in result for p in row))
        print(json.dumps({'stage':name,'factor':i+1,'monomials':counts[-1]}), flush=True)
    return result, counts


def main():
    script = Path(__file__).resolve()
    folder = script.parent
    output_names = [
        'affine_obstruction_stage_output.json',
        'affine_nonproduct_boundary_quotient_stage_output.json',
        'affine_nonproduct_source_zero_stage_output.json',
        'affine_nonproduct_retained_source_annihilators_stage_output.json',
        'affine_nonproduct_general_moving_rows_stage_output.json',
        'affine_nonproduct_rank_one_special_roots_stage_output.json',
        'affine_nonproduct_q_special_rows_stage_output.json',
        'affine_nonproduct_same_rh_row_cover_stage_output.json']
    names = ['full_cross_source_stage/marginal_braids.json']+output_names
    names += [name.replace('_output.json','.py') for name in output_names]
    names += ['affine_four_parameter_extension_independent_audit.py','affine_full_product_one_independent_audit.py']
    paths = {Path(name).name:folder/name for name in names}
    hashes = {name:sha256(path.read_bytes()).hexdigest() for name,path in paths.items()}
    records = {name:json.loads(paths[name].read_text()) for name in output_names}
    for name, data in records.items():
        check(data['producer_sha256'] == hashes[name.replace('_output.json','.py')],
              'frozen_producer_binding_'+name)
        for old_path, expected in data.get('inputs',{}).items():
            check(hashes[Path(old_path).name] == expected, 'frozen_input_binding_'+name)
    universal = records[output_names[0]]
    check(universal['source_sha256'] == hashes['marginal_braids.json'], 'universal_original_braid_binding')
    boundary, outer, retained, moving, special_columns, special_rows, cover = [
        records[name] for name in output_names[1:]]
    braid_records = [x for x in json.loads(paths['marginal_braids.json'].read_text())['records'] if x['index'] < 11]
    old_records = [x for x in universal['records'] if x['index'] < 11]
    check([x['index'] for x in braid_records] == list(range(11)), 'all_eleven_actual_old_source_indices')
    for generator in UNITS:
        check(from_h(to_h({generator:1})) == {generator:1}, 'forward_inverse_coefficient_generator')
        check(to_h(from_h({generator:1})) == {generator:1}, 'inverse_forward_coefficient_generator')
        check(from_h(to_h({tuple(-x for x in generator):1})) == {tuple(-x for x in generator):1},
              'forward_inverse_negative_generator')
    chars = [parse(x) for x in ['r','s','t','u','v','w','z']]
    delta = [[plus(x,neg(ONE))] for x in chars]
    D = [[ONE]]
    for value in chars[:-1]:
        D[0].append(times(D[0][-1],value))
    hm1 = parse('h-1')
    Q = matrix_minus(scale(hm1,eye(7)),mm(delta,D))
    J = [[neg(D[0][j+1]) for j in range(6)]]+eye(6)
    E = [[{}]+row for row in eye(6)]
    e1 = [[ONE]]+[[{}] for _ in range(6)]
    matrix_check(mm(D,delta),[[hm1]],'boundary_principal_pairing')
    matrix_check(mm(Q,delta),[[{}] for _ in range(7)],'cleared_projection_principal_kernel')
    matrix_check(mm(D,Q),[[{}]*7],'cleared_projection_boundary_kernel')
    matrix_check(mm(Q,Q),scale(hm1,Q),'cleared_projection_square')
    matrix_check(mm(D,J),[[{}]*6],'boundary_section_kernel')
    matrix_check(mm(E,J),eye(6),'boundary_left_inverse')
    matrix_check(mm(J,E),matrix_minus(eye(7),mm(e1,D)),'boundary_right_inverse')
    matrix_check(mm(Q,J),scale(hm1,J),'cleared_principal_section')
    matrix_check(mm(mm(J,E),Q),Q,'cleared_quotient_inverse')
    for field, actual in [('boundary_row',D),('principal_vector',delta),('cleared_projection',Q),
                          ('basis_inclusion',J),('basis_projection',E)]:
        expected = [[to_h(p) for p in row] for row in unpack_matrix(boundary[field])]
        matrix_check(actual,expected,'recorded_'+field)
    scalar_table = ['1','1','r*t','1','1','1','1/u**2','1/(h*t)','1/v**2','1/w**2','1/z**2']
    matrices = {}
    for word, old, expected in zip(braid_records,old_records,boundary['records']):
        index = word['index']
        check(index == old['index'] == expected['index'] and word['label'] == old['label'] == expected['label'],
              'actual_old_source_identity')
        deco, original_action, original_pure = literal_braid(word['negative_braid'])
        check(list(deco[0]) == old['u_character'], 'actual_decoration_character')
        matrix_check([deco[1]],[parsed for parsed in [[unpack(x) for x in old['u_derivation_row']]]],
                     'actual_decoration_derivative')
        matrix_check(original_action,unpack_matrix(old['action_matrix']),'actual_seven_coordinate_decorated_action')
        for matrix in [original_action,original_pure,[deco[1]]]:
            for row in matrix:
                for poly in row:
                    check(from_h(to_h(poly)) == poly, 'coefficient_transport_both_directions')
        A = [[to_h(p) for p in row] for row in original_action]
        M = [[to_h(p) for p in row] for row in original_pure]
        a = [[to_h(p) for p in deco[1]]]
        scalar = to_h({deco[0]:1})
        check(scalar == parse(scalar_table[index]), 'exact_source_scalar_table')
        check(scalar == to_h(unpack(expected['decoration_character'])), 'recorded_source_scalar')
        U = matrix_plus(A,mm(delta,a))
        matrix_check(U,scale(scalar,M),'actual_decoration_removal')
        matrix_check(mm(A,delta),delta,'actual_principal_line_fixed')
        matrix_check(mm(M,delta),delta,'pure_principal_line_fixed')
        matrix_check(mm(a,delta),[[plus(scalar,neg(ONE))]],'decoration_principal_identity')
        matrix_check(mm(D,M),D,'literal_pure_boundary_fixed')
        matrix_check(mm(D,U),scale(scalar,D),'corrected_boundary_scalar')
        matrix_check(mm(U,delta),scale(scalar,delta),'corrected_principal_scalar')
        matrix_check(mm(Q,A),mm(U,Q),'full_cleared_quotient_intertwiner')
        T = mm(mm(E,U),J)
        matrix_check(mm(U,J),mm(J,T),'full_six_coordinate_intertwiner')
        matrix_check(T,[[to_h(p) for p in row] for row in unpack_matrix(expected['boundary_quotient_matrix_6'])],
                     'actual_recorded_boundary_operator')
        matrices[index] = T
        print(json.dumps({'stage':'literal_source_complete','source':index}),flush=True)
    q = [parsed_row(outer['row_q'])]
    a = parsed_column(outer['column_a'])
    d = parse('r/h')
    matrix_check(shifted(matrices[0],d),mm(a,q),'source_zero_outer_factor')
    matrix_check(mm(q,a),[[parse('1-r/h')]],'source_zero_outer_scalar')
    matrix_check(mm(q,matrices[0]),q,'source_zero_left_fixed')
    matrix_check(mm(matrices[0],a),a,'source_zero_right_fixed')
    matrix_check(mm(shifted(matrices[0],d),shifted(matrices[0],ONE)),
                 [[{}]*6 for _ in range(6)],'source_zero_full_annihilator')
    check(plus(*(matrices[0][i][i] for i in range(6))) == parse('5*r/h+1'),'source_zero_trace')
    check(q[0][0] == parse('r*t*v') and q[0][1] == parse('r*r*s*t*v'),'two_retained_q_pivots')
    check(a[5][0] == parse('(z-1)*(h+w-1)/(h*u*z)'),'column_a_last_factor')
    check(a[4][0] == parse('-(w-1)*(h*(h+w-1)*(z-1)-w*z)/(h*h*u*z)'),
          'column_a_penultimate_full_factor')
    for index,subs,formula in [
        (4,{6:ONE},'w*(w-1)/(h*h*u)'),
        (3,{6:ONE,5:ONE},'(v-1)/(h*h*u)'),
        (2,{6:ONE,5:ONE,4:ONE},'(u-1)/u')]:
        check(specialize(a[index][0],subs) == parse(formula),'column_a_nonzero_ordered_cover')
    # Preserve the historical failed trials without using them.
    check(boundary['records'][0]['source_zero_r_h_quadratic_zero'] is False
          and boundary['records'][0]['source_zero_trace_equals_5r_plus_h'] is False,
          'historical_failed_source_zero_flags_preserved')
    retained_specs = {2:['r*t','r*t/(u*v)','r*t/(w*z)','1/(r*t)'],
                      7:['t/h','t/(h*u*v)','t/(h*w*z)','h/t']}
    for record in retained['records']:
        index = record['index']; roots = retained_specs[index]
        check(record['roots'] == roots,'retained_exact_root_order')
        product,counts = polynomial_product(matrices[index],roots,'retained_'+str(index))
        matrix_check(product,[[{}]*6 for _ in range(6)],'retained_full_degree_four_annihilator')
        check(counts == record['ordered_product_monomial_counts'],'retained_ordered_monomial_counts')
        trace = plus(*(matrices[index][i][i] for i in range(6)))
        check(trace == plus(times(parse('3'),parse(roots[0])),*(parse(x) for x in roots[1:])),
              'retained_trace_multiplicities_3_1_1_1')
    moving_specs = {
        1:(['1','1/(r*u)**2','1/(v*w)'],'1/(t*z)'),
        3:(['1','1/(r*v)**2','1/(u*z)'],'1/(t*w)'),
        4:(['1','1/(r*w)**2','1/(v*z)'],'1/(t*u)'),
        5:(['1','1/(r*z)**2','1/(u*w)'],'1/(t*v)'),
        6:(['1','(h/u)**2','1/(v*w)'],'1/(t*z)'),
        8:(['1','(h/v)**2','1/(u*z)'],'1/(t*w)'),
        9:(['1','(h/w)**2','1/(v*z)'],'1/(t*u)'),
        10:(['1','(h/z)**2','1/(u*w)'],'1/(t*v)')}
    moving_rows = {}
    for record in moving['records']:
        index = record['index']; bases,b = moving_specs[index]
        check(record['base_roots'] == bases and record['moving_root'] == b,'moving_exact_source_root_table')
        operator,_ = polynomial_product(matrices[index],bases,'moving_'+str(index))
        product = mm(operator,shifted(matrices[index],parse(b)))
        matrix_check(product,[[{}]*6 for _ in range(6)],'moving_full_degree_four_annihilator')
        row = [parsed_row(record['row_q'])]
        tau = ONE
        for root in bases:
            tau = times(tau,plus(parse(b),neg(parse(root))))
        check(tau == parse(record['trace_product']),'moving_exact_root_difference_product')
        check(plus(*(operator[i][i] for i in range(6))) == tau,'moving_polynomial_trace')
        matrix_check(mm(row,matrices[index]),scale(parse(b),row),'moving_direct_left_eigenrow')
        matrix_check(mm(row,operator),scale(tau,row),'moving_polynomial_left_row_evaluation')
        check(mm(row,a)[0][0] == parse(cover['pairings_q_l_a'][str(index)]),'moving_exact_q_l_a_pairing')
        moving_rows[index] = row
    paired_cover = [
        (4,{},'u*w*z*(h-1)*(t-1)*(u-1)'),
        (9,{},'-u*w*z*(h-1)*(t-1)*(u-1)/h'),
        (1,{3:ONE},'v*w*z*(h-1)*(t-1)*(z-1)/h'),
        (6,{3:ONE},'w*z*(h-1)*(t-1)*(z-1)'),
        (3,{3:ONE,6:ONE},'w*(h-1)*(t-1)*(w-1)/h'),
        (8,{3:ONE,6:ONE},'v*w*w*(h-1)*(t-1)*(w-1)/(h*h)'),
        (5,{3:ONE,6:ONE,5:ONE},'-(h-1)*(t-1)*(v-1)/h'),
        (10,{3:ONE,6:ONE,5:ONE},'(h-1)*(t-1)*(v-1)/h')]
    for index,subs,formula in paired_cover:
        check(specialize(mm(moving_rows[index],a)[0][0],subs) == parse(formula),
              'paired_positive_negative_nonzero_cover')
    special_specs = {10:(['1','1/(u*w)','1/(t*v)'],'(h/z)**2'),
                     9:(['1','1/(v*z)','1/(t*u)'],'(h/w)**2'),
                     8:(['1','1/(u*z)','1/(t*w)'],'(h/v)**2'),
                     6:(['1','1/(v*w)','1/(t*z)'],'(h/u)**2')}
    column_images = {}
    for record in special_columns['records']:
        index = record['index']; roots,root = special_specs[index]
        check(record['base_roots'] == roots and record['special_root'] == root,'special_column_exact_root_table')
        image = a
        counts = []
        for value in roots:
            image = mm(shifted(matrices[index],parse(value)),image)
            counts.append(sum(len(x[0]) for x in image))
        matrix_check(image,[[unpack(p)] for p in record['image']],'special_column_complete_polynomial_image')
        matrix_check(image,parsed_column(record['image_factored']),'special_column_complete_factored_image')
        matrix_check(mm(matrices[index],image),scale(parse(root),image),'special_column_direct_eigenvector')
        check(counts == record['ordered_image_monomial_counts'],'special_column_ordered_monomial_counts')
        column_images[index] = image
    special_cover = [
        (9,4,{},'(h+w)*(w-1)*(h*h*t*u-w*w)*(h*h*v*z-w*w)*(h*w*z-h*w+h-w*z)/(h*h*t*u*u*v*w**5*z*z)'),
        (10,5,{5:ONE},'-(-h+z)*(h+z)*(z-1)*(-h*h*u+z*z)*(-h*h*t*v+z*z)/(t*u*u*v*z**7)'),
        (8,3,{5:ONE,6:ONE},'-(-h+v)*(h+v)*(v-1)*(h*h*t-v*v)*(h*h*u-v*v)/(h*h*t*u*u*v**6)'),
        (6,2,{5:ONE,6:ONE,4:ONE},'(-h+u)**2*(h+u)**2*(u-1)*(h*h*t-u*u)/(t*u**7)')]
    for index,coordinate,subs,formula in special_cover:
        check(specialize(column_images[index][coordinate][0],subs) == parse(formula),
              'nonzero_rank_one_special_column_cover')
    primitive_specs = {
        10:['0','0','0','0','0','1'],
        9:['0','0','0','0','1','w-1'],
        8:['0','0','0','-1','1-v','-w*(v-1)'],
        6:['0','0','v*w*z','-h*(u-1)','-h*(u-1)*(v+z-1)',
           '-(u-1)*(h*v*w+h*w*z-h*w-h*z-w*z)']}
    for record in special_rows['records']:
        index = record['index']; roots,root = special_specs[index]
        check(record['roots_removed'] == roots and record['special_root'] == root,'special_row_exact_root_table')
        primitive = [parsed_row(primitive_specs[index])]
        matrix_check(primitive,[parsed_row(record['primitive_row'])],'special_primitive_printed_row')
        image = q
        for value in roots:
            image = mm(image,shifted(matrices[index],parse(value)))
        matrix_check(image,scale(parse(record['q_polynomial_orbit_factor']),primitive),'special_row_undivided_orbit_factor')
        matrix_check(mm(primitive,matrices[index]),scale(parse(root),primitive),'special_primitive_direct_eigenrow')
    result = {
        'status':'PASS_INDEPENDENT_GENERAL_NONPRODUCT_LITERAL_SOURCE_AUDIT',
        'checker':{'path':script.name,'sha256':sha256(script.read_bytes()).hexdigest()},
        'input_bindings':[{'path':name,'bytes':(folder/name).stat().st_size,
                           'sha256':sha256((folder/name).read_bytes()).hexdigest()} for name in names],
        'coefficient_variables':['r','h','t','u','v','w','z'],
        'original_character_chart':['r','h/(r*t*u*v*w*z)','t','u','v','w','z'],
        'literal_old_sources':11,'retained_full_annihilators':2,'moving_full_annihilators':8,
        'special_column_images':4,'special_primitive_rows':4,
        'source_zero_outer_factor':'T0-(r/h)I=a*q; q*a=1-r/h; q*T0=q; T0*a=a',
        'checks':dict(sorted(CHECKS.items())),'check_count':sum(CHECKS.values()),
        'arithmetic':'Independent sparse integer Laurent arithmetic and generic group multiplication; standard-library imports only.',
        'scope':'All eleven literal original decorated actions, complete cleared boundary quotient and inverse maps, source-zero identities/nonzero cover, full retained and moving degree-four annihilators, direct moving rows, paired nonzero cover, complete special polynomial images and primitive special eigenrows. Fixed-field and invariant-kernel arguments are supplied separately in the written proof.'}
    output = script.with_name('affine_nonproduct_general_source_independent_audit_output.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'checks':result['check_count'],
                      'output_sha256':sha256(output.read_bytes()).hexdigest()},indent=2),flush=True)


if __name__ == '__main__':
    main()
