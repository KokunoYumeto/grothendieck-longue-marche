#!/usr/bin/env python3
"""Literal rank-four to two rank-two source graph maps at the solvable boundary.

The two minimal nonnilpotent solvable even bases are S4 and A4 x C2.
Their relative pro2 reductions are the actual S3 and C6 source markings.
This certificate uses the recorded K basis, with both integral graph
projection matrices and the retained D33/D39 homology action modulo16.
"""
from pathlib import Path
from collections import deque
import argparse,json,time

ap=argparse.ArgumentParser()
ap.add_argument('--source-code',type=Path,
                default=Path(__file__).resolve().parents[2]/'LM7_FERMAT_TOWER'/'code')
args=ap.parse_args();OUT=Path(__file__).resolve().parent;started=time.time()
def pm(a,b):return tuple(a[b[i]] for i in range(len(a)))
def cycles(n,*blocks):
    a=list(range(n))
    for b in blocks:
        for j,x in enumerate(b):a[x]=b[(j+1)%len(b)]
    return tuple(a)
def closure(I,gs,m):
    G=[I];seen={I}
    for q in G:
        for g in gs:
            h=m(q,g)
            if h not in seen:seen.add(h);G.append(h)
    return G
I3=(0,1,2);ss=(1,0,2);rr=(1,2,0)
S3=closure(I3,[ss,rr],pm);assert len(S3)==6
C6=[(a,b) for a in range(2) for b in range(3)]
cm=lambda a,b:((a[0]+b[0])%2,(a[1]+b[1])%3)
ci=(0,0);cs=(1,0);cr=(0,1)
def invword(w):return [0 if a==0 else 3-a for a in reversed(w)]
def graph(G,m,e,s,r):
    ix={q:i for i,q in enumerate(G)};r2=m(r,r)
    v2={q:(0,min(ix[q],ix[m(q,s)])) for q in G}
    v3={q:(1,min(ix[q],ix[m(q,r)],ix[m(q,r2)])) for q in G}
    adj={v:[] for v in set(v2.values())|set(v3.values())}
    for j,q in enumerate(G):adj[v2[q]].append((v3[q],j));adj[v3[q]].append((v2[q],j))
    paths={v2[e]:[]};queue=deque(paths);tree=set()
    while queue:
        a=queue.popleft()
        for b,j in adj[a]:
            if b not in paths:
                paths[b]=paths[a]+[(j,1 if a[0]==0 else -1)];tree.add(j);queue.append(b)
    chords=[j for j in range(len(G)) if j not in tree];chord={j:i for i,j in enumerate(chords)}
    words=[]
    for j in chords:
        path=paths[v2[G[j]]]+[(j,1)]+[(k,-z) for k,z in reversed(paths[v3[G[j]]])]
        q=e;w=[]
        for k in range(0,len(path),2):
            a,z=path[k];b,zz=path[k+1];assert z==1 and zz==-1;a=G[a];b=G[b]
            if q!=a:assert m(q,s)==a;w.append(0);q=a
            if b!=q:
                if m(q,r)==b:w.append(1)
                else:assert m(q,r2)==b;w.append(2)
            q=b
        if q!=e:assert q==s;w.append(0)
        words.append(w)
    def collapse(w,start=None):
        q=e if start is None else start;out=[]
        def add(j,z):
            i=chord.get(j)
            if i is None:return
            a=z*(i+1)
            if out and out[-1]==-a:out.pop()
            else:out.append(a)
        for a in w:
            if a==0:q=m(q,s)
            else:
                h=m(q,r if a==1 else r2);add(ix[q],1);add(ix[h],-1);q=h
        return q,out
    for j,w in enumerate(words):assert collapse(w)==(e,[j+1])
    return {'G':G,'mul':m,'e':e,'s':s,'r':r,'ix':ix,'chords':chords,
            'words':words,'collapse':collapse,'vertices':len(adj)}
F=graph(S3,pm,I3,ss,rr);E=graph(C6,cm,ci,cs,cr)
assert len(F['words'])==len(E['words'])==2
Kwords=json.loads((args.source_code/'d_cm_rank4_refine.json').read_text())['K_basis_words']
structure=json.loads((args.source_code/'d_cm_rank4_structure.json').read_text())
def ab(w,d=2):return [sum((1 if a>0 else -1) for a in w if abs(a)==j+1) for j in range(d)]
maps=[];collapsed=[]
for R in [F,E]:
    col=[];ww=[]
    for w in Kwords:
        q,v=R['collapse'](w);assert q==R['e'];col.append(ab(v));ww.append(v)
    maps.append([[col[j][i] for j in range(4)] for i in range(2)]);collapsed.append(ww)
P=maps[0]+maps[1]
def determinant(A):
    A=[list(r) for r in A];n=len(A);den=1;sgn=1
    for k in range(n-1):
        if not A[k][k]:
            j=next(j for j in range(k+1,n) if A[j][k]);A[k],A[j]=A[j],A[k];sgn=-sgn
        z=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):A[i][j]=(A[i][j]*z-A[i][k]*A[k][j])//den
        for i in range(k+1,n):A[i][k]=0
        den=z
    return sgn*A[-1][-1]
