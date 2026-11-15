"""Complete compact-relator expansions of the positive-genus cone diagrams.

All source lower cells are retained. The map into the fixed compact
presentation is specified by freely checked relator certificates.
The chosen open coherence disk is the inverse boundary-triangle disk,
simultaneously for every triangle. Each resulting cone identity maps
to T followed by inverse(T), with literal Peiffer cancellation.
"""
from pathlib import Path
from collections import Counter
from functools import lru_cache
import importlib.util,json,time,sys
P=Path(__file__).resolve().parent
def load(name):
 spec=importlib.util.spec_from_file_location(name,P/(name+'.py'))
 obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj)
 return obj
def elliptic_data():
 d=json.loads((P/'d_p2_elliptic_three.json').read_text())
 return {'type':[1,3],'objects':d['objects'],'groups':d['groups'],
         'arrows':d['arrows'],'triangles':d['coherences'],
         'global_names':['a1','a2','a3','b']}

def genus_two_data():
 d=json.loads((P/'d_p2_genus_two.json').read_text())
 groups={}
 for name,g in d['groups'].items():
  names=list(g['generators']);ix={s:i+1 for i,s in enumerate(names)}
  def word(w):
   return tuple(-ix[s[1:]] if s.startswith('-') else ix[s] for s in w)
  groups[name]={'generator_names':names,'global_images':list(g['generators'].values()),
                'relators':[word(w) for w in g['relators']]}
 objects=[{'id':name,'group':o['group']} for name,o in d['cells'].items()]
 obj={o['id']:o for o in objects};arrows=[];aix={}
 for i,a in enumerate(d['face_injections']):
  gn=groups[obj[a['source']]['group']]['generator_names']
  tn=groups[obj[a['target']]['group']]['generator_names'];ix={s:j+1 for j,s in enumerate(tn)}
  def word(w):
   return tuple(-ix[s[1:]] if s.startswith('-') else ix[s] for s in w)
  arrows.append({'id':i,'source':a['source'],'target':a['target'],
                 'transporter':a['transport'],'generator_images':[word(a['images'][s]) for s in gn]})
  aix[a['source'],a['target']]=i
 tris=[]
 for z in d['coherence_triangles']:
  a,b,c=z['source'],z['middle'],z['target']
  f=()
  if z['twist']:
   assert (a,b,c)==('DBN','BN','N')
   f=(2,3,4,2,3,2,-1)  # Delta4(b,d,c) a^{-1} in the named N alphabet.
  tris.append({'source':a,'target':c,'first':aix[a,b],'second':aix[b,c],
               'direct':aix[a,c],'target_twist_word':f})
 return {'type':[2,0],'objects':objects,'groups':groups,'arrows':arrows,
         'triangles':tris,'global_names':['sigma1','sigma2','sigma3','sigma4','sigma5']}

