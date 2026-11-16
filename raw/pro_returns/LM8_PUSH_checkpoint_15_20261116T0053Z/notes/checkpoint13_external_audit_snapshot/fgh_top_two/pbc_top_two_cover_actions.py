#!/usr/bin/env python3
"""Actual Q104 actions on the two central C2 covers of A72.

Automorphisms fix the CHOSEN central C2 kernel (not necessarily the whole
center). A lift is (M,l): (v,z) -> (Mv,z+q_M(v)+l.v). The canonical q_M has
zero linear part and polar form c(Mv,Mw)+c(v,w). Exact normalizer equations
split the pullback extension with kernel A*, using the normal odd subgroup.
This file computes actions only, not the remaining obstruction values.
"""
from pathlib import Path
import hashlib,itertools,json,time
CODE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
start=time.time();source=CODE/'pbc_iterated_shortcut_v2_original_source.json'
s=json.loads(source.read_text());cp=CODE/'pbc_two_top_certificate.json';c=json.loads(cp.read_text())
assert c['source_sha256']==sha(source)
d=72;N=list(range(87,105));C={(i,j):w for i,j,w in s['conjugates']}
def tail(w):
    assert all(105<=i<=176 for i in w[::2])
    return sum((e%2)<<(i-105) for i,e in zip(w[::2],w[1::2]))
M={g:[tail(C[i,g]) for i in range(105,177)] for g in range(1,105)}
def action(v,mat):
    z=0
    while v:
        b=v&-v;v^=b;z^=mat[b.bit_length()-1]
    return z
def solve(rows):
    B={};count=0
    for v,rhs in rows:
        count+=1
        while v:
            p=v.bit_length()-1
            if p not in B:B[p]=(v,rhs);break
            w,b=B[p];v^=w;rhs^=b
        assert v or rhs==0,('inconsistent',count)
    x=0
    for p,(v,rhs) in sorted(B.items()):
        if ((v&x).bit_count()&1)^rhs:x|=1<<p
    return x,len(B),count
def quad(v,rows):
    z=0;w=v
    while w:
        b=w&-w;w^=b;z^=(rows[b.bit_length()-1]&v).bit_count()&1
    return z
pairs=list(itertools.combinations(range(d),2));outputs=[]
for fi,(hh,qr) in enumerate(zip(c['invariant_alternating_forms_hex'],c['quadratic_refinements']),1):
    B=int(hh,16);qlinear=int(qr['linear_part_hex'],16);crow=[0]*d
    for i in range(d):
        if qlinear>>i&1:crow[i]|=1<<i
    for k,(i,j) in enumerate(pairs):
        if B>>k&1:crow[i]|=1<<j
    def cocycle(v,w):
        z=0
        while v:
            b=v&-v;v^=b;z^=(crow[b.bit_length()-1]&w).bit_count()&1
        return z
    Q={}
    for g in range(1,105):
        rows=[0]*d
        for i,j in pairs:
            bit=cocycle(M[g][i],M[g][j])^((crow[i]>>j)&1)
            if bit:rows[i]|=1<<j
        # Preserved squares and alternating pairing make the cocycle
        # difference symmetric, with zero diagonal: this is an automorphism.
        for i in range(d):assert cocycle(M[g][i],M[g][i])==((qlinear>>i)&1)
        Q[g]=rows
    rows=[]
    for i in N:
        for k in range(d):
            mi=M[i][k];mi2=action(mi,M[i]);assert action(mi2,M[i])==1<<k
            v=(1<<k)^mi^mi2
            rhs=quad(mi,Q[i])^quad(mi2,Q[i])
            rows.append((v<<((i-87)*d),rhs))
    for i in N:
        for j in N:
            if i<=j:continue
            for k in range(d):
                assert action(M[i][k],M[j])==action(M[j][k],M[i])
                v=(((1<<k)^M[j][k])<<((i-87)*d))^(((1<<k)^M[i][k])<<((j-87)*d))
                rhs=quad(M[i][k],Q[j])^quad(M[j][k],Q[i])
                rows.append((v,rhs))
    sol,rank,count=solve(rows);assert rank==18*d-d
    assert all(((v&sol).bit_count()&1)==rhs for v,rhs in rows)
    L={i:(sol>>((i-87)*d))&((1<<d)-1) for i in N}
    def evaluate_N(v,w):
        z=0
        for i,e in zip(w[::2],w[1::2]):
            assert i in N and 0<=e<3
            for _ in range(e):
                z^=quad(v,Q[i])^((L[i]&v).bit_count()&1)
                v=action(v,M[i])
        return v,z
    ranks=[]
    for g in range(1,87):
        equations=[]
        for i in N:
            w=C[i,g];nw=[x for k,e in zip(w[::2],w[1::2]) if k<=104 for x in (k,e)]
            assert all(k in N for k in nw[::2])
            for k in range(d):
                image,z=evaluate_N(M[g][k],nw)
                assert image==action(M[i][k],M[g])
                rhs=z^quad(M[i][k],Q[g])^((L[i]>>k)&1)
                equations.append((M[i][k]^(1<<k),rhs))
        lg,rg,ct=solve(equations);assert rg==d
        assert all(((v&lg).bit_count()&1)==rhs for v,rhs in equations)
        L[g]=lg;ranks.append(rg)
        if g%10==0:print('COVER_ACTION_PROGRESS',fi,g,'seconds',time.time()-start,flush=True)
    outputs.append(dict(form_index=fi,normal_three_equations=count,normal_three_equation_rank=rank,
                        normalizer_ranks=ranks,chosen_kernel_fixed=True,
                        linear_action_corrections_hex={str(g):hex(L[g]) for g in range(1,105)}))
out=dict(status='PASS: actual central-cover action normalizer equations',
         source_sha256=sha(source),module_certificate_sha256=sha(cp),checker_sha256=sha(__file__),
         covers=outputs,seconds=time.time()-start,
         scope='Constructed actions on central class-two covers, fixing the chosen C2 kernel. The rank36 alternating form is degenerate. No target-bit value or full C31 conclusion.')
(CODE/'pbc_top_two_cover_actions.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','seconds','scope')},indent=2),flush=True)
