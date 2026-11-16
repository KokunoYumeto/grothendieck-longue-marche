"""Certify the exact analytic order two in the six remaining cubic cases.

For Lambda(1)=Lambda'(1)=0 and even functional equation,
  |Lambda''(1)-2 Lambda(1+h)/h^2| <= B4*h^2/12.
Here B4 is a rigorous absolute bound for Lambda'''' on [1-h,1+h].
All special-function computations use Arb balls.
"""
import csv,gzip,json,math,time
from flint import arb,ctx
from a_main_cubic_census import OUT,CACHE,gp_run
ctx.prec=256

def certify(row):
    d=int(row["d"]);N=int(row["conductor"]);M=20*(math.isqrt(N)+1)
    data=json.loads(gzip.decompress((CACHE/f"d{d}.json.gz").read_bytes()))
    assert row["central_status"]=="zero" and row["infinite_order_point"]
    assert int(row["root_number"])==1
    coeffs=gp_run(f"E=ellinit({row['minimal_model']});print(ellan(E,{M}));")[0]
    c=2*arb.pi()/arb(N).sqrt();r=(-c).exp()
    h=arb(2)**(-45);s1=1+h;s2=1-h
    value=arb(0)
    for n,a in enumerate(coeffs,1):
        if not a:continue
        z=c*n
        value+=a*(z.gamma_upper(s1)/z**s1+z.gamma_upper(s2)/z**s2)
    # t^(+-h) <= t for t>=1, |a_n|<=2n.
    tail=4*r**(M+1)/(1-r)*(1/c+1/(c*c*(M+1)))
    value+=arb(0,tail.upper())
    # (log t)^4 <= 256*t, t^h<=t, and
    # sum n*exp(-cnt)=exp(-ct)/(1-exp(-ct))^2.
    B4=1024*r/(1-r)**2*(1/c+2/c**2+2/c**3)
    remainder=B4*h*h/12
    lambda_second=2*value/(h*h)+arb(0,remainder.upper())
    Lsecond=c*lambda_second
    assert Lsecond.is_finite() and not Lsecond.contains(0),(d,Lsecond)
    result={"d":d,"conductor":N,"terms":M,"bits":ctx.prec,"h":"2^-45",
            "completed_value":value.str(45),"completed_tail":tail.str(16),
            "fourth_derivative_bound":B4.str(16),
            "second_derivative_remainder":remainder.str(16),
            "L_second_derivative":Lsecond.str(35)}
    data["rank2_coefficients"]=coeffs
    data["rank2_certificate"]=result
    (CACHE/f"d{d}.json.gz").write_bytes(gzip.compress(json.dumps(data,separators=(",",":")).encode()))
    return result

def main():
    with (OUT/"a_main_cubic_census.csv").open() as f:rows=list(csv.DictReader(f))
    results=[];start=time.time()
    for row in rows:
        if row["analytic_rank"]!=">=2":continue
        result=certify(row);results.append(result)
        row["analytic_rank"]="2"
        row["certificate"]="exact infinite-order point and even sign; Arb second derivative with rigorous fourth-derivative remainder"
        row["arb_interval"]=result["L_second_derivative"]
        row["tail_bound"]="see a_main_cubic_rank2.csv"
        row["terms"]=str(result["terms"]);row["bits"]=str(result["bits"])
        print("rank2 certified",result["d"],result["L_second_derivative"],
              f"elapsed {time.time()-start:.1f}s",flush=True)
        with (OUT/"a_main_cubic_rank2.csv").open("w",newline="") as f:
            w=csv.DictWriter(f,fieldnames=list(results[0]));w.writeheader();w.writerows(results)
    for row in rows:row["certified_derivative_order"]=row["analytic_rank"]
    with (OUT/"a_main_cubic_census.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    assert sum(r["analytic_rank"]=="2" for r in rows)==6
    print("ALL81_ANALYTIC_RANKS_CERTIFIED: rank0=34 rank1=41 rank2=6",flush=True)

if __name__=="__main__":main()
