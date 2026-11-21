from pathlib import Path
import json
root=Path('/workspace/scratch/f28c4f52d3ec'); page='148_scan062'
parts=json.loads((root/'proposed'/f'{page}_parts.json').read_text())
records=json.loads((root/'proposed'/f'{page}_crop_boxes.json').read_text())
for rec in records: rec['viewed']=True
(root/'proposed'/f'{page}_crop_boxes.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
crops={x['name']:x for x in records}
changes=[]
def add(place,c,h,final,dc,dh,kind,error,evidence,crop,confidence='high',marked=False,consequential=False):
    cr=crops[crop]
    changes.append(dict(id=f'{page}-{len(changes)+1:02}',place=place,c=c,h=h,final=final,diff_c=dc,diff_h=dh,kind=kind,error_kind=error,evidence=evidence,crop=cr['crop'],box=cr['box'],confidence=confidence,marked_in_h=marked,consequential=consequential))
add('Opening paragraph, qui dira/dise','dira','dise',r'\unsure{dira|dise}',False,True,'misread word','Words','The d loop and the dotted i are distinct. The following short raised hook and detached low ending do not separate r-a from s-e securely; both readings remain, with C first.','dira','medium')
add('Opening paragraph, after isom.','uniques','unique',r'\unsure{uniques|unique}',False,True,'misread word','Words','The opening u-n-i run, i mark and descending q are visible. The final low run ends in a downturned hook; e and a possible final s cannot be separated securely.','uniques','medium')
add('First ambient groupoid formula',r'$S_*\mathcal TD_{\mathrm{top}}^\pm$',r'$S_f\mathcal T D^\pm_{\mathrm{top}}$',r'$S_{\unsure{*|f}}\mathcal TD_{\mathrm{top}}^\pm$',False,True,'misread symbol or index','Symbols and indices','The entire formula has S, the broad-topped calligraphic T, D, top and a two-level plus-minus. The small S index has looped upper/lower strokes and a transverse arm, hence its f-like appearance. The lower definition clearly has a star, but this upper shape remains doubtful.','global_formula','medium',True,True)
add('Interlinear insertion, singular expression','avec le foncteur','avec les foncteurs','avec le foncteur',False,True,'misread word','Words','After the tall l loop there is one short e tail, without a separate s. The final foncteur stroke ends as r; no additional plural letter is detached beyond it.','insertion')
add('Interlinear insertion, Gamma decoration',r'$\Gamma$',r'$\underline{\Gamma}$',r'$\Gamma$',False,True,'misread symbol or index','Symbols and indices','Gamma has a heavy vertical and top arm. Its short lower foot joins the upright; there is no separated underline below the letter.','insertion')
add('Interlinear insertion, target abbreviation',r'\unsure{\mathrm{rep}|\mathrm{top}}',r'\mathrm{top}',r'\mathrm{top}',True,False,'misread word','Words','The first letter rises above the line and is crossed, the middle letter is an open oval, and the final p descends. These support top rather than rep; the whole target was checked.','insertion')
add('Interlinear insertion, point after pond',r'\mathrm{Gr.pond.}',r'\mathrm{Gr.pond.}',r'\mathrm{Gr.pond}',True,True,'text not on the page','Text that is not on the page','A point is visible after Gr. There is no independent point after pond: the adjacent dark curved end is continuous with the long descending q from the line above.','insertion')
add('Interlinear insertion, functor into the sign object',r'$\unsure{\chi|f}$',r'$f$',r'$\unsure{\chi|f}$',False,True,'misread symbol or index','Symbols and indices','The symbol has crossing curved strokes and a long lower-left sweep, favoring chi. The short upper-right return also permits an f-like reading, so the doubt remains. The following dans and full [plus-minus 1] target are clear.','insertion','medium',False,True)
add('Elementary operation range',r'$1^\circ$ à $7^\circ$','1° : 7°',r'$1^\circ:7^\circ$',True,False,'misread symbol or index','Symbols and indices','Between the first and seventh ordinal labels are two separated dark dots, one above the other. No letter a body is present. Both digits and ordinal circles are visible.','operations',consequential=True)
add('Parenthesis after operation range','ou','avec','ou',False,True,'misread word','Words','After the opening parenthesis there is a short rounded initial stroke and a low connected u run. The longer a-v-e-c sequence is not present.','operations')
add('Opening paragraph, verb after se','réconstitue','reconstitue','réconstitue',False,True,'misread word','Words','A separate short accent stroke is visible above the first e of the word. The remaining con-sti-tue run follows in the main line. C already preserves this accent.','reconstitue')
add('First cancelled diagram, blackened old superscript',r'S_1\mathcal T_{g,\nu}^{\deleted{\unsure{0}}\pm}',r'S_1\mathcal T_{g,\nu}^{\pm}',r'S_1\mathcal T_{g,\nu}^{\deleted{\unsure{0}}\pm}',False,True,'omission','Omissions','A separately blackened small superscript lies between the T top and the surviving plus-minus. Rounded residual strokes are visible, but the candidate 0 cannot be resolved through the overwriting.','cancelled_diagrams','low')
add('First cancelled diagram, old arrow label','absent',r'\struck{\ill{}}',r'\deleted{\unsure{\chi}}',True,True,'omission','Omissions','Crossed rising and descending strokes stand above the rightward arrow shaft under the hatching. A chi-like form survives, but its exact identity is obscured; it is retained as a doubtful cancelled label rather than silently omitted.','cancelled_diagrams','low',True)
add('First cancelled diagram, downward target',r'\unsure{\mathrm{Ens}(\nu)}',r'\mathcal T_{g,\nu}^{\pm}',r'\mathrm{Ens}(\nu)',False,True,'drawing or diagram','Drawings and diagrams','Below the vertical arrow, the E bars, low n connection, curled s, opening parenthesis, heavy nu and closing parenthesis remain distinguishable through the strike. This is Ens(nu), above the separate T object.','cancelled_diagrams',consequential=True)
add('Separate lower cancelled diagram',r'\mathcal T_{g,\nu}^{\pm}\arrow[dl]','one conflated cancelled diagram with a vertical target and an oblique arrow',parts['old2'],False,True,'drawing or diagram','Drawings and diagrams','A second calligraphic T with g,nu and plus-minus sits below the crossed Ens target. Its own oblique shaft runs down-left. The heavily crossed endpoint does not establish any additional mathematical object.','cancelled_diagrams',consequential=True)
add('Asterisk tag beside the live diagram',r'$(*)$ before the live diagram','(*) as a label on the old vertical arrow',r'$(*)$ at the left of the live frame',False,True,'insertion or placement','Insertions put in the wrong place','The star and parentheses are dark and are not struck with the old vertical arrow. They sit immediately outside the live left frame at the height of its first object.','cancelled_diagrams','medium')
add('Live diagram enclosure',r'\fbox{...}','two horizontal enclosure strokes',parts['live'],True,True,'drawing or diagram','Drawings and diagrams','The crop shows one long top bar, one long bottom bar and a separate left vertical. The right ends of the two horizontal bars are visible, with no connecting right edge.','live_frame')
add('Annotation beneath the first live object',r'\unsure{on siglera|on notera|ou simplement}','ou simplement','on siglera',False,True,'misread word','Words','The first word has a closed o and short n ending. The next has a dotted i, a descending looped g and a tall l, followed by the low e-r-a ending; these identify siglera.','shorthand')
add('Shorthand annotation leader and parentheses',r'(on siglera $S\mathcal T_{g\nu}^\pm$)',r'(ou simplement $S\mathcal T_{g,\nu}^\pm$)',r'on siglera $S\mathcal T_{g\nu}^{\pm}$, attached by a curved leader',True,True,'drawing or diagram','Drawings and diagrams','The long initial curve begins below the live S object and descends to the annotation. No closing parenthesis follows its formula. It is reproduced as a leader, without adding a matched pair of punctuation marks.','shorthand')
add('Shorthand annotation, lower index',r'g\nu',r'g,\nu',r'g\nu',False,True,'misread symbol or index','Symbols and indices','The descending g runs directly into the nu stroke. No separate comma occurs between them; the comma is visible in other g,nu occurrences on the same page.','shorthand')
add('Isolated erased sign on the live bottom bar',r'\deleted{\unsure{$\varnothing$}}','absent',r'$\deleted{\unsure{\varnothing}}$',False,True,'omission','Omissions','A small densely overwritten sign stands on the lower frame bar beneath the right part of the diagram. Its loop and crossing strokes are real ink; the empty-set candidate remains unresolved.','live_frame','low')
add('Large diagonal margin, after pour',r'\unsure{reconstituer|avoir toutes}','avoir toutes','avoir toutes',True,False,'misread word','Words','There are two word groups: a-v-o-i-r with a short i mark, then the tall t of toutes and its following low run. A single reconstituer sequence is not present.','margin')
add('Large diagonal margin, punctuation before Notamment','opérations Notamment','opérations. Notamment','opérations Notamment',False,True,'text not on the page','Text that is not on the page','The first opérations ends in its continuous final s hook. Before the next-line capital N there is no separated sentence point.','margin')
add('Large diagonal margin, cancelled old word',r'\deleted{\unsure{liens}}',r'\struck{\ill{}}',r"\deleted{\unsure{l'introd.|liens}}",True,True,'misread word','Words','Under the strike there is a tall initial l, a small apostrophe/i-like mark and a middle tall t. These favor an l-intro... beginning over liens, but the later letters are obscured; the complete word is not resolved.','margin_replacement','low',True)
add('Large diagonal margin, live lower replacement',r"\inserted{\unsure{``ou''|l'introd.}}",r"l'\uncertain{introd.}",r"\inserted{\unsure{``ou''}}",False,True,'misread word','Words','Below the cancelled line is a shorter dark group, with a closed o-like loop, a low following run and quotation strokes at its sides. No cancellation passes through this group; quoted ou remains the proposed, uncertain reading.','margin_replacement','medium',True)
add('Large diagonal margin, position of des',r"des \deleted{\unsure{liens}} \inserted{\unsure{``ou''|l'introd.}}",r"\struck{\ill{}} l'\uncertain{introd.}\ des",r"\deleted{\unsure{l'introd.|liens}} \inserted{\unsure{``ou''}} des",True,False,'insertion or placement','Insertions put in the wrong place','The small des group lies to the right of the crossed old word and the live lower replacement. It does not precede that replacement group as in C.','margin_replacement')
add('Large diagonal margin, quoted term',r'\unsure{structures}','structures',"``structures''",True,True,'omission','Omissions','The s-t-r-u-c-t-u-r-e-s run is visible, with the two t ascenders and final s. Separate quotation strokes precede and follow the word.','margin_lower')
add('Large diagonal margin, material after quoted structures','absent',r'; \ill{} \ill{}','absent',False,True,'text not on the page','Text that is not on the page','After the closing quotation strokes the next source unit is the lower-line T formula. There is no independent semicolon and no two-word intervening run in this area.','margin_lower')
add('Large diagonal margin, final category',r'\unsure{$\mathcal T_{g,\infty}$|$\mathcal T_{g,\nu}$}',r'$\mathcal T_{g,\nu}$',r'$\mathcal T_{g,\infty}$',False,True,'misread symbol or index','Symbols and indices','The T, descending g and comma are followed by two connected loops. This differs from the simple wedge-and-return nu elsewhere on the page and supports infinity. The entire formula and closing parenthesis were checked.','margin_lower',consequential=True)
add('Definition paragraph, ambient groupoid index',r'$S_*\mathcal T_{\mathrm{top}}^\pm$',r'$S_f\mathcal T_{\mathrm{top}}^\pm$',r'$S_*\mathcal T_{\mathrm{top}}^\pm$',False,True,'misread symbol or index','Symbols and indices','The small index below S has five short radiating arms, without the upper and lower letter loops needed for f. The T, top index and plus-minus are also visible.','definition_index','high',True,True)
add('Definition paragraph, before pour tout','(pour tout','pour tout','(pour tout',False,True,'omission','Omissions','A separate curved opening parenthesis runs to the left of the heavily retraced p of pour; it is not the p descender.','pour_tout')
add('Small graph, ray count and brace trace','seven rays and a font right brace','a fan of nu free edges and a brace',parts['graph'],True,False,'drawing or diagram','Drawings and diagrams','Five ray traces are visible from the vertex: two near-vertical left rays, one faint central ray and two right-slanting rays. The brace-like mark is overworked, with a leftward bend and short transverse arm to the right; its strokes are drawn directly instead of replacing it by a font glyph. The labels g and nu are retained.','graph_complete','medium',False,True)
add('Graph caption, parenthetical adjective','libres','lisières','libres',False,True,'misread word','Words','After l and the i mark there is a tall b with its returning loop, followed by a short r-e-s run. The extra s-i-è sequence needed by lisières is not present.','libres_weight')
add('Final defining triple, empty-set glyphs',r'$(X,\varnothing,\varnothing)$',r'$(X,\emptyset,\emptyset)$',r'$(X,\phi,\phi)$',True,True,'misread symbol or index','Symbols and indices','Each small empty-set sign is an oval traversed by a descending stem, the phi form used for the empty set. They are not plain circles with an independent diagonal slash.','final_clause')
add('Final defining clause, conjunction','où','avec','où',False,True,'misread word','Words','After the closing parenthesis there is one short o-u group with its small upper mark. No a-v-e-c sequence intervenes before X.','final_clause')
add('Final defining clause, after X','de','du','de',False,True,'misread word','Words','The d has a low loop and ascending stroke; its connected ending is a short flattened e tail, without an additional u trough.','final_clause')
add('Lower-left folio annotation',r'\mspage{61}','absent',r'\mspage{61}',False,True,'omission','Omissions','The pale annotation has a curled 6 with closed lower loop followed by the straight 1. The hand is not positively attributable from this page alone.','bottomfolio')

def decision(ident,choice,reading,evidence,crop,confidence='high'):
    cr=crops[crop]
    return dict(id=ident,decision=choice,reading=reading,evidence=evidence,crop=cr['crop'],box=cr['box'],confidence=confidence)

decisions=[
 decision('M0756','alternative',r'\mathrm{top}','A tall crossed t, oval o and descending p are visible in the complete target; rep has no supporting initial r shape.','insertion'),
 decision('M0757','undecided',r'\unsure{\chi|f}','The crossed curved strokes favor chi, but the compact upper return remains f-like. The whole inserted functor-and-target line was read.','insertion','medium'),
 decision('M0758','first','on siglera','Closed o and n are followed by dotted i, descending g, tall l and the low e-r-a ending. The long opening curve is a leader and no closing parenthesis follows the formula.','shorthand'),
 decision('M0759','alternative','avoir toutes','The two separately spaced word groups and the second group’s tall initial t support avoir toutes.','margin'),
 decision('M0760','first','demande','The initial d loop, linked low middle humps and final d-e run can be followed in the oblique line after qui; the proposed word is supported without adding a plural ending.','margin'),
 decision('M0761','undecided',r"\unsure{``ou''}",'The live lower group is short, has an o-like loop and a low following run, and is flanked by quotation strokes. The longer l-intro... belongs to the crossed group above; quoted ou remains uncertain.','margin_replacement','medium'),
 decision('M0762','first',"``structures''",'The long word has the two t ascenders and an s ending; quotation strokes are visible on both sides.','margin_lower'),
 decision('M0763','first',r'$\mathcal T_{g,\infty}$','The complete formula contains T, g, a comma and a connected double-loop infinity sign, unlike the page’s wedge-shaped nu.','margin_lower'),
]
implicit=[
 decision('C062-D01','undecided',r'\deleted{\unsure{0}}','The old superscript is heavily blackened; its residual loop does not establish the digit securely.','cancelled_diagrams','low'),
 decision('C062-D02','first',r'\mathrm{Ens}(\nu)','The E bars, n connection, s curve, parentheses and nu are separately visible despite the diagonal strike.','cancelled_diagrams'),
 decision('C062-D03','undecided',r'\deleted{\unsure{\varnothing}}','The isolated erased sign has a loop and several crossing strokes; the underlying symbol remains unresolved.','live_frame','low'),
 decision('C062-D04','first',r'\deleted{\mathcal T_{g,\nu}}','The cancelled T retains its broad top loop and curved body; below it the descending g, comma and nu wedge remain visible.','tuple'),
 decision('C062-D05','undecided',r"\deleted{\unsure{l'introd.|liens}}",'A tall l, apostrophe/i-like trace and middle tall t favor l-intro..., but the cancellation obscures the later letters. The old word is not resolved.','margin_replacement','low'),
]
doubts=[
 dict(place='Opening paragraph, qui',reading=r'\unsure{dira|dise}',alternatives='dira; dise',confidence='medium',reason='The final short strokes after di are compressed.'),
 dict(place='Opening paragraph, after isom.',reading=r'\unsure{uniques|unique}',alternatives='uniques; unique',confidence='medium',reason='The final e/s distinction is not securely separable from the terminal hook.'),
 dict(place='First S-index in the ambient formula',reading=r'S_{\unsure{*|f}}\mathcal TD_{\mathrm{top}}^\pm',alternatives='star; f',confidence='medium',reason='The upper index is looped and f-like. The lower definition has a clear star, but that does not remove the upper shape doubt.'),
 dict(place='Interlinear functor into [plus-minus 1]',reading=r'\unsure{\chi|f}',alternatives='chi; f',confidence='medium',reason='Crossing curves favor chi; their compact upper return still permits f.'),
 dict(place='First cancelled diagram, old superscript',reading=r'\deleted{\unsure{0}}',alternatives='0; unidentified overwritten sign',confidence='low',reason='Dense black overwriting hides the original shape.'),
 dict(place='First cancelled diagram, old horizontal arrow label',reading=r'\deleted{\unsure{\chi}}',alternatives='chi-like sign; unidentified cancelled label',confidence='low',reason='Only crossed, rising and descending strokes survive above the shaft.'),
 dict(place='Erased sign on live frame bottom bar',reading=r'\deleted{\unsure{\varnothing}}',alternatives='empty-set sign; unidentified erased symbol',confidence='low',reason='Multiple heavy crossing strokes obscure the underlying form.'),
 dict(place='Diagonal margin, cancelled old word',reading=r"\deleted{\unsure{l'introd.|liens}}",alternatives="l'introd.; liens",confidence='low',reason='The initial l and middle t-like stem survive, but the strike obscures the interior and ending.'),
 dict(place='Diagonal margin, live replacement',reading=r"\inserted{\unsure{``ou''}}",alternatives='quoted ou; unidentified short quoted group',confidence='medium',reason='The o-like loop and low following run favor ou but are not fully distinct.'),
]

inventory=[]
def inv(kind,pos,first,hand='his hand'):
    inventory.append(dict(element=f'E{len(inventory)+1:02}',sheet_kind='text',hand=hand,kind=kind,position=pos,first_words_or_objects=first,transcribed='yes'))
inv('text','upper centre','18')
inv('text','upper main block','Il faudrait expliciter un petit théorème')
inv('insertion','between opening main lines, above avec les opérations',r'avec le foncteur $\Gamma$ ... $\unsure{\chi|f}$')
inv('margin note','left of operation range, oblique and underlined',r"à l'exception de $4^\circ$ et $5^\circ$")
inv('deletion','middle upper-left, first cancelled diagram',r'S_1\mathcal T_{g,\nu}^{\deleted{\unsure{0}}\pm}\to[\pm1],\quad\downarrow\mathrm{Ens}(\nu)')
inv('deletion','below first cancelled target, second cancelled diagram',r'\mathcal T_{g,\nu}^{\pm}, down-left arrow')
inv('diagram','middle right, frame open on the right',r'(*)\quad S_1\mathcal T_{g,\nu}^{\pm}\to\mathcal T_{g,\nu}^{\pm}\to(\mathrm{Ens}(\nu)\times[\pm1])')
inv('margin note','below first live object, with curved leader',r'on siglera $S\mathcal T_{g\nu}^{\pm}$')
inv('deletion','on lower edge of live frame, toward right',r'\deleted{\unsure{\varnothing}}')
inv('margin note','large oblique left margin alongside diagrams and definition',r'Ça ne suffit pas tout à fait, pour avoir toutes les opérations')
inv('deletion','inside large margin note, after qui demande',r"\deleted{\unsure{l'introd.|liens}}")
inv('insertion','below crossed marginal word and before des',r"\inserted{\unsure{``ou''}}")
inv('text','main lower block',r'$S_1\mathcal T_{g,\nu}^{\pm}$ désigne le sous-groupoïde')
inv('insertion','above des after le graphe','bipondéré')
inv('deletion','left of the tuple in lower definition',r'\deleted{\mathcal T_{g,\nu}}')
inv('display','lower main tuple',parts['tuple'])
inv('insertion','vertical annotation directly under the tuple’s tilde-Sigma',r'\Vert\quad\partial X, stacked vertically')
inv('drawing','below the tuple, one vertex and a five-ray fan','g below the vertex; brace-like stroke and nu at upper right')
inv('text','right of the graph, two lines','toutes ces arêtes (libres) sont de poids 1')
inv('text','bottom main block',r'et $\mathcal T_{g,\nu}^{\pm}$ est défini ... $(X,\phi,\phi)$')
inv('text','lower-left corner','61','unnamed hand (folio annotation; attribution uncertain)')
notes=[
 dict(id=f'{page}-N01',text='The leaf asks for a preliminary devissage theorem: a global signed topological groupoid, with its graph and sign functors and elementary operations, should be reconstructed from the displayed connected fixed-type groupoids and functors. The underlined marginal exception removes operations 4 and 5 from the initial range 1:7; the larger margin explicitly says the displayed information is not quite sufficient. This is a proposed programme, not a proof on this leaf.'),
 dict(id=f'{page}-N02',text='The local definition sets nu equal to the number of boundary components and requires card(R intersect C_a)=1 for every boundary component. The figure carries the corresponding nu label and states weight 1 on its free edges. I checked this numerical agreement against the written definition. I did not establish the general graph construction or the reconstruction theorem.'),
 dict(id=f'{page}-N03',text='The final sentence defines the unmarked fixed-type groupoid through triples (X,phi,phi) with X of type g,nu. The marginal category is written T_{g,infinity}; it is not silently changed to T_{g,nu} merely to match the main display. No definition of that infinity-indexed object is supplied on this page.'),
 dict(id=f'{page}-N04',text='The first cancelled diagram has a rightward arrow to [plus-minus 1] and a downward arrow to Ens(nu). A separate lower cancelled T object has an oblique down-left arrow. Its crossed endpoint supplies no secure separate object. The old superscript, old horizontal-arrow label and isolated erased sign remain doubtful.'),
 dict(id=f'{page}-N05',text='The live enclosure has top and bottom bars and a separate left side, with no right side. Its lower-left annotation is on siglera, joined by a curved leader; the leader is not replaced by an opening parenthesis and no closing parenthesis is supplied. The annotation has gnu without a comma.'),
 dict(id=f'{page}-N06',text='Five rays are drawn in the small graph; the central one is faint. The brace-like mark is overworked and is reproduced by a path, not identified solely by a font brace. The numerical parameter remains nu: five drawn rays are a schematic count, not an assertion that nu=5. Under tilde-Sigma, the two short vertical strokes and partial-X form a vertical annotation column.'),
 dict(id=f'{page}-N07',text='The small pale mark after que is above the word baseline and is weaker than the adjacent writing; it is not promoted to punctuation. The lower folio 61 is transcribed without attributing its different-looking hand to a named writer.'),
]
checks=[
 dict(statement_id=f'{page}-N01',type='carried as background without fault found',outcome='The proposed reconstruction statement and its explicit marginal restrictions were retained as the author’s research programme. No proof was supplied by this leaf or attempted in this first reading.'),
 dict(statement_id=f'{page}-N02',type='used and rechecked in this run',outcome='I compared the local boundary-component count nu and the per-boundary marked-point count 1 with the figure’s nu label and written edge weight 1. This is a check of the stated numerical correspondence, not a proof of the construction.'),
 dict(statement_id=f'{page}-N03',type='carried as background without fault found',outcome='The fixed-type unmarked groupoid definition and the separate marginal infinity-indexed notation were carried literally. The page does not provide enough information to prove their role in operations 4 and 5.'),
]
notation=[
 dict(sign=r'S_* / S_f',meaning_or_form='The lower definition has a five-armed star under S. The earlier corresponding index is looped and f-like and remains explicitly doubtful.',places='upper ambient formula; lower definition',universality='The clear star settles only the lower occurrence; the upper shape is not asserted identical.',witness_errors='H reads f at both places; C reads star at both. The upper doubt is retained, while the lower f is corrected.'),
 dict(sign=r'\chi',meaning_or_form='Crossed curved strokes with a long lower-left sweep can resemble f in this hand.',places='interlinear sign functor; cancelled horizontal-arrow label',universality='Both local occurrences are obstructed or compressed; no universal identification is claimed.',witness_errors='C offers chi/f for the insertion; H gives f. The cancelled label is missing in C and left illegible in H.'),
 dict(sign=r'\Gamma',meaning_or_form='A heavily retraced Gamma has a connected lower foot; that foot is not a detached underline.',places='interlinear graph functor',universality='One occurrence on this page.',witness_errors='H adds an underline.'),
 dict(sign=r'\nu / \infty',meaning_or_form='Nu is generally a wedge-and-return form here; the marginal infinity has two connected loops.',places='main diagrams and definitions; T_{g,infinity} in the large margin',universality='The infinity distinction is local and was checked on the complete marginal formula.',witness_errors='H reads nu in the marginal category; C had infinity/nu alternatives.'),
 dict(sign=r'\phi',meaning_or_form='An oval crossed by a descending stem denotes the empty set; preserve the written phi shape.',places='both empty-set positions in the final triple',universality='Both final-triple instances agree. The heavily erased frame-bottom sign is not identified by this habit.',witness_errors='C uses varnothing and H emptyset in the final triple.'),
 dict(sign=r'\Vert',meaning_or_form='Two short vertical parallel strokes give an equality-type annotation above partial X, below tilde-Sigma.',places='lower tuple',universality='One vertical annotation column on this page.',witness_errors='Both witnesses record the annotation, but the proposal explicitly stacks its two levels.'),
 dict(sign='Gr.pond top',meaning_or_form='The graph-category abbreviation has a point after Gr and a space before top, with no independent point after pond.',places='interlinear target',universality='Page-specific punctuation only; do not standardize other occurrences from it.',witness_errors='Both witnesses print a point after pond; C also doubts top against rep.'),
]
abbreviations=[
 dict(form='isom.',expansion='isomorphisme(s), according to context; the ending of uniques/unique remains doubtful'),
 dict(form='Gr.pond top',expansion='graphes pondérés topologiques (expansion in notes only)'),
 dict(form='i.e.',expansion='id est'),
 dict(form='card',expansion='cardinal'),
 dict(form='Ens',expansion='ensembles'),
 dict(form="l'introd.",expansion="l'introduction, only if the doubtful cancelled reading is correct"),
]
boxes=[]
def box(kind,coords,reading):
    boxes.append(dict(box=f'B{len(boxes)+1:02}',kind=kind,x0=coords[0],y0=coords[1],x1=coords[2],y1=coords[3],reading=reading))
box('handwritten number',[730,20,825,95],r'\mspage{18}')
box('different words',[1110,225,1440,340],r'qui \unsure{dira|dise}')
box('different words',[1350,338,1610,418],r'\unsure{uniques|unique}')
box('doubtful formula',[586,455,860,596],r'$S_{\unsure{*|f}}\mathcal TD_{\mathrm{top}}^\pm$')
box('insertion',[824,392,1645,508],r'\inserted{avec le foncteur $\Gamma$ dans $(\mathrm{Gr.pond\ top})$ et $\unsure{\chi|f}$ dans $[\pm1]$, et}')
box('different words',[745,580,1620,695],r'$1^\circ:7^\circ$ (ou leurs variantes')
box('different words',[1046,677,1604,782],'se réconstitue')
box('margin note',[28,669,321,924],r"\margin{\uline{à l'exception de $4^\circ$ et $5^\circ$}}")
box('struck passage',[480,1047,1120,1602],parts['old1']+'\n'+parts['old2'])
box('doubtful formula',[690,1158,1673,1515],parts['live'])
box('margin note',[20,1275,610,1980],parts['margin'])
box('handwritten number',[510,1588,715,1694],r'$S_1\mathcal T_{g,\nu}^\pm$')
box('different words',[296,1715,458,1830],r'$S_*\mathcal T_{\mathrm{top}}^\pm$')
box('handwritten number',[1000,1817,1652,1892],r'$\operatorname{card}\pi_0\partial X=\nu$, et $\operatorname{card}R\cap C_a=1$')
box('different words',[306,1915,805,2023],r'(pour tout $a\in\pi_0\partial X$')
box('insertion',[1315,1875,1520,1951],r'\inserted{bipondéré}')
box('struck passage',[308,2012,804,2136],parts['tuple'])
box('low-confidence departure',[765,2070,910,2245],parts['graph'])
box('different words',[920,2098,1418,2235],r'toutes ces arêtes (libres) sont de poids $1$')
box('different words',[846,2279,1544,2348],r'$(X,\phi,\phi)$ où $X$ de type $g,\nu$.')
box('handwritten number',[36,2268,120,2334],r'\mspage{61}')
assert len({(b['x0'],b['y0'],b['x1'],b['y1']) for b in boxes})==len(boxes)
line_groups=[
 ('opening main paragraph',8),('two-line interlinear functor insertion',2),('underlined exception margin',2),
 ('cancelled diagram object rows',3),('live diagram row',1),('shorthand annotation rows',2),('isolated erased sign',1),
 ('large diagonal margin including separate crossed and replacement groups',9),('lower main definition lines',5),
 ('bipondere insertion',1),('two-level annotation below tilde-Sigma',2),('graph labels at two heights',2),
 ('two-line graph caption',2),('final main paragraph',2),('two folio annotations',2),
]
obj=dict(page=page,reader='reader_a',places_cropped=20,crop_files_saved=23,crop_files_viewed=23,lines_read=sum(n for _,n in line_groups),changes=changes,decisions=decisions,implicit_decisions=implicit,doubts=doubts,inventory=inventory,notes=notes,check_events=checks,notation=notation,abbreviations=abbreviations,second_boxes=boxes)
(root/'proposed'/f'{page}.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
(root/'proposed'/f'{page}_line_inventory.json').write_text(json.dumps(dict(method='Physical text/formula baselines, including separately written interlinear groups and object/label rows; bare arrows and frame strokes are not counted.',groups=[dict(group=g,lines=n) for g,n in line_groups],total=obj['lines_read']),ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'decisions':len(decisions),'implicit_decisions':len(implicit),'doubts':len(doubts),'inventory':len(inventory),'second_boxes':len(boxes),'lines_read':obj['lines_read'],'viewed_crops':len(records)},ensure_ascii=False))