det=determinant(P);assert det%2==1
def matmul(A,B,mod=16):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%mod for j in range(len(B[0]))] for i in range(len(A))]
def inverse_mod(A,mod=16):
    n=len(A);M=[[x%mod for x in A[i]]+[int(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        j=next(j for j in range(k,n) if M[j][k]%2);M[k],M[j]=M[j],M[k]
        z=pow(M[k][k],-1,mod);M[k]=[z*x%mod for x in M[k]]
        for i in range(n):
            if i!=k:
                z=M[i][k];M[i]=[(a-z*b)%mod for a,b in zip(M[i],M[k])]
    return [row[n:] for row in M]
Pinv=inverse_mod(P);AM=structure['D33_K_homology_mod16']
block=matmul(matmul(P,AM),Pinv)
assert all(block[i][j]==0 for i in range(4) for j in range(4) if (i//2)!=(j//2))
blocks=[[row[2*k:2*k+2] for row in block[2*k:2*k+2]] for k in range(2)]
for M in blocks:assert determinant(M)%16==1

# These are the actual joint quotient coordinates, not merely groups of
# the same order.  The recorded 18 source section words give a bijection.
joint=[]
for w in structure['Q0_B_section_words']:
    f,_=F['collapse'](w);e,_=E['collapse'](w);joint.append((f,e))
assert len(set(joint))==18
assert all((sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2)==c[0] for p,c in joint)

# Enumerate both minimal order24 bases with their literal source maps.
I4=tuple(range(4));S4s=cycles(4,(0,1));S4r=cycles(4,(1,2,3))
S4=closure(I4,[S4s,S4r],pm);assert len(S4)==24
A4s=cycles(4,(0,1),(2,3));A4r=cycles(4,(0,1,2))
A4=closure(I4,[A4s,A4r],pm);assert len(A4)==12
im=lambda a,b:(pm(a[0],b[0]),(a[1]+b[1])%2)
inner=closure((I4,0),[(A4s,1),(A4r,0)],im);assert len(inner)==24
def canon3(a):return min(a,tuple(-x%3 for x in a))
def mm3(a,b):
    return canon3(((a[0]*b[0]+a[1]*b[2])%3,(a[0]*b[1]+a[1]*b[3])%3,
                   (a[2]*b[0]+a[3]*b[2])%3,(a[2]*b[1]+a[3]*b[3])%3))
mi=(1,0,0,1);ms=(0,1,2,0);mr=(0,2,1,2)
mod3_map={mi:I4};mq=[mi]
for a in mq:
    for m,p in [(ms,A4s),(mr,A4r)]:
        z=mm3(a,m);v=pm(mod3_map[a],p)
        if z in mod3_map:assert mod3_map[z]==v
        else:mod3_map[z]=v;mq.append(z)
assert len(mod3_map)==12 and set(mod3_map.values())==set(A4)
assert all(mod3_map[mm3(a,b)]==pm(mod3_map[a],mod3_map[b]) for a in mq for b in mq)
summary={
    'minimal_nonnilpotent_solvable_even_order':12,
    'minimal_sign_preserving_base_order':24,
    'minimal_bases':['S4','A4 x C2'],
    'actual_mod3_A4_source_isomorphism_all144_products_checked':True,
    'relative_pro2_reduction_bases':['S3','C6'],
    'rank_two_free_kernels':['F=ker(B to S3)','B_prime=ker(B to C6)'],
    'rank_four_joint_base_order':18,
    'all18_recorded_Q0_section_maps_checked':True,
    'rank_four_to_rank_two_integral_matrix':P,
    'combined_integral_determinant':det,
    'combined_matrix_is_invertible_over_Z2':True,
    'retained_normalized_D39_H1_blocks_mod16':blocks,
    'retained_action_descends_to_both_H1_targets':True,
    'sphere_rank_two_H1_block_is_identity':blocks[0]==[[1,0],[0,1]],
    'elliptic_rank_two_H1_block_is_identity':blocks[1]==[[1,0],[0,1]],
    'scope':'Exact quotient/graph maps and retained homology action. Full peripheral compatibility on the two rank-two pro2 groups is not inferred from this linear test.',
    'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'K_basis_words':Kwords,
      'sphere_F_basis_B_words':F['words'],'elliptic_Bprime_basis_B_words':E['words'],
      'K_to_sphere_free_words':collapsed[0],'K_to_elliptic_free_words':collapsed[1],
      'sphere_quotient_states':[list(q) for q in F['G']],
      'elliptic_quotient_states':[list(q) for q in E['G']],
      'sphere_cycle_chords':F['chords'],'elliptic_cycle_chords':E['chords'],
      'combined_matrix_inverse_mod16':Pinv,
      'S4_generators':[list(S4s),list(S4r)],
      'A4_times_C2_generators':[{'A4':list(A4s),'C2':1},{'A4':list(A4r),'C2':0}]}
cert['actual_mod3_A4_isomorphism']=[{'matrix':list(m),'permutation':list(mod3_map[m])} for m in mq]
(OUT/'d_cm_solvable_even_boundary.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
