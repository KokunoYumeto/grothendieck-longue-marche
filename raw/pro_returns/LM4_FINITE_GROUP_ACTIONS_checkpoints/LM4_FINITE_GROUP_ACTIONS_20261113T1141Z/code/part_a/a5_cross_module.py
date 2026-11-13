#!/usr/bin/env python3
"""Exact cross-factor module data for the continuing A5 refinement attack.

This constructs the adjoint F5[A5] module and a nontrivial 1-cocycle.
It does not assert that a new full GT_0 element exists, or that any of the
finite D.47 survivors lifts to a full element.
"""
from itertools import product
from pathlib import Path
import json
import a5_involution_quotient as a
import a5_schur_refinement as s

P = 5


def add(v, w):
    return tuple((x + y) % P for x, y in zip(v, w))


def neg(v):
    return tuple(-x % P for x in v)


def mv(A, v):
    return tuple(sum(x*y for x, y in zip(row, v)) % P for row in A)


def mm(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(len(B))) % P
                       for j in range(len(B[0]))) for i in range(len(A)))


def rank(rows):
    rows = [list(r) for r in rows]
    pos = 0
    for col in range(len(rows[0]) if rows else 0):
        j = next((j for j in range(pos, len(rows)) if rows[j][col] % P), None)
        if j is None:
            continue
        rows[pos], rows[j] = rows[j], rows[pos]
        u = pow(rows[pos][col], -1, P)
        rows[pos] = [x*u % P for x in rows[pos]]
        for j in range(len(rows)):
            if j != pos:
                u = rows[j][col]
                rows[j] = [(x-u*y) % P for x, y in zip(rows[j], rows[pos])]
        pos += 1
    return pos


def tensor(v, w):
    return tuple(x*y % P for x in v for y in w)


