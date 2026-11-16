"""Targeted genuine B4 specializations against the known finite A5 fake table.

This is a necessary-condition probe, not a full canonical-word construction.
The two standard braid generators T,U satisfy TUT=UTU; set sigma_1=sigma_3=T,
sigma_2=U. All pure braid and pentagon inputs are then genuine.
"""
from contextlib import redirect_stdout
from io import StringIO
from collections import Counter
with redirect_stdout(StringIO()):
    import check_a5_duality_orbits as G
L,m,iv,e,pr,li,qm,qiv,qe=G.L,G.m,G.iv,G.e,G.pr,G.li,G.qm,G.qiv,G.qe

def mul(*xs):
    z=e
    for x in xs:z=m[z][x]
    return z
def conj(x,y):return mul(x,y,iv[x])
def power(x,n):
    z=e
    for _ in range(n):z=m[z][x]
    return z

tab=[e]*19
tab[4]=G.ix[(0,2,2,0)]
tab[10]=G.ix[(0,3,3,0)]
def value(a,b):
    if (pr[a],pr[b]) in G.orbits:
        j,au=G.orbits[pr[a],pr[b]]
        return au[tab[j]]
    return e

count=bad=0;patterns=Counter();witness=None
for T in range(120):
 for U in range(120):
    if mul(T,U,T)!=mul(U,T,U):continue
    count+=1
    # A_ij=sigma_(j-1)...sigma_(i+1) sigma_i^2
    #       sigma_(i+1)^-1...sigma_(j-1)^-1.
    a=power(T,2);c=power(U,2);f=a
    b=conj(U,a);ee=conj(T,c);d=conj(mul(T,U),a)
    ps=[(a,mul(c,ee)),(mul(b,c),f),(c,f),(mul(a,b),mul(ee,f)),(a,c)]
    vals=[value(*p) for p in ps]
    lhs=mul(vals[0],vals[1]);rhs=mul(vals[2],vals[3],vals[4])
    sig=[]
    for aa,bb in ps:
        if (pr[aa],pr[bb]) in G.orbits:sig.append(('A5',G.orbits[pr[aa],pr[bb]][0]))
        else:sig.append(('proper',len(G.subgroup(pr[aa],pr[bb])),mul(aa,bb)==mul(bb,aa)))
    patterns[tuple(sig)]+=1
    if lhs!=rhs:
        bad+=1
        if witness is None:witness=(T,U,[a,b,c,d,ee,f],ps,vals,sig,lhs,rhs)
print('Genuine B4 representations of the form sigma1=sigma3:',count)
print('Distinct pentagon orbit patterns:',len(patterns))
print('Violations of the particular fake A5 table with proper evaluations 1:',bad)
if witness:
    T,U,pure,ps,vals,sig,lhs,rhs=witness
    print('Witness T,U:',L[T],L[U])
    print('Pure generators A12,A13,A23,A14,A24,A34:',[L[x] for x in pure])
    print('Pentagon signatures:',sig)
    print('Five values:',[L[x] for x in vals])
    print('LHS,RHS:',L[lhs],L[rhs])
print('No arbitrary finite assignment is claimed to lift to a full word or full involution.')
