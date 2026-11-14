#!/usr/bin/env python3
"""E97: rebuild the two exact PARI stages and independently check the norm defect.

Only the degree-six L1 BNF is computed.  The degree-eighteen upper field is
used through exact nf/ideal operations and the proved lower genus map.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
from itertools import product
import json
from math import gcd, lcm
from pathlib import Path
import shutil
import subprocess
import tempfile
import sympy as sp

HERE=Path(__file__).resolve().parent

def lower_source():
    for p in (HERE/"e_stable_lower_genus.gp",
              HERE.parent.parent/"research_e86/code/e_stable_lower_genus.gp"):
        if p.exists(): return p
    raise FileNotFoundError("e_stable_lower_genus.gp")

def rebuild(gp):
    gp=str(Path(gp).resolve())
    with tempfile.TemporaryDirectory(prefix="e97_exact_") as td:
        root=Path(td)
        lower=root/"research_e86/code"; own=root/"research_e97/code"
        lower.mkdir(parents=True); own.mkdir(parents=True)
        stages=[(lower_source(),lower/"e_stable_lower_genus.gp","e_unit_norm_coset_lower"),
                (HERE/"e_unit_norm_coset.gp",own/"e_unit_norm_coset.gp","e_unit_norm_coset_gp")]
        for source,dest,label in stages:
            shutil.copyfile(source,dest)
            result=subprocess.run([gp,"-q",str(dest)],cwd=root,text=True,
                                  stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            (HERE/(label+".out")).write_text(result.stdout)
            assert result.returncode==0,(label,result.returncode)
            assert "***   at top-level" not in result.stdout,result.stdout
            assert "***   user error" not in result.stdout,result.stdout
            assert "DONE" in result.stdout,label
            print(label,"PASS",flush=True)
        shutil.copyfile(own/"e_unit_norm_coset.bin",HERE/"e_unit_norm_coset.bin")
        shutil.copyfile(lower/"e_stable_lower_genus.bin",HERE/"e_unit_norm_coset_lower.bin")

class Field:
    def __init__(self,mod):
        self.mod=tuple(map(Q,mod));self.n=len(mod)-1
        assert self.mod[-1]==1
        self.zero=(Q(0),)*self.n
        self.one=(Q(1),)+(Q(0),)*(self.n-1)
    def elt(self,a):
        if isinstance(a,(int,Q)):
            return (Q(a),)+(Q(0),)*(self.n-1)
        a=list(map(Q,a))
        a += [Q(0)]*max(0,self.n-len(a))
        for k in range(len(a)-1,self.n-1,-1):
            v=a[k]
            if v:
                for j in range(self.n):
                    a[k-self.n+j]-=v*self.mod[j]
        return tuple(a[:self.n])
    def add(self,a,b):return tuple(x+y for x,y in zip(a,b))
    def neg(self,a):return tuple(-x for x in a)
    def mul(self,a,b):
        c=[Q(0)]*(2*self.n-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):c[i+j]+=x*y
        return self.elt(c)
    def scale(self,a,k):return tuple(x*k for x in a)
    def pow(self,a,n):
        r=self.one
        while n:
            if n&1:r=self.mul(r,a)
            a=self.mul(a,a);n//=2
        return r
    def sub(self,a,b):return self.add(a,self.neg(b))
    def eval(self,a,t):
        ans=self.zero
        for v in reversed(a):ans=self.add(self.mul(ans,t),self.elt(v))
        return ans
    def matmul(self,A,B):
        return [[sum_field(self,[self.mul(A[i][k],B[k][j])
                    for k in range(len(B))]) for j in range(len(B[0]))]
                for i in range(len(A))]
    def matadd(self,A,B):return [[self.add(x,y) for x,y in zip(a,b)] for a,b in zip(A,B)]
    def matscale(self,A,k):return [[self.mul(x,k) for x in row] for row in A]
    def eye(self,n):return [[self.one if i==j else self.zero for j in range(n)] for i in range(n)]

def sum_field(F,xs):
    ans=F.zero
    for x in xs:ans=F.add(ans,x)
    return ans

def valuation(n,p):
    assert n
    k=0
    while n%p==0:k+=1;n//=p
    return k

def polyval(a,x):
    y=0
    for c in reversed(a):y=y*x+c
    return y

def hensel_root(a,r,p,k):
    der=[i*a[i] for i in range(1,len(a))]
    modulus=p
    assert polyval(a,r)%p==0 and gcd(polyval(der,r),p)==1
    for _ in range(1,k):
        correction=(-(polyval(a,r)//modulus)*pow(polyval(der,r),-1,p))%p
        r+=modulus*correction;modulus*=p
        assert polyval(a,r)%modulus==0
    return r

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--gp");arg=ap.parse_args()
    if arg.gp:rebuild(arg.gp)
    source=(HERE/"e_unit_norm_coset_gp.out").read_text()
    assert "***   at top-level" not in source and "***   user error" not in source
    records=[json.loads(line) for line in source.splitlines() if line.startswith("{")]
    data={r["name"]:r["value"] for r in records if "name" in r}
    assert records[-1]=={"type":"completion","status":"PASS","prime_orbits":4,
                         "ordinary_unit_defect":[0,1],"xic1_S_unit_defect":1}
    F=Field([289,0,0,17,0,0,1]);b=F.elt([0,1]);z=F.scale(F.pow(b,3),Q(1,17))
    u=[F.scale(F.elt(row),Q(1,data["horizontal_witness_denominator"]))
       for row in data["horizontal_witness_numerator"]]
    norm=sum_field(F,[F.pow(u[0],3),F.mul(z,F.pow(u[1],3)),
                     F.mul(F.pow(z,2),F.pow(u[2],3)),
                     F.scale(F.mul(z,F.mul(u[0],F.mul(u[1],u[2]))),-3)])
    assert norm==b and F.add(F.add(F.pow(z,2),z),F.one)==F.zero
    A=[[F.zero,F.zero,z],[F.one,F.zero,F.zero],[F.zero,F.one,F.zero]]
    I=F.eye(3);A2=F.matmul(A,A)
    S=[[F.one,F.zero,F.zero],[F.zero,z,F.zero],[F.zero,F.zero,F.pow(z,2)]]
    B=F.matmul(F.matadd(F.matadd(F.matscale(I,u[0]),F.matscale(A,u[1])),
                       F.matscale(A2,u[2])),S)
    assert F.matmul(A2,A)==F.matscale(I,z)
    assert F.matmul(F.matmul(B,B),B)==F.matscale(I,b)
    assert F.matmul(B,A)==F.matscale(F.matmul(A,B),z)
    poly=[289]+[0]*8+[17]+[0]*8+[1]
    L=Field(poly);a=L.elt([0,1]);za=L.scale(L.pow(a,9),Q(1,17))
    w=L.elt([Q(*x) for x in data["switched_witness"]])
    sigmaa=L.mul(a,za)
    sw=L.eval(w,sigmaa);s2w=L.eval(sw,sigmaa)
    assert L.mul(L.mul(w,sw),s2w)==za
    assert L.eval(s2w,sigmaa)==w
    den=lcm(*(x.denominator for x in w));num=[int(x*den) for x in w]
    hensel_checks=0;class_sum=[0,0,0];divisor_orbits=[]
    for p,r,rb,v,d,art,total in data["support_orbits"]:
        assert sp.isprime(p)
        assert pow(r,3,p)==rb
        zz=pow(r,9,p)*pow(17,-1,p)%p
        assert zz!=1 and (zz*zz+zz+1)%p==0
        roots=[r,r*pow(zz,-1,p)%p,r*pow(zz,-2,p)%p]
        assert len(set(roots))==3
        vd=valuation(den,p) if den%p==0 else 0
        for root,expected in zip(roots,v):
            lifted=hensel_root(poly,root,p,vd+4)
            value=polyval(num,lifted)
            assert value
            actual=valuation(value,p)-vd
            assert actual==expected,(p,root,expected,actual)
            hensel_checks+=1
        assert [d[2]-d[0],d[0]-d[1],d[1]-d[2]]==v
        assert sum(v)==0 and sum(d)==total
        class_sum=[x+total*y for x,y in zip(class_sum,art)]
        divisor_orbits.append({"prime":p,"root":r,"valuations":v,"divisor_coefficients":d,
                               "arithmetic_genus_coordinate":art})
    genus=[class_sum[i]%m for i,m in enumerate([9,3,3])]
    assert genus==data["genus_coordinate"][:3]==[0,1,2]
    C=sp.Matrix([[sp.Rational(*x) for x in row] for row in data["class_forward"]])
    CI=sp.Matrix(data["class_inverse"])
    assert C*CI==sp.eye(3) and CI*C==sp.eye(3)
    cv=C*sp.Matrix(genus);orders=data["class_orders"]
    assert all(x.q==1 for x in cv)
    result=[int(x)%m for x,m in zip(cv,orders)]
    assert result==data["ideal_class"]==[0,1,0]
    q=sp.Matrix(data["strongly_ambiguous_generator"])
    H=sp.Matrix(data["strongly_ambiguous_lattice"])
    assert q==sp.Matrix([3,0,0]) and H==sp.diag(3,3,1)
    assert H.inv()*sp.Matrix(result)==sp.Matrix([0,sp.Rational(1,3),0])
    class_checks=0
    for x,y,z0 in product(range(9),range(3),range(3)):
        if (x+y+z0)%3:continue
        cl=[(x-3*y-3*z0)%9,y]
        back=[(-2*cl[0])%9,cl[1]%3,(-cl[0]-cl[1])%3]
        assert back==[x,y,z0]
        class_checks+=1
    assert class_checks==27
    c1=F.add(F.add(b,F.one),F.scale(z,3))
    cu=L.eval(c1,L.pow(a,3))
    assert L.eval(cu,sigmaa)==cu
    quotient={}
    for aa,bb in product(range(9),range(3)):
        quotient.setdefault((aa%3,bb),[]).append((aa,bb))
    assert len(quotient)==9 and all(len(v)==3 for v in quotient.values())
    horizontal={i:(0,i) for i in range(3)}
    assert [i for i,v in horizontal.items() if v==tuple(result[:2])]==[1]
    summary={
        "status":"PASS","literal_horizontal_norm_identity":True,
        "cyclic_algebra_matrix_identities":3,"independent_absolute_norm_identity":True,
        "complete_GP_prime_orbits":len(divisor_orbits),
        "independent_Hensel_valuation_checks":hensel_checks,
        "class_coordinate_inverses":class_checks,
        "ordinary_norm_quotient_cosets":len(quotient),
        "horizontal_defect_preimage":1,
        "ordinary_unit_defect":[0,1],"strongly_ambiguous_subgroup_generator":[3,0],
        "ordinary_unit_norm_quotient":[3,3],"xic1_S_unit_defect":1,
        "completed_power_line_norm_exponents":"3 Z_3",
        "completed_nonempty_fiber_kernel":{"torsion":[3],"free_rank":18},
        "divisor_orbits":divisor_orbits,
        "eventual_h_evaluated":False,"old_transvection_evaluated":False,
        "upper_BNF_used":False
    }
    (HERE/"e_unit_norm_coset.json").write_text(json.dumps(summary,indent=2)+"\n")
    print(json.dumps(summary,indent=2))

if __name__=="__main__":main()
