#!/usr/bin/env python3
"""Exploratory complete theta-n coordinate tests for ordinary F4 genus-two models.

For h=A+B(y+beta), deg A,B <=(n-3)/2, vanishing of the high jets
is the rectangular Hankel rank condition. All maximal minors are
checked unless their gcd is already a unit away from 0,1.
This does not itself promote a new manuscript claim.
"""
from pathlib import Path
from itertools import combinations_with_replacement
import json,time
from A_theta_three_power_experiment import (
    ZERO,ONE,X,add,mul,scale,power,determinant,gcdp,divmodp,
    exactdiv,deg
)
def strip_branch_factors(G):
    for F in [X,add(X,ONE)]:
        while G!=ZERO and divmodp(G,F)[1]==ZERO:G=exactdiv(G,F)
    return G

def test(a,b,c,n):
    d=(n-3)//2
    xp1=add(X,ONE);D=mul(X,xp1)
    P={}
    for k in range(1,n):
        v=add(scale(mul(power(X,k-1),power(xp1,2*k)),b),
              scale(mul(power(X,2*k),power(xp1,k-1)),c))
        if k==1:v=add(v,scale(power(D,2),a))
        if k%2==0:v=add(v,mul(P[k//2],P[k//2]))
        P[k]=v
    matrix=[[P[i-j] for j in range(d+1)] for i in range(d+1,n)]
    order=[0,d+1]+list(range(1,d+1))
    G=ZERO;records=[]
    for omitted in order:
        det=determinant([row for i,row in enumerate(matrix) if i!=omitted])
        G=gcdp(G,det)
        residual=strip_branch_factors(G)
        records.append({"omit":omitted,"minor_degree":deg(det),
                        "gcd_degree":deg(G),"residual_degree":deg(residual)})
        if residual==ONE:break
    assert G!=ZERO
    return {"n":n,"theta_n_exists":residual!=ONE,
            "coordinate_polynomial_degree":deg(residual),
            "coordinate_polynomial_masks":[str(k) for k in residual],
            "all_minors_used_or_unit_gcd":True,"minor_records":records}
def main():
    start=time.time();rows=[]
    for abc in combinations_with_replacement([1,2,3],3):
        tests=[test(*abc,n) for n in [3,5,7,9,13]]
        good=[r["n"] for r in tests if r["theta_n_exists"]]
        row={"coefficients":list(abc),"successful_orders":good,"tests":tests}
        rows.append(row)
        print(json.dumps({"coefficients":abc,"successful_orders":good,
                          "degrees":[r["coordinate_polynomial_degree"] for r in tests]}),
              flush=True)
    out={"status":"EXACT exploratory scan complete",
         "field":"F4=F2[alpha]/(alpha^2+alpha+1), encoding1,2=alpha,3=alpha^2",
         "orders":[3,5,7,9,13],"curves":rows,
         "remaining_without_these_orders":[r["coefficients"] for r in rows if not r["successful_orders"]],
         "runtime_seconds":time.time()-start,
         "scope":"Maximal-minor criterion is to be proved/reviewed before promotion; computes geometric theta n-torsion coordinates, not only rational points."}
    Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k!="curves"},indent=2))
if __name__=="__main__":main()