def run(data,F,stem):
 started=time.time()
 red,inv,cat=F.red,F.inv,F.cat
 def ev(w,images):return cat(*(images[abs(x)-1] if x>0 else inv(images[abs(x)-1]) for x in w))
 source_gens=[{'kind':'open','name':n,'target_word':(i+1,)} for i,n in enumerate(data['global_names'])]
 groups=data['groups'];objects={o['id']:o for o in data['objects']}
 local={};localmu={}
 for g,o in objects.items():
  G=groups[o['group']];local[g]=[];localmu[g]={}
  for n,w in zip(G['generator_names'],G['global_images']):
   idx=len(source_gens)+1;w=tuple(w)
   local[g].append(idx);localmu[g][idx]=w
   source_gens.append({'kind':'local','object':g,'name':n,'target_word':w})
 arrows={a['id']:a for a in data['arrows']};edge={};q={}
 for i,a in arrows.items():
  edge[i]=len(source_gens)+1;q[i]=tuple(a['transporter'])
  source_gens.append({'kind':'edge','arrow':i,'source':a['source'],'target':a['target'],'target_word':q[i]})
 t={}
 for g in objects:
  t[g]=len(source_gens)+1
  source_gens.append({'kind':'open_crossing','source':g,'target':'O','target_word':()})
 MU=[tuple(g['target_word']) for g in source_gens]
 def image(w):return ev(w,MU)
 def localword(g,w):return tuple(local[g][abs(x)-1]*(1 if x>0 else -1) for x in w)
 @lru_cache(maxsize=100000)
 def fill(w):return F.fill(w)
 rels=[];certs=[];certix={}
 def addrel(kind,w,metadata=None,certificate=None):
  w=red(w);mu=image(w)
  C=fill(mu) if certificate is None else tuple(certificate)
  assert F.expanded(C)==mu
  if C not in certix:certix[C]=len(certs);certs.append(C)
  r={'id':len(rels),'kind':kind,'word':w,'target_word':mu,'certificate':certix[C]}
  if metadata:r.update(metadata)
  rels.append(r);return r['id']
 for i,r in enumerate(F.RELS):assert addrel('open_relator',r,{'compact_relator':i},[((),i,1)])==i
 for g,o in objects.items():
  for k,r in enumerate(groups[o['group']]['relators']):
   addrel('local_relator',localword(g,r),{'object':g,'local_relator':k})
 print(stem,'local relators',len(rels)-len(F.RELS),flush=True)
 for i,a in arrows.items():
  g,h=a['source'],a['target'];e=edge[i]
  for z,w in zip(local[g],a['generator_images']):
   addrel('sewing_relator',cat((e,z,-e),inv(localword(h,w))),
          {'arrow':i,'source':g,'target':h,'source_generator':z})
 print(stem,'sewing relators certified',flush=True)
 open_arrow={}
 for g in objects:
  for s,mu in localmu[g].items():
   open_arrow[g,s]=addrel('open_arrow_relator',cat((t[g],s,-t[g]),inv(mu)),
                         {'object':g,'source_generator':s})
 triangle={};triwords={}
 for i,z in enumerate(data['triangles']):
  g,h,k=z['source'],arrows[z['first']]['target'],z['target']
  a,b,c=z['first'],z['second'],z['direct']
  f=localword(k,z['target_twist_word'])
  w=cat((edge[b],edge[a],-edge[c]),inv(f))
  triangle[i]=addrel('triangle_relator',w,{'triangle':i,'source':g,'middle':h,'target':k})
  triwords[i]=f
 open_face={}
 for i,a in arrows.items():
  g,h=a['source'],a['target']
  open_face[i]=addrel('open_face_relator',cat((t[h],edge[i],-t[g]),inv(q[i])),{'arrow':i,'source':g,'target':h})
 print(stem,'all lower-cell images certified',Counter(r['kind'] for r in rels),flush=True)
 def src_expanded(S):
  return red(x for c,j,e in S for x in c+(rels[j]['word'] if e>0 else inv(rels[j]['word']))+inv(c))
 def open_arrow_certificate(g,w):
  out=[];prefix=()
  for x in w:
   mu=MU[abs(x)-1];rid=open_arrow[g,abs(x)]
   out.append((prefix if x>0 else cat(prefix,inv(mu)),rid,1 if x>0 else -1))
   prefix=cat(prefix,mu if x>0 else inv(mu))
  assert src_expanded(out)==cat((t[g],),w,(-t[g],),inv(image(w)))
  return tuple(out)
 def mapped_sequence(S):
  out=[]
  for c,j,e in S:
   C=certs[rels[j]['certificate']]
   if e<0:C=F.inverse(C)
   out.extend(F.conjugate(image(c),C))
  return tuple(out)
 tetra=[];source_factors=0;target_factors=0
 for i,z in enumerate(data['triangles']):
  g,h,k=z['source'],arrows[z['first']]['target'],z['target']
  a,b,c=z['first'],z['second'],z['direct'];f=triwords[i];muf=image(f)
  rid=triangle[i];T=certs[rels[rid]['certificate']]
  delta=cat(muf,q[c],inv(q[a]),inv(q[b]))
  assert delta==inv(rels[rid]['target_word'])
  coherence=F.inverse(T);assert src_expanded(coherence)==delta
  S=F.conjugate((t[k],),[((),rid,1)])
  S+=open_arrow_certificate(k,f)
  S+=F.conjugate(muf,[((),open_face[c],1)])
  S+=coherence
  S+=F.inverse(F.conjugate(q[b],[((),open_face[a],1)]))
  S+=(((),open_face[b],-1),)
  assert src_expanded(S)==(),('source cone identity',i)
  mapped=mapped_sequence(S)
  assert mapped==T+F.inverse(T),('nonpaired mapped cone',i)
  assert F.reduce_sequence(mapped)==()
  assert F.expanded(mapped)==()
  source_factors+=len(S);target_factors+=len(mapped)
  tetra.append({'triangle':i,'flag':[g,h,k,'O'],'boundary_triangle_relator':rid,
                'boundary_triangle_certificate':rels[rid]['certificate'],
                'open_coherence_word':delta,'open_coherence_filler':coherence,
                'source_identity_sequence':S,'mapped_identity_sequence':mapped,
                'Peiffer_reduction':'successively cancel the middle adjacent pair in T inverse(T)',
                'map_of_selected_three_cell':'zero: its spherical map factors through the compact two-skeleton'})
 # Retain every local/sewing/triangle mapping-cylinder prism, with its disk.
 open_onecell={s:rid for (g,s),rid in open_arrow.items()}
 open_onecell.update({edge[i]:rid for i,rid in open_face.items()})
 prisms=[]
 for r in rels:
  if r['kind'] not in ('local_relator','sewing_relator','triangle_relator'):continue
  base=r.get('object',r.get('target'))
  C=[];prefix=()
  for x in r['word']:
   mu=MU[abs(x)-1]
   C.append((prefix if x>0 else cat(prefix,inv(mu)),open_onecell[abs(x)],1 if x>0 else -1))
   prefix=cat(prefix,mu if x>0 else inv(mu))
  assert src_expanded(C)==cat((t[base],),r['word'],(-t[base],),inv(r['target_word']))
  T=certs[r['certificate']]
  S=F.conjugate((t[base],),[((),r['id'],1)])+F.inverse(T)+F.inverse(C)
  assert src_expanded(S)==()
  mapped=mapped_sequence(S)
  assert mapped==T+F.inverse(T) and F.reduce_sequence(mapped)==()
  prisms.append({'boundary_relator':r['id'],'family':r['kind'],'base_vertex':base,
                 'source_identity_sequence':S,'mapped_factor_count':len(mapped),
                 'Peiffer_reduction':'T inverse(T) adjacent inverse cancellation'})
 counts={'objects_including_open':len(objects)+1,'oriented_one_cells':len(source_gens),
         'crossing_tree_edges':len(t),'one_vertex_generators_after_tree_collapse':len(source_gens)-len(t),
         'compact_relators':len(F.RELS),'source_relators':len(rels),
         'source_relator_types':dict(Counter(r['kind'] for r in rels)),
         'distinct_compact_certificates':len(certs),'certificate_factors':sum(len(C) for C in certs),
         'selected_cone_identities':len(tetra),'nonempty_triangle_certificates':sum(bool(certs[rels[triangle[i]]['certificate']]) for i in triangle),
         'source_cone_factors':source_factors,'mapped_cone_factors':target_factors,
         'boundary_two_cell_prisms':len(prisms),'seconds':time.time()-started}
 out={'type':data['type'],'compact_relators':F.RELS,'source_generators':source_gens,
      'source_vertices':['O']+list(objects),'source_relators':rels,'compact_certificates':certs,
      'cone_identities':tetra,'boundary_two_cell_prisms':prisms,'counts':counts,
      'scope':'Explicit coherent mapping-cylinder cellular comparison, retaining all lower cells and full local BG models. Every listed cone has a compact free-crossed-module identity and Peiffer cancellation. No finite positive-genus basis of the entire identity module or omission of other BG/product three-cells is asserted.',
      'chain_map':'one-cells use target_word; two-cells use the displayed conjugate-relator certificates; every selected cone and every lower-cell prism has the displayed spherical identity.',
      'simultaneous_choice':'For each closed triangle fix its certificate T; choose the corresponding open coherence disk as inverse(T). All such choices are made on distinct cell interiors. The resulting source identities are freely verified and map exactly to T inverse(T).'}
 (P/(stem+'.json')).write_text(json.dumps(out,separators=(',',':'))+'\n')
 print(stem,counts,flush=True)
 return out
if __name__=='__main__':
 if '--genus-two' in sys.argv:
  run(genus_two_data(),load('b_genus2_fill'),'d_genus_two_peiffer')
 else:
  run(elliptic_data(),load('d_artin_d4_fill'),'d_elliptic_three_peiffer')
