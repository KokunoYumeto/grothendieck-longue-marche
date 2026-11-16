"""Complete F_q-isomorphism representatives of genus-two curves in char 2.

Artin--Schreier pole types are (5), (3,1), (1,1,1). The last type
has split, quadratic, and cubic Frobenius orbits. We quotient the
explicit normal forms by their entire PGL2 stabilizers and by the
constant Artin--Schreier image. Isomorphisms are over F_q, not over
an algebraic closure; coefficient Frobenius is not divided out.
"""
from itertools import product
from finite_jacobian import *
from even_jacobian import *

def representatives(F):
    R=PolynomialRing(F);q=F.q;tau=next(a for a in range(q) if F.trace(a));cs=(0,tau)
    cn=lambda c:tau if F.trace(c) else 0
    done=set()
    for par in product(range(1,q),range(q),range(q),cs):
        if par in done:continue
        a,b,c,d=par;orb=set()
        for u in range(1,q):
            for v in range(q):
                a1=F.mul(a,F.power(u,5));b1=F.mul(b,F.power(u,3))
                r2=F.sqrt(F.mul(a,F.mul(F.power(u,4),v)))
                r1=F.sqrt(F.mul(b,F.mul(F.power(u,2),v))^r2)
                c1=F.mul(a,F.mul(u,F.power(v,4)))^F.mul(b,F.mul(u,F.power(v,2)))^F.mul(c,u)^r1
                d1=cn(F.mul(a,F.power(v,5))^F.mul(b,F.power(v,3))^F.mul(c,v)^d)
                orb.add((a1,b1,c1,d1))
        done.update(orb);a,b,c,d=min(orb)
        yield {'type':'rank0','parameters':(a,b,c,d),'orbit_size':len(orb),'h':(1,),'f':(d,c,0,b,0,a),'even':False}
    done=set()
    for par in product(range(1,q),range(q),range(1,q),cs):
        if par in done:continue
        a,b,c,d=par
        orb={(F.mul(a,F.power(u,3)),F.mul(b,u),F.div(c,u),d) for u in range(1,q)}
        done.update(orb);a,b,c,d=min(orb)
        yield {'type':'rank1','parameters':(a,b,c,d),'orbit_size':len(orb),'h':(0,1),'f':(0,c,d,b,0,a),'even':False}
    done=set();h=(0,1,1);hh=R.sq(h)
    for par in product(range(1,q),range(1,q),range(1,q),cs):
        if par in done:continue
        orb={par};queue=[par]
        while queue:
            a,b,c,d=queue.pop()
            for z in [(a,c,b,cn(d^a)),(b,a,c,cn(d^c))]:
                if z not in orb:orb.add(z);queue.append(z)
        done.update(orb);a,b,c,d=min(orb)
        f=R.add(R.mul((d,a),hh),R.add(R.scale((0,1,0,1),b),R.scale((0,0,1,1),c)))
        yield {'type':'ordinary_split','parameters':(a,b,c,d),'orbit_size':len(orb),'h':h,'f':f,'even':False}
    done=set();h=(tau,1,1);hh=R.sq(h)
    for par in product(range(1,q),range(q),range(q),cs):
        a,b,c,d=par
        if b==c==0 or par in done:continue
        orb={par,(a,b,c^b,cn(d^a))};done.update(orb);a,b,c,d=min(orb)
        f=R.add(R.mul((d,a),hh),R.mul((c,b),h))
        yield {'type':'ordinary_quadratic','parameters':(a,b,c,d),'orbit_size':len(orb),'h':h,'f':f,'even':False}
    h=next((a,b,c,1) for a,b,c in product(range(q),repeat=3) if all(R.eval((a,b,c,1),x) for x in range(q)))
    def powpoly(a,n):
        z=(1,)
        for _ in range(n):z=R.mul(z,a)
        return z
    def transform(f,m):
        a,b,c,d=m;out=()
        for i,x in enumerate(f):out=R.add(out,R.scale(R.mul(powpoly((b,a),i),powpoly((d,c),3-i)),x))
        return out
    mats=[]
    for a,b,c,d in [(1,b,c,d) for b,c,d in product(range(q),repeat=3)]+[(0,1,c,d) for c in range(1,q) for d in range(q)]:
        if F.mul(a,d)==F.mul(b,c):continue
        m=(a,b,c,d);ht=transform(h,m)
        if len(ht)==4 and R.monic(ht)==h:mats.append((m,ht[-1]))
    assert len(mats)==3,(q,h,mats)
    done=set()
    for a,b,c,d in product(range(q),range(q),range(q),cs):
        par=(a,b,c,d)
        if a==b==c==0 or par in done:continue
        orb=set()
        for m,lam in mats:
            nt=R.scale(transform((a,b,c),m),F.inv(lam))
            constant=nt[3] if len(nt)==4 else 0
            nt=R.add(nt,R.scale(h,constant));nt=tuple(nt)+(0,)*(3-len(nt))
            orb.add((*nt,cn(d^constant)))
        done.update(orb);a,b,c,d=min(orb)
        J,iso=normalize_rational_infinity(F,h,(a,b,c),d)
        yield {'type':'ordinary_cubic','parameters':(a,b,c,d),'orbit_size':len(orb),'original_h':h,'original_n':(a,b,c),'original_constant':d,'h':J.h if J else None,'f':J.f if J else None,'isomorphism':iso,'even':True,'pointless':J is None}

if __name__=='__main__':
    import json,collections
    for modulus in (7,11,19):
        F=BinaryField(modulus);reps=list(representatives(F));counts=collections.Counter(r['type'] for r in reps)
        masses=collections.Counter()
        for r in reps:masses[r['type']]+=r['orbit_size']
        print(json.dumps({'q':F.q,'representatives':len(reps),'by_type':counts,'parameter_orbit_sums':masses,'pointless_cubic_models':sum(r.get('pointless',False) for r in reps)}))
