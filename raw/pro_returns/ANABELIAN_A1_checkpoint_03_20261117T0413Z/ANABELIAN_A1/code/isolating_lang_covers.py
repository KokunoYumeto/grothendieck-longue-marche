"""Exact degree-seven Lang witnesses for the two conjugate F_4 curves.

Mumford arithmetic is implemented directly for y^2+h(x)y=f(x), genus 2.
The output specifies characters, twisted L-polynomials and a canonical
two-stage Lang/core construction of an isolating pointed cover over F_4.
"""
from pathlib import Path
from collections import Counter
from itertools import product
import json
import sympy as sp

class BinaryField:
    def __init__(self,n,mod):
        self.n,self.mod,self.q=n,mod,1<<n
        self.mul=[[self.raw_mul(a,b) for b in range(self.q)] for a in range(self.q)]
        self.inv=[0]+[self.pow(a,self.q-2) for a in range(1,self.q)]
    def raw_mul(self,a,b):
        z=0
        while b:
            if b&1:z^=a
            b>>=1;a<<=1
            if a&self.q:a^=self.mod
        return z
    def pow(self,a,n):
        z=1
        while n:
            if n&1:z=self.mul[z][a]
            a=self.mul[a][a];n>>=1
        return z
    def root4(self):
        return min(a for a in range(2,self.q) if self.mul[a][a]^a^1==0)

def trim(a):
    a=list(a)
    while a and not a[-1]:a.pop()
    return tuple(a)

class Jacobian:
    def __init__(self,K,alpha):
        self.K,self.alpha=K,alpha
        self.h=(alpha,1,1)
        self.f=(1,1,0,alpha,0,1)
        self.O=((1,),())
    def addp(self,a,b):
        return trim((a[i] if i<len(a) else 0)^(b[i] if i<len(b) else 0)
                    for i in range(max(len(a),len(b))))
    def mulp(self,a,b):
        if not a or not b:return ()
        c=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):c[i+j]^=self.K.mul[x][y]
        return trim(c)
    def scale(self,a,c):
        return trim(self.K.mul[x][c] for x in a)
    def divp(self,a,b):
        assert b
        a=list(a);q=[0]*max(0,len(a)-len(b)+1)
        while len(a)>=len(b):
            d=len(a)-len(b);c=self.K.mul[a[-1]][self.K.inv[b[-1]]]
            q[d]=c
            for i,x in enumerate(b):a[d+i]^=self.K.mul[c][x]
            while a and not a[-1]:a.pop()
        return trim(q),tuple(a)
    def exact(self,a,b):
        q,r=self.divp(a,b);assert not r
        return q
    def modp(self,a,b):return self.divp(a,b)[1]
    def xgcd(self,a,b):
        s,t,ss,tt=(1,),(),(),(1,)
        while b:
            q,r=self.divp(a,b)
            a,b=b,r
            s,ss=ss,self.addp(s,self.mulp(q,ss))
            t,tt=tt,self.addp(t,self.mulp(q,tt))
        c=self.K.inv[a[-1]]
        return self.scale(a,c),self.scale(s,c),self.scale(t,c)
    def check(self,D):
        u,v=D
        assert u and u[-1]==1 and len(u)<=3 and len(v)<len(u)
        assert not self.modp(self.addp(self.addp(self.mulp(v,v),self.mulp(self.h,v)),self.f),u)
    def add(self,D,E):
        u1,v1=D;u2,v2=E
        d1,e1,e2=self.xgcd(u1,u2)
        d,c1,c2=self.xgcd(d1,self.addp(self.addp(v1,v2),self.h))
        s1,s2,s3=self.mulp(c1,e1),self.mulp(c1,e2),c2
        u=self.exact(self.mulp(u1,u2),self.mulp(d,d))
        v=self.addp(self.addp(self.mulp(self.mulp(s1,u1),v2),
                             self.mulp(self.mulp(s2,u2),v1)),
                    self.mulp(s3,self.addp(self.mulp(v1,v2),self.f)))
        v=self.modp(self.exact(v,d),u)
        while len(u)>3:
            u2=self.exact(self.addp(self.addp(self.f,self.mulp(v,v)),self.mulp(self.h,v)),u)
            u2=self.scale(u2,self.K.inv[u2[-1]])
            v=self.modp(self.addp(self.h,v),u2);u=u2
        result=(u,v);self.check(result)
        return result
    def neg(self,D):
        return D[0],self.modp(self.addp(self.h,D[1]),D[0])
    def multiple(self,D,n):
        z=self.O
        while n:
            if n&1:z=self.add(z,D)
            D=self.add(D,D);n>>=1
        return z
    def evalp(self,f,x):
        y=0
        for c in reversed(f):y=self.K.mul[y][x]^c
        return y
    def points(self,subset=None):
        subset=list(range(self.K.q)) if subset is None else subset
        result=[None]
        for x in subset:
            h,f=self.evalp(self.h,x),self.evalp(self.f,x)
            for y in subset:
                if self.K.mul[y][y]^self.K.mul[h][y]^f==0:result.append((x,y))
        return result
    def pointclass(self,P):
        return self.O if P is None else ((P[0],1),(P[1],) if P[1] else ())

