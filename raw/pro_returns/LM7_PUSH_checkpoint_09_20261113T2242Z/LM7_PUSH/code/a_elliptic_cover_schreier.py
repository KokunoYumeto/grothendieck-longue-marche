#!/usr/bin/env python3
"""Exact second source morphism for the multiplication-by-three cover.

G=C3*C3=<r,s|r^3=s^3=1>, x=s*r^-1, y=r*x*r^-1.
H=ker(G->C3; r->1,s->2) is free on p=s*r,q=r*s.
This script rewrites the original Fermat subgroup N literally in H.
Every cusp lies in H', so its metabelian quotient kills Lambda²W.
"""
from pathlib import Path
import importlib.util,json
import numpy as np
import sympy as sp
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('fermat',HERE/'de_fermat_schreier.py')
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)

# G letters: r=1,s=2. H letters: p=1,q=2.
def reduce_G(word):
    out=[]
    for z in word:
        gen=abs(z);exp=1 if z>0 else 2
        if out and out[-1][0]==gen:
            exp=(out.pop()[1]+exp)%3
        if exp:out.append((gen,exp))
    return out

Hlabels={0:[1],1:[2],2:[-1,-2]}
def rewrite_H(word):
    q=0;out=[]
    for z in word:
        value=1 if abs(z)==1 else 2
        qq=(q+(value if z>0 else -value))%3
        if abs(z)==2:
            lab=Hlabels[q] if z>0 else f.inverse_word(Hlabels[qq])
            out+=lab
        q=qq
    assert q==0
    return f.free_reduce(out)

images={1:[2,-1],2:[1,2,1]}
images[-1]=f.inverse_word(images[1]);images[-2]=f.inverse_word(images[2])
def NtoG(word):return [a for z in word for a in images[z]]
def NtoH(word):return rewrite_H(NtoG(word))

# Verify the literal C3*C3-to-H replacement relations and original order3 Nielsen action.
for q in range(3):
    assert rewrite_H([1]*q+[2]*3+[-1]*q)==[]
    assert rewrite_H([1]*q+[1]*3+[-1]*q)==[]
assert reduce_G([1]+images[1]+[-1])==reduce_G(images[2])
assert reduce_G([1]+images[2]+[-1])==reduce_G(f.inverse_word(images[1]+images[2]))

words=[NtoH(w) for w in f.NWORDS]
AB=np.array([[sum((1 if z==i else -1 if z==-i else 0) for z in w)
              for w in words] for i in (1,2)],dtype=np.int64)
assert not np.any(AB%3)
proper=AB//3
cusps={name:NtoH(w) for name,w in f.CUSP_WORDS.items()}
assert all(all(sum((1 if z==i else -1 if z==-i else 0) for z in w)==0
               for i in (1,2)) for w in cusps.values())
assert not np.any(proper@f.CUSP_VECTORS)
T=sp.Matrix(f.TATE_QUOTIENT.tolist())
R=sp.Matrix(proper.tolist())*T.T*(T*T.T).inv()
assert R*T==sp.Matrix(proper.tolist()) and abs(R.det())==1
print('H free basis: p=s*r, q=r*s; omitted Schreier generator is p^-1*q^-1.')
print('N proper homology map divided by3:',proper.tolist())
print('Comparison with the saved primitive proper quotient:',R.tolist(),'determinant',R.det())
print('All nine cusp words have exactly zero H abelianization.')
print('Consequently the actual induced N-central map to H/H-double-prime kills Lambda²W.')
print('The two saved invisible Johnson output directions lie in Lambda²W, so this map detects neither.')
out={'G_presentation':'<r,s | r^3=s^3=1>',
     'H_kernel_character':{'r':1,'s':2},'H_basis':{'p':[2,1],'q':[1,2]},
     'x_G_word':images[1],'y_G_word':images[2],
     'N_basis_H_words':words,'cusp_H_words':cusps,
     'proper_homology_map_divided_by3':proper.tolist(),
     'proper_quotient_comparison':[[int(a) for a in row] for row in R.tolist()],
     'metabelian_central_map_kills':'Lambda²W'}
(HERE/'a_elliptic_cover_schreier.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: exact source morphism; no uncomputed arithmetic action inferred.')
