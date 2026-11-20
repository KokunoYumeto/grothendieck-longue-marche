from pathlib import Path
import json,copy
O=Path(__file__).resolve().parents[1]
R={a:json.loads((O/f'readers/scan075/{a}/report.json').read_text()) for a in 'ABC'}
A,B,C=[R[a]['decisions'] for a in 'ABC']
ds=[]
for k,bi,ai,ci in [(0,0,0,0),(1,1,1,1),(2,2,3,2),(3,4,None,7),(4,5,None,6),(5,6,4,3)]:
 d=copy.deepcopy(B[bi]);d['id']=f'M075-{k+1:02}'
 d['readers']={'A':A[ai]['reading'] if ai is not None else (r'\tag*{(1)}' if k==3 else ''),'B':B[bi]['reading'],'C':C[ci]['reading']}
 d['marked_in_H']='no'
 d['crop']='readers/scan075/B/'+Path(d['crop']).name
 if isinstance(d.get('alternatives'),list):d['alternatives']='; '.join(d['alternatives'])
 ds.append(d)
ds[0].update(confidence='low',scan_shows='The initial has a high diagonal entry joining a long descending stroke with a looped low turn; no separate dot is visible. Its height is comparable to the following d ascender, favoring B’s capital J candidate. A and C retain lowercase joindre. Main adds Joindre first while retaining the lowercase alternative and uncertainty in the compressed middle joins. The location as an instruction does not determine the word or its case.')
ds[1]['scan_shows']='Two distinct dark heads sit at the top of the thick left member, but their lower traces merge into one broad blue stem. The right upper and lower diagonal arms establish K. All readers and main retain the ordinary-versus-doubled left-stroke ambiguity locally; the plain K forms elsewhere do not erase this ink difference.'
ds[2]['scan_shows']='The s, c, looped h, accented e and m can be followed separately. The terminal contains several overlapping blue loops and a small rightward loop, favoring a but hiding its construction. Main agrees with all readers in retaining schéma as unsure, without inventing a recoverable deleted underletter from the grammatical expectation.'
ds[3].update(reading=r'\tag*{(1)}',diff_c=False,unresolved=False,alternatives='',confidence='high',scan_shows='A short nearly upright central stroke stands between the parentheses. The isolated upper point lies far to its left, near the upper continuation of the opening parenthesis; it is not aligned over the central stroke. B retains a possible displaced i dot, while A and C read 1. Main keeps (1), from the separation and alignment of the visible components, without using the following label (2) to supply the reading.')
ds[4]['scan_shows']='A compact grey-brown triangular/flattened trace lies distinctly below the formula, with a much paler short oblique companion to its right. C regards these as surface flecks and A adds no token; B preserves their shapes. Main retains the coherent detached shapes under an uncertainty marker, without assigning pen authorship, punctuation or a mathematical value. Their grey color differs from the blue letters; preservation does not assert that they belong to the formula.'
# Retain C's lobe contours and A's two faint adjoining traces, at their observed relative scale.
graphic=C[3]['reading'].replace(r'\end{tikzpicture}',r'''\fill[gray!65] (0.20,-0.19) .. controls (0.22,-0.13) and (0.31,-0.23) .. (0.34,-0.34)
 .. controls (0.30,-0.46) and (0.18,-0.36) .. (0.20,-0.19) -- cycle;
\fill[gray!50] (0.47,-0.50) ellipse[x radius=0.06,y radius=0.08];
\end{tikzpicture}''')
ds[5].update(reading=graphic,crop='readers/scan075/C/crops/crop_C_075_marginal_points.jpg',confidence='medium',scan_shows='The lower-left dark mark is rounded and lobed; the upper-right one is taller, with an indented right edge and a raised upper lobe. They form an ascending diagonal rather than a vertical typographic colon. Two paler traces continue below-right of the lower mark, as A records; B and C draw only the main pair. Main combines C’s lobe contours with the two faint traces, keeps the cluster beside the upper diagram row, and leaves its punctuation value and material origin unresolved.')
s=(O/'readers/scan075/B/reading.tex').read_text()
s=s.replace(B[4]['reading'],ds[3]['reading'])
s=s.replace(B[6]['reading'],'')
s=s.replace(r'\diagram{\footnotesize',graphic+'\n\n'+r'\diagram{\footnotesize')
(O/'pages/H37-01_37_scan075.tex').write_text(s)
inv=copy.deepcopy(R['B']['inventory'])
for x in inv:
 if x['hand'].startswith('his hand'):x['hand']='unnamed pencil hand; attribution not independently established'
 if x['hand'].startswith('named other hand'):x['hand']='unnamed blue-ink writer; H attributes P. Deligne'
