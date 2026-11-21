import csv
import json
import re
from pathlib import Path

OUT=Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148/readers/148_scan046')
PACKET=Path('/workspace/scratch/8132fe1cca43/work/packets/148_scan046')
C=(PACKET/'C.tex').read_text()
H=(PACKET/'H.tex').read_text()
F=(OUT/'candidate.tex').read_text()
BOXES=json.loads((OUT/'crop_boxes.json').read_text())

def part(text,start,end,keep=True):
    a=text.index(start)
    b=text.index(end,a)+(len(end) if keep else 0)
    return text[a:b]
def crop(label):return 'crops/148_scan046_'+label+'.png'
changes=[]
def change(place,c,h,final,ink,label,ac,ah,kind,math=False,confidence='high'):
    assert not c or c in C,('C quotation',place,c)
    assert not h or h in H,('H quotation',place,h)
    changes.append(dict(place=place,c=c,h=h,final=final,ink=ink,crop=crop(label),box=BOXES[label],confidence=confidence,kind=kind,against_c=ac,against_h=ah,math=math))

change('opening lowercase objets',r'\uline{Objets}',r'\emph{objets}',r'\uline{objets}',
       'The initial o is a short oval beside the much taller b ascender. It is not a capital O reaching that height.','heading_triple',True,False,'misread word')
blob=part(F,r'\begin{tikzpicture}[x=.13cm',r'\end{tikzpicture}')
change('small canceled blob before the finite-subset line','','',blob,
       'A separate small cluster of crossed strokes stands immediately before the larger canceled S. Its underform is physically indistinct, so it is reproduced without assigning a letter.','finite_subset',True,True,'drawing or diagram',True,'low')
change('top-right canceled partial X',r'\deleted{\unsure{\partial X}}',r'\struck{\partial X}',r'\deleted{\partial X}',
       'The partial sign retains its upper curl, descending stem and lower loop; the following X has two distinct crossing diagonals beneath the cancellation.','top_symbols',True,False,'misread symbol or index',True)
change('surface-line terminal punctuation','compacte orientée','compacte orientée,','compacte orientée',
       'The last low stroke is part of the final e. No separate comma follows it.','surface_line',False,True,'text not on the page')
change('canceled close after X',r'\deleted{\unsure{close}}',r'\struck{\ill{}}',r'\deleted{\unsure{close}}',
       'Surviving low loops and a tall middle stroke permit close, but the hatching obscures enough letters to retain the doubt.','sigma_condition',False,True,r'readable ink left as \ill{}',False,'low')
change('sigma-condition terminal punctuation',r'$\widetilde\Sigma\supset\partial X$',r'$\widetilde{\Sigma} \supset \partial X$,',r'$\widetilde\Sigma\supset\partial X$',
       'No detached comma follows the final X; the following-line material is separate.','sigma_condition',False,True,'text not on the page',True)
change('finite-subset leading canceled S',r'\deleted{\unsure{S}}R\subset\Sigma',r'\struck{\ill{}} $R \subset \Sigma$',r'\deleted{\unsure{S}}R\subset\Sigma',
       'The large canceled form has upper and lower curves consistent with S, but dense crossing strokes prevent complete resolution. The live R, subset sign and Sigma are clear.','finite_subset',False,True,r'readable ink left as \ill{}',True,'low')
change('finite-subset trailing canceled symbol',r'\deleted{\unsure{\widetilde\Sigma}}',r'\struck{\ill{}}',r'\deleted{\unsure{\widetilde\Sigma}}',
       'A separate group after the live Sigma is crossed by several diagonal strokes. The tentative tilde-Sigma reading remains unresolved rather than omitted.','finite_subset',False,True,r'readable ink left as \ill{}',True,'low')
change('finite-subset terminal period','partie finie','partie finie.','partie finie',
       'The final e ends in a low curl, without a separate terminal point.','finite_subset',False,True,'text not on the page')
change('margin disjoint-union sign',r'\partial X\amalg\Sigma',r'\partial X \sqcup \Sigma',r'\partial X\amalg\Sigma',
       'The bottom horizontal stroke extends to the left and right beyond both upright strokes; the written sign is retained as amalg.','left_note',False,True,'misread symbol or index',True,'medium')
change('margin-formula terminal period',r'$\widetilde\Sigma=\partial X\amalg\Sigma$',r'$\widetilde{\Sigma} = \partial X \sqcup \Sigma$.',r'$\widetilde\Sigma=\partial X\amalg\Sigma$',
       'The formula ends at Sigma. No separate period stands between its final stroke and the prose on the following line.','left_note',False,True,'text not on the page',True)
change('margin mais aussi',r'\unsure{mais} aussi',r'\ill{}',r'\unsure{mais} aussi',
       'After the comma, a flattened m-like group, a short dotted stroke and a terminal curl favor mais. The following aussi is visible. Mais itself remains uncertain.','left_note',False,True,r'readable ink left as \ill{}',False,'low')
change('margin que R découpe',r"que $R$ ``découpe''", 'le\n« découpage » par $R$',r"que $R$ ``découpe''",
       'The lower line begins with a q descender in que, then R, followed by découpe inside paired raised quotation strokes. No le or par occurs in this line.','left_note',False,True,'misread word')
