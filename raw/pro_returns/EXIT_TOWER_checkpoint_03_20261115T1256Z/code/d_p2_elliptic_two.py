#!/usr/bin/env python3
"""All fifteen orbit cells, face injections and twists for P2 of S1,2."""
from pathlib import Path
from itertools import combinations
from collections import deque
import ast,json
P=Path(__file__).resolve().parent
tree=ast.parse((P/'b_genus_zero.py').read_text())
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef)],type_ignores=[]),'b_genus_zero.py','exec'),globals())

def word(*x):return tuple(x)
def comm(a,b):return a+b+inv(a)+inv(b)
def relation(a,b):return a+inv(b)
a,b,c=(1,),(2,),(3,)
h=(1,2)*3;q=(1,2,3)*2;s=(1,2,1);Delta=(1,2,3,1,2,1);r=inv(s)+Delta+s
emb={'O':{'a':a,'b':b,'c':c},'N':{'a':a,'c':c,'r':r},'T':{'a':a,'b':b},
     'D':{'a':a,'h':h},'C':{'a':a,'c':c,'q':q},'A':{'a':a,'c':c}}
gens={g:list(e) for g,e in emb.items()}
def expand_named(g,w):return red(x for name,e in w for x in (emb[g][name] if e==1 else inv(emb[g][name])))
def named(s):return [(x,1) for x in s]
def ni(w):return [(x,-e) for x,e in reversed(w)]
def nc(a,b):return a+b+ni(a)+ni(b)
def nr(a,b):return a+ni(b)
na,nb,nc_=[named(x) for x in ('a','b','c')];nh,nq,nr_=[named(x) for x in ('h','q','r')]
rels={'O':[nc(na,nc_),nr(na+nb+na,nb+na+nb),nr(nb+nc_+nb,nc_+nb+nc_),(na+nb+nc_)*4],
      'N':[nc(na,nc_),nc(na,nr_),nr_*2], 'T':[nr(na+nb+na,nb+na+nb)],
      'D':[nc(na,nh)],'C':[nc(na,nc_),nq*2,nr(nq+na+ni(nq),nc_)],'A':[nc(na,nc_)]}
def trivial(w):
    exponent=sum(1 if x>0 else -1 for x in w)
    assert exponent%12==0,w
    return eq(4,w,pw(full(4),exponent//12))
for g,rr in rels.items():
    for rr0 in rr:assert trivial(expand_named(g,rr0))
assert eq(4,h,a+inv(c)+r)
cells=[(('O',),'O'),(('N',),'N'),(('T',),'T'),(('D',),'D'),(('C',),'C'),
       (('D','N'),'D'),(('D','T'),'D'),(('C','N'),'A'),(('N','O'),'N'),
       (('T','O'),'T'),(('D','O'),'D'),(('C','O'),'C'),
       (('D','N','O'),'D'),(('D','T','O'),'D'),(('C','N','O'),'A')]
def image(s,t,x):
    if s==t:return named(x)
    if t=='O':return [(('a','b','c')[abs(k)-1],1 if k>0 else -1) for k in emb[s][x]]
    if s=='D' and t=='N':return named('a') if x=='a' else [('a',1),('c',-1),('r',1)]
    if s=='D' and t=='T':return named('a') if x=='a' else named('ab')*3
    if s=='A' and t in ('N','C'):return named(x)
    raise ValueError((s,t,x))
arrows=[];arrow={};count=0
for i,(ci,gi) in enumerate(cells):
    for j,(cj,gj) in enumerate(cells):
        if not set(cj)<set(ci):continue
        inj={x:image(gi,gj,x) for x in gens[gi]}
        for x,z in inj.items():
            assert trivial(expand_named(gi,named(x))+inv(expand_named(gj,z)))
            count+=1
        arrow[i,j]=inj;arrows.append({'source':i,'target':j,'injections':inj,'transporter':[]})
triangles=[]
for i,j in arrow:
    for jj,k in arrow:
        if jj!=j:continue
        gi=cells[i][1];gj=cells[j][1];gk=cells[k][1]
        for x in gens[gi]:
            a=arrow[i,j][x]
            composite=[]
            for y,e in a:composite+=arrow[j,k][y] if e==1 else ni(arrow[j,k][y])
            assert trivial(expand_named(gk,composite)+inv(expand_named(gk,arrow[i,k][x])))
        triangles.append({'vertices':[i,j,k],'twisting_element':[]})
adj={i:[] for i in range(len(cells))}
for i,j in arrow:adj[i].append(j);adj[j].append(i)
seen={0};queue=deque([0]);span=[]
while queue:
 i=queue.popleft()
 for j in sorted(adj[i]):
  if j not in seen:seen.add(j);queue.append(j);span.append([i,j])
assert len(seen)==15
data={'type':[1,2],'groups':{g:{'generators':gens[g],'relators':rels[g],'braid_embeddings':emb[g]} for g in emb},
      'cells':[{'id':i,'flag':ci,'group':gi} for i,(ci,gi) in enumerate(cells)],
      'arrows':arrows,'triangles':triangles,'maximal_tree':span,
      'inverse_open_generators':{'a':{'cell':1,'generator':'a'},'b':{'cell':2,'generator':'b'},'c':{'cell':1,'generator':'c'}},
      'counts':{'orbit_cells':len(cells),'face_arrows':len(arrows),'face_triangles':len(triangles),'generator_images':count,'tree_edges':len(span)}}
(P/'d_p2_elliptic_two.json').write_text(json.dumps(data,indent=2)+'\n')
print('M1,2 full P2 barycentric certificate:',data['counts'])
print('All local relators, face generator images and composite maps verified in B4/<Delta4^2>.')
print('All transports and all triangle twists are identity.  CN and CNO use the proper index-two group A=<a,c>.')
