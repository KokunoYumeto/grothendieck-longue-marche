"""Exact finite multiplication-gadget colimits of framed 3/4-point pieces.
Every noncentral arrow map has target F2 and is recorded generator by
generator. Elimination gives the supplied central presentation, with
explicit forward and inverse dictionaries. Geometric paths are B.28--29.
"""
from pathlib import Path
import json
P=Path(__file__).resolve().parent
H={};exec((P/'b_genus_zero.py').read_text().split('\ndata={}')[0],H)
red,inv,eq=H['red'],H['inv'],H['eq']
def compile_diagram(name,r,n,relations,braids=None,strands=None,central_braid=None):
 zero=(0,)*r;nodes=[dict(id='C',kind='trinion',rank=r),dict(id='K',kind='trinion',rank=r)]
 arrows=[dict(source='C',target='K',name='central_identity',images=[])]
 values={};constraints=[];gadgets=[]
 def variable(v,w):
  nodes.append(dict(id=v,kind='four_point',rank=r,role='variable'))
  values[v]=tuple(w)
  arrows.append(dict(source='C',target=v,name='central_inclusion',images=[]))
  arrows.append(dict(source=v,target=v,name='idempotent_retraction',images=[dict(word=[1],central=zero),dict(word=[],central=zero)]))
 for i in range(1,n+1):variable('x'+str(i),(i,))
 for j,(rel,c) in enumerate(relations,1):
  w=red(rel);assert len(c)==r
  if not w:assert c==zero;continue
  prefix=();previous='p%d_0'%j;variable(previous,())
  arrows.append(dict(source=previous,target='K',name='initial_value',images=[dict(word=[],central=zero),dict(word=[],central=zero)]))
  for k,letter in enumerate(w,1):
   current='p%d_%d'%(j,k);prefix=red(prefix+(letter,));variable(current,prefix)
   mid='M%d_%d'%(j,k);nodes.append(dict(id=mid,kind='four_point',rank=r,role='multiplication'))
   arrows.append(dict(source='C',target=mid,name='central_inclusion',images=[]))
   maps=[(previous,[1]),('x'+str(abs(letter)),[2 if letter>0 else -2]),(current,[1,2])]
   for source,targetword in maps:
    arrows.append(dict(source=source,target=mid,name='multiplication_incidence',images=[dict(word=targetword,central=zero),dict(word=[],central=zero)]))
   gu=values[previous];gv=(letter,)
   for source,targetword in maps:
    image=red(x for t in targetword for x in ((gu if t==1 else inv(gu) if t==-1 else gv if t==2 else inv(gv))))
    assert image==values[source],(source,mid,image,values[source])
   gadgets.append(dict(block=mid,left=previous,right='x'+str(abs(letter)),right_sign=1 if letter>0 else -1,output=current,global_generator_images=[gu,gv]))
   previous=current
  arrows.append(dict(source=previous,target='K',name='terminal_value',images=[dict(word=[],central=c),dict(word=[],central=zero)]))
  constraints.append(dict(variable=previous,word=values[previous],central=c))
  assert values[previous]==w
  if braids is not None:
   bw=red(x for t in w for x in (braids[abs(t)-1] if t>0 else inv(braids[abs(t)-1])))
   rhs=() if central_braid is None else central_braid(c)
   assert eq(strands,bw,rhs),(name,j)
 # All idempotents fix the first generator and kill the second; all outgoing
 # incidence/evaluation maps kill the second generator, so f r=f exactly.
 for a in arrows:
  if a['images']:assert a['images'][1]['word']==[] and tuple(a['images'][1]['central'])==zero
 counts=dict(trinion_blocks=sum(v['kind']=='trinion' for v in nodes),four_point_blocks=sum(v['kind']=='four_point' for v in nodes),multiplication_blocks=len(gadgets),relations=len(constraints),explicit_arrows=len(arrows),objects_per_block=2**r)
 out=dict(type=name,central_rank=r,generators=n,relations=[dict(word=w,central=c) for w,c in relations],nodes=nodes,arrows=arrows,gadgets=gadgets,constraints=constraints,forward_variables=values,inverse_generators={str(i):'x'+str(i)+'.t' for i in range(1,n+1)},counts=counts)
 print(name,counts,flush=True)
 return out
c=lambda u,v:inv(v)+inv(u)+v+u
a=(1,);b=(2,);x=(3,);y=(4,);z=(5,)
compact=[red(a+x+inv(a)+inv(inv(z)+x+z)),red(a+y+inv(a)+inv(c(x,z)+y+inv(c(x,z)))),red(a+z+inv(a)+inv(c(x,z)+z)),red(b+x+inv(b)+inv(x)),red(b+y+inv(b)+inv(inv(z)+y+z)),red(b+z+inv(b)+inv(c(y,z)+z))]
data={}
data['0,3']=compile_diagram('0,3',3,0,[])
data['0,4']=compile_diagram('0,4',4,2,[])
data['0,5']=compile_diagram('0,5',5,5,[(w,(0,)*5) for w in compact],[H['A'](1,3),H['A'](2,3),H['A'](1,4),H['A'](2,4),H['A'](3,4)],4)
data['1,1']=compile_diagram('1,1',1,2,[((1,2,1,-2,-1,-2),(0,)),((1,2)*6,(1,))],[(1,),(2,)],3,lambda c:H['full'](3)*(2*c[0]))
data['1,2']=compile_diagram('1,2',2,3,[((1,2,1,-2,-1,-2),(0,0)),((2,3,2,-3,-2,-3),(0,0)),((1,3,-1,-3),(0,0)),((1,2,3)*4,(1,1))],[(1,),(2,),(3,)],4,lambda c:H['full'](4) if c==(1,1) else ())
(P/'b_sphere_colimit.json').write_text(json.dumps(data,indent=2)+'\n')
print('All variable substitutions, multiplication incidence maps, terminal relators and low-type braid images verified.')
