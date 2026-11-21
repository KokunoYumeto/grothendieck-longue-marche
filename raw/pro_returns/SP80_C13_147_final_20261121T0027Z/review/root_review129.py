from pathlib import Path
import json
R=Path('edition');d=json.loads((R/'reports/147_scan129_report.json').read_text())
for i in (2,8,12,19):d['rows'][i]['math_consequential']=False
# Store actual witness text or a truly empty span, never a fabricated editorial gloss.
d['rows'][1]['H']=r'\begin{aligned}'
d['rows'][14]['H']=''
d['rows'][22]['H']=''
hnote=next(x for x in Path('packets/147_scan129/H.tex').read_text().splitlines() if x.startswith(r'\note{diagramme (209)'))
for i in (20,21):
    d['rows'][i]['H']=hnote
    d['rows'][i]['kind']='insertion or placement'
    d['rows'][i]['error_category']='Insertions put in the wrong place'
    d['rows'][i]['math_consequential']=False
    d['rows'][i]['scan_shows']+=' H recognizes this source text in its editorial note; the difference here is its placement outside the actual diagram, not a failure to recognize the text.'
# The index alternatives narrow, but the whole glyph remains uncertain in case.
d['decisions'][4]['decision']='undecided'
d['decisions'][4]['ink']+=' Because the capital/lower-case glyph is still undecided, the complete mark is not counted as fully resolved.'
links={0:[2,3,8],1:[5],2:[6],3:[7],4:[7]}
for i,e in enumerate(d['check_events']):e['statement_id']+='; '+'; '.join(f'N129-{j:02d}' for j in links[i])
d['check_events'].append({'statement_id':'N129-01; N129-04; N129-09; N129-10; N129-11','type':'used and rechecked in this run','outcome':'Root inspected all12 crops, the bracket extents, insertion attachment, retraced layers and written numbers. This is a visual/coverage review, not a proof of the geometric claims. The packet incident is documented separately.'})
d['notes'].append('MC129-R: root checked the covering-base refinement by path lifting. If q:B′→B is a covering and E′=E×_B B′, lifting paths and homotopies gives an equivalence Π₁(E′)≃Π₁(E)×^h_{Π₁(B)}Π₁(B′). In the flag-cover situation described on scan128, this explains why unstarred lower D bases can be compatible with the starred P pullback. The proof is conditional on the covering/pullback hypotheses; it does not establish every analytic identification of the manuscript and does not decide any overwritten star. See review/mathematical_checks.md, MC129-R.')
d['check_events'].append({'statement_id':'MC129-R; N129-12','type':'targeted proof check','outcome':'Root checked essential surjectivity by lifting the comparison path to B′, and full faithfulness by uniqueness of path/homotopy lifting. This verifies the stated conditional covering-base refinement, not the unrestricted generalization or every manuscript hypothesis.'})
(R/'review/147_scan129_reviewed.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
with (R/'notation.md').open('a') as f:f.write('\n- Scan129: the small base after sur is D_0/d_0, with no separate extra d. Named Pi variables are capital; the low operator Pi/pi case remains uncertain. The lower209 D bases are bare or locally bare/star doubtful as recorded. One-sided connector turns are drawn literally. The first206 brace stops before i.e.;209 begins with a curve and has an uncertain first digit.\n')
with (R/'review/root_visual_readings.md').open('a') as f:f.write('\n### Scan129 final return review\nAll12 crop findings accepted. Four pure connector-geometry rows are excluded from mathematical-correction counts. H’s source-number and central-label recognition in its editorial note is recorded honestly as placement, not omitted recognition. The D_0/d_0 mark remains undecided overall even though the additional-d alternative has been excluded. All12 notes have scoped check-event links, including the root covering-base proof.\n')
