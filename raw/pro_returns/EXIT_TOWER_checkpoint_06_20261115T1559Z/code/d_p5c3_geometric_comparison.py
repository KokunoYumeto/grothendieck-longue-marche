"""Explicit cellular/Peiffer comparison from the six-point cone diagram.

The two-map uses exact certificates in the fixed26 compact relators.
For each tetrahedron the open coherence filler is the inverse of the
chosen boundary-triangle certificate. The resulting identity sequence
is verified freely in the FULL source alphabet, then mapped factor by
factor. Its Peiffer reduction is empty. The24 open prism cells map to
D.25's basis identically. This is a specified simultaneous CW choice,
not a claim of canonical coordinates for bare group equalities.
"""
from pathlib import Path
from collections import Counter
from functools import lru_cache
import json,importlib.util
P=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('filler',P/'d_p5c3_fill.py');F=importlib.util.module_from_spec(spec);spec.loader.exec_module(F)
red,inv,cat=F.red,F.inv,F.cat
V=json.loads((P/'d_p2_genus_zero.json').read_text())[1]
I=json.loads((P/'d_p5c3_identities.json').read_text())
compact_names=['a','b','x','y','z','p','q','r','s']
pairs=[(1,3),(2,3),(1,4),(2,4),(3,4),(1,5),(2,5),(3,5),(4,5)];pairid={p:i+1 for i,p in enumerate(pairs)}
def modword(w):return tuple(pairid[i,j]*e for i,j,e in w)
source_gens=[{'kind':'open','name':n,'target_word':(i+1,)} for i,n in enumerate(compact_names)]
local={};localmu={};verts={v['graph_index']:v for v in V['vertices']}
for v in V['vertices']:
 g=v['graph_index'];local[g]={};localmu[g]={}
 for x in v['generators']:
  key=tuple(x['name']);idx=len(source_gens)+1;mu=modword(x['moduli_word'])
  local[g][key]=idx;localmu[g][idx]=mu
  source_gens.append({'kind':'local','graph':g,'name':key,'target_word':mu})
arrows={};edge={};q={}
for a in V['arrows']:
 pair=(a['source'],a['target']);arrows[pair]=a;edge[pair]=len(source_gens)+1;q[pair]=modword(a['moduli_word'])
 source_gens.append({'kind':'edge','source':pair[0],'target':pair[1],'target_word':q[pair]})
t={}
for g in verts:
 t[g]=len(source_gens)+1;source_gens.append({'kind':'open_crossing','source':g,'target':0,'target_word':()})
MU=[tuple(g['target_word']) for g in source_gens]
def image(w):return cat(*(MU[abs(x)-1] if x>0 else inv(MU[abs(x)-1]) for x in w))
def localword(g,w):return tuple(local[g][v,i,j]*e for v,i,j,e in w)
@lru_cache(maxsize=100000)
def fill(w):return F.fill(w)
rels=[];certificates=[];certix={}
def addrel(kind,w,metadata=None,certificate=None):
 w=red(w);mu=image(w)
 if certificate is None:certificate=fill(mu)
 else:certificate=tuple(certificate)
 assert F.expanded(certificate)==mu
 if certificate not in certix:certix[certificate]=len(certificates);certificates.append(certificate)
 r={'id':len(rels),'kind':kind,'word':w,'target_word':mu,'certificate':certix[certificate]}
 if metadata:r.update(metadata)
 rels.append(r);return r['id']
for i,r in enumerate(F.RELS):assert addrel('open_relator',r,{'compact_relator':i},[((),i,1)])==i
for g,v in verts.items():
 for k,r in enumerate(v['relators']):addrel('local_relator',localword(g,r),{'graph':g,'local_relator':k})
print('Local relators certified:',Counter(r['kind'] for r in rels),flush=True)
for pair,a in arrows.items():
 g,h=pair;e=edge[pair]
 for z in a['injections']:
  s=local[g][tuple(z['source_generator'])];target=localword(h,z['target_local_word'])
  addrel('sewing_relator',cat((e,s,-e),inv(target)),{'source':g,'target':h,'source_generator':s})
