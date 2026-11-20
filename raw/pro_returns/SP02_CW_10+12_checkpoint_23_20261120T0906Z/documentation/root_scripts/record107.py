from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-07',10,107);ch=r.change
r.edit(r'\scanpage{107}',r'\scanpage{107}'+'\n'+r'\mspage{106}')
r.edit('% archive sheet number: 106','')
r.edit('rationnelle','rationelle')
r.edit(r'\inserted{$\unsure{\otimes|\Omega}$-}',r'\inserted{$\otimes$-}')
r.edit(r'\unsure{OU|Ou}',r'O\rlap{\raisebox{.6ex}{U}}u')
r.edit(r'\unsure{celle-ci,}','celle-ci,')
r.edit(r'\unsure{la}','la')
r.edit(r'$(n,n)$,',r'$(n,n)$),')
r.edit(r'sur $V_{\underline{C}}$,',r'sur $V_{\underline{\mathbb{C}}}$,')
r.edit(r'(\handwritten{i})',r'(\handwritten{\unsure{i|-i}})')
r.edit('muni du',r'muni d\rlap{e}u')
r.edit('sur $H^*(X,',r'sur $H^{\handwritten{*}}(X,')
r.edit(r'i_1(\handwritten{\bar{\lambda}})}',r'i_1(\handwritten{\bar{\lambda}}\rlap{\tikz[baseline=0pt,x=1em,y=1em]{\draw (-.05,.25)--(.65,.25);}})}')
r.edit('des pré-structures de Hodge. La conjecture',r'des pré-s\rlap{c}t\rlap{t}r\unsure{\rlap{r}u|u}ctures de Hodge. La conjecture')
r.edit('de pré-structures de Hodge engendrée',r'''de pré-s\unsure{\begin{tikzpicture}[baseline=0pt,x=1em,y=1em]
\node[anchor=base west,inner sep=0pt] at (0,0) {c};
\node[anchor=base west,inner sep=0pt] at (.6,0) {t};
\draw (.2,.95) .. controls (.18,.55) and (.14,.1) .. (.35,-.05);
\draw (.05,.5)--(.48,.45);
\draw (.05,.25) .. controls (.05,-.2) and (.4,-.25) .. (.45,-.1) .. controls (.6,.3) and (.65,.3) .. (.7,.15) .. controls (.78,-.3) and (.9,-.3) .. (1,-.05) .. controls (1.15,.4) and (1.3,.5) .. (1.4,.45);
\end{tikzpicture}}ructures de Hodge engendrée''')
r.edit('On appelle',r'O\rlap{\raisebox{-.6em}{\handwritten{n}}}n appelle')
r.edit('Une '+r'\uline{structure de Hodge}',r'''U\rlap{\tikz[baseline=0pt,x=1em,y=1em]{
\draw (.1,.95) .. controls (.08,.75) and (.12,.65) .. (.27,.65);
\draw (.45,1) .. controls (.45,.8) and (.55,.7) .. (.7,.9);
\draw (.55,.7)--(.62,.6);
}}ne \uline{structure de Hodge}''')
# Three physically raised tensor prefixes and their distinct guides.
guides=[r'\draw (-.3,-.5) .. controls (.4,.2) and (1.7,.05) .. (2,.7);',r'\draw (.4,-.6) .. controls (.35,-.1) and (1.6,.65) .. (1.8,1.3);',r'\draw (-.3,.3) .. controls (.2,0) and (.35,-.3) .. (.5,-.7) .. controls (.5,.1) and (1.5,.7) .. (1.9,1.1);']
old=r'\inserted{$\otimes$-}'
# Replace the three occurrences in sequence by a single asserted whole-text operation.
source=Path('source/SP02_CW_10+12_witnesses/codex/B10-07/pages/B10-07_10_scan107.tex').read_text()
first=r'\inserted{$\unsure{\otimes|\Omega}$-}'
# Subsequent asserted edits use adjoining words to identify each insertion.
for tail,guide in zip(['foncteur naturel','foncteur de Betti','catégorie de pré-'],guides):
 new=r'\inserted{\begin{tikzpicture}[baseline=-.2ex,x=1em,y=1em]'+'\n'+r'\node[anchor=base west] at (0,.4) {$\otimes$-};'+'\n'+guide+'\n'+r'\end{tikzpicture}}'+tail
 r.edit(old+tail,new)
