"""Literal local-square witnesses for both non-small Fisher quartics.

Once a nonzero quartic value is a local square, Hensel's criterion supplies
the actual point.  Away from the displayed finite support the quartic is
smooth of genus one, and the finite-field bound supplies a point.
"""
from pathlib import Path
from fractions import Fraction as F
import contextlib,io,runpy,json,math,itertools
BASE=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    D=runpy.run_path(str(BASE/'harmonic_prym_fisher_local_certificate.py'))
globals().update({k:v for k,v in D.items() if not k.startswith('__')})

def value_square(cs,x,p,root):
    val=polyval(cs,x)
    if val==ZERO:return False
    return local2(val)==0 if p==2 else square_odd(val,p,root)
def get_v(z,p,root):
    if z==ZERO:return 10**9
    return min(2*vp(z[0],2),2*vp(z[1],2)+1) if p==2 else odd_data(z,p,root)[0]
def candidate_valuations(cs,p,root):
    vs=[get_v(c,p,root) for c in cs]
    es={0,1,-1}
    for i in range(5):
        for j in range(i+1,5):
            if max(vs[i],vs[j])>=10**8:continue
            a=F(vs[i]-vs[j],j-i)
            fl=a.numerator//a.denominator
            es.update([fl-1,fl,fl+1,fl+2])
    return sorted(es,key=lambda x:(abs(x),x))
def residue(x,p,root):
    if root is None:return (modq(x[0],p),modq(x[1],p))
    D=math.lcm(x[0].denominator,x[1].denominator)
    A=int(x[0]*D);B=int(x[1]*D);vD=vp(D,p)
    rt=root_lift(root,p,vD+1);vv=(A+B*rt)%(p**(vD+1))
    assert vv%p**vD==0
    return (vv//p**vD*pow(D//p**vD,-1,p))%p
def residue_roots(cs,p,root):
    v=min(get_v(c,p,root) for c in cs if c!=ZERO)
    rs=[residue(div(c,F(p)**v),p,root) for c in cs]
    if root is not None:
        Z=sp.Symbol('Z')
        poly=sp.Poly(sum(int(c)*Z**i for i,c in enumerate(rs)),Z,modulus=p)
        return [k(int(z)%p) for z in poly.ground_roots()]
    out=[]
    for a in range(p):
        for bb in range(p):
            A=B=0
            for c,d in reversed(rs):
                A,B=(A*a+2*B*bb+c)%p,(A*bb+B*a+d)%p
            if A==B==0:out.append((F(a),F(bb)))
    return out
def shift_poly(cs,c,s):
    ans=[]
    for j in range(5):
        total=ZERO
        for i in range(j,5):total=add(total,mul(math.comb(i,j),mul(cs[i],power(c,i-j))))
        ans.append(mul(power(s,j),total))
    return ans
def recurse_witness(cs,p,root,origin=ZERO,scale=ONE,depth=0):
    if depth>8:return None
    samples=[k(a) for a in range(16)]
    if root is None:samples += [(F(a),F(bb)) for a in range(4) for bb in range(1,4)]
    for u in samples:
        if value_square(cs,u,p,root):return add(origin,mul(scale,u))
    for u in residue_roots(cs,p,root):
        new=shift_poly(cs,u,k(p))
        ans=recurse_witness(new,p,root,add(origin,mul(scale,u)),mul(scale,p),depth+1)
        if ans is not None:return ans
    return None
def finite_witness(cs,p,root):
    if value_square(cs,ZERO,p,root):return {'chart':'finite','x':ser(ZERO)}
    if cs[4]!=ZERO and (local2(cs[4])==0 if p==2 else square_odd(cs[4],p,root)):
        return {'chart':'infinity','coefficient':ser(cs[4])}
    pi=T if p==2 else k(p)
    es=candidate_valuations(cs,p,root)
    # Small units first, then a complete small-residue grid where feasible.
    candidates=[]
    if p==2:
        candidates=[(F(a),F(bb)) for a in range(-16,17) for bb in range(-8,9) if a%2]
    elif root is None:
        n=min(p,16)
        candidates=[(F(a),F(bb)) for a in range(n) for bb in range(n) if a or bb]
    else:
        candidates=[k(a) for a in range(1,min(p,256))]
    for e in es:
        pe=power(pi,e)
        for u in candidates:
            xx=mul(pe,u)
            if value_square(cs,xx,p,root):return {'chart':'finite','x':ser(xx)}
    if p!=2:
        for e in es:
            pe=power(k(p),e)
            ans=recurse_witness([mul(c,power(pe,i)) for i,c in enumerate(cs)],p,root,scale=pe)
            if ans is not None:
                assert value_square(cs,ans,p,root)
                return {'chart':'finite','x':ser(ans),'residue_recursion':True}
    return {'unresolved':True,'candidate_valuations':es}

rows=[]; unresolved=[]; supports={}
for name,cs in [('g2',g2),('g3',g3)]:
    den=math.lcm(*(q.denominator for c in cs for q in c))
    factors=sp.factorint(den)
    primes={2,3,7,13,23,139,191,r}|{int(p) for p in factors}
    assert all(prime(p) for p in primes)
    supports[name]={'denominator':str(den),'denominator_factors':{str(p):int(e) for p,e in factors.items()},'finite_support':sorted(primes)}
    print(name,'support',sorted(primes),flush=True)
    for p in sorted(primes):
        roots=[None] if p==2 else (sqrtmod(2,p) or [None])
        for root in roots:
            w=finite_witness(cs,p,root)
            row={'curve':name,'p':p,'root':root,**w}
            if 'unresolved' in w:unresolved.append(row)
            elif w['chart']=='finite':
                xx=tuple(F(z) for z in w['x']); vv=polyval(cs,xx)
                assert vv!=ZERO and value_square(cs,xx,p,root)
                row['value_local_class']=local2(vv) if p==2 else odd_data(vv,p,root)
            rows.append(row);print(row,flush=True)
    for embedding in [1,-1]:
        found=next((xx for xx in [ZERO,k(F(-1,M))]
                    if sign(polyval(cs,xx),embedding)>0),None)
        assert found is not None,(name,embedding)
        row={'curve':name,'real_embedding':embedding,'x':ser(found),'value_sign':1}
        rows.append(row);print(row,flush=True)
data={'supports':supports,'witnesses':rows,'unresolved':unresolved}
(BASE/'harmonic_prym_fisher_els_certificate_data.json').write_text(json.dumps(data,indent=2)+'\n')
print('Unresolved:',unresolved,flush=True)
assert not unresolved
print('PASS: both Fisher quartics are everywhere locally soluble, with all exceptional witnesses literal.')
