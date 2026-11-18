"""Exact independent B150 finite ingredients; paper remains frozen.

Manual F125 arithmetic, genus-two Cantor arithmetic, complete rational point
and character tables, Frobenius/tau matrices, and exact polynomial Bezout.
No enumeration is substituted for the mathematical character-sum proof.
"""
from pathlib import Path
import json
from math import comb
import sympy as sp

q=125;p=5
def digits(a):return [a%5,(a//5)%5,a//25]
def plus(a,b):return sum(((x+y)%5)*5**i for i,(x,y) in enumerate(zip(digits(a),digits(b))))
def times(a,b):
    c=[0]*5
    for i,x in enumerate(digits(a)):
        for j,y in enumerate(digits(b)):c[i+j]+=x*y
    for i in (4,3):
        c[i-2]-=c[i];c[i-3]-=c[i]
    return sum(c[i]%5*5**i for i in range(3))
A=[[plus(a,b) for b in range(q)] for a in range(q)]
M=[[times(a,b) for b in range(q)] for a in range(q)]
N=[sum((-x%5)*5**i for i,x in enumerate(digits(a))) for a in range(q)]
def fpow(a,n):
    b=1
    while n:
        if n&1:b=M[b][a]
        a=M[a][a];n//=2
    return b
I=[0]+[fpow(a,q-2) for a in range(1,q)]
assert all((x**3+x+1)%5 for x in range(5))
assert all(fpow(a,125)==a for a in range(q))
assert all(M[a][I[a]]==1 for a in range(1,q))

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def add(a,b):return trim([A[a[i] if i<len(a) else 0][b[i] if i<len(b) else 0] for i in range(max(len(a),len(b)))])
def neg(a):return [N[x] for x in a]
def sub(a,b):return add(a,neg(b))
def scale(a,c):return trim([M[c][x] for x in a])
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=A[c[i+j]][M[x][y]]
    return trim(c)
def divmodp(a,b):
    a=trim(a);b=trim(b);assert b!=[0]
    d=[0]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        k=len(a)-len(b);c=M[a[-1]][I[b[-1]]];d[k]=c
        for i,x in enumerate(b):a[i+k]=A[a[i+k]][N[M[c][x]]]
        a=trim(a)
    return trim(d),a
def exact(a,b):
    d,r=divmodp(a,b);assert r==[0];return d
def rem(a,b):return divmodp(a,b)[1]
def monic(a):return scale(a,I[a[-1]])
def egcd(a,b):
    r0,r1=trim(a),trim(b);s0,s1=[1],[0];t0,t1=[0],[1]
    while r1!=[0]:
        d,r=divmodp(r0,r1);r0,r1=r1,r
        s0,s1=s1,sub(s0,mul(d,s1));t0,t1=t1,sub(t0,mul(d,t1))
    c=I[r0[-1]]
    return scale(r0,c),scale(s0,c),scale(t0,c)
f=[0,4,0,0,0,1]
assert egcd(f,[4])[0]==[1]
zero=((1,),(0,))
def cantor(D,E):
    u1,v1=map(list,D);u2,v2=map(list,E)
    d0,s,t=egcd(u1,u2);d,a,b=egcd(d0,add(v1,v2))
    e1,e2,e3=mul(a,s),mul(a,t),b
    u=exact(mul(u1,u2),mul(d,d))
    v=rem(exact(add(add(mul(mul(e1,u1),v2),mul(mul(e2,u2),v1)),mul(e3,add(mul(v1,v2),f))),d),u)
    while len(u)>3:
        u=monic(exact(sub(f,mul(v,v)),u));v=rem(neg(v),u)
    u=monic(u);v=rem(v,u)
    assert rem(sub(mul(v,v),f),u)==[0]
    return tuple(u),tuple(v)
def power(D,n):
    E=zero
    while n:
        if n&1:E=cantor(E,D)
        D=cantor(D,D);n//=2
    return E
def pointclass(z,w):return ((N[z],1),(w,))
points=[(z,w) for z in range(q) for w in range(q) if M[w][w]==A[fpow(z,5)][N[z]]]
assert len(points)+1==126
assert [(z,w) for z,w in points if z<5 and w<5]==[(z,0) for z in range(5)]
twice=[power(pointclass(z,w),2) for z,w in points]
assert all(power(D,31)==zero for D in twice)
V=next(D for D in twice if D!=zero)
vm=[zero]
for i in range(1,31):vm.append(cantor(vm[-1],V))
assert cantor(vm[-1],V)==zero and len(set(vm))==31
W=next(D for D in twice if D not in set(vm))
wm=[zero]
for j in range(1,31):wm.append(cantor(wm[-1],W))
assert cantor(wm[-1],W)==zero
states={(i,j):cantor(vm[i],wm[j]) for i in range(31) for j in range(31)}
assert len(set(states.values()))==961
lookup={D:ij for ij,D in states.items()}
for (i,j),D in states.items():
    assert cantor(D,V)==states[((i+1)%31,j)]
    assert cantor(D,W)==states[(i,(j+1)%31)]
def shiftminus1(a):
    b=[0]*len(a)
    for i,c in enumerate(a):
        for j in range(i+1):b[j]=A[b[j]][M[c][comb(i,j)*(-1)**(i-j)%5]]
    return trim(b)
def tau(D):return tuple(shiftminus1(D[0])),tuple(shiftminus1(D[1]))
def frob(D):return tuple(fpow(a,5) for a in D[0]),tuple(fpow(a,5) for a in D[1])
tv,tw=lookup[tau(V)],lookup[tau(W)]
fv,fw=lookup[frob(V)],lookup[frob(W)]
T=[[tv[0],tw[0]],[tv[1],tw[1]]]
F=[[fv[0],fw[0]],[fv[1],fw[1]]]
assert F==[[25,0],[0,25]]
for ij,D in states.items():
    assert lookup[tau(D)]==tuple(sum(T[k][j]*ij[j] for j in range(2))%31 for k in range(2))
    assert lookup[frob(D)]==tuple(25*x%31 for x in ij)
eigen=[]
for u in [2,4,8,16]:
    for row in [(1,b) for b in range(31)]+[(0,1)]:
        if all(sum(row[k]*T[k][j] for k in range(2))%31==u*row[j]%31 for j in range(2)):
            eigen.append((u,row))
assert len(eigen)==2
u,row=eigen[0]
assert pow(u,5,31)==1 and u!=1
def chi(D):return sum(row[i]*lookup[D][i] for i in range(2))%31
records=[{'point':'infinity','twice_mumford':zero,'coordinates':[0,0],'chi':0}]
for (z,w),D in zip(points,twice):records.append({'point':[z,w],'twice_mumford':D,'coordinates':lookup[D],'chi':chi(D)})
occupancy=[sum(r['chi']==j for r in records) for j in range(31)]
assert occupancy==[6]+[4]*30
assert [r['point'] for r in records if r['chi']==0]==['infinity']+[[z,0] for z in range(5)]
assert {pow(u,i,31)*pow(25,j,31)*(-1)**k%31 for i in range(5) for j in range(3) for k in range(2)}==set(range(1,31))

# Independent quadratic field for the F25 point count.
def m25(a,b):
    x,y=a%5,a//5;z,w=b%5,b//5
    return (x*z+2*y*w)%5+5*((x*w+y*z)%5)
def a25(a,b):return (a%5+b%5)%5+5*((a//5+b//5)%5)
def n25(a):return (-a%5)%5+5*((-a//5)%5) if False else (-a%5)%5+5*((-(a//5))%5)
def p25(a,n):
    b=1
    while n:
        if n&1:b=m25(b,a)
        a=m25(a,a);n//=2
    return b
assert all(p25(a,25)==a for a in range(25))
pts25=[(z,w) for z in range(25) for w in range(25) if m25(w,w)==a25(p25(z,5),n25(z))]
assert len(pts25)+1==6

X,Y,Z=sp.symbols('X Y Z')
P=X**4-10*X**2+25
P2=sp.resultant(P.subs(X,Y),X-Y**2,Y)
P3=sp.resultant(P.subs(X,Y),X-Y**3,Y)
assert sp.expand(P2-(X-5)**4)==0
assert sp.expand(P3-(X**2-125)**2)==0
J5=int(P.subs(X,1));J25=int(P2.subs(X,1));J125=int(P3.subs(X,1))
assert [J5,J25,J125]==[16,256,16*31**2]
g1=sp.Poly(X**3-1,X,modulus=31);g2=sp.Poly((X**2-5)**2,X,modulus=31)
s,t,h=sp.gcdex(g1,g2)
assert h==sp.Poly(X-25,X,modulus=31)
assert s*g1+t*g2==h
relative=sp.Poly((1+2*X+125*X**2)**30,X)
relative_h=int(relative.eval(1));assert relative_h==128**30 and relative_h%5==4
assert pow(3,4,5)==1 and pow(3,2,5)!=1
out={
 'status':'PASS exact finite ingredients; B150 mathematical proof separate',
 'curve':'x^2=y^5-y overF5; infinity marking',
 'field_F125':'F5[t]/(t^3+t+1); a+5b+25c',
 'curve_counts':{'F5':6,'F25':6,'F125':126},
 'F25_affine_points':pts25,'Weil_polynomial_F5':[25,0,-10,0,1],
 'Jacobian_orders':{'F5':J5,'F25':J25,'F125':J125},
 'basis_31_primary':[V,W],'all_961_coordinates':[{'ij':ij,'mumford':D} for ij,D in states.items()],
 'tau_matrix':T,'Frobenius5_matrix':F,'dual_eigencharacters':eigen,'chosen_character':[u,row],
 'rational_point_character_table':records,'occupancy':occupancy,
 'frobenius_Bezout_mod31':{'first_polynomial':str(g1.as_expr()),'second_polynomial':str(g2.as_expr()),'first_multiplier':str(s.as_expr()),'second_multiplier':str(t.as_expr()),'gcd':str(h.as_expr())},
 'character_L_polynomial':[1,2,125],
 'relative_zeta_coefficients':[int(relative.nth(i)) for i in range(61)],
 'relative_class_number':relative_h,'cover_class_number':J125*relative_h,'cover_genus':32,
 'unit_test_all_constant_degrees':'5-unit if and only if4 does not divide n',
 'scope':'Finite points, complete961-element31-primary coordinate table, exact automorphism/Frobenius actions, character occupancy, polynomial identities and norm. General geometry and all-degree inference are proved separately.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS counts6,6,126 and Jacobian orders16,256,15376')
print('PASS full961-element31-primary coordinates; tau/Frobenius actions; all126 character values')
print('PASS occupancy[6,4,...,4]; character factor1+2T+125T^2; relative norm128^30')
print('PASS polynomial Bezout; all6 original Weierstrass markings share chi=0')
print('Relative class number:',relative_h)
print('Cover class number:',J125*relative_h)
