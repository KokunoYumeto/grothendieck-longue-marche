import json
from pathlib import Path

ROOT=Path('/workspace/scratch/d7279cb02214')
WORK=ROOT/'SP92_C13_150+151_work'
PACK=json.loads((ROOT/'reading_packets/151_scan003/packet.json').read_text())
C,H=PACK['witness_C'],PACK['witness_H']
T=(WORK/'records/151_scan003.tex').read_text()
MAN=json.loads((WORK/'records/151_scan003_crop_manifest.json').read_text())
CR={x['name']:x for x in MAN}
R={'page':'151_scan003','cote':'151','scan':'3','reader':'reader_b',
   'model':'GPT-6 Astra Pro','effort':'not exposed','run':'SP92',
   'line_count':None,'half_review':'The whole source was viewed once for layout, then both supplied native overlapping halves were viewed once and read throughout against C and H. All words, coordinates, subscripts, arrows, brackets, cancellations, marginal formulas and both foliations were read; all 40 saved crops were individually viewed. Some existing crops were reopened for still-open local distinctions; no OCR, research or compilation was used.',
   'deletion_insertion_review':[],'changes':[],'diff_coverage':[],'decisions':[],
   'inventory':[],'notes':'','check_events':[],'notation':[],'hand_log':[],
   'abbreviations':[],'doubts':[],'second_boxes':[],'crop_manifest':MAN,
   'status':'core collation saved; coverage and inventory being assembled'}

KINDS={1:'misread symbol or index',2:'misread word',3:'omission',4:'drawing or diagram',5:r'readable ink left as \ill{}',6:'insertion or placement',7:'deletion state (struck given live or live given struck)',8:'abbreviation expanded or spelling modernised',9:'text not on the page',10:'other'}
def add(place,c,h,f,ev,crop,code=1,ac=False,ah=True,conf='high',conseq=False,typ='reading change',marked=False):
    item={'id':f'C{len(R["changes"])+1:02d}','place':place,'C':c,'H':h,'final':f,
          'evidence':ev,'crop':CR[crop]['crop'],'box':CR[crop]['box'],
          'confidence':conf,'kind':KINDS[code],'error_kind':code,
          'against_C':ac,'against_H':ah,'consequential':conseq,
          'change_type':typ,'marked_in_H':marked}
    R['changes'].append(item)

cline=C.splitlines()[3]
hline=H.split('\\begin{tikzcd}[column sep=large]\n',1)[1].split('\n',1)[0]
tline=T.splitlines()[3]
add('Upper diagram: all live arrow paths',cline,hline,tline,
    'Two independent left-facing shafts join E1 to E0, three left-facing shafts join E2 to E1, one upper right-facing arc joins E0 to E1, and three upper right-facing arcs join E1 to E2. Each terminal is separately visible. H draws only four paths and discusses the others in editorial prose.', 'top_diagram',4,conseq=True)
add('Upper diagram: middle return label, M0734',r'\unsure{p_{23}}',r'p_{23}',r'p_{23}',
    'The shaft crosses the label, but the p ascender and lower loop, the low bent 2 with right foot, and the separate double-lobed 3 remain distinguishable. The whole diagram was checked with the tight label crop.', 'top_returns',ac=True,ah=False,conf='medium',typ='doubt resolution')
add('Upper diagram: bottom return label',r'p_{13}',r'p_{31}',r'p_{13}',
    'After p the first numeral is a short single upright; the second has two right-facing turns. The written order is 1 then 3. H names p31 in its prose replacement of the omitted return arrows.', 'top_returns',conseq=True)
for n in (2,3):
    add(f'Upper diagram: group glyph with subscript {n}, M{733+n:04d}',
        rf'\unsure{{\mathfrak S_{n}|\mathcal G_{n}}}',rf'\mathfrak{{S}}_{n}',rf'\mathcal G_{n}',
        'The outline is an open rounded outer bowl with a curled upper tip and an inward horizontal return ending in a loop. It repeats in both prose names and the lower diagram. The visible glyph is G-like; the nature of the permutation group does not supply an S.',
        'top_groups',ac=True,conf='medium',typ='doubt resolution')
for n in (2,3):
    add(f'Upper diagram: vertical membership beneath G{n}',r'\arrow[d,phantom,"\ni" rotate=90]','',r'\arrow[d,phantom,"\in" rotate=90]',
        'The sign opens upward and has a middle upright, producing three upward tines. Rotating in by +90 degrees gives that drawn orientation; rotating ni by +90 would open downward. H replaces this vertical relation with editorial prose.',
        'top_groups',4,ac=True)
