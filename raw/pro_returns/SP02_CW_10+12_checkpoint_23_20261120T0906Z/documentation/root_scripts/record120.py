from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-08',10,120);ch=r.change
r.edit(r'\scanpage{120}',r'\scanpage{120}'+'\n'+r'\mspage{119}')
r.edit('% archive sheet number: 119','')
r.edit(r"``compatible avec $\otimes$ èommutatif",r"``compatible avec $\unsure{\otimes|\Omega}$ èommutatif")
r.edit(r'\unsure{v|c}',r'\rlap{v}c')
r.edit(r'\inserted{dans 1º}',r'\inserted{dans 1º\handwritten{\begin{tikzpicture}[x=.45cm,y=.45cm,baseline=-.2ex]\draw (0,-.3) .. controls (-.12,.14) and (.05,.3) .. (.29,.28)--(1.5,.32) .. controls (1.71,.35) and (1.77,.53) .. (1.73,.66);\end{tikzpicture}}}')
unit=r'\unsure{\rlap{\begin{tikzpicture}[x=1em,y=1em,baseline=0pt]\draw[line width=.45pt] (.38,.04)--(.38,.45) .. controls (.43,.42) and (.48,.29) .. (.42,.24);\fill (.28,.72) circle (.045);\fill (.82,.77) circle (.03);\fill (.96,.75) circle (.04);\draw[line width=.4pt] (.7,.08)--(.62,.27)--(.73,.43);\end{tikzpicture}}unité|mité}'
r.edit(r'\unsure{unité|mité}',unit)
r.edit('bilatèrité',r'bilatèr\rlap{e}ité')
r.edit(r'\unsure{foncteu}','foncteu')
r.edit(r'\inserted{\handwritten{(mais bien de b)}}',r'\inserted{\handwritten{(mais bien de b)\begin{tikzpicture}[x=.6cm,y=.6cm,baseline=-.2ex]\draw (0,-.25) .. controls (.03,.05) and (.11,.15) .. (.31,.17)--(2.6,.19) .. controls (2.86,.21) and (3.05,.32) .. (3.04,.56);\end{tikzpicture}}}')
curl=r'\handwritten{\unsure{\begin{tikzpicture}[x=.45cm,y=.45cm,baseline=-.3ex]\draw[line width=.8pt] (.48,.9) .. controls (.22,.68) and (.25,.64) .. (.55,.66) .. controls (.72,.68) and (.68,.49) .. (.61,.45);\draw[line width=.8pt] (.38,.61) .. controls (-.03,.54) and (.02,.39) .. (.15,.29)--(.55,.29);\draw[line width=1pt] (.16,.3) .. controls (-.04,.1) and (.02,.01) .. (.18,-.09)--(.16,.3);\end{tikzpicture}}}'
r.edit(r'$c$\deleted{\unsure{)}}',r'$c$\deleted{\unsure{)}}'+curl)
marke=r'\unsure{\rlap{\raisebox{1ex}{\hspace{.25em}\begin{tikzpicture}[x=1em,y=1em]\draw[line width=1pt] (0,0)--(0,.28);\end{tikzpicture}}}e|e}'
r.edit('sous réserve de vérification','sous réserve d'+marke+' vérification')
r.edit(r'\unsure{biaddiv|biadditiv}',r'\unsure{biaddii|biaddiv}')
r.edit(' NB Si',r' $\mathbb{NB}$ Si')
r.edit(r'\unsure{\mathbb{E}|\mathrm{E}}',r'\unsure{\rlap{\(\mathrm{e}\)}\mathrm{E}|\mathbb{E}}')
r.edit('ce monoïde opère','ce monoide opère')
r.edit('coïncident',r'co\rlap{n}ïncident')
r.edit(r'add\unsure{i|o}tive',r'add\rlap{o}itive')
r.edit(r'add\rlap{o}itive, $\mathrm{End}',r'add\rlap{o}itive, $\mathrm{E}\rlap{\(\mathrm{b}\)}\mathrm{nd}')
r.edit('commytatif',r'comm\rlap{u}ytatif')
ch('opening and later quotation marks','paired straight quotes','guillemets','paired straight quotes','The opening and closing marks are pairs of short typed strokes, also in the later Foncteur quotation; no angular guillemets are drawn.','opening; foncteur-row','other')
ch('first and recurring typed tensor','otimes','otimes',r'first \unsure{\otimes|\Omega}; eight later typed occurrences otimes','The nine recurring typed glyphs have crossed inner strokes, an arched top and lower feet. The first is qualified; later occurrences use its first candidate. The separate disputed sign after des and the clear final hand circled cross are distinguished.','tensor1; loi2; loi3; foncteur-row; hom-row; tensor-add; nbline; formula','misread symbol or index','medium',True,True,False,True)
ch('opening èommutatif','èommutatif','commutatif','èommutatif','The first letter has a closed e bowl and crossbar, with a detached left-sloping grave mark above it.','comm-initial','abbreviation expanded or spelling modernised')
ch('opening sign after des',r'\unsure{\otimes|\deleted{x}}','omitted',r'\unsure{\otimes|\deleted{x}} retained','An enclosing oval with crossing strokes and flat upper/lower bars is visible. Its relation to a canceled x cannot be separated securely, so both readings and the possible deletion state remain.','desmark','omission','low',False,True,False,True)
ch('opening handwritten letter',r'\unsure{\mu|\psi}','psi',r'\unsure{\mu|\psi} retained','The hand sign has low joined legs and a long through-stroke; its mu/psi identity remains uncertain after enlargement.','mu','misread symbol or index','medium',False,True,False,True)
ch('del\'axiomatique spacing',"del'axiomatique","de l'axiomatique","del'axiomatique",'The e and l occupy adjacent regular typewriter cells without an intervening blank cell. The m/a bodies within axiomatique are adjacent letters, not an overprint.','para1; axiomatique','other')
ch('second pair a) et v/c',r'\unsure{v|c}','qualified c',r'\rlap{v}c','The same type cell contains a pointed v with two diagonals and an open curved c body. Both are retained as an overlap without assigning a revision order.','cv; loi2','misread symbol or index','high',True,True,True,True)
ch('canceled fragment after paquet',r"\unsure{d'ax}",'deleted ill',r"\unsure{d'ax} retained",'The d ascender, raised apostrophe and a bowl can be followed beneath the crosses. The last x could be only a cancellation mark, so the fragment remains qualified.','dax','readable ink left as \\ill{}','low',False,True,True)
ch('guide for dans 1º','omitted','omitted','local curved insertion guide','A thin line rises from after haut, runs beneath the inserted words, and turns upward to their right. Its left curl is a guide rather than an additional parenthesis.','dans1; compat-row','drawing or diagram','high',True,True)
ch('unité initial overmarks',r'\unsure{unité|mité}','unité','qualified unité with initial strokes/dots drawn; mité alternative','There are extra vertical/curved traces in the first two cells, one dot over the first and two over the second; the following i-t-é are clear. The visible marks are reproduced without assigning the obscured lower letter sequence confidently.','unit-over; unit-first','drawing or diagram','low',True,True)
ch('bilatèrité overprint','bilatèrité','bilatèrité',r'bilatèr\rlap{e}ité','The cell after r has a rounded e bowl/crossbar together with the stem and dot of i. The overlap does not remove the remaining t-é.','bilaterite','misread word','high',True,True)
ch('canceled foncteu fragment',r'\unsure{foncteu}','deleted ill','deleted foncteu','The seven cells f-o-n-c-t-e-u remain readable beneath the x row. No further r body is visible, and no completion is supplied.','foncteu','readable ink left as \\ill{}','medium',True,True,True)
ch('mais bien de b insertion position','after envisager','before qu\'on peut envisager','after envisager','The guide begins at the end of envisager and passes beneath the handwritten insertion. It is placed before the following comma.','mais; struct-row','insertion or placement','high',False,True,False,True)
ch('mais bien de b closing mark','one closing parenthesis','two closing parentheses','one closing parenthesis','There is one hand closing curve directly after b. The farther right rising stroke belongs to the insertion guide.','mais','text not on the page')
ch('mais insertion guide','omitted','omitted','long shallow guide reproduced','The line runs under the inserted words and turns up after them, with its left end at the insertion point.','mais','drawing or diagram','high',True,True)
ch('canceled mark after c',r'\deleted{\unsure{)}}','live )',r'\deleted{\unsure{)}} retained','A typed closing curve lies under blue zigzag strokes; the precise body remains obscured, but the cancellation is visible.','cclose','deletion state','low',False,True)
ch('curl below canceled parenthesis','omitted','omitted','qualified graphic trace reproduced','Below the crossed parenthesis are a hooked upper curve, a left-returning curve, a rightward middle arm and a thick small lower loop. Whether this is a separate letter or a cancellation flourish is unresolved.','close-bottom; cclose','drawing or diagram','low',True,True)
ch('de in canceled verification clause','de','de','d plus e with qualified vertical overmark drawn','A thick short vertical stroke rises from the top of e to ascender height. It is retained graphically; its origin as a second letter or accent cannot be identified securely.','de-verif; verification','drawing or diagram','medium',True,True)
ch('dash before Quant','short hyphen','em dash','short hyphen','One typewriter-length horizontal dash follows the preceding point; it is not a long hand dash.','quant','other')
ch('Quand correction',r'Quan\deleted{d}\handwritten{t}','Quant',r'Quan\deleted{d}\handwritten{t}','The typed d bowl/ascender is crossed, with a thinner hand t written across/above it. Both states remain visible.','quant','deletion state')
ch('a after Quant','a','à','a','The vowel has no detached accent above its body.','quant','abbreviation expanded or spelling modernised')
ch('long canceled phrase','structure bilinéaire, il y a lieu de','deleted ill','structure bilinéaire, il y a lieu de, deleted','The full letter sequence, comma and accent remain legible below the x cancellation, from structure through the final de.','structdel; structdel-left; structdel-right','readable ink left as \\ill{}','high',False,True,True)
ch('upper canceled biaddiv fragment',r'\unsure{biaddiv|biadditiv}','live biadditiv ill',r'\deleted{\unsure{biaddii|biaddiv}}','Seven underlying letter remnants can be distinguished before a further bare cancellation x. The final dotted upright favors i; the complete expected word is not supplied. Typed x marks cross the upper insertion itself.','biaddiv','deletion state','low',True,True,True)
ch('section5 old enumeration','deleted5) and inserted hand5)','one live5)','deleted5) and inserted hand5)','The original typed 5) is crossed by blue pen; a separate hand 5) stands above it.','five','omission')
ch('NB punctuation','NB','N.B.','NB without points','No point occurs between or after the two capital letters.','NB','abbreviation expanded or spelling modernised')
ch('NB repeated type','plain NB','plain NB',r'\mathbb{NB}','Offset repeated stems/diagonals are visible in N, and two displaced outer bowl contours in B. Repeated type is represented with the prescribed mathbb convention.','NB','other','medium',True,True)
ch('hand exclamation at first equality','overset hand !','omitted','overset hand !','A short oblique stroke and lower point stand above the equality between u tensor v and uv.','formula; bang','omission','high',False,True,False,True)
ch('canceled small mark after commutativité',r'\deleted{\unsure{x|,}}','omitted',r'\deleted{\unsure{x|,}} retained','A lowered crossed character has projecting short stems. The underlying punctuation cannot be distinguished reliably from the overstrike.','commx','omission','low',False,True)
ch('first End initial letter',r'\unsure{\mathbb{E}|\mathrm{E}}','ordinary E',r'\unsure{\rlap{\(\mathrm{e}\)}\mathrm{E}|\mathbb{E}}','The upper E arms coexist with a rounded lower bowl and crossing bar resembling e. An e/E overlap is the qualified first candidate; repeated E remains possible.','End1','misread symbol or index','low',True,True,False,True)
ch('canceled upper il opère sur tous','inserted and deleted il opère sur tous','deleted ill','inserted and deleted il opère sur tous','The i/l, accent, separate word spaces and tous remain legible beneath the x row above the baseline cancellation.','ilopere','readable ink left as \\ill{}','high',False,True,True)
ch('canceled lower Si C est additif','deleted Si underlined C est additif, c\'est','same undifferentiated deleted ill','deleted Si underlined C est additif, c\'est','The full baseline text is readable under the separate cancellation; the C has its own short underline.','sic','readable ink left as \\ill{}','high',False,True,True)
ch('second monoide accent','monoïde','monoide','monoide','One round dot lies above the i stem. There is no second dot or grave stroke in the close-up.','monoid2; sans-row','misread word','high',True,False)
ch('coïncident overlapped cell','coïncident','coïncident',r'co\rlap{n}ïncident','The first cell after co contains the dotted ï stem and an additional n arch with left/right stems; the following n occupies a separate cell.','coincide; co-over','misread word','high',True,True)
ch('inserted C after la structure','plain C','underlined C','plain C','The inserted C is one open curved type body, without a detached lower bar.','structure','misread symbol or index','high',False,True,False,True)
ch('additive fourth letter',r'add\unsure{i|o}tive','additive',r'add\rlap{o}itive','The same cell has a complete o oval and a central i stem with a detached dot. Both bodies can be read, resolving the alternative as an overlap.','additive','misread word','high',True,True)
ch('second End n cell','ordinary n','ordinary n',r'\mathrm{E}\rlap{\(\mathrm{b}\)}\mathrm{nd}','A tall b ascender and rounded bowl share the n cell with the lower n arch. The initial E and final d remain separate regular letters.','End2','misread symbol or index','medium',True,True,False,True)
ch('C after chaque objet de','plain C','underlined C','plain C','Only the open C body is present; no separate lower stroke appears.','droit-row','misread symbol or index','high',False,True,False,True)
ch('last End equals k',r'\unsure{\mathbb{k}|k}','plain k',r'\unsure{\mathbb{k}|k} retained','Two close vertical outlines are visible, while the right arms are congested. The doubled-type reading remains qualified rather than inferred from darkness alone.','End3k; k-over','misread symbol or index','medium',False,True,False,True)
ch('commytatif overlapped vowel','commytatif','commutatif',r'comm\rlap{u}ytatif','A u bowl and right foot coexist with the diagonal and long descending loop of y. The two bodies share one cell; neither is suppressed.','commytatif; commy-over','misread word','high',True,True)
ch('final catégorie C','plain C','underlined C','plain C','The C is an open typed curve without a lower bar.','last-row','misread symbol or index','high',False,True,False,True)
ch('folio','comment119','administrative page119','mspage119','Three pencil figures at lower left read119.','folio','insertion or placement','high',True,True)
for args in [
 ('first recurring typed tensor',r'\otimes',r'\Omega','medium','Nine typed instances; the first is qualified, with later first-candidate tokens.'),
 ('sign after des',r'\otimes','canceled x','low','Oval, cross and flat bars do not settle symbol/deletion state.'),
 ('hand sign after des',r'\mu',r'\psi','medium','Joined legs and through-stroke remain ambiguous.'),
 ('canceled fragment after paquet',"d'ax","d'a followed by cancellation x",'low','Last x may belong only to cancellation.'),
 ('unité initial cells','unité with extra initial strokes/dots drawn','mité; mixed overwritten initial letters','low','The physical traces are kept; the obscured sequence is not completed from grammar.'),
 ('canceled mark after c',')','','low','Blue zigzag obscures the typed curved body.'),
 ('curl below canceled parenthesis','drawn hooked/looped trace','cancellation flourish; epsilon-like letter','low','Visible geometry retained without a letter assignment.'),
 ('e of de in canceled verification','e with vertical overmark drawn','plain e; accent or overtyped letter','medium','The upper stroke is distinct, its origin unresolved.'),
 ('canceled upper fragment','biaddii','biaddiv','low','Seven underlying letter remnants; final dotted upright favors i.'),
 ('canceled small mark before c)','x','comma beneath x','low','The lowered crossed form remains unclear.'),
 ('first End initial','qualified e/E overlap','doubled E; ordinary E','low','Rounded lower loop favors an additional e body, but dense ink obscures the layers.'),
 ('last End equals k',r'\mathbb{k}','k','medium','Two upright outlines are visible; the right arms are congested.')]:r.doubt(*args)
