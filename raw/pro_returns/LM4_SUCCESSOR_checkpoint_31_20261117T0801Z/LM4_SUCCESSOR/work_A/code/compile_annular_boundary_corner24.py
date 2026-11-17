#!/usr/bin/env python3
"""Actual boundary-corner Tietze data; exact free/dihedral reductions only.

No quotient solver and no assertion that the isolated corner injects into
the final group. The replacement of generic relators is proved in the
companion note, including the two explicit k/d,e commutations.
"""
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parents[2]
src=ROOT/'work_A/annular_mirror_fold23.json'
data=json.loads(src.read_text())

def old_reduce(w):
    ans=[]
    for x in w:
        if abs(x)<=7:x=abs(x)
        if ans and (ans[-1]==-x or abs(x)<=7 and ans[-1]==x):ans.pop()
        else:ans.append(x)
    return tuple(ans)

def new_reduce(w):
    # Free product: D_infinity(j,u) * C2(r1)*...*C2(r4)*C2(D)*Z(k).
    # Each dihedral block is u^n j^eps, multiplication (n,e)(m,f)
    # = (n+(-1)^e*m,e+f).
    blocks=[]
    for x in w:
        ax=abs(x)
        if ax==1:tag,val='dih',(0,1)
        elif ax==7:tag,val='dih',((1 if x>0 else -1),0)
        elif 2<=ax<=6:tag,val=ax,1
        elif ax==8:tag,val=8,(1 if x>0 else -1)
        else:raise AssertionError(x)
        if blocks and blocks[-1][0]==tag:
            _,prev=blocks.pop()
            if tag=='dih':
                val=(prev[0]+(-1 if prev[1] else 1)*val[0],prev[1]^val[1])
                zero=val==(0,0)
            elif tag==8:
                val=prev+val;zero=val==0
            else:zero=True
            if not zero:blocks.append((tag,val))
        else:blocks.append((tag,val))
    ans=[]
    for tag,val in blocks:
        if tag=='dih':
            ans.extend(([7] if val[0]>0 else [-7])*abs(val[0]))
            if val[1]:ans.append(1)
        elif tag==8:ans.extend(([8] if val>0 else [-8])*abs(val))
        else:ans.append(tag)
    return tuple(ans)

def inv(w,red):return red(-x for x in reversed(w))
def mul(*words,red):return red(x for w in words for x in w)
def sub(w,images,red):
    return red(y for x in w for y in (images[abs(x)] if x>0 else inv(images[-x],red)))
def comm(v,w,red):return mul(v,w,inv(v,red),inv(w,red),red=red)

# New: 1=j, 2..5=r1..r4, 6=D=j c_gap j, 7=u=T D, 8=k.
j=(1,);D=(6,);u=(7,);k=(8,)
a_old=(2,3)
c_old=mul(a_old,(7,),inv(a_old,old_reduce),red=old_reduce)
P5_old=(1,6)
T_old=mul(c_old,P5_old,red=old_reduce)
D_old=mul((1,),c_old,(1,),red=old_reduce)
u_old=mul(T_old,D_old,red=old_reduce)
new_to_old={1:(1,),2:(2,),3:(3,),4:(4,),5:(5,),6:D_old,7:u_old,8:(8,)}
a=(2,3)
old_to_new={i:(i,) for i in range(1,6)}
old_to_new.update({
    6:mul(D,j,u,D,red=new_reduce),
    7:mul(inv(a,new_reduce),j,D,j,a,red=new_reduce),
    8:k,
})
for i in range(1,9):
    assert sub(new_to_old[i],old_to_new,new_reduce)==(i,)
    assert sub(old_to_new[i],new_to_old,old_reduce)==(i,)

K={int(i):sub(w,old_to_new,new_reduce)
   for i,w in data['common_adapted_K_in_fold'].items()}
a,B,d,e,f=(K[i] for i in range(1,6))
C=old_to_new[7]
b=mul(C,B,C,red=new_reduce)
h=mul(f,k,red=new_reduce)
z=mul(C,h,red=new_reduce)
c=mul(a,C,inv(a,new_reduce),red=new_reduce)
P5=mul(a,B,f,d,e,red=new_reduce)
T=mul(c,P5,red=new_reduce)
assert c==mul(j,D,j,red=new_reduce)
assert P5==mul(j,D,j,u,D,red=new_reduce)
assert T==mul(u,D,red=new_reduce)
assert mul(j,P5,j,red=new_reduce)==inv(P5,new_reduce)
assert mul(j,u,j,red=new_reduce)==inv(u,new_reduce)