draft=C[C.index(r'\deleted{\diagram'):C.index(r'\[\boxed{\begin{aligned}')]
add('Cancelled three-arrow draft below the upper diagram',draft.strip(),'',draft.strip(),
    'Three broad arcs end in separate right-facing tips and are crossed by diagonal hatching. The first two delta labels are partly covered and retain their local doubts; the third delta3 is exposed. H describes this draft but does not transcribe its paths and cancelled labels.', 'top_cancel_arrows',4,marked=True)
for n,xyz in [(3,'x,x,y'),(1,'y,x,x'),(2,'x,y,x')]:
    add(f'Delta coordinate box: punctuation after delta{n}',rf'\delta_{n}(x,y)&=({xyz})',rf'\delta_{n}(x,y) = ({xyz}),',rf'\delta_{n}(x,y)&=({xyz})',
        'The row ends with the closing parenthesis, followed by clear blank space before the box boundary. There is no detached comma after the coordinate tuple.', 'delta_coordinates',9)
add('Upper-right coordinate trial: cancellation state',r'\deleted{$\delta_1\sigma(x,y)=(y,y,x)$}',r'$\delta_1\sigma(x,y) = \uncertain{(y,y,x)}$',r'\deleted{$\delta_1\sigma(x,y)=(y,y,x)$}',
    'Two sustained near-horizontal strikes traverse the full expression from delta1 through the final parenthesis. The lower tails and the tuple (y,y,x) remain readable; H prints the expression without a struck wrapper.', 'top_margin',7,marked=True)
add('Upper-right note: separate equality sign',r'$=$','',r'$=$',
    'Two short parallel horizontal bars sit below the cancelled trial. A curved leader descends from the upper expression to this separate equality; it is not a third slash making an inequality.', 'top_margin',3)
add('Upper-right note: first letter of lower live product',r'\sigma_3\delta_3',r'\delta_3\delta_3',r'\unsure{\sigma|\delta}_3\delta_3',
    'The first glyph has a low closed loop and a projecting top bar, favoring sigma, but internal retracing also leaves a delta-like spine. The following delta and both subscript3 forms are clear. The uncertainty is confined to the first glyph.', 'top_margin',conf='medium',conseq=True)
add('Author page number at upper right',r'\mspage{\textcircled{1}}','',r'\mspage{\textcircled{1}}',
    'A dark upright 1 lies inside a large closed oval. Its weight matches the manuscript formulas and differs from the later thin lower foliation.', 'circled1',3)
add('Two p-sigma relations: final stop',r'p_0=p_1\sigma',r'$p_0 = p_1\sigma$.',r'p_0=p_1\sigma',
    'The final sigma has its own rightward terminal; no detached full stop follows it. The newly narrowed uncertainty on the first p subscript is recorded separately in doubts.', 'p_relations',9)
add('Projection coordinate box: replaced subscript in second row',r'p_{\deleted{\unsure{21}}\inserted{23}}',r'p_{23}',r'p_{\deleted{\unsure{21}}\inserted{23}}',
    'An older pair of small digits is crossed at the lower subscript position, with a fresh 23 visibly raised above it. The old pair remains uncertain because the cancelling line covers its joins. The insertion attaches to this p, not the argument tuple.', 'projection_cancel',6)
for sub,xyz in [('12','x,y'),('23','y,z'),('31','z,x')]:
    cc=(rf'p_{{{sub}}}(x,y,z)&=({xyz})' if sub!='23' else rf'p_{{\deleted{{\unsure{{21}}}}\inserted{{23}}}}(x,y,z)&=({xyz})')
    add(f'Projection coordinate box: punctuation after p{sub}',cc,rf'p_{{{sub}}}(x,y,z) = ({xyz}),',cc,
        'The closing parenthesis is followed by blank paper up to the enclosing box; no independent comma is written after this row.', 'projection_coordinates',9)
add('Right-margin rho coordinates: final stop',r'\rho(x,y,z)=(y,z,x)',r'\rho(x,y,z) = (y,z,x).',r'\rho(x,y,z)=(y,z,x)',
    'The final parenthesis ends the formula. The mark near it belongs to that curved stroke; there is no separate baseline stop.', 'rho_margin',9)
