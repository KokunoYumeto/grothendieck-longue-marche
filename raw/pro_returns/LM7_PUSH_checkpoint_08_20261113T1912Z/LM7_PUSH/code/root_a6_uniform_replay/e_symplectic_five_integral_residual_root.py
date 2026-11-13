#!/usr/bin/env python3
"""Exact integral parity, conjugation, and commutator-image certificate.

All identities are checked over Q in the literal forty-eight evaluations.
The output is a finite list of word and lattice identities; the closure
argument over every modulus prime to six is supplied in the manuscript.
"""
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import json
import time
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from sympy.polys.domains import ZZ
from de_ferrari_a6_source_data import load_data

HERE = Path(__file__).resolve().parent
STEM = 'e_symplectic_five_integral_residual_root'
INPUT = 'e_symplectic_five_integral_probe_root.json'


def enc(matrix):
    return [[str(v) for v in row] for row in sp.Matrix(matrix).tolist()]


def array(matrix):
    return np.array(sp.Matrix(matrix).tolist(), dtype=object)


def lattice_record(matrix):
    matrix = sp.Matrix(matrix)
    denominator = sp.ilcm(*[sp.denom(v) for v in matrix])
    integral = (denominator * matrix).applyfunc(int)
    hnf = hermite_normal_form(integral.T)
    smith = smith_normal_form(hnf, domain=ZZ)
    return {'rank': matrix.rank(), 'common_denominator': str(denominator),
            'integer_lattice_HNF': enc(hnf),
            'integer_lattice_Smith': [abs(int(smith[i,i])) for i in range(smith.cols)]}


class IntegralModel:
    def __init__(self):
        self.d = json.loads((HERE / INPUT).read_text())
        self.source = load_data()
        self.pairs = [(sp.Matrix(a), sp.Matrix(b)) for a,b in self.d['evaluation_pairs']]
        self.letters = {1: np.array([array(a) for a,b in self.pairs], dtype=object),
                        2: np.array([array(b) for a,b in self.pairs], dtype=object),
                        -1: np.array([array(a.inv()) for a,b in self.pairs], dtype=object),
                        -2: np.array([array(b.inv()) for a,b in self.pairs], dtype=object)}
        self.identity8 = np.array([array(sp.eye(4)) for _ in range(8)], dtype=object)
        self.identity48 = np.array([array(sp.eye(4)) for _ in range(48)], dtype=object)
        self.basis = np.array(sp.Matrix(self.d['radical_basis']).tolist(), dtype=object)
        self.coordinates = sp.Matrix(self.d['radical_N_coordinates'])
        self.columns = self.d['radical_pivot_columns']
        self.minor_inverse = array(sp.Matrix(self.basis[:, self.columns]).inv())
        self.theta_index = self.d['theta_coordinate']
        self.lift_coefficients = []
        for a in range(2):
            for b in range(2):
                unit = sp.zeros(2)
                unit[a,b] = 1
                pieces = []
                for rec in self.d['coordinate_decompositions']:
                    pieces.append(array(sum((sp.Matrix(t['T'])*unit*sp.Matrix(t['P'])
                                             for t in rec['blocks']), sp.zeros(4))))
                self.lift_coefficients.append(np.array(pieces, dtype=object))

    @lru_cache(None)
    def free(self, word):
        if not word:
            return self.identity8
        return self.free(word[:-1]) @ self.letters[word[-1]]

    @lru_cache(None)
    def induced(self, bword):
        values, words = [], []
        for rep in self.d['B_coset_section']:
            word = self.source['fword'](rep + list(bword) + self.source['binv'](rep))
            words.append(word)
            values.extend(self.free(tuple(word)))
        return np.array(values, dtype=object), words

    def lift(self, theta):
        out = self.identity48.copy()
        for i, coefficient in enumerate(list(sp.Matrix(theta)-sp.eye(2))):
            if coefficient:
                out += coefficient * self.lift_coefficients[i]
        return out

    def factor(self, bword):
        matrices, fwords = self.induced(tuple(bword))
        theta = sp.Matrix(matrices[self.theta_index][1:3, 1:3])
        assert theta.det() == 1
        radical = self.lift(theta.inv()) @ matrices - self.identity48
        flat = radical.reshape(1,48*16)
        coordinates = flat[:,self.columns] @ self.minor_inverse
        assert np.array_equal(coordinates @ self.basis, flat), ('factorization', bword)
        assert np.array_equal(self.lift(theta) @ (self.identity48+radical), matrices)
        return theta, sp.Matrix(coordinates), fwords


