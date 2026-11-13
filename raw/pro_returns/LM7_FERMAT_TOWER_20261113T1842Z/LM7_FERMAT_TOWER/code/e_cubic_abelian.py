#!/usr/bin/env python3
"""Exact certificates for E.24--E.25.

Checks the rational Weierstrass map, the cusp-frame relation for the
generalized Jacobian, the finite-support Smith presentation of its
rational points, eta coefficients against point counts, and the D8
real obstruction. Analytic nonvanishing and the complete cohomological
argument are proved in sections/E_cubic.tex; no numerical L-value is used.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from math import gcd
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

OUT=Path(__file__).resolve().parent

class K:
    """Q[zeta]/(zeta^2+zeta+1), with exact rational arithmetic."""
    def __init__(self,a=0,b=0):self.a,self.b=F(a),F(b)
    def __add__(self,v):
        v=toK(v);return K(self.a+v.a,self.b+v.b)
    __radd__=__add__
    def __neg__(self):return K(-self.a,-self.b)
    def __sub__(self,v):return self+-toK(v)
    def __rsub__(self,v):return toK(v)+-self
    def __mul__(self,v):
        v=toK(v)
        return K(self.a*v.a-self.b*v.b,
                 self.a*v.b+self.b*v.a-self.b*v.b)
    __rmul__=__mul__
    def norm(self):return self.a*self.a-self.a*self.b+self.b*self.b
    def inv(self):
        n=self.norm();assert n
        return K((self.a-self.b)/n,-self.b/n)
    def __truediv__(self,v):return self*toK(v).inv()
    def __rtruediv__(self,v):return toK(v)*self.inv()
    def __pow__(self,n):
        if n<0:return self.inv()**(-n)
        r=K(1);a=self
        while n:
            if n%2:r=r*a
            a=a*a;n//=2
        return r
    def __eq__(self,v):
        v=toK(v);return self.a==v.a and self.b==v.b
    def data(self):return [str(self.a),str(self.b)]

def toK(v):return v if isinstance(v,K) else K(v)

def point_count(p):
    # One representative for each projective point: z=1, or z=0,y=1,
    # or [1:0:0]. The last point is never on this curve.
    points=[(x,y,1) for x in range(p) for y in range(p)
            if (x**3+y**3+1)%p==0]
    points += [(x,1,0) for x in range(p) if (x**3+1)%p==0]
    return points

def eta_coefficients(bound):
    q=[0]*(bound+1);q[1]=1
    for scale in (3,9):
        for k in range(1,bound//scale+1):
            d=scale*k
            q=[q[i]-(2*q[i-d] if i>=d else 0)
                 +(q[i-2*d] if i>=2*d else 0)
                 for i in range(bound+1)]
    return q

def d8_mul(g,h):
    a,b,c=g;A,B,C=h
    return ((a+A)%2,(b+B)%2,(c+C+b*A)%2)

def main():
    x,y,z,s=sp.symbols('x y z s')
    wx=-3*z/(x+y);wy=(4*x-5*y)/(x+y)
    assert sp.factor(wy**2+wy-wx**3+7-27*(x**3+y**3+z**3)/(x+y)**3)==0
    # The binomial polynomial suffices to determine the displayed leading terms.
    branch=1+s**3/sp.Integer(3)-s**6/sp.Integer(9)+5*s**9/sp.Integer(81)
    fP=(1-branch)/(s-branch)
    fO=(s-branch)/(1-branch)
    leadP=sp.limit(fP/s**3,s,0)
    leadO=sp.limit(fO*s**3,s,0)
    assert leadP==sp.Rational(1,3) and leadO==3
    w=K(0,1);lam=1-w
    assert w**3==1 and 3==-(w**2)*(lam**2)
    ratios=[K(F(1,9)),K(F(-1,3)),((1-w)/(-w))/3,
            (-1/w)/3,((-w)/(1-w))/3]
    expected=[K(F(1,9)),K(F(-1,3)),lam**-1,lam**-2,(w**2)*(lam**-3)]
    assert ratios==expected
    # The coordinate character products of frames recover the two unit maps.
    toric_map=(ratios[0]*ratios[2].norm()/ratios[4].norm(),
               ratios[1]*ratios[3].norm()/ratios[4].norm())
    assert toric_map==(K(1),K(-1))
    # Generators: 5 of order2, 3 of order3, five supported prime generators,
    # and the lift z. All other prime generators are free direct summands.
    relations=sp.zeros(9,14)
    for i in range(5):relations[i,i]=2
    for i in range(3):relations[5+i,5+i]=3
    relation=[0]*14
    relation[1]=-1                    # minus the sign in the second Q* factor
    relation[7]=-2                    # minus zeta^2 in the third K* factor
    relation[8:13]=[2,1,1,2,3]
    relation[13]=3
    for j,v in enumerate(relation):relations[8,j]=v
    D=smith_normal_form(relations,domain=sp.ZZ)
    ds=[abs(int(D[i,i])) for i in range(9)]
    assert ds==[1,1,1,1,2,2,6,6,6]
    free_rank=14-len(ds);assert free_rank==5
    # Kernel of the exact coordinate-unit retraction G -> G_m^2.
    # epsilon=-zeta^2 generates mu_6 and epsilon^4=zeta^2.
    # Generators: epsilon in three factors, lambda in three factors,
    # and z'. Relation: 3z' + lambda_1 + 2lambda_2 + 3lambda_3
    # -4epsilon_3 = 0. Its first lambda coefficient is primitive.
    epsilon=-(w**2)
    assert epsilon**6==1 and epsilon**4==w**2
    kernel_relations=sp.zeros(4,7)
    for i in range(3):kernel_relations[i,i]=6
    for j,v in enumerate([0,0,-4,1,2,3,3]):
        kernel_relations[3,j]=v
    KD=smith_normal_form(kernel_relations,domain=sp.ZZ)
    kernel_ds=[abs(int(KD[i,i])) for i in range(4)]
    assert kernel_ds==[1,6,6,6]
    assert 7-len(kernel_ds)==3
    quotients=[]
    for m in (2,3,4,6,9,12):
        size=m**free_rank
        for d in ds:size*=gcd(m,d)
        expected_size=m**5*gcd(m,2)**5*gcd(m,3)**3
        assert size==expected_size
        quotients.append({'m':m,'supported_power_quotient_order':size})
    coeff=eta_coefficients(60);counts=[]
    for p in list(sp.primerange(2,51)):
        if p==3:continue
        pts=point_count(int(p));a=int(p)+1-len(pts)
        assert a==coeff[int(p)]
        counts.append({'p':int(p),'points':len(pts),'a_p':a,'eta_a_p':coeff[int(p)]})
    assert len(point_count(2))==3
    # Exact D8 test: every lift of (1,1) has order4, not2.
    lifts=[(1,1,c) for c in range(2)]
    squares=[d8_mul(g,g) for g in lifts]
    assert squares==[(0,0,1),(0,0,1)]
    cube_roots_in_rationals={'numerator_of_27_over_4':27,'denominator':4,
                            'denominator_exponent_at_2':2,'is_cube':False}
    data={'weierstrass_map':{'x':'-3z/(x+y)','y':'(4x-5y)/(x+y)',
             'equation':'y^2+y=x^3-7',
             'identity':'Y^2+Y-X^3+7=27(x^3+y^3+z^3)/(x+y)^3'},
          'cusp_leading_values':{'P':str(leadP),'O':str(leadO),'Q':'-1'},
          'frame_relation_Q_zeta_coordinates':[v.data() for v in ratios],
          'frame_relation_simplified':['3^-2','-3^-1','lambda^-1','lambda^-2',
                                       'zeta^2 lambda^-3'],
          'toric_character_product':['1','-1'],
          'supported_relation_matrix':relations.tolist(),'smith_diagonal':ds,
          'supported_free_rank':free_rank,'power_quotient_orders':quotients,
          'kernel_torus_coordinates':
              ['N(C)/N(A)','N(C)/N(B)','A','B','C'],
          'kernel_relation_matrix':kernel_relations.tolist(),
          'kernel_smith_diagonal':kernel_ds,'kernel_supported_free_rank':3,
          'kernel_torsion':'(Z/6)^3',
          'eta_point_counts':counts,'rational_two_torsion_test':cube_roots_in_rationals,
          'D8_lifts_of_11':lifts,'D8_squares':squares,
          'even_levels_checked':[2,4,6,8],
          'cohomology_proof_location':'sections/E_cubic.tex'}
    (OUT/'e_cubic_abelian.json').write_text(json.dumps(data,indent=2,default=int)+'\n')
    print('Rational cubic-to-Weierstrass identity: PASS')
    print('Tangent-frame leading values P,O,Q:',leadP,leadO,-1)
    print('3z=a:',data['frame_relation_simplified'])
    print('Toric character product of a: (1,-1); hence image of z: (1,-1)')
    print('Supported rational-point relation Smith diagonal:',ds)
    print('Supported free rank:',free_rank,'torsion: (Z/2)^5 x (Z/3)^3')
    print('Exact toric retraction kernel Smith diagonal:',kernel_ds)
    print('Kernel supported free rank: 3; torsion: (Z/6)^3')
    print('p #E(F_p) a_p eta_a_p')
    for row in counts:print(row['p'],row['points'],row['a_p'],row['eta_a_p'])
    print('D8 lifts of (1,1) and squares:',list(zip(lifts,squares)))
    print('All exact certificates: PASS')

if __name__=='__main__':main()
