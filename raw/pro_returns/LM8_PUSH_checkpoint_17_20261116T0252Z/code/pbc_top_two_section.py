#!/usr/bin/env python3
"""Construct an actual section of G176 -> G104 by exact F2 equations.

The chosen Hall-three subgroup above the elementary normal 3^18 is first
constructed in the ORIGINAL presentation.  Its normalizer supplies the
unique correcting A-vector over every quotient generator, since A^N=0.
No target-bit or C31 conclusion is made by this calculation.
"""
from pathlib import Path
import hashlib,itertools,json,time
CODE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
start=time.time();source=CODE/'pbc_iterated_shortcut_v2_original_source.json'
s=json.loads(source.read_text());cert=CODE/'pbc_two_top_certificate.json'
c=json.loads(cert.read_text());assert c['status']=='PASS' and c['source_sha256']==sha(source)
C={(i,j):w for i,j,w in s['conjugates']};d=72
def tail(w):
    assert all(105<=i<=176 for i in w[::2])
    return sum((a%2)<<(i-105) for i,a in zip(w[::2],w[1::2]))
M={g:[tail(C[i,g]) for i in range(105,177)] for g in range(1,105)}
def action(v,mat):
    z=0
    while v:
        b=v&-v;v^=b;z^=mat[b.bit_length()-1]
    return z
def transpose(mat):
    return [sum(((mat[j]>>i)&1)<<j for j in range(d)) for i in range(d)]
def solve(rows,n):
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
N=list(range(87,105));normal_rows=[]
for i in N:
    mat=[(1<<k)^M[i][k]^action(M[i][k],M[i]) for k in range(d)]
    rhs=tail(s['powers'][i-1])
    normal_rows.extend((v<<((i-87)*d),(rhs>>k)&1) for k,v in enumerate(transpose(mat)))
for i in N:
    for j in N:
        if i<=j:continue
        w=C[i,j];assert w[:2]==[i,1]
        rhs=tail(w[2:])
        mi=transpose([M[j][k]^(1<<k) for k in range(d)])
        mj=transpose([M[i][k]^(1<<k) for k in range(d)])
        normal_rows.extend(((mi[k]<<((i-87)*d))^(mj[k]<<((j-87)*d)),(rhs>>k)&1) for k in range(d))
sol,rank,count=solve(normal_rows,len(N)*d)
a={i:(sol>>((i-87)*d))&((1<<d)-1) for i in N}
assert all(((v&sol).bit_count()&1)==rhs for v,rhs in normal_rows)
assert rank==len(N)*d-d
def section_N_tail(w):
    z=0
    for i,e in zip(w[::2],w[1::2]):
        assert i in N and 0<=e<3
        for _ in range(e):z=action(z,M[i])^a[i]
    return z
def action_N(w):
    mat=[1<<k for k in range(d)]
    for i,e in zip(w[::2],w[1::2]):
        assert i in N
        for _ in range(e):mat=[action(v,M[i]) for v in mat]
    return mat
normalizer=[]
for g in range(1,87):
    rows=[];checks=[]
    for i in N:
        w=C[i,g];assert all(k>=87 for k in w[::2])
        nw=[x for k,e in zip(w[::2],w[1::2]) if k<=104 for x in (k,e)]
        aw=[x for k,e in zip(w[::2],w[1::2]) if k>=105 for x in (k,e)]
        delta=tail(aw)^action(a[i],M[g])^section_N_tail(nw)
        mat=action_N(nw);lin=transpose([v^(1<<k) for k,v in enumerate(mat)])
        rows.extend((v,(delta>>k)&1) for k,v in enumerate(lin))
        checks.append((mat,delta))
    ag,rg,ct=solve(rows,d);assert rg==d
    assert all(action(ag,mat)^ag==delta for mat,delta in checks)
    a[g]=ag;normalizer.append(dict(generator=g,equations=ct,rank=rg))
# Verify the invariant-form ranks independently from their literal bit vectors.
pairs=list(itertools.combinations(range(d),2));form_ranks=[]
for hh in c['invariant_alternating_forms_hex']:
    B=int(hh,16);mat=[0]*d
    for q,(i,j) in enumerate(pairs):
        if B>>q&1:mat[i]|=1<<j;mat[j]|=1<<i
    _,rg,_=solve([(v,0) for v in mat],d);form_ranks.append(rg)
assert form_ranks==[72,36]
out=dict(status='PASS: explicit original-presentation section equations',
         source_sha256=sha(source),module_certificate_sha256=sha(cert),
         checker_sha256=sha(__file__),normal_three_generators=N,
         normal_three_lift_corrections_hex={str(i):hex(a[i]) for i in N},
         normal_three_equations=count,normal_three_equation_rank=rank,
         normal_three_free_dimension=len(N)*d-rank,
         quotient_generator_corrections_hex={str(i):hex(a[i]) for i in range(1,105)},
         normalizer_equations=normalizer,
         invariant_alternating_form_ranks=form_ranks,
         seconds=time.time()-start,
         scope='Exact section construction and form ranks only. The automorphism group for a central cover fixes its CHOSEN central C2 kernel; it need not fix the whole center. No target-bit value or full C31 lift is claimed.')
(CODE/'pbc_top_two_section.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','normal_three_equations','normal_three_equation_rank','normal_three_free_dimension','invariant_alternating_form_ranks','seconds','scope')},indent=2))
