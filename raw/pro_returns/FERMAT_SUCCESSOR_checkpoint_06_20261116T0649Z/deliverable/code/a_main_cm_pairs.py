"""Lossless full class-pair CSVs, compressed with gzip, and exact join tables.

The input coefficient census must be complete.  A row whose criterion_mask
is zero is not classified by the rank-zero criterion.  For a nonzero mask,
point_ids and cusp_flags give the complete Selmer section centres; every
rational cusp contributes its whole completed Kummer packet.

CSV columns: alpha_id,beta_id,criterion_mask,point_ids,cusp_flags.
Use --decode ALPHA_ID BETA_ID for a human-readable lossless row decoder.
"""
import argparse,csv,gzip,itertools,json,math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from sympy import integer_nthroot
from a_main_cubic_census import OUT,PRIMES

RULES={
 "quartic":[
  ("-4*alpha*beta",1,1,1,(2,0,0,0)),
  ("4*alpha/beta^2",1,-2,0,(2,0,0,0)),
  ("4*beta/alpha^2",-2,1,0,(2,0,0,0))],
 "sextic":[
  ("alpha^2*beta^3",2,3,0,(0,0,0,0)),
  ("alpha^3*beta^2",3,2,0,(0,0,0,0)),
  ("alpha^2*beta",2,1,0,(0,0,0,0)),
  ("alpha*beta^2",1,2,0,(0,0,0,0)),
  ("-alpha^3*beta",3,1,1,(0,0,0,0)),
  ("-alpha*beta^3",1,3,1,(0,0,0,0)),
  ("-4*alpha*beta",1,1,1,(2,0,0,0)),
  ("4*alpha/beta^2",1,-2,0,(2,0,0,0)),
  ("4*beta/alpha^2",-2,1,0,(2,0,0,0)),
  ("-432*(alpha*beta)^2",2,2,1,(4,3,0,0))]}

def classes(m):
    return [(sign,)+es for sign in (0,1) for es in itertools.product(range(m),repeat=4)]

def representative(digits):
    return (-1)**digits[0]*math.prod(p**e for p,e in zip(PRIMES,digits[1:]))

def index(ds,m):
    result=ds[0]
    for e in ds[1:]:result=result*m+int(e)
    return result

def class_id(q,m):
    q=F(q);sign=int(q<0);num=abs(q.numerator);den=q.denominator;es=[]
    for p in PRIMES:
        e=0
        while num%p==0:num//=p;e+=1
        while den%p==0:den//=p;e-=1
        es.append(e%m)
    assert num==den==1
    return index((sign,)+tuple(es),m)

def nthroot(q,m):
    q=F(q);assert q>=0
    a,ok1=integer_nthroot(q.numerator,m);b,ok2=integer_nthroot(q.denominator,m)
    assert ok1 and ok2
    return F(a,b)

def orbit(t):
    t=F(t)
    return {t,1-t,1/t,1/(1-t),t/(t-1),(t-1)/t}

def point_dictionary(m,ds):
    ts=sorted(orbit(-1) if m==4 else orbit(-1)|orbit(-8)|orbit(4))
    assert len(ts)==(3 if m==4 else 15)
    results=[]
    for i,t in enumerate(ts):
        a=class_id(t,m);b=class_id(1-t,m)
        alpha=representative(ds[a]);beta=representative(ds[b])
        u=nthroot(t/alpha,m);v=nthroot((1-t)/beta,m)
        pts=[[str(su*u),str(sv*v),"1"] for su in (1,-1) for sv in (1,-1)]
        for x,y,z in pts:assert alpha*F(x)**m+beta*F(y)**m==F(z)**m
        results.append({"point_id":i,"t":str(t),"alpha_id":a,"beta_id":b,
            "curve_points":json.dumps(pts,separators=(",",":"))})
    return results

def write_table(path,rows):
    with path.open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def prepare(family):
    m=4 if family=="quartic" else 6;ds=classes(m);size=len(ds)
    with (OUT/f"a_main_{family}_census.csv").open() as f:
        curves={int(r["coefficient"]):r for r in csv.DictReader(f)}
    assert len(curves)==size
    assert all(r["central_status"] in ("zero","nonzero") for r in curves.values())
    rows=[];zero=np.zeros(size,dtype=bool)
    for i,digits in enumerate(ds):
        value=representative(digits);r=curves[value];zero[i]=r["central_status"]=="nonzero"
        rows.append(dict(class_id=i,representative=value,sign=(-1)**digits[0],
            **dict(zip(("e2","e3","e5","e7"),digits[1:])),
            elliptic_conductor=r["conductor"],analytic_rank=r["analytic_rank"],
            central_status=r["central_status"]))
    write_table(OUT/f"a_main_{family}_classes.csv",rows)
    points=point_dictionary(m,ds)
    write_table(OUT/f"a_main_{family}_point_dictionary.csv",points)
    rule_rows=[dict(bit=i,coefficient=f,alpha_exponent=a,beta_exponent=b,
        constant_sign=(-1)**s,**dict(zip(("constant_e2","constant_e3","constant_e5","constant_e7"),e)))
         for i,(f,a,b,s,e) in enumerate(RULES[family])]
    write_table(OUT/f"a_main_{family}_join_rules.csv",rule_rows)
    return m,ds,zero,points

