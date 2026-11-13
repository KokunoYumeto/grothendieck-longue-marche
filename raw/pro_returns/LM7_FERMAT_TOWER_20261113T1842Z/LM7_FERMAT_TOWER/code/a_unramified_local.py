#!/usr/bin/env python3
"""E.68: exact local unramified graded factors and comparison certificates.

All matrices below are those of the actual q=4 Frobenius on the cubic
Tate lattice.  An integral change of basis reduces them to small invariant
multidegree blocks.  The separate normalizer test uses the actual evaluated
rank-two arithmetic quotient of E.54, including its nonlinear terms.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import random
import sympy as s

HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument("--source-code",type=Path)
args = ap.parse_args()
source = (args.source_code or HERE)/"e_unramified_sections.py"
if not source.exists():
    source = HERE.parents[1]/"LM7_FERMAT_TOWER/code/e_unramified_sections.py"
assert source.exists(),source
spec = importlib.util.spec_from_file_location("e41_hall",source)
e41 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e41)

def val3(x):
    x=Q(x)
    if not x:return 10**9
    n,d=abs(x.numerator),x.denominator
    ans=0
    while n%3==0:n//=3;ans+=1
    while d%3==0:d//=3;ans-=1
    return ans

def sm(mat):
    return s.Matrix([[s.Rational(x.numerator,x.denominator) for x in row]
                     for row in mat])

smith_store=[]
smith_ids={}
def smith(matrix):
    n=matrix.rows
    assert matrix.cols==n
    key=tuple(tuple(int(x) for x in row) for row in matrix.tolist())
    if key in smith_ids:
        return smith_store[smith_ids[key]]
    if n==0:
        obj={"id":len(smith_store),"matrix":matrix,"vals":[],
             "L":s.zeros(0),"R":s.zeros(0),"Li":s.zeros(0),"Ri":s.zeros(0)}
    else:
        a=[[Q(x) for x in row] for row in matrix.tolist()]
        left=[[Q(i==j) for j in range(n)] for i in range(n)]
        right=[[Q(i==j) for j in range(n)] for i in range(n)]
        vals=[]
        for k in range(n):
            v,i,j=min((val3(a[i][j]),i,j)
                      for i in range(k,n) for j in range(k,n))
            assert 0<=v<10**9
            a[k],a[i]=a[i],a[k];left[k],left[i]=left[i],left[k]
            for mat in (a,right):
                for row in mat:row[k],row[j]=row[j],row[k]
            u=Q(3**v)/a[k][k]
            assert val3(u)==0
            a[k]=[u*x for x in a[k]]
            left[k]=[u*x for x in left[k]]
            for i in range(n):
                if i!=k and a[i][k]:
                    c=a[i][k]/3**v
                    assert val3(c)>=0
                    a[i]=[x-c*y for x,y in zip(a[i],a[k])]
                    left[i]=[x-c*y for x,y in zip(left[i],left[k])]
            for j in range(n):
                if j!=k and a[k][j]:
                    c=a[k][j]/3**v
                    assert val3(c)>=0
                    for mat in (a,right):
                        for i in range(n):mat[i][j]-=c*mat[i][k]
            vals.append(v)
        L,R=sm(left),sm(right)
        Li,Ri=L.inv(),R.inv()
        diag=s.diag(*[3**v for v in vals])
        assert L*matrix*R==diag and Li*diag*Ri==matrix
        for mat in (L,R,Li,Ri):
            assert val3(mat.det())==0 and all(val3(x)>=0 for x in mat)
        obj={"id":len(smith_store),"matrix":matrix,"vals":vals,
             "L":L,"R":R,"Li":Li,"Ri":Ri}
    smith_ids[key]=obj["id"];smith_store.append(obj)
    return obj

coords=[(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2)]
U=s.Matrix([[v,-u] for u,v in coords])
A=(-2*s.eye(2)).row_join(s.zeros(2,8)).col_join(
    (-2*U).row_join(4*s.eye(8)))
# Use the unit minor at A2,A0, retaining the actual marked B0 vector.
L8=s.zeros(8)
L8[0,2]=1
L8[1,0]=-1
others=[1,3,4,5,6,7]
for k,i in enumerate(others,2):
    L8[k,i]=1
    L8[k,:]=L8[k,:]-U[i,0]*L8[0,:]-U[i,1]*L8[1,:]
assert L8*U==s.eye(8).extract(range(8),[0,1])
assert abs(L8.det())==1
L10=s.diag(s.eye(2),L8)
perm=[0,2,1,3,4,5,6,7,8,9]
P=s.eye(10).extract(perm,range(10))*L10
Pi=P.inv()
F=P*A*Pi
E=s.Matrix([[-2,0],[-2,4]])
assert F==s.diag(E,E,4,4,4,4,4,4)
assert abs(P.det())==1 and all(x.q==1 for x in Pi)
assert P*s.eye(10)[:,5]==s.eye(10)[:,5]
assert Pi*s.eye(10)[:,5]==s.eye(10)[:,5]
print("Actual Frobenius: integral two rank-two blocks plus six Tate lines; marked vector retained.",flush=True)

base=e41.dense_to_columns(F.tolist())
hall=e41.Hall(4)
block_of_letter=[0,0,1,1,2,3,4,5,6,7]
def multidegree(i):
    out=[0]*8
    for j,n in enumerate(hall.letters[i]):
        out[block_of_letter[j]]+=n
    return tuple(out)
def kernel(kind,i,r):
    if kind=="marked":return hall.letters[i][5]>=3
    if kind=="metabelian" and r==4:
        a,b=hall.children[i]
        return hall.degree[a]==hall.degree[b]==2
    return False
def matrix_from(columns,indices):
    rowpos={v:i for i,v in enumerate(indices)}
    ans=s.zeros(len(indices))
    for j,col in enumerate(indices):
        for row,a in columns[col].items():
            assert row in rowpos
            ans[rowpos[row],j]=a
    return ans
def encoded(mat):
    return [[str(x) for x in row] for row in mat.tolist()]
def count_nonunit(vals):
    return {str(v):n for v,n in sorted(Counter(vals).items()) if v}
def exact_cokernel_sequence(DF,ki,qi):
    """Record actual lattice maps and the snake inverse, not just orders."""
    n=DF.rows
    assert sorted(ki+qi)==list(range(n))
    J=s.eye(n).extract(range(n),ki)
    proj=s.eye(n).extract(qi,range(n))
    section=s.eye(n).extract(range(n),qi)
    pk=s.eye(n).extract(ki,range(n))
    DK=DF.extract(ki,ki);DQ=DF.extract(qi,qi)
    assert proj*DF*J==s.zeros(len(qi),len(ki))
    assert DF*J==J*DK and proj*DF==DQ*proj
    sf,sk,sq=smith(DF),smith(DK),smith(DQ)
    inj=sf["L"]*J*sk["Li"]
    sur=sq["L"]*proj*sf["Li"]
    representative_lift=sf["L"]*section*sq["Li"]
    assert sur*inj==s.zeros(len(qi),len(ki))
    assert sur*representative_lift==s.eye(len(qi))
    # The lift is a function on chosen finite Smith residues, not asserted
    # to descend to a homomorphic splitting of the finite cokernel groups.
    for i,vi in enumerate(sf["vals"]):
        for j,vj in enumerate(sk["vals"]):
            assert val3(inj[i,j])+vj>=vi
    for i,vi in enumerate(sq["vals"]):
        for j,vj in enumerate(sf["vals"]):
            assert val3(sur[i,j])+vj>=vi
    if qi:
        H=pk*(s.eye(n)-DF*section*DQ.inv()*proj)
    else:
        H=pk
    assert H*J==s.eye(len(ki))
    assert H*DF==DK*pk
    assert sum(sf["vals"])==sum(sk["vals"])+sum(sq["vals"])
    return {
        "kernel_indices":ki,"quotient_indices":qi,
        "full_smith_id":sf["id"],"kernel_smith_id":sk["id"],
        "quotient_smith_id":sq["id"],
        "cokernel_inclusion":encoded(inj),
        "cokernel_projection":encoded(sur),
        "chosen_representative_lift":encoded(representative_lift),
        "kernel_inverse_on_liftable_vectors":encoded(H)},sf,sk,sq

layers={}
sequence_checks=0
for r in range(1,5):
    columns,basis=hall.action(base,r)
    groups=defaultdict(list)
    for j,i in enumerate(basis):
        groups[multidegree(i)].append(j)
    for j,col in enumerate(columns):
        assert all(multidegree(basis[i])==multidegree(basis[j])
                   for i in col)
    full_vals=[]
    totals={k:{"kernel":[],"quotient":[]} for k in ["metabelian","marked"]}
    records=[]
    for sig,inds in sorted(groups.items()):
        DF=matrix_from(columns,inds)-s.eye(len(inds))
        sf=smith(DF);full_vals+=sf["vals"]
        rec={"multidegree":list(sig),
             "Hall_indices":[basis[i] for i in inds],
             "full_smith_id":sf["id"],"sequences":{}}
        for kind in totals:
            ki=[j for j,i in enumerate(inds) if kernel(kind,basis[i],r)]
            qi=[j for j in range(len(inds)) if j not in ki]
            seq,sf,sk,sq=exact_cokernel_sequence(DF,ki,qi)
            rec["sequences"][kind]=seq
            totals[kind]["kernel"]+=sk["vals"]
            totals[kind]["quotient"]+=sq["vals"]
            sequence_checks+=1
        records.append(rec)
    assert len(full_vals)==e41.layer_data("full",r)["rank"]
    for kind in totals:
        assert len(totals[kind]["quotient"])==e41.layer_data(kind,r)["rank"]
    layers[r]={
        "rank":len(basis),"full_factors":count_nonunit(full_vals),
        "full_det_valuation":sum(full_vals),
        "maximum_block_size":max(map(len,groups.values())),
        "quotients":{kind:{
            "rank":len(v["quotient"]),
            "factors":count_nonunit(v["quotient"]),
            "det_valuation":sum(v["quotient"]),
            "kernel_rank":len(v["kernel"]),
            "fiber_factors":count_nonunit(v["kernel"]),
            "fiber_det_valuation":sum(v["kernel"])}
            for kind,v in totals.items()},
        "blocks":records}
    print("degree",r,"full",layers[r]["full_factors"],
          "met fiber",layers[r]["quotients"]["metabelian"]["fiber_factors"],
          "marked fiber",layers[r]["quotients"]["marked"]["fiber_factors"],
          "max block",layers[r]["maximum_block_size"],flush=True)
assert layers[4]["quotients"]["metabelian"]["kernel_rank"]==990
assert layers[4]["quotients"]["marked"]["kernel_rank"]==9
assert layers[4]["quotients"]["metabelian"]["fiber_det_valuation"]==1138

# Exact nonlinear normalization in the actual E.54 arithmetic quotient.
def mul(g,h):
    a,b,n,r,t=g;A,B,N,R,T=h
    return (a+A,b+B,n+N-A*b,
            r+R+b*A*(A+1)/2-A*n,
            t+T+A*b*(b+1)/2-B*n+A*b*B)
def inverse(g):
    a,b,n,r,t=g
    return (-a,-b,-n-a*b,-r-b*a*(a-1)/2-a*n,
            -t-a*b*(b-1)/2-b*n)
def frob(g):
    a,b,n,r,t=g
    return (4*a,4*b,4*b+16*n,40*n+64*r,
            24*n+64*t-8*b*(b-1)-Q(15,2)*b)
zero=(Q(0),)*5
def conjugate(g,z):
    return mul(mul(g,z),inverse(frob(g)))
def residue(x,m):
    x=Q(x)
    assert x.denominator%3
    return (x.numerator*pow(x.denominator,-1,m))%m
def normalize(z):
    aa,bb=residue(z[0],3),residue(z[1],3)
    g0=((z[0]-aa)/3,(z[1]-bb)/3,Q(0),Q(0),Q(0))
    z1=conjugate(g0,z)
    nn=residue(z1[2],3)
    g1=(Q(0),Q(0),(z1[2]-nn)/15,Q(0),Q(0))
    z2=conjugate(g1,z1)
    rr,tt=residue(z2[3],9),residue(z2[4],9)
    g2=(Q(0),Q(0),Q(0),(z2[3]-rr)/63,(z2[4]-tt)/63)
    total=mul(mul(g2,g1),g0)
    ans=conjugate(g2,z2)
    assert ans==tuple(map(Q,(aa,bb,nn,rr,tt)))
    assert conjugate(total,z)==ans
    assert all(val3(x)>=0 for x in total)
    return ans,total
rng=random.Random(680041)
normalizer_checks=0
nonlinear_occurrences=0
for _ in range(500):
    canonical=tuple(map(Q,[rng.randrange(3) for _ in range(3)]+
                         [rng.randrange(9) for _ in range(2)]))
    h=tuple(Q(rng.randint(-30,30),rng.choice([1,2,5,7])) for _ in range(5))
    z=mul(mul(inverse(h),canonical),frob(h))
    result,g=normalize(z)
    assert result==canonical and g==h
    graded_only=tuple(x*y for x,y in zip(h,(4,4,16,64,64)))
    nonlinear_occurrences+=frob(h)!=graded_only
    normalizer_checks+=1
assert nonlinear_occurrences>0
print("Actual nonlinear E54 normalizers recovered:",normalizer_checks,flush=True)

# For the actual projection to class two choose target degree-one lifts
# x^(a+3)y^(b+3).  This deliberately exposes the triangular correction.
eps={}
for a,b in product(range(3),repeat=2):
    lower=(Q(a),Q(b),Q(0),Q(0),Q(0))
    g=(Q(-1),Q(-1),Q(0),Q(0),Q(0))
    shifted=conjugate(g,lower)
    assert shifted[:2]==(a+3,b+3)
    eps[a,b]=residue(shifted[2],3)
fiber_counts=Counter()
for a,b,n,r,t in product(range(3),range(3),range(3),range(9),range(9)):
    source_rep=tuple(map(Q,(a,b,n,r,t)))
    shifted=conjugate((Q(-1),Q(-1),Q(0),Q(0),Q(0)),source_rep)
    target=(a,b,residue(shifted[2],3))
    assert target[2]==(n+eps[a,b])%3
    fiber_counts[target]+=1
assert len(fiber_counts)==27 and set(fiber_counts.values())=={81}
print("Actual triangular quotient map: all2187 source classes,27 fibers of81.",flush=True)

def serial_smith(o):
    return {"id":o["id"],"matrix":o["matrix"].tolist(),"valuations":o["vals"],
            "left":encoded(o["L"]),"right":encoded(o["R"]),
            "left_inverse":encoded(o["Li"]),"right_inverse":encoded(o["Ri"])}
out={
    "statement":"E.68","status":"PASS",
    "source_dependency":"e_unramified_sections.py",
    "source_dependency_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
    "actual_original_Frobenius":A.tolist(),
    "integral_basis_map":P.tolist(),"integral_basis_inverse":Pi.tolist(),
    "actual_block_Frobenius":F.tolist(),
    "marked_vector_index":5,
    "layers":layers,"smith_blocks":[serial_smith(o) for o in smith_store],
    "exact_sequence_certificates":sequence_checks,
    "actual_E54_normalizer_checks":normalizer_checks,
    "nonlinear_Frobenius_occurrences":nonlinear_occurrences,
    "actual_E54_target_Hall_lifts":"x^(a+3)y^(b+3), with a,b in{0,1,2}",
    "actual_E54_triangular_correction":[
        {"a":a,"b":b,"epsilon":eps[a,b]} for a,b in sorted(eps)],
    "actual_E54_source_classes":2187,
    "actual_E54_target_classes":27,
    "actual_E54_fiber_size":81,
    "scope":(
        "All first-four-degree factors and exact graded comparison maps at q4. "
        "The actual nonlinear normalization is independently checked in E54's "
        "evaluated arithmetic quotient. The inverse-limit normal forms, "
        "all-degree strict kernels and full comparison fibers are proved in E68.")}
(HERE/"a_unramified_local.json").write_text(
    json.dumps(out,indent=2,default=int)+"\n")
print("PASS: exact local factors, strict kernel maps, snake inverses and nonlinear normalizers.",flush=True)