for sub,n,punc in [('12',3,','),('23',1,','),('31',2,'.')]:
    add(f'Sigma-projection relations: punctuation after p{sub} row',rf'\sigma p_{{{sub}}}&=p_{{{sub}}}\sigma_{n}',rf'\sigma p_{{{sub}}} = p_{{{sub}}}\sigma_{n}{punc}',rf'\sigma p_{{{sub}}}&=p_{{{sub}}}\sigma_{n}',
        'The terminal subscript ends the row and is followed by open paper. There is no independent comma or full stop at the position supplied by H.', 'sigma_relations',9)
add('Cancelled coordinate arrow chain at centre',r'\deleted{\[(x,y,z)\longrightarrow(y,z,x)\longrightarrow(y,z)\]}','',r'\deleted{\[(x,y,z)\longrightarrow(y,z,x)\longrightarrow(y,z)\]}',
    'All three parenthesized tuples and two connecting shafts remain visible under the long crossing strokes. The draft is separately cancelled and is not part of the adjacent live three-row identity boxes.', 'cancelled_coordinates',3)
add('Third delta-rho identity: small raised terminal mark',r'\rho^2\delta_2\unsure{\,a}','',r'\rho^2\delta_2{}^{\unsure{a}}',
    'A tiny loop and short return stand above and to the right of the last delta2. It is raised rather than on the formula baseline; its identity remains a narrow a-like doubt. No letters are supplied from the formula meaning.', 'delta_relations',6,ac=True,conf='low')
add('Cancelled small glyph before Il',r'\deleted{\unsure{a}}','',r'\deleted{\unsure{a}}',
    'A small loop with a descending/returning stroke is crossed before the separate live capital I. The crossing prevents certainty about the old glyph; it is not a live initial letter of Il.', 'prose_cancel',3,conf='low')
add('Opening prose verb, M0738',r'\unsure{avoir|donner}',r'se donner',r'avoir',
    'The word begins with a low closed a, followed by a pointed v, rounded o, short dotted i and terminal r. There is no initial tall d and no separate se between de and this word. The literal wording de avoir is retained.', 'prose_avoir',2,ac=True,typ='doubt resolution')
add('Prose preposition before les trois ensembles',r'entre',r'avec',r'entre',
    'The initial low e is followed by n, a tall crossed t, then r and e. The vertical crossed stroke in the middle rules out avec.', 'prose_entre',2)
for n,mark in [(2,'M0739'),(3,'M0740')]:
    add(f'Prose group name with subscript {n}, {mark}',rf'\unsure{{\mathfrak S_{n}|\mathcal G_{n}}}',rf'\mathfrak{{S}}_{n}',rf'\mathcal G_{n}',
        'The letter has the same large open outer bowl, upper curl and inward return as the corresponding symbols in both diagrams. The small subscript is separately visible. The glyph is read G without inferring the group name from the mathematics.', 'prose_groups',ac=True,conf='medium',typ='doubt resolution')
add('After boxed p0 delta0 identity: alleged comma',r'\boxed{p_0\delta_0=\mathrm{id}_{E_0}},',r'\boxed{p_0\delta_0 = \mathrm{id}_{E_0}},',r'\boxed{p_0\delta_0=\mathrm{id}_{E_0}}',
    'At the box right edge the descending and curved traces connect to the adjacent cancelled p draft. There is no separately identifiable comma between the live box and that draft; the exact local attachment is retained as a narrow punctuation doubt in metadata.', 'p0_identity',9,ac=True,conf='medium')
add('Cancelled draft beside first identity box',r'\deleted{\unsure{p_1\delta_0}}','',r'\deleted{\unsure{p_1\delta_0|p_{12}\delta_0}}',
    'The p, a small lower numeral area and delta0 are crossed beside the box. A low footed trace before delta may be an additional 2; the cancelling strokes do not permit a firm expansion of the index. The old expression remains struck, while the neighbouring boxed identity is live.', 'cancelled_p1',3,conf='low')
add('Main chain: first delta3 and its underannotation',r'p_{12}\underbrace{\delta_3}_{\rho\deleted{\unsure{{}^2|\sigma}}\delta_1}',r'p_{12}\,\underbrace{\rho\delta_1}_{\delta_3}',r'p_{12}\underbrace{\delta_3}_{\rho^{\deleted{\unsure{2|\sigma}}}\delta_1}',
    'The live delta3 is on the main equality baseline after p12. A bracket below it carries rho, a crossed raised glyph, and delta1. H interchanges the upper term and the lower annotation.', 'main_chain',6,conseq=True)
