"""Full literal (1,3) flag complex: exact D4 words and named local groups.
All proofs of the geometric generators are recorded in the accompanying D section.
"""
from pathlib import Path
from itertools import permutations, combinations, combinations_with_replacement, product
from collections import Counter, deque
from functools import lru_cache
import ast,json,importlib.util
P=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('d4',P/'d_artin_d4.py');D=importlib.util.module_from_spec(spec);spec.loader.exec_module(D)
cat,inv,conj,eq=D.cat,D.inv,D.conj,D.equal
# Generic free-word functions, also used for words in each named local alphabet.
def comm(x,y):return cat(x,y,inv(x),inv(y))
def ev(w,images):return cat(*(images[abs(x)-1] if x>0 else inv(images[abs(x)-1]) for x in w))
# Universal named geometric words.
U={};UI={};UW=[]
def atom(name,w):
 U[name]=len(U)+1;UI[U[name]]=name;UW.append(tuple(w));return (U[name],)
A={i:atom('a'+str(i),(i,)) for i in (1,2,3)};B=atom('b',(4,))
H={i:atom('h'+str(i),(i,4)*3) for i in (1,2,3)}
SEP={};Q={};pairs={}
for i in (1,2,3):
 j,k=[x for x in (1,2,3) if x!=i];pairs[i]=(j,k)
 SEP[i]=atom('d'+str(i),(j,4,k)*4)
 Q[i]=atom('q'+str(i),(j,4,k,j,4,j))
D0=atom('D0',(1,4)*6)
DT1=atom('D1tail',cat(UW[D0[0]-1],inv(UW[SEP[3][0]-1]),inv(UW[SEP[2][0]-1])))
DTAIL={1:DT1,2:SEP[2],3:SEP[3]}
R={};distinguished={1:(3,2),2:(1,3),3:(1,2)}
for i,(j,k) in distinguished.items():R[i]=atom('r'+str(i),cat((k,-j),(j,4)*3))
S=atom('s',cat((1,4)*3,(-1,)))
NP={};NP[1,2]=atom('A12',cat(UW[S[0]-1],UW[S[0]-1]))
NP[1,3]=atom('A13',(2,-1));NP[1,4]=atom('A14',cat((-2,3),inv(UW[SEP[2][0]-1])))
NP[3,4]=atom('A34',UW[SEP[2][0]-1])
NP[2,3]=atom('A23',conj(UW[S[0]-1],UW[NP[1,3][0]-1]))
NP[2,4]=atom('A24',conj(UW[S[0]-1],UW[NP[1,4][0]-1]))
def gu(w):return ev(w,UW)
# Each group has a named presentation and its literal global generator images.
groups={}
def addgroup(name,gens,rels,extra=None):
 names=[x[0] for x in gens];univ=[x[1] for x in gens];images=[gu(x) for x in univ]
 groups[name]={'name':name,'generator_names':names,'universal_images':univ,'global_images':images,'relators':[tuple(r) for r in rels]}
 if extra:groups[name].update(extra)
 return groups[name]
def braidrels(i,j):return cat((i,j,i),inv((j,i,j)))
def zrels(n):return [comm((i,),(j,)) for i,j in combinations(range(1,n+1),2)]
# Nonseparating full group: PB4, the node half braid, central node, and Z4=a^-2.
BG={};tree=ast.parse((P/'b_genus_zero.py').read_text());exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'b_genus_zero','exec'),BG)
npairs=[(i,j) for j in range(2,5) for i in range(1,j)]
ngens=[('a',A[1]),('s',S)]+[('A%d%d'%p,NP[p]) for p in npairs]
nidx={p:3+k for k,p in enumerate(npairs)}
def pbe(w):return tuple(nidx[i,j]*e for i,j,e in w)
nrels=[cat((2,2),(-nidx[1,2],))]
for ell in (3,4):
 for i,j in combinations(range(1,ell),2):
  for k in range(1,ell):
   rhs=pbe(BG['comb'](ell,BG['A'](i,j)+BG['A'](k,ell)+BG['inv'](BG['A'](i,j))))
   nrels.append(cat((nidx[i,j],nidx[k,ell],-nidx[i,j]),inv(rhs)))
for i,j in npairs:
 rhs=pbe(BG['comb'](4,(1,)+BG['A'](i,j)+(-1,)))
 nrels.append(cat((2,nidx[i,j],-2),inv(rhs)))