r.edit(r'\inserted{$\underline{C}_o$} \inserted{de type fini} de motifs',r'''\begin{tikzpicture}[baseline=0pt,x=1em,y=1em]
\node[anchor=base west] at (0,.8) {\inserted{$\underline{C}_o$}};
\node[anchor=base west] at (1,0) {de motifs};
\node[anchor=base west] at (6.2,0) {\inserted{de type fini}};
\draw (-.25,.8)--(.7,-.35)--(1.8,1.1);
\draw (1,.3) .. controls (2,.9) and (5.2,.85) .. (5.9,.4) .. controls (6.4,.05) and (5.9,-.45) .. (6.8,-.6) .. controls (8.1,-.85) and (10.3,-.85) .. (11.6,-.6) .. controls (12,-.5) and (12,.2) .. (11.85,.5);
\end{tikzpicture}''')
r.edit('% A curved transposition mark takes “de type fini” from after “de motifs” to the caret before it.','')
r.edit(r'\margin{\handwritten{\uline{$\unsure{\psi|\phi}$}}}',r'''\margin{\handwritten{\unsure{\begin{tikzpicture}[baseline=0pt,x=1em,y=1em,rotate=25]
\draw (0,0) .. controls (.15,.2) and (.35,.5) .. (.45,.8) .. controls (.3,.2) and (.1,-.15) .. (0,0);
\draw (.25,.6)--(.42,.4)--(.8,.9)--(.48,.2)--(.7,.35)--(1.15,.8) .. controls (1,.4) and (.7,0) .. (.95,.05) -- (1.8,.35);
\draw (1.1,.4) .. controls (1.1,.75) and (1.4,.7) .. (1.5,.4) .. controls (1.65,.4) and (1.68,.72) .. (1.8,.5);
\draw (.05,-.3)--(2,-.3);
\end{tikzpicture}|$\psi$|$\phi$}}}''')
r.edit('une sous-$\\otimes$-catégorie',r'une \margin{\tikz[baseline=0pt,x=1em,y=1em]{\draw (0,0)--(.13,.12)--(.2,.3);}}sous-$\otimes$-catégorie')
for place,cr,shows in [('first conjugation bar','i1bar','The thick irregular rule lies over i and its subscript1.'),('two argument lambdas and inner bar','toplambdas','Both lambdas have freehand oblique strokes and the second has a short separate bar.'),('outer conjugation bar','toplambdas','A long irregular rule spans the i1 and barred-lambda group.'),('lambda and membership at right','memberstop','The lambda and open curved membership stroke are freehand beside the typed underlined C.')]:
 ch(place,'handwritten','no hand distinction','handwritten',shows,cr,'other','high',False,True)
ch('trace across right parenthesis in top display','omitted','omitted','short horizontal trace drawn','A short dark horizontal impression crosses the closing parenthesis after barred lambda; it is drawn without assigning it a mathematical meaning.','toplambdas','drawing or diagram','medium',True,True)
ch('rationnelle','rationnelle','rationelle','rationelle','There is one n cell between o and e, followed by two tall l cells.','rationnelle','misread word','high',True,False)
ch('first cohomology exponent',r'\unsure{*|\prime}','*',r'\unsure{*|\prime} retained','The faint elevated mark has a long upper stroke and a short descending trace, but not all asterisk arms separate. The uncertainty is retained despite the clearer later stars.','star1','misread symbol or index','low',False,True,False,True)
for place,cr in [('first rational cohomology','star1'),('third cohomology','Hthird'),('pairing target','Qpair'),('trivial space Q(n)','Qn'),('trivial rational space','Qtrivial'),('field after sur','Qsur'),('base-changed trivial space','QC')]:
 ch(place+' Q alphabet','plain underlined Q','underlined blackboard Q','plain underlined Q','One oval body and tail occur above a separate underline, without a displaced repeated body.',cr,'misread symbol or index','high',False,True,False,True)
ch('Hodge coproduct','handwritten','no hand distinction','handwritten coproduct','The two tall uneven uprights meet a long extended baseline; q,p,X and C around it are typed.','coprod; Hdg','other','high',False,True)
ch('Omega hand and underline','handwritten underlined Omega','no hand distinction','handwritten underlined Omega','The open-bottom curved body has separate outward feet and a detached lower rule.','Omega','other','high',False,True)
ch('third cohomology star','star without hand distinction','star without hand distinction','hand-retraced star','The star has a long dark slanting pen stroke across the lighter short radial impressions.','Hthird','other','medium',True,True)
ch('first tensor-prefix doubt',r'\unsure{\otimes|\Omega}',r'\otimes',r'\otimes','Two crossing interior diagonals are visible inside the typed oval; the enlarged later prefixes and bottom sign show the same crossed body.','tensor1; tensor2; tensor3; tensor4','misread symbol or index','medium',True,False,False,True)
for place,cr,shows in [('first tensor guide','tensor1','A long shallow stroke curves upward at its right end and down left before foncteur.'),('Betti tensor guide','tensor2','A long slanting stroke descends to the position before foncteur de Betti.'),('subcategory tensor guide','tensor3','Two slanting strokes form a deep V before catégorie, surrounding the raised prefix.')]:
 ch(place,'omitted','omitted','guide drawn',shows,cr,'drawing or diagram','high',True,True)
