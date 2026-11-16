#!/usr/bin/env python3
"""Evaluate literal retained K3 elements locally; finite-row divisor data remain discovery data."""
from pathlib import Path
from fractions import Fraction as Q
import ast,re,json,math
import sympy as sp
BASE=Path(__file__).resolve().parent
D=649

def vq(x,q):
    x=Q(x)
    if not x:return 10**9
    a,b=abs(x.numerator),x.denominator; v=0
    while a%q==0:a//=q;v+=1
    while b%q==0:b//=q;v-=1
    return v

def kmul(a,b):
    out=[Q(0)]*5
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    for i in (4,3):out[i-3]+=3*out[i]
    return out[:3]

def kpow(a,n):
    out=[Q(1),Q(0),Q(0)]
    while n:
        if n&1:out=kmul(out,a)
        a=kmul(a,a);n//=2
    return out

class Ring:
    def __init__(self,q,prec):
        self.q=q;self.mod=q**prec
        self.s,self.t={11:(2,4),59:(10,41)}[q]
    def add(self,a,b):return tuple((x+y)%self.mod for x,y in zip(a,b))
    def neg(self,a):return tuple(-x%self.mod for x in a)
    def mul(self,a,b):
        x,y=a;u,v=b
        return ((x*u-self.t*y*v)%self.mod,(x*v+y*u+self.s*y*v)%self.mod)
    def inv(self,a):
        x,y=a;norm=(x*x+self.s*x*y+self.t*y*y)%self.mod
        inv=pow(norm,-1,self.mod)
        return ((x+self.s*y)*inv%self.mod,-y*inv%self.mod)
    def power(self,a,n):
        if n<0:return self.power(self.inv(a),-n)
        out=(1,0)
        while n:
            if n&1:out=self.mul(out,a)
            a=self.mul(a,a);n//=2
        return out
    def scalar(self,x):
        x=Q(x);assert x.denominator%self.q
        return (x.numerator*pow(x.denominator,-1,self.mod)%self.mod,0)
    def root(self):
        a=(0,1)
        for _ in range(9):
            residual=self.add(self.power(a,3),(-3%self.mod,0))
            deriv=self.mul((3,0),self.power(a,2))
            a=self.add(a,self.neg(self.mul(residual,self.inv(deriv))))
        assert self.power(a,3)==(3,0)
        return a

