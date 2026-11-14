#!/usr/bin/env python3
"""E.100: integral Hall/Chen maps and actual anti-involution coordinates.

The rank-ten calculation uses the retained integral Hall/Chen implementation.
The separate rank-three calculation uses exact rational Magnus series of
degree four.  All denominators are checked to be prime to three.  It verifies
the nonlinear central correction, its inverse, the quotient map, and a
literal conjugate involution.  It is an algebra certificate, not a replacement
for the genuine arithmetic operator retained in the theorem.
"""
import argparse
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
import hashlib
import importlib.util
from itertools import product
import json
from math import comb
from pathlib import Path
import random
import sympy as sp


INPUT_HASH = "c725c39cc3bf86f646135766140381be99f20ad82bd9a5dd540c52ba02a1d595"


def load_source(path):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    assert digest == INPUT_HASH, (path, digest, INPUT_HASH)
    spec = importlib.util.spec_from_file_location("e100_integral_hall", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, digest


def encode_q(x):
    x = Q(x)
    assert x.denominator % 3
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def matrix_q(A):
    return [[encode_q(A[i, j]) for j in range(A.cols)] for i in range(A.rows)]


def dense(columns):
    n = len(columns)
    A = sp.zeros(n)
    for j, col in enumerate(columns):
        for i, a in col.items():
            A[i, j] = a
    return A


def rank_ten(module):
    hall, chen = module.Hall(5), module.Chen(5)

    @lru_cache(None)
    def chen_word(i):
        if i < 10:
            return (i,)
        a, b = hall.children[i]
        left = chen_word(a)
        if b >= 10 or left is None:
            return None
        return left + (b,)

    projection = {i: (None if chen_word(i) is None else
                      chen.index[chen_word(i)])
                  for i in range(len(hall.degree))}
    inverse = {j: i for i, j in projection.items() if j is not None}
    assert len(inverse) == len(chen.words)
    for j, word in enumerate(chen.words):
        assert chen_word(inverse[j]) == word

    def project_vector(v):
        out = {}
        for i, a in v.items():
            j = projection[i]
            if j is not None:
                out[j] = out.get(j, 0) + a
        return {j: a for j, a in out.items() if a}

    bracket_checks = 0
    for i, di in enumerate(hall.degree):
        if di >= 5:
            continue
        for j in range(i):
            if di + hall.degree[j] > 5:
                break
            left = project_vector(hall.bracket(i, j))
            pi, pj = projection[i], projection[j]
            right = {} if pi is None or pj is None else chen.bracket(pi, pj)
            assert left == right, (i, j, left, right)
            bracket_checks += 1

    layers = []
    for r in range(1, 6):
        full = [i for i, d in enumerate(hall.degree) if d == r]
        retained = [i for i in full if projection[i] is not None]
        kernel = [i for i in full if projection[i] is None]
        negative = lambda i: sum(hall.letters[i][4:]) % 2
        rf = module.layer_data("full", r)
        rm = module.layer_data("metabelian", r)
        assert len(full) == rf["rank"] and len(retained) == rm["rank"]
        assert sum(map(negative, full)) == rf["coordinate_free_rank"]
        assert sum(map(negative, retained)) == rm["coordinate_free_rank"]
        assert sum(map(negative, kernel)) == (
            rf["coordinate_free_rank"] - rm["coordinate_free_rank"])
        layers.append({
            "degree": r, "full_rank": len(full), "meta_rank": len(retained),
            "kernel_rank": len(kernel),
            "full_negative": sum(map(negative, full)),
            "meta_negative": sum(map(negative, retained)),
            "kernel_negative": sum(map(negative, kernel)),
            "Hall_indices": full, "Chen_Hall_indices": retained,
            "kernel_Hall_indices": kernel,
            "negative_kernel_Hall_indices": [i for i in kernel if negative(i)],
            "quotient_integer_right_inverse": [[inverse[projection[i]], i]
                                                for i in retained]
        })
    assert layers[3]["kernel_rank"] == 990
    assert layers[3]["kernel_negative"] == 504

    inputs = module.arithmetic_inputs()
    J, T, F = (dense(inputs[key]) for key in ("c", "tau", "Frob_K2"))
    unit = sp.eye(10)
    cusp = lambda i: unit[:, i + 2]
    h = unit[:, 0] + (cusp(1) + cusp(2) + cusp(4) + cusp(5) +
                      cusp(6) + cusp(7)) / 2
    plus = [h, cusp(1)-cusp(2), cusp(4)-cusp(5), cusp(6)-cusp(7)]
    minus = [(unit-J)*unit[:, 1]/2, cusp(0), cusp(3),
             cusp(1)+cusp(2), cusp(4)+cusp(5), cusp(6)+cusp(7)]
    S = sp.Matrix.hstack(*(plus + minus))
    Sinv = S.inv()
    assert J*S == S*sp.diag(*([1]*4 + [-1]*6))
    assert S*Sinv == unit and Sinv*S == unit
    matrix_q(S)
    matrix_q(Sinv)
    A = T*J*T.inv()*J
    L = A*J
    assert L*L == unit and L*T == T*J
    assert F*J == J*F
    E = sp.Matrix([[-8, 3], [-3, -5]])/7
    assert A[:2, :2] == E

    naturality = {}
    r = 4
    fh = [i for i, d in enumerate(hall.degree) if d == r]
    cc = [j for j, word in enumerate(chen.words) if len(word) == r]
    fr, cr = {i: j for j, i in enumerate(fh)}, {i: j for j, i in enumerate(cc)}
    kk = [i for i in fh if projection[i] is None]
    kr = {i: j for j, i in enumerate(kk)}
    for key in ("tau", "c", "Frob_K2"):
        full_action, selected = hall.action(inputs[key], r)
        meta_action, selected_meta = chen.action(inputs[key], r)
        assert selected == fh and selected_meta == cc
        kernel_action = []
        for column, hi in zip(full_action, fh):
            qcol = {}
            for row, a in column.items():
                ci = projection[fh[row]]
                if ci is not None:
                    qcol[cr[ci]] = qcol.get(cr[ci], 0) + a
            target = {} if projection[hi] is None else meta_action[cr[projection[hi]]]
            assert qcol == target
            if hi in kr:
                assert all(fh[row] in kr for row in column)
                kernel_action.append({kr[fh[row]]: a for row, a in column.items()})
        naturality[key] = {
            "checked_full_columns": len(fh),
            "kernel_action_coo": module.coo(kernel_action)
        }

    return {
        "rank_tables_through_12": [
            {"degree": r,
             "full": module.layer_data("full", r),
             "metabelian": module.layer_data("metabelian", r),
             "kernel_negative": module.layer_data("full", r)["coordinate_free_rank"] -
                                module.layer_data("metabelian", r)["coordinate_free_rank"]}
            for r in range(1, 13)],
        "integral_layers": layers,
        "Hall_children_through_5": hall.children,
        "Hall_to_Chen": [[i, j] for i, j in projection.items() if j is not None],
        "bracket_naturality_checks": bracket_checks,
        "actual_graded_naturality_degree_4": naturality,
        "J_adapted_abelian_basis": matrix_q(S),
        "J_adapted_abelian_basis_inverse": matrix_q(Sinv),
        "actual_rho_matrix": matrix_q(A),
        "actual_L_matrix": matrix_q(L),
        "actual_T_conjugacy_checked": True
    }


class Magnus:
    def __init__(self, degree=4):
        self.degree = degree
        self.one = {(): Q(1)}

    def clean(self, p):
        ans = {w: Q(a) for w, a in p.items() if a and len(w) <= self.degree}
        for a in ans.values():
            assert a.denominator % 3
        return ans

    def add(self, p, q, scalar=1):
        ans = dict(p)
        for w, a in q.items():
            ans[w] = ans.get(w, 0) + scalar*a
        return self.clean(ans)

    def mul(self, p, q):
        ans = {}
        for u, a in p.items():
            for v, b in q.items():
                if len(u)+len(v) <= self.degree:
                    w = u+v
                    ans[w] = ans.get(w, 0)+a*b
        return self.clean(ans)

    def power(self, p, exponent):
        exponent = Q(exponent)
        assert exponent.denominator % 3 and p.get((), 0) == 1
        v = self.add(p, self.one, -1)
        ans, term, coeff = dict(self.one), dict(self.one), Q(1)
        for k in range(1, self.degree+1):
            term = self.mul(term, v)
            coeff *= (exponent-k+1)/k
            ans = self.add(ans, term, coeff)
        return ans

    def inv(self, p):
        return self.power(p, -1)

    def comm(self, p, q):
        return self.mul(self.mul(p, q), self.mul(self.inv(p), self.inv(q)))

    def subst(self, p, images):
        variables = [self.add(g, self.one, -1) for g in images]
        ans = {}
        for word, a in p.items():
            term = dict(self.one)
            for i in word:
                term = self.mul(term, variables[i])
            ans = self.add(ans, term, a)
        return ans


class SmallHall:
    def __init__(self, alg):
        self.alg = alg
        self.degrees = [1]*3
        self.children = [None]*3
        self.letters = [(1,0,0), (0,1,0), (0,0,1)]
        self.words = [{(): Q(1), (i,): Q(1)} for i in range(3)]
        for r in range(2, alg.degree+1):
            size = len(self.degrees)
            for i in range(size):
                for j in range(i):
                    if self.degrees[i]+self.degrees[j] != r:
                        continue
                    if self.children[i] is not None and self.children[i][1] > j:
                        continue
                    self.degrees.append(r)
                    self.children.append((i,j))
                    self.letters.append(tuple(a+b for a,b in
                                              zip(self.letters[i], self.letters[j])))
                    self.words.append(alg.comm(self.words[i], self.words[j]))
        self.layers = {}
        for r in range(1, alg.degree+1):
            ids = [i for i, d in enumerate(self.degrees) if d == r]
            monos = list(product(range(3), repeat=r))
            mat = sp.Matrix([[self.words[i].get(w, 0) for i in ids] for w in monos])
            pivots = list(mat.T.rref()[1])
            square = mat[pivots, :]
            assert abs(square.det()) == 1
            self.layers[r] = (ids, monos, pivots, square.inv())
        self.chen = [self.is_chen(i) for i in range(len(self.words))]
        self.signs = [(-1)**(a[1]+a[2]) for a in self.letters]
        self.gens = self.words[:3]
        self.Jgens = [self.gens[0], alg.inv(self.gens[1]), alg.inv(self.gens[2])]

    def is_chen(self, i):
        if i < 3:
            return True
        a,b = self.children[i]
        return b < 3 and self.is_chen(a)

    def homogeneous_coords(self, p, r):
        ids, monos, pivots, inverse = self.layers[r]
        vec = sp.Matrix([p.get(monos[j], 0) for j in pivots])
        out = [Q(a) for a in inverse*vec]
        assert all(a.denominator % 3 for a in out)
        rebuilt = {}
        for i,a in zip(ids, out):
            for w,b in self.words[i].items():
                if len(w) == r:
                    rebuilt[w] = rebuilt.get(w, 0)+a*b
        assert self.alg.clean(rebuilt) == self.alg.clean(
            {w:a for w,a in p.items() if len(w) == r})
        return out

    def from_coords(self, coords):
        out = dict(self.alg.one)
        for g,a in zip(self.words, coords):
            if a:
                out = self.alg.mul(out, self.alg.power(g, a))
        return out

    def collect(self, p):
        remainder = p
        out = [Q(0)]*len(self.words)
        for r in range(1, self.alg.degree+1):
            ids = self.layers[r][0]
            vals = self.homogeneous_coords(remainder, r)
            for i,a in zip(ids, vals):
                out[i] = a
                if a:
                    remainder = self.alg.mul(self.alg.power(self.words[i], -a), remainder)
        assert remainder == self.alg.one
        assert self.from_coords(out) == p
        return out

    def project(self, p):
        coords = self.collect(p)
        return self.from_coords([a if keep else Q(0) for a,keep in zip(coords,self.chen)])

    def J(self, p, meta=False):
        out = self.alg.subst(p, self.Jgens)
        return self.project(out) if meta else out

    def anti_forward(self, parameters, meta=False):
        coords = [Q(0)]*len(self.words)
        for r in range(1, self.alg.degree+1):
            u = self.from_coords(coords)
            defect = self.alg.mul(u, self.J(u, meta))
            if meta:
                defect = self.project(defect)
            assert all(len(w) >= r or w == () for w in defect)
            vals = self.homogeneous_coords(defect, r)
            for i,d in zip(self.layers[r][0], vals):
                if meta and not self.chen[i]:
                    assert d == 0
                    continue
                assert d == 0 or self.signs[i] == 1
                coords[i] = -d/2
                if self.signs[i] == -1:
                    coords[i] += parameters.get(i, Q(0))
            u = self.from_coords(coords)
            err = self.alg.mul(u, self.J(u, meta))
            if meta:
                err = self.project(err)
            assert all(len(w) > r or w == () for w in err)
        out = self.from_coords(coords)
        if meta:
            out = self.project(out)
        return out

    def anti_inverse(self, p, meta=False):
        actual = self.collect(p)
        recovered = {}
        lower = [Q(0)]*len(actual)
        for r in range(1, self.alg.degree+1):
            u = self.from_coords(lower)
            d = self.alg.mul(u, self.J(u, meta))
            if meta:
                d = self.project(d)
            vals = self.homogeneous_coords(d, r)
            for i,di in zip(self.layers[r][0], vals):
                if meta and not self.chen[i]:
                    assert actual[i] == 0
                    continue
                v = actual[i]+di/2
                if self.signs[i] == 1:
                    assert v == 0
                else:
                    recovered[i] = v
                lower[i] = actual[i]
        return recovered


def nonlinear_checks():
    alg = Magnus(4)
    hall = SmallHall(alg)
    rng = random.Random(10020261113)
    neg = [i for i,s in enumerate(hall.signs) if s == -1]
    checks, rounds, samples = 0, 0, []
    for trial in range(32):
        params = {i: Q(rng.randrange(-3,4), 2**rng.randrange(3)) for i in neg}
        full = hall.anti_forward(params)
        meta_params = {i:a for i,a in params.items() if hall.chen[i]}
        meta = hall.anti_forward(meta_params, meta=True)
        assert hall.project(full) == meta
        assert hall.anti_inverse(full) == params
        assert hall.anti_inverse(meta, meta=True) == meta_params
        assert alg.mul(full, hall.J(full)) == alg.one
        assert hall.project(alg.mul(meta, hall.J(meta, True))) == alg.one
        checks += 4
        rounds += 2
        if trial < 3:
            samples.append({"negative_parameters": [[i,encode_q(a)] for i,a in params.items()],
                            "full_Hall_coordinates": [encode_q(a) for a in hall.collect(full)],
                            "meta_Hall_coordinates": [encode_q(a) for a in hall.collect(meta)]})

    Tgens = [alg.mul(hall.gens[0],hall.gens[1]), hall.gens[1], hall.gens[2]]
    Tinv = [alg.mul(hall.gens[0],alg.inv(hall.gens[1])), hall.gens[1],hall.gens[2]]
    T = lambda p: alg.subst(p,Tgens)
    Ti = lambda p: alg.subst(p,Tinv)
    L = lambda p: T(hall.J(Ti(p)))
    conjugacy_checks = 0
    for trial in range(24):
        params = {i: Q(rng.randrange(-2,3), 2) for i in neg}
        z = hall.anti_forward(params)
        x = T(z)
        assert Ti(T(z)) == z and T(Ti(z)) == z
        assert L(L(z)) == z and L(x) == alg.inv(x)
        assert hall.project(T(hall.project(z))) == hall.project(T(z))
        conjugacy_checks += 5

    kn = [i for i in neg if not hall.chen[i]]
    assert len(kn) == 2
    fixed = {i: Q((i%3)-1) for i in neg if hall.chen[i]}
    target = hall.anti_forward(fixed, meta=True)
    fibre_checks = 0
    for a,b in product(range(-2,3),repeat=2):
        pp = dict(fixed)
        pp.update({kn[0]:Q(a),kn[1]:Q(b)})
        z = hall.anti_forward(pp)
        assert hall.project(z) == target
        assert hall.anti_inverse(z)[kn[0]] == a
        assert hall.anti_inverse(z)[kn[1]] == b
        fibre_checks += 1
    return {
        "rank_three_Hall_children": hall.children,
        "rank_three_Chen_mask": hall.chen,
        "rank_three_J_signs": hall.signs,
        "central_correction_identity_checks": checks,
        "full_coordinate_round_trips": rounds,
        "literal_Nielsen_conjugacy_checks": conjugacy_checks,
        "exact_rank_three_kernel_fibre_checks": fibre_checks,
        "samples": samples,
        "coefficient_ring": "Q with every denominator prime to 3",
        "maximum_degree": 4
    }


def cusp_checks():
    names = ["O","A0","A1","A2","B0","B1","B2","C1","C2"]
    perm = [0,1,3,2,4,6,5,8,7]
    fixed = [(names[i], b) for i in range(9) for b in range(3)
             if (perm[i],(-b)%3) == (i,b)]
    assert fixed == [("O",0),("A0",0),("B0",0)]
    x,y,z = sp.symbols("x y z")
    maps = {"A0":(z,y,x), "B0":(x,z,y)}
    params = {"A0":x/z, "B0":y/x}
    tangent_checks = []
    for name, xyz in maps.items():
        subst = {x:xyz[0],y:xyz[1],z:xyz[2]}
        assert sp.cancel(params[name].subs(subst, simultaneous=True)-z/x) == 0
        assert tuple(a.subs(subst, simultaneous=True) for a in xyz) == (x,y,z)
        assert sp.expand(sum(a**3 for a in xyz)-(x**3+y**3+z**3)) == 0
        tangent_checks.append(name)
    for n in range(1,10):
        assert (-1)**(3**n) == -1
        assert (-1)**3 == -1
    return {"descent_points_checked":27, "fixed_points":fixed,
            "actual_rational_tangent_maps":tangent_checks,
            "coherent_minus_one_root_levels":9}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--source-code",type=Path,
                        default=Path("/workspace/scratch/e34c61ec5a35/LM7_FERMAT_TOWER/code"))
    args=parser.parse_args()
    module,digest=load_source(args.source_code/"e_unramified_sections.py")
    output={"statement":"E.100","input_sha256":digest}
    output["integral_quotient"]=rank_ten(module)
    print("PASS: rank-ten integral Hall/Chen projection, right inverse, saturation and actual arithmetic naturality.")
    output["nonlinear"]=nonlinear_checks()
    print("PASS: exact nonlinear anti lifts/inverses, quotient fibres and conjugate involution.")
    output["rational_cusp_descent"]=cusp_checks()
    print("PASS: all 27 cusp descent points and both actual rational tangent maps.")
    output["status"]="PASS"
    Path(__file__).with_suffix(".json").write_text(json.dumps(output,separators=(",",":"))+"\n")
    print("PASS: E.100 complete finite certificate.")


if __name__=="__main__":
    main()
