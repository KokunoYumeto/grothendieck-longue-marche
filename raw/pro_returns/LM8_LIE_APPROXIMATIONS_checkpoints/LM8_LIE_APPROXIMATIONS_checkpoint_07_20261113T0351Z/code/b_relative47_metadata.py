#!/usr/bin/env python3
"""Write the provenance and result ledgers for B.25--B.28."""
from pathlib import Path
import csv
import json

ROOT=Path(__file__).resolve().parent.parent
SEC=ROOT/'sections'
PASSAGES=[
    'C3 §47, ff.415–420, scans229–240; map types via supplied LM2 B.m3 and E.4',
    'C3 §47, ff.416–420, scans231–240, equations (14),(15),(20),(30); exact normalized equation via LM2 B.m3',
]
rows=[
    dict(id='B.25',status='Proved',
         statement='The quotient F2→C2*C3 has a rank-seven relative radical over S3; its two graded rank-two projections are the degree-six eight-puncture cover and five-puncture filling, with explicitly stated peripheral images.',
         where_proved='sections/B_relative47.tex, Statement B.25 and proof; code/b_relative47.py homology_checks',
         depends_on=['Hain 1998 §1, pp.47–48: definition of relative completion','B.8 finite-index relative-completion argument','Schreier formula and explicit rational Belyi map'],
         notes='The quotient φ, the level-two inclusion ι, and the two radical maps c,d remain distinct. Original cote-140-3 scans were not freshly inspected; all displayed algebraic maps are defined and proved independently.'),
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
         depends_on=['LM2 B.m3, E.3, E.4, B.g12','B.25','B.26','B.27'],
         notes='A profinite automorphism induces a particular action on N. The graded lift in B.26 is freely chosen; a compatible and incompatible lift share the same absolute action. B.12 pro-ell lifts do not supply a full profinite word, since v:F2→S3 does not factor through the absolute pro-ell completion for ell≥5. Missing: compute the induced relative action from a full word or prove a reconstruction/comparison with the required additional data. No simultaneous filtered peripheral formality is assumed.'),
]
for row in rows:
    row['manuscript_passages']=PASSAGES
    row['depends_on_doubtful_reading']=False
(SEC/'B_relative47_results.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')

coverage=[
    dict(task='B.relative47.map_types',requested='Retain the separate quotient and level-two inclusion and identify the appropriate relative radicals',status='complete',results=['B.25'],remaining=[]),
    dict(task='B.relative47.graded_compatibility',requested='Determine whether correctly typed relative compatibility imposes computable graded constraints',status='complete',results=['B.26','B.27'],remaining=[]),
    dict(task='B.relative47.through9',requested='Exact graded dimensions and q7 test through weight nine',status='complete',results=['B.27'],remaining=[]),
    dict(task='B.relative47.profinite_equation',requested='Decide the actual §47 compatibility condition on a prescribed profinite automorphism and compare all pentagon solutions',status='partial',results=['B.25','B.26','B.27','B.28'],remaining=['Specify the relative action induced by the full profinite word, retaining its rank-seven source data.','Evaluate that action in the corrected diagram, or prove a comparison that reconstructs it from additional data.','A graded existential lift alone cannot decide the prescribed equation.']),
    dict(task='B.relative47.source_image',requested='Check original §47 reading against the source when accessible',status='partial',results=['B.25','B.28'],remaining=['The cote-140-3 original was unavailable in the supplied scan folders; an external original-PDF attempt failed. Source anchoring here relies on the supplied LM2 reconstruction, expressly identified as such.']),
]
(SEC/'B_relative47_coverage.json').write_text(json.dumps(coverage,indent=2,ensure_ascii=False)+'\n')

readings=[
 ['140-3','229–240','415–420','§47','Two maps F2→C2*C3: quotient φ and level-two inclusion ι','Read the supplied LM2 B.m3/E.4 reconstruction; original scans not independently viewed. Both maps defined and checked algebraically.','B.25–B.28','no; source access limitation stated'],
 ['140-3','231–240','416–420','(14),(15),(20),(30)','ξ=(φ(ξ)σ(φ(ξ))^−1)x^ν','Read exactly in LM2 B.m3 together with its two-generator proof; no claim of a fresh manuscript image check.','B.28','no; source access limitation stated'],
 ['LM2','B.g12','supplied return','finite quotient obstruction','A rational prounipotent group does not retain arbitrary nontrivial finite quotients','Read supplied text; retain S3 by relative completion and rank7 source.','B.25','no'],
 ['primary-source','Hain1998Relative','47–48','§1','Universal prounipotent extension of a reductive quotient','Opened primary Numdam PDF; definition and explicit finite-quotient example read.','B.25','no'],
 ['computed','b_relative47.json','weights1–9','exact certificates','Every special invariant basis vector admits two independently projected lifts','Exact rational calculations executed; full output saved, with large source dimensions obtained by character formulas.','B.26–B.27','no'],
]
with (SEC/'B_relative47_readings.csv').open('w',newline='') as f:
    w=csv.writer(f); w.writerow(['cote','scan','folio','equation','reading','resolution','used_by','doubtful']); w.writerows(readings)
print('B.25–B.28: 3 Proved, 1 Open; all metadata written.')
