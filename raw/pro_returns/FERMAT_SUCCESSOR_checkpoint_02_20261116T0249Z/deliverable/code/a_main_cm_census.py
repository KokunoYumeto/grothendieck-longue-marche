"""Certified CM coefficient census: 512 quartic and 2592 sextic classes.

Central nonvanishing uses Arb intervals with a proved exponential tail.
Zero uses the exact functional-equation sign or a verified infinite-order
point and Rubin's CM rank-zero theorem. Higher derivatives are certified
by a finite difference of the completed L-function with an explicit
Taylor remainder. An inconclusive interval is never called zero.
"""
import argparse,csv,gzip,itertools,json,math,time
from pathlib import Path
from flint import arb,ctx
from a_main_cubic_census import ROOT,OUT,PRIMES,gp_run,interval,on_curve,mul,rational_json

CACHE=OUT/"a_main_cm_data"
CACHE.mkdir(exist_ok=True)
FIELDS=("family","coefficient","e2","e3","e5","e7","sign","conductor",
        "root_number","analytic_rank","central_status","certificate",
        "certified_derivative_order","arb_interval","tail_bound","terms",
        "bits","minimal_model","torsion","rank_bounds","infinite_order_point")

def save(data):
    path=CACHE/f"{data['family']}_{data['coefficient']}.json.gz"
    path.write_bytes(gzip.compress(json.dumps(data,separators=(",",":")).encode()))

def data_for(family,b):
    path=CACHE/f"{family}_{b}.json.gz"
    if path.exists():return json.loads(gzip.decompress(path.read_bytes()))
    model=[b,0] if family=="quartic" else [0,b]
    code=f"""
E=ellminimalmodel(ellinit({model}),&v);
N=ellglobalred(E)[1];w=ellrootno(E);M=8*(sqrtint(N)+1);
print([N,w,M,[E.a1,E.a2,E.a3,E.a4,E.a6],v,elltors(E)]);
print(ellan(E,M));
"""
    meta,coeffs=gp_run(code)
    data={"family":family,"coefficient":b,"conductor":meta[0],"root_number":meta[1],
          "M":meta[2],"minimal_model":rational_json(meta[3]),
          "change":rational_json(meta[4]),"torsion":rational_json(meta[5]),
          "coefficients":coeffs}
    save(data);return data

def point_certificate(data):
    if "rank" in data:rank=data["rank"]
    else:
        rank=gp_run(f"E=ellinit({data['minimal_model']});print(ellrank(E,1));")[0]
        data["rank"]=rational_json(rank);save(data)
    bound=4 if data["family"]=="quartic" else 6
    points=rank[3]
    good=[]
    for P in points:
        assert on_curve(P,data["minimal_model"])
        if mul(P,bound,data["minimal_model"]) is not None:good.append(P)
    if not good and data["root_number"]==1:
        rank=gp_run(f"E=ellinit({data['minimal_model']});print(ellrank(E,3));",timeout=120)[0]
        data["rank"]=rational_json(rank);save(data)
        for P in rank[3]:
            assert on_curve(P,data["minimal_model"])
            if mul(P,bound,data["minimal_model"]) is not None:good.append(P)
    return rank,good

def higher_certificate(data,order):
    """Order2 requires a non-torsion point; order3 requires rank lower>=2."""
    assert order in (2,3)
    N=data["conductor"];M=20*(math.isqrt(N)+1)
    if "higher_coefficients" not in data:
        data["higher_coefficients"]=gp_run(
            f"E=ellinit({data['minimal_model']});print(ellan(E,{M}));")[0]
    ctx.prec=256
    c=2*arb.pi()/arb(N).sqrt();r=(-c).exp();h=arb(2)**(-45)
    s1=1+h;s2=1-h;w=data["root_number"];value=arb(0)
    for n,a in enumerate(data["higher_coefficients"],1):
        if a:
            z=c*n
            value+=a*(z.gamma_upper(s1)/z**s1+w*z.gamma_upper(s2)/z**s2)
    tail=4*r**(M+1)/(1-r)*(1/c+1/(c*c*(M+1)))
    value+=arb(0,tail.upper())
    j=order+2
    Bj=4*(j**j)*r/(1-r)**2*(1/c+2/c**2+2/c**3)
    remainder=Bj*h*h/((order+1)*(order+2))
    Lderivative=c*(math.factorial(order)*value/(h**order)+arb(0,remainder.upper()))
    data["higher_certificate"]={"order":order,"h":"2^-45","terms":M,"bits":256,
         "completed_value":value.str(45),"completed_tail":tail.str(16),
         "next_derivative_bound":Bj.str(16),"remainder":remainder.str(16),
         "L_derivative":Lderivative.str(35)}
    save(data);ctx.prec=160
    return Lderivative,M

