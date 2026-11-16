"""Exact antipodal proper-rank2 Fitting gate for the reverse-prime cover."""
from pathlib import Path
import numpy as np,json
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'agent_five'
D=np.load(P/'ferrari_d3_fox.npz');F=np.load(P/'ferrari_d3_filtration.npz');S=np.load(P/'ferrari_d3_controlled_seed.npz')
M=[[((a&1)*(b&1)^((a>>1)*(b>>1)))+2*(((a&1)*(b>>1))^((a>>1)*(b&1))^((a>>1)*(b>>1)))for b in range(4)]for a in range(4)]
V=[0,1,3,2];I=(1,0,0,1)
def mm(a,b):return(M[a[0]][b[0]]^M[a[1]][b[2]],M[a[0]][b[1]]^M[a[1]][b[3]],M[a[2]][b[0]]^M[a[3]][b[2]],M[a[2]][b[1]]^M[a[3]][b[3]])
def mi(a):
 z=V[M[a[0]][a[3]]^M[a[1]][a[2]]];assert z
 return tuple(M[z][q]for q in(a[3],a[1],a[2],a[0]))
def identity(n):return(tuple(range(n)),(I,)*n)
def mul(g,h):return(tuple(g[0][q]for q in h[0]),tuple(mm(g[1][h[0][j]],h[1][j])for j in range(len(h[0]))))
def inv(g):
 p=tuple(g[0].index(j)for j in range(len(g[0])))
 return p,tuple(mi(g[1][p[j]])for j in range(len(p)))
def power(g,n):
 r=identity(len(g[0]))
 while n:
  if n&1:r=mul(r,g)
  g=mul(g,g);n//=2
 return r
def closure(gs,bound=100000):
 n=len(gs[0][0]) if gs else 2;one=identity(n);G=[one];seen={one}
 for h in G:
  for g in gs:
   z=mul(h,g)
   if z not in seen:seen.add(z);G.append(z)
  if len(G)>bound:return None,None
 return G,seen
def nmm(a,b):
 out=np.zeros((a.shape[-2],b.shape[-1]),dtype=int);mt=np.array(M)
 for k in range(a.shape[-1]):out^=mt[a[:,k,None],b[None,k,:]]
 return out
px,py=D['X_permutations'][:2];sigma=S['seed_permutations'][24]
chosen=None
for q in range(243):
 if int(F['homology_dimensions'][q]-F['boundary_dimensions'][q])!=2 or sigma[q]==q:continue
 orb={q};todo=[q]
 for j in todo:
  for p in(px,py):
   r=int(p[j])
   if r not in orb:orb.add(r);todo.append(r)
 if len(orb)==8:chosen=sorted(orb);break
assert chosen is not None
lookup={q:j for j,q in enumerate(chosen)}
def extract(p,blocks):
 pp=tuple(lookup[int(p[q])]for q in chosen);ms=[]
 for q in chosen:
  r=int(p[q]);a=nmm(nmm(F['basis_inverse'][r],blocks[q]),F['basis'][q]);b=int(F['boundary_dimensions'][q]);h=int(F['homology_dimensions'][q]);assert h-b==2
  ms.append(tuple(map(int,a[b:h,b:h].ravel())))
 return pp,tuple(ms)
gg=[extract(D['X_permutations'][k],D['X_blocks'][k])for k in(0,1)]
ss=[extract(S['seed_permutations'][k],S['seed_blocks'][k])for k in range(24,30)]
assert all(g[0]==ss[0][0]for g in ss)
pairs=sorted({tuple(sorted((i,ss[0][0][i])))for i in range(8)})
assert len(pairs)==4 and all(len(set(p))==2 for p in pairs)
base=pairs[0];reps=[None]*4;reps[0]=identity(8);todo=[0]
def pair_target(g,p):return pairs.index(tuple(sorted(g[0][i]for i in p)))
for j in todo:
 for g in gg:
  k=pair_target(g,pairs[j])
  if reps[k]is None:reps[k]=mul(g,reps[j]);todo.append(k)
assert len(todo)==4
def restrict(g):
 assert {g[0][i]for i in base}==set(base)
 return tuple(base.index(g[0][i])for i in base),tuple(g[1][i]for i in base)
hg=[]
for j,r in enumerate(reps):
 for g in gg:
  k=pair_target(g,pairs[j]);hg.append(restrict(mul(mul(inv(reps[k]),g),r)))
hg=list(dict.fromkeys(hg));H,hs=closure(hg);assert H is not None
print(json.dumps({'phase':'ambient','order':len(H),'orbit':chosen,'base_antipodal_pair':[chosen[i]for i in base]}),flush=True)
ng=[restrict(mul(mul(inv(r),s),r))for r in reps for s in ss]
ng=list(dict.fromkeys(ng));NG,ns=closure(ng);assert NG is not None
changed=True
while changed:
 changed=False
 for h in list(ng):
  for g in hg:
   z=mul(mul(g,h),inv(g))
   if z not in ns:
    ng.append(z);NG,ns=closure(ng);assert NG is not None;changed=True
print(json.dumps({'phase':'normal_image','order':len(NG)}),flush=True)
one=identity(2);n2=len(H)
while n2%2==0:n2//=2
n2=len(H)//n2
pg=[];PG=[one];ps={one}
for g in H:
 if len(PG)==n2:break
 if g in ps or power(g,n2)!=one:continue
 tt,ts=closure(pg+[g],n2)
 if tt is not None and len(tt)&(len(tt)-1)==0:pg.append(g);PG,ps=tt,ts
assert len(PG)==n2
core=set(PG);changed=True
while changed:
 old=set(core)
 for g in hg:core&={mul(mul(g,h),inv(g))for h in core}
 changed=core!=old
assert all(mul(mul(g,h),inv(g))in core for g in hg for h in core)
out={'harmonic_character_orbit':chosen,'characters':D['characters'][chosen].tolist(),
 'antipodal_pair':[chosen[i]for i in base],'ambient_pair_stabilizer_image_order':len(H),
 'source_normal_closure_image_order':len(NG),'sylow2_order':n2,'O2_ambient_order':len(core),
 'O2_contains_antipodal_swap':any(h[0]==(1,0)for h in core),
 'all_source_seed_generators_have_swap':all(h[0]==(1,0)for h in ng[:24]),
 'scope':'Local proper-rank2 antipodal image. A trivial O2 swap image would obstruct every normal nilpotent image carrying the signed frame bit; a nontrivial swap does not yet prove a global lift.'}
(ROOT/'agent_lifting'/'records'/'d3_rank2_fitting.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
