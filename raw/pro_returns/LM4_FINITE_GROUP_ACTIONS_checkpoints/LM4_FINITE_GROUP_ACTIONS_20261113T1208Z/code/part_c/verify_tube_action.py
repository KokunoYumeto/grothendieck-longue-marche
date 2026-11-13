"""Exact word and mod-2 checks for LM4 B.30--B.32.

No numerical surface approximation is used.  The genus-g presentation is
R=x_0...x_(g-1) p_0^-1 x_0^-1 p_0 ... p_(g-1)^-1 x_(g-1)^-1 p_(g-1).
The checked finite word certificates supplement the cell proof in b_extra.tex.
"""
from pathlib import Path
import json


def red(w):
    out=[]
    for a in w:
        if out and out[-1]==-a:
            out.pop()
        else:
            out.append(a)
    return tuple(out)


def mul(*ws):
    return red(a for w in ws for a in w)


def inv(w):
    return tuple(-a for a in reversed(w))


def subst(w,f):
    return mul(*(f[a-1] if a>0 else inv(f[-a-1]) for a in w))


def cyclic(w):
    w=red(w)
    while len(w)>1 and w[0]==-w[-1]:
        w=w[1:-1]
    return w


def same_cyclic(w,v):
    w,v=cyclic(w),cyclic(v)
    return len(w)==len(v) and any(w==v[i:]+v[:i] for i in range(len(v)))


def model(g):
    n=2*g
    x=[(j+1,) for j in range(g)]
    p=[(g+j+1,) for j in range(g)]
    x += [mul(inv(p[j]),inv(x[j]),p[j]) for j in range(g)]
    p += [inv(w) for w in p]
    prefix=()
    u=[]
    for w in x:
        prefix=mul(prefix,w)
        u.append(inv(prefix))
    relation=prefix
    u[-1]=()
    q=[mul(inv(u[j]),p[j],u[(j+g-1)%n]) for j in range(n)]
    r=tuple(x[(j+1)%n] for j in range(g))+tuple(p[j+1] for j in range(g))
    s=tuple(mul(inv(u[-j%n]),x[-j%n],u[-j%n]) for j in range(g))+tuple(q[-j%n] for j in range(g))
    t=tuple(mul(inv(u[(j+g-1)%n]),inv(x[j+g]),u[(j+g-1)%n]) for j in range(g))+tuple(inv(q[j]) for j in range(g))
    twists=[]
    for k in range(g):
        twists.append(tuple(x[:g])+tuple(mul(x[j],p[j]) if j==k else p[j] for j in range(g)))
    return dict(g=g,n=n,x=x,p=p,u=u,q=q,R=relation,r=r,s=s,t=t,twists=twists)


def mat(f):
    n=len(f)
    m=[[0]*n for _ in range(n)]
    for j,w in enumerate(f):
        for a in w:
            m[abs(a)-1][j]+=1 if a>0 else -1
    return m


def mm(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def ident(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]


def powm(a,n):
    out=ident(len(a))
    for _ in range(n):
        out=mm(out,a)
    return out


def spin_check(g):
    # Enumerate every skew matrix of transversal intersections modulo 2.
    count=0
    for bits in range(1<<(g*(g-1)//2)):
        jmat=[[0]*(2*g) for _ in range(2*g)]
        for i in range(g):
            jmat[i][g+i]=jmat[g+i][i]=1
        k=0
        for i in range(g):
            for j in range(i+1,g):
                jmat[g+i][g+j]=jmat[g+j][g+i]=(bits>>k)&1
                k+=1
        def pairing(v,w):
            return sum(v[i]*jmat[i][j]*w[j] for i in range(2*g) for j in range(2*g))%2
        def q(v):
            return (sum(v)+sum(v[i]*v[j]*jmat[i][j] for i in range(2*g) for j in range(i+1,2*g)))%2
        basis=[[int(i==j) for i in range(2*g)] for j in range(2*g)]
        for mask in range(1<<(2*g)):
            v=[(mask>>i)&1 for i in range(2*g)]
            for e in basis:
                p=pairing(v,e)
                assert q([(v[i]+p*e[i])%2 for i in range(2*g)])==q(v)
        d=[int(i in (0,1)) for i in range(2*g)]
        assert q(d)==0
        v=basis[g]
        assert pairing(v,d)==1
        assert q([(v[i]+d[i])%2 for i in range(2*g)])!=q(v)
        count+=1
    return count


def main():
    output={"word_checks":[],"spin_checks":[]}
    for g in range(2,9):
        a=model(g)
        r,s,t=(mat(a[k]) for k in ('r','s','t'))
        e=ident(2*g)
        assert powm(r,2*g)==e
        assert mm(s,s)==e and mm(t,t)==e
        assert mm(mm(s,r),s)==powm(r,2*g-1)
        assert mm(t,r)==mm(r,t) and mm(t,s)==mm(s,t)
        orientations={}
        for k,sign in [('r',1),('s',1),('t',-1)]:
            image=subst(a['R'],a[k])
            orientations[k]=same_cyclic(image,a['R'] if sign==1 else inv(a['R']))
            assert orientations[k],(g,k,image,a['R'])
        for j,f in enumerate(a['twists']):
            assert subst(a['R'],f)==a['R']
            fm=mat(f)
            assert mm(mm(r,fm),powm(r,2*g-1))==mat(a['twists'][(j+1)%g])
            assert mm(mm(s,fm),s)==mat(a['twists'][(-j)%g])
            assert mm(mm(t,fm),t)==mat(tuple(subst((k+1,), tuple(a['x'][:g])+tuple(mul(inv(a['x'][l]),a['p'][l]) if l==j else a['p'][l] for l in range(g))) for k in range(2*g)))
        output['word_checks'].append({"g":g,"relator_length":len(a['R']),"r_s_tau_preserve_relator_with_orientation":orientations,"all_twists_fix_relator_exactly":True,"all_finite_and_semidirect_relations_on_integral_homology":True})
    for g in range(2,5):
        output['spin_checks'].append({"g":g,"all_transversal_intersection_matrices":spin_check(g),"all_vectors_and_generating_transvections_checked":True,"band_sum_twist_breaks_quadratic_form":True})
    destination=Path(__file__).with_name('verify_tube_action_output.json')
    destination.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))


if __name__=='__main__':
    main()
