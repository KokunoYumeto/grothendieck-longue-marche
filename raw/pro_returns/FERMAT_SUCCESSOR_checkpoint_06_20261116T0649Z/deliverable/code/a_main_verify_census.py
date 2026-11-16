"""Independent integrity checks for all coefficient and full pair tables.

This does not replace the enclosure computation: it verifies all saved
intervals exclude zero, independently checks prime coefficients by direct
finite-field point counts, checks exact infinite-order witnesses, and reads
every row of both full compressed CSVs in its prescribed lexicographic order.
"""
import csv,gzip,json,math,time
from collections import Counter
from fractions import Fraction
from flint import arb,ctx
from a_main_cubic_census import OUT,on_curve,mul,PRIMES

ctx.prec=256

def check_coefficients(family):
    rows=list(csv.DictReader((OUT/f"a_main_{family}_census.csv").open()))
    expected={"cubic":81,"quartic":512,"sextic":2592}[family]
    assert len(rows)==expected
    seen=set();counts=Counter();witnesses=0
    for row in rows:
        b=int(row["d" if family=="cubic" else "coefficient"])
        assert b not in seen;seen.add(b)
        power={"cubic":3,"quartic":4,"sextic":6}[family]
        sign=1 if family=="cubic" else int(row["sign"])
        assert b==sign*math.prod(p**int(row[f"e{p}"]) for p in PRIMES)
        assert all(0<=int(row[f"e{p}"])<power for p in PRIMES)
        rank=int(row["analytic_rank"]);assert rank in (0,1,2)
        assert int(row["certified_derivative_order"])==rank
        assert int(row["root_number"])==(-1)**rank
        assert row["central_status"]==("nonzero" if rank==0 else "zero")
        I=arb(row["arb_interval"].strip("[]"));assert I.is_finite() and not I.contains(0)
        counts[rank]+=1
        cache=OUT/("a_main_cubic_data" if family=="cubic" else "a_main_cm_data")
        filename=f"d{b}.json.gz" if family=="cubic" else f"{family}_{b}.json.gz"
        data=json.loads(gzip.decompress((cache/filename).read_bytes()))
        assert int(row["conductor"])==data["conductor"]
        assert int(row["root_number"])==data["root_number"]
        assert json.loads(row["minimal_model"])==data["minimal_model"]
        assert len(data["coefficients"])==data["M"]
        assert data["coefficients"][0]==1
        coeffsets=[data["coefficients"]]
        if rank==2:
            assert row["infinite_order_point"]
            P=json.loads(row["infinite_order_point"])
            assert on_curve(P,data["minimal_model"])
            assert mul(P,4 if family=="quartic" else 6,data["minimal_model"]) is not None
            witnesses+=1
            higher=data["rank2_coefficients" if family=="cubic" else "higher_coefficients"]
            assert len(higher)==int(row["terms"])
            assert higher[:data["M"]]==data["coefficients"]
            coeffsets.append(higher)
        A,B=((b,0) if family=="quartic" else (0,-432*b*b if family=="cubic" else b))
        for p in (11,13,17,19):
            # Direct finite-field count, independent of GP's ellan.
            points=1
            for x in range(p):
                rhs=(x**3+A*x+B)%p
                points+=1 if rhs==0 else (2 if pow(rhs,(p-1)//2,p)==1 else 0)
            ap=p+1-points
            for coeffs in coeffsets:
                assert coeffs[p-1]==ap,(family,b,p,coeffs[p-1],ap)
        for coeffs in coeffsets:
            assert all(type(a) is int and abs(a)<=2*n for n,a in enumerate(coeffs,1))
    print(f"{family}: {expected} rank certificates; counts {dict(sorted(counts.items()))}; "
          f"{witnesses} exact infinite-order witnesses; all direct prime traces and coefficient bounds checked.",flush=True)

def check_pairs(family):
    m=4 if family=="quartic" else 6;size=2*m**4
    expected=json.loads((OUT/f"a_main_{family}_pair_counts.json").read_text())
    counts=Counter(total_pairs=0,criterion_pairs=0,no_sections=0,cusp_only=0,
                   ordinary_only=0,ordinary_and_cusp=0)
    masks=Counter();maxmask=1<<(3 if m==4 else 10)
    points=list(csv.DictReader((OUT/f"a_main_{family}_point_dictionary.csv").open()))
    lookup={(int(p["alpha_id"]),int(p["beta_id"])):p["point_id"] for p in points}
    assert len(lookup)==(3 if m==4 else 15)
    with gzip.open(OUT/f"a_main_{family}_pairs.csv.gz","rt",newline="") as f:
        assert next(f).strip()=="alpha_id,beta_id,criterion_mask,point_ids,cusp_flags"
        for i,line in enumerate(f):
            ai,bi,mask,ids,flags=line.strip().split(",")
            ai=int(ai);bi=int(bi);mask=int(mask);flags=int(flags)
            assert (ai,bi)==divmod(i,size)
            assert 0<=mask<maxmask
            wanted=int(bi==0)+2*int(ai==0)+4*int(bi==(ai+m**4)%size)
            assert flags==wanted
            assert ids==(lookup.get((ai,bi),"") if mask else "")
            counts["total_pairs"]+=1;masks[mask]+=1
            if mask:
                counts["criterion_pairs"]+=1
                key=("ordinary_and_cusp" if flags else "ordinary_only") if ids else ("cusp_only" if flags else "no_sections")
                counts[key]+=1
    assert counts["total_pairs"]==size*size
    assert dict(counts)==expected,(family,dict(counts),expected)
    saved={int(r["criterion_mask"]):int(r["pair_count"]) for r in
           csv.DictReader((OUT/f"a_main_{family}_criterion_masks.csv").open())}
    assert dict(masks)==saved
    print(f"{family}: every one of {size*size} full CSV rows checked; counts {dict(counts)}.",flush=True)

if __name__=="__main__":
    start=time.time()
    for family in ("cubic","quartic","sextic"):check_coefficients(family)
    for family in ("quartic","sextic"):check_pairs(family)
    print(f"ALL_CENSUS_INTEGRITY_CHECKS_PASSED in {time.time()-start:.1f} seconds.",flush=True)
