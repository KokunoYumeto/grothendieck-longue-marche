"""Experimental exact Frobenius coefficients from normalized Cantor doubling.

This script is a probe until its comparison theorem has been independently
proved.  It is checked against independent point-character computations.
"""
import json,time
from pathlib import Path
from finite_jacobian import *

def doubling_coefficient(J,D):
    """Return (2D,c) for monic degree-five model, based at infinity."""
    F,R=J.F,J.R;u1,v1=D
    assert J.f[-1]==1 and D!=J.zero
    d1,a0,b0=R.xgcd(u1,u1)
    d,e,c=R.xgcd(d1,J.h)
    a=R.mul(e,a0);b=R.mul(e,b0)
    u=R.exact(R.sq(u1),R.sq(d))
    num=R.add(R.add(R.mul(R.mul(a,u1),v1),R.mul(R.mul(b,u1),v1)),R.mul(c,R.add(R.sq(v1),J.f)))
    v=R.mod(R.exact(num,d),u)
    if len(d)==2:
        assert len(u1)==3 and len(u)==3
        out=R.monic(u),v
        coeff=J.h[2] if len(J.h)>2 else 0
    elif len(u)<=3:
        assert d==(1,),('impossible odd-torsion cancellation',D,d)
        assert len(u1)==2 and len(u)==3
        out=R.monic(u),v
        coeff=J.h[1] if len(J.h)>1 else 0
    else:
        assert d==(1,),('impossible odd-torsion cancellation',D,d)
        nn=R.exact(R.add(R.add(R.sq(v),R.mul(J.h,v)),J.f),u)
        unew=R.monic(nn);vnew=R.mod(R.add(v,J.h),unew)
        out=unew,vnew
        if len(unew)==3:
            assert len(v)==4
            coeff=F.mul(v[3],unew[1])
        else:
            assert len(unew)==2
            coeff=1
    assert out==J.add(D,D)
    return out,coeff

def power_coefficient(J,D,d):
    a=1;E=D
    for _ in range(d):
        E,c=doubling_coefficient(J,E);a=J.F.mul(J.F.mul(a,a),c)
    return E,a

def main():
    F=BinaryField(67);R=PolynomialRing(F);a=F.embed_f4();h=(a,1,1)
    J=Jacobian(F,h,R.mul(h,(a^1,1,1,1)));elts=J.enumerate()
    tors=[D for D in elts if J.scale(D,7)==J.zero and D!=J.zero]
    assert len(tors)==48
    frob=lambda D,q:tuple(tuple(F.power(c,q) for c in poly) for poly in D)
    eig=[D for D in tors if frob(D,4)==J.scale(D,4)]
    assert len(eig)==6
    outputs=[]
    for q,d,points in [(4,2,eig),(64,6,tors)]:
        seen=set();covers=[]
        for D in points:
            if D in seen:continue
            subgroup=[J.scale(D,i) for i in range(1,7)];seen.update(subgroup)
            cs=[power_coefficient(J,E,d)[1] for E in subgroup]
            covers.append({'D':D,'Frobenius_coefficients':cs,'predicts_L1':all(c!=1 for c in cs)})
        outputs.append({'q':q,'covers':covers,'predicted_good_covers':sum(x['predicts_L1'] for x in covers)})
    source=json.loads((Path(__file__).parent/'A4_203_F64_output.json').read_text())
    actual=[x for x in source['tests'] if x['point']=='infinity' and x['ell']==7]
    outputs.append({'independent_point_character_good_F64':sum(x['L1_passes'] for x in actual),'independent_point_character_total_F64':len(actual)})
    assert outputs[0]['predicted_good_covers']==1
    assert outputs[1]['predicted_good_covers']==sum(x['L1_passes'] for x in actual)
    print(json.dumps({'status':'experimental formula checked against independent census','curve':'203','outputs':outputs},indent=2))

if __name__=='__main__':main()
