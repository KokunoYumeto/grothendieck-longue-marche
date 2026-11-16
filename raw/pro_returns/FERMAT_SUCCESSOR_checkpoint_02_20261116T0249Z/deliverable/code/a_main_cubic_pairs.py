"""Complete rational-point and cusp-packet lists in the 6561 cubic classes.

The classification applies only when the associated central value is nonzero.
Blank lists outside that criterion mean 'not classified here', never 'empty'.
The proof uses torsion <=6, the plane-cubic hyperplane divisor, and the
valuation obstruction (1,2,0) modulo3 at a prime.
"""
import csv,itertools,json,math
from fractions import Fraction as F
from pathlib import Path
import sympy as s
from a_main_cubic_census import OUT,PRIMES

def main():
    with (OUT/"a_main_cubic_census.csv").open() as f:
        curves={int(r["d"]):r for r in csv.DictReader(f)}
    assert len(curves)==81 and all(r["analytic_rank"] in ("0","1","2") for r in curves.values())
    X,Y,Z,a,b=s.symbols("X Y Z a b")
    polynomial=a*X**3+b*Y**3-Z**3
    assert s.factor(s.det(s.hessian(polynomial,(X,Y,Z))))==-216*a*b*X*Y*Z
    print("Diagonal cubic Hessian is -216*a*b*X*Y*Z.",flush=True)
    for d,row in curves.items():
        for p,expected in ((11,12),(17,18)):
            assert 1+sum((y*y-x**3+432*d*d)%p==0 for x in range(p) for y in range(p))==expected
        root2=s.integer_nthroot(432*d*d,3)[1]
        root3=s.integer_nthroot(1728*d*d,3)[1]
        assert root2==(d==2)
        assert root3==(d==1)
        expected=3 if d==1 else 2 if d==2 else 1
        assert json.loads(row["torsion"])[0]==expected
    print("All81 exact torsion groups checked against inert reductions and division polynomials.",flush=True)
    classes=sorted((math.prod(p**e for p,e in zip(PRIMES,es)),es)
                   for es in itertools.product(range(3),repeat=4))
    rows=[];counts={"criterion_pairs":0,"no_sections":0,"cusp_only":0,"ordinary_and_cusp":0}
    special={(1,2):[-1,1,1],(2,1):[1,-1,1],(4,4):[1,1,2]}
    for alpha,ae in classes:
        for beta,be in classes:
            d=math.prod(p**((x+y)%3) for p,x,y in zip(PRIMES,ae,be))
            rank=curves[d]["analytic_rank"]
            row={"alpha":alpha,"beta":beta,"d":d,"analytic_rank":rank,
                 "criterion_applies":int(rank=="0"),"rational_points":"",
                 "ordinary_tripod_values":"","cusp_packets":""}
            if rank=="0":
                counts["criterion_pairs"]+=1
                cusps=[];packets=[]
                if beta==1:
                    cusps.append([0,1,1])
                    packets.append({"cusp":"0","parameter":"t","cube_class":alpha})
                if alpha==1:
                    cusps.append([1,0,1])
                    packets.append({"cusp":"1","parameter":"1-t","cube_class":beta})
                if alpha==beta:
                    cusps.append([1,-1,0])
                    inverse=math.prod(p**((-x)%3) for p,x in zip(PRIMES,ae))
                    packets.append({"cusp":"infinity","parameter":"1/t","cube_class":inverse})
                points=cusps+([special[(alpha,beta)]] if (alpha,beta) in special else [])
                # Nontrivial d=1 twists and all other d=2 twists have a
                # prime at which the three valuations are distinct mod3.
                if d==1 and (alpha,beta)!=(1,1):
                    assert any(sorted((x,y,0))==[0,1,2] for x,y in zip(ae,be))
                    assert not points
                if d==2 and (alpha,beta) not in special:
                    assert any(sorted((x,y,0))==[0,1,2] for x,y in zip(ae,be))
                    assert not points
                vals=[]
                for x,y,z in points:
                    assert alpha*x**3+beta*y**3==z**3
                    if x*y*z:
                        vals.append(str(F(alpha*x**3,z**3)))
                row.update(rational_points=json.dumps(points,separators=(",",":")),
                    ordinary_tripod_values=json.dumps(vals,separators=(",",":")),
                    cusp_packets=json.dumps(packets,separators=(",",":")))
                counts["ordinary_and_cusp" if vals else "cusp_only" if cusps else "no_sections"]+=1
            rows.append(row)
    with (OUT/"a_main_cubic_pairs.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    assert len(rows)==6561 and counts["ordinary_and_cusp"]==3
    print("6561 cubic pairs classified for the stated criterion.",flush=True)
    print(json.dumps(counts,sort_keys=True),flush=True)

if __name__=="__main__":main()
