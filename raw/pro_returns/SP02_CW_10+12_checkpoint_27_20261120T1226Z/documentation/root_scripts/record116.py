from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B10-08',10,116);ch=r.change
r.edit(r'\scanpage{116}',r'\scanpage{116}'+'\n'+r'\mspage{115}')
r.edit('% archive sheet number: 115','')
r.edit(r'Généralités sur les $\otimes$',r'Généralités sur les $\unsure{\otimes|\Omega}$')
r.edit(r'\unsure{exemples}}\par',r'\unsure{exemples}.}\par')
r.edit(r'\unsure{torseurs}',r'torseurs')
r.edit(r'\unsure{modules}',r'modules')
r.edit(r'\unsure{groupe}',r'\unsure{gr.}')
r.edit(r'\deleted{Les données}',r'\deleted{\unsure{,|I.} Les données}')
r.edit(r'\handwritten{\deleted{$\unsure{X^\vee}$}}',r'\deleted{$X^{\handwritten{\unsure{\vee}}}$}')
r.edit(r'1.5. $X^\vee,\ \unsure{X^{-1}}$',r'1.5. $X^\vee,\ X^{-1}$')
r.edit(r'{; \deleted{\unsure{1.6.}} $X^{-1}$.}',r'{, \deleted{\unsure{1.6.}} $X^{-1}$.}')
r.edit(r'\draw (-3,-.3) -- (-1.8,-.15);',r'\draw[<-] (-4,-.4) .. controls (-3.3,-.5) and (-2.5,-.2) .. (-1.8,-.15);')
r.edit(r'\handwritten{(Toutes les \inserted{compatibilités entre} contraintes sont satisfaites, quand elles ont un sens, dans les exemples du par.0)}',r'''\handwritten{\figure{\begin{tikzpicture}[x=1em,y=1em]
\node[anchor=west] at (0,0) {(Toutes les contraintes sont satisfaites,};
\node[anchor=west] at (1,-1.2) {quand elles ont un sens, dans les};
\node[anchor=west] at (1,-2.4) {exemples du par.0)};
\node[anchor=west] at (5,1.1) {\inserted{compatibilités entre}};
\draw (5,-.45) .. controls (4.9,.1) and (4.9,.45) .. (5.4,.5) -- (15.6,.5) -- (15.4,.75);
\end{tikzpicture}}}''')
r.edit('Associativité et commutativité.',r'Associativité e\unsure{\rlap{r}t|\rlap{n}t} commutativité.')
r.edit('1.2. Commutativité et unité.',r'1.\rlap{1}2. Commutativité et unité.')
r.edit(r'\inserted{\handwritten{(X,Y)}}',r'\inserted{\handwritten{(X,Y)\figure{\begin{tikzpicture}[x=1em,y=1em,baseline]\draw (0,.9) .. controls (.2,.8) and (.5,.55) .. (.5,0) .. controls (.6,-.2) and (.85,-.25) .. (1,-.2);\end{tikzpicture}}}}')
r.edit(r'\inserted{\handwritten{\deleted{(Lois $\otimes$ rigides)}}}',r'''\inserted{\handwritten{\deleted{(Lois $\otimes$ rigides)}}}
\figure{\begin{tikzpicture}[x=1em,y=1em]
\draw (0,.7) .. controls (-.3,-.1) and (.5,-.4) .. (3.5,-.35) .. controls (5.5,-.3) and (6.1,-.1) .. (6.4,.45);
\draw (6.4,.7)--(6.9,-.15)--(7.15,.8);
\end{tikzpicture}}''')
r.edit(r'1.6. \uline{Hom} et unité :',r'1.6. \unsure{\uline{Hom} et unité|\deleted{\uline{Hom} et unité}} :')
r.edit(r'\inserted{\handwritten{\uline{Lois $\otimes$ rigides.}}}',r'''\inserted{\handwritten{\figure{\begin{tikzpicture}[x=1em,y=1em]
\node[anchor=west] at (0,0) {Lois $\otimes$ \uline{rigides.}};
\draw (-.2,-.7) .. controls (.1,-.55) and (.8,-.65) .. (3.2,-.5) -- (3.2,.25);
\draw (5.3,.3) .. controls (6.3,.2) and (8.6,-.2) .. (10.3,-1.2);
\end{tikzpicture}}}}''')
r.edit(r'\handwritten{)}.\handwritten{---}',r'\handwritten{)}.\handwritten{-\, -\, -}')
r.edit(r'Y\handwritten{\simeq}\underline{\mathrm{Hom}}',r'Y\handwritten{\unsure{\simeq|\xleftarrow{\sim}}}\underline{\mathrm{Hom}}')
r.edit(r'$).\handwritten{; rang',r'$)\handwritten{; rang')
r.edit('Formes normales',r'Formes norm\rlap{a}les')
r.edit(r'\unsure{après le|pour le}',r'après le')
r.edit(r'\unsure{§}',r'§')
r.edit(r"Compatibilité d'un",r"Compatibilité \rlap{d}\handwritten{d}\rlap{v}\handwritten{'}\rlap{u}\handwritten{u}\rlap{n}\handwritten{n}")
r.edit(r'\unsure{agrandissement} de \unsure{catégories}',r'\unsure{agrandissement} \unsure{de} \unsure{catégories}')
r.edit(r'\unsure{4|5}',r'\deleted{4}\handwritten{5}')
r.edit(r'\uline{Exemples typiques:}\deleted{\illegible{1}}',r'\uline{Exemples typiques;}\deleted{\unsure{les}}')
r.edit(r'5.0. $\otimes$-Catégories: (catégories',r'5.0. $\otimes$-Catégories; catégories')
r.edit(r'\unsure{Gros} méc.',r'(pas néc.')
r.edit('première manière',r'première ma\rlap{j}nière')
r.edit(r'\deleted{\unsure{notions}}',r'\deleted{\unsure{noti}}')
ch('chapter title emphasis and punctuation',r'\uline{Chapitre} 1','Chapitre 1.',r'\uline{Chapitre} 1','Only Chapitre carries a straight underline; the space following 1 has no period.','title','other')
ch('title first typed tensor sign','otimes','otimes',r'\unsure{\otimes|\Omega}','Crossed interior, rounded upper arch and broad feet leave the outer contour ambiguous. The nine later typed occurrences were also enlarged and use the first candidate under the per-page convention.','tensor-title; tensor0; tensor1; traceformula; tensor4; tensor41; tensor41b; tensor42; tensor5; tensor54','misread symbol or index','medium',True,True,False,True)
ch('upper-right canceled heading',r'\unsure{catégories} \illegible{1} \unsure{exemples}','struck ill; following dash',r'\deleted{\unsure{catégories} \illegible{1} \unsure{exemples}.}','Diagonal cancellation leaves fragments of the first and last words but obscures the middle. A separate small terminal point remains; the apparent long line belongs to the cancellation, not a following textual dash.','margindel; marginall','readable ink left as \\ill{}','low',True,True,True)
ch('upper-right list numbering and separators','circled1–5; line breaks','1)–5); added semicolons','circled1–5; line breaks','Closed loops surround each numeral. The notes occupy separate lines without H semicolon separators.','marginall; margin1; margin2; margin3; margin4; margin5','drawing or diagram')
ch('margin item2 cart.','cart.','uncertain cart.','cart.','The c, a, r, tall t and terminal point are individually visible.','margin2','misread word','high',False,True,True)
ch('margin item3',r'\unsure{torseurs} sous faisceau abélien','Torseurs sous un faisceau abélien','torseurs sous faisceau abélien','The small initial t and following joined orseurs can be followed. There is only a gap between sous and faisceau, without letters un.','margin3','misread word','high',True,True)
ch('margin item4 modules',r'\unsure{modules}','modules ill','modules','The sequence m-o-d-u-l-e-s is visible, with the tall d loop continuing beneath the line. No independent omitted word follows before indexés.','margin4','misread word','medium',True,True,True)
ch('margin item4 indexés',r'\unsure{indexés}','indexées',r'\unsure{indexés} retained','Joined central strokes and overlap from the line above do not settle every letter; no separate second e is established before the final s-like curve.','margin4','misread word','low',False,True)
ch('margin item4 clipped last word',r'\unsure{groupe}','ill',r'\unsure{gr.}','The surviving first form has a descending g-like stroke followed by a short r-like turn. The right edge interrupts the remainder; a complete groupe cannot be recovered.','groupe-edge; margin4','readable ink left as \\ill{}','low',True,True,True)
ch('margin item5 wording','espace des lacets d’un espace','espace des uncertain lacets d’un ill','espace des lacets d’un espace','Both e-s-p-a-c-e sequences and l-a-c-e-t-s are visible; the t is tall and the terminal s turns below the baseline.','margin5','readable ink left as \\ill{}','high',False,True,True)
ch('margin item5 box',r'\fbox{topologique}','added topologique',r'\fbox{topologique}','Four enclosing sides surround the word; the lower-right side curves up into the right side.','margin5','drawing or diagram')
for label,crop in [('Par.0','par0'),('Par.1','par1'),('Par.2','par2'),('Par.3','formes'),('Par.4','par4'),('Par.5','par5')]:
 ch(label+' underline','underlined Par','plain Par','underlined Par','A distinct horizontal line lies beneath Par, ending before the number.',''+crop,'omission')