add('Main chain: cancelled raised glyph after underwritten rho',r'\rho\deleted{\unsure{{}^2|\sigma}}\delta_1','',r'\rho^{\deleted{\unsure{2|\sigma}}}\delta_1',
    'Between the annotation rho and delta1 is a small raised glyph crossed independently by short strokes. Its contour can be 2 or sigma under the cancellation. Only that raised glyph is struck, not the rho or following delta1.', 'chain_cancel1',3,conf='low')
add('Main chain: underlabel of p23',r'\underbrace{p_{23}}_{p_{12}\rho}',r'p_{23}',r'\underbrace{p_{23}}_{p_{12}\rho}',
    'The bracket directly under p23 carries a complete p12 rho; its p stem, digits1 and2 and following rho are separate and readable.', 'main_chain',3,conseq=True)
add('Main chain: cancelled underlabel of following delta1',r'\underbrace{\delta_1}_{\deleted{\unsure{\rho}}}',r'\delta_1',r'\underbrace{\delta_1}_{\deleted{\unsure{\rho}}}',
    'A short independent bracket below this delta1 carries a densely crossed rho-like loop and stem. It does not cancel the main delta1 or the neighbouring p23 annotation.', 'chain_cancel2',3,conf='low')
add('Main chain: underlabel of p31',r'\underbrace{p_{31}}_{p_{12}\rho^2}',r'p_{31}',r'\underbrace{p_{31}}_{p_{12}\rho^2}',
    'Under the main p31 a separate bracket contains p12 rho2, including a distinct raised2. It is separate from the following delta2 annotation.', 'main_chain',3,conseq=True)
add('Main chain: final delta2 and its underannotation',r'\underbrace{\delta_2}_{\rho^2\delta_1}',r'\underbrace{\rho^2\delta_1}_{\delta_2}',r'\underbrace{\delta_2}_{\rho^2\delta_1}',
    'The delta2 is visibly on the main equality baseline. Rho2 delta1 is below its own bracket, not in the main product. The long diagonal nearby separates annotations and is not an algebraic slash.', 'main_chain',6,conseq=True)
add('Main chain: final punctuation',r'\underbrace{\delta_2}_{\rho^2\delta_1}',r'\underbrace{\rho^2\delta_1}_{\delta_2}.',r'\underbrace{\delta_2}_{\rho^2\delta_1}',
    'The last main delta2 and its lower annotation have no detached following full stop.', 'main_chain',9)
add('Boxed sigma delta0 identity: punctuation',r'\boxed{\sigma\delta_0=\delta_0}',r'\boxed{\sigma\delta_0 = \delta_0},',r'\boxed{\sigma\delta_0=\delta_0}',
    'The formula is enclosed by its own rectangular box; no comma follows the final delta0 or the right edge of that box.', 'sigma_delta0',9)
ie=C[C.index(r'\deleted{\[\text{i.e.}'):C.index(r'\deleted{\[\underbrace{(p_{12}\rho)}')].strip()
add('Cancelled i.e. equality chain',ie,'',ie,
    'The complete i.e. chain is visible under an enclosing cancellation and long diagonals: delta0 p0, p12 delta1 with sigma underneath, p12 rho delta1 with id underneath, and p12 rho2 delta1. The first and last terms also have brackets. H mentions this second chain editorially but does not transcribe it.', 'cancelled_ie',3,conseq=True,marked=True)
add('Cancelled inequality: right-hand p index',r'\unsure{p_{23}|p_{22}|p_{12}}',r'p_{23}',r'\unsure{p_{22}|p_{12}|p_{23}}',
    'The first small digit has an angled upper entry followed by a low hooked rightward foot, unlike the nearly straight1 in the left-hand p12. The second has a curved top and broad rightward foot like2. These contours favor22, while12 and23 remain alternatives under the cancellation. The first reading is changed from23 to22 without asserting certainty.', 'cancelled_inequality',ac=True,conf='low')
add('Cancelled inequality: first underlabel',r'\underbrace{(p_{12}\rho)}_{p_{23}}',r'(p_{12}\rho)',r'\underbrace{(p_{12}\rho)}_{p_{23}}',
    'A bracket beneath the first parenthesized product carries p23, partly crossed by the enclosing cancellation. The 2 and double-lobed3 remain identifiable.', 'cancelled_inequality',3)
add('Cancelled inequality: final underlabel delta2',r'\unsure{\delta_2|\delta_3}','',r'\delta_2',
    'The lower delta has an exposed upper cap and lower loop. Its subscript has one curved upper turn, diagonal descent and a broad flat right foot, unlike the two open lobes of3 elsewhere in this crop. The visible strokes support2 despite the diagonal crossing.', 'cancelled_inequality',ac=True,conf='medium',typ='doubt resolution')