for place,cr in [('Betti tensor prefix status','tensor2'),('subcategory tensor prefix status','tensor3')]:
 ch(place,'inserted','editorially supplied','inserted','The crossed oval and following short hyphen are physically typed above the baseline, beside an insertion guide.',cr,'insertion or placement','high',False,True)
ch('first pré-structures overtyping','pré-structures','pré-structures',r'pré-s\rlap{c}t\rlap{t}r\unsure{\rlap{r}u|u}ctures','The first affected cell contains a c curve and tall t; the next combines t with r. In the u cell the extra right curl is weaker, so a possible r underlay remains qualified.','structure1; structure1close','omission','medium',True,True)
ch('standart accent doubt',r'\unsure{stándart|standart}','standart',r'\unsure{stándart|standart} retained','Two small rising dark traces lie above the first a. Their accent status remains uncertain; the final letter is clearly t.','standart','abbreviation expanded or spelling modernised','medium',False,True)
ch('fully faithful emphasis','underlined','italic','underlined','A long separate continuous rule lies beneath pleinement fidèle.','faithful','other','high',False,True)
ch('extra e cancellation',r'l\deleted{e} homomorphisme','l homomorphisme',r'l\deleted{e} homomorphisme','The e loop with medial stroke survives under an x between l and the apostrophe.','extrae','omission','high',False,True)
ch('OU doubt',r'\unsure{OU|Ou}','Ou',r'O\rlap{\raisebox{.6ex}{U}}u','A full-height capital U is displaced upward over a distinct lower-case u bowl and right serif. Both bodies are preserved without assigning chronological priority.','OU','omission','high',True,True)
for place,cr in [('inserted category index','Cinsert'),('Ob category index','Ob'),('group target index','Gmap'),('functor source index','Cmap')]:
 ch(place,'lower-case o','zero','lower-case o','The lowered body is a small round typewriter o, shorter than a full-height numeral and consistent at all four places.',cr,'misread symbol or index','medium',False,True,False,True)
ch('finite-type phrase placement and mark','phrase moved before de motifs; mark described in comment','phrase after de motifs; no mark','physical de motifs / de type fini with complete curved transposition stroke and insertion caret','The ink phrase de type fini stands after de motifs. Its lower enclosure rises over de motifs and runs to the left caret beneath the raised C_o. The printed positions and connecting stroke are reproduced together.','transpose; transposetip; transposeword','drawing or diagram','high',True,True)
ch('second pré-structures correction','pré-structures','pré-structures','two typed c,t cells with overlying tall t-like and curved correction strokes, followed by ructures; affected cluster qualified','A typed c and following t are individually visible before r. A tall additional stroke crosses the first cell and a heavy two-bend line crosses below and through both; the physical cluster is drawn instead of silently deleting it.','structure2; structure2close','drawing or diagram','medium',True,True)
ch('cancelled celle-ci doubt',r'\deleted{\unsure{celle-ci,}}','omitted',r'\deleted{celle-ci,}','The c curve, e medial bar, two tall l stems, second e, short hyphen, c, dotted i and final comma are distinguishable below the x row.','celleci','omission','medium',True,True)
for place,cr,shows in [('M membership','Ob','The open curved membership stroke and its medial horizontal are handwritten.'),('G arrow','Gmap','A thick irregular shaft with rightward head joins the typed G bodies.'),('category arrow','Cmap','The long uneven shaft and rightward head are handwritten between the typed categories.')]:
 ch(place,'handwritten','no hand distinction','handwritten',shows,cr,'other','high',False,True)