ch('Par.0 terminal points','four points','ellipsis','four points','Four separate typed points follow divers.','par0','misread symbol or index')
ch('Par.1 canceled prefix','Les données','I. Les données',r'\deleted{\unsure{,|I.} Les données}','Two crossed cells precede Les. The first preserves a comma-like descending tail; an independent capital I and period are not secure beneath the x strokes.','Les','deletion state','low',True,True)
ch('upper1.4 punctuation','hand semicolon','comma','hand semicolon','A short high point and lower curved stroke form a semicolon after the Moh expression.','upper14','misread symbol or index')
ch('upper1.4 canceled dual',r'handwritten unsure X^vee','struck ill',r'\deleted{$X^{\handwritten{\unsure{\vee}}}$}','The lower X has typed serifs and two crossed diagonals. The small raised strokes remain obscured by cancellation, so the candidate vee is qualified.','dualdelete; upper14','readable ink left as \\ill{}','low',True,True,True,True)
ch('upper1.5 faint inverse',r'\unsure{X^{-1}}','struck checkX^-1',r'X^{-1}','The faint X and raised minus-one remain visible inside the overlap of the two ovals; no separate vee or independent cancellation through this expression is established.','faintinverse; ovals','deletion state','medium',True,True,False,True)
ch('upper1.5 canceled old number',r'\deleted{\unsure{1.6.}}','omitted',r'\deleted{\unsure{1.6.}} retained','A compact crossed-out group precedes the second inverse. The low point and parts of the vertical/curved numerals survive, but dense blue hatching prevents resolving the full number.','numberdelete; ovals','omission','low',False,True)
ch('upper1.5 separator','semicolon','no separator at old number','comma','A single thick hook lies at baseline before the canceled number, without an independent upper point.','ovals','misread symbol or index','high',True,True)
ch('upper addition ovals and connector','two ovals; short line','omitted','two ovals and long leftward connector with head','Two incomplete overlapping loops enclose the additions. The line running toward upper1.4 extends beyond the first oval and ends with a pointed left termination.','ovals; upper14','drawing or diagram','high',True,True)
ch('Par.2 handwritten note punctuation and placement','parentheses; inserted compatibilités entre','margin without parentheses or insertion','parentheses; inserted phrase above contraintes','The large opening and closing curves enclose the three-line note. compatibilités entre is written separately above contraintes.','constraintnote','insertion or placement')
ch('Par.2 insertion guide','omitted','omitted','curved left guide and long upper line with turned-up right end','The thin pencil line rises at the left of contraintes, runs under the inserted words and ends in a short upturned stroke at the right.','constraintnote','drawing or diagram','high',True,True)
ch('second1.1 et overlap','et','et',r'e\unsure{\rlap{r}t|\rlap{n}t}','An extra left stem/top and curved right shoulder share the t cell. The additional form resembles r, with n also possible; the separate t stem and foot are visible.','etover','misread symbol or index','low',True,True)
ch('second1.2 numeral overlap','1.2.','1.2.',r'1.\rlap{1}2.','A vertical1 stem and foot lie inside the curved upper body and sloping stroke of2.','number12','misread symbol or index','high',True,True)
ch('second1.5 raised arguments','inserted (X,Y)','baseline (X,Y)','raised inserted (X,Y)','The arguments are above the typed baseline, between Hom and the handwritten equivalence sign.','isom; second15','insertion or placement')
ch('second1.5 curved guide','omitted','omitted','curved insertion guide drawn','A descending pencil curve at the right of the raised arguments bends toward the following relation sign.','isom','drawing or diagram','high',True,True)
ch('second1.5 ending','period and three dashes','ellipsis','period and three dashes','A low typed point is followed by three detached short horizontal strokes.','second15','misread symbol or index')
ch('deleted Lois rigides above second1.6','deleted parenthetical phrase','live marginal Lois tensor rigides','deleted parenthetical phrase','Blue oblique strokes traverse the parenthesized words, including the circled-cross operation and rigides.','loisdeleted','deletion state','high',False,True,False,True)
ch('second1.6 Hom et unité state','live phrase','struck phrase',r'\unsure{\uline{Hom} et unité|\deleted{\uline{Hom} et unité}}','A thin pencil curve crosses the upper part of the typed words and is continuous with the outline beneath the canceled annotation. Whether it also cancels the typed phrase is not settled by the strokes.','loisdeleted; second16','deletion state','low',True,True,False,True)
ch('second1.6 outline and angle','omitted','omitted','curved pencil outline and right angular pen mark','The pencil outline below the canceled phrase turns up at the right, where a darker two-segment angular stroke stands. Their shapes are retained without assigning an editorial intention.','loisdeleted; second16','drawing or diagram','medium',True,True)
ch('non annotation position and drawing','underlined non! and pointer beside1.6','non! after1.5','underlined non! and pointer beside1.6','The underline and descending curved pointer stand directly over the question at the end of1.6, not at the preceding item.','non; second16','insertion or placement','high',False,True,False,True)
ch('live Lois rigides heading','whole phrase underlined; inserted above1.7','omitted here',r'Lois $\otimes$ \uline{rigides.} above1.7','The live words sit above Formalisme. A short independent line underlines rigides; the longer line below Lois bends and continues as a guide.','loisguide; second17','insertion or placement','high',True,True,False,True)
ch('second1.7 guides','opening curve only','omitted','opening curve plus bent guide and long arc','The left opening curve precedes Formalisme. A separate line beneath Lois turns up after the operation; a broad arc runs from the right of the inserted heading toward the cas parenthesis.','loisguide; second17','drawing or diagram','high',True,True)
ch('second1.7 canceled word after cas','deleted illegible1','omitted','deleted illegible1 retained','A short group between cas and d’isomorphie is covered by repeated x-like strokes; no complete word is recoverable.','casdel','omission','low',False,True)
ch('second1.7 relation sign','simeq','simeq',r'\unsure{\simeq|\xleftarrow{\sim}}','The strong wave and lower bar are clear. A faint diagonal under the left end of the bar may be a left arrowhead, but its upper branch is not independently visible.','traceiso; traceformula','misread symbol or index','low',True,True,False,True)
ch('second1.7 final punctuation','period then handwritten semicolon','comma','single semicolon','The typed upper point and added lower comma-like curve together form one semicolon after the closing parenthesis.','rank; second17','misread symbol or index','high',True,True)
ch('Par.3 canceled old number',r'\deleted{1.8.}','omitted',r'\deleted{1.8.}','The1, point, two loops of8 and final point survive under blue diagonal strokes beside the new handwritten Par.3.','old18','omission')
ch('Formes normales overprint','normales','normales',r'norm\rlap{a}les','The a bowl and right side share the same cell as the full-height l stem and its long baseline foot. There is no separate l cell before e.','normales-over; formes','misread symbol or index','high',True,True)
ch('canceled annotation opening',r'\unsure{après le|pour le} \unsure{§}','struck ill','après le §','The opening a and descending p, joined r/è/s and le can be followed beneath the diagonal strokes; the section sign has two opposed loops.','afterformes','readable ink left as \\ill{}','medium',True,True,True)
ch('canceled annotation final word',r'\uuline{\unsure{suivant}}','struck ill',r'\uuline{\unsure{suivant}} retained','The ending is still heavily traversed by cancellation. Two distinct horizontal lines remain underneath; the full word is not resolved.','afterformes','readable ink left as \\ill{}','low',False,True,True)
for label,crop in [('Par.4','number4'),('4.1','number41'),('4.2','number42'),('4.3','number43'),('4.4','number44')]:
 ch(label+' old number','deleted3 plus hand4','4 only','deleted3 plus hand4','The rounded typed3 remains under the angled handwritten4, which crosses its former body.',''+crop,'deletion state')
