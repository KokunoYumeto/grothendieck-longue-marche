#!/usr/bin/env python3
"""Audit the auxiliary central ramification of the explicit norm witnesses.

An actual cubic residue extension is constructed from each irreducible
denominator h, and the three candidate points are tested on the curve.
Their Frobenius traces determine the divisor class needed for an etale
central twist.  No etaleness conclusion is inferred from the norm alone.
"""
from pathlib import Path
import json
from bc_miller_norm import *

data=json.loads(Path(__file__).with_name('bc_miller_norm_rr.json').read_text())
Q=tuple(F(c) for c in data['Q'])
a,_=miller3(Q)
zeta=F(2)
results=[]
cleaned_cover=None

for index,row in enumerate(data['witnesses']):
    h=tuple(F(c) for c in row['denominator_h3'])
    if any(not peval(h,v) for v in FIELD):
        results.append({'witness':index,'denominator_irreducible':False})
        continue
    modulus=tuple(c/h[-1] for c in h)

    class G:
        __slots__=('v',)
        def __init__(self,v=0):
            self.v=v.v if isinstance(v,G) else ((F(v),Z,Z) if isinstance(v,(int,F)) else tuple(F(c) for c in v))
        def __add__(self,b): return G(tuple(x+y for x,y in zip(self.v,G(b).v)))
        __radd__=__add__
        def __neg__(self): return G(tuple(-x for x in self.v))
        def __sub__(self,b): return self+-G(b)
        def __rsub__(self,b): return G(b)+-self
        def __mul__(self,b):
            out=[Z]*5
            for i,x in enumerate(self.v):
                for j,y in enumerate(G(b).v): out[i+j]+=x*y
            for j in (4,3):
                c=out[j]
                for k in range(3): out[j-3+k]-=c*modulus[k]
            return G(out[:3])
        __rmul__=__mul__
        def __pow__(self,n):
            if n<0:
                assert self
                return self**((343**3-1)-((-n)%(343**3-1)))
            ans,b=G(1),self
            while n:
                if n&1: ans*=b
                b*=b
                n>>=1
            return ans
        def __truediv__(self,b):
            assert G(b)
            return self*G(b)**(343**3-2)
        def __rtruediv__(self,b): return G(b)/self
        def __bool__(self): return any(self.v)
        def __eq__(self,b): return self.v==G(b).v

    alpha=G((Z,ONE,Z))
    assert sum((G(c)*alpha**i for i,c in enumerate(h)),G(0))==0
    assert alpha**(343**3)==alpha and alpha**343!=alpha
    x=alpha**3+3
    p=tuple(F(c) for c in row['numerator_p5'])
    def ev(p,v):
        out=G(0)
        for c in reversed(p): out=out*v+c
        return out
    ramification=[]
    trace_functions=[]
    for i in range(3):
        y=-ev(p,alpha*(zeta**i))
        if y*y+y!=x**3:
            continue
        R=(x,y)
        Rq=tuple(v**343 for v in R)
        Rqq=tuple(v**343 for v in Rq)
        trace=add(add(R,Rq),Rqq)
        assert trace is None or all(not v.v[1] and not v.v[2] for v in trace)
        traceF=None if trace is None else tuple(v.v[0] for v in trace)
        if index==0:
            assert trace is not None
            R01=add(R,Rq)
            assert R01 is not None and R01!=neg(Rqq)
            lam1=(Rq[1]-R[1])/(Rq[0]-R[0])
            nu1=R[1]-lam1*R[0]
            lam2=(Rqq[1]-R01[1])/(Rqq[0]-R01[0])
            nu2=R01[1]-lam2*R01[0]
            c1=lam1*lam2+R01[0]
            c0=lam1*nu2+nu1*lam2+R01[0]*c1
            b0=-(lam1+lam2)
            assert -R01[0]*c0==nu1*nu2
            assert -R01[0]*b0==-1-nu1-nu2
            coeffs=[c0,c1,G(1),b0]
            assert all(not v.v[1] and not v.v[2] for v in coeffs)
            f=((tuple(v.v[0] for v in coeffs[:3]),(coeffs[3].v[0],)),vertical(traceF))
            trace_functions.append((i,traceF,f))
        ramification.append({'numerator_zero_at_zeta_power':i,
                             'central_residue_exponent_mod3':i,
                             'point_trace':encP(traceF),
                             'trace_order_divides3':times(3,traceF) is None,
                             'trace_order_divides9':times(9,traceF) is None})
    assert len(ramification)==2
    total=None
    for r in ramification:
        P0=None if r['point_trace'] is None else tuple(F(c) for c in r['point_trace'])
        total=add(total,times(r['central_residue_exponent_mod3'],P0))
    if index==0:
        assert [r['numerator_zero_at_zeta_power'] for r in ramification]==[1,2]
        T1,T2=trace_functions[0][1],trace_functions[1][1]
        assert T1==neg(T2) and total==T2
        S0=next(P for P in points if times(3,P)==total)
        mS,_=miller3(S0)
        mS_min=(tuple(pexact(p,vertical(times(2,S0))) for p in mS[0]),vertical(total))
        assert feq(mS,mS_min)
        # The first chosen norm has order vector (0,0,3) over Q, so its
        # central radical has no residue at this interior point.
        assert row['orders_at_lifts_Q']==[0,0,3]
        root_values=[r for r in FIELD if r**3==Q[0]-3]
        order_index=root_values.index(zeta*root_values[0])
        assert (row['orders_at_lifts_Q'][0]+2*row['orders_at_lifts_Q'][order_index])%3==0
        cleaned_cover={
            'field':'F7[theta]/(theta^3-2)',
            'curve':'y^2+y=x^3',
            'Q':encP(Q), 'S':encP(S0),'T1':encP(T1),'T2':encP(T2),
            'three_S_equals_T2':True,
            'a':encf(a),'b':'x-3',
            'norm_witness_numerator_p5':row['numerator_p5'],
            'norm_witness_denominator_h3':row['denominator_h3'],
            'f1':encf(trace_functions[0][2]),'f2':encf(trace_functions[1][2]),
            'miller_3S':encf(mS_min),
            'central_twist':'f=miller_3S/(f1*f2^2*(x-x(T2)))',
            'div_f':'3(S)+6(O)-R1-2(R2), with R1,R2 the degree-three auxiliary points',
            'central_radical':'r=f*u(v)*u(zeta*v)^2',
            'cover_equations':['v^3=b','w^3=a','z^3=r'],
            'sigma':['v->zeta*v','w->w','z->u(zeta^2*v)*z/w'],
            'tau':['v->v','w->zeta*w','z->z'],
            'rho':['v->v','w->w','z->zeta*z'],
            'tangent_leading_a':2,'tangent_leading_b':2,
            'tangent_exponent_r':4,'tangent_leading_r':1,
            'tangent_constants_explanation':'a,b retain s-leading 9 over Q (2 mod7); u~v, zeta^2*9=1 mod7, f~s^6/3^6 and 3^6=1 mod7',
            'all_auxiliary_ramification_removed':True}
    results.append({'witness':index,'denominator_irreducible':True,
                    'ramification_points':ramification,
                    'weighted_ramification_trace':encP(total),
                    'weighted_trace_order_divides3':times(3,total) is None,
                    'weighted_trace_order_divides9':times(9,total) is None})

out={'Q':encP(Q),'results':results,'cleaned_cover':cleaned_cover,
     'scope':'Exact auxiliary divisor and Frobenius-trace audit. No based Frobenius cochain inferred.'}
encoded=json.dumps(out,indent=2)+'\n'
print(encoded,end='')
Path(__file__).with_suffix('.json').write_text(encoded)
