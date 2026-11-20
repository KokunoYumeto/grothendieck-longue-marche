"""Exact local checks of natural conjugator transport and the stated finite action.
No OCR, external sources, recognition, or TeX compilation.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
from functools import reduce
import json

def red(w):
    s=[]
    for x in w:
        if s and s[-1]==-x:s.pop()
        else:s.append(x)
    return tuple(s)
def inv(w):return tuple(-x for x in w[::-1])
def cat(*ws):return red(sum((tuple(w) for w in ws),()))
def sub(w,imgs):return cat(*(imgs[x] if x>0 else inv(imgs[-x]) for x in w))
a=(1,);b=(2,);c=(-1,-2)
r={1:b,2:c};loops=[a,b,c]
assert all(sub(loops[i],r)==loops[(i+1)%3] for i in range(3))
# u=int(a), with all three g_i=a and p=1. Natural rho transport
# yields int(b), with all three transported labels b, not a.
natural=[sub(a,r)]*3
literal_shift=[a]*3
assert natural!=literal_shift

# Q(P), where P^2-P+1=0 and conjugation sends P to 1-P.
def q(x,y=0):return (F(x),F(y))
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
def qi(x):
    n=x[0]*x[0]+x[0]*x[1]+x[1]*x[1]
    assert n
    return ((x[0]+x[1])/n,-x[1]/n)
def bar(x):return (x[0]+x[1],-x[1])
def scale(k,x):return (k*x[0],k*x[1])
def act(M,x,anti=0):
    if anti:x=bar(x)
    a,b,c,d=M
    return mul(add(scale(a,x),q(b)),qi(add(scale(c,x),q(d))))
I=(1,0,0,1);R=(0,1,-1,1);R2=(-1,1,-1,0)
S0=(1,0,1,-1);S1=(0,1,1,0);Si=(-1,1,0,1)
mats={'1':I,'rho':R,'rho^2':R2,'sigma0':S0,'sigma1':S1,'sigmaInfinity':Si}
P=q(0,1);Pb=bar(P);two=q(2)
fixP=[];toPb=[];fixTwo=[]
for name,M in mats.items():
    for e in (0,1):
        label=name+(' tau' if e else '')
        z=act(M,P,e)
        assert z in [P,Pb]
        (fixP if z==P else toPb).append(label)
        if act(M,two,e)==two:fixTwo.append(label)
assert len(fixP)==6 and len(toPb)==6
assert set(fixP)=={'1','rho','rho^2','sigma0 tau','sigma1 tau','sigmaInfinity tau'}
assert set(fixTwo)=={'1','1 tau','sigma0','sigma0 tau'}
assert act(R,P)==P and act(R,Pb)==Pb
assert act(R,P,1)==Pb and act(R,Pb,1)==P
assert act(S0,two)==two
out={'scope':'Natural rho transport only on scan026, not an identification of an unspecified lift. Exact evaluation of the twelve specified Mobius/anti-Mobius elements on scan027; no theorem about all splitting classes.',
     'scan026':{'rho_cycles_loop_words':True,'inner_a_natural_transported_labels':natural,'literal_i_plus_1_labels':literal_shift,'counterexample_under_natural_lift':True},
     'scan027':{'field':'Q(P), P^2-P+1=0; bar(P)=1-P','stabilizer_P':fixP,'elements_sending_P_to_barP':toPb,'stabilizer_2':fixTwo,'rho_tau_swaps_roots':True}}
dest=Path(__file__).resolve().parents[1]/'reader_reports/145_scans026_027_algebra_check.json'
dest.write_text(json.dumps(out,indent=2))
print(json.dumps(out))