inv[11]['element']='Sheaf-functor display with label (1)'
inv[15]['element']='Detached diagonal cluster with faint companion traces'
inv[15]['first_words_or_objects']='Two dark lobed marks, upper one to the right, and two faint lower-right traces'
notes="""Handwritten letter leaf on squared paper, dated ‘Bures sur Yvette, le 21 octobre 1968’ and addressed ‘Cher Grothendieck,’. H attributes it to P. Deligne, but this page is unsigned. The only heading is underlined ‘proposition’; no own page number or total count is written. Archive number 74 is a comment. The separate pencil note has ‘SGA 7 VI ?’ and ‘App. II’, both Roman groups ruled above and below; its opening Joindre/joindre remains uncertain.

The writer says ‘il n’est pas nécessaire de faire de savants recollages de complexes cotangents’ for the stated criterion: a compact complex analytic X is a scheme if and only if its reduction is. He reduces to a square-zero ideal, introduces analytic and algebraic infinitesimal extension groups and a cotangent complex ‘donné localement, dans la catégorie dérivée’, then gives the sheaf functors and a two-row comparison diagram. He states ‘les lignes sont exactes’ and invokes GAGA for the outer vertical isomorphisms. The unresolved task in his own words is ‘Reste à’, followed by cancelled ‘comparer les images de α et β’ and live ‘montrer que Im(β) ⊂ Im(α)’. These are the page’s claims and remaining step; no proof or computation was checked.

The cancelled supposer, singular ‘Soit’ before two groups, lowercase ‘il’ after a stop and capital ‘Idéal’ are preserved. All four C doubts remain, with an added initial-case alternative and a graphical replacement of the marginal colon. The new low grey traces remain materially unassigned. The proposed 1/i uncertainty is rejected on the crop. H is descriptive only and has no collation rows."""
math=[
'The introductory K has two dark upper traces but a merged lower stem; K versus blackboard K remains unresolved. Script N, Hom and Ext are distinguished from ordinary cohomology H and extension-group E by the repeated ink forms.',
'Diagram (2) retains the second rise of alg/an beside the H degrees: top H^{1^{alg}}, E^{alg}, H^0; bottom H^{1^{an}}, E^{an}, H^{0^{an}}. No alg is supplied to the upper-right H^0. The lowered red suffix has no clear acute, and the later round indices remain 0.',
'The reduction has a double-shaft right implication. The comparison diagram has six rightward arrows and three downward arrows, with alpha and beta on the respective final horizontal arrows. The final image inclusion has no lower equality bar. No terminal zero or extra arrow is inferred.',
'At the first display label, B proposed 1/i because of a high point. Main retains 1 with A/C: the point is displaced toward the opening parenthesis rather than aligned over the upright. This is a reading decision, not a mathematical verification.',
'The crowded final letter of schéma remains unsure; the expected phrase schéma lisse does not resolve the overwritten strokes. The grey low trace is drawn as unassigned and does not change the Ext degree.'
]
notation=copy.deepcopy(R['B']['notation'])
notation[6].update(sign='First display label',latex='(1)',evidence='Central upright with a detached point displaced toward the opening parenthesis; main rejects a dotted-i interpretation.')
notation[7]['latex']=graphic;notation[7]['evidence']='Two diagonal lobed dark forms and two faint lower-right traces; shape preserved, function and origin unresolved.'
out=dict(scan=75,decisions=ds,inventory=inv,notes=notes,math_reading_decisions=math,notation=notation,abbreviations=R['B']['abbreviations'],slips=R['B']['slips'],check_events=[],main_crops=[])
(O/'decisions/scan075.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
with (O/'workflow_assessment.txt').open('a') as f:f.write('\nScan 075: A/B/C made 5/7/8 crops. Main viewed five B crops and C’s marginal-cluster crop, with no additional crop. The page texts agreed on every diagram object and arrow. Main retained the new capital-J alternative, rejected a proposed 1/i ambiguity from the point’s offset, and recorded the low detached grey shapes without asserting authorship. The marginal graphic combines the independently observed main lobes and faint companions. Reader A adjusted its margin-anchor position after the initial text was written; the completed return and report agree. No brief change was needed.\n')
print('Wrote scan 075: six mandatory rows, three C differences, four C doubts retained/revised.')
