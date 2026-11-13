#!/usr/bin/env python3
"""Exact arithmetic and lattice certificates for E.79.

The optional --gp rebuild uses the already certified E.76 field algorithms,
then computes the full S-unit norm characters, correction maps and prime73.
Every executed stage's combined stdout/stderr is retained. No computation
of either original, still-running L2 BNF problem is launched here.
"""
from __future__ import annotations

import argparse
from itertools import product
import json
from math import gcd, prod
from pathlib import Path
import shutil
import subprocess
import tempfile

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

HERE = Path(__file__).resolve().parent
DEPENDENCIES = [
    ("e_basechange_field", "cyclotomic_base1"),
    ("e_basechange_local_norms", "cyclotomic_base1_local_norms"),
    ("e_basechange_ninth_norms", "cyclotomic_base1_ninth_norms"),
]
OWNED = [
    ("e_sclass_field_norms", "cyclotomic_sclass_norms"),
    ("e_sclass_coordinates", "cyclotomic_sclass_coordinates"),
    ("e_sclass_principal_tests", "cyclotomic_principal_norm_test"),
    ("e_sclass_export", "e_sclass_export"),
]


def dependency(name):
    candidates = [HERE / (name + ".gp"),
                  HERE.parent.parent / "research_e76/code" / (name + ".gp")]
    return next(p for p in candidates if p.exists())


def rebuild(gp):
    gp = str(Path(gp).resolve())
    with tempfile.TemporaryDirectory(prefix="e79_sclass_") as folder:
        folder = Path(folder)
        dest = folder / "research_norm_index/code"
        dest.mkdir(parents=True)
        for name, internal in DEPENDENCIES + OWNED:
            source = dependency(name) if (name, internal) in DEPENDENCIES else HERE / (name + ".gp")
            target = dest / (internal + ".gp")
            shutil.copyfile(source, target)
            run = subprocess.run([gp, "-q", str(target)], cwd=folder,
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                 text=True)
            outname = ("e_sclass_dependency_" + name.removeprefix("e_basechange_")
                       if (name, internal) in DEPENDENCIES else name)
            (HERE / (outname + ".out")).write_text(run.stdout)
            assert run.returncode == 0, (name, run.returncode)
            assert "***   at top-level" not in run.stdout, run.stdout
            assert "***   user error" not in run.stdout, run.stdout
            assert "DONE" in run.stdout or '"status":"PASS"' in run.stdout, name
        shutil.copyfile(dest / "cyclotomic_sclass_coordinates.bin",
                        HERE / "e_sclass_coordinates.bin")


def integral(M):
    return all(x.q == 1 for x in M)