change('flèches-definition terminal period',"conservant l'orientation","conservant l'orientation.","conservant l'orientation",
       'The final n finishes in a connected writing stroke; no detached period follows it. The earlier homéom. abbreviation does have a distinct dot.','arrows_definition',False,True,'text not on the page')
change('canceled de after Variante',r'\deleted{Variante \unsure{de}}',r'\struck{Variante}',r'\deleted{Variante \unsure{de}}',
       'A small crossed group sits just above and to the right of Variante. Its loop and short following stroke permit de, but do not settle every letter.','components_start',False,True,'omission',False,'low')
change('first compos. abbreviation','Les composantes connexes',r'Les compos.\ connexes','Les compos. connexes',
       'The short word ends after compos with a separate abbreviation dot before connexes. No later t or full antes ending belongs to this occurrence. Comparison with the later fully written word confirms the shorter span.','components_start',True,False,'abbreviation expanded or spelling modernised',False,'high')
change('Sigma equality insertion without literal parentheses',r'\inserted{=\Sigma}',r'($= \Sigma$)',r'\inserted{=\Sigma}',
       'The equality and Sigma sit above the main line. A curved leader below them is not a pair of enclosing parentheses.','components_start',False,True,'insertion or placement',True)
insert_c=r'\inserted{celles de $\partial X$ sont les cercles de raccord}'
insert_h=part(H,r'\add{et} celles de',r'\emph{cercles de découpage}')
change('interlinear raccord definition and baseline order',insert_c,insert_h,insert_c,
       'The interline starts celles, without et. The main baseline reads sont les cercles de découpage; the inserted words separately define the boundary components as cercles de raccord. A long curved leader marks the insertion.','components_start',False,True,'insertion or placement')
change('canceled S before vertex term',r'\deleted{\unsure{S}}R',r'les éléments de $R$',r'\deleted{\unsure{S}}R',
       'Dense canceled S-like ink remains immediately beside the live R. Its curves are partly visible but too crossed to resolve fully.','circle_terms',False,True,'omission',True,'low')
change('canceled pts de marquage',r'\deleted{\unsure{pts de marquage}}','',r'\deleted{\unsure{pts de marquage}}',
       'The struck phrase retains a p descender, small following strokes and the long marquage-like body. Internal letters remain obscured by the strike.','circle_terms',False,True,'omission',False,'low')
term_c=part(C,r'\uline{sommets de',r'\inserted{rigidification}}')
term_f=part(F,r'\uline{sommets de}',r'\inserted{rigidification}')
change('vertex-term underline and replacement scope',term_c,r'\emph{sommets de rigidification}',term_f,
       'Underline strokes lie beneath the old baseline sommets de marquage. Marquage is crossed, while rigidification is written above it without a separately drawn new underline.','circle_terms',True,True,'insertion or placement',False,'medium')
change('canceled tentative composantes',r'les composantes connexes de $\partial X$ sont les',r'les compos.\ connexes de $\partial X$ sont les',r'les \unsure{composantes} connexes de $\partial X$ sont les',
       'The crossed word has a long connected body that permits composantes. The crop overlaps intersect its raised ending, so that ending cannot be certified letter by letter. The full word remains a tentative first reading, distinct from the clearly abbreviated first compos. and the later fully written live composantes.','components_end',False,True,'misread word',False,'low')
trous_c=r"\deleted{les composantes connexes de $\partial X$ sont les ``trous''.}"
trous_h=part(H,r'\struck{, les compos.',r'« trous »}.')
trous_f=r"\deleted{les \unsure{composantes} connexes de $\partial X$ sont les ``\uline{trous}''}."
change('trous underline, quotation and deletion scope',trous_c,trous_h,trous_f,
       'A separate line survives beneath trous in addition to the cancellation through the phrase. The quotes are paired raised ticks. The period lies to the right of the cancellation endpoint and remains live.','components_end',True,True,'deletion state')
change('canceled connexes before replacement',r'$\deleted{\text{connexes}}$','',r'\deleted{connexes}',
       'Below the new word, the old connexes remains crossed by a separate dark stroke. Its initial c and connected n/e/x forms are visible.','components_end',False,True,'omission')
change('inserted composants',r'\inserted{\uline{composants}}',r'\emph{composantes}',r'\inserted{\uline{composants}}',
       'The inserted word ends with a tall t followed directly by a small s; no e intervenes. A distinct underline lies below this new word.','components_end',False,True,'misread word')
diagram_c=part(C,r'\diagram{\begin{tikzcd}',r'\end{tikzcd}}')
diagram_h=part(H,r'\begin{tikzcd}',r'\end{tikzcd}')
diagram_f=part(F,r'\diagram{\begin{tikzcd}',r'\end{tikzcd}}')
change('variant diagram headless hooked connector',diagram_c,diagram_h,diagram_f,
       'The first connector begins with a rounded left hook and continues as one long shaft to a blunt right end. No right arrowhead is visible. The second connector has a clear right head; all object labels and decorations were read with the two shafts.','variant_diagram',True,True,'drawing or diagram',True)
change('comme tantôt','comme tantôt.',r'\ill{} \uncertain{fibre}.','comme tantôt.',
       'The first word has the connected c/o and m strokes of comme. Tantôt has tall t strokes and a distinct circumflex over o, followed by a separate period.','comme_tantot',False,True,'misread word')
