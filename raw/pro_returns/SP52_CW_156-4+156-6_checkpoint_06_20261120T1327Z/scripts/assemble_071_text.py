from pathlib import Path
O=Path(__file__).resolve().parents[1];K='156-4_071'
r1=(O/'readers'/K/'R1/reading.tex').read_text();r2=(O/'readers'/K/'R2/reading.tex').read_text()
t=r2[:r2.index('% Cancelled draft, written upside down.')]
t=t.replace('% R2-margin-marks:', '% G1 margin-mark columns:').replace('% R2-corollary-correction:', '% G2 corollary correction:').replace('% R2-itou-mark:', '% G3 itou high mark:').replace('% R2-right-punctuation:', '% G4 right punctuation:')
t=t.replace('% G2 corollary correction: de is crossed by the long rising stroke under the raised addition.', '% G2: the long rising stroke crosses de beneath the raised addition; deletion versus a crossing insertion arm remains uncertain.')
t=t.replace(r'{\deleted{de}};',r'{\unsure{\deleted{de}|de}};')
t=t.replace(r'{\inserted{dans $\mathcal F$}};',r'{\inserted{dans $\unsure{F|\mathcal F}$}};')
t=t.replace(r'non \unsure{seult|seulemt} pour','non seult pour')
t=t.replace(r'\unsure{itou|itout}',r'\unsure{itou}')
t=t.replace(r'cf page $67$)',r'cf \unsure{pg|page|pge} $67$)')
folio=r'\mspage{5\rlap{\deleted{\unsure{4|3}}}5}'
t+='''% The following two-position folio and draft are upside down on the sheet.
% The second numeral is overwritten; the broad cancellation strokes start below the folio.
'''+folio+'\n\n'
draft=r1[r1.index('% fig:inverted-cancelled-draft.'):]
draft=draft.replace('% fig:inverted-cancelled-draft.', '% G5 inverted cancelled draft.')
draft=draft.replace(r'\begin{scope}[rotate=180]',r'\begin{scope}[rotate=180,transform shape]')
old=r'\unsure{\deleted{\mathcal F}\Phi|\deleted{F}\Phi|\Phi}'
new=r'\unsure{\rlap{\ensuremath{\deleted{\mathcal F}}}\Phi|\rlap{\ensuremath{\deleted{F}}}\Phi|\Phi}'
assert old in draft;draft=draft.replace(old,new)
draft=draft.replace(r"d'inclusion\unsure{,}",r"d'inclusion,")
draft=draft.replace(r'\unsure{\mathrel{\vdash\joinrel\dashv}|\mapsto}',r'\mathrel{\vdash\joinrel\dashv}')
draft=draft.replace(r'\deleted{\unsure{ses|son} \unsure{p|par}}',r'\deleted{\unsure{ses|son}} \deleted{\unsure{p|par}}')
draft=draft.replace(r'\unsure{Dém}',r'Dém')
points='''% One detached high point after the second inner cancellation, and two low points beneath irreductibles.
\\fill (1046,970) circle (2.0);
\\fill (1663,972) circle (1.7);
\\fill (1675,979) circle (1.7);
'''
draft=draft.replace('% The boundary is open at the scan edge;',points+'% The boundary is open at the scan edge;')
t+=draft
p=O/'pages/J156-4-09_156-4_scan071.tex';p.write_text(t)
print(p)