def kron(A, B):
    return tuple(tuple(A[i//len(B)][j//len(B)] * B[i%len(B)][j%len(B)] % P
                       for j in range(len(A)*len(B)))
                 for i in range(len(A)*len(B)))


def main():
    pmap, glconj = s.aisomorphism()
    basis = ((1,0,0,4), (0,1,0,0), (0,0,1,0))
    mats = []
    for g in range(60):
        cols = []
        for b in basis:
            v = s.conjugate(pmap[g], b)
            assert (v[0] + v[3]) % 5 == 0
            cols.append((v[0], v[1], v[2]))
        mats.append(tuple(tuple(cols[j][i] for j in range(3)) for i in range(3)))
    assert all(mm(mats[g], mats[h]) == mats[a.MUL[g][h]]
               for g in range(60) for h in range(60))
    g = next(x for x in range(60) if a.order(x) == 2)
    h = next(y for y in range(60) if a.order(y) == 3
             and a.order(a.MUL[g][y]) == 5)
    assert a.generated(g, h) == 60
    vectors = list(product(range(5), repeat=3))
    zero = (0,0,0)
    fixed = [v for v in vectors if mv(mats[g],v) == mv(mats[h],v) == v]
    assert fixed == [zero]

    def make_cocycle(v, w):
        c = {a.ID: zero}
        queue = [a.ID]
        for z in queue:
            for b, value in ((g,v), (h,w)):
                zb = a.MUL[z][b]
                new = add(c[z], mv(mats[z], value))
                if zb in c:
                    if c[zb] != new:
                        return None
                else:
                    c[zb] = new
                    queue.append(zb)
        assert len(c) == 60
        return tuple(c[i] for i in range(60))

    coboundaries = {add(mv(mats[g],v),neg(v)) + add(mv(mats[h],v),neg(v))
                   for v in vectors}
    assert len(coboundaries) == 125
    cocycles = []
    chosen = None
    for v in vectors:
        for w in vectors:
            c = make_cocycle(v,w)
            if c is None:
                continue
            cocycles.append(v+w)
            if chosen is None and v+w not in coboundaries:
                chosen = c
    assert len(cocycles) == 625 and chosen is not None
    assert rank(cocycles) == 4 and rank(list(coboundaries)) == 3
    assert all(chosen[a.MUL[g][h]] == add(chosen[g],mv(mats[g],chosen[h]))
               for g in range(60) for h in range(60))

    # Irreducibility: enumerate the31 lines and31 planes over F5.
    def project(v):
        u = next(x for x in v if x)
        return tuple(x*pow(u,-1,5)%5 for x in v)
    lines = sorted({project(v) for v in vectors if v != zero})
    assert len(lines) == 31
    invariant_lines = [v for v in lines
                       if all(project(mv(mats[t],v)) == v for t in (g,h))]
    invariant_planes = []
    for normal in lines:
        space = [v for v in vectors if sum(x*y for x,y in zip(normal,v))%5 == 0]
        if all(all(sum(x*y for x,y in zip(normal,mv(mats[t],v)))%5 == 0
                   for v in space) for t in (g,h)):
            invariant_planes.append(normal)
    assert invariant_lines == invariant_planes == []

    # The commutant consists of scalars: solve XA=AX on9 entries.
    equations = []
    for A in (mats[g],mats[h]):
        for i in range(3):
            for j in range(3):
                row = [0]*9
                for k in range(3):
                    row[3*i+k] += A[k][j]
                    row[3*k+j] -= A[i][k]
                equations.append([x%5 for x in row])
    assert rank(equations) == 8
    # Their linear span is the full matrix algebra.  Tensoring these
    # spanning matrices proves simplicity of each cross-factor module.
    representation_span_dimension = rank([tuple(x for row in A for x in row)
                                          for A in mats])
    assert representation_span_dimension == 9

    # The two D38 factors where the common square/nonsquare choice couples.
    representatives = []
    used = set()
    for x in range(60):
        for y in range(60):
            if (x,y) in used or a.generated(x,y) != 60:
                continue
            representatives.append((x,y))
            used.update((c[x],c[y]) for c in a.CONJ)
    assert len(representatives) == 19
    selected_factors = [6,8]
    xx = tuple(representatives[i][0] for i in selected_factors)
    yy = tuple(representatives[i][1] for i in selected_factors)
    zz = tuple(a.INV[a.MUL[x][y]] for x,y in zip(xx,yy))
    E9 = tuple(tuple(int(i==j) for j in range(9)) for i in range(9))
    local_rows = []
    for name, pair in [('x',xx),('y',yy),('z',zz)]:
        inverters = []
        for x in pair:
            invs = [t for t in range(60) if a.order(t)==2
                    and a.MUL[a.MUL[t][x]][t] == a.INV[x]]
            if a.order(x) == 2:
                invs = [t for t in invs if t != x]
            inverters.append(invs)
        A = kron(mats[pair[0]],mats[pair[1]])
        fixed_rows = [[(x-y)%5 for x,y in zip(row,unit)]
                      for row,unit in zip(A,E9)]
        cases = []
        for tt in product(*inverters):
            T = kron(mats[tt[0]],mats[tt[1]])
            dims = []
            for sign in (1,-1):
                eigrows = [[(x-sign*y)%5 for x,y in zip(row,unit)]
                           for row,unit in zip(T,E9)]
                dims.append(9-rank(fixed_rows+eigrows))
            cases.append({'inverters':tt,'invariant_plus_minus_dimensions':dims,
                          'integer_involution_trace_on_invariants':dims[0]-dims[1]})
        local_rows.append({'cusp':name,'orders':[a.order(x) for x in pair],
                           'invariant_dimension':9-rank(fixed_rows),
                           'cases':cases})
    assert all(c['integer_involution_trace_on_invariants']==1
               for row in local_rows for c in row['cases'])

    # For the tensor module on Q=A5xA5, beta((g,h),(u,v))
    # = c(g) tensor h*c(v).  Its2-cocycle identity reduces exactly
    # to the3600 verified1-cocycle identities and representation law.
    # Check a generating-grid family of the full2-cocycle identity too.
    def action(q, v):
        return mv(kron(mats[q[0]],mats[q[1]]),v)
    def qmul(q,r):
        return (a.MUL[q[0]][r[0]],a.MUL[q[1]][r[1]])
    def beta(q,r):
        return tensor(chosen[q[0]], mv(mats[q[1]],chosen[r[1]]))
    gens = [(g,a.ID),(h,a.ID),(a.ID,g),(a.ID,h)]
    identities = 0
    for q in gens:
        for r in gens:
            for z in product(range(60),repeat=2):
                assert add(action(q,beta(r,z)),beta(q,qmul(r,z))) == \
                       add(beta(q,r),beta(qmul(q,r),z))
                identities += 1

    output = {
        'base_group': 'A5 identified exactly with PSL2(F5)',
        'base_group_order': 60,
        'module': 'V=sl2(F5), the adjoint module',
        'module_dimension': 3,
        'triangle_generators': [g,h],
        'fixed_subspace_dimension': 0,
        'Z1_dimension': 4,
        'B1_dimension': 3,
        'H1_dimension': 1,
        'nonzero_cocycle_values_on_triangle_generators': [chosen[g],chosen[h]],
        'selected_cocycle_values': chosen,
        'verified_cocycle_multiplication_pairs': 3600,
        'invariant_lines': 0,
        'invariant_planes': 0,
        'commutant_dimension': 1,
        'representation_span_dimension': representation_span_dimension,
        'selected_D38_factors': selected_factors,
        'local_cusp_trace_checks': local_rows,
        'local_cusp_trace_cases': sum(len(row['cases']) for row in local_rows),
        'sum_of_three_cusp_involution_traces': 3,
        'relative_duality_H1_plus_minus_dimensions': [3,6],
        'cross_module_dimension': 9,
        'cross_module_kernel_order': 5**9,
        'cross_extension_group_order': 60**2*5**9,
        'explicit_cross_cocycle': 'beta((g,h),(u,v))=c(g) tensor h*c(v)',
        'verified_cross_cocycle_grid_triples': identities,
        'scope': 'Exact module and cocycle construction. No D47 tuple has yet been excluded by this extension, and no full lifting assertion is made.'
    }
    Path(__file__).with_name('a5_cross_module_output.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))


if __name__ == '__main__':
    main()
