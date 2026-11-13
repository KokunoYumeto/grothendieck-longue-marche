"""Independent exact Levi certificates for the requested n=5,6 cases.
The topology conclusion uses the proved Morse-index and end-collar argument
in the paper. This script is an exact algebraic certificate, not a finite
approximation to the infinite curve complex.
"""
from itertools import combinations
import sympy as s
for d in (2,3):
    z=s.symbols('z1:'+str(d+1));forms=[];rows=[]
    for i in range(d):
        for c in (0,1):
            forms.append(z[i]-c);rows.append([int(i==j) for j in range(d)])
    for i,j in combinations(range(d),2):
        forms.append(z[i]-z[j]);rows.append([int(a==i)-int(a==j) for a in range(d)])
    w=s.symbols('w1:'+str(len(forms)+1),positive=True)
    L=s.eye(d)
    for q,row in zip(w,rows):
        a=s.Matrix(row);L+=q*a*a.T
    print(f'M0,{d+3}: dim_C={d}, arrangement forms={forms}')
    print('Levi matrix I+sum |ell|^-4 a a^T =')
    print(L)
    for size in range(1,d+1):
        count=0;monomials=0
        for I in combinations(range(d),size):
            det=s.Poly(s.expand(L.extract(I,I).det()),*w)
            assert det.coeff_monomial((0,)*len(w))==1
            assert all(c>0 for c in det.coeffs())
            count+=1;monomials+=len(det.monoms())
        print(f'Principal minors of size {size}: {count}, total positive monomials={monomials}; constant term 1 and all coefficients positive PASS')
    print(f'Strict Levi positivity certified; real Morse index <= {d}; reversed relative cells have dimension >= {d}; boundary -> U is {d-1}-connected; homotopy fibre is {d-2}-connected.')
print('M0,6, k=3: empty multicurve is a minimum of P_3; its order complex is a cone, hence contractible (all reduced homology and homotopy vanish).')
