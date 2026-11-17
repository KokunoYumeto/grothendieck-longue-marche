#!/usr/bin/env python3
"""Record the23 complete page images actually opened and inspected by root."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1];directory=ROOT/'notes/pdf_qa'
assignments=json.loads((directory/'checkpoint08_assignments.json').read_text())
observations={
1:'Full title, author credit, abstract and first contents entries inspected. Typography, margins and footer are clear.',
34:'A.5 transition and A.J1--A.J3 inspected. Long normalized-frame display and boxed equation fit without overlap.',
44:'FCE.4--FCE.6 geometric pullback, inverse formulas and integral matrix inspected; all tags and text remain inside margins.',
48:'FCM.6--FCM.10 graph formulas, obstruction row and complete six-row table inspected. Matrix entries and table labels are readable.',
131:'Finite braid proof ending and A.4.38 opening inspected. Quotient arrows and OCM.1 orders fit; subsection starts cleanly.',
135:'FEC.2--FEC.7 inspected, including large explicit bounds, finite-locus inclusion and cusp-cycle formula; no collisions or clipping.',
139:'FEC.25--FEC.26, central recovery and next subsection inspected. Long program path breaks cleanly; new heading has following text.',
143:'FGA.13--FGA.15 and finite sewing/center-killing paragraphs inspected. Two-line formula, powers and center map are clear.',
147:'OGS.4--OGS.9 signed frames and auxiliary word inspected. The cap-defect display, actual matrices and six-deck equation fit.',
151:'MFP.1--MFP.4 actual re-marking and A.4.42 opening inspected. The period comparison and first discrepancy displays are readable.',
155:'CDF.9 and MFP.5--MFP.7 inspected. Full fibre-product map, order and factorization fit without tag overlap.',
159:'COB.4--COB.9 inspected. The free-product marking, Heisenberg law and three affine maps fit on their intended lines.',
163:'TMR.9--TMR.11 modular gate and following distribution section inspected. Source-fibre equations and dual obstruction fit.',
181:'B.K11--B.K13 and B.X1 inspected. Long conjugation formula and new subsection have clear spacing.',
197:'B.M8--B.M10 inspected. Framed fibre equations, cohomology kernel and large exact order are fully visible.',
201:'B.N3--B.N6 inspected. The cohomology-dimension table and all final three-line frame equations are legible and bounded.',
205:'B.Q9--B.Q10 proof page inspected. Dense proof text, displayed images and compactness set remain clear within margins.',
220:'B.2.19 and B.S26--B.S31 inspected. Crossed-homomorphism law, index expression and two-line frame equations have no overlaps.',
248:'B.AD4--B.AD7 full harmonic proof inspected. Repaired paragraph headers, matrix product law and final determinant line are clean.',
257:'B.O8--B.O10 origami proof ending inspected. Cover formulas and breakable program path fit; next subsection is properly spaced.',
268:'C.2.2 explicit ghost and covering model inspected. Products, modular calculation and mutually inverse rational formulas are legible.',
281:'C.1.13 localization statement and proof inspected. Long exact sequence and derived triangles fit without clipping.',
290:'C.1.19 and C.2.5 openings inspected. Twenty-four-section formula, invariant equation and factorial products are clear.'}
assert set(observations)==set(assignments['assignments']['root'])
sha=hashlib.sha256((ROOT/'GT_TOWER_CHECK_paper.pdf').read_bytes()).hexdigest()
assert sha==assignments['pdf_sha256']
rows=[{'page':page,'visually_inspected':True,'observations':observations[page],
       'png_sha256':hashlib.sha256((directory/f'page_{page:03d}.png').read_bytes()).hexdigest()}
      for page in sorted(observations)]
(directory/'checkpoint08_root.json').write_text(json.dumps({
    'pdf_sha256':sha,'inspector':'root','pages':rows},indent=2)+'\n')
print('Recorded23 actual full-page root inspections, with exact PNG hashes.')