def smith(record):
    H, L, R = [sp.Matrix(record[k]) for k in ("hnf", "left", "right")]
    Li, Ri = [sp.Matrix(record[k]) for k in ("left_inverse", "right_inverse")]
    ds = record["diagonal"]
    assert L*H*R == sp.diag(*ds)
    assert L*Li == Li*L == R*Ri == Ri*R == sp.eye(H.rows)
    assert integral(Li) and integral(Ri)
    assert abs(L.det()) == abs(R.det()) == 1
    assert abs(H.det()) == prod(ds)
    assert all(ds[i] % ds[i+1] == 0 for i in range(len(ds)-1))
    return H, L, R, ds


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gp")
    args = parser.parse_args()
    if args.gp:
        rebuild(args.gp)
    raw = (HERE / "e_sclass_export.out").read_text()
    assert "***   at top-level" not in raw
    records = [json.loads(line) for line in raw.splitlines() if line.startswith("{")]
    assert records[-1] == {"type": "completion", "status": "PASS"}
    indexed = {(r["type"], r.get("n")): r for r in records}
    base = indexed["base", None]
    assert base["certified"] == 1 and base["class_group"] == [3, 3]
    assert base["s_class_group"] == [3]
    V = sp.Matrix(base["s_valuation_basis"])
    assert V == sp.Matrix([[3,2,2,1,1,1], [0,1,0,0,0,0],
                          [0,0,1,0,0,0], [0,0,0,1,0,0],
                          [0,0,0,0,1,0], [0,0,0,0,0,1]])
    assert sp.Matrix(base["valuation_matrix"]) == sp.zeros(6,9).row_join(V)
    assert base["s_prime_classes"] == [[1,0]]*3 + [[2,0]]*3
    classes = sp.Matrix([[1,1,1,2,2,2], [0,0,0,0,0,0]])
    assert all(int(x) % 3 == 0 for x in classes*V)
    assert V.det() == 3
    for j, nrm in enumerate(base["s_generator_norms"]):
        assert nrm == 3**sum(V[i,j] for i in range(3))*17**(2*sum(V[i,j] for i in range(3,6)))

    x = sp.symbols("x")
    P = sp.Poly(sum(c*x**i for i,c in enumerate(base["polynomial_ascending"])),x,domain=sp.QQ)
    def element(vec):
        return sp.Poly(sum(sp.Rational(a,b)*x**i for i,(a,b) in enumerate(vec)),x,domain=sp.QQ)
    def power(a,n):
        out=sp.Poly(1,x,domain=sp.QQ)
        while n:
            if n&1: out=(out*a).rem(P)
            a=(a*a).rem(P); n//=2
        return out
    xi,a=element(base["xi"]),element(base["a"])
    assert power(xi,9).as_expr()==1 and power(a,3).as_expr()==17
    assert (a-xi).as_expr()==x
    beta=(a*xi).rem(P)
    assert power(beta,3)==17*power(xi,3)

    smith_count=0
    correction_count=0
    tests=0
    summary={}
    for n in (3,9):
        rec=indexed["norm_characters",n]
        M,U,C=[sp.Matrix(rec[k]) for k in ("matrix","unit_matrix","nonunit_matrix")]
        assert M==U.row_join(C) and M.shape==(6,15)
        image,_,_,ids=smith(indexed["s_image",n]); smith_count+=1
        assert image==hermite_normal_form((n*sp.eye(6)).row_join(M))
        assert ids==[n,1,1,1,1,1]
        full,_,_,fds=smith(indexed["s_norm_kernel",n]); smith_count+=1
        assert all(int(z)%n==0 for z in M*full)
        assert fds==[n]*5+[1]*10
        assert full.det()==n**5
        ku,_,_,uds=smith(indexed["unit_norm_kernel",n]); smith_count+=1
        assert all(int(z)%n==0 for z in U*ku)
        assert ku.det()=={3:27,9:2187}[n]
        K,_,_,kds=smith(indexed["correctable_exponents",n]); smith_count+=1
        VK,_,_,vds=smith(indexed["correctable_divisors",n]); smith_count+=1
        assert VK==V*K
        UH=hermite_normal_form((n*sp.eye(6)).row_join(U))
        assert integral(UH.inv()*C*K)
        assert K.det()==UH.det()/image.det()
        assert [d for d in kds if d>1]=={3:[3,3],9:[9,3]}[n]
        assert [d for d in vds if d>1]=={3:[3,3,3],9:[9,3,3]}[n]
        R=sp.Matrix(rec["ordinary_unit_correction"])
        assert all(int(z)%n==0 for z in U*R+C*K)
        correction_count+=6

        # Exhaust the complete residue domain for the two displayed input
        # congruences; exact index equality above proves all integer lifts.
        period=n
        Ki=K.inv()
        for t in product(range(period),repeat=5):
            v=sp.Matrix([0,*t])
            expected=(t[2]-t[4])%3==0 and (t[3]-t[4])%3==0
            if n==9:
                expected=expected and (3*t[0]-3*t[1]-2*t[2]-2*t[3]+4*t[4])%9==0
            assert integral(Ki*v)==expected
            tests+=1

        c1=indexed["c1_correction",n]
        CU=sp.Matrix(c1["unit_matrix"])
        scalars=c1["comparison_scalars"]
        assert all(gcd(n,s)==1 for s in scalars)
        assert all(int(z)%n==0 for z in CU-sp.diag(*scalars)*U)
        cc=sp.Matrix(c1["c1_character"])
        sol=sp.Matrix(c1["correction_exponents"])
        assert all(int(z)%n==0 for z in CU*sol+cc)
        assert c1["c1_valuations"]==[1,1,1,0,0,0]
        correction_count+=1
        summary[str(n)]={"s_unit_field_norm_index":n**5,
                         "s_class_coinvariants_first_step":[3],
                         "s_exponent_quotient":[d for d in kds if d>1],
                         "s_divisor_quotient":[d for d in vds if d>1],
                         "complete_exponent_kernel_diagonal":fds,
                         "c1_correction":c1["correction_exponents"],
                         "actual_s_unit_norm_defect_order_divides":3}

    prime=indexed["prime73",None]
    assert prime["rational_prime"]==73 and prime["degree"]==1 and prime["class"]==[2,1]
    I=sp.Matrix(prime["ideal"])
    ev=sp.Matrix([prime["integral_basis_residues"]])
    assert I.det()==73 and all(int(v)%73==0 for v in ev*I)
    assert sp.isprime(73) and P.eval(prime["primitive_residue"])%73==0
    def mod_eval(v):
        value=element(v).eval(prime["primitive_residue"])
        return int(value.p)*pow(int(value.q),-1,73)%73
    assert mod_eval(base["xi"])==prime["xi_residue"]==55
    assert mod_eval(base["a"])==prime["a_residue"]==15
    assert [mod_eval(v) for v in base["integral_basis"]]==prime["integral_basis_residues"]
    assert 55*15%73==prime["beta_residue"]==22
    assert pow(63,3,73)==22 and pow(22,3,73)==63 and pow(22,8,73)==1
    assert pow(22,4,73)!=1
    chain=[]
    for d in range(1,41):
        rd=22 if d%2 else 63
        assert pow(rd,3**(d-1),73)==22
        if chain: assert pow(rd,3,73)==chain[-1]
        assert (3**(d-1)*pow(rd,max(0,3**(d-1)-1),73))%73!=0
        chain.append(rd)

    # Literal finite residue witness for the uncorrected c1 at 17.
    def mul(v,w):
        a,b=v; c,d=w
        return ((a*c-b*d)%17,(a*d+b*c-b*d)%17)
    def fpower(a,n):
        b=(1,0)
        while n:
            if n&1:b=mul(b,a)
            a=mul(a,a);n//=2
        return b
    z=(0,1);c1=(1,3)
    assert fpower(z,3)==(1,0) and fpower(c1,96)==z
    xis=[w for w in product(range(17),repeat=2) if fpower(w,3)==z]
    assert len(xis)==3
    for w in xis:
        assert fpower(w,9)==(1,0) and fpower(w,3)!=(1,0)
        assert fpower(mul(w,c1),96)==(1,0)

    result={"status":"PASS","statement":"E.79",
            "full_integer_smith_inverse_certificates":smith_count,
            "literal_ordinary_unit_corrections":correction_count,
            "complete_congruence_residue_checks":tests,
            "exact_s_unit_divisor_identities":15,
            "coherent_prime73_levels":len(chain),
            "prime73_class":[2,1],"prime73_roots":chain[:6],
            "tame_c1_correction_checks":len(xis),
            "finite_data":summary,
            "uniform_theorem":"For every d>=1 and n=3 or9, the complete S-unit field-norm index is n^5 and actual norm identifies S-class coinvariants with the base S-class group.",
            "remaining_data":["The higher full S-class groups and cyclic module annihilators are unevaluated.","The capitulation maps determining the actual S-unit norm defect are unevaluated.","The eventual original exponent h is unevaluated."]}
    (HERE/"e_sclass_norms.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__=="__main__":main()
