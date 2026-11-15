"""Executed graph flags and explicit D4 sewing homomorphism for(1,3).
This does not yet certify all304 named face maps of the full diagram.
"""
from pathlib import Path
from itertools import permutations,combinations,combinations_with_replacement,product
from collections import Counter
import ast,json,importlib.util
P=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('d4',P/'d_artin_d4.py');D=importlib.util.module_from_spec(spec);spec.loader.exec_module(D)
G={};tree=ast.parse((P/'a_graphs.py').read_text())
G.update(permutations=permutations,combinations_with_replacement=combinations_with_replacement,product=product,Counter=Counter)
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'a_graphs','exec'),G)
graphs=[tuple((tuple(a[0]),tuple(a[1]),tuple(map(tuple,a[2])))) for a in json.loads((P/'a_graphs_1_3.json').read_text())['graphs']]
ix={g:i for i,g in enumerate(graphs)}
def edge_group(g):
 gen,legs,edges=g;r=len(edges);out=set()
 for vp in permutations(range(len(gen))):
  if any(gen[i]!=gen[vp[i]] for i in range(len(gen))) or any(vp[x]!=x for x in legs):continue
  for ep in permutations(range(r)):
   if all(tuple(sorted((vp[a],vp[b])))==tuple(sorted(edges[ep[i]])) for i,(a,b) in enumerate(edges)):out.add(ep)
 return sorted(out)
def act(mask,p):return sum(1<<p[i] for i in range(len(p)) if mask>>i&1)
flags=[]
for i,g in enumerate(graphs[1:],1):
 r=len(g[2]);full=(1<<r)-1;E=edge_group(g)
 allflags=[(full,)]+[(full,s) for s in range(1,full)]+[(full,s,t) for s in range(1,full) for t in range(1,s) if t&s==t]
 seen=set()
 for flag in allflags:
  canon=min(tuple(act(s,p) for s in flag) for p in E)
  if canon in seen:continue
  seen.add(canon)
  types=[ix[G['contract'](g,[j for j in range(r) if not (m>>j&1)])] for m in canon]
  flags.append({'largest_graph':i,'retained_masks':canon,'graph_types':types,'edge_permutation_stabilizer':[p for p in E if all(act(s,p)==s for s in canon)]})
counts=[sum(len(x['retained_masks'])==r for x in flags) for r in (1,2,3)]
assert counts==[22,53,33],counts
# Exact mixed B4 source: pure generators plus node half-braid s.
B={};tree=ast.parse((P/'b_genus_zero.py').read_text())
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'b_genus_zero','exec'),B)
a=(1,);h=(1,4)*3;s=D.cat(h,(-1,));tail=(1,4,3)*4
im={(1,2):D.cat(s,s),(1,3):(2,-1),(1,4):D.cat((-2,3),D.inv(tail)),(3,4):tail}
im[2,3]=D.conj(s,im[1,3]);im[2,4]=D.conj(s,im[1,4])
def ev(w):return D.cat(*(im[i,j] if e>0 else D.inv(im[i,j]) for i,j,e in w))
checks=[]
for ell in (3,4):
 for i,j in combinations(range(1,ell),2):
  for k in range(1,ell):
   x=B['A'](i,j);u=B['A'](k,ell);rhs=B['comb'](ell,x+u+B['inv'](x))
   assert D.equal(D.conj(im[i,j],im[k,ell]),ev(rhs));checks.append(['PB',ell,i,j,k])
for i,j in combinations(range(1,5),2):
 rhs=B['comb'](4,(1,)+B['A'](i,j)+(-1,))
 assert D.equal(D.conj(s,im[i,j]),ev(rhs));checks.append(['half_conjugation',i,j])
for w in [s,*im.values()]:assert D.equal(D.cat(a,w),D.cat(w,a))
Z=D.cat(*(im[i,j] for j in range(2,5) for i in range(1,j)))
assert D.equal(Z,(-1,-1));checks.append(['full_twist_equals_node_minus_two'])
curves=[]
for i in (1,2,3):
 j,k=[x for x in (1,2,3) if x!=i];q=(j,4,k,j,4,j);sep=(j,4,k)*4
 assert D.equal(D.cat(q,q),sep)
 assert D.equal(D.conj(q,(j,)),(k,))
 assert D.equal(D.conj(q,(k,)),(j,))
 assert D.equal((q+(i,))*2,(j,k))
 curves.append({'omitted_leaf':i,'separating_pair_twist':sep,'edge_exchange':q,'star_comparison_Delta_power':D.normal(D.cat((q+(i,))*2,(-k,-j)))[0]})
out={'type':[1,3],'orbit_counts':dict(vertices=22,edges=53,triangles=33,barycentric_objects=108,face_arrows=304,face_coherences=198),
     'flags':flags,'mixed_braid_source':'(PB4 plus s, s²=A12, Artin conjugation by sigma1) times central<a>, quotient Z4=a^-2',
     'mixed_braid_images':{f'A{i}{j}':w for (i,j),w in im.items()},'half_braid_image':s,'node_image':a,'mixed_braid_checks':checks,
     'pair_families':curves,'unresolved':'Complete named local word dictionary for all304 arrows is not yet supplied.'}
(P/'d_p2_elliptic_three_partial.json').write_text(json.dumps(out,indent=2)+'\n')
print('P2(1,3) orbit cells:',out['orbit_counts'])
print('Mixed braid sewing:11 pure relations,6 half-conjugations,central node and full-twist relation verified.')
print('Three pair families: q_i²=D_i, q_i exchanges the two retained leaves, (q_i a_i)²=a_j a_k; all exact.')
print('The full304-arrow named local dictionary remains unresolved.')
