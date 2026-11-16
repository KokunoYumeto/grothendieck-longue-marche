"""Fresh Q/Birman certificate reconstructed after the runtime replacement.

The only input braids are the verified checkpoint-06 full eleven-strand
common-base words.  No stdout from the unavailable old environment is used.
This proves relations and action formulas, not injectivity of Q or theta5.
"""
from pathlib import Path
import json,itertools,sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'next_B56'))
from membership_rigid7 import reduce_word as red,inverse as inv,multiply as mul,substitute as sub,artin
data=json.loads((HERE.parent/'next_B59_image/common_base_braid_words.json').read_text())
initial=data['initial_order_labels']
def delete(w,order,keep):
    state=list(order);out=[]
    for a in w:
        j=abs(a)-1
        if state[j] in keep and state[j+1] in keep:
            q=sum(x in keep for x in state[:j])+1
            out.append(q if a>0 else -q)
        state[j],state[j+1]=state[j+1],state[j]
    assert state==list(order)
    return red(out)
def comm(a,b):return mul(a,b,inv(a),inv(b))
def is_identity(w,n):return artin(w,n)==tuple((i,) for i in range(1,n+1))
keep={1,4,6,10,11};order=[x for x in initial if x in keep]
assert order==[4,11,1,10,6]
braids={int(i)+1:delete(w,initial,keep) for i,w in data['C5'].items()}
t=(-6,-5,-1,-3,-4)
named={'a':(1,),'t':t,'c':(3,),'f':(6,),'e':(5,)}
relations={'f1':(2,),'[a,t]':comm((1,),t),'[c,f]':comm((3,),(6,))}
for name,w in relations.items():
    assert w and is_identity(sub(w,braids),5)
    print(name,'nonempty source word, identity exact Artin action in PB5: PASS',flush=True)
assert mul(inv(t),(-6,),(-5,),(-1,),(-3,))==(4,)
print('Nielsen basis (a,t,c,f,e); reconstructed old f3 is exactly signed word (4,): PASS',flush=True)
basekeep={1,4,6,11};baseorder=[x for x in initial if x in basekeep]
assert baseorder==[4,11,1,6]
for name in ['c','t']:
    w=sub(named[name],braids)
    assert is_identity(delete(w,order,basekeep),4)
print('Further deletion of label10 kills c and t exactly in PB4: PASS',flush=True)

# Put moving label10 last.  Conjugate through the adjacent transposition.
tau=(4,);neworder=[4,11,1,6,10]
last={i:mul(inv(tau),b,tau) for i,b in braids.items()}
def conjugator(A):
    v=list(A[-1]);q=[]
    while len(v)>1:
        assert v[0]==-v[-1]
        q.append(v.pop(0));v.pop()
    assert v==[5]
    return red(a for a in q if abs(a)!=5)
def push(w):return conjugator(artin(w,5))
def action(w):
    A=artin(w,5);q=conjugator(A)
    return {i:mul(inv(q),red(a for a in A[i-1] if abs(a)!=5),q) for i in range(1,5)}
C=(-3,-2,1,2,3);T=(-3,2,3);R=(3,);S=(4,)
new_to_old={1:C,2:T,3:R,4:S}
old_to_new={1:(3,2,1,-2,-3),2:(3,2,-3),3:(3,),4:(4,)}
for i in range(1,5):
    assert sub(old_to_new[i],new_to_old)==(i,)
    assert sub(new_to_old[i],old_to_new)==(i,)
assert push(sub(named['c'],last))==C
assert push(sub(named['t'],last))==T
print('Exact free fiber basis C,T,R,S and c/t push words: PASS',flush=True)
actions={}
for name in ['a','f','e']:
    b=sub(named[name],last);alpha=action(b)
    out={i:sub(sub(new_to_old[i],alpha),old_to_new) for i in range(1,5)}
    actions[name]=out
    for s in ['c','t']:
        h=sub(named[s],last)
        assert push(mul(b,h,inv(b)))==sub(push(h),alpha)
    print(name,'action in basis (C,T,R,S):',out,flush=True)
p=(-4,-4,-1,-2,-3);U=mul(p,(2,),inv(p));q=mul(U,(-4,-2))
expected={
 'a':{1:(-2,-3,1,3,2),2:(2,),3:(3,),4:(-2,-3,4,3,2)},
 'f':{1:(1,),2:(4,2,-4),3:mul(comm((4,),(2,)),(3,),inv(comm((4,),(2,)))),4:(4,2,4,-2,-4)},
 'e':{1:(-4,1,4),2:U,3:mul(q,(3,),inv(q)),4:(4,)}
}
assert actions==expected
print('All three compact automorphism formulas match the fresh Artin computation: PASS',flush=True)

# The standard last-conjugator extraction is an ANTIhomomorphism on this kernel.
A1=mul((4,3,2),(1,1),(-2,-3,-4))
A2=mul((4,3),(2,2),(-3,-4))
assert is_identity(delete(A1,neworder,set(neworder[:-1])),4)
assert is_identity(delete(A2,neworder,set(neworder[:-1])),4)
u,v=push(A1),push(A2)
assert push(mul(A1,A2))==mul(v,u)
assert push(mul(A1,A2))!=mul(u,v)
print('Antihomomorphism convention: push(A1 A2)=push(A2)push(A1), not direct product: PASS',flush=True)
print('Taking the inverse of every push word gives the actual free-fiber homomorphism.',flush=True)

# The six-root arrangement collision multiplicities are elementary exact integers.
fixed=[0,1,4];moving=[0,2,3]
mult=[sum((i-j)%5==r for i in fixed for j in moving) for r in range(5)]
assert mult==[1,2,2,2,2] and 3+3+sum(mult)==15
print('Six-form Vandermonde multiplicities x^3 y^3 (y-x) product_(r=1)^4(y-zeta^r x)^2: PASS',flush=True)
cert={'provenance':'Fresh exact reconstruction from verified checkpoint-06 words',
      'five_strand_order':order,'five_strand_source_images':braids,
      'relations':relations,'nielsen_basis':named,'base_order':baseorder,
      'last_strand_order':neworder,'tau':tau,'new_basis_in_old':new_to_old,
      'old_basis_in_new':old_to_new,'actions':actions,
      'push_convention':'antihomomorphism; invert each output for a homomorphism',
      'anti_check':{'A1':A1,'A2':A2,'push1':u,'push2':v,'push_product':push(mul(A1,A2))},
      'cross_collision_multiplicities':mult,
      'not_proved':['Q embeds into PB5','theta5 is injective','full induced profinite topology','completed kernel equals closure of discrete kernel']}
(HERE/'Q_birman_reconstructed_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS exact Q-factor relations, Birman action, and convention audit; all injection questions remain open',flush=True)
