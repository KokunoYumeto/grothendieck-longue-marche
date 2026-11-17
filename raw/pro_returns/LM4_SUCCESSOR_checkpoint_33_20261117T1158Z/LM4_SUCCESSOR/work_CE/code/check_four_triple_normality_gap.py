"""Exact limitation of the four transported b-triple relations.

This checks the supplied common-marking words, an explicit Nielsen basis,
and a single S4 quotient of the partial presentation.  It also records
why this quotient does NOT extend across the retained base1 monodromy.
It is not a quotient/counterexample for the actual total ratio pencil.
"""
from pathlib import Path
import hashlib,itertools,json
ROOT=Path(__file__).resolve().parents[2]
CE=ROOT/'work_CE'
TFILE=ROOT/'work_DE/next_marginal_source/pencil_triple_transports.json'
BFILE=ROOT/'work_DE/next_marginal_source/ratio_pencil_braids.json'
RFILE=ROOT/'work_DE/next_marginal_source/remaining_pencil_words.json'
TD=json.loads(TFILE.read_text());BD=json.loads(BFILE.read_text())
def red(w):
 out=[]
 for x in w:
  if out and out[-1]==-x:out.pop()
  else:out.append(x)
 return tuple(out)
def iv(w):return tuple(-x for x in reversed(w))
def wd(*ws):return red(itertools.chain.from_iterable(ws))
def sub(w,A):return wd(*(A[x] if x>0 else iv(A[-x]) for x in w))
def conj(w,u):return wd(w,u,iv(w))
# New basis names retain the index of the U puncture being replaced.
pre={9:(),15:(),20:(16,),2:(-9,),6:(-9,-8,-7),12:(10,),
     1:(-9,-8,-7,-5,-4,-3,-2),19:(10,12,14,15,16,17,18)}
order=[9,15,20,2,6,12,1,19]
phi={i:conj(pre[i],(i,)) if i in pre else (i,) for i in range(1,21)}
psi={i:(i,) for i in range(1,21) if i not in pre}
for i in order:
 assert all(abs(j) in psi for j in pre[i])
 p=sub(pre[i],psi);psi[i]=conj(iv(p),(i,))
for i in range(1,21):
 assert sub(phi[i],psi)==(i,)==sub(psi[i],phi)
pairs=[(phi[6],phi[12]),(phi[1],phi[19]),(phi[20],phi[2]),(phi[15],phi[9])]
normalized=[]
for j,t in enumerate(TD['triples']):
 h=tuple(t['b_conjugator_special_basis_mod_right_b'])
 ms=[conj(iv(h),m) for m in t['meridians_special_basis']]
 assert ms[0]==(11,)
 prod=wd(*(m for _,m in sorted(zip(t['local_positions'],ms))))
 P,Q=pairs[j];expected=wd(P,Q,(11,)) if j<3 else wd((11,),P,Q)
 assert prod==expected
 # Express actual local U meridians using only b,P,Q in each case.
 expected_U=[
  (conj((-11,),P),conj((-11,),Q)),
  (conj((-11,),conj(iv(Q),P)),conj((-11,),Q)),
  (conj((-11,),Q),P),
  (Q,conj((11,),P))
 ][j]
 assert tuple(ms[1:])==expected_U
 normalized.append({'name':t['name'],'h':h,'P':P,'Q':Q,
                    'local_meridians':ms,'ordered_product':prod})
# Four-point permutations, composition rightmost first.
I=tuple(range(4))
def pm(a,b):return tuple(a[b[i]] for i in range(4))
def pi(a):return tuple(a.index(i) for i in range(4))
def pc(a,b):return pm(pm(a,b),pi(a))
def tr(i,j):
 a=list(I);a[i-1],a[j-1]=a[j-1],a[i-1];return tuple(a)
def ev(w,q):
 r=I
 for x in w:r=pm(r,q[x] if x>0 else pi(q[-x]))
 return r
