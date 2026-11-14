"""Integral cellular certificate for the common norm kernel of a mod-2
homology cover of a closed oriented genus-two surface.

The input presentation is <a,b,c,d | [a,b][c,d]>.  The 16-sheeted
cover is the kernel of abelianization modulo 2.  Quotienting its H_1
by the transfer images from all fifteen two-sheeted quotients computes
the character group of the finite common kernel of the Jacobian norms.
All calculations are over Z, not floating point.
"""
from pathlib import Path
import json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

n=4
vertices=list(range(1<<n))
edges=[(v,i) for v in vertices for i in range(n)]
idx={e:j for j,e in enumerate(edges)}
tree={(v^(1<<(v.bit_length()-1)),v.bit_length()-1) for v in vertices[1:]}
chords=[e for e in edges if e not in tree]
chord_idx={e:j for j,e in enumerate(chords)}

def chain_path(v):
    out=S.zeros(len(edges),1)
    w=0
    for i in range(n):
        if (v>>i)&1:
            out[idx[(w,i)]]+=1
            w^=1<<i
    return out

def boundary(c):
    out=S.zeros(len(vertices),1)
    for (v,i),j in idx.items():
        out[v]-=c[j]
        out[v^(1<<i)]+=c[j]
    return out

def coords(c):
    assert boundary(c)==S.zeros(len(vertices),1)
    return S.Matrix([c[idx[e]] for e in chords])

cycles=[]
for v,i in chords:
    c=chain_path(v)-chain_path(v^(1<<i))
    c[idx[(v,i)]]+=1
    cycles.append(c)
C=S.Matrix.hstack(*cycles)
assert S.Matrix([[C[idx[e],j] for j in range(len(chords))] for e in chords])==S.eye(len(chords))

faces=[]
word=[(0,1),(1,1),(0,-1),(1,-1),(2,1),(3,1),(2,-1),(3,-1)]
for start in vertices:
    c=S.zeros(len(edges),1)
    v=start
    for i,sign in word:
        if sign==1:
            c[idx[(v,i)]]+=1
            v^=1<<i
        else:
            v^=1<<i
            c[idx[(v,i)]]-=1
    assert v==start
    faces.append(coords(c))
F=S.Matrix.hstack(*faces)
assert F.rank()==15
F_snf=smith_normal_form(F,domain=ZZ)
assert [abs(F_snf[i,i]) for i in range(min(F.shape)) if F_snf[i,i]]==[1]*15

transfers=[]
transfer_labels=[]
for a in range(1,1<<n):
    bits=[(a>>i)&1 for i in range(n)]
    pivot=bits.index(1)
    small_edges=[(v,i) for v in range(2) for i in range(n)]
    small_idx={e:j for j,e in enumerate(small_edges)}
    def small_path(v):
        out=S.zeros(2*n,1)
        if v:
            out[small_idx[(0,pivot)]]=1
        return out
    for v,i in small_edges:
        if (v,i)==(0,pivot):
            continue
        z=small_path(v)-small_path(v^bits[i])
        z[small_idx[(v,i)]]+=1
        transfer=S.zeros(len(edges),1)
        for g,j in edges:
            parity=(a&g).bit_count()%2
            transfer[idx[(g,j)]]=z[small_idx[(parity,j)]]
        transfers.append(coords(transfer))
        transfer_labels.append([a,v,i])

M=S.Matrix.hstack(F,*transfers)
D=smith_normal_form(M,domain=ZZ)
diag=[int(abs(D[i,i])) for i in range(min(D.shape))]
assert all(diag)
result={
    'presentation':'<a,b,c,d | [a,b][c,d]>',
    'deck_group':'(Z/2)^4',
    'cover_genus':17,
    'vertices':16,'edges':64,'faces':16,
    'tree_edges':sorted([list(x) for x in tree]),
    'chords':len(chords),
    'face_boundary_rank':int(F.rank()),
    'H1_rank':len(chords)-int(F.rank()),
    'transfer_columns':len(transfers),
    'relation_matrix_shape':list(M.shape),
    'smith_diagonal':diag,
    'nontrivial_invariant_factors':[d for d in diag if d>1],
    'finite_quotient_order':int(S.prod(diag)),
    'interpretation':'Pontryagin dual of common kernel of the 15 Jacobian norm maps',
    'scope':'Topological integral calculation; transport to odd characteristic requires prime-to-characteristic smooth proper comparison.'
}
assert result['H1_rank']==34
here=Path(__file__).resolve().parent
(here/'A_norm_kernel_output.json').write_text(json.dumps(result,indent=2)+'\n')
(here/'A_norm_kernel_matrix.json').write_text(json.dumps({'matrix':[[int(x) for x in row] for row in M.tolist()],'transfer_labels':transfer_labels})+'\n')
print(json.dumps(result,indent=2))