ch('4.2 d’un','plain d’un','struck d’un',r"\rlap{d}\handwritten{d}\rlap{v}\handwritten{'}\rlap{u}\handwritten{u}\rlap{n}\handwritten{n}",'Pen follows the typed d, u and n bodies. A typed v with two angled arms lies below the raised apostrophe. The strokes retrace letters; they do not form an independent horizontal cancellation.','dun','deletion state','medium',True,True)
ch('4.2 final mark','handwritten exclamation','period','handwritten exclamation','A long descending pen stroke ends in a small rounded lower blob; it is separate from the typed word ending.','bang','misread symbol or index')
ch('4.4 final mark','short dash','period','short dash','A single short horizontal pen stroke follows the inverse expression.','dualinv44','misread symbol or index')
ch('4.5 canceled phrase',r'unsure agrandissement; de; unsure catégories','struck ill',r'\unsure{agrandissement} \unsure{de} \unsure{catégories}','Fragments of the long first word and capital/looped start of the last remain under the broad line. The intervening de is also obscured and should not stand unqualified.','del45; de45','readable ink left as \\ill{}','low',True,True,True)
ch('4.5 calcul insertion','inserted calcul','inline calcul','calcul inserted above cancellation','calcul is written on a higher baseline directly over the canceled phrase, before the following des fractions.','calcul; row45','insertion or placement')
ch('4.5 terminal points','four points','ellipsis','four points','Four separately placed pen points follow fractions.','row45','misread symbol or index')
ch('Par.5 overwritten number',r'\unsure{4|5}','5',r'\deleted{4}\handwritten{5}','A typed angular4 remains beneath the added5, whose upper bar and rounded lower turn are separately visible.','number5','deletion state','high',True,True)
ch('Exemples typiques punctuation','colon','semicolon','semicolon','The lower point has a descending comma-like extension; it is not a second round colon point.','par5','misread symbol or index','high',True,False)
ch('Exemples heading underlines','underlined heading parts','underlines omitted','underlined heading parts','Separate long strokes run beneath Exemples typiques, catégories and the added définies par des bigèbres.','par5; definition5','omission')
ch('Exemples canceled word','deleted illegible1','deleted les',r'\deleted{\unsure{les}}','A tall left loop and short joined e/s-like remnants survive under the cancellation, sufficient for a qualified les but not an unqualified reading.','les5','readable ink left as \\ill{}','medium',True,True)
ch('5.0 punctuation after Catégories','colon','colon','semicolon','The lower dark mark narrows into a descending oblique tail beneath the upper point.','semicolon50; row50','misread symbol or index','high',True,True)
ch('5.0 parentheses','opening before catégories','opening before pas','opening before pas','There is no curved mark between the semicolon and catégories; a clear opening curve precedes pas near the end of the line.','row50; tail50','insertion or placement','high',True,False)
ch('5.0 canceled word',r'\unsure{avec}','struck ill',r'\unsure{avec} retained','Upper letter fragments survive under blue diagonal hatching, but the centers remain covered. The C candidate cannot be made certain.','tail50','readable ink left as \\ill{}','low',False,True,True)
ch('5.0 pas',r'\unsure{Gros}','pas','pas','After the opening curve comes a p with a long descender, followed by low a and s; there is no capital G body or r.','tail50','misread word','high',True,False,False,True)
ch('5.0 néc.','méc.','néc.','néc.','The initial has one arch, then an accented e and open c; a detached terminal point follows.','tail50','misread word','high',True,False,False,True)
ch('5.0 last underlined word',r'\unsure{Huy|Hom}','Hom',r'\unsure{\mathrm{Huy}|\mathrm{Hom}} retained','The H is followed by an open u-like joined curve and a final descending y/m-like stroke meeting the underline. The interior cannot distinguish the candidate letter groups securely.','tail50','misread word','low',False,True,False,True)
for label,crop in [('5.1','num51'),('5.2','num52'),('5.3','num53'),('5.4','num54')]:
 ch(label+' old number','deleted4 plus hand5','5 only','deleted4 plus hand5','The typed4 body survives below the broad upper and curved lower strokes of the added5.',''+crop,'deletion state')