change('first table-row canceled condition',r'\deleted{\unsure{R=\widetilde\Sigma=\varnothing}}',r'\struck{\ill{}}',r'\deleted{\unsure{R=\widetilde\Sigma=\varnothing}}',
       'The lower canceled condition retains an initial R-like form, equality strokes, a Sigma-like group and a final slashed oval. The hatching prevents secure resolution of the whole expression.','row1',False,True,r'readable ink left as \ill{}',True,'low')
row1_c=part(C,r'R=\varnothing,\ \Sigma=\unsure{\varnothing}&',r'\deleted{\unsure{R=\widetilde\Sigma=\varnothing}}&&\\')
row1_h=part(H,r'\item[] $R = \emptyset$, $\Sigma = \emptyset$',r'$\mathcal{T}_{\mathrm{top}}$ et $\mathcal{T}^{\pm}_{\mathrm{top}}$ ;')
row1_f=part(F,r'R=\varnothing,\ \Sigma=\unsure{\varnothing}&',r'\deleted{\unsure{R=\widetilde\Sigma=\varnothing}}&&\\')
change('first table-row added list punctuation',row1_c,row1_h,row1_f,
       'The conditions and the two calligraphic T labels are aligned without a written colon or terminal semicolon. The lower crossed condition is a separate line.','row1',False,True,'text not on the page',True)
change('second table-row canceled condition',r'\Sigma=\deleted{\unsure{\partial X}}\varnothing',r'$\Sigma = \emptyset$ \struck{\ill{}}',r'\Sigma=\deleted{\unsure{\partial X}}\unsure{\partial X|\varnothing\deleted{X}}',
       'An earlier dense canceled cluster follows the equality. To its right are an oval with a tall oblique stem and a separate substantial X-like form. The visible sequence favors partial X; an empty-set replacement with a surviving canceled X remains a status alternative. A lone empty-set glyph omits the visible rightmost ink.','row2',True,True,'misread symbol or index',True,'low')
change('second table-row added colon',r'R\text{ quelconque}',r'$R$ quelconque :',r'R\text{ quelconque}',
       'Quelconque ends with its final low e stroke. There are no two detached dots after it.','row2',False,True,'text not on the page',True)
teich_c=part(C,r'\begin{gathered}',r'\end{gathered}')
teich_h=part(H,r'(\emph{groupoïdes de Teichmüller',r'(topologiques orientés))')
teich_f=part(F,r'\begin{gathered}',r'\end{gathered}')
change('Teichmüller annotation, frame and parentheses',teich_c,teich_h,teich_f,
       'Teich- ends the first line with a visible hyphen and müller continues below. Only spéciaux is underlined in the baseline phrase. The interlinear ou rigidifiés has a separate underline and a continuous curved lower frame joining its side strokes. After topologiques orientés only one closing parenthesis is drawn; no second one is supplied.','teichmuller',True,True,'drawing or diagram',False,'medium')
change('Teichmüller annotation terminal semicolon',r'(topologiques orientés))',r'(topologiques orientés)) ;',r'(topologiques orientés)',
       'After the single observed closing parenthesis there is no separate semicolon. The added balancing parenthesis is addressed in the frame and annotation decision.','teichmuller',False,True,'text not on the page')
change('canceled top subscript in third table row',r'\mathcal T_{\deleted{\unsure{\mathrm{top}}}}D_{\mathrm{top}}',r'\mathcal{T}D_{\mathrm{top}}',r'\mathcal T_{\deleted{\unsure{\mathrm{top}}}}D_{\mathrm{top}}',
       'Small old t/o/p-like strokes remain below T and partly beneath the larger D. The live top subscript after D is separate. The old subscript remains tentative and canceled.','row3',False,True,'omission',True,'low')
change('third table-row added colon',r'R=\varnothing&',r'$R = \emptyset$ :',r'R=\varnothing&',
       'The slashed oval is followed by an open gap before the first calligraphic T label, without a written colon.','row3',False,True,'text not on the page',True)
change('Cas-comment terminal punctuation','également)','également).','également)',
       'One closing parenthesis ends the comment. No separate period follows it.','case_comment',False,True,'text not on the page')
change('MD margin ou and quotation form',r"MD = ``modulaire'' ou Mumford--Deligne",r'MD = « modulaire » Mumford--Deligne',r"MD = ``modulaire'' ou \unsure{Mumford}--Deligne",
       'Two raised quotation ticks occur on each side of modulaire. A separate small ou follows the closing quotes. The surname’s strokes after f are compressed, so Mumford retains local doubt.','md_margin',False,True,'omission',False,'medium')
change('canceled Dé before heading',r'\deleted{\unsure{Dé}}','',r'\deleted{\unsure{Dé}}',
       'A small canceled initial group has a D-like cap and a short following accented stroke before the live Détermination. The crossed e-like form is not completely secure.','determination',False,True,'omission',False,'low')
change('lower-left foliation',r'\mspage{45}','',r'\margin{45}',
       'A thin gray open 4 and a separate 5 with a horizontal cap and lower curve are visible at the lower left, in another unnamed hand.','folio',False,True,'omission')

