"""Exact new counterexample to injectivity of the actual full cyclic map.

This reads original common-base eleven-strand braids and imports no search
or discovery code.  It verifies the nontrivial finite source witness,
all six Artin identities, the boundary-action derivation, and an infinite
image witness.  It does not identify the completed kernel with the closure
of the discrete kernel and does not construct an element of K.
"""
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent

def red(w):
    result=[]
    for a in w:
        if result and result[-1]==-a: result.pop()
        else: result.append(a)
    return tuple(result)
def inv(w):return tuple(-a for a in reversed(w))
def mul(*ws):return red(a for w in ws for a in w)
def sub(w,ims):return mul(*(ims[a] if a>0 else inv(ims[-a]) for a in w))
def comm(a,b):return mul(a,b,inv(a),inv(b))
def artin(w,n):
    ims=[(i,) for i in range(1,n+1)]
    for a in w:
        k=abs(a)-1;x,y=ims[k:k+2]
        ims[k:k+2]=[mul(x,y,inv(x)),x] if a>0 else [y,mul(inv(y),x,y)]
    return tuple(ims)
def delete(w,initial,retained):
    labels=list(initial);result=[]
    for a in w:
        k=abs(a)-1
        if labels[k] in retained and labels[k+1] in retained:
            c=1+sum(x in retained for x in labels[:k])
            result.append(c if a>0 else -c)
        labels[k],labels[k+1]=labels[k+1],labels[k]
    assert labels==initial
    return red(result)
def extract(A):
    v=list(A[-1]);q=[]
    while len(v)>1:
        assert v[0]==-v[-1]
        q.append(v.pop(0));v.pop()
    assert v==[6]
    return red(x for x in q if abs(x)!=6)

data=json.loads((HERE.parent/'next_B59_image/common_base_braid_words.json').read_text())
initial=data['initial_order_labels'];keep={1,4,5,6,10,11}
order=[x for x in initial if x in keep]
assert order==[4,11,5,1,10,6]
braids={int(i)+1:delete(b,initial,keep) for i,b in data['C5'].items()}
g=(-6,-1,-3)
h=(-6,2,6)
k=mul(inv(h),g)
assert k==(-6,-2,-1,-3)
w=comm(k,(2,))
assert w==(-6,-2,-1,-3,2,3,1,2,6,-2)
assert red(w)==w and len(w)==10
b=sub(w,braids)
A=artin(b,6)
assert len(b)==132 and A==tuple((i,) for i in range(1,7))
print('Nonempty freely reduced source word:',w)
print('Original 11-strand words -> actual full PB6 substitution length132: PASS')
print('All six faithful Artin images:',A,'; identity: PASS')

# Independent finite source witness; tuple permutations act on {1,2,3}.
def compose(p,q):return tuple(p[q[i]-1] for i in range(3))
def pinv(p):return tuple(p.index(i)+1 for i in range(1,4))
perms={i:(1,2,3) for i in range(1,7)}
perms[2]=(2,1,3);perms[6]=(1,3,2)
value=(1,2,3)
for a in w:value=compose(value,perms[a] if a>0 else pinv(perms[-a]))
assert value!=(1,2,3)
print('Finite S3 witness f1=(12), f5=(23), others1; source image:',value,': PASS')

# Structural explanation in the actual last-strand Birman fiber.
tau=(3,4,5)
last={i:mul(inv(tau),b,tau) for i,b in braids.items()}
B=(1,2,3,4,5);q=(3,5)
quot={i:(i,) for i in range(1,5)};quot[5]=(-4,-3,-2,-1)
to_B_basis={i:(i,) for i in range(1,5)}
to_B_basis[5]=(-4,-3,-2,-1,5) # final letter5 here is the new generator B
def source_action(s):
    A=artin(sub(s,last),6);Q=extract(A)
    alpha={i:mul(inv(Q),red(x for x in A[i-1] if abs(x)!=6),Q) for i in range(1,6)}
    normalized={i:mul(inv(q),sub(mul(q,(i,),inv(q)),alpha),q) for i in range(1,6)}
    R=mul(inv(q),sub(q,alpha),inv(Q))
    assert sub(B,normalized)==mul(R,B,inv(R))
    return A,Q,normalized,R
_,Q1,a1,R1=source_action((2,))
assert Q1==mul(q,inv(B),inv(q))
assert all(a1[i]==mul(B,(i,),inv(B)) for i in range(1,6))
_,Qg,ag,Rg=source_action(g)
_,Qs,as_,Rs=source_action((-6,))
_,Qh,ah,Rh=source_action(h)
actual_h=mul(inv(q),inv(Qh),q)
assert Rs==mul(inv(B),(1,),B)
assert Rg==mul(Rs,B,inv(Rs))
assert actual_h==Rg
_,Qk,ak,Rk=source_action(k)
assert sub(B,ak)==B
assert not sub(Rg,quot)
print('Normalized f1 is B; R_(f5^-1)=B^-1 x1 B: PASS')
print('R_g=B^-1 x1 B x1^-1 B equals the actual fiber image of h=f5^-1 f1 f5: PASS')
print('Therefore k=h^-1 g fixes B literally, explaining the full commutator identity: PASS')

# A linking difference descends through the central full twist and proves
# the image in the seven-punctured sphere group has infinite order.
labels=list(order);crossings={}
for a in braids[6]:
    i=abs(a)-1;pair=tuple(sorted((labels[i],labels[i+1])))
    crossings[pair]=crossings.get(pair,0)+(1 if a>0 else -1)
    labels[i],labels[i+1]=labels[i+1],labels[i]
assert labels==order and all(n%2==0 for n in crossings.values())
linking={pair:n//2 for pair,n in crossings.items()}
assert linking.get((4,6),0)==0
pair=next(pair for pair,n in sorted(linking.items()) if n)
assert linking[pair]!=0
print('Infinite-image witness f5: linking',pair,'=',linking[pair],'; fixed linking(4,6)=0: PASS')
print('PASS full theta5 is not injective; nontrivial source word also survives the full completion')
(HERE/'full_theta5_noninjection_certificate.json').write_text(json.dumps({
    'provenance':'Fresh verification directly from original common-base eleven-strand words',
    'finite_order':order,'six_source_braids':braids,'g':g,'h':h,'k':k,
    'kernel_word':w,'actual_braid':b,'Artin_images':A,'S3_assignments':perms,'S3_value':value,
    'last_strand_transport':tau,'normalizing_conjugator':q,'fiber_boundary':B,
    'R_f5_inverse':Rs,'R_g':Rg,'fiber_image_h':actual_h,
    'R_g_in_basis_x1_x2_x3_x4_B':sub(Rg,to_B_basis),
    'normalized_action_k':ak,'linking_f5':{str(p):n for p,n in linking.items()},
    'infinite_linking_witness':{'pair':pair,'value':linking[pair],'fixed_pair':[4,6]},
    'not_claimed':['complete kernel presentation','completed kernel equals closure of discrete kernel','nontrivial element of K']
},indent=2)+'\n')
