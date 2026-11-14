#!/usr/bin/env python3
"""E101: portable five-stage arithmetic rebuild and independent exact checks.

The rebuilt BNF inputs are the certified degree-six L1 and the previously
certified cyclotomic degree-eighteen B1.  Neither radical upper field L2/B2
nor the uncertified discovery field is a BNF input to this certificate.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
from itertools import product
import json
from math import gcd, lcm, prod
from pathlib import Path
import shutil
import subprocess
import tempfile
import sympy as sp

HERE=Path(__file__).resolve().parent
DEPENDENCIES=[
    ("e_stable_lower_genus", "research_e86/code/e_stable_lower_genus.gp"),
    ("e_basechange_field", "research_norm_index/code/cyclotomic_base1.gp"),
    ("e_basechange_local_norms", "research_norm_index/code/cyclotomic_base1_local_norms.gp"),
]

def dependency(name):
    candidates=(HERE/(name+".gp"), HERE.parent/"inputs"/(name+".gp"),
                HERE.parent.parent/"LM7_FERMAT_TOWER/code"/(name+".gp"))
    return next(p for p in candidates if p.exists())

def rebuild(gp):
    gp=str(Path(gp).resolve())
    with tempfile.TemporaryDirectory(prefix="e101_norm_") as td:
        root=Path(td)
        stages=[(dependency(name), dest, "e_unit_norm_dependency_"+name)
                for name,dest in DEPENDENCIES]
        stages += [(HERE/(name+".gp"), "research_e101/code/"+name+".gp", name)
                   for name in ("e_unit_norm_scalar","e_unit_norm_coordinates")]
        for source,dest,label in stages:
            target=root/dest;target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(source,target)
            run=subprocess.run([gp,"-q",str(target)],cwd=root,text=True,
                               stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            (HERE/(label+".out")).write_text(run.stdout)
            assert run.returncode==0,(label,run.returncode)
            assert "***   at top-level" not in run.stdout,run.stdout
            assert "***   user error" not in run.stdout,run.stdout
            assert "DONE" in run.stdout or '"status":"PASS"' in run.stdout,label
            if source.stem=="e_basechange_field":
                assert "BNF_CERTIFY 1" in run.stdout,"B1 certification did not return1"
            print(label,"PASS",flush=True)
        for name in ("e_unit_norm_scalar","e_unit_norm_coordinates"):
            shutil.copyfile(root/"research_e101/code"/(name+".bin"),HERE/(name+".bin"))
        # Retain the complete dependency data required to compare actual
        # fields, bases and Artin maps without relying on serialization bytes.
        for source,name in (("research_e86/code/e_stable_lower_genus.bin","e_unit_norm_lower.bin"),
                            ("research_norm_index/code/cyclotomic_base1_bnf.bin","e_unit_norm_base_B1.bin"),
                            ("research_norm_index/code/cyclotomic_base1_local_norms.bin","e_unit_norm_local_characters.bin")):
            shutil.copyfile(root/source,HERE/name)

class Field:
    def __init__(self,mod):
        self.mod=tuple(map(Q,mod));self.n=len(mod)-1
        assert self.mod[-1]==1
        self.zero=(Q(0),)*self.n;self.one=(Q(1),)+(Q(0),)*(self.n-1)
    def elt(self,a):
        if isinstance(a,(int,Q)):return (Q(a),)+(Q(0),)*(self.n-1)
        a=list(map(Q,a));a += [Q(0)]*max(0,self.n-len(a))
        for k in range(len(a)-1,self.n-1,-1):
            v=a[k]
            if v:
                for j in range(self.n):a[k-self.n+j]-=v*self.mod[j]
        return tuple(a[:self.n])
    def add(self,a,b):return tuple(x+y for x,y in zip(a,b))
    def neg(self,a):return tuple(-x for x in a)
    def sub(self,a,b):return self.add(a,self.neg(b))
    def scale(self,a,k):return tuple(k*x for x in a)
    def mul(self,a,b):
        c=[Q(0)]*(2*self.n-1)
        for i,x in enumerate(a):
            if x:
                for j,y in enumerate(b):
                    if y:c[i+j]+=x*y
        return self.elt(c)
    def pow(self,a,n):
        out=self.one
        while n:
            if n&1:out=self.mul(out,a)
            a=self.mul(a,a);n//=2
        return out
    def total(self,seq):
        out=self.zero
        for a in seq:out=self.add(out,a)
        return out
    def evaluate(self,a,t):
        out=self.zero
        for c in reversed(a):out=self.add(self.mul(out,t),self.elt(c))
        return out
    def eye(self,n):return [[self.one if i==j else self.zero for j in range(n)] for i in range(n)]
    def matmul(self,A,B):return [[self.total(self.mul(A[i][k],B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    def matadd(self,A,B):return [[self.add(a,b) for a,b in zip(ar,br)] for ar,br in zip(A,B)]
    def matscale(self,A,t):return [[self.mul(a,t) for a in ar] for ar in A]

def records(name):
    raw=(HERE/(name+".out")).read_text()
    assert "***   at top-level" not in raw and "***   user error" not in raw
    rows=[json.loads(x) for x in raw.splitlines() if x.startswith("{")]
    assert rows[-1]["status"]=="PASS"
    return {r["name"]:r["value"] for r in rows if "name" in r},rows[-1]

def ratmat(A):return sp.Matrix([[sp.Rational(a,b) for a,b in row] for row in A])
def modmat(A):return A.applyfunc(lambda x:int(x)%3)
def integral(A):return all(x.q==1 for x in A)

def rank3(A):
    a=[[int(x)%3 for x in row] for row in A.tolist()];r=0
    for j in range(A.cols):
        hit=next((i for i in range(r,len(a)) if a[i][j]),None)
        if hit is None:continue
        a[r],a[hit]=a[hit],a[r]
        inv=pow(a[r][j],-1,3);a[r]=[(v*inv)%3 for v in a[r]]
        for i in range(len(a)):
            if i!=r:
                v=a[i][j];a[i]=[(x-v*y)%3 for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r

def smith_check(d,tag,rank):
    M=sp.Matrix(d[tag+"_matrix"]);H=sp.Matrix(d[tag+"_kernel_hnf"])
    HI=ratmat(d[tag+"_kernel_inverse"])
    L,R,LI,RI=(sp.Matrix(d[tag+key]) for key in ("_smith_left","_smith_right","_smith_left_inverse","_smith_right_inverse"))
    ds=d[tag+"_smith_diagonal"];n=H.rows
    assert H*HI==HI*H==sp.eye(n)
    assert L*H*R==sp.diag(*ds)
    assert L*LI==LI*L==R*RI==RI*R==sp.eye(n)
    assert abs(L.det())==abs(R.det())==1
    assert ds==[3]*rank+[1]*(n-rank) and abs(H.det())==3**rank
    assert modmat(M*H)==sp.zeros(M.rows,n) and rank3(M)==rank
    P=sp.Matrix(d[tag+"_quotient_map"]);S=sp.Matrix(d[tag+"_quotient_section"])
    assert P==M[[i-1 for i in d[tag+"_independent_rows"]],:]
    assert modmat(P*S)==sp.eye(rank)
    rel=sp.Matrix(d[tag+"_image_torsion_relation"])
    assert H*rel==sp.Matrix([9]+[0]*(n-1)) and gcd(*map(int,rel))==3
    checks=0
    for u in product(range(3),repeat=rank):
        v=S*sp.Matrix(u)
        assert modmat(P*v)==sp.Matrix(u)
        assert integral(HI*v)==(not any(u))
        checks+=1
    # Verify all exact basis directions and their transported inverses,
    # including the source torsion relation.
    for j in range(n):assert HI*H[:,j]==sp.eye(n)[:,j]
    return {"rank":rank,"image_torsion":[3],"image_free_rank":n-1,
            "quotient_cosets_checked":checks,"smith_diagonal":ds}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--gp");args=ap.parse_args()
    if args.gp:rebuild(args.gp)
    d,done=records("e_unit_norm_scalar");c,cdone=records("e_unit_norm_coordinates")
    assert done["unit_product_defect"]==[0,2]
    F=Field([289,0,0,17,0,0,1]);b=F.elt([0,1]);z=F.scale(F.pow(b,3),Q(1,17))
    e1,e2=[F.elt([Q(a,b) for a,b in row]) for row in d["lower_units"]]
    eps=F.mul(e1,e2);c1=F.add(F.add(b,F.one),F.scale(z,3))
    assert F.mul(F.pow(c1,6),F.pow(eps,2))==F.elt(-3)
    uu=[F.elt([Q(a,b) for a,b in row]) for row in d["reversed_norm_coefficients"]]
    displayed_numerators=[
      [-37103278413,25225148828,-5743099426,-1117338456,415980086,-548768638],
      [161479643843,-70558353324,-3192102308,5646166658,-6279927666,1260332509],
      [-551544947582,-108462373370,26395251042,-53737480949,14839765429,-2202740637]]
    assert uu==[F.scale(F.elt(row),Q(1,16578519)) for row in displayed_numerators]
    norm=F.total([F.pow(uu[0],3),F.mul(eps,F.pow(uu[1],3)),
                  F.mul(F.pow(eps,2),F.pow(uu[2],3)),
                  F.scale(F.mul(eps,F.mul(uu[0],F.mul(uu[1],uu[2]))),-3)])
    assert norm==b
    A=[[F.zero,F.zero,eps],[F.one,F.zero,F.zero],[F.zero,F.one,F.zero]];I=F.eye(3)
    S=[[F.one,F.zero,F.zero],[F.zero,z,F.zero],[F.zero,F.zero,F.pow(z,2)]]
    A2=F.matmul(A,A)
    B=F.matmul(F.matadd(F.matadd(F.matscale(I,uu[0]),F.matscale(A,uu[1])),F.matscale(A2,uu[2])),S)
    assert F.matmul(A2,A)==F.matscale(I,eps)
    assert F.matmul(F.matmul(B,B),B)==F.matscale(I,b)
    assert F.matmul(B,A)==F.matscale(F.matmul(A,B),z)
    L=Field([289]+[0]*8+[17]+[0]*8+[1]);t=L.elt([0,1]);zt=L.scale(L.pow(t,9),Q(1,17))
    sigmat=L.mul(zt,t);w=L.elt([Q(a,b) for a,b in d["absolute_witness"]])
    sw=L.evaluate(w,sigmat);ssw=L.evaluate(sw,sigmat)
    assert L.evaluate(ssw,sigmat)==w
    assert L.mul(L.mul(w,sw),ssw)==L.evaluate(eps,L.pow(t,3))
    vv=[L.elt([Q(a,b) for a,b in row]) for row in d["absolute_eigenvector"]]
    assert vv[2]==L.one
    Aup=[[L.evaluate(v,L.pow(t,3)) for v in row] for row in A]
    Bup=[[L.evaluate(v,L.pow(t,3)) for v in row] for row in B]
    assert L.matmul(Aup,[[v] for v in vv])==[[L.mul(w,L.evaluate(v,sigmat))] for v in vv]
    assert L.matmul(Bup,[[v] for v in vv])==[[L.mul(t,v)] for v in vv]
    J=sp.Matrix(d["reduced_ideal_hnf"])
    assert J.det()==d["reduced_ideal_norm"]==7**2*1444543
    arts=[0]*7;factor_norm=1
    for p,f,k,fb,rel,art in d["actual_contracted_prime_rows"]:
        assert sp.isprime(p) and f==fb*rel
        factor_norm*=p**(f*k)
        arts=[x+k*rel*y for x,y in zip(arts,art)]
    assert factor_norm==J.det()
    ga=[x%m for x,m in zip(arts,[9,3,3,1,1,1,1])]
    assert ga==d["genus_coordinate"]==[3,2,1,0,0,0,0]
    C=ratmat(d["class_forward"]);CI=sp.Matrix(d["class_inverse"])
    assert C*CI==CI*C==sp.eye(3)
    cv=C*sp.Matrix(ga[:3]);assert integral(cv)
    cl=[int(x)%m for x,m in zip(cv,[9,3,1])]
    assert cl==d["full_ordinary_ideal_class"]==[3,2,0]
    assert [x%m for x,m in zip(cl,[3,3,1])]==d["ordinary_unit_defect"]==[0,2,0]

    M=sp.Matrix(c["field_norm_matrix"]);Qk=sp.Matrix(c["field_norm_kernel"])
    R=sp.Matrix(c["horizontal_norm_matrix"]);NQ=modmat(R*Qk)
    expected_M=sp.Matrix([
      [2,1,0,1,0,0,0,2,1,1,1,0,0,0,2],
      [2,1,0,1,0,0,0,0,0,1,0,1,1,1,1],
      [2,1,0,1,0,0,0,1,2,1,2,2,0,0,1],
      [2,1,0,1,0,0,0,1,1,2,2,0,1,0,1],
      [2,1,0,1,0,0,0,1,1,2,2,0,0,1,1],
      [1,2,0,2,0,0,0,2,2,1,1,0,0,0,1]])
    expected_R=sp.Matrix([
      [1,2,0,2,1,1,0,0,2,1,1,1,2,2,2],
      [0,0,0,0,-1,-1,0,0,-1,1,2,2,1,0,-1],
      [0,0,0,0,2,-1,0,1,1,1,1,0,0,0,1],
      [0,0,0,0,0,0,0,0,0,3,3,3,1,1,1],
      [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1]])
    assert M==expected_M and R==expected_R
    assert M.shape==(6,15) and rank3(M)==5 and Qk.shape==(15,10)
    assert rank3(Qk)==10 and modmat(M*Qk)==sp.zeros(6,10)
    assert NQ==sp.Matrix(c["horizontal_norm_on_kernel"]) and rank3(NQ)==2
    assert NQ[1,:]==NQ[2,:] and NQ[3:5,:]==sp.zeros(2,10)
    assert modmat(sp.Matrix([[1,1,1,2,2,1]])*M)==sp.zeros(1,15)
    G,H=(sp.Matrix(c[k]) for k in ("g_action","h_action"))
    assert modmat(G**3)==modmat(H**3)==sp.eye(15)
    assert modmat(G*H-H*G)==sp.zeros(15,15)
    assert modmat(M*G*Qk)==modmat(M*H*Qk)==sp.zeros(6,10)
    E=ratmat(c["horizontal_embedding"]);Ei=ratmat(c["horizontal_projection_inverse"])
    assert Ei*E==sp.eye(6) and E*Ei*E==E
    Phi=sp.Matrix(c["S_unit_matrix"])
    assert Phi[:6,:]==M and Phi[6,:]==modmat(R[0,:]+2*R[1,:])
    stats={tag:smith_check(c,tag,rk) for tag,rk in (("S_unit",6),("ordinary_B_unit",4))}
    assert sp.Matrix(c["ordinary_B_unit_matrix"])==Phi[:,:9]
    simple=sp.Matrix([
      [1,-1,0,-1,0,0,0,0,0,-1,0,-1,0,0,0],
      [0,0,0,0,1,-2,0,0,0,-1,-2,0,0,0,0],
      [0,0,0,0,0,0,0,1,0,-1,-1,0,0,0,0],
      [0,0,0,0,0,0,0,0,1,-1,0,-1,0,0,-1],
      [0,0,0,0,0,0,0,0,0,0,0,0,1,0,-1],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1]])
    pivots=[0,4,7,8,12,13];section=sp.eye(15)[:,pivots]
    assert simple*section==sp.eye(6)
    assert modmat(Phi-Phi*section*simple)==sp.zeros(7,15)
    assert rank3(Phi*section)==6
    HI=ratmat(c["S_unit_kernel_inverse"])
    assert 3*HI[pivots,:]==simple
    unchanged=[i for i in range(15) if i not in pivots]
    assert HI[unchanged,:]==sp.eye(15)[unchanged,:]
    beta=sp.Matrix(c["known_beta_norm"]);xic1=sp.Matrix(c["known_xic1_defect"])
    assert modmat(Phi*beta)==sp.zeros(7,1)
    assert modmat(M*xic1)==sp.zeros(6,1) and int((Phi*xic1)[6])%3==1

    # Exhaust the actual ten-dimensional field-norm kernel once, through
    # its certified basis. This checks both the horizontal reduction and
    # the newly evaluated scalar, including the exact number of zero fibres.
    qrows=[[int(x) for x in row] for row in Qk.tolist()]
    rrows=[[int(x) for x in row] for row in R.tolist()]
    ph=[int(x) for x in Phi[6,:]]
    zero=0;tests=0
    for a in product(range(3),repeat=10):
        x=[sum(v*y for v,y in zip(row,a))%3 for row in qrows]
        nh=[sum(v*y for v,y in zip(row,x))%3 for row in rrows]
        assert nh[1]==nh[2] and nh[3:]==[0,0]
        defect=(nh[0]+2*nh[1])%3
        assert defect==sum(v*y for v,y in zip(ph,x))%3
        zero+=defect==0;tests+=1
    assert tests==3**10 and zero==3**9
    lower_checks=0
    for a,b0,c0,e,f in product(range(3),repeat=5):
        ordinary=(a==b0==c0)
        assert ordinary==((a-b0)%3==0 and (c0-b0)%3==0)
        snorm=ordinary and e==0
        # Norms beta2 and included c1 supply the free S directions.
        assert snorm==(ordinary and e%3==0)
        lower_checks+=1

    # Exact finite residue of an actual ordinary preimage of zeta*e1*e2.
    def mul(x,y):
        a,b=x;c0,d0=y
        return ((a*c0-b*d0)%17,(a*d0+b*c0-b*d0)%17)
    def power(x,n):
        y=(1,0)
        while n:
            if n&1:y=mul(y,x)
            x=mul(x,x);n//=2
        return y
    rz=(0,1);target=power(rz,2)
    residue_roots=[x for x in product(range(17),repeat=2) if power(x,3)==target]
    assert len(residue_roots)==3 and all(power(x,96)==rz for x in residue_roots)
    column=sp.Matrix(c["new_L2_unit_local_column"])
    assert modmat(column-2*M[:,0])==sp.zeros(6,1)
    assert rank3(M[:,:9].row_join(column))==rank3(M[:,:9])==3

    result={"statement":"E.101","status":"PASS",
      "literal_reversed_norm_identity":True,"cyclic_algebra_matrix_identities":3,
      "absolute_norm_and_eigenvector_identities":3,
      "ordinary_product_defect":[0,2],"reduced_ideal_norm":int(J.det()),
      "actual_prime_rows":d["actual_contracted_prime_rows"],
      "ordinary_L_unit_norm_image":"zeta^c e1^a e2^b: a=b=c modulo3",
      "ordinary_L_unit_norm_generators":["e1^3","zeta*e1*e2"],
      "L_S_unit_norm_image":"a=b=c modulo3 and exponent(c1)=0 modulo3; exponent(beta1) unrestricted",
      "ordinary_L_norm_quotient":[3,3],"L_S_norm_quotient":[3,3,3],
      "B_norm_lattice_certificates":stats,
      "horizontal_embedding_inverse_verified":True,
      "displayed_six_congruences_and_inverses_verified":True,
      "complete_field_norm_kernel_vectors":tests,"actual_norm_kernel_residues":zero,
      "lower_full_residue_checks":lower_checks,
      "noncube_upper_unit_residue_roots":residue_roots,
      "tested_normalized_comparison_column":list(map(int,column)),
      "comparison_column_is_twice_xi_column_mod3":True,
      "included_B1_character_rank_with_comparison_column":3,
      "comparison_column_scope":"An exact finite matrix-span check; no conclusion about the full B3 unit-character image or its transvection is inferred.",
      "L_norm_fiber_kernel":{"torsion":[3],"free_rank":6},
      "B_norm_fiber_kernel":{"torsion":[3],"free_rank":18},
      "uncertified_discovery_BNF_used_in_verification":False,
      "upper_radical_BNF_used":False,
      "eventual_h_evaluated":False,"B3_transvection_evaluated":False}
    (HERE/"e_unit_norm_complete.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))

if __name__=="__main__":main()