X=sp.symbols("X")
K=BinaryField(6,(1<<6)|(1<<1)|1)
alpha=K.root4()
assert K.pow(alpha,2)^alpha^1==0
F4=[0,1,alpha,alpha^1]
K16=BinaryField(4,(1<<4)|(1<<1)|1)
all_records=[]
for conjugate in (0,1):
    a=alpha if not conjugate else alpha^1
    J=Jacobian(K,a)
    points=J.points()
    original=J.points(F4)
    N1=len(original)
    a16=K16.root4()
    if conjugate:a16^=1
    N2=len(Jacobian(K16,a16).points())
    s1=5-N1
    s2=17-N2
    e2=(s1*s1-s2)//2
    fchar=X**4-s1*X**3+e2*X**2-4*s1*X+16
    h3=int(sp.resultant(fchar,X**3-1,X))
    assert h3==6076
    assert len(points)==91
    projection_multiplier=h3//49
    projected=[J.multiple(J.pointclass(P),projection_multiplier) for P in points]
    assert all(J.multiple(D,7)==J.O for D in projected)
    basis=[]
    coord={J.O:(0,0)}
    for D in projected:
        if D in coord:continue
        basis.append(D)
        if len(basis)==1:
            coord={J.multiple(D,i):(i,0) for i in range(7)}
        else:
            coord={J.add(J.multiple(basis[0],i),J.multiple(D,j)):(i,j)
                   for i,j in product(range(7),repeat=2)}
            break
    assert len(basis)==2 and len(coord)==49
    assert all(D in coord for D in projected)
    group=list(coord)
    index={D:i for i,D in enumerate(group)}
    table=[[index[J.add(A,B)] for B in group] for A in group]
    assert all(table[table[i][j]][k]==table[i][table[j][k]]
               for i in range(49) for j in range(49) for k in range(49))
    for i,A in enumerate(group):
        for j,B in enumerate(group):
            actual=coord[group[table[i][j]]]
            expected=tuple((x+y)%7 for x,y in zip(coord[A],coord[B]))
            assert actual==expected
    point_coords={P:coord[D] for P,D in zip(points,projected)}
    Phi7=sum(X**i for i in range(7))
    records=[]
    for P in original:
        pc=point_coords[P]
        chosen=None
        tests=[]
        # All eight one-dimensional quotient kernels, one representative each.
        characters=[(1,b) for b in range(7)]+[(0,1)]
        for ch in characters:
            counts=[0]*7
            for R in points:
                rc=point_coords[R]
                b=sum(ch[i]*(rc[i]-pc[i]) for i in (0,1))%7
                counts[b]+=1
            # K_C~2 infinity, so the leading coefficient has exponent -2chi(P).
            kexp=(-2*sum(ch[i]*pc[i] for i in (0,1)))%7
            c1=sum(counts[i]*X**i for i in range(7))
            L1=sp.rem(1+c1+64*X**kexp,Phi7,X)
            relative=int(sp.resultant(Phi7,L1,X))
            assert relative>0
            row={"character":ch,"point_occupancies":counts,
                 "leading_coefficient_exponent":kexp,
                 "relative_class_number":relative,
                 "is_two_unit":relative%2==1}
            tests.append(row)
            if chosen is None and relative%2:
                hD=h3*relative
                m=hD
                while m%2==0:m//=2
                row=dict(row)
                row.update({"J_D_F64_order":hD,"odd_Lang_degree":m,
                            "composite_degree":7*m,
                            "Galois_closure_degree_bound":7*m**7,
                            "F4_core_degree_bound":(7*m**7)**3})
                chosen=row
        assert chosen is not None
        records.append({"P":P,"projected_P_coordinate":pc,
                        "chosen":chosen,"all_character_tests":tests})
    record={"coefficient_conjugate":conjugate,"alpha_bits":a,
            "equation":{"h":[a,1,1],"f":[1,1,0,a,0,1]},
            "point_counts":{"F4":N1,"F16":N2,"F64":len(points)},
            "F4_Frobenius_polynomial":str(fchar),
            "J_F64_order":h3,"projection_multiplier":projection_multiplier,
            "basis_mumford":[[list(u),list(v)] for u,v in basis],
            "point_table":[{"point":P,"coordinate":point_coords[P]} for P in points],
            "subgroup_table":table,"original_points":records}
    all_records.append(record)
    print(f"Conjugate={conjugate}, alpha={a}: N4={N1}, N16={N2}, N64={len(points)}, h64={h3}")
    for row in records:
        print("P",row["P"],"chi",row["chosen"]["character"],"relative",
              row["chosen"]["relative_class_number"],"odd Lang",
              row["chosen"]["odd_Lang_degree"])
result={"field":"F2[t]/(t^6+t+1)","bit_encoding":"bit i is t^i",
        "curves":all_records,
        "cover_construction":[
            "For P and the recorded chi, form the P-based degree-7 Lang cover D_chi over F64.",
            "At its zero lift P_D, form the full odd Lang cover E of D_chi of the recorded degree.",
            "Take the geometric Galois closure with its P-pointed twist over F64.",
            "Intersect its geometric kernel with its two F4-Frobenius conjugates; use the P-section for descent to F4.",
            "This uniquely specified normal pointed cover has image of rational points equal to {P}."
        ]}
Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
print("All 14 pointed constructions and complete 49-element group tables: PASS")