r.notation('typed tensor sign','crossed arch with lower feet; first tensor/Omega qualified, eight later first-candidate tokens','10/120','unresolved')
r.notation('opening special crossed sign','oval and cross with flat bars; tensor or canceled x, distinct from recurring typed family','10/120','unresolved')
r.notation('hand commutor','mu/psi qualified','10/120','unresolved')
r.notation('physical typed overlaps','v/c; e/i in bilatèrité; n/ï in coïncident; o/i in additive; b/n in second End; u/y in commytatif; qualified e/E in first End','10/120','partly unresolved')
r.notation('repeated type','NB as mathbb; final k doubled/plain qualified','10/120','partly unresolved')
r.r['abbreviations']=[dict(abbreviation=a,expansion=b,attestations='10/120') for a,b in [('NB','nota bene'),('comm.','commutativité / commutatif'),('foncteu','foncteur (canceled fragment)')]]
r.r['inventory_overrides']={
 '001':{'first_words_or_objects':'opening quotation; èommutatif; qualified tensor/canceled-x and hand mu/psi'},
 '002':{'first_words_or_objects':'possible cancellation x, retained as alternative to crossed symbol'},
 '009':{'first_words_or_objects':'dans 1º with curved guide'},
 '010':{'first_words_or_objects':'foncteu, canceled readable fragment'},
 '012':{'first_words_or_objects':'(mais bien de b) after envisager, one closing curve, local guide'},
 '013':{'first_words_or_objects':'same handwritten insertion and guide'},
 '015':{'first_words_or_objects':'canceled verification clause; e of de with qualified upper stroke'},
 '019':{'first_words_or_objects':'canceled inserted qualified biaddii/biaddiv'},
 '020':{'first_words_or_objects':'qualified biaddii/biaddiv under typed cancellation'},
 '029':{'first_words_or_objects':"Si underlined C est additif, c'est, canceled"}}