def main():
    start = time.time()
    original = sha256((HERE/INPUT).read_bytes()).hexdigest()
    m = IntegralModel()
    data = m.source
    x, y = data['xword'], data['yword']
    mx, _ = m.induced(tuple(x))
    my, _ = m.induced(tuple(y))
    theta_x = sp.Matrix(mx[m.theta_index][1:3,1:3])
    theta_y = sp.Matrix(my[m.theta_index][1:3,1:3])
    sign_records = []
    for j, record in enumerate(m.d['coordinate_decompositions']):
        for block in record['blocks']:
            t = sp.Matrix(block['T'])
            phases = []
            for matrices, theta in ((mx,theta_x),(my,theta_y)):
                image = sp.Matrix(matrices[j])*t
                signs = [s for s in (1,-1) if image == s*t*theta]
                phases.append(signs)
            sign_records.append({'coordinate': j, 'x_signs': phases[0], 'y_signs': phases[1]})
    sign_rows = [[int(r['x_signs']==[-1]),int(r['y_signs']==[-1])]
                 for r in sign_records if len(r['x_signs'])==len(r['y_signs'])==1]
    sign_matrix = sp.Matrix(sign_rows)
    sign_minor = next(([i,j] for i in range(sign_matrix.rows) for j in range(i)
                       if int(sign_matrix[[i,j],:].det()) % 2), None)
    print(json.dumps({'stage':'standard_signs','records':sign_records,
                      'parity_witness_rows':sign_minor}), flush=True)

    # Conjugation is b*n*b^{-1}; row coordinates transform on the right.
    action_records = {}
    for name, word in (('s',[0]),('r',[1]),('x',x),('y',y)):
        images = []
        source_words = []
        theta_images = []
        for nword in m.d['N_basis_B_words']:
            conjugate = list(word) + nword + data['binv'](word)
            theta, coordinates, _ = m.factor(conjugate)
            images.append(list(coordinates))
            source_words.append(conjugate)
            theta_images.append(enc(theta))
        matrix = sp.Matrix(images)[m.d['radical_basis_N_indices'],:]
        assert m.coordinates * matrix == sp.Matrix(images), name
        assert matrix.det() in (1,-1), (name, matrix.det())
        action_records[name] = {'matrix':enc(matrix),'conjugated_N_words':source_words,
                                'conjugated_N_theta':theta_images,
                                'all_97_coordinate_rows':enc(sp.Matrix(images))}
        print(json.dumps({'stage':'conjugation_action','generator':name,
                          'matrix':enc(matrix),'seconds':round(time.time()-start,3)}), flush=True)
    s,r,ax,ay = [sp.Matrix(action_records[t]['matrix']) for t in ('s','r','x','y')]
    # Right row convention reverses the product of successive conjugators.
    assert s**2 == r**3 == sp.eye(5)
    assert ax**2 == ay**2 == sp.eye(5) and ax*ay == ay*ax
    assert ax == s*r**-1*s*r**-1
    assert ay == r**-1*s*r**-1*s

    # F' is normally generated in F by [x,y]. Since K2 acts trivially on
    # the additive image, these four conjugates give the complete image.
    commutator = (1,2,-1,-2)
    representatives = [(),(1,),(2,),(1,2)]
    derived_records = []
    for word in representatives:
        conjugate = data['freered'](word+commutator+data['finv'](word))
        theta, coordinates, fwords = m.factor(data['to_B'](conjugate))
        derived_records.append({'F_word':conjugate,'B_word':data['to_B'](conjugate),
                                'theta':enc(theta),'coordinates':enc(coordinates),
                                'induced_F_words':fwords})
    derived_rows = sp.Matrix([r['coordinates'][0] for r in derived_records])
    independent = list(derived_rows.T.rref()[1])
    dbasis = derived_rows[independent,:]
    dpivots = list(dbasis.rref()[1])
    dminor = dbasis[:,dpivots]
    dcoordinates = derived_rows[:,dpivots] * dminor.inv()
    assert dcoordinates * dbasis == derived_rows
    restrictions, differences = {}, []
    for name, a in (('x',ax),('y',ay),('s',s),('r',r)):
        image = dbasis*a
        restriction = image[:,dpivots]*dminor.inv()
        assert restriction*dbasis == image
        restrictions[name] = enc(restriction)
        if name in ('x','y'):
            differences.extend((restriction-sp.eye(len(independent))).tolist())
    derived_lattice = lattice_record(dcoordinates)
    stable_commutator = lattice_record(sp.Matrix(differences))

    # The two surviving characters and exact ordinary source powers.
    quotient = dbasis.nullspace()
    annihilator = sp.Matrix.hstack(*quotient)
    assert annihilator.cols == 2 and dbasis*annihilator == sp.zeros(3,2)
    power_records = []
    for letter in (1,2):
        for power in (2,6):
            word = (letter,)*power
            theta, coordinates, fwords = m.factor(data['to_B'](word))
            power_records.append({'F_word':word,'B_word':data['to_B'](word),
                                  'theta':enc(theta),'coordinates':enc(coordinates),
                                  'abelian_characters':enc(coordinates*annihilator),
                                  'induced_F_words':fwords})
    power_character_matrix = sp.Matrix([r['abelian_characters'][0] for r in power_records
                                       if len(r['F_word'])==2])

    result = {'status':'PASS_EXACT_INTEGRAL_ACTION_AND_DERIVED_IMAGE',
              'scope':'Word, parity and lattice identities over Z[1/6]; topological closure is proved separately.',
              'input_sha256':{INPUT:original,
                               'de_ferrari_a6_source_data.py':sha256((HERE/'de_ferrari_a6_source_data.py').read_bytes()).hexdigest()},
              'standard_signs':sign_records,'parity_sign_matrix':enc(sign_matrix),
              'parity_witness_rows':sign_minor,
              'all_24_standard_coordinates_have_signs':len(sign_rows)==24,
              'parity_characters_independent':sign_minor is not None,
              'conjugation_actions':action_records,
              'all_388_conjugated_N_factorizations_verified':True,
              'K2_acts_trivially_on_radical':True,
              'F_derived_normal_generator_conjugates':derived_records,
              'F_derived_radical_rank':len(independent),
              'derived_basis_record_indices':independent,
              'derived_basis':enc(dbasis),'derived_pivot_columns':dpivots,
              'derived_pivot_determinant':str(dminor.det()),
              'derived_generators_in_basis':enc(dcoordinates),
              'derived_lattice':derived_lattice,'derived_action_restrictions':restrictions,
              'stable_commutator_lattice':stable_commutator,
              'abelian_character_annihilator':enc(annihilator),
              'source_power_records':power_records,
              'x2_y2_character_matrix':enc(power_character_matrix),
              'x2_y2_character_determinant':str(power_character_matrix.det()),
              'all_original_inputs_unchanged':sha256((HERE/INPUT).read_bytes()).hexdigest()==original,
              'seconds':round(time.time()-start,3)}
    (HERE/(STEM+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ('status','all_24_standard_coordinates_have_signs',
                     'parity_characters_independent','F_derived_radical_rank','derived_pivot_determinant',
                     'derived_lattice','stable_commutator_lattice','x2_y2_character_determinant','seconds')},indent=2),flush=True)


if __name__ == '__main__':
    main()