ch('5.3 manière overlap','manière','manière',r'ma\rlap{j}nière','The n arch and two stems are present; an extra descending curved j tail runs below the right stem. The ordinary i remains in the next cell.','maniere; row53','misread symbol or index','high',True,True)
ch('5.4 clipped canceled word',r'\unsure{notions}','struck ill',r'\deleted{\unsure{noti}}','Only n/o/t/i-like portions can be followed beneath the x strokes before the black scan edge. The following ons is not visible and is not restored from the repeated next-line word.','notions-edge; notionsdel','readable ink left as \\ill{}','low',True,True,True)
ch('folio','comment only','administrative page115','mspage115','Three lower-left pencil numerals read115.','folio','insertion or placement','high',True,True)
for line,reading,alt,conf,comment in [
 ('first typed tensor',r'\otimes',r'\Omega','medium','Crossed arch with feet; the graphic family is the same at later typed occurrences.'),
 ('upper-right canceled heading','catégories [illegible1] exemples','','low','Dense cancellation obscures the middle and parts of both words.'),
 ('margin item4','indexés','','low','Joined strokes overlap adjacent writing.'),
 ('margin item4 clipped end','gr.','','low','Only the g-like descent and short following turn survive at the edge; the terminal point is tentative.'),
 ('Par.1 canceled prefix',',','I.','low','Descending tail under the cancellation; full I plus point not settled.'),
 ('upper1.4 exponent',r'\vee','','low','Typed X is clear; small raised strokes are canceled.'),
 ('upper oval old number','1.6.','','low','Dense pen hatching over the numerals.'),
 ('second1.1 et cell',r'\rlap{r}t',r'\rlap{n}t','low','Extra stem and shoulder are clear but the overwritten letter is not.'),
 ('second1.6 Hom et unité','live','deleted','low','Crossing pencil curve may belong to annotation outline or cancellation.'),
 ('second1.7 after cas','[illegible1]','','low','Fully covered canceled word.'),
 ('second1.7 relation',r'\simeq',r'\xleftarrow{\sim}','low','Faint diagonal under left endpoint may be an arrowhead.'),
 ('after Formes normales','suivant','','low','Double underline clear, letters traversed by cancellation.'),
 ('4.5 canceled phrase','agrandissement de catégories','','low','All three word readings remain tentative under broad cancellation.'),
 ('after Exemples typiques','les','','medium','Surviving left loop and joined short remnants support a qualified reading.'),
 ('5.0 canceled word','avec','','low','Only upper fragments survive hatching.'),
 ('5.0 final word','Huy','Hom','low','Joined strokes and underline obscure letter distinctions.'),
 ('5.4 clipped prefix','noti','','low','Visible prefix only; the right edge prevents reading the rest.')]:r.doubt(line,reading,alt,conf,comment)
