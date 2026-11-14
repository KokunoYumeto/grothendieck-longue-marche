#!/usr/bin/env python3
"""Exact theta/isogeny distribution for the eight actual cusp units.

The certificate retains all norm constants.  It does not divide the
proper regulator operator, whose 3-Smith factors are 3 and 9.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import sympy as s
from a_e120_exact import QZ
from a_local_smith import local_smith, encode

base=Path(__file__).resolve().parent
units=json.loads((base/'a_cusp_unit_symbols.json').read_text())
theta=json.loads((base/'a_elliptic_theta_pi.json').read_text())
z=QZ(0,1); D=1+2*z; lam=1-z; pi=1+3*z
B=QZ(F(-27,4)); c=QZ(-27)/pi; C=81*(z-4)/7
theta_lead=-D/(9*pi)
assert D**2==-3 and pi*theta_lead==-D/9
labels=units['cusp_order']

def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))

# The nonzero pi-kernel has X roots of X^3+c and both Y signs.
# For a line A(X)+bY, first take the product over the two signs,
# then the determinant of multiplication in Q(zeta)[X]/(X^3+c).
def norm_cubic(v):
    v=list(v)+[QZ(0)]*(3-len(v))
    columns=[]
    for j in range(3):
        a=[QZ(0)]*5
        for i in range(3):a[i+j]+=v[i]
        for k in (4,3):a[k-3]-=c*a[k]
        columns.append(a[:3])
    return det3([[columns[j][i] for j in range(3)] for i in range(3)])

def norm_line_nonzero_pi(line):
    aa,bb,cc=[QZ(*v) for v in line]
    a0=(aa+bb)/2; a1=-cc/3; b=(aa-bb)/9
    # A(X)^2-b^2(X^3+B), reduced by X^3=-c.
    return norm_cubic([a0*a0-b*b*B+b*b*c,2*a0*a1,a1*a1])

class Quad:
    """Q(zeta)[v]/(v^2+23/4), for one exact ordinary test point."""
    square=QZ(F(-23,4))
    def __init__(self,a=0,b=0):self.a=QZ.coerce(a);self.b=QZ.coerce(b)
    @staticmethod
    def coerce(x):return x if isinstance(x,Quad) else Quad(x)
    def __add__(self,x):
        x=self.coerce(x);return Quad(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self):return Quad(-self.a,-self.b)
    def __sub__(self,x):return self+-self.coerce(x)
    def __rsub__(self,x):return self.coerce(x)+-self
    def __mul__(self,x):
        x=self.coerce(x)
        return Quad(self.a*x.a+self.square*self.b*x.b,self.a*x.b+self.b*x.a)
    __rmul__=__mul__
    def inv(self):
        n=self.a*self.a-self.square*self.b*self.b
        return Quad(self.a/n,-self.b/n)
    def __truediv__(self,x):return self*self.coerce(x).inv()
    def __rtruediv__(self,x):return self.coerce(x)*self.inv()
    def __pow__(self,n):
        if n<0:return self.inv()**(-n)
        a=Quad(1);b=self
        while n:
            if n&1:a=a*b
            b=b*b;n//=2
        return a
    def __eq__(self,x):
        x=self.coerce(x);return self.a==x.a and self.b==x.b
    def key(self):return [self.a.key(),self.b.key()]

def plane_to_weierstrass(label):
    i=int(label[1]);zz=z**i
    x,y,zzp={'A':(QZ(0),-zz,QZ(1)),
             'B':(-zz,QZ(0),QZ(1)),
             'C':(QZ(1),-zz,QZ(0))}[label[0]]
    if label=='C0':return None
    return -3*zzp/(x+y),9*(x-y)/(2*(x+y))

def function_value(unit,X,Y):
    x=Quad(F(1,2))+Y/9;y=Quad(F(1,2))-Y/9;zzp=-X/3
    out=Quad(QZ(*unit['constant']))
    for factor in unit['linear_factors']:
        aa,bb,cc=[QZ(*v) for v in factor['line']]
        out=out*(x*aa+y*bb+zzp*cc)**factor['power']
    return out

P=(Quad(1),Quad(0,1))
assert P[1]**2==P[0]**3+B
den=1+c
XV=1-18*c/den+12*(B-c)*(1-2*c)/den**2
Yfac=1-18*c*(c-2)/den**2+12*(B-c)*(-2+14*c-2*c*c)/den**3
piP=(Quad(XV/pi**2),P[1]*(Yfac/pi**3))
assert piP[1]**2==piP[0]**3+B
theta_shift={}
for label in labels:
    T=plane_to_weierstrass(label)
    if T is None:X=P[0]
    else:
        xt,yt=T
        slope=(P[1]+yt)/(P[0]-xt)  # P minus T
        X=slope*slope-P[0]-xt
    theta_shift[label]=Quad(C)/(X**3+c)

records=[]
for unit in units['normalized_units']:
    r=unit['divisor'];rO=r[0]
    product=QZ(*unit['constant'])**6
    line_norms=[]
    for factor in unit['linear_factors']:
        nl=norm_line_nonzero_pi(factor['line'])
        assert nl
        product*=nl**factor['power']
        line_norms.append({'line':factor['line'],'power':factor['power'],'norm_nonzero_kernel':nl.key()})
    norm_constant=product*pi**(-rO)
    expected=(3*D)**rO
    tame=theta_lead**rO
    shift=Quad(1)
    for label,ri in zip(labels,r):
        shift*=theta_shift[label]**ri
        if label!='C0':
            val=3*D if label[0]=='C' else -lam
            expected*=val**(-ri)
            tame*=val**ri
    tame*=product
    assert tame==1 and norm_constant==expected
    value=function_value(unit,*P)
    image=function_value(unit,*piP)
    rhs=value**7/(image*norm_constant)
    assert shift==rhs
    records.append({'index':unit['index'],'divisor':r,
      'all_line_norms':line_norms,'product_f_on_nonzero_pi_kernel':product.key(),
      'Norm_pi_f_over_f':norm_constant.key(),'full_tame_product_theta_f':tame.key(),
      'theta_translated_product_at_P':shift.key(),'isogeny_ratio_at_P':rhs.key()})

# Literal regulator maps, retaining pullback, transfer, and all 3 factors.
AE=s.Matrix([[1,-3],[3,-2]])
pullback=AE.T
transfer=7*AE.inv().T
operator=7*transfer-s.eye(2)
assert pullback*transfer==transfer*pullback==7*s.eye(2)
assert operator==49*AE.inv().T-s.eye(2)
sm=local_smith(operator.tolist())
assert sm['valuations']==[1,2]
enc=lambda A:[[str(v) for v in A.row(i)] for i in range(A.rows)]

out={'status':'PASS',
 'scope':'literal theta/principal-unit norm identity and typed integral regulator operator; no division or actual handle value is inferred',
 'input_sha256':{name:hashlib.sha256((base/name).read_bytes()).hexdigest() for name in
                 ['a_cusp_unit_symbols.json','a_elliptic_theta_pi.json','a_e120_exact.py','a_local_smith.py']},
 'theta_O_leading':theta_lead.key(),'pi':pi.key(),
 'ordinary_test_point':{'field':'Q(zeta)[v]/(v^2+23/4)','X':P[0].key(),'Y':P[1].key(),
                       'pi_X':piP[0].key(),'pi_Y':piP[1].key()},
 'norm_records':records,
 'exact_function_identity':'product_t theta_pi(Q-t)^ord_t(f) = f(Q)^7 / (Norm_[pi] f)([pi]Q)',
 'Norm_pi_f_constant':'c_f=(3D)^r_O product_(t neq O) theta_pi(t)^(-r_t); Norm_pi f=c_f f',
 'literal_K2_identity':'(7 Norm_pi-1){f,g}=Norm_pi(sum_t ord_t(g){f,theta_pi(Q-t)})+{c_f,c_g}+{f,c_g}+{c_f,g}',
 'proper_regulator':{'pi_pullback':enc(pullback),'pi_transfer':enc(transfer),
     'seven_transfer_minus_identity':enc(operator),'inverse':enc(operator.inv()),
     'actual_tau_minus_identity':enc(49*AE.inv().T-s.eye(2)),
     'smith':encode(sm),'three_primary_factors':[3,9]},
 'proof_checks':{'actual_eight_unit_norms':8,'actual_full_tame_products':8,
                'exact_ordinary_point_function_identities':8,'all_inverse_and_projection_maps':True}}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all eight literal Norm_pi(f)=c_f f constants by exact six-point kernel products.')
print('PASS eight full tame products and exact theta/principal-unit distribution identities.')
print('PASS actual pi test point, cohomological pullback/transfer inverses, and residual Smith(3,9).')
