#!/usr/bin/env python3
"""Exact independent arithmetic for the degree-18 ninth-root base.

PARI supplies candidate polynomials only.  Rational multiplication checks
the field maps and global units; independent finite residue maps prove the
full pro-three unit saturation and the six tame-character image.
"""
from pathlib import Path
from fractions import Fraction as F
import json,re,itertools
import sympy as S

B=Path(__file__).resolve().parent
txt=(B/'two_inert_zeta9_base_units_discovery_output.txt').read_text()
x=S.Symbol('x')
def parse(s): return S.Poly(S.sympify(s.replace('^','**')),x,domain=S.QQ)
pol=parse(re.search(r'^POLYNOMIAL (.*)$',txt,re.M)[1]);N=pol.degree()
assert N==18 and pol.LC()==1 and pol.is_irreducible
pc=[F(pol.nth(i)) for i in range(N)]
def vec(p):return [F(p.nth(i)) for i in range(N)]
aa=vec(parse(re.search(r'^ALPHA (.*)$',txt,re.M)[1]))
zz=vec(parse(re.search(r'^ZETA9 (.*)$',txt,re.M)[1]))
units=[vec(parse(v))for _,v in re.findall(r'^UNIT (\d+) (.*)$',txt,re.M)]
assert len(units)==9 and units[0]==zz
one=[F(1)]+[F(0)]*(N-1)
def add(a,b):return [u+v for u,v in zip(a,b)]
def scale(a,c):return [c*u for u in a]
def mul(a,b):
    c=[F(0)]*(2*N-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):
            if u and v:c[i+j]+=u*v
    for k in range(2*N-2,N-1,-1):
        if c[k]:
            for j,p in enumerate(pc):
                if p:c[k-N+j]-=c[k]*p
    return c[:N]
def pw(a,n):
    c=one
    while n:
        if n&1:c=mul(c,a)
        a=mul(a,a);n//=2
    return c
assert pw(aa,3)==scale(one,3)
assert add(add(pw(zz,6),pw(zz,3)),one)==[0]*N
assert pw(zz,9)==one and pw(zz,3)!=one
print('PASS: exact alpha and zeta9 maps in the irreducible degree-18 field',flush=True)

# Literal A.191.7: coefficients of 3e_i in alpha^a*zeta9^b,
# ordered by a=0,1,2 and b=0,...,5.  This independent small table
# defines the paper's units without the reduced-generator output.
natural_rows=[
[0,3,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0],
[0,0,0,0,0,0, 0,0,0,0,0,0, 1,0,1,1,-1,1],
[0,0,0,0,0,0, 0,0,0,0,0,0, 0,-1,1,1,-1,0],
[1,0,-1,-1,0,-2, 1,-1,0,0,-1,1, 0,0,0,0,-1,0],
[-1,2,2,-2,1,1, 0,2,0,0,1,0, 0,0,0,0,0,0],
[0,-1,-2,0,-2,-1, 1,1,1,0,0,0, -1,0,0,-1,1,0],
[-2,2,0,-1,1,0, 0,-1,0,-1,0,-1, 0,-1,0,0,-1,0],
[-2,0,-1,-1,0,-2, -1,1,-1,-1,0,-1, -1,0,0,0,0,0],
[1,2,0,2,1,0, 1,-1,1,1,0,1, 0,0,-1,0,0,-1]]
natural_basis=[mul(pw(aa,a),pw(zz,b))for a in range(3)for b in range(6)]
for row,u in zip(natural_rows,units):
    v=[F(0)]*N
    for c,e in zip(row,natural_basis):v=add(v,scale(e,F(c,3)))
    assert v==u
print('PASS: all nine literal small natural-basis unit definitions in A.191.7',flush=True)

charpolys=[]
for j,u in enumerate(units):
    cols=[]
    for i in range(N):
        e=[F(0)]*N;e[i]=1;cols.append(mul(u,e))
    A=S.Matrix([[S.Rational(cols[k][i].numerator,cols[k][i].denominator)
                 for k in range(N)]for i in range(N)])
    cp=A.charpoly().all_coeffs()
    assert all(v.q==1 for v in cp) and abs(cp[-1])==1
    charpolys.append(list(map(int,cp)))
    print('PASS: literal monic integral unit and inverse',j+1,flush=True)

def rank(rows,m):
    a=[[v%3 for v in row]for row in rows];r=0
    for c in range(m):
        k=next((i for i in range(r,len(a))if a[i][c]),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r];iv=pow(a[r][c],-1,3)
        a[r]=[v*iv%3 for v in a[r]]
        for i in range(len(a)):
            if i!=r:
                k=a[i][c];a[i]=[(v-k*w)%3 for v,w in zip(a[i],a[r])]
        r+=1
    return r