nrels += [comm((1,),(j,)) for j in range(2,9)]
nrels.append(tuple(nidx[p] for p in npairs)+(1,1))
addgroup('N',ngens,nrels)
addgroup('S0',[('a',A[1]),('b',B),('d2',SEP[2]),('d3',SEP[3])],[braidrels(1,2)]+[comm((i,),(j,)) for i in (1,2) for j in (3,4)])
addgroup('L0',[('a',A[1]),('h',H[1]),('d2',SEP[2]),('d3',SEP[3])],[comm((i,),(j,)) for i,j in combinations(range(1,5),2) if (i,j)!=(3,4)])
for i in (1,2,3):
 j,k=pairs[i];l,m=distinguished[i]
 addgroup('S'+str(i),[('a'+str(j),A[j]),('b',B),('a'+str(k),A[k])],[braidrels(1,2),braidrels(2,3),comm((1,),(3,))])
 addgroup('L'+str(i),[('a'+str(l),A[l]),('a'+str(m),A[m]),('r',R[i])],[comm((1,),(2,)),comm((1,),(3,)),comm((3,3),(2,))])
 cg=[('a1',A[1]),('a2',A[2]),('a3',A[3]),('q',Q[i])]
 cr=zrels(3)+[cat((4,j,-4),(-k,)),cat((4,k,-4),(-j,)),cat((4,i,4,i),(-k,-j))]
 addgroup('C'+str(i),cg,cr)
 addgroup('C'+str(i)+'o',[('a1',A[1]),('a2',A[2]),('a3',A[3]),('d',SEP[i])],zrels(3)+[comm((4,),(j,)),comm((4,),(k,))])
 addgroup('T'+str(i),[('a',A[1]),('b',B),('d',DTAIL[i])],[braidrels(1,2),comm((1,),(3,)),comm((2,),(3,))])
 addgroup('F'+str(i),[('a',A[1]),('h',H[1]),('d',DTAIL[i])],zrels(3))
 addgroup('E'+str(i),[('a'+str(j),A[j]),('a'+str(k),A[k]),('q',Q[i])],[comm((1,),(2,)),cat((3,1,-3),(-2,)),cat((3,2,-3),(-1,))])
 addgroup('E'+str(i)+'o',[('a'+str(j),A[j]),('a'+str(k),A[k]),('d',SEP[i])],zrels(3))
addgroup('Theta',[('a1',A[1]),('a2',A[2]),('a3',A[3])],zrels(3))
# Exact stable graph edge positions, including the fixed puncture labels.
V={1:('N',[A[1]]),2:('S0',[D0]),3:('S3',[SEP[3]]),4:('S2',[SEP[2]]),5:('S1',[SEP[1]]),
 6:('L0',[D0,A[1]]),7:('C3',[A[1],A[2]]),8:('L3',[SEP[3],A[1]]),9:('C2',[A[1],A[3]]),10:('L2',[SEP[2],A[1]]),11:('L1',[A[3],SEP[1]]),12:('C1',[A[2],A[3]]),
 13:('T3',[SEP[3],D0]),14:('T2',[SEP[2],D0]),15:('T1',[DT1,D0]),
 16:('F3',[SEP[3],D0,A[1]]),17:('E3',[SEP[3],A[1],A[2]]),18:('F2',[SEP[2],D0,A[1]]),19:('E2',[SEP[2],A[1],A[3]]),20:('F1',[DT1,D0,A[1]]),21:('E1',[A[2],A[3],SEP[1]]),22:('Theta',[A[3],A[2],A[1]])}
AG={};tree=ast.parse((P/'a_graphs.py').read_text());AG.update(permutations=permutations,combinations_with_replacement=combinations_with_replacement,product=product,Counter=Counter)
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'a_graphs','exec'),AG)
graphs=[tuple((tuple(g[0]),tuple(g[1]),tuple(map(tuple,g[2])))) for g in json.loads((P/'a_graphs_1_3.json').read_text())['graphs']];gix={g:i for i,g in enumerate(graphs)}
def edge_group(g):
 gen,legs,edges=g;r=len(edges);out=set()
 for vp in permutations(range(len(gen))):
  if any(gen[i]!=gen[vp[i]] for i in range(len(gen))) or any(vp[x]!=x for x in legs):continue
  for ep in permutations(range(r)):
   if all(tuple(sorted((vp[a],vp[b])))==tuple(sorted(edges[ep[i]])) for i,(a,b) in enumerate(edges)):out.add(ep)
 return sorted(out)
