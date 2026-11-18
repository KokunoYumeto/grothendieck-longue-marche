"""Exact checks of explicit objects used in the post-freeze research notes.

This script performs no OCR and never writes transcription files. Symbolic
identities and finite matrix relations do not certify a group presentation,
a general uniformization theorem, or the supplied results registers.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s

R=Path(__file__).resolve().parent
checks=[]
def check(name, assertion, detail):
    assert assertion, name
    checks.append({'id':name,'outcome':'pass','detail':detail})

I=s.eye(2)
S=s.Matrix([[0,-1],[1,0]])
P=s.Matrix([[0,-1],[1,1]])
r2=s.Matrix([[0,1],[1,0]])
r1=S*r2
r3=r2*P
check('C01.modular',S**2==P**3==-I and S**4==P**6==I,
      'S^2=P^3=-I; S^4=P^6=I for the explicitly listed integral matrices.')
check('C01.reflections',all(m*m==I and m.det()==-1 for m in (r1,r2,r3)) and r1*r2==S and r2*r3==P,
      'Three determinant-minus-one involutions realize both scan050 product relations.')
check('C01.shear',S.inv()*P==s.Matrix([[1,1],[0,1]]),'S^{-1}P is the unit upper shear.')

a,d,u,v=s.symbols('a d u v',real=True)
A=s.Matrix([[a,u+s.I*v],[u-s.I*v,d]])
J=s.Matrix([[0,-1],[1,0]])
D=s.diag(-1,1)
check('C02.rotation',D.T*A*D==s.Matrix([[a,-u-s.I*v],[-u+s.I*v,d]]),
      'Pullback of the form by z -> -z negates both off-diagonal entries.')
check('C02.conjugation',s.conjugate(A)==s.Matrix([[a,u-s.I*v],[u+s.I*v,d]]),
      'Pullback by z -> conjugate(z) fixes precisely the real-symmetric forms.')
check('C02.antipodal',s.conjugate(J.T*A*J)==s.Matrix([[d,-u-s.I*v],[-u+s.I*v,a]]),
      'Antipodal pullback equality imposes a=d and u=v=0.')
t,x,y,z=s.symbols('t x y z',real=True)
H=s.Matrix([[t+x,y+s.I*z],[y-s.I*z,t-x]])
check('C02.lorentz',s.expand(H.det())==t*t-x*x-y*y-z*z,
      'The displayed Hermitian-to-Lorentz linear map preserves the determinant quadratic form.')

A0=s.Matrix([[1,-s.Rational(1,2)],[-s.Rational(1,2),1]])
B=s.Matrix([[-1,1],[0,1]])
U=s.Matrix([[0,1],[1,0]])
check('C03.symmetric_metric',B.T*A0*B==A0 and U.T*A0*U==A0 and A0.det()==s.Rational(3,4),
      'The positive form A0 is fixed by z -> 1-z and z -> 1/z, generating the six label permutations.')
xx,yy=s.symbols('xx yy',real=True)
zz=xx+s.I*yy
norm2=lambda q:s.expand(q*s.conjugate(q))
check('C03.bisectors',s.expand(norm2(1-zz/2)-norm2((zz+1)/2))==s.Rational(3,4)*(1-2*xx)
      and s.expand(norm2(1-zz/2)-norm2(zz-s.Rational(1,2)))==s.Rational(3,4)*(1-xx*xx-yy*yy),
      'The cell of0 is |z|<=1 and Re(z)<=1/2 in the invariant spherical metric.')
check('C03.annulus',s.Rational(7,4)<s.Rational(4,3)**2<s.Rational(7,5)**2<s.Rational(3,2)**2,
      'sqrt(7)/2 < 4/3 < 7/5 < 3/2; the annulus separates the entire cell from1 and infinity.')
check('C03.numeric_obstruction',s.Rational(1024,21)>4*s.Rational(22,7)**2,
      '1024 log(21/20) >1024/21 >4(22/7)^2 >4pi^2. This verifies the numerical gap used in the length32 example.')

check('C04.heavy_sign_example',2*0+2+1>=1 and not(2*0+1>=3),
      'At(g,nu)=(0,1), the plus reading of the first inequality in scan040 and the following test have different truth values; this is a reading question only.')

report={'utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
        'who':'GPT-6 Astra Pro; effort not separately exposed; MPL_67_002-052/root',
        'sympy_version':s.__version__,
        'scope':'Exact symbolic and rational calculations on explicitly displayed objects; no transcription mutations',
        'matrices':{k:str(m) for k,m in {'S':S,'P':P,'r1':r1,'r2':r2,'r3':r3,'A0':A0}.items()},
        'checks':checks}
(R/'calculation_results.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
