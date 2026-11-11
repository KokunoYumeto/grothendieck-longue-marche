"""Exact modular matrix and BISITE checks requested in LM2.

The calculation does not identify a finite shadow with a global GT image.
Run: python code/finite_congruence.py
"""
import json,csv
from pathlib import Path
from itertools import product
from math import gcd
from finite_groups import matmul,sl_elements,permutation_group

HERE=Path(__file__).resolve().parent


def closure(gens,n):
    e=(1%n,0,0,1%n);seen={e};todo=[e]
    for a in todo:
        for g in gens:
            b=matmul(a,g,n)
            if b not in seen:seen.add(b);todo.append(b)
    return seen


def run():
    rows=[]
    for n in [2,3,4,5,6,7,8,12,24]:
        units=[i for i in range(n) if gcd(i,n)==1]
        squares=sorted({a*a%n for a in units})
        sl=sl_elements(n);gl=[a for a in product(range(n),repeat=4)
                             if gcd(a[0]*a[3]-a[1]*a[2],n)==1]
        E=(1,1,0,1);F=(1,0,1,1)
        centralizer=[a for a in gl if matmul(a,E,n)==matmul(E,a,n)
                     and matmul(a,F,n)==matmul(F,a,n)]
        assert set(centralizer)=={(u,0,0,u) for u in units}
        zsl=[a for a in centralizer if (a[0]*a[3]-a[1]*a[2])%n==1]
        leg=closure([(1%n,2%n,0,1%n),(1%n,0,-2%n,1%n)],n)
        minus=lambda a:tuple((-v)%n for v in a)
        legproj={min(a,minus(a)) for a in leg}
        # Membership D_u in SL times scalars is checked, independently of formula.
        inner_units=[]
        for u in units:
            d=(u,0,0,1)
            if any(((pow(v,-1,n)**2)*u)%n==1 for v in units):inner_units.append(u)
        assert inner_units==squares
        rows.append(dict(n=n,SL_order=len(sl),GL_order=len(gl),center_SL=len(zsl),
            units=units,squares=squares,arithmetic_outer_order=len(units)//len(squares),
            GL_conjugation_aut_order=len(gl)//len(centralizer),
            SL_inner_order=len(sl)//len(zsl),Legendre_SL_image=len(leg),
            Legendre_PSL_image=len(legproj)))
    G=permutation_group(3)
    x=G.index[(1,0,2)];y=G.index[(2,1,0)]
    comm=G.mul(G.mul(G.mul(x,y),G.inv[x]),G.inv[y])
    ynew=G.mul(y,comm)
    orbit=lambda gens: sorted({G.elements[g][0] for g in G.generated(gens)})
    bis=dict(x=G.elements[x],y=G.elements[y],commutator=G.elements[comm],
             y_commutator=G.elements[ynew],old_generated=len(G.generated([x,y])),
             new_generated=len(G.generated([x,ynew])),old_orbit=orbit([x,y]),new_orbit=orbit([x,ynew]))
    assert ynew==x and len(G.generated([x,y]))==6 and len(G.generated([x,ynew]))==2
    # A relation in the chosen S3 quotient need not survive cusp permutation.
    # x=(12), y=(123): x^2=1, while swap sends it to y^2 !=1.
    a=G.index[(1,0,2)];b=G.index[(1,2,0)]
    descent=dict(x=G.elements[a],y=G.elements[b],x_order=G.orders[a],y_order=G.orders[b],
                 x_squared=G.elements[G.power(a,2)],swap_x_squared=G.elements[G.power(b,2)])
    result=dict(congruence=rows,BISITE=bis,swap_descent_failure=descent)
    (HERE/'finite_congruence.json').write_text(json.dumps(result,indent=2)+'\n')
    with (HERE/'finite_congruence.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    print(json.dumps(result,indent=2))

if __name__=='__main__':run()
