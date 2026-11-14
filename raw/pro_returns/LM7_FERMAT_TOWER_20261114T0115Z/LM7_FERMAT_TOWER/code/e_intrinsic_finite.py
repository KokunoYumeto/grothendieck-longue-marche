#!/usr/bin/env python3
"""Exact norm and conjugation certificates for E.35."""
from pathlib import Path
import json
import sympy as sp
from e_cubic_abelian import K
from e_intrinsic_obstruction import mul,inv

OUT=Path(__file__).resolve().parent
W=K(0,1)

def lmul(a,b,A=2):
    r=[K(),K(),K()]
    for i in range(3):
        for j in range(3):
            r[(i+j)%3]=r[(i+j)%3]+a[i]*b[j]*(A if i+j>=3 else 1)
    return r

def lp(a,n):
    r=[K(1),K(),K()]
    for _ in range(n):r=lmul(r,a)
    return r

def sigma(a):return [a[i]*(W**i) for i in range(3)]

def conjugate(h,g):return mul(mul(h,g),inv(h))

def main():
    X,Y,Z,A,B=sp.symbols('X Y Z A B')
    matrix=sp.Matrix([[X,A*Z,A*Y],[Y,X,A*Z],[Z,Y,X]])
    norm=sp.expand(matrix.det())
    expected=X**3+A*Y**3+A**2*Z**3-3*A*X*Y*Z
    assert sp.expand(norm-expected)==0
    split_solution={A:1,X:(B+2)/3,Y:(B-1)/3,Z:(B-1)/3}
    assert sp.factor(expected.subs(split_solution)-B)==0
    assert expected.subs({A:2,X:1,Y:1,Z:0})==3
    w=[K(1),K(1),K()]
    nw=lmul(lmul(w,sigma(w)),sigma(sigma(w)))
    assert nw==[K(3),K(),K()]
    v=lmul(lp(w,2),sigma(w))
    assert v==[1+2*W,2+W,1+2*W]
    assert lmul(sigma(v),lp(w,3))==[3*t for t in v]
    # For every assignment of two free generators to H3, calculate
    # exact conjugacy orbits with the prescribed abelian images.
    H=[(a,b,c) for a in range(3) for b in range(3) for c in range(3)]
    rows=[];hist={0:0,1:0,2:0};total_orbits=0
    for a in range(3):
      for b in range(3):
       for d in range(3):
        for e in range(3):
            rank=0 if a==b==d==e==0 else (2 if (a*e-b*d)%3 else 1)
            hist[rank]+=1
            pending={(c,f) for c in range(3) for f in range(3)}
            orbits=[]
            while pending:
                c,f=min(pending);g=(a,b,c);h=(d,e,f)
                orbit=set()
                for k in H:
                    kg=conjugate(k,g);kh=conjugate(k,h)
                    assert kg[:2]==g[:2] and kh[:2]==h[:2]
                    assert (kg[2]-g[2])%3==(k[0]*b-k[1]*a)%3
                    assert (kh[2]-h[2])%3==(k[0]*e-k[1]*d)%3
                    orbit.add((kg[2],kh[2]))
                assert len(orbit)==3**rank
                pending-=orbit
                orbits.append(sorted(orbit))
            assert len(orbits)==3**(2-rank)
            total_orbits+=len(orbits)
            rows.append({'abelian_columns':[[a,b],[d,e]],'span_rank':rank,
                         'central_fiber_orbits':len(orbits),
                         'central_conjugation_orbits':orbits})
    assert hist=={0:1,1:32,2:48} and total_orbits==153
    data={'statement':'E.35','norm_multiplication_matrix':
              [[str(x) for x in row] for row in matrix.tolist()],
          'norm_form':str(norm),'split_case_solution':
              ['(B+2)/3','(B-1)/3','(B-1)/3'],
          'independent_example':{'A':2,'B':3,'w':'1+alpha',
                                  'v_coefficients':[x.data() for x in v]},
          'sigma_v_times_w3_equals_Bv':True,
          'conjugation_difference':'r*v-s*u',
          'all_abelian_assignments':81,'all_generator_assignments':729,
          'span_rank_histogram':hist,'total_conjugacy_orbits':total_orbits,
          'fiber_orbit_certificates':rows,
          'proof_location':'sections/E_intrinsic_finite.tex'}
    (OUT/'e_intrinsic_finite.json').write_text(json.dumps(data,indent=2)+'\n')
    print('E.35 finite intrinsic quotient classification certificates')
    print('Norm form:',norm)
    print('Split cubic algebra norm solution: ((B+2)/3,(B-1)/3,(B-1)/3)')
    print('Independent example: A=2, B=3, w=1+alpha, Norm(w)=3')
    print('v=w^2*sigma(w) coefficients:',[x.data() for x in v])
    print('sigma(v)*w^3=B*v: PASS')
    print('All 81 abelian assignments and 729 H3 generator assignments checked')
    print('Span-rank histogram:',hist)
    print('Conjugacy orbits:',total_orbits)
    print('Each central fiber count is 3^(2-span_rank): PASS')
    print('All exact certificates: PASS')

if __name__=='__main__':main()
