#!/usr/bin/env python3
"""Write only the G.23--G.24 companion ledgers; do not rebuild root metadata."""
from pathlib import Path
import csv
import json

root=Path(__file__).resolve().parents[1]
sec=root/'sections'
records=[
 {
  'id':'G.23',
  'statement':'Every A8+lambda B8 exponentiates to a one-parameter subgroup of the universal elliptic Grothendieck--Teichmueller kernel. All such subgroups have the prescribed CM torus character and finite symmetries; exact finite CM lifts do not select lambda.',
  'status':'Proved',
  'where_proved':'sections/g_degree8_nonmet.tex, G.23; input immediately after G.16 in sections/G.tex',
  'depends_on':['G.16, definitions (G.24)','Enriquez2014, Proposition4.19, equation(48), Sections4.7--4.8 and Proposition4.20'],
  'manuscript_passages':['Modern prompt G(e), actual embedded arithmetic image','Explicit follow-up: nonmetabelian degree-eight constraint from exact universal elliptic equations and finite CM transport'],
  'depends_on_doubtful_reading':False,
  'notes':'This proves a limitation of the universal algebraic constraints, not arithmetic realization for any chosen parameter. The finite-lift assertion uses successive averaging in characteristic-zero central vector layers, with convergence in the positive-degree filtration. Positive conjugation preserves the leading degree-eight vector. No conjectural equality between the universal kernel and the epsilon-generated subalgebra is used.'
 },
 {
  'id':'G.24',
  'statement':'The degree-eight plane has saturated ambient Z5-lattice Z5*(A8+(31/20)B8) + Z5*B8. Two integral length-nine Magnus coefficients are dual coordinates and determine lambda from an actual eighth-Johnson Galois element with nonzero first coordinate; the coordinate extractor is realized on characteristic finite Magnus quotients.',
  'status':'Proved',
  'where_proved':'sections/g_degree8_nonmet.tex, G.24; code/g_degree8_nonmet.py, g_degree8_nonmet.json and g_degree8_nonmet.out',
  'depends_on':['G.15','G.16, formula(G.25)','G.23','Exact Lyndon/tensor and finite group-word calculations in code/g_degree8_nonmet.py'],
  'manuscript_passages':['Modern prompt G(e), rational embedding and integral arithmetic lattice','Explicit follow-up: an actual nonmetabelian finite Galois observable distinguishing B8'],
  'depends_on_doubtful_reading':False,
  'notes':'alpha(D)=-[x^5y^4]D(x), nu(D)=[x^4yxy^3]D(x)+4[x^5y^4]D(x). On C8=A8+(31/20)B8 and B8 these are the identity matrix. Both Lie vectors are integral at5. In the characteristic quotient by (5^r,I^10), an actual Johnson-eight action gives these coordinates without logarithms or division by5. Actual group-commutator expansions modulo125 give ambient examples (alpha,nu)=(1,0),(1,1), with inverse and peripheral checks. No actual Galois value of nu, no unit value of alpha, and no saturation or index for the arithmetic image lattice is claimed.'
 }
]
coverage=[
 {
  'task':'G(e).degree8.universal_constraints',
  'requested':'Determine whether all universal elliptic equations and exact finite CM transport select the remaining degree-eight scalar.',
  'status':'Proved',
  'results':['G.16','G.23'],
  'remaining':[],
  'notes':'They do not: every lambda yields an actual universal one-parameter subgroup with the stated character and symmetries. This negative conclusion does not concern arithmetic realization.'
 },
 {
  'task':'G(e).degree8.nonmetabelian_measurement',
  'requested':'Determine the degree-eight arithmetic scalar through a second nonmetabelian functional or finite Galois action.',
  'status':'Open',
  'results':['G.16','G.24'],
  'remaining':['Evaluate nu on an actual eighth-Johnson Galois element with nonzero alpha, where alpha=d^3*chi_4^(4)/267840. The finite quotient and two coefficient functionals are explicit, but no arithmetic action on that quotient has been computed.'],
  'notes':'Then lambda=31/20+nu/alpha. The arithmetic alpha image need not contain a unit.'
 },
 {
  'task':'G(e).degree8.arithmetic_index_observable',
  'requested':'Determine the integral arithmetic image lattice and its indices in the embedded ambient module.',
  'status':'Open',
  'results':['G.16','G.24'],
  'remaining':['Determine the actual joint image of (alpha,nu), and the higher-degree arithmetic image lattices. The saturated ambient degree-eight plane proved in G.24 is not an arithmetic saturation assertion.']
 },
 {
  'task':'G(e).degree8.depth_two_source',
  'requested':'Use an available primary depth-two CM elliptic source to compute the missing arithmetic coordinate.',
  'status':'Open',
  'results':['G.16','G.24'],
  'remaining':['Malkin2020CM Theorems11 and16 are Hodge-correlator statements. Section2.2.3 explicitly conditions the motivic/ell-adic transfer on additional hypotheses, and the averaged-basepoint torsion-punctured setting must be compared with the prescribed once-punctured tangent before it could evaluate nu. Enriquez Section7.5 full cusp-to-cusp Mellin formulas do not supply this CM specialization.']
 }
]
(sec/'G_nonmet_results.json').write_text(json.dumps(records,indent=2)+'\n')
(sec/'G_nonmet_coverage.json').write_text(json.dumps(coverage,indent=2)+'\n')
rows=[
 ['Modern prompt','G(e)','','degree-eight embedded arithmetic line','Exact elliptic equations and a depth-two coordinate were requested as a follow-up to G.16.','Universal equations leave all parameters; finite coefficient extraction is proved, while actual arithmetic evaluation remains Open.','G.16;G.23;G.24','no'],
 ['Enriquez2014','Sections4.7--4.8','','Proposition4.19;equation(48);Proposition4.20','Primary supplied TeX and arXiv PDF reopened. The delta_(2n) formula agrees with epsilon_(2n+2), up to the stated opposite bracket convention.','The epsilon-generated positive Lie algebra exponentiates inside the actual universal elliptic kernel; associator isomorphisms preserve the canonical associated graded. No generation conjecture is needed.','G.23','no'],
 ['Enriquez2014','Section7.5','','depth-two Mellin formulas','Opened the explicit total-degree-eight full cusp-to-cusp iterated Eisenstein Mellin formulas.','They are not the needed CM specialization or its comparison path; no arithmetic lambda is extracted.','G.16 attempted route','no'],
 ['Malkin2020CM','Section2.2.3','12--13','Lemma3 and following paragraph','Primary arXiv2010.07238v1 PDF opened. The passage from Hodge relations to motivic and ell-adic realizations is explicitly conditional.','No unconditional etale depth-two coefficient or value of nu is inferred.','G.16 attempted route','no'],
 ['Malkin2020CM','Sections3--4','','Theorem11;Theorems15--16;remark after Theorem15','Second-shuffle Hodge correlator and Bianchi-complex statements inspected, including the averaged-basepoint construction.','The source treats a different torsion-punctured/averaged-basepoint setting; the specific once-punctured tangential arithmetic comparison remains missing.','G.16 attempted route','no']
]
with (sec/'G_nonmet_readings.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['cote','scan','folio','equation','reading','resolution','used_by','doubtful']);w.writerows(rows)
print('Saved G_nonmet_results.json, G_nonmet_coverage.json, G_nonmet_readings.csv')