def classify(data):
    ctx.prec=160;N=data["conductor"];w=data["root_number"]
    I,tail=interval(N,data["coefficients"],int(w==-1))
    row=dict(family=data["family"],coefficient=data["coefficient"],conductor=N,
         root_number=w,terms=data["M"],bits=160,
         minimal_model=json.dumps(data["minimal_model"]),torsion=json.dumps(data["torsion"]),
         rank_bounds="",infinite_order_point="",arb_interval=I.str(35),
         tail_bound=tail.str(12))
    if not I.contains(0):
        order=int(w==-1)
        row.update(analytic_rank=str(order),central_status="zero" if order else "nonzero",
             certified_derivative_order=str(order),
             certificate="exact root sign; Arb derivative interval with explicit tail")
        return row
    rank,points=point_certificate(data)
    row["rank_bounds"]=str(rank[:3])
    if points:row["infinite_order_point"]=json.dumps(rational_json(points[0]))
    if w==1 and not points:
        row.update(analytic_rank="undetermined",central_status="undetermined",
              certified_derivative_order="",certificate="interval contains zero; no non-torsion point obtained")
        return row
    row["central_status"]="zero"
    eligible=(w==1 and bool(points)) or (w==-1 and rank[0]>=2)
    if eligible:
        order=2 if w==1 else 3
        J,M=higher_certificate(data,order)
        row.update(arb_interval=J.str(35),terms=M,bits=256,
                   tail_bound="see raw higher_certificate")
        if J.is_finite() and not J.contains(0):
            row.update(analytic_rank=str(order),certified_derivative_order=str(order),
                certificate="exact rank/point lower bound, parity, Arb completed-L Taylor remainder")
        else:
            row.update(analytic_rank=f">={order}",certified_derivative_order="",
                certificate="central zero exact; higher derivative interval inconclusive")
    else:
        row.update(analytic_rank=">=1",certified_derivative_order="",
            certificate="root number -1; first derivative and higher-order lower bound unresolved")
    return row

def run(family):
    power=4 if family=="quartic" else 6
    classes=sorted(((sign*math.prod(p**e for p,e in zip(PRIMES,es)),sign,es)
           for sign in (1,-1) for es in itertools.product(range(power),repeat=4)),
           key=lambda x:(abs(x[0]),x[0]))
    dest=OUT/f"a_main_{family}_census.csv"
    previous={}
    if dest.exists():
        with dest.open() as f:previous={int(r["coefficient"]):r for r in csv.DictReader(f)}
    rows=[];start=time.time()
    for i,(b,sign,es) in enumerate(classes,1):
        if b in previous:row=previous[b]
        else:
            row=classify(data_for(family,b))
            row.update(sign=sign,**dict(zip(("e2","e3","e5","e7"),es)))
        rows.append(row)
        if b not in previous:
            with dest.open("w",newline="") as f:
                writer=csv.DictWriter(f,fieldnames=FIELDS);writer.writeheader();writer.writerows(rows)
        if i%10==0 or row["analytic_rank"] not in ("0","1"):
            print(f"{family} {i}/{len(classes)} coeff={b} N={row['conductor']} "
                  f"rank={row['analytic_rank']} central={row['central_status']} "
                  f"({time.time()-start:.1f}s)",flush=True)
    counts={}
    for row in rows:
        key=(row["central_status"],row["analytic_rank"])
        counts[str(key)]=counts.get(str(key),0)+1
    print("FINAL_COUNTS",family,json.dumps(counts,sort_keys=True),flush=True)
    assert len(rows)==2*power**4

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("family",choices=("quartic","sextic"))
    run(p.parse_args().family)