decisions=[
    dict(id='M0686',decision='undecided',reading=r'\unsure{mais}',ink='A flattened m-like group, a dotted short stroke and a terminal curl favor mais, but the middle strokes remain too compressed to resolve.',crop=crop('left_note'),box=BOXES['left_note'],confidence='low'),
    dict(id='M0687',decision='undecided',reading=r'\unsure{\varnothing}',ink='The first-row value has an oval and long crossing stroke, with further dense intersecting ink. Its current form and possible retracing remain locally uncertain.',crop=crop('row1'),box=BOXES['row1'],confidence='low'),
    dict(id='M0688',decision='undecided',reading=r'\unsure{\varnothing}',ink='The comment’s value repeats the thick oval-and-crossing pattern of the first row; the overtracing prevents a confident resolution.',crop=crop('case_comment'),box=BOXES['case_comment'],confidence='low')
]

inventory=[]
def inv(element,kind,position,words,hand='his hand'):
    inventory.append(dict(element=element,kind=kind,position=position,first_words_or_objects=words,sheet_kind='text',hand=hand,transcribed='yes'))
inv('author page number','text','upper right of main heading','2')
inv('objects heading and triple','text','top main line',r'\uline{objets} : Triples $(X,\widetilde\Sigma,\deleted{\unsure{S}}\inserted{R})$')
inv('old third entry of triple','deletion','inside the opening triple',r'\deleted{\unsure{S}}')
inv('new third entry of triple','insertion','above old S in opening triple',r'\inserted{R}')
inv('isolated upper symbols','margin note','upper right',r'$X,\deleted{\partial X},\Sigma,S$')
inv('canceled upper partial X','deletion','upper-right symbol row',r'\deleted{\partial X}')
inv('surface condition','text','below heading',r'$X$ surface à bord compacte orientée')
inv('Sigma condition','text','third main line',r'$\widetilde\Sigma$ sous-variété compacte de $X$')
inv('canceled close','deletion','after compacte de X',r'\deleted{\unsure{close}}')
inv('finite subset condition','text','fourth main line',r'$R\subset\Sigma$, partie finie')
inv('small unassigned crossed trace','drawing','before the large canceled S on finite-subset line',blob)
inv('large canceled S on finite-subset line','deletion','immediately before live R',r'\deleted{\unsure{S}}')
inv('canceled symbol after finite Sigma','deletion','after the live finite-subset formula',r'\deleted{\unsure{\widetilde\Sigma}}')
inv('left-margin decomposition formula','display','upper left, oblique',r'\widetilde\Sigma=\partial X\amalg\Sigma')
inv('left-margin rigidification note','margin note','upper left, oblique',r'On peut considérer que $R$ rigidifie, \unsure{mais} aussi')
inv('morphism definition','text','below finite subset condition',r'\uline{flèches} : classes d’isotopie d’homéom.')
inv('canceled Variante opening','deletion','left of first components line',r'\deleted{Variante \unsure{de}}')
inv('first components sentence','text','middle upper paragraph',r'Les compos. connexes de $\widetilde\Sigma\setminus\partial X$')
inv('Sigma equality','insertion','above first components formula',r'\inserted{=\Sigma}')
inv('boundary-component definition','insertion','interline below first components line',r'\inserted{celles de $\partial X$ sont les cercles de raccord}')
inv('cutting-circle term','text','next baseline in components paragraph',r'\uline{cercles de découpage}')
inv('old S in vertex sentence','deletion','before live R after les éléments de',r'\deleted{\unsure{S}}')
inv('tentative old vertex term','deletion','before sommets de',r'\deleted{\unsure{pts de marquage}}')
inv('old marquage term','deletion','under inserted rigidification',r'\deleted{\uline{marquage}}')
inv('replacement rigidification','insertion','above canceled marquage',r'\inserted{rigidification}')
inv('canceled parenthetic alternative','deletion','interline above vertex-term baseline',r'\deleted{(ou de rigidification)}')
inv('canceled boundary holes sentence','deletion','middle paragraph, two lines',trous_f)
inv('live components sentence','text','last two lines of components paragraph',r'Les composantes connexes de $X$ sont les')
inv('old connexes predicate','deletion','under inserted composants',r'\deleted{connexes}')
inv('new composants term','insertion','above canceled connexes',r'\inserted{\uline{composants}}')
inv('variant introduction','text','below components paragraph',r'Variante $S_*\mathcal TD_{\mathrm{top}}^\pm$, avec')
inv('variant connector diagram','diagram','middle of page',diagram_f)
inv('comme tantôt','text','below variant connector diagram','comme tantôt.')
inv('full-subgroupoid introduction','text','above lower table','On a des sous-groupoïdes pleins')
inv('first subgroupoid row','display','upper row of lower table',r'R=\varnothing,\ \Sigma=\unsure{\varnothing};\quad\mathcal T_{\mathrm{top}},\ \mathcal T^\pm_{\mathrm{top}}')
inv('canceled first-row condition','deletion','under first-row conditions',r'\deleted{\unsure{R=\widetilde\Sigma=\varnothing}}')
inv('second subgroupoid row','display','middle row of lower table',r'\Sigma=\deleted{\unsure{\partial X}}\unsure{\partial X|\varnothing\deleted{X}},\ R\text{ quelconque}')
inv('older canceled second-row group','deletion','immediately after Sigma equals in middle row',r'\deleted{\unsure{\partial X}}')
inv('Teichmüller subgroupoid annotation','text','right of second row',teich_f)
inv('framed rigidifiés annotation','insertion','between spéciaux and topologiques orientés',part(F,r'\inserted{\begin{tikzpicture}[baseline=(rig.base)]',r'\end{tikzpicture}}'))
inv('third subgroupoid row','display','lowest row of table',r'R=\varnothing;\quad\mathcal T_{\deleted{\unsure{\mathrm{top}}}}D_{\mathrm{top}},\ \mathcal TD^\pm_{\mathrm{top}}')
inv('canceled old top subscript','deletion','under first T in third row',r'\deleted{\unsure{\mathrm{top}}}')
inv('Cas comment','text','two lines below table',r'(Cas pas intéressant je crois, sauf pour $\Sigma=\unsure{\varnothing}$ également)')
inv('MD expansion note','margin note','lower left, oblique',r"MD = ``modulaire'' ou \unsure{Mumford}--Deligne")
inv('canceled initial Dé','deletion','before live Détermination heading',r'\deleted{\unsure{Dé}}')
inv('Détermination heading','text','bottom main block',r'\uline{Détermination} du')
inv('pi zero isomorphism','display','after Détermination du',part(F,r'$\pi_0(S_*',r')$.'))
inv('weighted graph introduction','text','last main line',r'On introduit les \uline{graphes} \deleted{\unsure{MD}} bipondérés')
inv('canceled MD','deletion','between graphes and bipondérés',r'\deleted{\unsure{MD}}')
inv('lower foliation','margin note','lower left','45','another unnamed hand')