extras=[('guide-dans','after haut','curved guide for dans 1º','drawing','his hand'),('unit-marks','first two cells of unité','qualified overtyped strokes and dots','drawing','typewriter'),('guide-mais','after envisager','curved guide for (mais bien de b)','drawing','his hand'),('curl-close','below canceled parenthesis after c','qualified hooked and looped trace','drawing','his hand'),('e-mark','e of de in verification clause','short vertical overmark','drawing','typewriter'),('nb-block','section5 paragraph','NB and endomorphism paragraph, including overlaps and cancellations','text','typewriter'),('formula','section5 on a','u,v of underlined1; u tensor v with ! over equality, equals uv equals vu','display','typewriter'),('folio','lower left','119','margin note','unnamed hand')]
for ident,pos,txt,kind,hand in extras:r.r['inventory_extra'].append(dict(scan='10:120',sheet_kind='typescript',hand=hand,element='120-extra-'+ident,kind=kind,position=pos,first_words_or_objects=txt,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops120.json').read_text())
r.r['inspection_note']='Root viewed whole120 then both halves, C/H, all12 C uncertainty fields and32 C inventory elements. All67 crops were viewed: the final four more-crop images were initially output-truncated and then repeated individually successfully. The mais insertion and bottom handwritten note were rotated upright. All agreed text, formula signs, indices, deletions and insertions were checked against ink. The initial d of données is dark but no securely separable second full letter was established; plain d is retained. The m/a in axiomatique and s\'exprimant are neighboring cells, not overlaps. No OCR, parallel transcription, context, compilation or mathematical checking. No121 image opened before finalization.'
r.save('work/record120.json')
