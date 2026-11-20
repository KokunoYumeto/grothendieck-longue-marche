from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-10',10,135);ch=r.change
four=r'fo\rlap{r}u\uline{r}bis'
r.edit(r'fou\uline{r}bis',four)
r.edit(r'itéré\deleted{\unsure{e|s}}',r'itéré\deleted{e}')
r.edit(r"cela entraîne qu'il y a un \unsure{antipodisme} ?",r"cela entraine qu'il y a un antipodisme ?")
r.edit(r'$A$-linéaire\unsure{,|.}',r'$A$-linéaire,')
r.edit(r'\unsure{6|b|Il}',r'\unsure{6|b}')
r.edit(r'\unsure{mett.|mettre}',r'mett.')
r.edit(r'\unsure{counités|co-unités}',r'counités')
r.edit(r'\underset{M}{\mathrm{L}}',r'\underset{M}{\mathrm{l}}')
r.edit(r'\unsure{\epsilon|\varepsilon}',r'\epsilon')
r.edit(r'\unsure{commute|commuta}',r'commute')
r.edit(r'\unsure{\mathbb{U}|\mathbb{u}|U|u}',r'\rlap{\(U\)}u')
r.edit("`centre'",r"\handwritten{``}centre\handwritten{''}")
r.edit(r'M\otimes M$ provenant',r'M\unsure{\ominus|\otimes}M$ provenant')
r.edit(r'A\longrightarrow A\otimes A$; il',r'A\longrightarrow A\unsure{\otimes|\ominus}A$; il')
r.edit(r'de dire que $A\otimes M\longrightarrow M$',r'de dire que $A\unsure{\ominus|\otimes}M\longrightarrow M$')
def leader(text,width):
 return r'''\begin{tikzpicture}[baseline=-.6ex,x=1cm,y=1cm]
\node[anchor=west,inner sep=0] at (0,.42) {'''+text+r'''};
\draw (.06,-.24) .. controls (.02,.12) and (.34,.18) .. (.75,.2) -- ('''+str(round(width-.4,2))+r''',.2) .. controls ('''+str(width)+r''',.22) and ('''+str(width)+r''',.32) .. ('''+str(round(width-.04,2))+r''',.43);
\end{tikzpicture}'''
ins=r'\inserted{\handwritten{\unsure{intersect°|intersect.} avec $A^{+}$}}'
r.edit(ins,leader(ins,4.2))
ins=r'\inserted{sur $k$}';r.edit(ins,leader(ins,1.6))
ins=r'\inserted{\handwritten{ayant une base dont fait partie $e$;}}';r.edit(ins,leader(ins,7.4))
ins=r'\inserted{de $A$ dans $M$}';r.edit(ins,leader(ins,3.8))
einsert=r'''\begin{tikzpicture}[baseline=-.6ex,x=1cm,y=1cm]
\node[anchor=west,inner sep=0] at (0,.42) {\inserted{$e_M$}};
\draw (.13,-.2) .. controls (.46,.2) and (.94,.26) .. (1.01,.67);
\end{tikzpicture}'''
r.edit(r'$\inserted{e_{M}}$',einsert)
def caret(letter):
 return r'''\begin{tikzpicture}[baseline=-.6ex,x=1cm,y=1cm]
\node[inner sep=0] at (.54,.52) {\inserted{$'''+letter+r'''$}};
\draw (-.08,.42) .. controls (-.35,.25) and (.65,.47) .. (.58,-.24) -- (1.02,.65);
\end{tikzpicture}'''
r.edit(r'$\inserted{G}$',caret('G'));r.edit(r'$\inserted{V}$',caret('V'))
# Reproduce the observed looped upright without identifying it as a letter.
loop=r'''\unsure{\begin{tikzpicture}[baseline=(e.base),x=1em,y=1em]
\node[inner sep=0] (e) at (0,0) {e};
\draw[line width=.35pt] (0,.1) .. controls (-.06,.28) and (-.08,.65) .. (.03,.67) .. controls (.2,.7) and (.14,.39) .. (.02,.34) -- (.01,.08);
\end{tikzpicture}}'''
r.edit(r'que\deleted{on}',r'qu'+loop+r'\deleted{on}')
r.edit(r'''M \arrow[dr] \& \& \unsure{A|\mathcal{A}}\otimes_{k}\overline{M} \arrow[ll,"\sim"'] \arrow[dl] \\
\& \overline{M} \&''',r'''M \arrow[dr] \& \unsure{A|\mathcal{A}}\otimes_{k}\overline{M} \arrow[l,"\sim"'] \arrow[d] \\
\& \overline{M}''')
ch('heading blank name','six separated dashes',r'\ill{} plus editorial note','six separated dashes','Six short horizontal marks occupy the name space. No letter remnants occur between them; this is a blank name represented by dashes, not physically unreadable writing.','heading; dashes','text not on the page','high',False,True,True)
ch('quotes around cocomplète',"``cocomplète''",'« cocomplète »',"``cocomplète''",'Each end has paired upright quote strokes, with no sideways chevrons. The grave on è is visible.','cocomplete','other','high')
ch('n over the two opening tensor signs',r'\overset{n}{\otimes}',r'\otimes^n',r'\overset{n}{\otimes}','Both n letters are centered directly above their tensor cells, rather than sitting after them as right superscripts. The crossed O-like typed construction is visible at both positions.','tensorformula','insertion or placement','high',False,True,False,True)
ch('fourbis overlapping cell and underline',r'fou\uline{r}bis','fourbis',four,'Inside the u cell an additional r stem and hooked upper shoulder remain visible. A separate short horizontal underline lies below the following r, not below the whole word. No independent strike cancels the overlapped r.','fourbis; fourbisfine','misread word','high',True,True)
ch('canceled ending of itéré',r'itéré\deleted{\unsure{e|s}}','itérée',r'itéré\deleted{e}','The canceled final cell retains an e bowl, middle bar and lower opening under the x strike. It is not a live extra e and the s alternative is excluded.','memeitere; itercancel','deletion state','high',True,True)
ch('intersection insertion',r'\unsure{intersect°|intersect.} avec A^+',r'intersection avec A^+ after Filt',r'\unsure{intersect°|intersect.} avec A^+ after noyau, with leader','The word is abbreviated: the small raised final mark remains ambiguous between a degree-like contraction and a point. The curved leader descends into the gap immediately after noyau and rises to the right of A-positive, so the insertion is placed there and the leader is reproduced.','intersection; interupright','insertion or placement','medium',True,True,False,True)
ch('opening of upper marginal question',r"cela entraîne qu'il y a un",r"\ill{} qu'il y a un",r"cela entraine qu'il y a un",'The upright crop shows cela, then e-n-t-r-a-i-n-e. The i carries a simple dot with blank paper around it, no circumflex. The words are readable.','uppermargin; entrainefine','readable ink left as \\ill{}','high',True,True,True)
ch('last word of upper marginal question',r'\unsure{antipodisme}','antipodisme','antipodisme','The initial a-n-t-i, descending p, round o, ascending d and final i-s-m-e sequence remain distinguishable after rotation; the question mark is separate. C doubt resolved.','uppermargin; antifine','other','high',True,False)
ch('avec unité insertion position','before à degrés','after degrees >= 0','before à degrés','The inserted typewritten words stand above the gap after coalgèbre and before à degrés. The acute on the final e meets the lowered m of Filt above it.','avecunite; avecunitefull; greater','insertion or placement','high')
ch('canceled s after degré',r'degré\deleted{s}','degré',r'degré\deleted{s}','The s reverse curves are visible beneath the x cancellation immediately before 0.','degre0; degreecancel','omission','high')
ch('sur k insertion and leader','before unitaire','after unitaire','before unitaire, with curved leader','The typed sur k sits above the gap between diagonal and unitaire. A curved line descends at that gap and curls upward to the right of k; both text and leader are reproduced.','surk','drawing or diagram','high',True,True)
ch('punctuation after A-linéaire',r'\unsure{,|.}','.',',','The punctuation has a dark upper head and a distinct descending pointed tail. It is a comma rather than a round full stop. C doubt resolved.','Alineaire','other','high',True,True)
ch('hand note first tensor',r'M\otimes M',r'M\otimes M',r'M\unsure{\ominus|\otimes}M','The open ellipse carries a nearly horizontal middle stroke; two crossing diagonals cannot be separated at maximum zoom. The barred-circle appearance is recorded first and a compressed tensor remains possible.','notemath1; tensorhand1fine','misread symbol or index','medium',True,True,False,True)
ch('hand note second tensor',r'A\otimes A',r'A\otimes A',r'A\unsure{\otimes|\ominus}A','The open loop has faint short interior strokes clustered at the lower left. They suggest a compressed cross but do not securely exclude a single bar.','notemath2; tensorhand2exact','misread symbol or index','medium',True,True,False,True)
ch('hand note third tensor',r'A\otimes M',r'A\otimes M',r'A\unsure{\ominus|\otimes}M','The flattened loop has a prominent oblique-to-horizontal bar. A second crossing stroke cannot be isolated from the thick lower edge.','notemath3; tensorhand3exact','misread symbol or index','medium',True,True,False,True)
ch('state of second hand-note line','live A tensor M to M comp. avec application diagonale','struck same clause','live clause, with qualified tensor','The complete second line is written without an independent horizontal or diagonal cancellation stroke. The connecting letters and the closing parenthesis remain live.','note2; notemath3','deletion state','high',False,True,False,True)
ch('initial mark in outlined marginal note',r'\unsure{6|b|Il}','omitted',r'\unsure{6|b}','One long slanted stem ends in a closed lower loop. There is no second stem for Il. The mark is 6-like but b cannot be excluded.','midmargin; midfirst','omission','medium',True,True)
ch('abbreviation in outlined marginal note',r'\unsure{mett.|mettre}','mettre','mett.','After m-e the two short tall strokes are followed by a distinct point. There is no r-e continuation. C doubt is resolved in favor of the abbreviation.','midfirst','abbreviation expanded or spelling modernised','high',True,True)
ch('last two lines of outlined note',r'compatible aux \unsure{counités|co-unités}',r'est-il aussi associatif','compatible aux counités','The upper line reads compatible aux; the lower reads c-o-u-n-i-t-é-s with a visible acute. No hyphen separates co and unités, and the exclamation mark follows. The ink does not read H associativity clause.','midlast; midmath','misread word','high',True,True,False,True)
ch('outline of middle marginal note','TikZ outline','described as encadrée','TikZ outline retained','A long top curve runs into the right boundary, then curves left below the words; the left side remains open. C drawing retains this shape, while H only describes it.','midmargin','drawing or diagram','high',False,True)
ch('quotes around unité',"``unité''",'« unité »',"``unité''",'Both ends have paired upright strokes, with no angle marks. The acute on unité is present.','unitquote','other','high')
ch('first letter and underwritten M in l-image',r'\underset{M}{\mathrm{L}}',"l'image without M",r'\underset{M}{\mathrm{l}}',"The first typed glyph has the top-left serif and bottom foot of lowercase l, not the two full-height strokes of a capital L. A plain M is typed directly below it and is not canceled.",'Limage','misread symbol or index','high',True,True)
ch('e-M insertion leader','e_M insertion','e_M insertion','same insertion with sloping curved leader','The e with lowered M stands above the gap after image. A rising S-like line begins in that gap and ends above-right of the inserted letters; it is reproduced in TikZ.','einsert','drawing or diagram','high',True,True)
ch('epsilon form',r'\unsure{\epsilon|\varepsilon}',r'\varepsilon',r'\epsilon','The hand sign has a single C-shaped outer curve with a straight middle bar, not the two opposed curves of varepsilon. C doubt resolved. The lowered M, e_M and right-hand 1 are clear.','epsformula; epsilon','misread symbol or index','high',True,True,False,True)
ch('looped trace over e in que','plain e','plain e','e with qualified looped trace reproduced in TikZ','A narrow dark loop rises above the e and continues as a short upright through its upper bowl. The trace is drawn as seen without calling it a particular letter or assigning a correction history. Its meaning remains uncertain.','queon; quemystery','drawing or diagram','low',True,True)
ch('canceled on after que',r'que\deleted{on}','que',r'que\deleted{on}, with qualified trace on e','The o and n remain visible below the typed x cancellation; H omits them.','queon','deletion state','high',False,True)
ch('base insertion, its endpoint and leader',r'ayant une base dont fait partie e; inserted',r'ayant une base dont fait partie e_1 in margin',r'ayant une base dont fait partie e; inserted after libre comma, with leader','The final e has no lowered numeral; the next marks are a semicolon. The long lower line turns down immediately after the comma following libre and curls up after the inserted semicolon, so the insertion and leader are retained at that position.','basenote; baseupright; baseend','insertion or placement','high',True,True,False,True)
ch('inline isomorphism arrow',r'\unsure{\longleftarrow|\longleftrightarrow}',r'\xrightarrow{\sim}',r'\overset{\sim}{\unsure{\longleftarrow|\longleftrightarrow}}','The left-pointing head and one wavy stroke above the shaft are clear. The heavily worked right end contains an apparent covered arrowhead; it is not possible to decide whether the right head remains live. C alternatives retained, with left arrow first.','isom; isoarrow','misread symbol or index','medium',False,True,False,True)
ch('A alphabet in handwritten diagram',r'\unsure{A|\mathcal{A}}','A',r'\unsure{A|\mathcal{A}}','A rounded top, heavy crossbar and long left downstroke remain visible. Heavy retracing obscures whether the extended left stroke belongs to a calligraphic form; C qualification retained.','diagram; diagramA','misread symbol or index','medium',False,True,False,True)
ch('diagram arrow and similarity label','triangle with both legs diagonal and sim',r'right leg vertical and approx','right leg vertical and sim','The left descending leg points toward barred M, while the right leg is drawn almost vertically down. Above the horizontal left-pointing arrow there is one wavy stroke, not the two strokes of approx. The diagram uses the observed vertical right leg and single sim label.','diagram; diagramarrow; tensordiagfine','drawing or diagram','high',True,True,False,True)
ch('word after diagram',r'\unsure{commute|commuta}','commute','commute','The terminal letter after the tall crossed t is a short open e-like return with no enclosed a bowl. C e/a doubt is resolved in favor of e.','diagramtail; commutefine','misread word','medium',True,False)
ch('question mark beside diagram','?','omitted','?','A curved upper hook, descending stem and separate lower dot stand in the left margin next to the diagram.','question; diagram','omission','high')
for letter,crop in [('G','Ginsert'),('V','Vinsert')]:
 ch(letter+' insertion caret',letter+' inserted',letter+' inserted',letter+' inserted with caret','The typed letter stands above the baseline. A left curved branch descends to the insertion point and a long oblique right branch rises beside the letter; the two-branch leader is reproduced in TikZ.',crop,'drawing or diagram','high',True,True)
