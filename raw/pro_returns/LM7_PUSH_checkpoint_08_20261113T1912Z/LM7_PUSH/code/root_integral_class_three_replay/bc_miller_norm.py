#!/usr/bin/env python3
"""Exact cubic-norm investigation for the supplied F343 Miller function.

The model and field operations are read from the root's checked module,
without executing its output-writing block.  This file owns only bc_* outputs.
"""
from pathlib import Path
import json

source = Path(__file__).with_name('a_miller_f343_root.py').read_text()
exec(compile(source.split('records=[]')[0], '<a_miller_f343_root definitions>', 'exec'))

Q = F((2, 0, 1)), F((1, 1, 6))
assert times(3, Q) == PC
a, line_coefficients = miller3(Q)


def pdivmod(f, g):
    f, g = list(clean(f)), clean(g)
    assert g != PZERO
    q = [Z] * max(1, len(f) - len(g) + 1)
    while len(f) >= len(g) and tuple(f) != PZERO:
        i = len(f) - len(g)
        c = f[-1] / g[-1]
        q[i] += c
        for j, d in enumerate(g):
            f[i+j] -= c*d
        f = list(clean(f))
    return clean(q), clean(f)


def pexact(f, g):
    q, r = pdivmod(f, g)
    assert r == PZERO
    return q


def peval(p, x):
    value = Z
    for c in reversed(p):
        value = value*x + c
    return value


def pder(p):
    return clean([i*p[i] for i in range(1, len(p))] or [Z])


def invnorm(f):
    num, den = f
    nn = nmul(num, conjugate_numerator(num))
    assert nn[1] == PZERO
    return nn[0], ppow(den, 2)


def regular_value(f, R):
    """Evaluate at points whose denominator has a simple zero at most."""
    (A, B), d = f
    x, y = R
    den, num = peval(d, x), peval(A, x)+peval(B, x)*y
    if den:
        return num/den
    assert not num and peval(pder(d), x)
    yp = 3*x*x/(2*y+1)
    return (peval(pder(A), x)+peval(pder(B), x)*y+peval(B, x)*yp)/peval(pder(d), x)


def pole_leading(f, R):
    """Coefficient of (x-x(R))^-1 at a simple pole."""
    (A, B), d = f
    x, y = R
    assert not peval(d, x) and peval(pder(d), x)
    return (peval(A, x)+peval(B, x)*y)/peval(pder(d), x)


def encf(f):
    return {'A': [list(x.v) for x in f[0][0]],
            'B': [list(x.v) for x in f[0][1]],
            'den': [list(x.v) for x in f[1]]}


def pshift(p, c):
    ans = PZERO
    for d in reversed(p):
        ans = padd(pmul(ans, (c, ONE)), (d,))
    return ans


