#!/usr/bin/env python3
"""Record the 26 full-page PNGs actually opened by root in this turn."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'notes/pdf_qa'
observations={
1:'Title, attribution, abstract and first contents entries are legible; margins and footer are clear.',
35:'Harmonic comparison A.J1–A.J4 and boxed identity fit; equation labels are separated from formulas.',
45:'Geometric pullback FCE.4–6, stack isomorphism and period matrix are readable with clear right margins.',
49:'Finite centralizer cycle formulas and both FCM tables align; matrix entries and word columns remain legible.',
103:'Local-image evaluation table and three-line generator display fit without collision or clipping.',
171:'The previously repaired SVM.6 rank row has adequate spacing; source maps and equation tags are distinct.',
187:'The full four-pair IFM diagram has readable horizontal and vertical arrows; IFM.6 and the following heading fit.',
191:'FBO.21–25, including nested characteristic quotients, have clear exponents and tag spacing.',
195:'DDP.11 and the transition to involution recognition are clean; ICR.1–2 fit above the footer.',
202:'The full binary canonical model and CMC.10–14 are readable; long certificate filenames wrap within margins.',
206:'ICF.8–9 and the new cone input retain clear arrows, superscripts and bounds; no overlapping text.',
210:'The orbifold transport proof, source paragraph and start of BCV.1 are legible; the section transition fits.',
214:'A.4.57 statement and FCP.9–13 bounds/actions fit; large exponents are clear and tags do not collide.',
218:'The transition from finite exclusion to A.4.58 is clean; mixed coefficient orders and fibre-product displays fit.',
222:'QCS.7–12 and the full quaternary canonical relation model are visually clean; the prose about twice the commutator class is being clarified in a subsequent source repair.',
226:'ICS.13–14, integral compatibility rows, reproduction paths and the following section heading fit cleanly.',
247:'The signed-frame equalizer proof and B.X14–17 covariance displays are legible and within margins.',
260:'Canonical-cover proof, B.M8–10 displays and the finite order at the bottom are readable without clipping.',
264:'The full central-kernel dimension table has aligned columns; B.N5–6 and the final frame display fit.',
268:'The normalized descent comparison and B.Q9–10 formulas have readable nested superscripts and clear margins.',
283:'The finite cusp-obstruction statement and composition formulas B.S26–31 are readable without overlap.',
320:'Origami covering formulas B.O8–10 fit; long program paths wrap, and the next theorem heading remains attached to its text.',
331:'The C.2.2 local counterexample, modular numeric identities and rational inverse maps are legible with clear spacing.',
345:'Cohomological complexes and the long exact sequence fit; inline superscripts and the final paragraph are readable.',
383:'The open dense failure statement and its proof use clear paragraph spacing and consistent margins.',
408:'Bibliography entries 41–46 are legible; exact source locations and long URLs wrap within margins.'}
assignment=json.loads((OUT/'checkpoint10_assignments.json').read_text())
assert set(observations)==set(assignment['assignments']['root'])
rows=[{'page':n,'visually_inspected':True,'observations':observations[n],
       'png_sha256':hashlib.sha256((OUT/f'page_{n:03d}.png').read_bytes()).hexdigest()}
      for n in sorted(observations)]
data={'inspector':'root','pdf_sha256':assignment['pdf_sha256'],'pages':rows}
(OUT/'checkpoint10_root.json').write_text(json.dumps(data,indent=2)+'\n')
print('Recorded 26 actual full-page root inspections.')