ch('example arrow after u',r'\unsure{\vdash|\mapsto}',r'\mapsto',r'\unsure{\vdash|\mapsto}','The left terminal bar and horizontal shaft are clear. The right tip is a compact rounded blot without two separable arrowhead arms. C alternatives remain; the adjacent g-arrow does have a clear right head.','umaplast; lastmaparrow; gmap','misread symbol or index','medium',False,True,False,True)
ch('example right-hand u/U collision',r'\unsure{\mathbb{U}|\mathbb{u}|U|u}','u',r'\rlap{\(U\)}u','The cell has upper serifs at capital height and a second pair at lowercase height, with a lower u-like terminal foot. These are overlapping unlike typed impressions, not a securely identifiable blackboard alphabet. Both U and u are retained without inferring order.','umaplast; lastu','misread symbol or index','high',True,True,False,True)
ch('de A dans M leader','insertion','insertion','same insertion with curved leader','The typed phrase sits above est injectif. Its leader descends immediately after the preceding e and curls up after the inserted M.','deAMinsert','drawing or diagram','high',True,True)
ch('quotes around centre',"`centre'",'« centre »',r"\handwritten{``}centre\handwritten{''}",'Each hand quote has two short upright strokes joined near the lower end. They are double quotes rather than a single apostrophe or guillemets.','centre; centrequotes','other','high',True,True)
ch('dash before parait-il','single short hyphen','em dash','single short hyphen','The isolated dash has the same short width as the internal hyphen in parait-il. The i of parait has a dot and no circumflex; both witnesses retain that spelling.','paraitdash','other','high')
for line,reading,alts,conf,comment in [
 ('intersection abbreviation','intersect°','intersect.','medium','Raised small final mark is not resolved between degree-like abbreviation and point.'),
 ('middle margin initial mark','6','b','medium','One long stem and lower loop; Il excluded.'),
 ('hand note first tensor',r'\ominus',r'\otimes','medium','Loop with nearly horizontal bar, no distinct crossing pair.'),
 ('hand note second tensor',r'\otimes',r'\ominus','medium','Faint interior strokes cluster at lower left.'),
 ('hand note third tensor',r'\ominus',r'\otimes','medium','One prominent bar; possible second stroke merged into lower loop.'),
 ('e in que','e with looped vertical trace','','low','The trace is reproduced in TikZ without assigning letter identity or correction history.'),
 ('inline isomorphism arrow',r'\longleftarrow',r'\longleftrightarrow','medium','Left head clear; right end overworked.'),
 ('diagram A alphabet','A',r'\mathcal{A}','medium','Heavy retracing and long left stroke.'),
 ('example map arrow',r'\vdash',r'\mapsto','medium','Right terminal blot does not expose a secure arrowhead.')]:r.doubt(line,reading,alts,conf,comment)