def ev(a,t,p):
    c=0
    for v in reversed(a):c=(c*t+v.numerator*pow(v.denominator,-1,p))%p
    return c
rows=[];witnesses=[];all_count=0
for p0 in S.primerange(7,50000):
    p=int(p0)
    if p%9!=1 or any(v.denominator%p==0 for a in [aa,zz]+units for v in a):continue
    ff=S.factor_list(pol,modulus=p)[1]
    roots=[int(-f.nth(0)*pow(int(f.nth(1)), -1,p))%p
           for f,e in ff if f.degree()==1]
    for t in roots:
        a,z=ev(aa,t,p),ev(zz,t,p)
        assert pow(a,3,p)==3%p and pow(z,9,p)==1 and pow(z,3,p)!=1
        om=pow(z,3,p);vals=[ev(u,t,p)for u in units]
        assert all(vals)
        chars=[pow(v,(p-1)//3,p)for v in vals]
        row=[next(k for k in range(3)if pow(om,k,p)==v)for v in chars]
        all_count+=1
        if rank(rows+[row],9)>len(rows):
            rows.append(row);witnesses.append({'p':p,'root':t,'alpha':a,'zeta9':z,
                                             'values':vals,'characters':chars,'row':row})
            print('INDEPENDENT',len(rows),'p=',p,'root=',t,'row=',row,flush=True)
        if len(rows)==9:break
    if len(rows)==9:break
assert len(rows)==9 and int(S.Matrix(rows).det())%3
print('PASS: full nine-dimensional unit quotient modulo cubes; pro-three saturation',flush=True)

def modpoly(a,p):
    return S.Poly.from_list([int(v.numerator*pow(v.denominator,-1,p)%p)
                            for v in reversed(a)],x,modulus=p)
qrows=[];qdata=[]
for q in (11,59):
    fs=S.factor_list(pol,modulus=q)[1]
    assert len(fs)==3 and all(f.degree()==6 and e==1 for f,e in fs)
    for f,e in fs:
        def qp(a,k):
            c=S.Poly(1,x,modulus=q);a=modpoly(a,q).rem(f)
            while k:
                if k&1:c=(c*a).rem(f)
                a=(a*a).rem(f);k//=2
            return c
        om=qp(zz,3);oneq=S.Poly(1,x,modulus=q)
        assert om!=oneq and (om*om*om).rem(f)==oneq
        powers=[oneq,om,(om*om).rem(f)]
        vals=[qp(u,(q**6-1)//3)for u in units]
        row=[next(i for i,v in enumerate(powers)if v==c)for c in vals]
        qrows.append(row)
        qdata.append({'q':q,'factor':list(map(int,f.all_coeffs())),'row':row})
        print('TAME',q,'row=',row,flush=True)
rawrows=[list(map(int,a.split(','))) for a in re.findall(r'^ROW .* \[(.*)\]$',txt,re.M)]
assert sorted(qrows)==sorted(rawrows) and rank(qrows,9)==3
print('PASS: all six exact tame rows agree up to prime order; full norm-character rank three',flush=True)
tex=(B.parent/'sections/two_inert_ninth_root_class_comparison.tex').read_text()
table=tex[tex.index('1&0&3&0'):tex.index(r'\tag{A.191.7}')]
printed=[]
for line in table.splitlines():
    if re.match(r'^[1-9]&',line):
        printed.append([int(v)for v in re.sub(r'\\\\$','',line).split('&')[1:]])
assert printed==natural_rows
assert tex.count(r'\[')==tex.count(r'\]') and '\x0c'not in tex
print('PASS: all 162 printed natural-basis coefficients and balanced display delimiters',flush=True)
out={'polynomial':list(map(int,pol.all_coeffs())),
     'natural_unit_numerators':natural_rows,'natural_common_denominator':3,
     'alpha':[str(v)for v in aa],'zeta9':[str(v)for v in zz],
     'units':[[str(v)for v in u]for u in units], 'unit_character_polynomials':charpolys,
     'saturation_matrix':rows,'saturation_witnesses':witnesses,
     'degree_one_maps_tested':all_count,'tame_rows':qdata,'tame_rank':3,
     'scope':'Exact base field/unit arithmetic; no value of psi_2 or higher norm assertion.'}
(B/'two_inert_zeta9_base_units_certificate_data.json').write_text(json.dumps(out,indent=2)+'\n')