def closure(gs):
 out={I};todo=[I]
 while todo:
  a=todo.pop()
  for g in gs:
   b=pm(a,g)
   if b not in out:out.add(b);todo.append(b)
 return out
# In the SPECIAL basis: c=x10, b=x11, H omits x11.
q={i:I for i in range(1,21)}
q[3]=tr(1,3);q[9]=tr(1,2);q[11]=tr(3,4)
for j,t in enumerate(normalized):
 ms=[ev(w,q) for w in t['local_meridians']];p=ev(t['ordered_product'],q)
 assert all(pc(p,m)==m for m in ms)
assert pc(q[11],q[10])==q[10]
H=closure([q[i] for i in range(1,21) if i!=11]);G=closure(list(q.values()))
k=ev((3,9,-3),q);bkb=pc(q[11],k)
assert len(H)==6 and len(G)==24 and k in H and bkb not in H
assert k==tr(2,3) and bkb==tr(2,4)
# ORIGINAL generic basis has x10_old=c*b^-1.
qo=[q[i] for i in range(1,21)];qo[9]=pm(q[10],pi(q[11]))
basechecks=[]
for row in BD['loops']:
 p=qo[:]
 for v in row['word']:
  i=abs(v)-1;a,b=p[i],p[i+1]
  p[i],p[i+1]=(pc(a,b),a) if v>0 else (b,pc(pi(b),a))
 inner=[a for a in itertools.permutations(range(4)) if all(pc(a,qo[i])==p[i] for i in range(20))]
 changes=[i+1 for i in range(20) if p[i]!=qo[i]]
 basechecks.append({'name':row['name'],'changed_indices':changes,'inner_implementers':inner})
 if row['name'].startswith('b_triple_'):assert p==qo
 if row['name']=='base1':assert not inner
 if row['name']=='base2':assert p==qo
RD=json.loads(RFILE.read_text())
assert RD['initial_order']==BD['initial_order']
filledchecks=[]
for row in RD['loops']:
 p=qo[:]
 for v in row['word']:
  i=abs(v)-1;a,b=p[i],p[i+1]
  p[i],p[i+1]=(pc(a,b),a) if v>0 else (b,pc(pi(b),a))
 filledchecks.append({'name':row['name'],'changed_indices':[i+1 for i in range(20) if p[i]!=qo[i]]})
assert [r['name'] for r in filledchecks if r['changed_indices']]==['discriminant_2_plus','discriminant_2_minus']
record={'scope':'Partial four-triple plus retained-node presentation only; actual base1 action excludes this S4 quotient.',
 'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (TFILE,BFILE,RFILE)},
 'nielsen_basis':phi,'inverse_basis':psi,'normalized_triples':normalized,
 'partial_S4_special_generator_images':q,'source_order':len(H),'ambient_order':len(G),
 'kernel_word':[3,9,-3],'kernel_image':k,'b_conjugated_image':bkb,
 'actual_base_monodromy_checks':basechecks,'other_filled_monodromy_checks':filledchecks}
(CE/'four_triple_normality_gap.json').write_text(json.dumps(record,indent=2)+'\n')
print('PASS: exact triangular Nielsen basis and both inverse compositions on all 20 generators.')
print('PASS: four actual normalized local triples have central products P_i Q_i b (last: b P_i Q_i).')
print('PASS: all four local triple relations plus [c,b] hold in S4.')
print('Source H image order:',len(H),'partial total image order:',len(G))
print('k=x3*x9*x3^-1 maps to (23); b*k*b^-1 maps to (24), outside source H.')
for x in basechecks:print(x['name'],'changed',x['changed_indices'],'inner implementers',len(x['inner_implementers']))
print('Other25 filled loops:23 pass; exactly discriminant_2_plus and discriminant_2_minus fail.')
print('LIMIT: base1 has no inner implementer, so this is NOT a representation of the actual total pencil.')