def act(mask,p):return sum(1<<p[i] for i in range(len(p)) if mask>>i&1)
def mask_contract(g,mask):return gix[AG['contract'](graphs[g],[i for i in range(len(graphs[g][2])) if not(mask>>i&1)])]
EG={i:edge_group(graphs[i]) for i in V}
# Check every named generator acts on exactly the specified edge set.
for i,(name,curves) in V.items():
 for w in groups[name]['global_images']:
  perm=tuple(next(k for k,v in enumerate(curves) if eq(conj(w,gu(c)),gu(v))) for c in curves)
  assert perm in EG[i],(i,name,w,perm)
# q_i reverses the two parallel node edges; all other graph edge actions are trivial.
QPOOL=[((),None)]+[(gu(Q[i]),(i,1)) for i in (1,2,3)]+[(inv(gu(Q[i])),(i,-1)) for i in (1,2,3)]
@lru_cache(None)
def subset_transport(g,mask):
 h=mask_contract(g,mask);src=[(i,c) for i,c in enumerate(V[g][1]) if mask>>i&1];target=V[h][1]
 for q,tag in QPOOL:
  mp={};ok=True
  for i,c in src:
   found=[j for j,d in enumerate(target) if eq(conj(q,gu(c)),gu(d))]
   if len(found)!=1:ok=False;break
   mp[i]=found[0]
  if ok and len(set(mp.values()))==len(target):return h,q,tag,tuple(sorted(mp.items()))
 raise AssertionError(('missing subset transporter',g,mask,h))
for g in V:
 for m in range(1,1<<len(V[g][1])):subset_transport(g,m)
objects=[];objix={}
for g in V:
 r=len(V[g][1]);full=(1<<r)-1
 fs=[(full,)]+[(full,s) for s in range(1,full)]+[(full,s,t) for s in range(1,full) for t in range(1,s) if t&s==t]
 for flag in sorted({min(tuple(act(m,p) for m in f) for p in EG[g]) for f in fs}):
  name=V[g][0]
  if any(any(act(m,p)!=m for m in flag) for p in EG[g]):
   assert name[0] in 'CE';name+='o'
  o={'id':len(objects),'largest_graph':g,'retained_masks':flag,'vertex_graphs':[mask_contract(g,m) for m in flag],'group':name}
  objix[g,flag]=o['id'];objects.append(o)
assert [sum(len(o['retained_masks'])==k for o in objects) for k in (1,2,3)]==[22,53,33]
# Translate a face to the chosen representative of its full flag, not only its max vertex.
def face_transport(g,flag):
 h,q,tag,mp=subset_transport(g,flag[0]);mp=dict(mp)
 mapped=tuple(sum(1<<mp[k] for k in mp if m>>k&1) for m in flag)
 canon=min(tuple(act(m,p) for m in mapped) for p in EG[h])
 if mapped!=canon:
  name=V[h][0];assert name[0] in 'CE';i=int(name[1]);uq=gu(Q[i]);p=tuple(next(k for k,d in enumerate(V[h][1]) if eq(conj(uq,gu(c)),gu(d))) for c in V[h][1])
  assert tuple(act(m,p) for m in mapped)==canon
  q=cat(uq,q);tag=(('compose',(i,1),tag))
 return objix[h,canon],q,tag
arrows=[];arix={}
for o in objects:
 g=o['largest_graph'];flag=o['retained_masks'];n=len(flag)
 for bits in range(1,(1<<n)-1):
  sub=tuple(flag[i] for i in range(n) if bits>>i&1);t,q,tag=face_transport(g,sub)
  a={'id':len(arrows),'source':o['id'],'target':t,'selected_positions':bits,'transporter':q,'transporter_tag':tag}
  arix[o['id'],bits]=a['id'];arrows.append(a)
assert len(arrows)==304
coherences=[]
for o in objects:
 if len(o['retained_masks'])!=3:continue
 for ebits in (3,5,6):
  first=arrows[arix[o['id'],ebits]];mid=objects[first['target']]
  for vpos in (0,1):
   # Mid flag has been transported; identify the original retained graph by rank.
   second=arrows[arix[mid['id'],1<<vpos]]
   rank=objects[second['target']]['vertex_graphs'][0]
   orig=[j for j in range(3) if ebits>>j&1][vpos]
   direct=arrows[arix[o['id'],1<<orig]]
   assert second['target']==direct['target']
   twist=cat(second['transporter'],first['transporter'],inv(direct['transporter']))
   coherences.append({'source':o['id'],'first':first['id'],'second':second['id'],'direct':direct['id'],'target':direct['target'],'global_twist':twist})