print('All3570 sewing-relator images certified.',flush=True)
open_arrow={}
for g in verts:
 for s,mu in localmu[g].items():
  open_arrow[g,s]=addrel('open_arrow_relator',cat((t[g],s,-t[g]),inv(mu)),{'graph':g,'source_generator':s})
triangle={};triwords={}
for z in V['triangles']:
 g,h,k=z['vertices'];f=localword(k,z['target_local_word']);w=cat((edge[h,k],edge[g,h],-edge[g,k]),inv(f))
 triangle[g,h,k]=addrel('triangle_relator',w,{'flag':(g,h,k)});triwords[g,h,k]=f
open_face={}
for g,h in arrows:
 w=cat((t[h],edge[g,h],-t[g]),inv(q[g,h]))
 open_face[g,h]=addrel('open_face_relator',w,{'flag':(g,h,0)})
print('All630 boundary triangle and840 open triangle images certified.',flush=True)
def conjugate(c,S):return tuple((cat(c,p),j,e) for p,j,e in S)
def inverse(S):return tuple((p,j,-e) for p,j,e in reversed(S))
def src_expanded(S):return red(x for c,j,e in S for x in c+(rels[j]['word'] if e>0 else inv(rels[j]['word']))+inv(c))
def open_arrow_certificate(g,w):
 out=[];prefix=()
 for x in w:
  mu=MU[abs(x)-1];rid=open_arrow[g,abs(x)]
  out.append((prefix if x>0 else cat(prefix,inv(mu)),rid,1 if x>0 else -1))
  prefix=cat(prefix,mu if x>0 else inv(mu))
 expected=cat((t[g],),w,(-t[g],),inv(image(w)))
 assert src_expanded(out)==expected
 return tuple(out)
def mapped_sequence(S):
 out=[]
 for c,j,e in S:
  cert=certificates[rels[j]['certificate']]
  if e<0:cert=F.inverse(cert)
  out.extend(F.conjugate(image(c),cert))
 return tuple(out)
tetra=[];total_source_factors=0;total_target_factors=0;nonempty=0
for z in V['triangles']:
 g,h,k=z['vertices'];f=triwords[g,h,k];muf=image(f);rid=triangle[g,h,k]
 T=certificates[rels[rid]['certificate']]
 delta=cat(muf,q[g,k],inv(q[g,h]),inv(q[h,k]))
 assert delta==inv(rels[rid]['target_word'])
 # The coherence filler is a completely explicit diagram in the open26 relators.
 coherence=F.inverse(T);assert src_expanded(coherence)==delta
 S=conjugate((t[k],),[((),rid,1)])
 S+=open_arrow_certificate(k,f)
 S+=conjugate(muf,[((),open_face[g,k],1)])
 S+=coherence
 S+=inverse(conjugate(q[h,k],[((),open_face[g,h],1)]))
 S+=(((),open_face[h,k],-1),)
 assert src_expanded(S)==(),('source tetrahedron failed',g,h,k)
 mapped=mapped_sequence(S)
 assert mapped==T+F.inverse(T),('mapped expression is not paired',g,h,k)
 assert F.reduce_sequence(mapped)==()
 assert F.expanded(mapped)==()
 nonempty+=bool(T);total_source_factors+=len(S);total_target_factors+=len(mapped)
 tetra.append({'flag':(g,h,k,0),'boundary_triangle_relator':rid,'open_coherence_word':delta,'boundary_triangle_certificate':rels[rid]['certificate'],
  'open_coherence_filler':'inverse of boundary_triangle_certificate in the open26 relators',
  'source_identity_sequence':S,'mapped_factor_count':len(mapped),'Peiffer_reduction':'adjacent inverse-factor cancellation of T followed by inverse(T)',
  'compact_basis_coordinates':[0]*24,'P5c3_basis_coordinates':[0]*24})
prisms=[]
for i,z in enumerate(I['identities']):
 S=tuple((tuple(e['conjugator']),e['relator'],e['exponent']) for e in z['identity_sequence'])
 assert src_expanded(S)==()
 assert mapped_sequence(S)==S
 coords=[0]*24;coords[i]=1
 prisms.append({'open_prism':i,'base_relator':z['base_relator'],'fibre_generator':z['fibre_generator'],'source_identity_sequence':S,'compact_basis_coordinates':coords,'P5c3_basis_coordinates':[-x for x in coords]})
