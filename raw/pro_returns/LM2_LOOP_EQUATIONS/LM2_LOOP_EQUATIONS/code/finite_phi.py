"""A genuine simultaneous-evaluation test of the section-47 condition.

The characteristic A4 envelope remembers BOTH the congruence inclusion j
and the orbifold quotient phi. This avoids evaluating phi on a residue in
a quotient through which phi does not factor.
"""
from pathlib import Path
from math import gcd
from collections import Counter
import json
from finite_groups import matrix_group,matmul,universal_envelope

HERE=Path(__file__).resolve().parent

def run_level(n):
    A=matrix_group(n,projective=True)
    canon=lambda a:min(a,tuple(-v%n for v in a))
    d=(n-1,0,0,1)
    outer=tuple(A.index[canon(matmul(matmul(d,a,n),d,n))] for a in A.elements)
    H,x,y,representatives=universal_envelope(A,[outer] if n==3 else [])
    print('level',n,'envelope constructed',H.n,flush=True)
    theta=H.map_from_generators(x,y,y,x)
    z=H.inv[H.mul(x,y)]
    omega=H.map_from_generators(x,y,y,z)
    assert theta and omega
    comm=H.mul(H.mul(H.mul(x,y),H.inv[x]),H.inv[y])
    derived=sorted(H.generated([c[comm] for c in H.conj]))
    S=A.index[canon((0,1,n-1,0))];R=A.index[canon((0,1,n-1,1))]
    jx=A.index[canon((1,0,2%n,1))];jy=A.power(A.mul(S,R),2)
    def evaluation(a,b):
        vals={H.e:A.e};todo=[H.e]
        for v in todo:
            for g,h in [(x,a),(y,b)]:
                q=H.mul(v,g);r=A.mul(vals[v],h)
                if q in vals:assert vals[q]==r
                else:vals[q]=r;todo.append(q)
        assert len(vals)==H.n
        return [vals[i] for i in range(H.n)]
    j=evaluation(jx,jy);phi=evaluation(S,A.mul(S,R))
    records=[]
    for lam in range(2*H.exponent):
        if gcd(lam,2*H.exponent)!=1:continue
        nu=(lam-1)//2
        for f in derived:
            if H.mul(f,theta[f])!=H.e:continue
            val=H.e
            for a in [omega[omega[f]],H.power(z,nu),omega[f],H.power(y,nu),f,H.power(x,nu)]:
                val=H.mul(val,a)
            if val!=H.e:continue
            ax=H.power(x,lam);ay=H.mul(H.mul(H.inv[f],H.power(y,lam)),f)
            generating=len(H.generated([ax,ay]))==H.n
            if not generating:continue
            xi=H.mul(H.power(y,nu),f)
            gauges=[];defects=[]
            for t in range(H.exponent):
                v=H.mul(H.mul(H.power(y,t),xi),H.power(x,-t))
                q=phi[v]
                rhs=A.mul(A.mul(A.mul(A.mul(q,S),A.inv[q]),A.inv[S]),A.power(jx,nu))
                defects.append(A.elements[A.mul(A.inv[j[v]],rhs)])
                if j[v]==rhs:gauges.append(t)
            records.append(dict(lambda_mod_2exponent=lam,f_index=f,
                f_coordinates=[A.elements[a] for a in H.elements[f]],
                phi_compatible_gauges=gauges,defects=defects))
    summary=dict(level=n,base=A.name,envelope_order=H.n,exponent=H.exponent,
                 derived_order=len(derived),generating_cycle_solutions=len(records),
                 compatible=sum(bool(r['phi_compatible_gauges']) for r in records),
                 incompatible=sum(not r['phi_compatible_gauges'] for r in records))
    result=dict(summary=summary,solutions=records,
                representing_pairs=[[A.elements[a],A.elements[b]] for a,b in representatives])
    print(json.dumps(summary),flush=True)
    for r in records:
        if not r['phi_compatible_gauges']:
            print('first incompatible certificate',json.dumps(r),flush=True);break
    return result

def main():
    results={n:run_level(n) for n in [2,3]}
    (HERE/'finite_phi.json').write_text(json.dumps(results,indent=2)+'\n')

if __name__=='__main__':main()
