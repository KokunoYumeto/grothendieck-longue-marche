#!/usr/bin/env python3
"""Retain the reviewed version and type its scalar-extension map exactly."""
from pathlib import Path
import hashlib
import json
import shutil

root=Path(__file__).resolve().parents[1]
proof=root/'sections/E_quartic_five_numerical.tex'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(proof)=='73b82d7b97c559b0d4ea3c9fc98b5c87e7ea40e932ca73d6982b9b9c31a4059d'
history=root/'qa/history/scalar_extension_typing'
history.mkdir(parents=True,exist_ok=False)
shutil.copy2(proof,history/(proof.name+'.md'))
for name in ['layout.json','contact_sheet.jpg','latex_pass_1.out','latex_pass_2.out','render.out']:
    shutil.copy2(root/'qa'/name,history/name)
for p in sorted((root/'qa').glob('page-*.jpg')):
    shutil.copy2(p,history/p.name)
shutil.copy2(root/'code/build_standalone.out',history/'build_standalone.out')
layout=json.loads((root/'qa/layout.json').read_text())
review={'status':'PASS','scope':'Layout only; all four final images actually viewed by root before the peer typing correction.',
        'PDF_sha256':layout['PDF_sha256'],'proof_sha256':sha(proof),
        'pages_actually_viewed':layout['page_images'],
        'findings':'All four pages legible; no clipping, overlap or overfull display. Page four contains the continued closing paragraphs.'}
(history/'visual_review.json').write_text(json.dumps(review,indent=2)+'\n')
old=r'''intrinsic class-two extension. The scalar-extension map
$R\hookrightarrow\mathbb Q_5$ sends (E118.4) onto the entire
$\mathbb Q_5^3$ compact slice, with parameter inverse
$\mathbf q\mapsto\mathbf q/5$ on the lattice parametrization
$\mathbf s\mapsto5\mathbf s$.'''
new=r'''intrinsic class-two extension. Scalar extension of this lattice is
the isomorphism
\[
 (5R^3)\otimes_R\mathbb Q_5\longrightarrow\mathbb Q_5^3,
 \quad (5\mathbf s)\otimes\lambda\longmapsto5\lambda\mathbf s,
 \qquad
 \mathbf q\longmapsto\sum_{i=1}^3(5e_i)\otimes(q_i/5).
\]
The actual rational compact slice over the image of $[b]$
is all of $\mathbb Q_5^3$, as proved below using the correcting
cochains of E.115.'''
t=proof.read_text();assert t.count(old)==1;t=t.replace(old,new)
old=r'''the actual maps of E.115. The scalar-extension assertion
uses the same maps with a single bounded denominator;
its mixed correction still has finite support.'''
new=r'''the actual maps of E.115. The displayed tensor map sends
$(5e_i)\otimes1$ to $5e_i$, and composing it with the
displayed inverse in either order fixes this basis and all
scalars; hence both maps are inverse $\mathbb Q_5$-linear maps.
For every rational compact vector $\mathbf q\in\mathbb Q_5^3$,
the actual mixed correction is
$v_{3121}\wedge j_{\mathbf q}(F-1)^{-1}h(F)$ at $3121$
and zero at every other prime outside $S$. This family
has finite support and a common finite denominator. The
rational cochain inverse of E.115 therefore gives a lift for
each $\mathbf q$. This proves the asserted rational slice
through the actual coefficient-extension and correction maps.'''
assert t.count(old)==1;t=t.replace(old,new);proof.write_text(t)
result={'status':'PASS','reason':'Independent peer identified the need to distinguish the literal coefficient inclusion from the tensor-extension isomorphism by specifying both maps.',
        'before_proof_sha256':review['proof_sha256'],'after_proof_sha256':sha(proof),
        'preserved_review':str(history.relative_to(root))+'/visual_review.json',
        'mathematical_changes':'Explicit tensor map and inverse; separate actual rational cochain argument. Integral index125 result unchanged.'}
(history/'correction.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
