"""Independent free-group verifier of the serialized positive-genus certificates.
This imports neither normalizer nor construction program. It checks the actual
JSON artifact and each signed factor, including source identities and all
listed mapping-cylinder prisms.
"""
from pathlib import Path
import json,sys,time
P=Path(__file__).resolve().parent
stem=sys.argv[1] if len(sys.argv)>1 else 'd_elliptic_three_peiffer'
start=time.time();D=json.loads((P/(stem+'.json')).read_text())
def reduce(w):
 out=[]
 for x in w:
  if out and out[-1]==-x:out.pop()
  else:out.append(x)
 return tuple(out)
def inverse(w):return tuple(-x for x in reversed(w))
def cat(*ws):return reduce(x for w in ws for x in w)
R=list(map(tuple,D['compact_relators']))
Q=[tuple(r['word']) for r in D['source_relators']]
C=[tuple((tuple(p),j,e) for p,j,e in S) for S in D['compact_certificates']]
MU=[tuple(g['target_word']) for g in D['source_generators']]
def image(w):return reduce(x for s in w for x in (MU[s-1] if s>0 else inverse(MU[-s-1])))
def expand(S,rels):
 return reduce(x for p,j,e in S for x in tuple(p)+(rels[j] if e>0 else inverse(rels[j]))+inverse(p))
def invseq(S):return tuple((p,j,-e) for p,j,e in reversed(S))
def mapped(S):
 out=[]
 for p,j,e in S:
  c=image(p);T=C[D['source_relators'][j]['certificate']]
  if e<0:T=invseq(T)
  out.extend((cat(c,t),k,s) for t,k,s in T)
 return tuple(out)
def cancel(S):
 out=[]
 for p,j,e in S:
  x=(tuple(p),j,e)
  if out and out[-1][:2]==x[:2] and out[-1][2]==-e:out.pop()
  else:out.append(x)
 return out
exp=[expand(S,R) for S in C]
for r in D['source_relators']:
 assert image(r['word'])==tuple(r['target_word'])==exp[r['certificate']]
for z in D['cone_identities']:
 S=z['source_identity_sequence'];assert expand(S,Q)==()
 M=mapped(S)
 assert M==tuple((tuple(p),j,e) for p,j,e in z['mapped_identity_sequence'])
 T=C[z['boundary_triangle_certificate']]
 assert M==T+invseq(T)
 assert not cancel(M) and expand(M,R)==()
for z in D['boundary_two_cell_prisms']:
 S=z['source_identity_sequence'];assert expand(S,Q)==()
 M=mapped(S);assert len(M)==z['mapped_factor_count']
 assert not cancel(M) and expand(M,R)==()
out={'artifact':stem+'.json','compact_certificates':len(C),
     'source_relators_verified':len(Q),'source_cone_identities_verified':len(D['cone_identities']),
     'boundary_prisms_verified':len(D['boundary_two_cell_prisms']),
     'all_signed_factor_products_freely_checked':True,
     'all_mapped_identity_sequences_cancel_by_adjacent_inverse_factors':True,
     'seconds':time.time()-start}
(P/(stem+'_verify.json')).write_text(json.dumps(out,indent=2)+'\n')
print(out,flush=True)
