from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-08',10,119);ch=r.change
r.edit(r'\scanpage{119}',r'\scanpage{119}'+'\n'+r'\mspage{118}')
r.edit('% archive sheet number: 118','')
r.edit(r'2) $\otimes$-Foncteur',r'2) $\unsure{\otimes|\Omega}$-Foncteur')
r.edit('trucs-catégories',r'trucs-caté\rlap{t}gories')
r.edit(r'\deleted{\unsure{deu|deux}}un',r'\deleted{d}\unsure{\rlap{e}u|u}\rlap{u}n')
r.edit(r'\unsure{bifoncteurs|bifoncteur}',r'\unsure{bifoncteur|bifoncteurs}')
r.edit(r"\unsure{\longrightarrow|\simeq}\unsure{\underline{1}_{C'}|\underline{1}'_C}",r"\unsure{\text{xxx}|\longrightarrow}\underline{1}_{C'}")
r.edit(r'\unsure{avec} et $c$','avec et $c$')
r.edit(r'\unsure{:|(}',r'\unsure{\rlap{(}:|:}')
r.edit(r"compatible avec $c$ et} avec",r"compatible avec $c$ et\handwritten{\begin{tikzpicture}[x=.65cm,y=.65cm,baseline=-.2ex]\draw (0,.28) .. controls (.3,.08) and (.77,.24) .. (.93,.05) .. controls (1.21,-.4) and (1.88,-.18) .. (2.26,.1)--(2.25,.7);\draw[line width=.15pt] (-.2,-.5) .. controls (-.35,-.13) and (-.34,.01) .. (-.12,.17);\end{tikzpicture}}} avec")
r.edit(r"u\inserted{u'}",r"u\inserted{u'\handwritten{\begin{tikzpicture}[x=.4cm,y=.4cm,baseline=-.2ex]\draw (0,-.25)--(0,.21) .. controls (.4,.48) and (.5,.83) .. (.75,.87) .. controls (.98,.9) and (1.08,1.09) .. (1.1,1.35);\end{tikzpicture}}}")
r.edit(r'\deleted{\unsure{qui}}',r'\deleted{qu}')
r.edit(r'avec \inserted{$c$ et}',r'avec \inserted{$c$ et\handwritten{\begin{tikzpicture}[x=.45cm,y=.45cm,baseline=-.2ex]\draw (0,.7) .. controls (.25,.47) and (.72,.67) .. (.99,.35) .. controls (1.08,.16) and (1.14,-.08) .. (1.1,-.23);\draw (1.1,-.23)--(1.55,.88);\end{tikzpicture}}}')
r.edit(r'le\deleted{s} condition',r'l\rlap{e}a\deleted{s} condition')
r.edit(r'\deleted{$c$ et}',r'\deleted{$c$, et}')
r.edit(r'\handwritten{\deleted{\unsure{(A)|(a)} \unsure{pour} \illegible{2}}}',r'''\handwritten{\deleted{\unsure{[a)|(A)} \unsure{pour} \illegible{2}}
\begin{tikzpicture}[x=.65cm,y=.65cm,baseline=-.2ex]
\draw[line width=.2pt] (0,-.25) .. controls (.13,.1) and (.3,.08) .. (.48,.07)--(2.62,.21) .. controls (2.9,.25) and (3.08,.3) .. (3,.48);
\end{tikzpicture}}''')
r.edit(r'\handwritten{\deleted{\unsure{(A)|(a)}}(}',r'\deleted{\unsure{(a)|(A)}}\handwritten{(}')
r.edit(r'\unsure{pas une|par un}','pas une')
r.edit(r'\handwritten{; cf plus bas)}',r'\handwritten{; \makebox[0pt][l]{\raisebox{1.4ex}{\hspace{.1em}\begin{tikzpicture}[x=1em,y=1em]\fill (0,0) circle (.035);\end{tikzpicture}}}cf plus bas)}')
r.edit(r'Remarque\handwritten{s}',r'Rem\unsure{\rlap{\raisebox{1.2ex}{\hspace{.25em}\begin{tikzpicture}[x=1em,y=1em]\draw[line width=1pt] (0,0)--(0,.17);\end{tikzpicture}}}a|a}rque\handwritten{s}')
r.edit(r'\inserted{\handwritten{ce qui précède}}',r'\inserted{\handwritten{ce qui précède\begin{tikzpicture}[x=.55cm,y=.55cm,baseline=-.2ex]\draw (0,-.35) .. controls (-.1,.21) and (.15,.41) .. (.48,.42)--(2.36,.51) .. controls (2.54,.53) and (2.55,.63) .. (2.5,.79);\end{tikzpicture}}}')
r.edit(r"\inserted{associat\deleted{t}if''}",r"\inserted{associat\deleted{t}if''\handwritten{\begin{tikzpicture}[x=.5cm,y=.5cm,baseline=-.2ex]\draw (0,-.3)--(0,.27) .. controls (.55,.36) and (1.56,.29) .. (2.15,.38) .. controls (2.4,.43) and (2.55,.62) .. (2.55,.82);\end{tikzpicture}}}")
r.edit(r'\inserted{\handwritten{$\otimes$ à}}',r'\inserted{\handwritten{$\otimes$ à\begin{tikzpicture}[x=.45cm,y=.45cm,baseline=-.2ex]\draw (0,-.25) .. controls (.28,.14) and (.51,.46) .. (.78,.51) .. controls (1.03,.57) and (1.32,.73) .. (1.4,.93);\end{tikzpicture}}}')
# Every C uncertainty is considered below; pure Greek rendering aliases are excluded from H collation.
ch('heading four category letters','plain C, C prime','underlined C at all four occurrences','plain C, C prime','Each C is an open typewritten curve; no separate lower stroke is visible at any of the four letters.','Cs; title','misread symbol or index','high',False,True,False,True)
ch('first and recurring typed tensor glyph','otimes','otimes',r'first \unsure{\otimes|\Omega}; later otimes','The glyph has a rounded upper arch, crossed inner strokes and projecting lower feet. The five typed instances share this form; the two hand-drawn circled crosses are distinct and clear.','tensor1; cformula; tensor3; a4line; handtensor4; tensor-a','misread symbol or index','medium',True,True,False,True)
ch('heading trucs-catégories','trucs-catégories','trucs-catégories',r'trucs-caté\rlap{t}gories','The g cell has two rounded bowls and a descender, together with a separate tall t stem and horizontal crossbar. Both visible bodies are retained as a physical overlap.','trucs; trucs-over','misread word','high',True,True)
ch('deleted adjective fragment','deleted add','deleted ill','deleted add','The a bowl and two d ascenders remain legible beneath independent typed x marks.','adddel','readable ink left as \\ill{}','high',False,True,True)
ch('deu/un overlapping correction',r'deleted \unsure{deu|deux} then un','deleted un',r'\deleted{d}\unsure{\rlap{e}u|u}\rlap{u}n','Only the d has a separable x cancellation. The next cell combines an e crossbar/counter with u-like stems, and the final cell combines an n arch with a u foot. There is no separate fourth letter or second word position.','deudel; data','deletion state','medium',True,True)
ch('isomorphismes final s','deleted s','live s','deleted s','The final s curves remain under an x with long horizontal feet; the preceding e is uncanceled.','isos','deletion state','high',False,True)
ch('right-edge bifoncteur ending',r'\unsure{bifoncteurs|bifoncteur}','bifoncteurs',r'\unsure{bifoncteur|bifoncteurs}','The word runs into the black right edge at the final r cell. No s body can be seen; singular/plural remains unresolved, with the shorter visible reading first.','bifoncteurclip','misread word','medium',True,True)
ch('canceled et isom.','deleted et isom.','deleted ill','deleted et isom.','The e/t bodies, i dot, s, o, m and final point remain visible under the x cancellation.','etisomdel','readable ink left as \\ill{}','high',False,True,True)
ch('canceled unit display readable text','deleted i:F(underlined1_C) and qualified terminal unit','deleted ill','deleted i:F(underlined1_C) and underlined1_C-prime','The initial i dot, colon, F, parentheses, both unit stems and detached lower bars remain. The last C is below the unit; its raised short stroke is at the upper right of that C.','idel; iunitdel','readable ink left as \\ill{}','medium',True,True,True,True)
ch('canceled unit display relation',r'\unsure{\longrightarrow|\simeq}','deleted ill',r'\unsure{\text{xxx}|\longrightarrow}','Three typed x cancellation cells are all that can be distinguished in the relation slot. They are preserved as the visible marks; the underlying arrow or isomorphism sign cannot be recovered securely.','iarrowdel; idel','misread symbol or index','low',True,True,True,True)
ch('b commutor pair',r'\unsure{\mu|\psi},\mu prime','psi, psi prime',r'\unsure{\mu|\psi},\mu prime retained','Both letters have a short left stem, a low bowl, a tall slanted through-stroke and a right foot. Mu/psi remains uncertain at the first occurrence; the primed repetition uses the first candidate.','mu-pair; b','misread symbol or index','medium',False,True,False,True)
ch('c canceled avec',r'\unsure{avec}','avec','avec','The a counter, v diagonals, e crossbar and c open bowl can be followed beneath the x row. The uncertainty is resolved from those remaining bodies.','cdelete2; cdelete','misread word','medium',True,False)
ch('c canceled et c','et c','ill','et c','An e bowl, tall crossed t and final open c survive below the cancellation.','cdelete2','readable ink left as \\ill{}','high',False,True,True)
ch('Exists isom. insertion attachment','replacement within c','separate paragraph after b','replacement within c','The typed inserted line stands immediately above the canceled opening of c. The lower/right curved guide joins it back to the surviving avec les isomorphismes.','exists-guide; cend','insertion or placement','high',False,True,False,True)
ch('c deleted fonct fragment','deleted fonct','deleted foncto.','deleted fonct','Five letter cells f-o-n-c-t can be distinguished; the following x occupies a space, without a readable o bowl or separate abbreviation point.','fonctdel','misread word')
ch('c mark after i',r'\unsure{:|(}',':',r'\unsure{\rlap{(}:|:}','A curved vertical stroke and two right-facing rounded thickenings occupy the same position. The physical overlap is retained without assigning its order; a colon alone remains an alternative.','icolon','misread symbol or index','medium',True,True,False,True)
ch('u-prime insertion attachment','after original u','after c et on inserted line','after original u','A separate rising curved guide begins directly after the original u and ends beside the upper u-prime. It is distinct from the guide ending the Exists insertion.','uprime; cend','insertion or placement','high',False,True,False,True)
ch('canceled repeated word at right edge',r'\deleted{\unsure{qui}}','omitted','deleted qu','The q bowl and descender and the u stems remain beneath x marks. The scan cuts immediately after u; no i is visible, so it is not supplied.','qui','omission','high',True,True)
ch('three guides in c','omitted','omitted','local curved guides for Exists insertion, u-prime and c et','The long bent lower/right guide, the separate u-prime rising line and the forked c-et guide are independently visible and reproduced beside their respective insertions.','exists-guide; uprime; vcinsert','drawing or diagram','high',True,True)
ch('NB punctuation','NB','N.B.','NB','There are no points between or after the two capital letters.','NB','abbreviation expanded or spelling modernised')
ch('section3 le/la cell and deleted s',r'le\deleted{s}','la',r'l\rlap{e}a\deleted{s}','The vowel cell has both an e crossbar and an a lower bowl/right foot. The next s is crossed by x. The overlap and deletion are retained together.','les','deletion state','high',True,True)
ch('section3a canceled c comma et',r'\deleted{$c$ et}','deleted ill',r'\deleted{$c$, et}','A low comma tail is visible in the canceled space after c, followed by recoverable e and t bodies.','cetdel; a3','readable ink left as \\ill{}','high',True,True,True)
ch('upper canceled handwritten label',r'\unsure{(A)|(a)}','deleted ill',r'\unsure{[a)|(A)}','The opening stroke has a flat upper horizontal and left vertical resembling a square bracket. The central loop/diagonal is crossed and leaves a/A unresolved; the right curved stroke remains.','handcancel-left; handcancel-upright','misread word','low',True,True,True)
ch('upper canceled handwritten pour',r'\unsure{pour}','deleted ill',r'\unsure{pour} retained','A long p descender and low joined curves survive, but the heavy horizontal cancellation obscures the inner letter sequence.','handcancel-word; handcancel-upright','readable ink left as \\ill{}','low',False,True,True)
ch('upper canceled handwritten tail',r'\illegible{2}','deleted ill',r'\illegible{2} retained','Two separated stretches of residual pen strokes follow pour. The strike covers their principal bodies even after enlargement and rotation; the estimated two-word illegibility is retained.','handcancel-word; handcancel-upright','other','low',False,False,True)
ch('upper canceled note lower guide','omitted','omitted','thin lower curve reproduced','A thin curved stroke runs below the canceled note, bends upward at its right end, and descends on the left beside compatibilité. It is separate from the heavy cancellation.','handcancel; handcancel-upright','drawing or diagram','medium',True,True)
ch('section3b numbering','one canceled b)','live b) followed by another canceled b)','one canceled b)','Only one b) is present, crossed by two long pen strokes. No second live enumeration mark occurs.','handcancel; b3all','text not on the page')
ch('section3b canceled label',r'handwritten \unsure{(A)|(a)}','deleted (i)',r'typed \unsure{(a)|(A)}','A rounded bowl with a right stem and baseline foot favors a, but the crossing strokes obscure its upper part. The regular serifed label is aligned with the typed line; the following thin opening parenthesis is handwritten and live.','handcancel-left; handcancel','misread symbol or index','medium',True,True)
ch('section3b live opening parenthesis','live ( before compatibilité','omitted','live ( before compatibilité','The thin curved stroke descends before the c of compatibilité without being crossed by the cancellation of the preceding label.','b3all; handcancel','omission')
ch('explanatory c-prime and hand overlay',r"deleted c prime and \unsure{ce n'|car}","added ça c'est",r"deleted c prime and \unsure{ce n'|car} retained",'The typed curved body and raised stroke are overlaid by darker joined handwritten curves. The middle loop and final stroke remain ambiguous; no separate preceding ça is legible.','cn; b3all','misread word','low',False,True)
ch('canceled first sans doute',r'\deleted{\unsure{sans doute}}','omitted',r'\deleted{\unsure{sans doute}} retained','An older handwritten line lies under a strong horizontal strike above peut-être. A tall d-like loop and t-like stem remain, but the phrase cannot be fully separated from the strike.','sans','omission','low',False,True)
ch('live replacement sans doute pas une',r'sans doute \unsure{pas une|par un}','sans doute pas une as separate margin text','inserted sans doute pas une','The upper line has an open a, a terminal s hook, then three low joined u/n/e turns. It sits directly above the canceled wording and replaces it locally.','sans','insertion or placement','high',True,True)
ch('old close and new semicolon','deleted ) then hand ;','live ),','deleted ) then hand ;','A blue stroke follows/crosses the old curved parenthesis; the following separate point and descending tail form the hand semicolon before cf.','closeold; plusbas','deletion state','medium',False,True)
ch('cf punctuation','cf','cf.','cf','No point follows f. A small detached point lies above the c, at a different horizontal position, and is reproduced separately.','cfplus','abbreviation expanded or spelling modernised')
ch('small point above cf','omitted','omitted','point drawn above c','A detached round black point is visible above the left part of c; it is not moved to the end of the abbreviation.','cfplus','drawing or diagram','medium',True,True)
ch('Remarques underline and final punctuation','underlined Remarques, no period','italic Remarques.','underlined Remarques, no period','A long straight stroke runs beneath the full word, including the handwritten final s. No terminal point follows that s.','remarques','other')
ch('Remarques a overmark','plain a','plain a','a with qualified small vertical overmark drawn','A short nearly vertical thick stroke rises above the a bowl. It does not show a full second letter; the graphic trace is preserved with a plain-a alternative.','remarque-over; remarques','drawing or diagram','medium',True,True)
ch('ce qui précède guide','omitted','omitted','local curved guide reproduced','The long shallow lower line turns up at its right end and descends on the left between dissocier and en.','precede','drawing or diagram','high',True,True)
ch('section4a quotation marks','paired straight quotes','guillemets','paired straight quotes','Two nearly vertical typed strokes open the phrase and two more close the inserted associatif. No angular guillemets occur.','a4line; associatif','other')
ch('section4a canceled second t','associat deleted t if','associatif','associat deleted t if','A second t stem and crossbar remain under an x between the live t and i.','assocdel; associatif','omission')
ch('section4a guide for associatif','omitted','omitted','local long curved guide','The insertion is above the line, with a guide rising from just after the tensor sign and turning up after its closing quotes.','associatif; a4line','drawing or diagram','high',True,True)
ch('section4a category letters','plain C and C prime','underlined C and C prime','plain C and C prime','Both typed C bodies are open curves without a detached underline.','a4line; associatif','misread symbol or index','high',False,True,False,True)
ch('section4b quotation marks','paired straight quotes','guillemets','paired straight quotes','The opening and closing marks each consist of two vertical typed strokes.','b4next; bilateres','other')
ch('section4b canceled plural endings','unités and bilatères with final s deleted','unité and bilatère','unités and bilatères with final s deleted','Each final s remains visible beneath its own oblique pen cancellation.','unites; bilateres','omission')
ch('section4b tensor-à guide','omitted','omitted','local rising curved guide','A slanting line begins before unité and rises under the hand tensor-à insertion, then bends upward to its right.','tensor-a; b4next','drawing or diagram','high',True,True)
ch('marginal NB form','underlined NB','N.B. without underline','underlined NB','A separate short bar lies beneath NB, with no internal points.','NBhand','omission')
ch('marginal comm. abbreviation','comm.','commutatif.','comm.','The final word ends after the two m humps with a distinct point; no t/i/f sequence follows.','NBhand; NB-unit-correct','abbreviation expanded or spelling modernised')
ch('final commutor','mu','psi','mu, first qualified family candidate','The final hand sign repeats the short left upright, low curve, tall crossing stroke and right foot of the pair above.','mufinal; c4','misread symbol or index','medium',False,True,False,True)
ch('last canceled opening parenthesis','deleted (','omitted','deleted (','A tall opening curve remains under a typed x immediately after the period of réflexivité.','parend; lastline','omission')
ch('folio','comment only','administrative page118','mspage118','Three pencil figures at the lower left read118.','folio','insertion or placement','high',True,True)
for args in [
 ('first typed tensor',r'\otimes',r'\Omega','medium','Five typed glyphs have crossed arches and projecting feet; first is qualified, later first candidate used.'),
 ('data sentence overlapped cell',r'\rlap{e}u','u','medium','e crossbar/counter and u-like stems coincide; identification of the lower layer is qualified.'),
 ('right edge bifoncteur','bifoncteur','bifoncteurs','medium','Final r is clipped; no s body visible.'),
 ('canceled unit relation','visible xxx cancellation','right arrow; isomorphism sign','low','No recoverable underlying relation; xxx records the cancellation marks, not a mathematical product.'),
 ('first and recurring commutor',r'\mu',r'\psi','medium','Short left stem, low bowl and tall crossing stroke; later signs use first candidate.'),
 ('inserted i punctuation',r'\rlap{(}:',':','medium','Curved vertical and two rounded thickenings coincide.'),
 ('upper canceled label','[a)','(A)','low','Square-bracket-like beginning; obscured inner label.'),
 ('upper canceled word','pour','','low','p descender and low curves remain under heavy strike.'),
 ('upper canceled tail',r'\illegible{2}','','low','Two estimated word groups remain physically unrecoverable under the strike.'),
 ('lower canceled label','(a)','(A)','medium','Rounded bowl favors a but hatching masks its upper structure.'),
 ('explanatory overlay',"ce n'",'car','low','Joined hand curves overlay typed c-prime; neither alternative is secure.'),
 ('older canceled insertion','sans doute','','low','Principal letter bodies are covered by the horizontal strike.'),
 ('Remarques a','a with vertical overmark drawn','a; possible accent-like trace','medium','The small upright mark is visible; its letter/punctuation origin is not imposed.')]:r.doubt(*args)
