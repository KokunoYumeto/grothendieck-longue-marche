"""Exact mixed coefficient ring for the harmonic frame phase.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 16 November 2026.
R=(Z/4)[w]/(w^2+w+1). Run: python -I -B check_harmonic_beta_phase.py
"""
import json
N=4
zero=(0,0);one=(1,0);w=(0,1);minus=(-1%N,0)
def add(a,b):return tuple((x+y)%N for x,y in zip(a,b))
def neg(a):return tuple(-x%N for x in a)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    x,y=a;z,t=b
    return ((x*z-y*t)%N,(x*t+y*z-y*t)%N)
def power(a,n):
    r=one
    for _ in range(n):r=mul(r,a)
    return r
c=(2,3)
assert mul(sub(one,w),c)==one
def affmul(a,b):return (add(a[0],mul(a[1],b[0])),mul(a[1],b[1]))
def affpower(a,n):
    r=(zero,one)
    for _ in range(n):r=affmul(r,a)
    return r
def affinv(a):
    z=next((x,y)for x in range(4)for y in range(4)if mul(a[1],(x,y))==one)
    return (neg(mul(z,a[0])),z)
ss=(c,minus);rr=(c,w);tau=affmul(ss,rr)
assert affpower(ss,2)==affpower(rr,3)==(zero,one)
xx=affpower(affinv(tau),2)
yy=affmul(affmul(ss,xx),ss)
assert xx==(zero,w) and yy==((1,0),w)
comm=affmul(affmul(affmul(xx,yy),affinv(xx)),affinv(yy))
assert comm==(sub(w,one),one)
seen={(zero,one)};todo=[(zero,one)]
while todo:
    a=todo.pop()
    for b in (ss,rr):
        d=affmul(a,b)
        if d not in seen:seen.add(d);todo.append(d)
assert len(seen)==96
checks=[]
for rho in range(3):
    q=power(w,rho)
    for eps in (0,1):
        wc=c if eps else zero
        b=neg(mul(q,wc))
        k=sub(mul(sub(one,q),c),add(b,b))
        beta=(b,q);f=(k,one)
        assert affmul(affmul(beta,ss),affinv(beta))==affmul(ss,f)
        V=(zero,q);WW=affmul(affinv(beta),V)
        assert WW==(wc,one)
        beta_value=sub(one,mul(sub(one,w),k))
        expected=mul(q,minus if eps else one)
        assert beta_value==expected
        checks.append({'rho_mod3':rho,'harmonic_bit':eps,'f_translation_mod4':k,'beta_value_mod4':beta_value})
print(json.dumps({'coefficient_ring':'(Z/4)[w]/(w^2+w+1)',
 'c_inverse_of_1_minus_w':c,'image_order':len(seen),
 's':ss,'r':rr,'tau':tau,'x':xx,'y':yy,
 'commutator_translation':comm[0],
 'all_six_phase_cases':checks,
 'identity':'1-(1-w)*k_f = w^rho * (-1)^epsilon_2(W)',
 'interpretation':'A direct integral affine consequence of the actual harmonic frame equation. No gamma multiplication theorem or unidentified section is assumed.'},indent=2))
