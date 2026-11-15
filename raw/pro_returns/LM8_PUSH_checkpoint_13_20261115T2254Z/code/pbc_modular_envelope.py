#!/usr/bin/env python3
"""Build a faithful degree-288 modular envelope and a literal F'' candidate.

The induced representation uses the exact old marking x=(rs)^2,
y=(sr)^2.  Its candidate is a finite cycle residue only.
"""
from pathlib import Path
from itertools import permutations
import json

def gn(w):
    a=[]
    for x in w:
        if a and ((a[-1]==1)==(x==1)):
            y=a.pop()
            if x!=1:
                z=((y-1)+(x-1))%3
                if z:a.append(z+1)
        else:a.append(x)
    return tuple(a)
def gi(w):return tuple(1 if x==1 else 5-x for x in w[::-1])
def gm(a,b):return gn(a+b)
def mm(a,b,n):return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%n for i in range(2) for j in range(2))
def mi(a,n):return (a[3],-a[1]%n,-a[2]%n,a[0])
I=(1,0,0,1);S2=(0,1,1,0);R2=(0,1,1,1)
cos=[(I,())];ci={I:0}
for a,w in cos:
    for b,t in ((S2,1),(R2,2)):
        c=mm(a,b,2)
        if c not in ci:ci[c]=len(cos);cos.append((c,gn(w+(t,))))
assert len(cos)==6
gx=(2,1,2,1);gy=(1,2,1,2)
letters={1:gx,2:gy,-1:gi(gx),-2:gi(gy)}
words={():()}
front=[((),())]
for depth in range(6):
    nxt=[]
    for g,w in front:
        for j in (1,2,-1,-2):
            if w and w[-1]==-j:continue
            h=gm(g,letters[j]);v=w+(j,)
            words.setdefault(h,v);nxt.append((h,v))
    front=nxt
M=[(a,b,c,d) for a in range(4) for b in range(4) for c in range(4) for d in range(4) if (a*d-b*c)%4==1]
idx={a:i for i,a in enumerate(M)}
SX=(0,1,3,0);TY=(1,3,0,1)
def ew(w,x=SX,y=TY):
    g=I;gg={1:x,2:y,-1:mi(x,4),-2:mi(y,4)}
    for j in w:g=mm(g,gg[j],4)
    return g
perms=[]
for modg,t in ((S2,1),(R2,2)):
    p=[0]*288
    for k,(a,w) in enumerate(cos):
        j=ci[mm(a,modg,2)]
        ret=gm(gm(w,(t,)),gi(cos[j][1]))
        fw=words[ret];val=ew(fw)
        for h,b in enumerate(M):p[k*48+h]=j*48+idx[mm(b,val,4)]+1
    perms.append(p)
def pp(a,b):return [b[x-1] for x in a]
ID=list(range(1,289))
assert pp(perms[0],perms[0])==ID
assert pp(pp(perms[1],perms[1]),perms[1])==ID

# A word in the second derived subgroup representing the desired residue.
tr=(SX,TY,mi(mm(SX,TY,4),4));pairs=list(permutations(tr,2))
TID=(I,)*6
def tm(a,b):return tuple(mm(x,y,4) for x,y in zip(a,b))
def ti(a):return tuple(mi(x,4) for x in a)
def tc(a,b):return tm(tm(a,b),ti(a))
def comm(a,b):return tm(tm(a,b),tm(ti(a),ti(b)))
X=tuple(a for a,b in pairs);Y=tuple(b for a,b in pairs)
C=comm(X,Y)
def vec(a):
    r=0
    for i,b in enumerate(a):
        assert b[0]%2==1 and b[1]%2==0 and b[2]%2==0 and b[3]%2==1
        d=(b[0]-1)//2;u=b[1]//2;l=b[2]//2
        assert (b[3]-1)//2==d
        r|=(d|(u<<1)|(l<<2))<<(3*i)
    return r
def fw_inv(w):return tuple(-a for a in w[::-1])
def fw_com(a,b):return a+b+fw_inv(a)+fw_inv(b)
cword=(1,2,-1,-2)
conjugates=[(TID,())]
for depth in range(3):
    old=list(conjugates)
    for g,w in old:
        for h,j in ((X,1),(Y,2),(ti(X),-1),(ti(Y),-2)):
            conjugates.append((tm(g,h),w+(j,)))
basis={}
for g,w in conjugates:
    value=comm(C,tc(g,C));word=fw_com(cword,w+cword+fw_inv(w));v=vec(value)
    for b in sorted(basis,reverse=True):
        if v>>b&1:v^=basis[b][0];word+=basis[b][1]
    if v:basis[v.bit_length()-1]=(v,word)
rows=json.loads(Path('LM8_PUSH/code/pbc_descent_cycle4.json').read_text())['rows']
target=next(r for r in rows if r['f']==43094540840)
tv=vec(tuple(tuple(a) for a in target['six_f']));outword=()
for b in sorted(basis,reverse=True):
    if tv>>b&1:tv^=basis[b][0];outword+=basis[b][1]
assert tv==0
# A shorter certificate found by breadth-first search in the 12-dimensional
# elementary abelian second derived image:
# [c,ycy^-1] [c,(yx)c(yx)^-1] [c,(x^-1 y^2)c(x^-1 y^2)^-1].
outword=()
for conjugator in ((2,),(2,1),(-1,2,2)):
    outword+=fw_com(cword,conjugator+cword+fw_inv(conjugator))
reduced=[]
for letter in outword:
    if reduced and reduced[-1]==-letter:reduced.pop()
    else:reduced.append(letter)
outword=tuple(reduced)
assert all(sum(1 if j==k else -1 if j==-k else 0 for j in outword)==0 for k in (1,2))
check=tuple(ew(outword,a,b) for a,b in pairs)
assert check==tuple(tuple(a) for a in target['six_f'])
def gapword(w):
    if not w:return 'One(G)'
    return '*'.join({1:'x',2:'y',-1:'x^-1',-2:'y^-1'}[j] for j in w)
dest=Path('LM8_PUSH/code/pbc_modular_envelope.g')
dest.write_text('s:=PermList('+str(perms[0])+');;\nr:=PermList('+str(perms[1])+');;\nG:=Group(s,r);;\nx:=(r*s)^2;; y:=(s*r)^2;;\nf:='+gapword(outword)+';;\nPrint("group_order ",Size(G),"\\n");\nPrint("candidate_order ",Order(f),"\\n");\nPrint("torsion_and_cusp ",Order(s*f^-1)," ",Order(f*r)," ",s*f^-1*f*r=s*r,"\\n");\na:=GroupHomomorphismByImages(G,G,[s,r],[s*f^-1,f*r]);;\nPrint("automorphism ",a<>fail and IsBijective(a),"\\n");\npciso:=IsomorphismPcGroup(G);; P:=Image(pciso);;\nPrint("pc_order ",Size(P),"\\n");\nPrint("pc_generators ",Length(Pcgs(P)),"\\n");\nPrint("schur_multiplier ",AbelianInvariantsMultiplier(P),"\\n");\nQUIT;\n')
out=dict(degree=288,source_relations_verified=True,second_derived_span_dimension=len(basis),
         candidate_word_length=len(outword),candidate_word=list(outword),
         target_six_f=target['six_f'],gap_input=str(dest),
         scope='Exact induced representation and finite candidate; full lifting not asserted')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('candidate_word','target_six_f')},indent=2))
