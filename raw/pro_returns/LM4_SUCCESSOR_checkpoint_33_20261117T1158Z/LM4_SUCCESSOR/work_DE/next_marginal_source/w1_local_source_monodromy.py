"""Exact local w=1 source action, with a local based marking only.

No global w-pencil whisker or whole source-normalizer inference is made.
"""
from pathlib import Path
import json
from weighted_stallings import multiply as mul,inverse as inv,substitute as sub
P=Path(__file__).resolve().parent

def artin(word,n):
 a={i:(i,) for i in range(1,n+1)}
 for s in word:
  k=abs(s);v,w=a[k],a[k+1]
  a[k],a[k+1]=(mul(v,w,inv(v)),v) if s>0 else (w,mul(inv(w),v,w))
 return a

def source_action(word,n=4):
 a=artin(word,n);w=a[n];h=[]
 while len(w)>1:
  assert w[0]==-w[-1];h.append(w[0]);w=w[1:-1]
 assert w==(n,)
 q=tuple(x for x in h if abs(x)!=n)
 return {i:mul(inv(q),tuple(x for x in a[i] if abs(x)!=n),q) for i in range(1,n)},q
# Rotate the local real ordering S,P,C,D by180 degrees, obtaining D,C,P,S.
# The full4 twist is central; the residual source/product full twist is sigma3^2.
Z=(1,2,3)*4;pbraid=(3,3);beta=Z+pbraid
for i in [1,2,3]:assert artin(Z+(i,),4)==artin((i,)+Z,4)
actZ,_=source_action(Z);act,q=source_action(beta);actp,qp=source_action(pbraid)
assert actZ=={i:(i,) for i in range(1,4)}
assert qp==(3,)
p=inv(qp)
assert act==actp=={i:mul(p,(i,),inv(p)) for i in range(1,4)}
print('Full4 twist central, and source-based local action of the full twist is identity: PASS')
print('Residual sigma3^2 has actual fiber homomorphism p=',p)
print('Local source action is exactly Inn(p) on all3 fiber generators: PASS')
# Forgetting source leaves the full3 twist, as a braid identity.
state=list(range(4));deleted=[]
for s in beta:
 k=abs(s)-1
 if state[k]!=3 and state[k+1]!=3:
  idx=sum(x!=3 for x in state[:k])+1;deleted.append(idx if s>0 else -idx)
 state[k],state[k+1]=state[k+1],state[k]
assert state==list(range(4))
assert artin(deleted,3)==artin((1,2)*3,3)
print('Forgetting the moving source leaves exactly the full3 fiber twist: PASS')
out={'description':__doc__,'initial_local_order_before_rotation':['source','product1','constant1','diagonal'],'order_after_half_turn':['diagonal','constant1','product1','source'],'beta':beta,'fiber_deletion_braid':deleted,'fiber_meridian_p':p,'local_source_action':act,'geometric_proof':'For epsilon=r exp(2pi it), divide v-1 by epsilon. Three points are fixed at -1,0,1; the product point is -1/(1+epsilon), whose displacement from the source -1 is epsilon/(1+epsilon). This winds once in a disk disjoint from0,1. The removed global rotation supplies the full4 twist.','scope':'Local4-point marking only; does not identify the action on the other nine global fiber punctures or the actual global source subgroup.'}
(P/'w1_local_source_monodromy.json').write_text(json.dumps(out,indent=2)+'\n')
