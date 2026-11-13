#!/usr/bin/env python3
"""Write the provenance and result ledgers for B.25--B.28 and B.30."""
from pathlib import Path
import csv
import json

ROOT=Path(__file__).resolve().parent.parent
SEC=ROOT/'sections'
PASSAGES=[
    'C3 §47, ff.415–420v, physical PDF pages/scans229–240, archive printed footers228–239; all twelve original images directly inspected',
    'C3 §47: equation(1) scan229/f415; composite to S3 and kernel scan233/f417; equations(14),(15) scan234/f417v; equation(20) scan235/f418; equation(30) scan240/f420v',
]
rows=[
    dict(id='B.25',status='Proved',
         statement='The quotient F2→C2*C3 has a rank-seven relative radical over S3; its two graded rank-two projections are the degree-six eight-puncture cover and five-puncture filling, with explicitly stated peripheral images.',
         where_proved='sections/B_relative47.tex, Statement B.25 and proof; code/b_relative47.py homology_checks',
         depends_on=['Hain 1998 §1, pp.47–48: definition of relative completion','B.8 finite-index relative-completion argument','Schreier formula and explicit rational Belyi map'],
         notes='The quotient φ, the level-two inclusion ι, and the two radical maps c,d remain distinct. All original cote-140-3 physical pages229–240 were directly inspected after a successful HTTP-range extraction. Equation20 explicitly distinguishes the restricted first action; equation12 defines the composite to S3. All displayed algebraic assertions are also proved independently.'),
    dict(id='B.26',status='Proved',
         statement='In every positive degree the joint map sder_out(L7)^{S3}→sder_out(L2)×sder_out(L2)^{S3} is surjective. Every special invariant admits a compatible relative graded lift, and every nonzero one admits an incompatible lift with the same absolute projection.',
         where_proved='sections/B_relative47.tex, Statement B.26 and constructive cabling/averaged filling proof',
         depends_on=['B.25','B.10 special outer derivation modules','Characteristic-zero finite-group averaging'],
         notes='Tangentiality is imposed at all eight source punctures. This is an associated-graded statement, not a claim about prescribed filtered or profinite word actions. The source c-quotient is the maximal deck-trivial free-Lie quotient.'),
    dict(id='B.27',status='Proved',
         statement='Exact compatible-image dimensions through weights 1–9 are 0,0,1,0,1,0,2,1,4. Exact source invariant dimensions are 4,5,38,120,693,3163,17356,92930,524166; compatible-source dimensions are 4,5,37,120,690,3163,17350,92926,524153. The explicit q7 passes the existential graded test.',
         where_proved='sections/B_relative47.tex, Statement B.27 and proof; code/b_relative47.py, .json, .csv, .out',
         depends_on=['B.10 exact special-derivation character sequence','B.12 definition of q7','B.25','B.26','Exact rational Lyndon computations'],
         notes='All rank-two invariant basis vectors through9 and q7 were checked exactly over Q. Rank-seven dimensions use the exact character-Witt formula, not expanded huge matrices or sampled modular ranks.'),
    dict(id='B.28',status='Open',
         statement='Whether a prescribed profinite loop automorphism satisfies the normalized §47 equation, and whether all pentagon solutions satisfy that equation, remain unresolved here. A full profinite lift of q7 is not constructed; if one is supplied, its equation is likewise not decided.',
         where_proved='sections/B_relative47.tex, Statement B.28 and following precise obstruction discussion; no proof of the unresolved profinite assertions is claimed',
         depends_on=['LM2 B.m3, E.3, E.4, B.g12','B.25','B.26','B.27','B.29','B.30'],
         notes='A profinite automorphism induces a particular action on N. B.30 upgrades B.26 to full rational filtered existential lifts, but compatible and incompatible relative actions still share the same absolute action. The all-prime lifts in B.14d do not supply a full profinite word: v:F2→S3 factors through no absolute pro-prime completion. B.29 shows why finite-factor lifting alone does not preserve the cusp. Missing: compute the induced relative action from a full word or prove a reconstruction/comparison with the required additional data. No simultaneous filtered peripheral formality is assumed.'),
    dict(id='B.30',status='Proved',
         statement='The actual joint map from deck-invariant peripheral outer IA automorphisms of the eight-puncture sphere to the two tripod automorphism groups is surjective over Q in the complete prounipotent topology and integrally in the relative pro-ell topology for every ell≥5. Every invariant q admits full relative actions with induced pairs (q,q) and (q,1).',
         where_proved='sections/B_filtered_relative.tex, Statement B.30 and complete filtered correction proof',
         depends_on=['B.25 actual relative-completion maps','B.26 all-degree graded surjectivity','B.11 leading-term correction proof over Q','Explicit finite-group cohomology averaging on prounipotent layers'],
         notes='The quotient by actual deck commutators is the absolute completion by its universal property. Outer invariant actions have strict deck-centralizing representatives. Tangentiality descends through c by unique roots, and through d by the filling kernel. The pro-ell variant uses Schur–Zassenhaus, coprime H1, and the fact that the graded lift formulas divide only by2 and3. Graded surjectivity and convergent corrections yield full filtered surjectivity without simultaneous formality. The relative source action is freely chosen, not the action induced by a prescribed full profinite word; B.28 remains unresolved.'),
]
for row in rows:
    row['manuscript_passages']=PASSAGES
    row['depends_on_doubtful_reading']=False
