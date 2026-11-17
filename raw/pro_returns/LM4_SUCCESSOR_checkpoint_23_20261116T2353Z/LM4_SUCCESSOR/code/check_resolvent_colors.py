"""Enumerate the exact quotient and cusp-color counts for the P5 attempt.

Conventions: permutation product a*b means a after b. Every map is
tracked from the same words s,r. No group-theoretic or lifting conclusion
is inferred from the finite counts alone.
"""
from collections import deque,Counter
from itertools import permutations
import json
from pathlib import Path
P=Path(__file__).resolve().parents[1]
S3=list(permutations(range(3)));ii={x:i for i,x in enumerate(S3)}
I3=(0,1,2);I30=tuple(range(30));S=(1,0,2);R=(1,2,0)
def mul(a,b):return tuple(a[b[i]] for i in range(len(a)))
def inv(a):return tuple(a.index(i) for i in range(len(a)))
def powp(a,n):
 b=tuple(range(len(a)))
 for _ in range(n):b=mul(b,a)
 return b
def ind(base,local):return tuple(6*base[i]+ii[mul(local.get(i,I3),g)] for i in range(5) for g in S3)
s=ind((1,0,3,2,4),{4:S});rp=ind((2,1,4,3,0),{1:R});rm=ind((2,1,4,3,0),{3:R})
gens=[(s,s,S,'s'),(rp,rm,R,'r')]
G=[I30];by={I30:0};minus=[I30];orig=[I3];words=[''];todo=deque([0])
while todo:
 i=todo.popleft()
 for gp,gm,go,letter in gens:
  a=mul(G[i],gp);b=mul(minus[i],gm);c=mul(orig[i],go)
  if a in by:
   j=by[a];assert minus[j]==b and orig[j]==c
  else:
   by[a]=len(G);G.append(a);minus.append(b);orig.append(c);words.append(words[i]+letter);todo.append(len(G)-1)
assert len(G)==29160
print('Q order',len(G),'both resolvents and original S3 factor through Q')
tau=mul(s,rp);taum=mul(s,rm);tauo=mul(S,R)
taus=[powp(tau,k) for k in range(10)];taums=[powp(taum,k) for k in range(10)];assert taus[-1]!=I30 and powp(tau,10)==I30
fixo=next(i for i in range(3) if tauo[i]==i)
def base(a,i):return a[6*i]//6
def local(a,i):
 assert base(a,i)==i
 return S3[a[6*i+ii[I3]]%6]
tp=local(taus[5],4);tm=local(taums[5],4)
fp=next(i for i in range(3) if tp[i]==i);fm=next(i for i in range(3) if tm[i]==i)
def color(i,which):
 if which=='original':return orig[i][fixo]
 a=G[i] if which=='plus' else minus[i];ts=taus if which=='plus' else taums
 k=next(k for k in range(5) if base(mul(a,ts[k]),4)==4)
 j=mul(a,ts[k]);return local(j,4)[fp if which=='plus' else fm]
colors={name:[color(i,name) for i in range(len(G))] for name in ['original','plus','minus']}
# Actual cusp classes are right cosets Q/<tau>; identify by enumeration.
cosets=[];coset_of=[-1]*len(G)
for i,g in enumerate(G):
 if coset_of[i]>=0:continue
 members=[by[mul(g,t)] for t in taus];assert len(set(members))==10
 c=len(cosets);cosets.append(members)
 for j in members:
  assert coset_of[j] in [-1,c];coset_of[j]=c
  for name in colors:assert colors[name][j]==colors[name][i]
assert len(cosets)==2916
print('Cusps',len(cosets),'stabilizer order10')
for name,v in colors.items():print(name,'cusp color counts',dict(Counter(v[c[0]] for c in cosets)))
# A pair starts at identity cusp and has the same original color.
h=next(i for i in range(len(G)) if coset_of[i]!=coset_of[0] and colors['original'][i]==colors['original'][0] and colors['plus'][i]!=colors['plus'][0])
print('Selected pair Q/<tau>: 1 and h; h word',words[h],'; h index',h)
print('Pair colors',{name:[v[0],v[h]] for name,v in colors.items()})
results={}
for name,v in colors.items():
 counts=Counter((v[i],v[by[mul(g,G[h])]]) for i,g in enumerate(G))
 # Check each individual cusp, rather than infer integral incidence from
 # an averaged count or from a derivation over F_7.
 incidence=[Counter() for c in cosets]
 for i,g in enumerate(G):
  j=by[mul(g,G[h])]
  incidence[coset_of[i]][v[j]]+=1
  incidence[coset_of[j]][v[i]]+=1
 for ci,members in enumerate(cosets):
  own=v[members[0]]
  expected=Counter({own:20}) if name=='original' else Counter({k:10 for k in range(3) if k!=own})
  assert incidence[ci]==expected,(name,ci,incidence[ci],expected)
 M=sum(n for (a,b),n in counts.items() if a!=b)
 # Treat each ordered trace contribution as one unordered marked pair.
 total=Counter()
 for (a,b),n in counts.items():
  if a!=b:total[tuple(sorted((a,b)))]+=n
 nA=972
 assert all(n%nA==0 for n in total.values())
 weights={f'{a}{b}':n//nA for (a,b),n in total.items()}
 assert M%nA==0
 coeff=M//nA
 results[name]={'ordered_pair_counts':{f'{a}{b}':n for (a,b),n in sorted(counts.items())},'different_color_pairs':M,'incidence_weights':weights,'coefficient':coeff,'mod7':coeff%7,'individual_cusp_incidence_checked':len(incidence),'individual_cusp_incidence_rule':'20 own color' if name=='original' else '10 each other color'}
 print(name,results[name])
assert results['original']['coefficient']==0
assert results['plus']['mod7']!=0
# Store the finite ingredients, not a claim that integration has been proved.
record={'convention':'rightmost first','order':len(G),'cusps':len(cosets),'s':s,'rplus':rp,'rminus':rm,'h_word':words[h],'h_plus':G[h],'h_minus':minus[h],'h_original':orig[h],'pair_colors':{k:[v[0],v[h]] for k,v in colors.items()},'counts':results}
(P/'data/resolvent_color_certificate.json').write_text(json.dumps(record,indent=2)+'\n')
print('PASS: exact finite trace coefficient separates both resolvent colorings from original.')
