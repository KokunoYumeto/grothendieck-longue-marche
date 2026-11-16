#!/usr/bin/env python3
"""Exact Q_2(sqrt(-6)) logarithm determinant with a proved tail bound."""
from pathlib import Path
from fractions import Fraction as F
from dataclasses import dataclass
from math import comb, ceil
import json

BASE=Path(__file__).resolve().parent

def v2(q):
    q=F(q)
    if not q:
        return float('inf')
    def order(n):
        n=abs(n)
        return (n & -n).bit_length()-1
    return order(q.numerator)-order(q.denominator)

@dataclass(frozen=True)
class K:
    a:F
    b:F=F(0)
    def __post_init__(self):
        object.__setattr__(self,'a',F(self.a))
        object.__setattr__(self,'b',F(self.b))
    @staticmethod
    def coerce(z): return z if isinstance(z,K) else K(z)
    def __add__(self,z):
        z=K.coerce(z);return K(self.a+z.a,self.b+z.b)
    __radd__=__add__
    def __neg__(self): return K(-self.a,-self.b)
    def __sub__(self,z): return self+-K.coerce(z)
    def __rsub__(self,z): return K.coerce(z)+-self
    def __mul__(self,z):
        z=K.coerce(z);return K(self.a*z.a-6*self.b*z.b,self.a*z.b+self.b*z.a)
    __rmul__=__mul__
    def inverse(self):
        n=self.a*self.a+6*self.b*self.b
        assert n
        return K(self.a/n,-self.b/n)
    def __truediv__(self,z): return self*K.coerce(z).inverse()
    def __rtruediv__(self,z): return K.coerce(z)*self.inverse()
    def __pow__(self,n):
        if n<0:return self.inverse()**(-n)
        result=K(1);base=self
        while n:
            if n%2:result=result*base
            base=base*base;n//=2
        return result
    def valuation(self): return min(v2(self.a),v2(self.b)+F(1,2))
    def text(self): return [str(self.a),str(self.b)]

s=K(0,1)
b=8*s
P=(K(-2),K(-4,2))
R=(K(-5,4),K(37,-1))
assert R[1]**2==R[0]**3-2*s*R[0]
Q=(R[0]-2*s/R[0],R[1]*(1+2*s/R[0]**2))
def on_curve(P):return P[1]**2==P[0]**3+b*P[0]
assert on_curve(P) and on_curve(Q)
print('PASS: both rational quadratic-field points and the literal scaled dual-isogeny image')

def double(P):
    x,y=P
    m=(3*x*x+b)/(2*y)
    xx=m*m-2*x
    result=(xx,m*(x-xx)-y)
    assert on_curve(result)
    return result

def residue(q,n):
    q=F(q)
    assert v2(q)>=0
    return q.numerator*pow(q.denominator,-1,2**n)%(2**n)

records=[]
logs=[]
for name,point in [('P',P),('Q',Q)]:
    current=point
    k=0
    while (-current[0]/current[1]).valuation()<F(3,2):
        current=double(current);k+=1
        assert k<=8
    t=-current[0]/current[1]
    vt=t.valuation()
    assert k==2 and vt=={'P':F(3,2),'Q':F(2)}[name]
    assert vt>=F(3,2) and b.valuation()==F(7,2)
    assert current[0].valuation()==-2*vt
    assert current[1].valuation()==-3*vt
    # log_E(t)=sum binom(2n,n)b^n*t^(4n+1)/(4n+1).
    # Keep n=0,1; every n>=2 has valuation at least
    # 2*v(b)+9*v(t), since the denominator is odd.
    log=(t+2*b*t**5/5)/(2**k)
    tail=2*b.valuation()+9*vt-k
    errors=[ceil(tail),ceil(tail-F(1,2))]
    logs.append((log,errors))
    row={'point':name,'coordinates':[q.text() for q in point],
         'doublings':k,'multiple_coordinates':[q.text() for q in current],
         'parameter':t.text(),'parameter_valuation':str(vt),
         'log_approximation':log.text(),'tail_valuation_bound':str(tail),
         'coefficient_error_bounds':errors,
         'coefficient_valuations':[v2(log.a),v2(log.b)]}
    records.append(row)
    print(name,'doublings',k,'v2(t)',vt,'tail bound',tail,
          'coefficient error bounds',errors,'coefficient valuations',row['coefficient_valuations'])

L1,e1=logs[0];L2,e2=logs[1]
det=L1.a*L2.b-L2.a*L1.b
detval=v2(det)
error=min(e1[0]+v2(L2.b),v2(L1.a)+e2[1],
          e2[0]+v2(L1.b),v2(L2.a)+e1[1],
          e1[0]+e2[1],e2[0]+e1[1])
assert det and detval<error
scale=max(0,-int(min(v2(L1.a),v2(L1.b),v2(L2.a),v2(L2.b))))
modulus=12
assert min(e1+e2)+scale>=modulus
residues=[[residue(2**scale*log.a,modulus),residue(2**scale*log.b,modulus)] for log,_ in logs]
assert scale==1 and residues==[[2526,1435],[270,4006]]
assert detval==-1 and error==18
normalized=det/(F(2)**detval)
assert v2(normalized)==0
print('LOG SCALE',2**scale,'COEFFICIENT RESIDUES MOD',2**modulus,residues)
print('DETERMINANT v2',detval,'ERROR v2 >=',error,
      'normalized odd residue mod256',residue(normalized,8))
print('PASS: the true Q2 logarithms are linearly independent; the displayed determinant cannot vanish')
(BASE/'point3_fermat8_dyadic_regulator_certificate_data.json').write_text(
    json.dumps({'field':'Q(s), s^2=-6','elliptic_coefficient':'8s',
                'records':records,'log_scale':2**scale,'modulus':2**modulus,
                'scaled_coefficient_residues':residues,'determinant_valuation':detval,
                'determinant_error_valuation_bound':error,
                'normalized_odd_determinant_mod256':residue(normalized,8)},indent=2)+'\n')
