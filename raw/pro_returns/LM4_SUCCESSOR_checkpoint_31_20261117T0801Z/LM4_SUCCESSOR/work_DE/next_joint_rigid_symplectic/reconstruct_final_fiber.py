"""Fresh recovery of the last-six-strand fiber observations.

The [c,f] row is a new post-recovery calculation: the corresponding old
command never executed. The other two rows recheck retained observations.
"""
from pathlib import Path
import json,sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'next_B56'))
from membership_rigid7 import reduce_word as red,inverse as inv,multiply as mul,substitute as sub,artin
j=json.loads((HERE/'cyclic_rigid_braid_words.json').read_text())
old=j['finite_order'];tau=(3,4,5)
assert old==[4,11,5,1,10,6]
braids={r['index']+1:mul(inv(tau),r['braid'],tau) for r in j['basis']}
new=[4,11,1,10,6,5]
def push(w):
    A=artin(w,6);v=list(A[-1]);q=[]
    while len(v)>1:
        assert v[0]==-v[-1]
        q.append(v.pop(0));v.pop()
    assert v==[6]
    return red(a for a in q if abs(a)!=6)
def cyclic(w):
    w=list(w)
    while len(w)>1 and w[0]==-w[-1]:w=w[1:-1]
    return tuple(w)
def conjugate(a,b):
    a,b=cyclic(a),cyclic(b)
    return len(a)==len(b) and any(a==b[k:]+b[:k] for k in range(len(b)))
def comm(a,b):return mul(a,b,inv(a),inv(b))
words={'f1':(2,),'[a,t]':comm((1,),(-6,-5,-1,-3,-4)),
       '[c,f]':comm((3,),(6,))}
quot={i:(i,) for i in range(1,5)};quot[5]=(-4,-3,-2,-1)
B=(1,2,3,4,5);records=[]
for name,w in words.items():
    p=push(sub(w,braids));q=sub(p,quot)
    assert p
    records.append({'name':name,'source':w,'push':p,'after_boundary_filling':q})
    print(name,'push length',len(p),'boundary-filled length',len(q),flush=True)
assert conjugate(records[0]['push'],inv(B))
assert records[1]['after_boundary_filling']
print('f1 push is conjugate to inverse total boundary: PASS',flush=True)
print('[a,t] survives killing the total boundary, so is outside its normal closure: PASS',flush=True)
print('[c,f] is explicitly marked a new post-recovery row, not recovered old stdout.',flush=True)
(HERE/'final_fiber_reconstructed_certificate.json').write_text(json.dumps({
    'provenance':'Fresh Artin computation from restored original braid words',
    'old_order':old,'new_order':new,'tau':tau,'push_convention':'antihomomorphism; invert to obtain homomorphism',
    'records':records},indent=2)+'\n')
