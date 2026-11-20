"""Local checks for scans 013–015; no scan text is inferred by this script."""
from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
def red(word):
    out=[]
    for x in word:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def prod(*words):return red(x for w in words for x in w)
def apply(f,w):return red(y for x in w for y in (f[x] if x>0 else inv(f[-x])))
def compose(f,g):return {i:apply(f,g[i]) for i in (1,2)}
def inner(w):return {i:prod(w,(i,),inv(w)) for i in (1,2)}
a=(1,);b=(2,);c=(-2,-1)
sinf={1:b,2:a}
s0={1:prod(inv(b),inv(c)),2:c}
s1={1:c,2:prod(inv(c),inv(a))}
einf=compose(compose(inner(a),sinf),inner(c))
e0=compose(compose(inner(b),s0),inner(a))
e1=compose(compose(inner(c),s1),inner(b))
checks13=[]
for alpha in (1,2):
    w=prod(a,b,a,(-1,-2)*alpha,b,(-2,-1)*alpha)
    checks13.append({'statement':'main product with alpha='+str(alpha),'reduced_word':w,'identity':not w})
assert checks13[0]['identity'] and not checks13[1]['identity']
checks14=[]
for name,e,w in [('epsilon0',e0,a),('epsilon1',e1,b),('epsiloninfty',einf,c)]:
    lhs=compose(e,e);rhs=inner(w)
    checks14.append({'statement':name+' squared = inner(l_i)','left':lhs,'right':rhs,'equal':lhs==rhs})
    assert lhs==rhs
# Independent free group on A=epsilon0, B=epsilon1, C=epsiloninfty.
A=(1,);B=(2,);C=(3,)
R1=prod(B,B,A,B,inv(A),inv(A))
R2=prod(C,C,B,C,inv(B),inv(B))
R3=prod(A,A,C,A,inv(C),inv(C))
left=prod(R3,R2,R1)
v=prod(A,A,C)
right=prod(v,A,B,C,A,B,C,inv(v))
assert left==right
checks14.append({'statement':'R3 R2 R1 = (A^2 C)(A B C)^2(A^2 C)^-1','left_reduced':left,'right_reduced':right,'equal':left==right,'scope':'This word identity alone proves the indicated implication if all three R_i equal rho and rho^3=1; it does not prove their equality or independence.'})
checks15=[]
left=compose(compose(e0,e1),einf)
checks15.append({'statement':'epsilon0 epsilon1 epsiloninfty = sigma1','left':left,'right':s1,'equal':left==s1})
assert left==s1
for name,lhs,f,g in [('epsilon0=epsilon1 epsiloninfty epsilon1^-1',e0,e1,einf),('epsilon1=epsiloninfty epsilon0 epsiloninfty^-1',e1,einf,e0),('epsiloninfty=epsilon0 epsilon1 epsilon0^-1',einf,e0,e1)]:
    # Compare lhs*f with f*g, avoiding a separately computed inverse map.
    le=compose(lhs,f);ri=compose(f,g)
    checks15.append({'statement':name,'equivalent_left_images':le,'equivalent_right_images':ri,'equal':le==ri})
    assert le==ri
out={'encoding':'For automorphisms and scan013 words, 1=l0 and 2=l1, with linfty=(-2,-1). For the scan014 R_i identity only, 1=A,2=B,3=C. Negative integers mean inverse. Composition applies the right map first. All reductions cancel adjacent inverse pairs only.','scan013':checks13,'scan014':checks14,'scan015':checks15}
(E/'reader_reports/145_scans013_015_word_checks.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out))
