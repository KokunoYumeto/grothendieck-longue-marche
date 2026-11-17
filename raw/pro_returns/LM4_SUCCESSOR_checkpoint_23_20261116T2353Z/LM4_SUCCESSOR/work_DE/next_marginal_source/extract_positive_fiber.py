"""Exact F7 fiber words/actions from the freshly certified positive marginal.

This uses an explicit far-basepoint chart, verifies the Artin/Birman
composition convention, and checks the actual four-puncture filling.
It does not assert that the source marginal is the whole filling kernel.
"""
from pathlib import Path
import json,importlib.util,itertools,time
import sympy as S
HERE=Path(__file__).resolve().parent
data=json.loads((HERE/'positive_marginal_words.json').read_text())
spec=importlib.util.spec_from_file_location('engine',HERE.parent/'next_B59_image/braid_engine.py')
E=importlib.util.module_from_spec(spec);spec.loader.exec_module(E)
u=E.u;I=S.I;R=S.Rational
E.N_STRANDS=8;E.rotation=1+R(371,1000)*I;E.EPS=R(1,10**25)
z=[R(a)+R(b)*I for a,b in data['geometry']['coefficient_points']]
base=2+2*I
original=[S.Integer(0),S.Integer(1)]+[S.cancel(((a-base)/(a+base))**2) for a in z]+[S.cancel((z[1]-base)/(z[1]+base))]
endpoint=[S.cancel(a+R(j*j,10**14)/E.rotation) for j,a in enumerate(original)]
far=8+3*I
E.fun=endpoint[:7]+[far+u*(endpoint[7]-far)]
E.exceptional=S.Integer(1);E.cache={}
chart,chart_record=E.segment(0,1)
initial_old=sorted(range(7),key=lambda j:S.re(S.cancel(E.rotation*endpoint[j])))
initial_far=initial_old+[7]
assert S.re(E.rotation*far)>max(S.re(S.cancel(E.rotation*a)) for a in endpoint[:7])
state=initial_far[:]
for a in chart:
    k=abs(a)-1;state[k],state[k+1]=state[k+1],state[k]
assert state==data['initial_order_zero_based']

def red(w):
    out=[]
    for a in w:
        if out and out[-1]==-a:out.pop()
        else:out.append(a)
    return tuple(out)
def inv(w):return tuple(-a for a in w[::-1])
def mul(*ws):return red(itertools.chain.from_iterable(ws))
def sub(w,images):return mul(*(images[a] if a>0 else inv(images[-a]) for a in w))
def artin(w,n=8):
    a=[(j+1,) for j in range(n)]
    for b in w:
        k=abs(b)-1;v,w=a[k:k+2]
        a[k:k+2]=[mul(v,w,inv(v)),v] if b>0 else [w,mul(inv(w),v,w)]
    return tuple(a)
def delete_last(w):
    state=list(range(8));out=[]
    for a in w:
        k=abs(a)-1
        if state[k]!=7 and state[k+1]!=7:
            j=sum(x!=7 for x in state[:k])+1
            out.append(j if a>0 else -j)
        state[k],state[k+1]=state[k+1],state[k]
    assert state==list(range(8))
    return red(out)
def conjugator(A):
    v=A[-1];i=0
    while len(v)-2*i>1:
        assert v[i]==-v[-1-i];i+=1
    assert v[i:i+1]==(8,)
    return red(a for a in v[:i] if abs(a)!=8)
def push(w):return conjugator(artin(w))
def action(w):
    A=artin(w);q=conjugator(A)
    return {i:mul(inv(q),red(a for a in A[i-1] if abs(a)!=8),q) for i in range(1,8)}
def cyclic_core(w):
    i=0
    while len(w)-2*i>1 and w[i]==-w[-1-i]:i+=1
    return w[i:len(w)-i] if i else w

chart=tuple(chart)
source=[mul(chart,tuple(row['word']),inv(chart)) for row in data['loops']]
print('Exact chart puts positive point last; old label order:',initial_old,flush=True)
print('Chart braid:',chart,flush=True)

# Concrete Artin/Birman conventions, not an assumed path orientation.
def A_i(i):
    return tuple(range(7,i,-1))+(i,i)+tuple(range(-i-1,-8,-1))
standards=[A_i(i) for i in range(1,8)]
for w in standards:
    assert artin(delete_last(w),7)==tuple((i,) for i in range(1,8))
p,q=push(standards[0]),push(standards[1])
assert push(mul(standards[0],standards[1]))==mul(q,p)
assert push(mul(standards[0],standards[1]))!=mul(p,q)
print('Last-conjugator extraction is antihomomorphic; its inverse is the fiber homomorphism: PASS',flush=True)

actions={};inverse_actions={};fiber={};started=time.time()
for k,w in enumerate(source):
    if k<11:
        A=action(w);Ai=action(inv(w))
        for i in range(1,8):
            assert sub(A[i],Ai)==(i,) and sub(Ai[i],A)==(i,)
            assert cyclic_core(A[i])==(i,)
        # Verify the conjugation recipe on a literal last-strand pure braid.
        test=standards[k%7]
        assert push(mul(w,test,inv(w)))==sub(push(test),A)
        actions[k]=A;inverse_actions[k]=Ai
        print('Old action',k,'total_length',sum(map(len,A.values())),
              'max_length',max(map(len,A.values())),'inverse/conjugation PASS',flush=True)
    else:
        assert artin(delete_last(w),7)==tuple((i,) for i in range(1,8))
        q=inv(push(w));core=cyclic_core(q)
        assert len(core)==1
        fiber[k]=q
        print('New fiber',k,'length',len(q),'peripheral_core',core,flush=True)

# The actual retained old labels are 0,1,v_zeta, i.e. indices0,1,3.
keep={i+1 for i,j in enumerate(initial_old) if j in (0,1,3)}
killed=set(range(1,8))-keep
assert len(keep)==3 and len(killed)==4
filling={i:((sorted(keep).index(i)+1,) if i in keep else ()) for i in range(1,8)}
assert all(not sub(w,filling) for w in fiber.values())
assert {abs(cyclic_core(w)[0]) for w in fiber.values()}==killed
for A in list(actions.values())+list(inverse_actions.values()):
    assert all(not sub(A[i],filling) for i in killed)
    assert all(cyclic_core(sub(A[i],filling))==(sorted(keep).index(i)+1,) for i in keep)
print('Exact retained labels/F7-to-F3 filling:',sorted(keep),'killed:',sorted(killed),flush=True)
print('All eight fiber words and all eleven actions respect this actual filling: PASS',flush=True)

out={
 'description':__doc__,'chart':chart,'chart_record':chart_record,
 'initial_far_old_labels_zero_based':initial_old,
 'source_braids':source,'old_actions':actions,'old_inverse_actions':inverse_actions,
 'new_fiber_words':fiber,'retained_basis':sorted(keep),'killed_basis':sorted(killed),
 'filling':filling,'standard_pure_generators':standards,
 'standard_push_words':[push(w) for w in standards],
 'convention':'push is anti; inverse(push) is the fiber homomorphism; displayed actions act on either convention',
 'source_image':'closed subgroup generated by the eleven-action orbit of the eight new fiber words',
 'not_proved':['marginal source equals the full filling kernel','actual K is trivial']
}
(HERE/'positive_fiber_data.json').write_text(json.dumps(out,indent=2)+'\n')
print('COMPLETE exact F7 data; elapsed',round(time.time()-started,2),flush=True)
