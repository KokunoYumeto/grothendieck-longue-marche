"""Identify the local q-meridian with the literal transported product-one word.

t=w-1, q=(z-1)/t^2.  Fix the actual w=1 northeast corner and move only
the source around a positive q-diamond based at q=-1.  The sign is retained.
"""
from pathlib import Path
import itertools,json
import sympy as S
from w_pencil_braid import Segment,F,Q,I,X,ROT,u,parts,lower_norm,frac,red
from weighted_stallings import multiply as mul,inverse as inv,substitute as sub
P=Path(__file__).resolve().parent
h=Q(1,10000);w=1+h+h*I;t=w-1
class QSegment(Segment):
 def __init__(self,a,b):
  self.a,self.b=a,b;self.t=a+(b-a)*X
  rr=[S.Integer(0)]+[S.expand(w*v) for v in u]+[S.expand(w*w)]+list(u)+[S.expand(1+t*t*self.t)]
  self.raw_rational=rr;self.rational=[parts(ROT*z) for z in rr]
  self.U=[];self.axis=[];self.center=parts(S.Integer(0));self.parameter_bound=6;self.derivative_bound=F(10**8)
  for r,s in itertools.combinations(rr,2):
   R,J=parts(r-s);lower_norm(R,J,F(1,10**12))
  self.records=[];self.candidates=[]
path=[-1,-I,1,I,-1]
records=[QSegment(a,b).compute() for a,b in zip(path,path[1:])]
word=red([x for r in records for x in r['word']])
assert word==[10,10] or tuple(word)==(10,10)
assert all(records[i]['final_order']==records[i+1]['initial_order'] for i in range(3))
assert records[0]['initial_order']==records[-1]['final_order']
assert records[0]['initial_order']==[3,9,10,4,2,8,0,11,5,7,12,1,6]
# In the actual inverse-conjugator extraction, sigma10^2 sends x11 to
# x10*x11*x10^-1.  Filling x11 and inverting therefore gives x10^-1.
local_pointpush=(-10,)
mark=json.loads((P/'w_local_markings.json').read_text())['all_local_markings'][1]
transport={int(j):tuple(v) for j,v in mark['local_to_initial_fiber'].items()}
actual=sub(local_pointpush,transport)
adapt=json.loads((P/'w_source_adapted_basis.json').read_text())
back={int(j):tuple(v) for j,v in adapt['initial_basis_in_new'].items()}
assert sub(actual,back)==(-12,)
out={'description':__doc__,'w_corner':['10001/10000','1/10000'],'q_path':['-1','-I','1','I','-1'],'records':records,'local_braid':word,'local_pointpush_word':local_pointpush,'initial_pointpush_word':actual,'adapted_word':[-12],'geometric_interpretation':'The positive q-meridian is b inverse in the inverse-conjugator convention. Reversing its orientation gives exactly b, with the same actual source whisker and no further conjugator.','scope':'This is a topological based identification. It does not provide a Galois-invariant global etale path.'}
(P/'w1_local_q_meridian.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all4 exact polynomial q segments; positive q loop has braid sigma10^2')
print('PASS inverse-conjugator convention: positive q meridian = b^-1 exactly in actual adapted marking')
print('No additional source conjugator; no arithmetic path invariance inferred')
