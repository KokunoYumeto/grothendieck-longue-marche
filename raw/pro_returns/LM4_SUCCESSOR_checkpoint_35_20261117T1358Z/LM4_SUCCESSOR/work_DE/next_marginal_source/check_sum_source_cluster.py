"""Actual common-marking five-point source cluster in the sum pencil."""
from pathlib import Path
import json,itertools
HERE=Path(__file__).resolve().parent
D=json.loads((HERE/'sum_pencil_braids.json').read_text())
def red(w):
 o=[]
 for x in w:
  if o and o[-1]==-x:o.pop()
  else:o.append(x)
 return tuple(o)
def inv(w):return tuple(-x for x in w[::-1])
def mul(*ws):return red(itertools.chain.from_iterable(ws))
def sub(w,A):return mul(*(A[x] if x>0 else inv(A[-x]) for x in w))
def art(w):
 A={i:(i,) for i in range(1,24)}
 for x in w:
  i=abs(x);a,b=A[i],A[i+1]
  A[i],A[i+1]=(mul(a,b,inv(a)),a) if x>0 else (b,mul(inv(b),a,b))
 return A
def Delta(start,size):return tuple(j for length in range(size-1,0,-1) for j in range(start,start+length))
order=D['initial_order'];cluster=sorted(order.index(j)+1 for j in [2,3,8,13,14])
assert cluster==list(range(10,15));C=tuple(cluster)
row=next(r for r in D['loops'] if r['name']=='positive_0')
W=row['forward_segments'][0]['word'];local=mul(*(s['word'] for s in row['forward_segments'][1:]))
standard=mul(Delta(10,5),Delta(11,3))
assert art(local)==art(standard)
assert art(row['word'])==art(standard)
assert sub(C,art(W))==C
A=art(standard);R=(10,11,12,13)
assert A[10]==mul(R,(14,),inv(R)) and A[14]==(10,)
for j in (11,12,13):assert A[j]==mul(R,(j,),inv(R))
for j in list(range(1,10))+list(range(15,24)):assert A[j]==(j,)
source={j:(j,) for j in list(range(1,10))+list(range(15,24))};source[10]=C
new={j:(j,) for j in range(1,24)};new[10]=(10,-14,-13,-12,-11)
old={j:(j,) for j in range(1,24)};old[10]=C
for j in range(1,24):assert sub(new[j],old)==(j,)==sub(old[j],new)
out={'scope':__doc__,'source_cluster_positions':cluster,'source_boundary_C':C,'whisker_word':W,
 'local_word':local,'global_word':row['word'],'standard_half_twist_product':standard,
 'R':R,'source_generators':source,'missing_generators':[11,12,13,14],
 'U_indices':sorted(order.index(j)+1 for j in [4,5,6,7,9,10,11,12]),
 'old_to_special_basis':new,'special_to_old_basis':old,
 'local_variation_quotient':'y14=y10; R=y10*y11*y12*y13 central; group Z(R) times F(y10,y11,y12)',
 'source_boundary_in_local_quotient':'C=R*y10, not the central element R'}
(HERE/'sum_source_cluster.json').write_text(json.dumps(out,indent=2)+'\n')
print('Actual local and global source lassos equal Delta5*Delta3_inner in the23-strand Artin action: PASS')
print('The common whisker fixes C=y10*y11*y12*y13*y14: PASS')
print('Local quotient Z times F3, source C=R*y10; both Nielsen substitutions: PASS')
print('U indices',out['U_indices'],'missing source directions',out['missing_generators'])
