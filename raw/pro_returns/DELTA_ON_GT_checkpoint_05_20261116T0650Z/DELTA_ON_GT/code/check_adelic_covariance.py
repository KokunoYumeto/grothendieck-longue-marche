"""Exact symbolic certificate for AD.1--AD.3; not a profinite lifting test."""
import sympy as s
a,b,c,lam,t=s.symbols('a b c lam t')
Ulam=s.Matrix([[1,lam],[0,1]])
B=s.Matrix([[a,b],[c,2-a]])
defect=(Ulam*B*Ulam-B*Ulam*B).applyfunc(s.expand)
assert s.expand(defect[1,0]+c*(lam*c+1))==0
det=B.det()
assert s.expand(det-(-a*a+2*a-b*c))==0
U=s.Matrix([[1,1],[0,1]])
L=s.Matrix([[1,0],[-1,1]])
V=s.Matrix([[lam,t],[0,1]])
Bt=(V*L*V.inv()).applyfunc(s.simplify)
assert (V*U*V.inv()-Ulam).applyfunc(s.simplify)==s.zeros(2)
assert (Ulam*Bt*Ulam-Bt*Ulam*Bt).applyfunc(s.simplify)==s.zeros(2)
assert s.simplify(Bt.trace()-2)==0 and s.simplify(Bt.det()-1)==0
R=-U*L; S=U*L*U
assert R**3==s.eye(2) and S**2==-s.eye(2)
p,q,r,w=s.symbols('p q r w')
Z=s.Matrix([[p,q],[r,w]])
for A,name,norm in [(R,'Eisenstein',a*a-a*b+b*b),(S,'Gaussian',a*a+b*b)]:
    sol=s.linsolve(list(Z*A-A*Z),(p,q,r,w))
    assert len(sol)==1
    assert s.expand((a*s.eye(2)+b*A).det()-norm)==0
    for sign in [1,-1]:
        assert any(int(v)%4 for v in sign*A-s.eye(2))
    assert int(A[0,1])%4!=0
    print(name,'centralizer solution',sol,'norm',norm)
assert U*L!=L*U
print('Braid defect lower-left:',s.factor(defect[1,0]))
print('Intertwined second generator:',Bt)
print('R0 and S are nonscalar modulo4, and neither sign is identity: PASS')
print('Signed adelic covariance algebra: PASS')