r.notation('typed tensor construction',r'\otimes','10:135 seven typed occurrences: two in opening formula; map to iterated I-positive; M diagonal; e diagonal; quotient; isomorphism. The O-like ring is overlaid with crossed strokes; n is centered above the first three.')
r.notation('hand tensor variants',r'\unsure{\ominus|\otimes}; \unsure{\otimes|\ominus}; \otimes','10:135 three interlinear-note symbols qualified individually; outlined marginal note and diagram have a distinguishable low cross','uncertain')
r.notation('plain typed alphabets','A,M,k,G,V,u,e,I','10:135 all occurrences individually enlarged; I-positive has straight serifs; U/u collision in example retained separately')
r.notation('hand epsilon and Delta',r'\epsilon_M; \Delta_M','10:135 counit formula has single C-curve and middle bar; two Delta triangles have an open upper/right join')
r.notation('arrows and mapsto',r'\longrightarrow; \mapsto; \unsure{\vdash|\mapsto}','10:135 three plain right arrows in typed text; u mapsto u.e; last g mapsto g.a; example u-arrow tip remains qualified','uncertain')
r.notation('bars and quotient',r'\overline M=M\otimes_A k','10:135 hand bars over typed M in quotient and isomorphism; two hand barred M labels in diagram')
r.notation('indices and plus signs',r'A^+; I^+; Filt_m(A); e_M; \geq0','10:135 raised plus in first formula, intersection and target; lowered m in Filt; lowered M in e and diagonal/counit; separate lower bar under greater')
r.notation('quote shapes',"``...''",'10:135 cocomplète and unité typed; centre supplied in hand; all double upright forms, no guillemets')
r.notation('unlike-letter overlap',r'fo\rlap{r}ur bis; \rlap{\(U\)}u','10:135 fourbis u-cell and example right-hand u; loop over que e kept as a drawing of uncertain meaning','uncertain')
r.r['abbreviations']=[dict(abbreviation=a,expansion=b,attestations='10:135 '+p) for a,b,p in [('NB','nota bene','parenthetic condition'),('m.ème','m-ième','iterated diagonal, kept literally'),('intersect° / intersect.','intersection','hand insertion, final mark uncertain'),('mett.','mettre','outlined marginal question'),('hyp.','hypothèses','outlined marginal question'),('comp.','compatible','interlinear note'),('i.e.','id est','unit and example')]]
r.r['inventory_overrides']={'135-05':dict(first_words_or_objects='itéré with canceled final e resolved'),'135-08':dict(first_words_or_objects="cela entraine qu'il y a un antipodisme ?"),'135-15':dict(first_words_or_objects='6/b faut il mett. dans les hyp. que A tensor M -> M compatible aux counités !'),'135-18':dict(first_words_or_objects='lowercase l with M below in l-image'),'135-20':dict(first_words_or_objects='epsilon_M and Delta_M, epsilon form resolved'),'135-21':dict(first_words_or_objects='canceled on, preceding e bears qualified looped trace'),'135-27':dict(first_words_or_objects='M <-sim- A tensor_k Mbar, diagonal left leg and vertical right leg to Mbar'),'135-28':dict(first_words_or_objects='commute, et que ...'),'135-35':dict(first_words_or_objects='u vdash/mapsto overlapping U/u . e')}
extra=[('r/u overlap in fourbis','text','first displayed tensor decomposition','typewriter'),('intersection insertion leader','drawing','after noyau','his hand'),('sur k insertion leader','drawing','between diagonal and unitaire','his hand'),('e_M insertion leader','drawing','after image','his hand'),('looped trace above e','drawing','que before canceled on','unnamed hand'),('base insertion leader','drawing','after libre comma','his hand'),('G insertion caret','drawing','after first connexe','his hand'),('V insertion caret','drawing','after second connexe','his hand'),('U/u overlapping typed impressions','text','example u-arrow expression','typewriter'),('de A dans M insertion leader','drawing','before est injectif','his hand'),('double hand quotes around centre','insertion','parenthesis a le centre de V','his hand')]
for i,(s,k,p,h) in enumerate(extra,1):r.r['inventory_extra'].append(dict(scan='10:135',sheet_kind='typescript',hand=h,element=f'135-R{i:03d}',kind=k,position=p,first_words_or_objects=s,transcribed='yes'))
r.r['crops']=sum([json.loads(Path('work/'+p).read_text()) for p in ['crops135.json','crops135_extra.json','crops135_extra2.json']],[])
r.r['inspection_note']='Root alone viewed whole135 and both supplied halves before C/H, all13 C doubts and all37 C inventory entries. All98 crop recipes were actually viewed. Three crops from an initially truncated output were re-viewed; two narrowly misplaced tensor fine crops were also viewed and followed by corrected exact crops. Both slanted margins were rotated upright. Every mathematical symbol, cancellation, insertion, marginal note and C/H difference was enlarged; both supplied halves were reread line by line before finalization. Typed O-plus-cross tensor construction is retained as otimes; hand flattened variants are qualified individually. The loop over que e is drawn without identifying its meaning. Archival134 remains solely a comment. No OCR, parallel transcription, context access or mathematical check occurred.'
r.save('work/record135.json')