r.notation('typed tensor sign','crossed arch with feet; first tensor/Omega qualified, four later first-candidate tokens','10/119','unresolved')
r.notation('hand tensor signs','two hand-drawn circles/cups with crossing diagonals','10/119','read')
r.notation('associator and commutor','phi pair and later phi; first mu/psi, later mu prime and mu','10/119','partly unresolved')
r.notation('physical typed overlaps','t/g in catégories; canceled d plus qualified e/u and u/n cells; e/a in les','10/119','partly unresolved')
r.r['abbreviations']=[dict(abbreviation=a,expansion=b,attestations='10/119') for a,b in [('add','additif / additive'),('isom.','isomorphisme'),('fonct','fonctoriel (canceled fragment)'),('NB','nota bene'),('cf','confer / compare'),('endom.','endomorphismes'),('comm.','commutatif')]]
r.r['inventory_overrides']={
 '001':{'first_words_or_objects':'2) tensor-Foncteur; plain Cs; t/g overlap in trucs-catégories'},
 '003':{'first_words_or_objects':'Les données; canceled d plus overlapping e/u and u/n; canceled final s; clipped bifoncteur ending'},
 '005':{'first_words_or_objects':'canceled d before the overlapping e/u and u/n cells'},
 '010':{'first_words_or_objects':'canceled i:F(underlined1_C), obscured relation recorded as visible xxx, underlined1_C-prime'},
 '011':{'first_words_or_objects':'same canceled unit formula with qualified unrecovered relation'},
 '018':{'first_words_or_objects':'c) canceled opening; Exists insertion; separately guided u-prime; canceled clipped qu'},
 '019':{'first_words_or_objects':'Compatibilité de i avec et c, canceled; avec resolved'},
 '020':{'hand':'typewriter','first_words_or_objects':'Exists isom. replacement; hand punctuation and isomorphism sign; local guide'},
 '022':{'first_words_or_objects':'qualified overlapping curved parenthesis-like stroke and colon'},
 '025':{'first_words_or_objects':'qu, canceled and clipped at right edge'},
 '029':{'first_words_or_objects':'3) Homomorphisme; f:F to G; e/a overlap and deleted s in les'},
 '033':{'first_words_or_objects':'c, et, canceled'},
 '034':{'first_words_or_objects':'canceled handwritten qualified [a)/(A), pour and two unreadable words'},
 '035':{'first_words_or_objects':'same canceled upper handwritten note with thin lower guide'},
 '036':{'first_words_or_objects':'qualified upper label and pour; two unreadable words'},
 '037':{'first_words_or_objects':'canceled b), qualified lower label, live opening parenthesis, uncertain ce n/car, two sans doute layers'},
 '039':{'first_words_or_objects':'live handwritten opening parenthesis before compatibilité'},
 '040':{'hand':'typewriter','first_words_or_objects':'canceled qualified (a)/(A) label'},
 '044':{'first_words_or_objects':'canceled qualified sans doute; live sans doute pas une'},
 '045':{'first_words_or_objects':'same two handwritten insertion layers'},
 '048':{'first_words_or_objects':'semicolon, cf plus bas); isolated point above c'},
 '049':{'hand':'typewriter','first_words_or_objects':'underlined Remarques with qualified small overmark at a; hand4 and final s; unaccented A dissocier'},
 '066':{'hand':'typewriter','first_words_or_objects':'Donnée de commutativité; hand c) and recurring commutor; canceled opening parenthesis after réflexivité'} }