r.notation('typed tensor prefix','crossed arch with feet; first occurrence tensor/Omega, later first candidate','10/116','unresolved')
r.notation('typed overlaps','a/l in normales; j/n in manière;1/2 numeral; uncertain r/t or n/t','10/116')
r.notation('dual and inverse','typed X with handwritten raised vee; handwritten X^-1; faint possible left arrow under relation wave','10/116','partly unresolved')
r.r['abbreviations']=[dict(abbreviation=a,expansion=b,attestations='10/116') for a,b in [('Par. / par.','paragraphe'),('tens.','tensoriel'),('cart.','cartésiens'),('gr.','groupe (clipped and tentative)'),('ass.','associatif / associativité'),('comm.','commutatif / commutativité'),('unit.','unitaire / unité'),('néc.','nécessairement'),('co','comodule-related prefix')]]
r.r['inventory_overrides']={'006':{'first_words_or_objects':'familles de modules; indexés qualified; gr. clipped and qualified'},'011':{'first_words_or_objects':'qualified comma/I. prefix and Les données'},'016':{'hand':'typewriter','first_words_or_objects':'typed X with uncertain handwritten raised vee, canceled'},'019':{'first_words_or_objects':'overlapping ovals and long leftward pointed connector'},'025':{'first_words_or_objects':'Associativité e(r/t or n/t overlap) commutativité'},'026':{'first_words_or_objects':'Commutativité et unité;1/2 numeral overlap'},'035':{'first_words_or_objects':'Hom et unité; deletion state qualified'},'039':{'first_words_or_objects':'Lois tensor rigides.; underline under rigides'},'044':{'first_words_or_objects':'simeq or faint left arrow under wave, qualified'},'048':{'first_words_or_objects':'Formes norm(a/l overlap)es de multifoncteurs composés'},'068':{'first_words_or_objects':'agrandissement de catégories; all three words qualified'},'070':{'first_words_or_objects':'Par. old4/new5; Exemples typiques; tensor-catégories'},'071':{'first_words_or_objects':'les (qualified)'},'074':{'position':'5.0 before (pas','first_words_or_objects':'avec (uncertain)'},'081':{'first_words_or_objects':'Dualité première ma(j/n overlap)ière'},'087':{'first_words_or_objects':'noti (qualified visible prefix, rest clipped)'}}
extras=[('folio','lower left','115','margin note','unnamed hand'),('note-guide','above contraintes in Par.2 note','curved insertion guide and upturned right end','drawing','his hand'),('argument-guide','second1.5','curved guide from raised arguments','drawing','his hand'),('outline16','above and across second1.6','curved pencil outline and angular right mark','drawing','his hand'),('guides17','above second1.7','bent lower guide and long right arc','drawing','his hand'),('dun','4.2','pen retracing d/un; typed v under apostrophe','text','his hand'),('heading-old4','Par.5 heading','overwritten typed4','deletion','typewriter'),('heading-new5','Par.5 heading','added5','insertion','his hand')]
for ident,pos,txt,kind,hand in extras:r.r['inventory_extra'].append(dict(scan='10:116',sheet_kind='typescript',hand=hand,element='116-extra-'+ident,kind=kind,position=pos,first_words_or_objects=txt,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops116.json').read_text())
r.r['inspection_note']='Whole, both halves, C/H,22 C macro doubt/illegible loci and88 C inventory rows read in order. All94 crop recipes viewed: the last-five initial truncated output was repeated; two additional closeups initially landed on neighbouring words and were corrected by normales-over/semicolon50 recipes. Upper margin and slanted annotations were rotated upright. Every agreed line and mathematical sign was read; additional a/l and j/n typed overlaps were found in agreed text. All C doubts were decided or explicitly retained, and the clipped ending was restricted to visible ink. Typed tensor ambiguity is marked once on this page. The deletion state of Hom et unité and faint possible arrowhead are qualified, without using mathematical expectations. No OCR, parallel transcription, context, compilation or mathematical check.'
r.save('work/record116.json')
