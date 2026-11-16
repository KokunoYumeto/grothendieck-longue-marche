"""Exact arithmetic and Arb central-value certificates for 81 cubic classes.

Requires PARI/GP 2.19.1 (source digest recorded in a_main_fetch_pari.py)
and python-flint 0.9.0.  No ellanalyticrank output is used as a certificate.
Run from the project root.  Each raw exact GP result is retained in gzip JSON.
"""
import ast
import csv
import gzip
import itertools
import json
import math
import os
from pathlib import Path
import subprocess
import time
from fractions import Fraction as F
from flint import arb, ctx

ROOT=Path(__file__).resolve().parents[2]
GP=Path(os.environ.get("A_MAIN_GP",str(ROOT/"work/pari-2.19.1/gp")))
OUT=ROOT/"deliverable/code"
CACHE=OUT/"a_main_cubic_data"
CACHE.mkdir(exist_ok=True)
ctx.prec=160
PRIMES=(2,3,5,7)

def parse_gp(s):
    """Parse only exact numbers and lists; GP rational fractions stay exact."""
    def rec(x):
        if isinstance(x,ast.Expression): return rec(x.body)
        if isinstance(x,ast.Constant) and isinstance(x.value,int): return x.value
        if isinstance(x,ast.List): return [rec(t) for t in x.elts]
        if isinstance(x,ast.UnaryOp) and isinstance(x.op,ast.USub): return -rec(x.operand)
        if isinstance(x,ast.BinOp) and isinstance(x.op,ast.Div): return F(rec(x.left),rec(x.right))
        raise ValueError(ast.dump(x))
    return rec(ast.parse(s,mode="eval"))

def gp_run(code,timeout=120):
    inp=code+"\nquit;\n"
    p=subprocess.run([str(GP),"-fq","-s","128000000"],input=inp,text=True,capture_output=True,timeout=timeout)
    if p.returncode or "***" in p.stderr:
        raise RuntimeError(p.stderr[:3000])
    return [parse_gp(line) for line in p.stdout.splitlines() if line.strip()]

def rational_json(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,list): return [rational_json(y) for y in x]
    return x

def add(P,Q,A):
    a1,a2,a3,a4,a6=map(F,A)
    if P is None: return Q
    if Q is None: return P
    x1,y1=map(F,P);x2,y2=map(F,Q)
    if x1==x2 and y2==-y1-a1*x1-a3:return None
    if (x1,y1)==(x2,y2):
        lam=(3*x1*x1+2*a2*x1+a4-a1*y1)/(2*y1+a1*x1+a3)
        nu=(-x1**3+a4*x1+2*a6-a3*y1)/(2*y1+a1*x1+a3)
    else:
        lam=(y2-y1)/(x2-x1)
        nu=(y1*x2-y2*x1)/(x2-x1)
    x3=lam*lam+a1*lam-a2-x1-x2
    return x3,-(lam+a1)*x3-nu-a3

def mul(P,n,A):
    Q=None
    for _ in range(n):Q=add(Q,P,A)
    return Q

def on_curve(P,A):
    x,y=map(F,P);a1,a2,a3,a4,a6=map(F,A)
    return y*y+a1*x*y+a3*y==x**3+a2*x*x+a4*x+a6

def interval(N,coeffs,derivative=0):
    c=2*arb.pi()/arb(N).sqrt()
    r=(-c).exp();S=arb(0);rn=arb(1)
    for n,a in enumerate(coeffs,1):
        if derivative==0:
            rn*=r
            if a:S+=a*rn/n
        elif a:S+=a*(c*n).expint(1)/n
    M=len(coeffs)
    tail=4*r**(M+1)/(1-r)
    if derivative:
        tail/=c*(M+1)
    I=2*S+arb(0,tail.upper())
    return I,tail