add('Cancelled inequality: author question position',r'\overset{??}{\ne}',r'\neq p_{23}(\rho\delta_1) \qquad ??',r'\overset{??}{\ne}',
    'Two separate question curves with detached dots sit above the not-equal sign, not at the end of the expression. Their placement and the cancellation are preserved.', 'cancelled_inequality',6)
add('Three-value box: delta3 label above the first rho delta1',r'\overbrace{\rho\delta_1}^{\delta_3}',r'\underbrace{\rho\delta_1}_{\delta_3}',r'\overbrace{\rho\delta_1}^{\delta_3}',
    'The bracket is above rho delta1 and its delta3 label is still higher; the first value row is distinct from the lower underbrace on the second row.', 'values_box',6)
add('Three-value box: cancelled small subscript beside rho squared',r'\rho^2',r'\rho^2',r'\rho_{\deleted{\unsure{1}}}^{2}',
    'A separate short upright sits below and right of rho, crossed by two short transverse strokes. It is independent of the live raised2 and following delta1. The crossed numeral is only tentatively1. The rho body itself is retraced without a separable old letter.', 'values_rho',3,ac=True,conf='low')
for ff,hh,lab in [(r'\boxed{\sigma_3\delta_1=\delta_1}',r'\boxed{\sigma_3\delta_1 = \delta_1},','upper'),(r'\boxed{p_{12}\sigma_3=\sigma p_{12}}',r'\boxed{p_{12}\sigma_3 = \sigma p_{12}},','lower')]:
    add(f'Right-margin {lab} box: punctuation',ff,hh,ff,
        'The relation ends at its last numeral inside the surrounding box. There is no detached comma after the formula or beside the right box edge. The upper sigma subscript is unmistakably3, and both delta subscripts there are1.', 'margin_values',9)
add('Cancelled label above lower diagram',r'\deleted{$\unsure{(\mathrm{Ens})|\mathrm{ens}}$}','',r'\deleted{$\unsure{(\mathrm{Ens})|\mathrm{ens}}$}',
    'The old label is crossed above the box; an opening parenthesis-like upright, E/e-like body, n turns and final s-like diagonal remain. The strikes prevent certainty about capitalization and both parentheses, so the C doubt is retained.', 'cancelled_Ens',3,conf='low')
lowcline=C[C.index('E_0\\arrow[r,bend right=30'):C.index('E_0\\arrow[r,bend right=30')+len(C[C.index('E_0\\arrow[r,bend right=30'):].splitlines()[0])]
add('Lower boxed diagram: objects and four maps',lowcline,'',lowcline,
    'Inside a distinct rectangular box, E0,E1,E2 lie in one row. Straight left-facing arrows are labelled p0 and p12; lower curved right-facing arrows are labelled delta0 and delta1. All four tips and labels are exposed. H omits this entire second diagram.', 'lower_diagram',4,conseq=True)
for n,mark in [(2,'M0741'),(3,'M0742')]:
    add(f'Lower diagram: group glyph with subscript {n}, {mark}',rf'\unsure{{\mathfrak S_{n}|\mathcal G_{n}}}','',rf'\mathcal G_{n}',
        'The open bowl, curled upper tip and inward horizontal loop repeat the four live group glyphs higher on the page. The lower2 or double-lobed3 is clearly distinct from the letter. The written G shape is retained independently of the groups mathematical identification.', 'lower_groups',ac=True,conf='medium',typ='doubt resolution')
add('Lower diagram: cancelled group-like label above E0',r'\deleted{\unsure{\mathfrak S_1}}','',r'\deleted{\unsure{\mathcal G|\mathfrak S}_{\unsure{2|1}}}',
    'The left glyph and its following numeral are crossed together. Its exposed outer loop permits G or S, while the numeral has a long descending diagonal and broad low rightward foot favoring2 over1. Both uncertainties remain local; the live G labels do not remove the struck glyph doubt.', 'cancelled_group1',3,ac=True,conf='low')
add('Final boxed rho/sigma identity: following punctuation',r'\boxed{\rho\delta_1\delta_0=\sigma_1\delta_1\delta_0=\delta_1\delta_0}',r'\boxed{\rho\,\delta_1\delta_0 = \sigma_1\,\delta_1\delta_0 = \delta_1\delta_0},',r'\boxed{\rho\delta_1\delta_0=\sigma_1\delta_1\delta_0=\delta_1\delta_0}',
    'The last delta0 ends the row within its box, with no independent comma afterwards. The sigma subscript is a serifed1 with a single upright, not a two-bend2.', 'final_box',9)