unresolved=[]
def un(place,reading,issue,alternatives=None,confidence='low'):
    unresolved.append(dict(place=place,reading=reading,issue=issue,alternatives=alternatives or [],confidence=confidence))
un('third entry of opening triple',r'\deleted{\unsure{S}}','Crossing strokes obscure the underform; two curves favor S without fully resolving it.',['S','unreadable canceled symbol'])
un('last word of opening line',r'\unsure{où|ou}','The word is legible as ou, but a detached grave accent is not securely distinguishable.',['où','ou'],'medium')
un('canceled adjective after X',r'\deleted{\unsure{close}}','The tall middle stroke and low loops permit close; the hatching obscures individual letters.',['close','unreadable canceled word'])
un('small trace before canceled S',blob,'The physically indistinct crossed trace cannot be assigned a letter. Its observed strokes are reproduced directly.')
un('large canceled S before finite R',r'\deleted{\unsure{S}}','The large curved underform is too crossed for a secure S reading.',['S','unreadable canceled symbol'])
un('canceled group after finite Sigma',r'\deleted{\unsure{\widetilde\Sigma}}','The tentative tilde-Sigma underform remains heavily obscured by diagonal strokes.',[r'\widetilde\Sigma','unreadable canceled symbol'])
un('M0686, left-margin connective',r'\unsure{mais}','Compressed middle strokes do not permit every letter to be certified.',['mais','unreadable connective'])
un('small canceled group after Variante',r'\unsure{de}','The raised group has a loop and a short trailing stroke, but its cancellation obscures the reading.',['de','unreadable canceled word'])
un('old S before R in vertex sentence',r'\deleted{\unsure{S}}','The live R is clear; the adjacent canceled curves are only tentatively S.',['S','unreadable canceled symbol'])
un('old vertex designation',r'\deleted{\unsure{pts de marquage}}','The p descender and long marquage-like body survive, but some short internal letters are crossed.',['pts de marquage','partly unreadable canceled phrase'])
un('canceled components word before trous',r'\unsure{composantes}','The long connected crossed body permits the full word, but the overlapping crops do not certify all strokes of its raised ending.',['composantes','compos.'])
un('M0687, first-row Sigma value',r'\unsure{\varnothing}','A thick oval with crossing strokes favors an empty-set sign; retracing and cancellation cannot be fully separated.',[r'\varnothing','unresolved overtraced sign'])
un('canceled first-row condition',r'\deleted{\unsure{R=\widetilde\Sigma=\varnothing}}','Hatching obscures the middle expression and exact cancellation underform.',[r'R=\widetilde\Sigma=\varnothing','partly unreadable canceled condition'])
un('older second-row canceled cluster',r'\deleted{\unsure{\partial X}}','The dense earlier group permits partial X, but the underlying strokes are not fully separable.',[r'\partial X','unreadable canceled group'])
un('second-row current condition and X status',r'\unsure{\partial X|\varnothing\deleted{X}}','The oval with a tall stem is followed by a substantial X-like glyph. Current partial X is favored; an empty-set replacement with surviving canceled X remains possible because the cancellation boundary is uncertain.',[r'\partial X',r'\varnothing\deleted{X}'])
un('old top subscript in third row',r'\deleted{\unsure{\mathrm{top}}}','Small crossed t/o/p-like strokes lie beneath T and partly under D; not all letters are separable.',[r'\mathrm{top}','unreadable canceled subscript'])
un('M0688, Sigma value in Cas comment',r'\unsure{\varnothing}','The oval and intersecting strokes are thick and locally overtraced, as in the first-row value.',[r'\varnothing','unresolved overtraced sign'])
un('surname in MD note',r'\unsure{Mumford}','The sequence after f is compressed and does not securely separate o from r. The first reading is retained without normalization.',['Mumford','partly unreadable surname'],'medium')
un('initial canceled Dé',r'\deleted{\unsure{Dé}}','The small initial D-like group and following accented stroke are crossed.',['Dé','unreadable canceled word opening'])
un('canceled MD before bipondérés',r'\deleted{\unsure{MD}}','The D bowl is visible; multiple cancellation strokes obscure the M.',['MD','unreadable canceled initials'])

