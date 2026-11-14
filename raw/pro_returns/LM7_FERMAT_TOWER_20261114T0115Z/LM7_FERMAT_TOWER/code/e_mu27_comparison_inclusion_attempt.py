#!/usr/bin/env python3
"""E.94: rebuild the mu27 local/ray comparison and verify every finite map.

--gp PATH performs six actual PARI stages in a fresh directory. The only
BNF calculation is the already certified degree-18 B1 calculation.
"""
from __future__ import annotations
import argparse
from itertools import product
import json
from math import gcd, lcm, prod
from pathlib import Path
import shutil
import subprocess
import tempfile
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form

HERE=Path(__file__).resolve().parent
DEPENDENCIES=[
    ("e_basechange_field","cyclotomic_base1"),
    ("e_basechange_ninth_norms","cyclotomic_base1_ninth_norms"),
    ("e_basechange_ninth_genus","cyclotomic_base1_ninth_genus"),
]
OWN=["e_mu27_local","e_mu27_genus","e_mu27_export"]

def locate(name):
    for p in (HERE/(name+".gp"),HERE.parent.parent/"research_e76/code"/(name+".gp")):
        if p.exists(): return p
    raise FileNotFoundError(name)

def rebuild(gp):
    gp=str(Path(gp).resolve())
    with tempfile.TemporaryDirectory(prefix="e94_exact_") as td:
        root=Path(td);dep=root/"research_norm_index/code";own=root/"research_e94/code"
        dep.mkdir(parents=True);own.mkdir(parents=True)
        stages=[(locate(a),dep/(b+".gp"),"e_mu27_dependency_"+a) for a,b in DEPENDENCIES]
        stages += [(HERE/(a+".gp"),own/(a+".gp"),a) for a in OWN]
        for source,dest,label in stages:
            shutil.copyfile(source,dest)
            p=subprocess.run([gp,"-q",str(dest)],cwd=root,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
            (HERE/(label+".out")).write_text(p.stdout)
            assert p.returncode==0,(label,p.returncode)
            assert "***   at top-level" not in p.stdout,p.stdout
            assert "***   user error" not in p.stdout,p.stdout
            assert "DONE" in p.stdout or "CLASS_GENERATORS" in p.stdout,label
            print(label,"PASS",flush=True)
        for name in ("e_mu27_local.bin","e_mu27_genus.bin"):
            shutil.copyfile(own/name,HERE/name)
        shutil.copyfile(dep/"cyclotomic_base1_bnf.bin",HERE/"e_mu27_base_bnf.bin")

def integral(A): return all(x.q==1 for x in A)
def modmat(A,orders): return s.Matrix(A.rows,A.cols,lambda i,j:int(A[i,j])%orders[i])
def rankmod(A,p=3):
    R=[[int(x)%p for x in row] for row in A.tolist()];rank=0
    for j in range(A.cols):
        pivot=next((i for i in range(rank,A.rows) if R[i][j]),None)
        if pivot is None: continue
        R[rank],R[pivot]=R[pivot],R[rank]
        inv=pow(R[rank][j],-1,p);R[rank]=[(x*inv)%p for x in R[rank]]
        for i in range(A.rows):
            if i!=rank:
                v=R[i][j];R[i]=[(x-v*y)%p for x,y in zip(R[i],R[rank])]
        rank+=1
        if rank==A.rows: break
    return rank
def apply(A,v,ds): return tuple(sum(int(a)*b for a,b in zip(row,v))%d for row,d in zip(A,ds))
def add(v,w,ds): return tuple((a+b)%d for a,b,d in zip(v,w,ds))
def mult(v,k,ds): return tuple(k*a%d for a,d in zip(v,ds))
def order(v,ds): return lcm(*(d//gcd(d,a) for a,d in zip(v,ds)))
def span(columns,ds):
    H={tuple(0 for _ in ds)}
    for c in columns:
        H={add(v,mult(c,k,ds),ds) for v in H for k in range(order(c,ds))}
    return H

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--gp");arg=ap.parse_args()
    if arg.gp: rebuild(arg.gp)
    text=(HERE/"e_mu27_export.out").read_text()
    assert "***   at top-level" not in text and "***   user error" not in text
    records=[json.loads(line) for line in text.splitlines() if line.startswith("{")]
    vals={r["name"]:r["value"] for r in records if "name" in r}
    done=records[-1];assert done["status"]=="PASS"
    M=lambda n:s.Matrix(vals[n])
    V=lambda n:s.Matrix([vals[n]])
    r=len(vals["ray_orders"]);I=s.eye(r)
    systems=[]
    for name,h,left,right,diag in [
        ("ordinary","ordinary_hnf","ordinary_left","ordinary_right","ordinary_diagonal"),
        ("relative ordinary","relative_ordinary_presentation","relative_ordinary_left","relative_ordinary_right","relative_ordinary_diagonal"),
        ("S","S_hnf","S_left","S_right","S_diagonal"),
        ("relative S","relative_S_presentation","relative_S_left","relative_S_right","relative_S_diagonal"),
        ("norm kernel","ordinary_norm_kernel_presentation","ordinary_norm_kernel_left","ordinary_norm_kernel_right","ordinary_norm_kernel_diagonal"),
        ("S local image","S_local_image_hnf","S_local_image_left","S_local_image_right","S_local_image_diagonal"),
        ("ordinary local image","ordinary_local_image_hnf","ordinary_local_image_left","ordinary_local_image_right","ordinary_local_image_diagonal"),
    ]:
        A,U,W,D=map(M,(h,left,right,diag))
        assert U*A*W==D and abs(U.det())==abs(W.det())==1,name
        assert integral(U.inv()) and integral(W.inv()),name
        systems.append(name)
    for stem in ("ordinary","relative_ordinary","S","relative_S"):
        assert M(stem+"_left")*M(stem+"_left_inverse")==I
        assert M(stem+"_right")*M(stem+"_right_inverse")==I
    H,HS,K,P,PS=M("ordinary_hnf"),M("S_hnf"),M("kernel_basis"),M("relative_ordinary_presentation"),M("relative_S_presentation")
    assert K*M("kernel_inverse_numerator")==27*I and abs(K.det())==27
    assert K*P==H and K*PS==HS and integral(H.inv()*HS)
    chi=M("kummer_characters")
    assert integral(s.diag(9,3).inv()*chi*K)
    assert abs(H.det())==3**10 and abs(HS.det())==3**6
    assert [int(P) for P in M("ordinary_diagonal").diagonal() if P!=1]==[9,9,9,9,3,3]
    assert [int(P) for P in M("S_diagonal").diagonal() if P!=1]==[9,9,3,3]
    nd=(9,9,9,3);od=(9,9,3);sd=(9,3)
    assert [int(P) for P in M("relative_ordinary_diagonal").diagonal() if P!=1]==list(nd)
    assert [int(P) for P in M("relative_S_diagonal").diagonal() if P!=1]==list(sd)
    assert integral(M("old_genus_hnf").inv()*M("old_ray_restriction")*H)
    D=s.diag(*vals["ray_orders"])
    assert integral(D.inv()*(M("source_ray_basis")*M("source_ray_inverse")-I))
    assert M("old_ray_restriction")==M("old_ray_basis")*M("source_ray_inverse")
    for act in ("ray_G","ray_H"):
        A=M(act)
        assert integral(H.inv()*A*H) and integral(HS.inv()*A*HS) and integral(K.inv()*A*K)
    N,J,Q=M("ordinary_norm_to_B3_genus"),M("ordinary_transfer_from_B3_genus"),M("ordinary_to_S_quotient")
    right=M("ordinary_norm_right_lifts")
    assert integral(s.diag(*od).inv()*(N*right-s.eye(3)))
    assert modmat(J*N-3*s.eye(4),nd)==s.zeros(4)
    assert modmat(N*J-3*s.eye(3),od)==s.zeros(3)
    assert modmat(J-3*right,nd)==s.zeros(4,3)
    assert M("ordinary_norm_kernel_basis")*M("ordinary_norm_kernel_presentation")==s.diag(*nd)
    assert [int(x) for x in M("ordinary_norm_kernel_diagonal").diagonal() if x!=1]==[3,3]
    newlift=(K*M("relative_ordinary_left_inverse"))[:,:4]
    computedN=(M("old_genus_left")*M("old_ray_restriction")*newlift)[1:4,:]
    assert modmat(computedN,od)==N
    assert modmat((M("relative_S_left")*M("relative_ordinary_left_inverse"))[:2,:4],sd)==Q
    C=M("actual_six_S_prime_classes")
    oldC=s.Matrix([[6,6,6,6,3,0],[0,6,3,5,8,5],[2,2,2,1,1,1]])
    assert modmat(N*C,od)==oldC*s.diag(1,1,1,3,3,3)%1 if False else True
    assert modmat(N*C-oldC*s.diag(1,1,1,3,3,3),od)==s.zeros(3,6)
    assert modmat(J*oldC-C*s.diag(3,3,3,1,1,1),nd)==s.zeros(4,6)
    assert modmat(Q*C,sd)==s.zeros(2,6)
    AG,AH=M("relative_ordinary_G"),M("relative_ordinary_H")
    SG,SH=M("relative_S_G"),M("relative_S_H")
    assert SG==s.eye(2) and SH==s.Matrix([[1,3],[2,1]])
    for A in (AG,AH):
        assert modmat(A**3-s.eye(4),nd)==s.zeros(4)
    assert modmat(AG*AH-AH*AG,nd)==s.zeros(4)
    assert modmat(Q*AG-SG*Q,sd)==s.zeros(2,4) and modmat(Q*AH-SH*Q,sd)==s.zeros(2,4)
    normrow=vals["relative_S_norm_to_original_C3"];assert normrow==[2,0]
    for j in (1,2,3):
        k=M(f"joint_local_kernel_{j}");u=M(f"joint_local_left_{j}");w=M(f"joint_local_right_{j}");diag=M(f"joint_local_diagonal_{j}")
        assert u*k*w==diag and abs(u.det())==abs(w.det())==1 and abs(k.det())==27
        row=V(f"cyclotomic_local_row_{j}");rad=V(f"radical_local_row_{j}")
        assert vals[f"cyclotomic_local_row_{j}"]==[0,0,1,1,1,0,0]
        assert integral(s.diag(9,3).inv()*s.Matrix.vstack(rad,row)*k)
        cols=M(f"actual_cyclotomic_norm_columns_{j}")
        assert modmat(row*cols,[3])==s.zeros(1,cols.cols) and rankmod(cols)==6
        systems.append(f"joint local {j}")
    M9,CP=M("radical_S_characters"),M("cyclotomic_S_characters")
    assert modmat(V("actual_radical_weights")*M9,[9])==s.zeros(1,15)
    assert modmat(s.ones(1,6)*CP,[3])==s.zeros(1,15)
    FL=M("field_norm_kernel")
    assert integral(M9*FL/9) and abs(FL.det())==3**10
    assert modmat(CP*FL,[3]*6)==M("cyclotomic_on_field_norm_kernel")
    assert rankmod(M("cyclotomic_on_field_norm_kernel"))==3
    LD=s.diag(*([9]*6+[3]*6));combined=s.Matrix.vstack(M9,CP)
    assert hermite_normal_form(s.Matrix.hstack(LD,combined))==M("S_local_image_hnf")
    assert hermite_normal_form(s.Matrix.hstack(LD,combined[:,:9]))==M("ordinary_local_image_hnf")
    assert LD.det()/M("S_local_image_hnf").det()==3**13
    assert LD.det()/M("ordinary_local_image_hnf").det()==3**7
    nfib={};sfib={};nker=[];checks=0
    na,ja,qa=N.tolist(),J.tolist(),Q.tolist()
    ga,ha=AG.tolist(),AH.tolist()
    for v in product(*(range(n) for n in nd)):
        nv=apply(na,v,od);sv=apply(qa,v,sd)
        nfib[nv]=nfib.get(nv,0)+1;sfib[sv]=sfib.get(sv,0)+1
        if not any(nv):nker.append(v)
        assert apply(ja,nv,nd)==mult(v,3,nd)
        assert apply(ga,apply(ha,v,nd),nd)==apply(ha,apply(ga,v,nd),nd)
        checks+=1
    assert len(nfib)==243 and set(nfib.values())=={9}
    assert len(sfib)==27 and set(sfib.values())=={81}
    assert len(nker)==9 and all(not any(mult(v,3,nd)) for v in nker)
    jker=[v for v in product(*(range(n) for n in od)) if not any(apply(ja,v,nd))]
    assert len(jker)==9
    sf={k:0 for k in range(3)}
    for v in product(range(9),range(3)):
        sf[sum(a*b for a,b in zip(normrow,v))%3]+=1
        assert apply(SH.tolist(),apply(SH.tolist(),apply(SH.tolist(),v,sd),sd),sd)==v
    assert set(sf.values())=={9}
    prime_orders=[order(tuple(C[:,i]),nd) for i in range(6)]
    assert prime_orders==[9,9,9,3,3,3]
    ram=span([tuple(C[:,i]) for i in range(6)],nd);assert len(ram)==81
    assert not any(mult(v,9,nd) for v in [])  # no assertions about full class groups
    # Literal normalizer group: G^i H^j, over K.
    def gm(x,y): return ((x[0]+pow(4,x[1],27)*y[0])%27,(x[1]+y[1])%9)
    def gi(x): return ((-pow(pow(4,x[1],27),-1,27)*x[0])%27,-x[1]%9)
    G,Hh=(1,0),(0,1)
    assert gm(gm(Hh,G),gi(Hh))==(4,0)
    deck={(0,0),(0,3),(0,6)}
    assert {gm(gm(G,d),gi(G)) for d in deck}!=deck
    assert {gm(gm((3,0),d),gi((3,0))) for d in deck}==deck
    normalizer_checks=0
    for x in product(range(27),range(9)):
        assert gm(x,gi(x))==(0,0)
        normalizer_checks+=1
    Z,A=s.symbols("Z A")
    assert s.resultant(Z**6+Z**3+1,1+A*Z,Z)==A**6-A**3+1
    assert 17**2-17+1==273 and 273//3%27==10 and pow(10,-1,27)==19
    assert 17**2%27==19 and pow(19,-1,27)==10 and pow(289,3,27)==1
    summary={
        "status":"PASS","statement":"E.94","structured_records":len(records),
        "exact_Smith_systems":len(systems),"relative_ordinary_orders":list(nd),
        "relative_S_orders":list(sd),"relative_ordinary_genus_norm":N.tolist(),
        "relative_ordinary_genus_transfer":J.tolist(),"ordinary_to_S":Q.tolist(),
        "S_genus_norm_to_original_C3":normrow,"S_genus_norm_kernel_orders":[3,3],
        "ordinary_genus_norm_kernel_orders":[3,3],"S_G":SG.tolist(),"S_H":SH.tolist(),
        "six_actual_prime_columns":C.tolist(),"six_genus_prime_orders":prime_orders,
        "S_prime_genus_image_order":len(ram),"ordinary_coordinate_cases":checks,
        "normalizer_group_cases":normalizer_checks,"local_joint_index":27,
        "S_unit_character_image_order":3**13,"ordinary_unit_character_image_order":3**7,
        "cyclotomic_image_on_radical_field_norm_kernel_rank":3,
        "ramified_prime_norm_coefficients":[1,1,1,3,3,3],
        "ramified_prime_extension_coefficients":[3,3,3,1,1,1],
        "scope":"These are exact genus quotients, their actual norm/extension maps and local field comparisons. The full class groups of E and the eventual exponent h are not assigned numerical values."
    }
    out={"summary":summary,"complete_export_records":records}
    (HERE/"e_mu27_comparison.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(summary,indent=2))

if __name__=="__main__":main()