add('Bottom formula: left underlabel, M0743',r'p_{\unsure{1|2}}','',r'p_{\unsure{2|1}}',
    'The numeral after the lower p has a bent upper stroke, oblique descent and substantial rightward foot, favoring2. Its lowest tip meets the page edge, so1 remains an alternative. The full formula and bracket attachment were reread; no expected index was substituted.', 'final_formula',ac=True,conf='medium',conseq=True)
add('Bottom formula: crossed sigma before rho squared',r'\deleted{\unsure{\sigma}}','',r'\deleted{\unsure{\sigma}}',
    'A dense crossed oval and projecting upper bar stand after p12 and before live rho2. The cancellation is confined to this old sigma-like glyph. Rho and its exponent remain live; the old letter stays uncertain.', 'final_cancel',3,conf='low')
add('Bottom formula: final live sigma2 factor',r'\sigma_2','',r'\sigma_2',
    'After rho2 and outside the inner lower bracket, there is a clean sigma with a distinct footed subscript2. It lies within the wider upper bracket and is absent from H.', 'final_formula',3,conseq=True)
add('Bottom formula: outer upper bracket and p12 label',r'\overbrace{\underbrace{p_{12}\deleted{\unsure{\sigma}}\rho^2}_{p_{31}}\sigma_2}^{p_{12}}',r'\underbrace{p_{12}\rho^2}_{p_{31}}',r'\overbrace{\underbrace{p_{12}\deleted{\unsure{\sigma}}\rho^2}_{p_{31}}\sigma_2}^{p_{12}}',
    'A long upper bracket spans the right-hand product from p12 through sigma2 and carries p12 above it. A distinct lower bracket ends at rho2 and carries p31. H retains only the lower bracket. The separate cancelled glyph and sigma2 factor are recorded in their own rows.', 'final_formula',6,conseq=True)
add('Bottom formula: final full stop',r'\sigma_2}^{p_{12}}',r'\underbrace{p_{12}\rho^2}_{p_{31}}.',r'\sigma_2}^{p_{12}}',
    'No independent full stop follows the final sigma2 or the upper p12 label. The lower annotations meet the trimmed sheet edge.', 'final_formula',9)
add('Later lower-left foliation',r'\margin{2}','',r'\margin{2}',
    'A slender grey2 has a rounded upper turn, long sloping diagonal and short horizontal foot. Its thin stroke and marginal position distinguish it from the dark authorial circled1 above.', 'folio2',3)

def decision(mid,dec,read,ev,crop,conf):
    R['decisions'].append({'id':mid,'cote':'151','scan':'3','decision':dec,'reading':read,'ink':ev,'crop':CR[crop]['crop'],'box':CR[crop]['box'],'confidence':conf})
decision('M0734','first',r'p_{23}','The p ascender/loop, bent footed2 and detached double-lobed3 survive the crossing arrow shaft. Whole diagram and tight middle-return crop checked.','top_returns','medium')
for mid,n,cr in [('M0735',2,'top_groups'),('M0736',3,'top_groups')]:
    decision(mid,'alternative',rf'\mathcal G_{n}','Large rounded open bowl, curled upper tip and inward looped return; same contour in all six live occurrences. Group identity is not used to replace the visible letter. ',cr,'medium')
decision('M0737','undecided',r'{}^{\unsure{a}}','Tiny raised loop-and-return after the last delta2; no secure letter beyond an a-like shape. Raised placement is clear but identity is not.','delta_relations','low')
decision('M0738','first','avoir','Low a, pointed v, rounded o, dotted i and terminal r; no initial d ascender, no separate se.','prose_avoir','high')
for mid,n,cr in [('M0739',2,'prose_groups'),('M0740',3,'prose_groups'),('M0741',2,'lower_groups'),('M0742',3,'lower_groups')]:
    decision(mid,'alternative',rf'\mathcal G_{n}','Open outer bowl, curled upper terminal and inward return match the repeated live G construction; subscript remains separate.',cr,'medium')
decision('M0743','undecided',r'\unsure{2|1}','Upper bend, oblique descent and rightward foot favor2, but the sheet edge clips the lowest part. First reading reordered without claiming full resolution.','final_formula','medium')

(WORK/'records/151_scan003.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n')
print(f'Saved {len(R["changes"])} core changes and {len(R["decisions"])} decisions')