def exact_data(d):
    path=CACHE/f"d{d}.json.gz"
    if path.exists():
        return json.loads(gzip.decompress(path.read_bytes()))
    code=f"""
E=ellminimalmodel(ellinit([0,{-432*d*d}]),&v);
N=ellglobalred(E)[1]; w=ellrootno(E); M=8*(sqrtint(N)+1);
print([N,w,M,[E.a1,E.a2,E.a3,E.a4,E.a6],v,elltors(E)]);
print(ellan(E,M));
"""
    meta,coeffs=gp_run(code)
    data={"d":d,"conductor":meta[0],"root_number":meta[1],"M":meta[2],
          "minimal_model":rational_json(meta[3]),"change":rational_json(meta[4]),
          "torsion":rational_json(meta[5]),"coefficients":coeffs}
    path.write_bytes(gzip.compress(json.dumps(data,separators=(",",":")).encode()))
    return data

FIELDS=("d","e2","e3","e5","e7","conductor","root_number","analytic_rank",
        "central_status","certificate","arb_interval","tail_bound","terms","bits",
        "minimal_model","torsion","rank_bounds","infinite_order_point")

def run():
    rows=[];start=time.time()
    exponents=sorted(itertools.product(range(3),repeat=4),
                     key=lambda es:math.prod(p**e for p,e in zip(PRIMES,es)))
    for es in exponents:
        d=math.prod(p**e for p,e in zip(PRIMES,es))
        data=exact_data(d);N=data["conductor"];w=data["root_number"]
        I,tail=interval(N,data["coefficients"],int(w==-1))
        row=dict(zip(("e2","e3","e5","e7"),es))
        row.update(d=d,conductor=N,root_number=w,terms=data["M"],bits=ctx.prec,
                   minimal_model=json.dumps(data["minimal_model"]),
                   torsion=json.dumps(data["torsion"]),
                   arb_interval=I.str(35),tail_bound=tail.str(12),
                   rank_bounds="",infinite_order_point="")
        if w==1 and not I.contains(0):
            row.update(analytic_rank="0",central_status="nonzero",
                       certificate="Arb interval and explicit exponential tail")
        elif w==-1 and not I.contains(0):
            row.update(analytic_rank="1",central_status="zero",
                       certificate="root number -1; nonzero certified first derivative")
        else:
            rank=gp_run("E=ellinit("+row["minimal_model"]+");print(ellrank(E,1));")[0]
            row["rank_bounds"]=str(rank[:3])
            data["rank"]=rational_json(rank)
            infinite=[]
            for P in rank[3]:
                assert on_curve(P,data["minimal_model"])
                if mul(P,6,data["minimal_model"]) is not None:infinite.append(P)
            if infinite:
                row["infinite_order_point"]=json.dumps(rational_json(infinite[0]))
            if w==-1:
                lower=3 if rank[0]>=2 else 1
                row.update(analytic_rank=f">={lower}",central_status="zero",
                           certificate="root number -1; higher order not yet certified")
            elif infinite:
                row.update(analytic_rank=">=2",central_status="zero",
                           certificate="exact infinite-order point; Rubin Corollary C; even sign")
            else:
                row.update(analytic_rank="undetermined",central_status="undetermined",
                           certificate="central interval contains zero; no point certificate obtained")
            (CACHE/f"d{d}.json.gz").write_bytes(gzip.compress(json.dumps(data,separators=(",",":")).encode()))
        rows.append(row)
        with (OUT/"a_main_cubic_census.csv").open("w",newline="") as f:
            writer=csv.DictWriter(f,fieldnames=FIELDS);writer.writeheader();writer.writerows(rows)
        print(f"d={d:5} N={N:8} w={w:+} rank={row['analytic_rank']:>4} "
              f"central={row['central_status']} ({time.time()-start:.1f}s)",flush=True)
    assert len(rows)==81
    counts={}
    for row in rows:
        key=(row["central_status"],row["analytic_rank"])
        counts[str(key)]=counts.get(str(key),0)+1
    print("FINAL_COUNTS",json.dumps(counts,sort_keys=True),flush=True)
    return rows

if __name__=="__main__":run()
