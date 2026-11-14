#!/usr/bin/env python3
"""Exact tangent-line norm and linear algebra for the rational E.36 coordinates.

Roots of unity are represented by their powers of zeta_3.  The program
checks all 54 pullbacks of all nine tangent lines and the exact linear
equations determining the averaged path class.  Integral torsion is not
evaluated by passing to rational Kummer classes.
"""
from itertools import permutations,product
from fractions import Fraction as Q
from pathlib import Path
import json

labels=[letter+str(i) for letter in 'ABC' for i in range(3)]
# A_i=[0:-zeta^i:1], etc.; line coefficients are powers of zeta.
lines=[]
for letter in 'ABC':
    for i in range(3):
        lines.append({'A':(None,2*i%3,0),
                      'B':(2*i%3,None,0),
                      'C':(2*i%3,0,None)}[letter])
origin=labels.index('C0')
norm_exponents=[0]*9
permuted_counts=[[0]*9 for _ in range(9)]
rows=[]
for p in permutations(range(3)):
    for a,b in product(range(3),repeat=2):
        exps=(a,b,0)
        perm=[];scalars=[]
        for c,L in enumerate(lines):
            pull=[None]*3
            for j in range(3):
                if L[j] is not None:pull[p[j]]=(L[j]+exps[p[j]])%3
            matches=[]
            for d,K in enumerate(lines):
                for t in range(3):
                    candidate=[None if x is None else (x+t)%3 for x in K]
                    if candidate==pull:matches.append((d,t))
            assert len(matches)==1
            d,t=matches[0]
            permuted_counts[c][d]+=1
            norm_exponents[c]=(norm_exponents[c]+t)%3
            perm.append(d);scalars.append(t)
        assert len(set(perm))==9
        rows.append({'p':list(p),'diagonal':[a,b,0],
                     'pullback_line_permutation':perm,'root_exponents':scalars})
assert len(rows)==54
assert all(row==[6]*9 for row in permuted_counts)
ratio_exponents=[(e-norm_exponents[origin])%3 for e in norm_exponents]

# Rational Kummer coefficient of the leading term of L_c/L_O at q=Z/X.
# q^{-3} times -3 L_c(1,-1,0).  At C1,C2 use
# (1-zeta)^2=-3zeta, and the conjugate identity.
leading=[Q(1)]*6+[Q(0),Q(3,2),Q(3,2)]
mean=[Q(-1,3)]*6+[Q(0),Q(-1,2),Q(-1,2)]
for i in range(9):
    assert 3*(mean[i]-mean[origin])==-leading[i]
assert all(e==0 for e in ratio_exponents)

# eta-e_A eta is the negative of this averaged path class under v->[v,w].
eta=[-x for x in mean]
lambda_six=Q(1,3);mu_two=Q(1,2)
assert eta==[lambda_six]*6+[Q(0),mu_two,mu_two]
out={
 'claim':'Exact rational Kummer coordinates under the stated path-cocycle sign convention',
 'cusp_order':labels,'origin':'C0','tangent_parameter':'q=Z/X with tangent1',
 'automorphism_count':len(rows),
 'each_line_pullback_multiplicity':6,
 'norm_of_each_tangent_line_ratio':'1',
 'norm_root_exponents':ratio_exponents,
 'leading_term_kappa3_coefficients':[str(x) for x in leading],
 'averaged_path_coefficients_mod_diagonal':[str(x) for x in mean],
 'eta_kernel_coefficients_mod_diagonal':[str(x) for x in eta],
 'lambda':str(lambda_six),'mu':str(mu_two),
 'automorphism_rows':rows,
 'integral_torsion_evaluated':False,'checks_passed':True
}
Path(__file__).with_name('kummer_coordinates_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='automorphism_rows'},indent=2))
