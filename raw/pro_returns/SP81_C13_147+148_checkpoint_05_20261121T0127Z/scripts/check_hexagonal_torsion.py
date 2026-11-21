"""Exact checks in the rank-two lattice presented on 148_scan009.
No scan recognition or transcription generation is performed here.
"""
from itertools import product
from pathlib import Path
from datetime import datetime, timezone
import json

# In Z[T]/(T^2+T+1), multiplication by T sends (a,b) to (-b,a-b).
M=((0,-1),(1,-1))
J=((1,-1),(1,0))  # 1+T = -T^2, the written minus-conjugate generator.
I=((1,0),(0,1))
def mul(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def add(A,B): return tuple(tuple(A[i][j]+B[i][j] for j in range(2)) for i in range(2))
def scale(a,A):return tuple(tuple(a*x for x in row) for row in A)
def apply(A,v,n):return tuple(sum(A[i][j]*v[j] for j in range(2))%n for i in range(2))
def power(A,n):
 R=I
 for _ in range(n):R=mul(R,A)
 return R
assert add(add(mul(M,M),M),I)==((0,0),(0,0))
assert mul(add(M,scale(-1,I)),add(M,scale(2,I)))==scale(-3,I)
assert power(J,3)==scale(-1,I) and power(J,6)==I
all2=list(product(range(2),repeat=2)); all3=list(product(range(3),repeat=2))
action2=[{'numerator':v,'image':apply(J,v,2)} for v in all2]
action3=[{'numerator':v,'image':apply(M,v,3),'fixed':apply(M,v,3)==v} for v in all3]
fixed3=[v for v in all3 if apply(M,v,3)==v]
assert fixed3==[(0,0),(1,2),(2,1)]
orbit=[];v=(1,0)
for _ in range(3):orbit.append(v);v=apply(J,v,2)
assert v==(1,0) and set(orbit)==set(all2)-{(0,0)}
# (1 - T^2)/3 = (2+T)/3; (1-T)/3 reduces to (1,2)/3.
assert apply(M,(2,1),3)==(2,1)
assert apply(M,(1,2),3)==(1,2)
result={'checked_at':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
 'base':'R^2/Z^2 in the basis (1,zeta) of the displayed C/Z[zeta]',
 'relation':'zeta^2+zeta+1=0','M':M,'J':J,
 'all_two_torsion_action_by_J':action2,'nonzero_two_torsion_orbit':orbit,
 'all_three_torsion_action_by_M':action3,'fixed_three_torsion_numerators':fixed3,
 'fixed_set_exhaustion':'(M-I)(M+2I)=-3I, so every M-fixed torus class is killed by 3; the nine classes were enumerated exactly.',
 'source_example_numerator':[2,1],'unbarred_alternative_numerator':[1,2],
 'reading_limit':'Both example classes are fixed and nonzero; this calculation cannot choose whether the written zeta has a bar. The crop supplies that decision. No letter is supplied to the handwritten exponential.'}
root=Path(__file__).resolve().parents[1]
p=root/'work/hexagonal_torsion_check.json'
assert not p.exists(),'Do not overwrite a prior certificate.'
p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