notes=[
 dict(id='148-046-N01',type='reading method',place='whole page',text='The whole page was inspected once for layout and both native overlapping halves once line by line, including agreed words, formulas, deletions and insertions. All 21 unique enhanced crops were loaded successfully and inspected. No OCR, web research or TeX compilation was used.'),
 dict(id='148-046-N02',type='reading adjudication',place='components words',text='The reader initially mistook the first short word for fully written composantes. Root identified the separate abbreviation stop. Reopening the same components_start crop established compos.; the candidate and evidence record preserve the abbreviation. The later canceled occurrence retains tentative composantes because its ending is not fully certified in the saved overlap. The final live occurrence is fully written composantes.'),
 dict(id='148-046-N03',type='deletion and insertion scope',place='components paragraph',text='The equality with Sigma and the boundary-component definition are interlinear insertions. The long lower strokes accompanying cercles de raccord function as an insertion leader, so no independent underline is assigned. Old marquage is underlined and canceled; rigidification is above it. The period following the canceled trous phrase remains outside the cancellation.'),
 dict(id='148-046-N04',type='drawing',place='finite-subset line',text='The small crossed blob before the larger canceled S is physically indistinct. A literal stroke trace preserves it without assigning an underletter.'),
 dict(id='148-046-N05',type='notation',place='variant diagram',text='The first connector has a left hook, a long shaft and no right arrowhead. The trace reproduces this observed course. The second connector has a clear right arrowhead. No stronger arrow convention is imposed on the first connector.'),
 dict(id='148-046-N06',type='reading adjudication',place='second subgroupoid condition',text='Reader and root independently observed a substantial X-like form after the tall-stemmed oval. The candidate favors current partial X and retains an empty-set-plus-canceled-X alternative because the cancellation scope is not secure. A lone empty-set transcription would omit visible ink.'),
 dict(id='148-046-S01',type='conditional mathematical check',place='finite-subset definition and second subgroupoid condition',text='The definition visibly gives R included in Sigma. Only if the disputed second-row value is read as the empty set does ordinary inclusion force R to be empty. The current first reading is partial X, so this does not establish a contradiction in the source. The check event states the exact conditional argument.'),
 dict(id='148-046-S02',type='source claim',place='morphism definition',text='The source defines arrows as isotopy classes of orientation-preserving homeomorphisms. This definition was transcribed; no additional mathematical verification was performed.'),
 dict(id='148-046-S03',type='source claim',place='variant diagram and subgroupoid table',text='The source displays the variant with a sign map and names several full subgroupoids. Their fullness and the structural properties of the sign map were not independently proved in this reading.'),
 dict(id='148-046-S04',type='source claim',place='Détermination formula',text='The written tilde over the rightward arrow asserts an isomorphism between the two pi-zero expressions. The formula was read sign by sign, but its isomorphism claim was not checked.'),
 dict(id='148-046-N07',type='source assessment',place='Cas comment',text='The author writes that this case is not interesting, apparently except when Sigma also has the disputed empty-set value. This is preserved as the author’s assessment and is not treated as a proved mathematical claim.'),
 dict(id='148-046-N08',type='layout and punctuation',place='Teichmüller annotation',text='Teich- and müller occupy successive lines. The inserted ou rigidifiés is enclosed by a continuous lower frame with curved side strokes. Only one closing parenthesis is visible after topologiques orientés; the transcription leaves the earlier outer opening unbalanced.'),
 dict(id='148-046-N09',type='hand and numbering',place='page numbers',text='The top 2 belongs to the principal manuscript hand. The thinner gray lower-left 45 belongs to another unnamed hand and is kept as a margin item. No calendar date appears on the page.'),
 dict(id='148-046-N10',type='crop limitation',place='Sigma condition',text='The saved sigma_condition crop clips the very upper tip of the second tilde. The full tilde had already been read on the native half, and no second crop was made.'),
 dict(id='148-046-N11',type='uncertainty',place='canceled and retraced material',text='The larger canceled S forms, close, the old subscript and the thick empty-like values retain local doubts. Retracing alone has not been used to invent any earlier letter or digit.')
]
checks=[dict(statement_id='148-046-S01',date='2026-11-21',who='GPT-6 Astra Pro; effort not exposed; run SP82_C13_148-20261120; reader C',type='targeted proof check',outcome='Conditional on the second-row value being the empty set and on the written subset sign meaning ordinary inclusion: if x belongs to R, then R included in Sigma implies x belongs to the empty set, impossible. Hence R is empty. This restricts R quelconque to the empty set under that reading only. The favored partial-X reading does not yield this conclusion, and no source contradiction is asserted.')]