assert len(coherences)==198
# Partial checkpoint, even before solving the target words.
base={'type':[1,3],'groups':groups,'universal_names':UI,'universal_global_words':UW,'vertices':V,'objects':objects,'arrows':arrows,'coherences':coherences,'counts':{'vertices':22,'edges':53,'triangles':33,'objects':108,'arrows':304,'coherences':198}}
(P/'d_p2_elliptic_three_structure.json').write_text(json.dumps(base,indent=2)+'\n')
print('All22 vertex representatives,28 named local groups,108 flag objects,304 exact transports,198 coherence words constructed.',flush=True)
print('Unique nonidentity global coherence words:',len({c['global_twist'] for c in coherences if not eq(c['global_twist'],())}),flush=True)
for name in sorted({objects[c['target']]['group'] for c in coherences if not eq(c['global_twist'],())}):
 words=sorted({c['global_twist'] for c in coherences if objects[c['target']]['group']==name and not eq(c['global_twist'],())})
 print('TWISTS',name,words,flush=True)
# Local inverses for the universal names, obtained from exact sewing identities.
recipes=[]
def recipe(dest,w):recipes.append((dest[0],tuple(w)))
for i in (1,2,3):
 j,k=pairs[i];l,m=distinguished[i]
 recipe(H[i],(A[i]+B)*3)
 recipe(SEP[i],(A[j]+B+A[k])*4)
 recipe(SEP[i],Q[i]*2)
 recipe(SEP[i],R[i]*2)
 recipe(Q[i],A[j]+B+A[k]+A[j]+B+A[j])
 recipe(R[i],cat(A[m],inv(A[l]),H[l]))
 recipe(H[l],cat(A[l],inv(A[m]),R[i]))
recipe(D0,H[1]*2)
recipe(DT1,cat(D0,inv(SEP[3]),inv(SEP[2])))
recipe(S,cat(H[1],inv(A[1])))
recipe(H[1],S+A[1])
recipe(A[2],NP[1,3]+A[1])
recipe(A[3],A[2]+NP[1,4]+SEP[2])
recipe(SEP[2],NP[3,4])
recipe(SEP[3],A[1]*2+NP[1,2]+NP[1,3]+NP[2,3])
recipe(DT1,A[1]*2+NP[1,2]+NP[1,4]+NP[2,4])
# Recipes hold in the exact global group, independently of any target group.
for dest,w in recipes:assert eq(UW[dest-1],gu(w)),('false recipe',UI[dest],w)
preimages={}
for name,g in groups.items():
 p={u[0]:(j+1,) for j,u in enumerate(g['universal_images']) if len(u)==1}
 changed=True
 while changed:
  changed=False
  for dest,w in recipes:
   if dest not in p and all(abs(x) in p for x in w):
    p[dest]=cat(*(p[abs(x)] if x>0 else inv(p[abs(x)]) for x in w));changed=True
 preimages[name]=p
 for dest,w in p.items():assert eq(ev(w,g['global_images']),UW[dest-1])
# Conjugate universal geometric generators using the actual q_i lift.
def q_transform_atom(i,sign,t):
 name=UI[t];j,k=pairs[i]
 if t==B[0]:return B
 for l in (1,2,3):
  if t==A[l][0]:
   if l==j:return A[k]
   if l==k:return A[j]
   if sign==1:return cat(A[j],A[k],inv(A[i]),inv(SEP[i]))
   return cat(A[j],A[k],inv(SEP[i]),inv(A[i]))
  if t==H[l][0] and l!=i:return H[k if l==j else j]
  if t==Q[l][0] and l==i:return Q[i]
  if t==SEP[l][0]:
   if l==i:return SEP[l]
   if l==1 and i in (2,3):
    if (i,sign) in ((2,1),(3,-1)):return DT1
    return cat(D0,inv(SEP[2]),inv(SEP[3]))
  if t==R[l][0]:
   u,v=distinguished[l]
   return q_transform(i,sign,cat(A[v],inv(A[u]),H[u]))
 if t==DT1[0] and (i,sign) in ((2,-1),(3,1)):return SEP[1]
 if t==D0[0]:return q_transform(i,sign,H[1]*2)
 raise KeyError(('unimplemented universal conjugation',i,sign,name))