(SEC/'B_relative47_results.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')

coverage=[
    dict(task='B.relative47.map_types',requested='Retain the separate quotient and level-two inclusion and identify the appropriate relative radicals',status='complete',results=['B.25'],remaining=[]),
    dict(task='B.relative47.graded_compatibility',requested='Determine whether correctly typed relative compatibility imposes computable graded constraints',status='complete',results=['B.26','B.27'],remaining=[]),
    dict(task='B.relative47.through9',requested='Exact graded dimensions and q7 test through weight nine',status='complete',results=['B.27'],remaining=[]),
    dict(task='B.relative47.profinite_equation',requested='Decide the actual §47 compatibility condition on a prescribed profinite automorphism and compare all pentagon solutions',status='partial',results=['B.25','B.26','B.27','B.28','B.29','B.30'],remaining=['Specify the relative action induced by the full profinite word, retaining its rank-seven source data.','Evaluate that action in the corrected diagram, or prove a comparison that reconstructs it from additional data.','B.30 gives freely chosen full rational filtered lifts; it does not recover the relative action induced by a prescribed profinite word.']),
    dict(task='B.relative47.filtered_compatibility',requested='Upgrade the all-degree graded existential relative lift to an actual rational filtered action and integral relative pro-ell action for ell≥5',status='complete',results=['B.30'],remaining=[]),
    dict(task='B.relative47.source_image',requested='Check original §47 reading against the source when accessible',status='complete',results=['B.25','B.28'],remaining=[]),
]
(SEC/'B_relative47_coverage.json').write_text(json.dumps(coverage,indent=2,ensure_ascii=False)+'\n')

readings=[
 ['140-3','229–240','415–420v','§47; physical PDF pages229–240, archive footers228–239','Two maps F2→C2*C3: quotient φ and level-two inclusion ι','All twelve original images directly inspected. LM2 scan numbers equal physical PDF page numbers; subtract one for zero-based indices and archive printed footers.','B.25–B.28','no'],
 ['140-3','229','415','(1)','φ(ℓ0)=ε0=σ∞ρ; φ(ℓ1)=σ∞; φ(ℓ∞)=ρ^−1','Direct image confirms the quotient map. Set s=σ∞,r=ρ,X=ℓ1,Y=ℓ0.','B.25','no'],
 ['140-3','233','417','(12),(13)','Composite φ-bullet:π̂0,3→S3 and kernel normally generated by ℓ0²,ℓ1²,ℓ∞³','Direct image confirms the finite quotient retained in the rank-seven relative source.','B.25','no'],
 ['140-3','234;240','417v;420v','(14),(15);(30)','ξρ(ξ)ρ²(ξ)=1 and ξ=(φ(ξ)σ∞(φ(ξ))^−1)ℓ1^ν','Both original displayed pairs directly inspected; the second equation is the normalized compatibility equation in B.28.','B.28','no'],
 ['140-3','235','418','(20)','φuξ=uξφ; the first uξ is its restriction to π̂0,3','Direct image explicitly explains this restriction, confirming the typed diagram and the distinction between the two maps.','B.25–B.28','no'],
 ['LM2','B.g12','supplied return','finite quotient obstruction','A rational prounipotent group does not retain arbitrary nontrivial finite quotients','Read supplied text; retain S3 by relative completion and rank7 source.','B.25','no'],
 ['primary-source','Hain1998Relative','47–48','§1','Universal prounipotent extension of a reductive quotient','Opened primary Numdam PDF; definition and explicit finite-quotient example read.','B.25','no'],
 ['computed','b_relative47.json','weights1–9','exact certificates','Every special invariant basis vector admits two independently projected lifts','Exact rational calculations executed; full output saved, with large source dimensions obtained by character formulas.','B.26–B.27','no'],
]
with (SEC/'B_relative47_readings.csv').open('w',newline='') as f:
    w=csv.writer(f); w.writerow(['cote','scan','folio','equation','reading','resolution','used_by','doubtful']); w.writerows(readings)
print('B.25–B.28 and B.30: 4 Proved, 1 Open; all metadata written.')