# Both original characters are retained. Original epsilon(D)=1,
# epsilon(u)=0; mirror parity is 1 on j,r1..r4 only.
eps=lambda w:sum(abs(x)==6 for x in w)%2
mirror=lambda w:sum(1<=abs(x)<=5 for x in w)%2
for i in range(1,9):
    assert eps(old_to_new[i])==(1 if i==7 else 0)
    assert mirror(old_to_new[i])==(1 if i<=6 else 0)

rels=[{'name':f'{i}_square','word':(i,i)} for i in range(1,7)]
rels += [
    {'name':'mirror_inverts_u','word':(1,7,1,7)},
    {'name':'k_fixes_D','word':comm(k,D,new_reduce)},
    {'name':'k_fixes_u','word':comm(k,u,new_reduce)},
]
rels += [{'name':'C_fixes_z','word':comm(C,z,new_reduce)}]
rels += [{'name':'k_fixes_'+name,'word':comm(k,w,new_reduce)}
         for name,w in [('a',a),('b',b),('d',d),('e',e)]]
bar=lambda w:mul(C,w,C,red=new_reduce)
pairs=[('diagonal_'+name,w,bar(w)) for name,w in [('a',a),('b',b),('d',d),('e',e)]]
pairs += [('pair_ab',a,b),('pair_bara_d',bar(a),d),
          ('pair_bara_e',bar(a),e),('pair_d_bare',d,bar(e)),
          ('pair_b_fdf',b,mul(f,d,inv(f,new_reduce),red=new_reduce)),
          ('pair_b_fef',b,mul(f,e,inv(f,new_reduce),red=new_reduce))]
rels += [{'name':name,'word':comm(v,w,new_reduce)} for name,v,w in pairs]
assert len(rels)==24
assert all(all(abs(x)!=8 for x in row['word']) for row in rels[-10:])

direct={row['name']:sub(row['word'],old_to_new,new_reduce) for row in data['relators']}
# These are literal equalities, before adding any non-dihedral relation.
assert direct['h_fixes_cone']==rels[9]['word']
for row in rels[10:14]:assert direct[row['name']]==row['word']
for row in rels[14:22]:assert direct[row['name']]==row['word']
assert direct['single_folded_cross']==comm(D,k,new_reduce)

# The whole-boundary proof is the explicit two-commutation sequence
# a b z k^-1 d e -> a b z d k^-1 e -> a b z d e k^-1.
# Use abstract labels a,b,z,k,d,e=1..6 here.
boundary_moves=[(1,2,3,-4,5,6),(1,2,3,5,-4,6),(1,2,3,5,6,-4)]
for v,w in zip(boundary_moves,boundary_moves[1:]):
    changed=[i for i in range(len(v)) if v[i]!=w[i]]
    assert len(changed)==2 and changed[1]==changed[0]+1
    i=changed[0]
    assert v[i:i+2]==w[i:i+2][::-1]
    assert -4 in v[i:i+2] and set(abs(x) for x in v[i:i+2]) in ({4,5},{4,6})

sources=[]
for row in data['actual_six_source_words']:
    w=sub(row['word'],old_to_new,new_reduce)
    assert eps(w)==mirror(w)==0
    sources.append({**row,'word':w})

out={'status':'PASS_ACTUAL_BOUNDARY_CORNER_TIEZE_DATA',
     'input_path':str(src.relative_to(ROOT)),
     'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
     'generators':{1:'j',2:'r1',3:'r2',4:'r3',5:'r4',6:'D',7:'u',8:'k'},
     'old_to_new':old_to_new,'new_to_old':new_to_old,
     'generator_inverse_checks':16,
     'corner_words':{'c_gap':c,'P5':P5,'T':T,'D':D,'u':u},
     'actual_regional_words':{'a':a,'B':B,'b':b,'C':C,'d':d,'e':e,'f':f,'h':h,'z':z},
     'boundary_commutation_steps':boundary_moves,
     'literal_relation_comparisons':14,
     'relators':rels,'relator_count':24,
     'transformed_original_relators':direct,
     'actual_six_source_words':sources,
     'source_word_lengths':[len(row['word']) for row in sources],
     'scope':'Exact actual presentation change. The old h-swaps-k relation is replaced using the printed boundary identity and four k/U commutations; the last two node words use those same k/d,e relations. No corner injection or post-cross centralizer is asserted.'}
(ROOT/'work_A/annular_boundary_corner24.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all16 free/dihedral generator inverse compositions')
print('PASS selected c, P5, T=uD and exact mirror-inversion identities')
print('PASS literal retained relation comparisons and both characters')
print('PASS two boundary commutation steps; all10 new node words avoid k')
print('PASS exact24-relator presentation data; six source lengths',out['source_word_lengths'])
print('Scope: full transformed relations retained; no corner-injection claim')