hand_log=[
 dict(form='D',habit='Uses a single curved bowl for ordinary D. Some occurrences are retraced, but the page does not supply a distinct doubled alphabet for these D forms.',holds_at_every_observed_occurrence=True,witness_effect='Preserve ordinary D in the variant, table and pi-zero formula.',pages=[46],hand='his hand'),
 dict(form=r'\mathcal T',habit='The T used in the category labels has a looped upper sweep and curled lower stroke.',holds_at_every_observed_occurrence=True,witness_effect='Retain the calligraphic T alphabet in all category labels.',pages=[46],hand='his hand'),
 dict(form='compos. / composantes',habit='Can shorten composantes to compos. with a separate stop, while writing the full word elsewhere on the page.',holds_at_every_observed_occurrence=False,witness_effect='The first occurrence is abbreviated; the later live occurrence is fully written. Do not expand the first by analogy.',pages=[46],hand='his hand'),
 dict(form='paired raised quotation strokes',habit='Uses paired raised ticks around découpe, trous and modulaire.',holds_at_every_observed_occurrence=True,witness_effect='Preserve the observed quotation form rather than H’s guillemets.',pages=[46],hand='his hand'),
 dict(form='interlinear replacements',habit='Places replacement words above canceled baseline words and sometimes connects insertions with long curved leaders.',holds_at_every_observed_occurrence=False,witness_effect='Separate the old baseline underlines from the inserted wording; do not turn leaders into new underlines.',pages=[46],hand='his hand'),
 dict(form='45',habit='Writes the lower folio in a thinner gray stroke, with an open 4 and a 5 having a horizontal cap and lower curve.',holds_at_every_observed_occurrence=True,witness_effect='Treat the lower number as a margin foliation in another unnamed hand.',pages=[46],hand='another unnamed hand')
]
notation=[
 dict(form=r'(X,\widetilde\Sigma,R)',use='Object triple; R replaces a canceled tentative S.',pages=[46],caution='The old S remains doubtful.'),
 dict(form=r'\widetilde\Sigma=\partial X\amalg\Sigma',use='Oblique margin decomposition of the marked locus.',pages=[46],caution='The union sign has a lower bar projecting beyond both uprights; no different product or union convention is substituted.'),
 dict(form=r'R\subset\Sigma',use='Finite-subset condition written literally.',pages=[46],caution='Keep distinct from the tilde-Sigma notation and from the disputed table condition.'),
 dict(form=r'S_*\mathcal TD_{\mathrm{top}}^\pm',use='Variant label with ordinary D, calligraphic T, star and sign decoration.',pages=[46],caution='The first connector is headless and is traced explicitly.'),
 dict(form=r'\pi_0(S_*\mathcal TD_{\mathrm{top}})\xrightarrow{\sim}\pi_0(S_*\mathcal TD^\pm_{\mathrm{top}})',use='Written isomorphism assertion at the bottom of the page.',pages=[46],caution='Transcribed, not proved in this reading.'),
 dict(form='MD',use='The margin gives modulaire or the tentative name Mumford--Deligne; MD is canceled before bipondérés.',pages=[46],caution='The surname and the canceled M retain local doubts.')
]
abbreviations=[
 dict(form='compos.',expansion='composantes',place='first components sentence',confidence='high'),
 dict(form='homéom.',expansion='homéomorphismes',place='morphism definition',confidence='high'),
 dict(form='pts',expansion='points',place='tentative canceled pts de marquage',confidence='low'),
 dict(form='top',expansion='topologique',place='category subscripts',confidence='medium'),
 dict(form='MD',expansion='modulaire ou Mumford--Deligne',place='oblique lower-left note',confidence='medium')
]

second_boxes=[]
def second(label,kind,reading,coords=None,suffix=''):
    x0,y0,x1,y1=coords or BOXES[label]
    second_boxes.append(dict(box='148-046-'+label+(('-'+suffix) if suffix else ''),kind=kind,x0=x0,y0=y0,x1=x1,y1=y1,reading=reading))
second('heading_triple','text',part(F,r'\mspage{2}',r'\unsure{où|ou}'))
second('top_symbols','margin note',r'\margin{$X,\deleted{\partial X},\Sigma,S$}')
second('surface_line','text',r'$X$ surface à bord compacte orientée')
second('sigma_condition','text',part(F,r'$\widetilde\Sigma$ sous-variété',r'$\widetilde\Sigma\supset\partial X$'))
second('finite_subset','deletion',part(F,r'\begin{tikzpicture}[x=.13cm',r'partie finie'))
second('left_note','margin note',part(F,r'\margin{$\widetilde\Sigma=',r"que $R$ ``découpe''}"))
second('arrows_definition','text',r"\uline{flèches} : classes d'isotopie d'homéom. conservant l'orientation")
second('components_start','insertion',part(F,r'\deleted{Variante',r'\inserted{celles de $\partial X$ sont les cercles de raccord},'),coords=[245,450,1665,795])
second('circle_terms','deletion',part(F,r'les éléments de $\deleted{\unsure{S}}R$',r'\deleted{(ou de rigidification)},'))
second('components_end','deletion',part(F,r'\deleted{les \unsure{composantes} connexes de $\partial X$',r"de l'objet envisagé."))
second('variant_diagram','diagram',part(F,r'Variante $S_*\mathcal TD_',r'\end{tikzcd}}'))
second('comme_tantot','text','comme tantôt.')
second('row1','formula',row1_f)
second('row2','formula',part(F,r'\Sigma=\deleted{\unsure{\partial X}}',r'S_*\mathcal T^\pm_{\mathrm{top}}&')+'\n'+r'R\text{ quelconque}')
second('teichmuller','insertion',teich_f)
second('row3','formula',part(F,r'R=\varnothing&',r'\mathcal TD^\pm_{\mathrm{top}}&'))
second('case_comment','text',part(F,'(Cas pas intéressant', 'également)'))
second('md_margin','margin note',r"\margin{MD = ``modulaire'' ou \unsure{Mumford}--Deligne}")
second('determination','formula',part(F,r'\deleted{\unsure{Dé}}',r')$.'))
second('bipondere','deletion',r'On introduit les \uline{graphes} \deleted{\unsure{MD}} bipondérés')
second('folio','handwritten number',r'\margin{45}')