def row_masks(family,m,ds,zero,ai):
    a=np.array(ds[ai],dtype=np.int64);beta=np.asarray(ds,dtype=np.int64)
    weights=np.array([m**3,m**2,m,1],dtype=np.int64)
    mask=np.zeros(len(ds),dtype=np.uint16)
    for i,(name,pa,pb,sign,es) in enumerate(RULES[family]):
        signs=(sign+pa*a[0]+pb*beta[:,0])%2
        exponents=(pa*a[1:]+pb*beta[:,1:]+np.array(es))%m
        targets=signs*m**4+exponents@weights
        mask|=zero[targets].astype(np.uint16)<<i
    return mask

def expand_cusps(ai,bi,m,ds):
    alpha=representative(ds[ai]);beta=representative(ds[bi]);pts=[]
    if bi==0:pts.extend([["0","1","1"],["0","-1","1"]])
    if ai==0:pts.extend([["1","0","1"],["-1","0","1"]])
    if bi==(ai+m**4)%(2*m**4):pts.extend([["1","1","0"],["1","-1","0"]])
    for x,y,z in pts:assert alpha*F(x)**m+beta*F(y)**m==F(z)**m
    return pts

def run(family):
    m,ds,zero,points=prepare(family);size=len(ds)
    lookup={}
    for p in points:lookup.setdefault((p["alpha_id"],p["beta_id"]),[]).append(p["point_id"])
    counts={"total_pairs":size*size,"criterion_pairs":0,"no_sections":0,
            "cusp_only":0,"ordinary_only":0,"ordinary_and_cusp":0}
    histogram=np.zeros(1<<len(RULES[family]),dtype=np.int64)
    dest=OUT/f"a_main_{family}_pairs.csv.gz"
    with gzip.open(dest,"wt",newline="",compresslevel=6) as f:
        f.write("alpha_id,beta_id,criterion_mask,point_ids,cusp_flags\n")
        for ai in range(size):
            masks=row_masks(family,m,ds,zero,ai)
            histogram+=np.bincount(masks,minlength=len(histogram))
            cuspflags=np.zeros(size,dtype=np.uint8)
            cuspflags[0]|=1
            if ai==0:cuspflags|=2
            cuspflags[(ai+m**4)%size]|=4
            lines=[]
            for bi,mask in enumerate(masks):
                mask=int(mask);cf=int(cuspflags[bi]);ids=lookup.get((ai,bi),[]) if mask else []
                if mask:
                    counts["criterion_pairs"]+=1
                    category=("ordinary_and_cusp" if cf else "ordinary_only") if ids else ("cusp_only" if cf else "no_sections")
                    counts[category]+=1
                elif (ai,bi) in lookup:
                    raise AssertionError(("known candidate missing every criterion",ai,bi))
                lines.append(f"{ai},{bi},{mask},{';'.join(map(str,ids))},{cf}\n")
            f.write("".join(lines))
            if ai%100==0:print(f"{family}: wrote alpha {ai}/{size}",flush=True)
    write_table(OUT/f"a_main_{family}_criterion_masks.csv",
        [{"criterion_mask":i,"pair_count":int(n)} for i,n in enumerate(histogram) if n])
    (OUT/f"a_main_{family}_pair_counts.json").write_text(json.dumps(counts,indent=2)+"\n")
    print("FINAL_COUNTS",json.dumps(counts,sort_keys=True),flush=True)

def decode(family,ai,bi):
    m,ds,zero,points=prepare(family);assert 0<=ai<len(ds) and 0<=bi<len(ds)
    mask=int(row_masks(family,m,ds,zero,ai)[bi])
    selected=[p for p in points if (p["alpha_id"],p["beta_id"])==(ai,bi)]
    print(json.dumps({"family":family,"alpha":representative(ds[ai]),"beta":representative(ds[bi]),
         "criterion_mask":mask,"applicable_targets":[r[0] for i,r in enumerate(RULES[family]) if mask&(1<<i)],
         "classification_complete":bool(mask),"ordinary_points":selected if mask else None,
         "cusps":expand_cusps(ai,bi,m,ds),"each_cusp_packet":"H^1(Q,Zhat(1)), with a chosen tangent origin"},
         indent=2))

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("family",choices=("quartic","sextic"))
    p.add_argument("--decode",nargs=2,type=int)
    a=p.parse_args()
    decode(a.family,*a.decode) if a.decode else run(a.family)
