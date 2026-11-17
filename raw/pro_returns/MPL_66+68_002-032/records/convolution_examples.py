"""Small post-freeze mathematical checks, not transcription/OCR.
The examples are advisory research checks, not novelty or general proofs.
"""
from collections import Counter
from itertools import permutations
import json
from pathlib import Path

def profile(v): return sorted(v.values(),reverse=True)
def conv(A,B,mul):
    c=Counter()
    for a,va in A.items():
        for b,vb in B.items(): c[mul(a,b)]+=va*vb
    return c
def ind(A): return Counter({a:1 for a in A})
def comp(p,q): return tuple(p[q[i]] for i in range(3))
e=(0,1,2); h=(1,0,2); s=(1,2,0)
H={e,h}; B={comp(a,s) for a in H}
ab=conv(ind(H),ind(B),comp); ba=conv(ind(B),ind(H),comp)
assert profile(ab)==[2,2] and profile(ba)==[1,1,1,1]
out={'S3_noncommutative':{'H':[list(x) for x in sorted(H)],'s':s,'B_Hs':[list(x) for x in sorted(B)],'AB_profile':profile(ab),'BA_profile':profile(ba),'max_rearrangement_pairing':2}}
A={0,1,3,4}; I=set(range(4)); add=lambda a,b:a+b
AA=conv(ind(A),ind(A),add); II=conv(ind(I),ind(I),add)
assert sum(profile(AA)[:2])==6 and sum(profile(II)[:2])==7
out['Hua_peak_not_good']={'A':sorted(A),'I':sorted(I),'AA_profile':profile(AA),'II_profile':profile(II),'top_two_AA':6,'top_two_II':7,'attribution':'Hua modernised reading of cote68, Couples tassés et condition K; independently recomputed here.'}
add4=lambda a,b:(a+b)%4
E={0,1,2}; ee=conv(ind(E),ind(E),add4)
assert ee==Counter({0:2,1:2,2:3,3:2})
out['order_four_scratch_profile']={'group':'Z/4','V1':[0,2],'x':1,'u':2,'E':sorted(E),'convolution':dict(ee),'profile':profile(ee)}
# Check the literal E/F positive-cone patterns in a few finite models.
models=[]
def cone_coeff(v,chain):
    last=set(); vals=[]
    for S in chain:
        layer=S-last
        layer_values={v.get(x,0) for x in layer}
        if len(layer_values)!=1: return None
        vals.append(next(iter(layer_values))); last=S
    coeff=[vals[i]-(vals[i+1] if i+1<len(vals) else 0) for i in range(len(vals))]
    return coeff if min(coeff)>=0 else None
for N in [3,5,7,9,11]:
    m=(N-1)//2; G=set(range(N)); E=[{x%N for x in range(-i,i+1)} for i in range(m+1)]
    F=[{x%N for x in range(m-j,m+2+j)} for j in range(m)]+[G]
    count=0
    for i in range(m+1):
        for j in range(m+1):
            for a,b,target in [(E[i],E[j],E),(F[i],F[j],E),(E[i],F[j],F)]:
                v=conv(ind(a),ind(b),lambda x,y:(x+y)%N)
                assert cone_coeff(v,target) is not None,(N,i,j,a,b)
                count+=1
    models.append({'N':N,'products_checked':count})
out['finite_EF_checks']=models
# Dropping K: powers of delta_0+1_G on Z/3 and translations form a
# convolution/translation-stable peak-extremal family with only singleton indicators.
checks=[]
for n in range(5):
    qn=(4**n-1)//3; fn=Counter({0:1+qn,1:qn,2:qn})
    for m in range(5):
        qm=(4**m-1)//3; fm=Counter({0:1+qm,1:qm,2:qm})
        result=conv(fn,fm,lambda x,y:(x+y)%3)
        q=(4**(n+m)-1)//3
        assert result==Counter({0:1+q,1:q,2:q})
        dot=sum(x*y for x,y in zip(profile(fn),profile(fm)))
        assert max(result.values())==dot
        checks.append([n,m])
out['no_K_level_set_counterexample']={'G':'Z/3','f':[2,1,1],'formula':'f^n=delta_0+((4^n-1)/3)1_G; S consists of translations for n>=0','S0':'singleton indicators only','missing_level':'E_1(f)=G','checks':checks,'qualification':'Demonstrates missing cardinality hypothesis matters; not a counterexample with K.'}
out['missing_first_majorization_test']={'f_prime':[2,0],'f':[1,1],'sums_from_index_zero_through_n_ge_1':'all equal to 2','first_entry_inequality':'2 > 1','qualification':'Only applies if the N^* reading is accepted; the frozen reading also allows N^0.'}
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k not in {'no_K_level_set_counterexample'}},indent=2))
print('No-K family: 25 finite product/peak checks passed; algebraic formula stated separately.')