diff_plan={
995:('macro-only','scan and author-page marker conventions'),
996:('macro-only','upper-right margin moved and described in an editorial note'),
997:('macro-only','canceled S in opening triple is also recorded in H’s note'),
998:('macro-only','H editorial note records the same inserted R and canceled S'),
999:('reading decision','surface-line terminal punctuation'),
1000:('reading decision','canceled close after X'),
1001:('reading decision','sigma-condition terminal punctuation and finite-subset leading canceled S'),
1002:('reading decision','finite-subset trailing canceled symbol'),
1003:('reading decision','finite-subset terminal period and relocated left-margin readings'),
1004:('reading decision','flèches-definition terminal period; margin-formula period, union sign, mais aussi and que R découpe'),
1005:('reading decision','canceled de after Variante'),
1006:('reading decision','first compos. abbreviation'),
1007:('reading decision','Sigma equality insertion without literal parentheses'),
1008:('reading decision','interlinear raccord definition and baseline order'),
1009:('reading decision','interlinear raccord definition and baseline order'),
1010:('reading decision','canceled S before vertex term'),
1011:('reading decision','canceled pts de marquage'),
1012:('reading decision','vertex-term underline and replacement scope'),
1013:('reading decision','vertex-term underline and replacement scope'),
1014:('macro-only','H note describes the same canceled parenthetic alternative'),
1015:('macro-only','closing quotation in H editorial account of canceled parenthesis'),
1016:('reading decision','canceled tentative composantes'),
1017:('reading decision','trous underline, quotation and deletion scope'),
1018:('reading decision','canceled connexes before replacement and inserted composants'),
1019:('macro-only','TeX grouping and order of subscript and superscript'),
1020:('macro-only','TeX order of subscript and superscript'),
1021:('macro-only','TikZ ampersand replacement option'),
1022:('macro-only','adjacent calligraphic T and ordinary D notation'),
1023:('reading decision','variant diagram headless hooked connector'),
1024:('macro-only','TeX grouping and order of subscript and superscript'),
1025:('macro-only','TeX order of subscript and superscript'),
1026:('reading decision','comme tantôt'),
1027:('macro-only','array and itemize presentation wrappers'),
1028:('reading decision','first table-row added list punctuation'),
1029:('reading decision','first table-row canceled condition and added list punctuation'),
1030:('reading decision','second table-row canceled condition and added colon'),
1031:('macro-only','gathered presentation wrapper'),
1032:('reading decision','Teichmüller annotation terminal semicolon; R quelconque remains in the second row'),
1033:('reading decision','third table-row added colon'),
1034:('reading decision','canceled top subscript in third table row'),
1035:('macro-only','adjacent calligraphic T and ordinary D notation'),
1036:('macro-only','array presentation wrapper'),
1037:('reading decision','Cas-comment terminal punctuation'),
1038:('reading decision','MD margin ou and quotation form'),
1039:('reading decision','canceled Dé before heading; H’s margin-location note is editorial'),
1040:('macro-only','adjacent calligraphic T and ordinary D notation'),
1041:('macro-only','adjacent calligraphic T and ordinary D notation'),
1042:('reading decision','lower-left foliation')
}
rows=list(csv.DictReader((PACKET/'differences.tsv').open(newline=''),delimiter='\t',quoting=csv.QUOTE_NONE))
assert set(int(r['source_row']) for r in rows)==set(diff_plan)
differences_review=[dict(source_row=int(r['source_row']),classification=diff_plan[int(r['source_row'])][0],place=diff_plan[int(r['source_row'])][1]) for r in rows]

result=dict(scan=46,reader='C',lines_read=41,changes=changes,decisions=decisions,inventory=inventory,unresolved=unresolved,notes=notes,checks=checks,hand_log=hand_log,notation=notation,abbreviations=abbreviations,second_boxes=second_boxes,differences_review=differences_review)
assert len(decisions)==3 and {x['id'] for x in decisions}=={'M0686','M0687','M0688'}
assert all(isinstance(x['math'],bool) for x in changes)
assert all(x['against_c'] or x['against_h'] for x in changes)
assert len({x['box'] for x in second_boxes})==len(second_boxes)
for x in changes+decisions:
    assert (OUT.parent.parent/x['crop']).exists(),x['crop']
    assert x['box'] in BOXES.values(),x['box']
(OUT/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:len(result[k]) for k in ['changes','decisions','inventory','unresolved','notes','checks','hand_log','notation','abbreviations','second_boxes','differences_review']},ensure_ascii=False))