extras=[('overlap-data','data sentence','overlapping e/u and u/n cells after canceled d','text','typewriter'),('guide-exists','after Exists replacement','long curved insertion guide','drawing','his hand'),('guide-u','after original u','rising guide for u-prime','drawing','his hand'),('guide-c','before v,v-prime','forked guide for c et','drawing','his hand'),('guide-cancel','below upper canceled note','thin lower curve beside compatibilité','drawing','his hand'),('point-cf','above c of cf','isolated point','drawing','unnamed hand'),('mark-a','above a of Remarques','qualified short vertical overmark','drawing','unnamed hand'),('guide-precede','after dissocier','curved guide for ce qui précède','drawing','his hand'),('guide-assoc','after typed tensor in4a','guide for associatif','drawing','his hand'),('guide-tensor','before unité in4b','rising guide for tensor-à','drawing','his hand'),('folio','lower left','118','margin note','unnamed hand')]
for ident,pos,txt,kind,hand in extras:r.r['inventory_extra'].append(dict(scan='10:119',sheet_kind='typescript',hand=hand,element='119-extra-'+ident,kind=kind,position=pos,first_words_or_objects=txt,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops119.json').read_text())
r.r['inspection_note']='Root viewed whole image then both halves, then C/H, all15 C uncertainty fields and69 C inventory rows. All81 crop recipes were viewed. The initially truncated adddel/deudel/isos/bifoncteurclip batch was repeated successfully. Slanted handwritten notes were rotated; handcancel-upright additionally levels the canceled note. NB-unit and NB-dash were mis-targeted closeups retained in provenance; corrected larger closeups were added and viewed, confirming the true underline of the marginal unit. All agreed text, formula signs, indices, deletion and insertion states were compared with ink. No OCR, parallel transcription, context, compilation or mathematical check. No page120 image was opened before finalization. The provisional checkpoint119 documentation is superseded by this completed record.'
r.save('work/record119.json')