def q_transform(i,sign,w):return cat(*(q_transform_atom(i,sign,abs(t)) if t>0 else inv(q_transform_atom(i,sign,abs(t))) for t in w))
def transformed(w,tag):
 if tag is None:return w
 if tag[0]=='compose':return transformed(transformed(w,tag[2]),tag[1])
 return q_transform(tag[0],tag[1],w)
image_count=0;missing=[]
for a in arrows:
 sg=groups[objects[a['source']]['group']];tn=objects[a['target']]['group'];tg=groups[tn];p=preimages[tn];local=[]
 for sn,uw,gw in zip(sg['generator_names'],sg['universal_images'],sg['global_images']):
  tw=transformed(uw,a['transporter_tag'])
  assert eq(gu(tw),conj(a['transporter'],gw)),('universal conjugation failed',a['id'],sn,tw)
  if not all(abs(t) in p for t in tw):missing.append((a['id'],objects[a['source']]['group'],tn,sn,[UI[abs(t)] for t in tw if abs(t) not in p]));continue
  lw=cat(*(p[abs(t)] if t>0 else inv(p[abs(t)]) for t in tw))
  assert eq(ev(lw,tg['global_images']),conj(a['transporter'],gw))
  local.append(lw);image_count+=1
 a['generator_images']=local
if missing:
 print('MISSING',missing,flush=True);raise AssertionError('local target word missing')
print('All304 arrows have explicit words for all',image_count,'source generators.',flush=True)
base['counts']['generator_images']=image_count
# Check every defining local relator in the faithful D4 quotient.
relator_count=0
for name,g in groups.items():
 for r in g['relators']:
  assert eq(ev(r,g['global_images']),()),('local relator',name,r);relator_count+=1
base['counts']['local_presentations']=len(groups);base['counts']['local_relators_checked']=relator_count
print('All',relator_count,'defining relators of28 complete local presentations verified.',flush=True)
# Save the fully named304 homomorphisms before the last coherence-word conversion.
(P/'d_p2_elliptic_three_maps.json').write_text(json.dumps(base,indent=2)+'\n')
# The six nonidentity global coherence values, with their literal target words.
twist_recipes={}
for i in (1,2,3):twist_recipes['C'+str(i)]=[(gu(Q[i]),(4,))]
ntarget=groups['N']['global_images'];np=preimages['N']
Nfirst=cat(gu(Q[3]),gu(Q[1]),inv(gu(Q[2])))
Nsecond=cat(gu(Q[2]),gu(Q[1]),inv(gu(Q[3])))
twist_recipes['N']=[(Nfirst,cat(np[H[1][0]],inv(np[SEP[2][0]]))),(Nsecond,cat(np[H[1][0]],inv(np[SEP[3][0]])))]
twist_recipes['S1']=[(gu(Q[1]),(1,2,3,1,2,1)),(cat(inv(gu(Q[2])),inv(gu(Q[3]))),(-3,-2,-3,1,2,3))]
for name,rr in twist_recipes.items():
 for globalword,localword in rr:assert eq(globalword,ev(localword,groups[name]['global_images']))
coherence_generator_checks=0
for c in coherences:
 name=objects[c['target']]['group'];tg=groups[name];f=c['global_twist']
 if eq(f,()):local=()
 else:
  matches=[lw for gw,lw in twist_recipes.get(name,[]) if eq(f,gw)];assert matches,('missing twist',name,f);local=matches[0]
 c['target_twist_word']=local
 a,b,direct=(arrows[c[k]] for k in ('first','second','direct'))
 # The middle group's indexed generators make this an actual word substitution.
 for w1,wd in zip(a['generator_images'],direct['generator_images']):
  left=ev(w1,b['generator_images']);right=conj(local,wd)
  assert eq(ev(left,tg['global_images']),ev(right,tg['global_images']))
  coherence_generator_checks+=1
 # The cone over the open stratum has this literal tetrahedral identity.
 assert cat(b['transporter'],a['transporter'])==cat(f,direct['transporter'])
base['counts']['coherence_generator_checks']=coherence_generator_checks
base['counts']['nonidentity_coherences']=sum(bool(c['target_twist_word']) for c in coherences)
base['counts']['open_cone_tetrahedra']=198
# Deterministic maximal tree using only arrows whose actual transport is the identity.
parent=list(range(len(objects)))
def find(i):
 while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
 return i