ch('On lower added n','On','On','typed On with an additional handwritten n below n','A second arched two-legged n form is directly below the typed n; its tapered strokes lack the regular typed lower serifs.','On','omission','medium',True,True)
ch('cancelled structure','deleted structure',r'\struck{\ill{}}','deleted structure','The s curve, two tall t strokes, r hooks, u bowls, c and final e remain distinct under x marks.','structurecancel','readable ink left as \\ill{}','high',False,True,True)
ch('polarisation emphasis','underlined','italic','underlined','A single separate horizontal rule extends beneath the complete word.','polar','other','high',False,True)
ch('pairing phi and arrow','handwritten','no hand distinction','handwritten phi and arrow','The phi has a slanted pen stem through an oval, and the arrow has an irregular shaft and head.','pairing','other','high',False,True)
ch('pairing multiplication cross','typed x','times sign','typed x','The crossed diagonals have four typewriter serifs, matching a lower-case x body.','cross','misread symbol or index','high',False,True)
ch('muni du overtyping','du','du',r'd\rlap{e}u','The second cell has the loop and medial stroke of e together with the separate left stem and lower bowl of u.','du','omission','high',True,True)
ch('cancelled la doubt',r'\deleted{\unsure{la}}','omitted',r'\deleted{la}','The first cell preserves a tall hooked l and the next an a bowl with a right stem beneath the x marks.','cancelLA','omission','medium',True,True)
ch('extra closing parenthesis','(n,n),','(n,n)),','(n,n)),','Two distinct rightward curved parenthesis bodies follow the second n before the comma.','bidegre','omission','high',True,False)
ch('C in V_C before hermitian display','plain underlined C','plain underlined C','underlined blackboard C','Two vertically displaced C curves are separately visible: the upper open curve and a second lower open curve with its own right terminal. The underline is separate below both.','VC','misread symbol or index','high',True,True,False,True)
ch('marginal symbol',r'underlined \unsure{\psi|\phi}','omitted','complete qualified pen-form drawing, with psi/phi as alternatives','The left branching retraced form continues into a long rightward stroke and two smaller loops; a separate rising underline runs below it. Rotating clockwise levels the underline, but the letter identity remains unsettled.','margin; marginrot; marginupright','omission','low',True,True)
ch('hermitian psi phi bar and exponent hand','handwritten','no hand distinction','handwritten psi, phi, y bar and -q','The Greek symbols, short y bar and minus-q have irregular pen forms; the x,y,p and parentheses are typed.','psi; phiy; exponent','other','high',False,True)
ch('imaginary factor',r'(\handwritten{i})','(-i)',r'(\handwritten{\unsure{i|-i}})','The long left entry joins the ascending curve of i; a short horizontal at that height could be a separate minus or part of the retracing. No independent minus can be established confidently, so both readings remain.','ifactor','misread symbol or index','medium',True,True,False,True)
ch('corrected bidegree',r'(p,\deleted{\unsure{n}}\handwritten{q}\unsure{-}p)','(p,n-p); editorial note says typed q overwritten by handwritten n',r'(p,\deleted{\unsure{n}}\handwritten{q}\unsure{-}p)','The dark overlying glyph has a closed loop and long descending q stem. A faint typed arch survives beneath it, consistent with n but partly hidden. A short horizontal continues to its right before a separate typed p; its cancellation status stays uncertain.','bidcorr','misread symbol or index','low',False,True,False,True)
ch('traces above n of Une','omitted','omitted','two small upper traces drawn','Two short descending/curving marks lie above the n; their complete character identity is not established, so their shapes are drawn without supplying a word.','Une; Uneclose','drawing or diagram','medium',True,True)
ch('structure de Hodge emphasis','underlined','italic','underlined','A continuous rule runs beneath structure de Hodge.','definition2','other','high',False,True)
ch('left-margin tick','omitted','omitted','short rising trace drawn','A small two-part rising stroke lies to the left of the final sous-tensor-category line.','tick','drawing or diagram','medium',True,True)
ch('folio','comment only','administrative page106','mspage106','The lower-left handwritten figures read106.','folio','insertion or placement','high',True,True)
r.doubt('first H exponent','*',r'\prime','low','Several faint arms do not fully separate.')
r.doubt('first pré-structures third overlapped cell',r'\rlap{r}u','u','low','The extra upper-right curl is only partly distinct.')
r.doubt('conjecture adjective','stándart','standart','medium','The small rising mark may be an accent or an extraneous trace.')
r.doubt('second pré-structures correction','drawn c,t cluster with correction strokes','','medium','The physical typed cells and strokes are preserved; their exact replacement/deletion sequence is not asserted.')
r.doubt('left marginal pen form','drawn form',r'\psi; \phi','low','Branching and retracing remain ambiguous after rotation.')
r.doubt('imaginary factor','i','-i','medium','A short horizontal merges with the entry stroke.')
r.doubt('overwritten bidegree letter','n','','low','The underlying typed arch is partly concealed by the handwritten q.')
r.doubt('horizontal after corrected q','-','correction stroke rather than live minus','low','It joins the correction and cannot securely be classified as live punctuation.')
r.notation('rational Q','ordinary single typed Q with separate underline at seven occurrences','10/107')
r.notation('category/group subscript','lower-case o in inserted C_o, Ob(C_o), G_o and source C_o','10/107')
r.notation('complex C alphabets','plain at other occurrences; visibly self-overstruck C immediately before hermitian display becomes mathbb C','10/107')
r.notation('tensor prefix','crossed oval at four occurrences; first doubt resolved from crossing strokes','10/107')
r.notation('imaginary-unit factor','qualified i / -i, connected left entry stroke','10/107','unresolved')
r.notation('corrected bidegree','typed n partly visible under handwritten q, retained final p and qualified preceding horizontal','10/107','unresolved')
r.notation('OU overlap','capital U vertically displaced above lower-case u; both bodies retained','10/107')
r.r['abbreviations']=[dict(abbreviation='i.e.',expansion='id est',attestations='10/107'),dict(abbreviation='Hdg',expansion='Hodge',attestations='10/107'),dict(abbreviation='Bet',expansion='Betti',attestations='10/107'),dict(abbreviation='Ob',expansion='objets',attestations='10/107')]
r.r['inventory_overrides']={'comparison paragraph':{'first_words_or_objects':'Si à toute variété; rationelle; qualified first exponent; U/u overlap'},'first tensor insertion':{'first_words_or_objects':'resolved tensor hyphen with guide'},'finite type transposition':{'first_words_or_objects':'de motifs de type fini in printed order with transposition curve and caret'},'obscured word':{'first_words_or_objects':'celle-ci, (resolved cancelled reading)'},'polarisation introduction':{'first_words_or_objects':'On appelle with extra lower n'},'la deletion':{'first_words_or_objects':'la (resolved)'},'trivial space explanation':{'first_words_or_objects':'où Q(n) est; d e/u overlap; extra right parenthesis; repeated C in V_C'},'marginal symbol':{'first_words_or_objects':'complete drawn retraced form; psi/phi alternatives'},'marginal handwriting':{'first_words_or_objects':'complete drawn retraced form and underline'},'hermitian form':{'first_words_or_objects':'psi(x,y)=phi(x,bar y)(qualified i / -i)^(p-q)'},'imaginary i':{'first_words_or_objects':'qualified i / -i'}}
extras=[('partrace','top formula','horizontal crossing right parenthesis','drawing','unnamed hand'),('overlap1','first pré-structures','c/t,t/r,qualified r/u overlaps','text','typewriter'),('overlap2','second pré-structures','typed c,t with correction strokes, qualified cluster','drawing','unnamed hand'),('OU','right end of epimorphism line','upper U overlapping lower u','text','typewriter'),('On','polarisation introduction','handwritten n beneath typed n','insertion','unnamed hand'),('du','trivial-space explanation','e/u overlap','text','typewriter'),('Cdouble','before hermitian display','self-overstruck C','text','typewriter'),('Une','final definition','two short traces above n','drawing','unnamed hand'),('tick','left of last subsection line','short rising mark','drawing','unnamed hand'),('folio','lower left','106','margin note','unnamed hand')]
for ident,pos in [('tensor1','before foncteur naturel'),('tensor2','before foncteur de Betti'),('tensor3','before catégorie'),('transpose','around de motifs de type fini')]:extras.append((ident+'guide',pos,'insertion or transposition strokes drawn','drawing','unnamed hand'))
for ident,pos,txt,kind,hand in extras:r.r['inventory_extra'].append(dict(scan='10:107',sheet_kind='typescript',hand=hand,element='107-extra-'+ident,kind=kind,position=pos,first_words_or_objects=txt,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops107.json').read_text())
r.r['inspection_note']='Whole image and both halves viewed before C/H, nine C doubt loci and inventory. All62 crop recipes displayed; the initial +25-degree margin rotation tilted the writing further, so a -25-degree upright view was added and read. Every agreed line, symbol, index, bar, deletion, insertion and mathematical sign checked against ink. Four C doubts resolved (tensor prefix, OU as two overlapping case bodies, celle-ci, la); remaining faint first star, adjective accent, marginal glyph and bidegree details stay qualified. New i/-i and letter-correction uncertainties are explicit. Extra parenthesis and rationelle follow visible ink also retained by H. Seven Q bodies and four o indices separately enlarged; the isolated repeated C follows the typed self-overstrike convention. Physical insertion/transposition guides, correction traces and folio are included. No OCR, parallel transcription, compilation, context access or mathematical correction.'
r.save('work/record107.json')