# Every mapping-cylinder prism over a boundary2-cell has a simultaneous certificate.
# Its top is the fixed compact filling; its side is made from the fixed
# local-generator/open-face cylinders. This includes the local and sewing families.
open_onecell={s:rid for (g,s),rid in open_arrow.items()}
open_onecell.update({edge[pair]:rid for pair,rid in open_face.items()})
boundary_prisms=[]
for r in rels:
 if r['kind'] not in ('local_relator','sewing_relator','triangle_relator'):continue
 base=r.get('graph',r.get('target',r.get('flag',[None,None,None])[-1]))
 assert base in t
 C=[];prefix=()
 for x in r['word']:
  mu=MU[abs(x)-1]
  C.append((prefix if x>0 else cat(prefix,inv(mu)),open_onecell[abs(x)],1 if x>0 else -1))
  prefix=cat(prefix,mu if x>0 else inv(mu))
 assert src_expanded(C)==cat((t[base],),r['word'],(-t[base],),inv(r['target_word']))
 T=certificates[r['certificate']]
 S=conjugate((t[base],),[((),r['id'],1)])+F.inverse(T)+inverse(C)
 assert src_expanded(S)==()
 mapped=mapped_sequence(S);assert mapped==T+F.inverse(T)
 assert F.reduce_sequence(mapped)==()
 boundary_prisms.append({'boundary_relator':r['id'],'family':r['kind'],'base_vertex':base,'source_identity_sequence':S,'compact_basis_coordinates':[0]*24})
assert len(boundary_prisms)==6395
counts={'source_vertices':236,'oriented_one_cells':len(source_gens),'crossing_tree_edges':235,'one_vertex_generators_after_tree_collapse':len(source_gens)-235,'source_relators':len(rels),'source_relator_types':dict(Counter(r['kind'] for r in rels)),
 'distinct_compact_certificates':len(certificates),'certificate_conjugate_factors':sum(len(c) for c in certificates),'cone_tetrahedra':len(tetra),'nonempty_triangle_certificates':nonempty,
 'tetrahedral_source_factors':total_source_factors,'tetrahedral_mapped_factors':total_target_factors,'open_prisms':24,'compact_basis_size':24,'all_boundary_two_cell_prisms':len(boundary_prisms),'degree3_matrix_on_specified_cells':'[zero_(24x630) | identity_24]'}
out={'scope':'Specified coherent CW model using the displayed compact open vertex and chosen open coherence diagrams. Coordinates refer to this explicit cellular map. No canonical coordinates for bare transport equalities are asserted.',
 'normalizer_certificate':'d_p5c3_fill.py','source_generators':source_gens,'source_vertices':[0]+list(verts),'crossing_maximal_tree':[t[g] for g in verts],'source_relators':rels,'compact_certificates':certificates,'tetrahedra':tetra,'boundary_two_cell_prisms':boundary_prisms,'open_prisms':prisms,'counts':counts,
 'chain_map':'C1 substitutes target words; C2 substitutes conjugate-relator certificates; C3 sends each of630 tetrahedra to0 and each of24 open prisms to its named basis cell.',
 'right_inverse':'include the compact open-vertex presentation and its24 prism cells; C1,C2,C3 composites are the identity.',
 'P5c3_original_basis_conversion':'D.25 basis vector is the negative of its named P5c3 vector; degree3 matrix in the original P5c3 basis is [zero | -identity]. The inverse uses the reversed open prism orientations.'}
(P/'d_p5c3_geometric_comparison.json').write_text(json.dumps(out,indent=2)+'\n')
print('Complete six-point cellular/Peiffer comparison:',counts,flush=True)
print('Every source tetrahedral identity is freely empty in the full source alphabet.',flush=True)
print('Every mapped tetrahedron has literal certificate T inverse(T), with an explicit Peiffer cancellation; all24 open prism identities map identically.',flush=True)