tree=[]
for a in arrows:
 if a['transporter']:continue
 u,v=find(a['source']),find(a['target'])
 if u!=v:parent[u]=v;tree.append(a['id'])
assert len(tree)==107 and len({find(i) for i in range(108)})==1
base['maximal_tree']=tree;base['counts']['maximal_tree_edges']=107
# Named inverse images of the compact four global generators.
vertices={o['largest_graph']:o['id'] for o in objects if len(o['retained_masks'])==1}
inverse_compact=[{'global_generator':j,'object':vertices[22],'local_generator':j} for j in (1,2,3)]+[{'global_generator':4,'object':vertices[2],'local_generator':2}]
for x in inverse_compact:assert eq(groups[objects[x['object']]['group']]['global_images'][x['local_generator']-1],(x['global_generator'],))
base['compact_inverse_generators']=inverse_compact
base['group_presentation_conventions']={'edge_relation':'t_a g_source t_a^-1 = psi_a(g)','triangle_relation':'t_b t_a = f_(b,a) t_(ba)','tree_relation':'t_a=1 for a in chosen maximal tree','map_to_global':'local generator maps to its named D4 word; t_a maps to its exact transporter'}
base['scope']='All vertex/flag groups,304 homomorphisms,198 twists,compact four-generator inverses and198 cone tetrahedra are supplied. A conversion to a minimal compact crossed-module identity basis is not asserted.'
(P/'d_p2_elliptic_three.json').write_text(json.dumps(base,indent=2)+'\n')
print('All198 coherence equations checked on',coherence_generator_checks,'generators;',base['counts']['nonidentity_coherences'],'have nonidentity twisting.',flush=True)
print('All198 open-stratum cone tetrahedra agree as freely reduced actual transporter words.',flush=True)
print('A107-edge identity-transport maximal tree and all4 compact inverse generators are supplied.',flush=True)
# A complete readable dictionary, alongside the machine-readable certificate.
def fmt(w,names):
 if not w:return '1'
 return ' '.join(names[abs(t)-1]+('^-1' if t<0 else '') for t in w)
lines=['# Full P2(1,3) complex of groups','', 'Global letters: a1,a2,a3,b; central quotient (a1 a2 a3 b)^3=1.','', '## Named local presentations','']
for name,g in groups.items():
 lines+=['### '+name,'','Generators: '+', '.join(g['generator_names'])+'.','']
 for n,w in zip(g['generator_names'],g['global_images']):lines.append('- '+n+' = '+fmt(w,['a1','a2','a3','b']))
 lines+=['','Relators (each equals1):','']+[str(k+1)+'. '+fmt(r,g['generator_names']) for k,r in enumerate(g['relators'])]+['']
lines+=['## All108 objects','','| ID | Largest graph | Retained masks | Group |','|---:|---:|---|---|']
for o in objects:lines.append('|%d|%d|%s|%s|'%(o['id'],o['largest_graph'],','.join(map(str,o['retained_masks'])),o['group']))
lines+=['','## All304 face homomorphisms','']
for a in arrows:
 so,to=objects[a['source']],objects[a['target']];sg,tg=groups[so['group']],groups[to['group']]
 lines+=['### Arrow %d: object%d → object%d'%(a['id'],a['source'],a['target']),'','Transport: '+fmt(a['transporter'],['a1','a2','a3','b'])+'.','']
 for n,w in zip(sg['generator_names'],a['generator_images']):lines.append('- '+n+' → '+fmt(w,tg['generator_names']))
 lines+=['']
lines+=['## All198 triangle twisting elements','','| First arrow | Second arrow | Direct arrow | Target object | Twisting word in target generators |','|---:|---:|---:|---:|---|']
for c in coherences:
 tg=groups[objects[c['target']]['group']]
 lines.append('|%d|%d|%d|%d|%s|'%(c['first'],c['second'],c['direct'],c['target'],fmt(c['target_twist_word'],tg['generator_names'])))
lines+=['','## Fundamental group presentation','','Use one copy of each object group and one letter t_a for each arrow. Impose t_a g t_a^-1=psi_a(g), t_b t_a=f_(b,a)t_(ba), and t_a=1 for the following tree arrows:','',', '.join(map(str,tree))+'.','','The map sends t_a to its displayed global transporter. Its inverse on a1,a2,a3 uses the correspondingly named generators at the Theta vertex; its inverse on b uses b at S0.','',base['scope'],'']
(P/'d_p2_elliptic_three_dictionary.md').write_text('\n'.join(lines))
