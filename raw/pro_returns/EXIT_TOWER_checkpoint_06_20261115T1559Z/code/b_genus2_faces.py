"""The19-cell genus-two P2 complex:42 injections and24 coherence triangles.
Every local generator is a literal B6 word. Every injection image is a word
in the target's named generators. Equality uses the faithful combination of
the sphere outer action and the genus-two symplectic representation.
"""
from pathlib import Path
import json,itertools
P=Path(__file__).parent
H={'__file__':str(P/'b_genus2_checks.py')}
exec((P/'b_genus2_checks.py').read_text().split('checks=[')[0],H)
cat,inv,conj=[H[k] for k in ('cat','inv','conj')]
def eq(u,v):
 w=cat(u,inv(v))
 return H['outer_identity'](w)[0] and H['symplectic'](w)==H['S'].eye(4)
a,b,c,W,e,t,u,v,q,h,td=[H[k] for k in ('a','b','cc','W','ee','t','u','v','q','hL','swap_dumbbell')]
global_groups={
 'N':dict(a=a,b=b,d=(4,),c=c,W=W),
 'S':dict(a=a,s=(2,),d=(4,),c=c,q=q,W=W),
 'B':dict(a=a,b=b,c=c,e=e,t=t,W=W),
 'L':dict(a=a,d=(4,),c=c,W=W),
 'Theta':dict(a=a,b=b,c=c,u=u,v=v,W=W),
 'D':dict(a=a,c=c,h=h,t=td,W=W),
 'H':dict(a=a,b=b,c=c,e=e,W=W),
 'TB':dict(a=a,b=b,c=c,u=u,W=W),
 'TN':dict(a=a,b=b,c=c,v=v,W=W),
 'AD':dict(a=a,c=c,h=h,W=W),
 'Z3W':dict(a=a,b=b,c=c,W=W),
}
cells={
 'N':('N',('N',)),'S':('S',('S',)),'B':('B',('B',)),
 'L':('L',('L',)),'Theta':('Theta',('Theta',)),'D':('D',('D',)),
 'BN':('H',('B','N')),'LN':('L',('L','N')),'LS':('L',('L','S')),
 'ThetaB':('TB',('Theta','B')),'ThetaN':('TN',('Theta','N')),
 'DB':('D',('D','B')),'DL':('AD',('D','L')),'DN':('AD',('D','N')),'DS':('D',('D','S')),
 'ThetaBN':('Z3W',('Theta','B','N')),
 'DBN':('AD',('D','B','N')),'DLN':('AD',('D','L','N')),'DLS':('AD',('D','L','S')),
}
def parse(expr):
 return tuple(expr.split()) if expr else ()
def evalword(expr,target):
 return cat(*(inv(target[x[1:]]) if x.startswith('-') else target[x] for x in expr))
def common(src,tgt):return {x:parse(x) for x in global_groups[src] if x in global_groups[tgt]}
maps={}
trans={}
def put(src,tgt,changes=None,transport=()):
 gs,gt=cells[src][0],cells[tgt][0]
 m=common(gs,gt)
 if changes:m.update({x:parse(w) for x,w in changes.items()})
 assert set(m)==set(global_groups[gs]),(src,tgt,set(global_groups[gs])-set(m))
 maps[src,tgt]=m;trans[src,tgt]=transport
put('BN','B')
put('BN','N',{'e':'-a c -b b d b d b d'})
put('LN','L');put('LN','N')
put('LS','L');put('LS','S')
put('ThetaB','Theta');put('ThetaB','B',{'u':'-c t'})
put('ThetaN','Theta');put('ThetaN','N',{'v':'b d c b d b -a'})
dbmap={'c':'b','h':'W a b -c e','t':'a -b -c t'}
put('DB','D');put('DB','B',dbmap,v)
put('DL','D');put('DL','L',{'h':'W d c d c d c'})
put('DN','D');put('DN','N',{'h':'W d c d c d c'})
put('DS','D');put('DS','S',{'h':'a s a s a s','t':'-s -a d c q'})
for target in ('ThetaB','ThetaN','BN','Theta','B','N'):put('ThetaBN',target)
for target in ('DB','DN','D'):put('DBN',target)
put('DBN','BN',{'c':'b','h':'W a b -c e'},v)
put('DBN','B',{'c':'b','h':'W a b -c e'},v)
put('DBN','N',{'h':'W d c d c d c'})
for target in ('DL','DN','D'):put('DLN',target)
for target in ('LN','L','N'):put('DLN',target,{'h':'W d c d c d c'})
for target in ('DL','DS','D'):put('DLS',target)
for target in ('LS','L'):put('DLS',target,{'h':'W d c d c d c'})
put('DLS','S',{'h':'a s a s a s'})
assert len(cells)==19 and len(maps)==42
records=[];nimages=0
for (source,target),m in maps.items():
 sg=global_groups[cells[source][0]];tg=global_groups[cells[target][0]]
 for x,expr in m.items():
  assert eq(evalword(expr,tg),conj(trans[source,target],sg[x])),(source,target,x)
  nimages+=1
 records.append(dict(source=source,target=target,transport=trans[source,target],images=m))
triangles=[];nontrivial=[]
for alpha,beta,gamma in itertools.permutations(cells,3):
 if (alpha,beta) not in maps or (beta,gamma) not in maps or (alpha,gamma) not in maps:continue
 if len(cells[alpha][1])!=3 or len(cells[beta][1])!=2 or len(cells[gamma][1])!=1:continue
 tw=v if (alpha,beta,gamma)==('DBN','BN','N') else ()
 mg=maps[beta,gamma];tg=global_groups[cells[gamma][0]]
 def compose(expr):
  words=[]
  for z in expr:
   im=mg[z[1:] if z.startswith('-') else z]
   bw=evalword(im,tg);words.append(inv(bw) if z.startswith('-') else bw)
  return cat(*words)
 for x,expr in maps[alpha,beta].items():
  assert eq(compose(expr),conj(tw,evalword(maps[alpha,gamma][x],tg))),(alpha,beta,gamma,x)
 triangles.append(dict(source=alpha,middle=beta,target=gamma,twist=tw))
 if tw:nontrivial.append((alpha,beta,gamma))
assert len(triangles)==24 and nontrivial==[('DBN','BN','N')]
print('Genus-two P2:19 cells (6 vertices,9 edges,4 triangles).')
print('Face injections:',len(maps),'generator images checked:',nimages)
print('Coherence triangles:',len(triangles),'nontrivial:',nontrivial)
print('The nontrivial twist in N is v=Delta4(3,4,5)*a^-1.')
out=dict(cells={k:dict(group=g,vertices=vs,generators=global_groups[g]) for k,(g,vs) in cells.items()},face_injections=records,coherence_triangles=triangles,counts=[19,42,nimages,24])
(P/'b_genus2_faces.json').write_text(json.dumps(out,indent=2)+'\n')