def swapped_norm_search():
    """Seek g=p_5(v)+c*y, v^3=x-3, with Norm(g)=a*(x-3)*(x-r)^3.

    The leading v^5 coefficient is fixed to 1.  The top four coefficient
    equations express p_1,q_0,p_0,u_0 in terms of c,u_1; all 342^2 choices
    with u_1 nonzero are checked by exact finite-field arithmetic.  The
    The moving denominator r ranges over all F343 values.  Both the B0
    and A0 coefficients are checked before the full polynomial identity.
    """
    import numpy as np

    def ix(c):
        return c.v[0]+7*c.v[1]+49*c.v[2]

    def ff(i):
        i = int(i)
        return F((i%7, (i//7)%7, i//49))

    inds = np.arange(343, dtype=np.int32)
    left, right = inds[:,None], inds[None,:]
    l = [left%7, (left//7)%7, left//49]
    r = [right%7, (right//7)%7, right//49]
    addtab = sum(((l[i]+r[i])%7)*(7**i) for i in range(3))
    multab = (((l[0]*r[0]+2*(l[1]*r[2]+l[2]*r[1]))%7)
              +7*((l[0]*r[1]+l[1]*r[0]+2*l[2]*r[2])%7)
              +49*((l[0]*r[2]+l[1]*r[1]+l[2]*r[0])%7))
    negtab = (-inds%7)+7*((-(inds//7)%7)%7)+49*((-(inds//49))%7)
    invtab = np.zeros(343, dtype=np.int32)
    for i in range(1,343):
        invtab[i] = np.flatnonzero(multab[i] == 1)[0]
    def A(a,b): return addtab[a,b]
    def N(a): return negtab[a]
    def S(a,b): return A(a,N(b))
    def M(a,b): return multab[a,b]
    def D(a,b): return M(a,invtab[b])
    def P(a,n):
        result = np.ones_like(a)
        for _ in range(n): result = M(result,a)
        return result

    rQ2 = vertical(times(2,Q))
    minimal_num = tuple(pexact(p,rQ2) for p in a[0])
    assert len(minimal_num[0])==3 and minimal_num[0][-1]==ONE
    assert len(minimal_num[1])==1
    NA, NB = (pshift(p,F(3)) for p in minimal_num)
    na, nb = [ix(z) for z in NA], ix(NB[0])
    cc, u1 = np.meshgrid(np.arange(1,343), np.arange(1,343), indexing='ij')
    cc, u1 = cc.ravel(), u1.ravel()
    candidates = []
    p1 = D(S(P(cc,3),nb), M(3,cc))
    c2,c3,u12 = P(cc,2),P(cc,3),P(u1,2)
    for k in range(343):
        k2, k3 = M(k,k), M(M(k,k),k)
        q0 = D(S(S(A(na[1],M(3,k)),P(p1,3)),M(M(3,u1),S(c2,p1))),3)
        p0 = S(S(A(u12,M(3,c2)),M(p1,q0)),D(M(nb,k),cc))
        u0 = D(A(A(S(M(cc,u1),M(2,c2)),M(p0,q0)),D(M(nb,k2),cc)),M(2,u1))
        b0 = S(M(M(3,cc),P(u0,2)),M(M(3,c2),u0))
        a0 = A(P(u0,3),M(6,S(M(M(3,c2),u0),c3)))
        for i in np.flatnonzero((b0==M(nb,k3)) & (a0==M(na[0],k3))):
            candidates.append((ff(k),)+tuple(ff(v[i]) for v in (cc,u0,u1,p0,p1,q0)))
    # The u1=0 row uses B1 then B0 and A0; enumerate its final scalar u0.
    for c in FIELD[1:]:
        p1c = (c**3-NB[0])/(3*c)
        for k in FIELD:
            q0c = (NA[1]+3*k-p1c**3)/3
            p0c = 3*c*c-p1c*q0c-NB[0]*k/c
            if 3*c**3*2-3*c*p0c*q0c != 3*NB[0]*k*k:
                continue
            for u0c in FIELD:
                if (3*c*u0c*u0c-3*c*c*u0c == NB[0]*k**3
                        and u0c**3+6*(3*c*c*u0c-c**3)==NA[0]*k**3):
                    candidates.append((k,c,u0c,Z,p0c,p1c,q0c))
    witnesses=[]
    for k,c,u0c,u1c,p0c,p1c,q0c in candidates:
        u, p, q = (u0c,u1c), (p0c,p1c), (q0c,ONE)
        # Compute the exact norm in the original x coordinate.
        ux, px, qx = (pshift(f,F(-3)) for f in (u,p,q))
        base = (ux,(c,))
        cub = npow(base,3)
        sumother = padd(pmul(vertical(PC),ppow(px,3)),pmul(ppow(vertical(PC),2),ppow(qx,3)))
        minus = nscale(base,pmul((F(-3),),pmul(vertical(PC),pmul(px,qx))))
        norm = (padd(padd(cub[0],sumother),minus[0]),padd(cub[1],minus[1]))
        r = F(3)-k
        target = nscale(minimal_num,ppow((-r,ONE),3))
        if norm==target:
            witnesses.append({'c_y':list(c.v),
                              'p5_coefficients':[list(t.v) for t in (u0c,p0c,q0c,u1c,p1c,ONE)],
                              'r':list(r.v),
                              'denominator':'v*(x-r)',
                              'norm_is_exact_a':True})
    return {'tested_nonexceptional_rows':343*342**2,
            'remaining_after_four_high_coefficients_and_B0_A0':len(candidates),
            'witnesses':witnesses,
            'target_b1_norm_a':True}


# The involution trace cancels the auxiliary vertical factor.
trace_num = padd(a[0][0], padd(a[0][0], pneg(a[0][1])))
trace_num = pexact(trace_num, vertical(times(2, Q)))
trace_den = vertical(PC)
trace = ((trace_num, PZERO), trace_den)
assert feq(trace, ((padd(a[0][0], padd(a[0][0], pneg(a[0][1]))), PZERO), a[1]))

records = []
for xx in [F(3), F(5)]:
    zeros = [R for R in E3 if R is not None and R[0] == xx]
    data = []
    for R in zeros:
        if R == PC:
            # tame symbol (a,b): v(a)=-1,v(b)=1 gives -a*b.
            residue = -pole_leading(a, R)
            va = -1
        else:
            residue = regular_value(a, R)
            va = 0
        data.append({'point': encP(R), 'v_a': va, 'tame_symbol': list(residue.v),
                     'cubic_residue': list((residue**114).v),
                     'cube_roots': [list(c.v) for c in FIELD if c**3 == residue]})
    # At the extra pole P when b is a unit, the tame symbol is b(P).
    if xx != PC[0]:
        residue = PC[0]-xx
        data.append({'point': encP(PC), 'v_a': -1, 'tame_symbol': list(residue.v),
                     'cubic_residue': list((residue**114).v),
                     'cube_roots': [list(c.v) for c in FIELD if c**3 == residue]})
    records.append({'b': 'x-'+str(xx.v), 'finite_tame_symbols': data})

out = {'Q': encP(Q), 'a': encf(a),
       'line_coefficients': [list(c.v) for c in line_coefficients],
       'involution_trace': encf(trace),
       'tame_symbol_checks': records,
       'status': 'EXACT_RESIDUE_AUDIT'}
if __name__ == '__main__':
    out['swapped_small_norm_search']=swapped_norm_search()
    encoded = json.dumps(out, indent=2)+'\n'
    print(encoded, end='')
    Path(__file__).with_suffix('.json').write_text(encoded)