local={}
for q in (11,59):
    high=Ring(q,30); low=Ring(q,1)
    root=high.root(); ar=(root[0]%q,root[1]%q)
    omega=low.power(ar,(q*q-1)//3)
    assert omega!=(1,0) and low.power(omega,3)==(1,0)
    local[q]=(high,low,root,omega)

def first_lead(a,q):
    k=min(vq(x,q) for x in a)
    if k==10**9:return None
    rr,ff,root,omega=local[q]
    denom=Q(q)**k
    acc=(0,0)
    for j,x in enumerate(a):
        acc=rr.add(acc,rr.mul(rr.scalar(x/denom),rr.power(root,j)))
    extra=min(vq(x,q) for x in acc)
    assert extra<30
    unit=tuple((x//(q**extra))%q for x in acc)
    assert unit!=(0,0)
    return k+extra,unit

def local_value(coeff,q):
    rr,ff,root,omega=local[q]
    c=[Q(0),Q(0),Q(9*(D//q))]
    cbar=ff.mul(ff.scalar(9*(D//q)),ff.power((root[0]%q,root[1]%q),2))
    terms=[]
    for j in range(9):
        a=[Q(0)]*3
        for r in range(3):
            i=j+9*r
            if i<len(coeff):
                term=kpow(c,r)
                for k in range(3):a[k]+=coeff[i]*(Q(q)**r)*term[k]
        lead=first_lead(a,q)
        if lead:
            val,unit=lead
            weight=9*val+j
            angle=ff.mul(unit,ff.power(cbar,-val))
            terms.append((weight,j,val,angle))
    terms.sort(); assert terms and (len(terms)==1 or terms[0][0]<terms[1][0])
    weight,j,val,angle=terms[0]
    char=ff.power(angle,(q*q-1)//3)
    logs=[e for e in range(3) if ff.power(omega,e)==char]
    assert len(logs)==1
    return {'valuation':weight,'angular_log':logs[0],'angular_component':angle,'least_j':j,'first_field_valuation':val}

raw=(BASE/'two_inert_level3_target_relations_pari_output.txt').read_text()
rows=[]
for line in raw.splitlines():
    ma=re.match(r'REL (\d+) TARGET (\d+) JFACT (\[.*?\]) COEFF (\[.*\])',line)
    if not ma:continue
    target=int(ma[2]);c11=target-5;c59=(4*c11+3+4)%9-4
    div={(2,1):1,(11,1):-2*c11,(11,2):c11,(59,1):-2*c59,(59,2):c59}
    for p,j,e in ast.literal_eval(ma[3]):div[p,j]=div.get((p,j),0)-e
    coeff=[Q(x.strip()) for x in ma[4][1:-1].split(',')]
    qdata={q:local_value(coeff,q) for q in (11,59)}
    for q in (11,59):
        # Identify the two q labels by their retained residue degree (label2 quadratic).
        assert qdata[q]['valuation']==div.get((q,2),0),(ma[1],q,qdata[q],div)
    rows.append({'id':int(ma[1]),'divisor':div,'coefficient':[str(x) for x in coeff],'local':qdata})
assert len(rows)==47
keys=sorted(set().union(*(r['divisor'] for r in rows)))
mat=sp.Matrix([[r['divisor'].get(k,0) for r in rows] for k in keys])
from sympy.matrices.normalforms import smith_normal_decomp
smith,left,right=smith_normal_decomp(mat,domain=sp.ZZ)
assert smith==left*mat*right
rank=mat.rank()
assert right.det() in (-1,1)
basis=[right[:,j] for j in range(rank,len(rows))]
assert mat*right[:,rank:]==sp.zeros(len(keys),len(rows)-rank)
assert (mat*right[:,:rank]).rank()==rank
candidates=[]
for b in basis:
    v=[int(x) for x in b]
    assert mat*sp.Matrix(v)==sp.zeros(len(keys),1)
    chars=[sum(v[i]*rows[i]['local'][q]['angular_log'] for i in range(len(rows)))%3 for q in (11,59)]
    candidates.append({'exponents':v,'characters':chars})
# Build F3 character span incrementally.
span={(0,0)}
for c in candidates:
    span={
        ((x[0]+a*c['characters'][0])%3,(x[1]+a*c['characters'][1])%3) for x in span for a in range(3)}
# Exact relative norms modulo a split physical prime, detecting the global
# first-field pro-three U-coordinate modulo27.  No global unit certification is assumed.
C=3**8*D**3
norm_witness=None
for physical in sp.primerange(100,200000):
    physical=int(physical)
    if (physical-1)%27 or pow(C%physical,(physical-1)//27,physical)!=1:
        continue
    if any(Q(c).denominator%physical==0 for row in rows for c in row['coefficient']):
        continue
    root27=int(sp.nthroot_mod(C%physical,27,physical))
    alpha=pow(root27,18,physical)*pow(243*D*D,-1,physical)%physical
    assert pow(alpha,3,physical)==3
    unit=(alpha*alpha-2)%physical
    omega27=pow(unit,(physical-1)//27,physical)
    if pow(omega27,9,physical)==1:
        continue
    g=int(sp.primitive_root(physical));zeta9=pow(g,(physical-1)//9,physical)
    norm_logs=[]
    for row in rows:
        val=1
        for j in range(9):
            xr=root27*pow(zeta9,j,physical)%physical
            ev=0
            for c in reversed(row['coefficient']):
                c=Q(c)
                ev=(ev*xr+c.numerator*pow(c.denominator,-1,physical))%physical
            val=val*ev%physical
        if val==0:break
        char=pow(val,(physical-1)//27,physical)
        log=[e for e in range(27) if pow(omega27,e,physical)==char]
        assert len(log)==1
        norm_logs.append(log[0])
    if len(norm_logs)!=len(rows):continue
    norm_witness={'p':physical,'root27':root27,'alpha':alpha,'U':unit,
                  'omega27':omega27,'zeta9':zeta9,'generator_norm_logs':norm_logs}
    break
assert norm_witness
for candidate in candidates:
    e=sum(a*b for a,b in zip(candidate['exponents'],norm_logs))%27
    candidate['relative_norm_pro_three_U_coordinate_mod27']=e
    assert e%9==0
    candidate['secondary_difference']=[(v-2*(e//9))%3 for v in candidate['characters']]
differences=sorted({tuple(c['secondary_difference']) for c in candidates})
print('Exact relative-norm witness:',norm_witness['p'],'root',norm_witness['root27'])
print('Secondary differences on the saturated integer kernel:',differences)
result={'literal_local_rows':[{k:v for k,v in r.items() if k!='divisor'} for r in rows],
        'relative_norm_witness':norm_witness,'secondary_differences':differences,
        'retained_divisor_rank':mat.rank(),'retained_rational_kernel_dimension':len(basis),
        'integer_kernel_generators':candidates,'unimodular_right_matrix':[list(map(int,row)) for row in right.tolist()],
        'smith_diagonal':[int(smith[i,i]) for i in range(rank)],'character_span':sorted(span),
        'scope':'Local values are exact. Global unit status for projected candidates still depends on independent certification of retained PARI divisor rows.'}
(BASE/'two_inert_retained_unit_character_search_data.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: exact local leading terms for47 retained literal degree27 elements at11 and59')
print('Finite retained divisor matrix rank',mat.rank(),'rational kernel dimension',len(basis))
print('Character span of the saturated INTEGER kernel:',sorted(span))
print('SCOPE: no full unit/class-group assertion; positive candidates require independent global unit proof')
