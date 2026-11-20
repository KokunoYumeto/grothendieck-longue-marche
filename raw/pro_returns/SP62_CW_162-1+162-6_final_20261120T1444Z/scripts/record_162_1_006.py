from records import *
p=page('162-1',6)
tex=r'''\scanpage{6}
Deligne 2 \deleted{(suite)}\qquad \deleted{Compliments Woodshole}

\deleted{\unsure{(Mumford + Matsusaka)|Mumford + Matsusaka)}\quad \unsure{Am. J. Math.|Amer. J. Math.} 1964}

\deleted{Mumford : Abelian quotients of Teichmüller group}

Mumford : Some aspects of the Pb of Moduli (mimeo.)

\deleted{Lang Néron}

\noindent Matsusaka $\left|\begin{array}{l}\text{\unsure{chow|char.} of Jac. variety}\\ \text{A correction to \ldots}\\ \text{The criteri. for alg \unsure{equivalens|equivalence} \unsure{.\,--|\ldots}}\end{array}\right.$

\deleted{Néron : \unsure{Quasi-fonctions|Quasi fonctions} et hauteurs sur les V.A.}

\deleted{Kleiman : notes pour SGA 6}

\deleted{Grothendieck : lettre à Hartshorne du 25.9.67 (sur son papier de dim. coh. des Var alg).}

\(\left.\begin{array}{l}\text{\deleted{Weil}}\\\text{Andreotti}\end{array}\right\vert\ \text{sur Torelli}\)

\deleted{Rédaction \unsure{Mumf|Mumf.} lemme de Abhyankar}

\deleted{Artin\qquad Kiehl, sur th. de Frisch, Inventiones Mathematicae}

\deleted{Samuel\qquad Papiers de Ramanan}

\dashuline{Berthelot} \deleted{(2)} 1 ///\quad Gabriel : \uline{groupes formels}

\deleted{Cartier : notes CR gr. form.}

notes sur stratifications

\deleted{notes sur groupe de BT et Cristaux}

\deleted{Artin\qquad Kiehl Ausgezeichnete Ringe.}

\deleted{Saavedra\qquad Atiyah, \uline{Finiteness} Theorems for compact}

\deleted{Lie groups}

\deleted{\unsure{Dolotheo|Dolontho|Dolotho}\qquad SGA 6 $\underline{\mathrm{X}}$ (\unsure{Manin|Mumford} \unsure{formel})}

\deleted{B. Mazur\qquad Correspondance avec Griffiths}

\deleted{Notes Kleiman, conj. \unsure{standart|standard}}

\deleted{\uline{Deligne} (suite))\qquad Notes \unsure{Jussila|Jussita}}

\deleted{Lettre : \unsure{Oort|Obstruction|O. Zariski} - \unsure{Piatetzki|Piatezki}-Schapiro}

\deleted{Notes CR \deleted{\unsure{Gabriel}} Cartier, groupes formels.}

\deleted{Notes \unsure{Catégories|Catégorie} \unsure{cofibrées|triangulées} \illegible{1}}

\deleted{\uline{Murre}\qquad Conjecture sur \unsure{Rosenlicht} uniforme}

\deleted{SGA 7 $\overline{\underline{\mathrm{I}}}$ \unsure{à|:} $\overline{\underline{\mathrm{V}}}$}

\deleted{Rim\qquad Thèse Gabriel}

Quillen\qquad \deleted{lettres à Verdier :}

Notes Verdier limite projective

Notes Karoubi sur définition de $K$.

% archive sheet number: 5
\clearpage
'''
def c(place,C,H,F,S,K='misread word',conf='high',a='CH',m='no'):change(p,place,C,H,F,S,K,conf,a,m)
c('Deligne / cancelled qualification',r'\deleted{(\unsure{suite|suite 2})}','editorial description of an illegible struck word',r'\deleted{(suite)}','Half a: parentheses and the opening s/t strokes survive the blue cancellation; no second 2 is distinguishable.','readable ink left as \\ill{}','medium','H','yes')
c('first title',r'\unsure{Compliments|Compléments} \unsure{Woodshole|Woods hole}',r'Compléments \uncertain{Kodaira}','Compliments Woodshole','Crop 162-1/006 (515,40,1105,118): an i dot follows pl; no acute e. The next word has W, oo, ds, h and ole; Kodaira does not match its initial or length.','misread word','high','H','yes')
c('first journal line / second name','(Mumford + Matsusaka), Am. J. Math. 1964','Mumford, Amer. J. Math. 1964',r'\unsure{(Mumford + Matsusaka)|Mumford + Matsusaka)}; \unsure{Am. J. Math.|Amer. J. Math.} 1964','Crop 162-1/006 (475,108,1360,180): plus sign, second capital M and Matsusaka are present. Outer initial parenthesis and middle journal abbreviation remain crossed.','omission','high','H')
c('live Mumford title / abbreviation','Pb','Pb.','Pb','Half a: no point after b before of.','other','high','H')
c('live Mumford title / mimeo','mimeo.','miméo.','mimeo.','Half a: letters visible without an acute over e.','abbreviation expanded or spelling modernised','high','H')
c('Matsusaka / first title',r'\unsure{char.|char}',r'Chow',r'\unsure{chow|char.}','Crop 162-1/006 (725,295,1515,431): small c, high h, oval and a short angled ending favor chow, but char. cannot be excluded. No capital C is written.','misread word','medium','CH')
c('Matsusaka / third title',r'The \unsure{criteri.|criterion} for alg \unsure{equivalens|equivalence} \unsure{..---|...}',r'The criteria for alg. equivalence \ill',r'The criteri. for alg \unsure{equivalens|equivalence} \unsure{.\,--|\ldots}','Same crop (725,295,1515,431): the abbreviated criteri. ends in a point; alg has no separate point; the last word has compressed terminal strokes; a dot and a short horizontal follow it.','abbreviation expanded or spelling modernised','medium','CH','yes')
c('Néron / initial compound',r'\unsure{Quasi-fonctions|Quasi fonctions}',r'\ill fonctions',r'\unsure{Quasi-fonctions|Quasi fonctions}','Half a: large Q and uasi visible before fonctions; cancellation prevents deciding whether a hyphen was present.','readable ink left as \\ill{}','medium','H','yes')
c('Grothendieck / date','25.9.67','21.9.67','25.9.67','Crop 162-1/006 (970,527,1660,642): second digit has angular upper bend and lower turn of 5; the date is followed by 9.67.','misread symbol or index','high','H')
c('Grothendieck / parenthesis',r'sur son papier de dim. coh. \unsure{des|de} Var \unsure{alg|alg.}',r'sur ses papiers de dim. cohomologique des variétés algébriques','sur son papier de dim. coh. des Var alg','Same date crop (970,527,1660,642): son, singular papier and short written forms dim., coh., Var, alg; no added punctuation before closing parenthesis.','abbreviation expanded or spelling modernised','high','H')
c('Rédaction / Abhyankar',r'Rédaction \unsure{Mumf|Mumf.|Mme} lemme de Abhyankar',r'Rédaction thèse \ill de Abhyankar',r'Rédaction \unsure{Mumf|Mumf.} lemme de Abhyankar','Crop 162-1/006 (575,685,1515,756): M and repeated humps precede clear lemme; no thèse is present. Final f/point remains partly obscured.','misread word','medium','H','yes')
c('Samuel entry / cancellation','struck','live','Samuel; Papiers de Ramanan (struck)','Half a: pencil zigzag crosses recipient and paper entry; independent dark rules also cross the words.','deletion state (struck given live or live given struck)','high','H')
c('Berthelot / reminder marks','dashed underline; struck (2); 1 ///','(2) inserted; 1','dashed underline; struck (2); 1 ///','Half a: hatching through parenthesized 2, uncancelled 1, three oblique reminder strokes, and short separate dashes under the name.','deletion state (struck given live or live given struck)','high','H')
c('Cartier entry / text and cancellation',r'\deleted{Cartier : \unsure{Note|notes} CR gr. form.}',r'Cartier : notes \ill groupes formels (live)',r'\deleted{Cartier : notes CR gr. form.}','Crop 162-1/006 (515,949,1160,1020): lower-case notes, capitals CR, abbreviated gr. form.; cancellation crosses the full line.','abbreviation expanded or spelling modernised','high','H','yes')
c('BT entry','notes sur groupe de BT et Cristaux','notes sur groupes de Barsotti–Tate et cristaux','notes sur groupe de BT et Cristaux','Half a: singular groupe, two capitals BT, capital C in Cristaux.','abbreviation expanded or spelling modernised','high','H','yes')
c('second Artin / Kiehl placement','Artin; Kiehl Ausgezeichnete Ringe.','Kiehl ill under Berthelot; Artin attached to Atiyah','Artin; Kiehl Ausgezeichnete Ringe. (struck)','Halves: second Artin at left aligns with the Kiehl line above Saavedra; Ausgezeichnete Ringe. is fully recoverable, including final point.','insertion or placement','high','H','yes')
c('Atiyah / title',r'Atiyah, \uline{\unsure{Finiteness}} \unsure{Theorems} for compact Lie groups','Atiyah, Equivariant K-theory for compact Lie groups',r'Atiyah, \uline{Finiteness} Theorems for compact Lie groups','Half b: F initial, repeated i/n strokes, -teness ending, then separate capital T and heorems; no K-theory appears.','misread word','high','H')
c('Saavedra recipient / cancellation','struck','live','struck','Half b: both the horizontal rule and enclosing crossed block traverse Saavedra.','deletion state (struck given live or live given struck)','high','H')
c('SGA 6 recipient',r'\unsure{Dolotheo|Dolontho|Dolotho}','absent',r'\unsure{Dolotheo|Dolontho|Dolotho}','Crop 162-1/006 (175,1220,1065,1348): large D, l and later tall strokes, but crossing prevents a secure surname.','omission','low','H')
c('SGA reference and parenthesis',r'SGA 6 X (\unsure{Manin|Mumford} \unsure{formel|feuillets|feuilles})',r'SGA 4 IX (?) \ill',r'SGA 6 \underline{X} (\unsure{Manin|Mumford} \unsure{formel})','Same crop (175,1220,1065,1348): a closed lower loop makes 6; X has two diagonal strokes and an underline; the two-line parenthesis is not a question mark. Name remains crossed; formel favored.','misread symbol or index','high','H','yes')
c('Kleiman / conjectures entry',r'Notes Kleiman conj. \unsure{standart|standard}',r'Notes Kleiman sur \uncertain{standard}',r'Notes Kleiman, conj. \unsure{standart|standard}','Crop 162-1/006 (535,1390,1170,1460): comma after name, c-on-j descender and point; final letter of standart has a t-like cross but intersects cancellation.','misread word','medium','CH','yes')
c('lower Deligne heading',r'\deleted{\uline{Deligne} (suite))}','Deligne (suite), live',r'\deleted{\uline{Deligne} (suite))}','Half b: horizontal rule through heading as well as underline below Deligne; two closing curves remain after suite.','deletion state (struck given live or live given struck)','high','H')
c('lower Deligne / Notes',r'Notes \unsure{Jussila|Jussita|Japonais}',r'Notes \ill avec Piatetski-Shapiro',r'Notes \unsure{Jussila|Jussita}','Crop 162-1/006 (610,1535,1520,1620): separate Notes J-initial surname line; no avec on this line. Piatetzki-Schapiro belongs to the Lettre line below.','insertion or placement','low','H','yes')
c('lower Deligne / Lettre',r'Lettre : \unsure{Obstruction|Obstructions|O. Zariski} - \unsure{Piatezki|Piatetzki}-Schapiro',r'Lettre : Artin \ill cohomologie \ill',r'Lettre : \unsure{Oort|Obstruction|O. Zariski} - \unsure{Piatetzki|Piatezki}-Schapiro','Crop 162-1/006 (610,1535,1520,1620): looped O-initial group with terminal t-like stroke; a shorter reading Oort is possible. To the right, P-i-a-t-e-t-z-k-i and Schapiro are substantially visible. Neither Artin nor cohomologie matches this line.','misread word','low','CH','yes')
c('lower Deligne / CR note',r'Notes CR \deleted{\unsure{Gabriel}} Cartier, groupes formels.','absent',r'\deleted{Notes CR \deleted{\unsure{Gabriel}} Cartier, groupes formels.}','Crop 162-1/006 (580,1590,1550,1679): CR, heavily locally cancelled name, Cartier and groupes formels. form another line beneath the Lettre.','omission','medium','H')
c('lower Deligne / categories line',r'Notes \unsure{Catégories|Catégorie} \unsure{cofibrées|triangulées} \illegible{1}','absent',r'\deleted{Notes \unsure{Catégories|Catégorie} \unsure{cofibrées|triangulées} \illegible{1}}','Same crop (580,1590,1550,1679): lowest distinct baseline has Notes, a Catégor- group, descending next word and a final wholly overstruck group.','omission','low','H')
c('Murre recipient',r'\deleted{\uline{Murre}}',r'\struck{Messing}',r'\deleted{\uline{Murre}}','Half b: M followed by u-r-r-e, with no ss, i-dot or ng descender. Underline distinct from the strike.','misread word','high','H')
c('Murre / conjecture ending',r'\unsure{Rosenlicht|Russellicht} uniforme',r'\uncertain{Rosenlicht} \ill',r'\unsure{Rosenlicht} uniforme','Crop 162-1/006 (590,1655,1495,1735): tall l/h/t and clear uniforme; the name is still partly crossed.','readable ink left as \\ill{}','medium','H','yes')
c('SGA 7 range',r'I \unsure{à|:} V',r'I \ldots V',r'I \unsure{à|:} V','Half b: one low loop/dot and one small higher mark between capped I and V; no written sequence of ellipsis dots.','misread symbol or index','low','H')
c('Rim / title','Thèse Gabriel','Rim, Gabriel','Thèse Gabriel','Half b: T-h-èse precedes Gabriel on right; Rim is the separate recipient at left.','misread word','high','H')
c('Quillen / Verdier letter','lettres à Verdier : (struck)','lettre à Verdier (live)','lettres à Verdier : (struck)','Half b: long cancellation through the entire line, final s before à, colon after Verdier.','deletion state (struck given live or live given struck)','high','H')
c('Quillen / next line',r'\unsure{Note|Notes} Verdier limite \unsure{projective|projectives}','Notes Verdier, limites projectives','Notes Verdier limite projective','Crop 162-1/006 (605,1993,1300,2055): Notes has a terminal small s; limite and projective have no separate plural s; no comma after Verdier.','misread word','high','H')
for place,before,after,why in [
 ('top qualification','suite|suite 2','suite','Parentheses and suite remain; no second numeral.'),('first title','Compliments|Compléments; Woodshole|Woods hole','Compliments Woodshole','Distinct i dot; no acute; continuous place name.'),('journal line','outer parentheses and Am.|Amer.','retained doubtful','Multiple diagonal crossings.'),('Teichmüller','Teichmüller','resolved','Half a shows T-e-i-ch-m-ü-ll-er including umlaut.'),('Pb','Pb|pb','Pb','High bowl of P.'),('Matsusaka third title','criteri.|criterion','criteri.','Crop shows final dot, no on.'),('Matsusaka ending','equivalens|equivalence','retained doubtful','Compressed final run.'),('Quasi-fonctions','hyphen|space','retained doubtful','Strike coincides with possible hyphen.'),('Hartshorne parenthesis','des|de; alg|alg.','des; alg','Date crop shows s; no terminal point before parenthesis.'),('Mumf','Mumf|Mumf.|Mme','Mumf|Mumf.','Final tall/descending stroke not an e.'),('Samuel name','Ramanan|Ramanam','Ramanan','Half a has final n turn, not another m hump.'),('Berthelot number','2','2','Clear curved base under hatching.'),('Cartier notes','Note|notes','notes','Lowercase initial and final s.'),('Atiyah title','Finiteness; Theorems','both resolved','Long words are legible beneath the crossing.'),('Dolotheo and parenthesis','name and Manin|Mumford; formel|feuillets|feuilles','name and Manin|Mumford retained; formel favored','Name remains crossed; lower group has -mel-like ending.'),('standart','standart|standard','retained doubtful','Final upright joins the cancellation.'),('Jussila','Jussila|Jussita|Japonais','Jussila|Jussita','No p descender in the word.'),('Gabriel overwrite','Gabriel','retained doubtful','Blue local strike consumes middle letters.'),('categories line','Catégories|Catégorie; cofibrées|triangulées; illegible 1','retained','Overlapping zigzag and pen strokes.'),('Rosenlicht','Rosenlicht|Russellicht','Rosenlicht, still doubtful','Single o after R favored; middle letters crossed.'),('SGA range','à|colon','retained','Two small marks not enough to settle.'),('Quillen last note','Note|Notes; projective|projectives','Notes; projective','Crop resolves endings.')]:certainty(p,place,before,after,why)
for args in [('journal','(Mumford + Matsusaka); Am. J. Math.','initial parenthesis absent; Amer. J. Math.','low','Cancellation obscures initial curve and journal abbreviation.'),('Matsusaka first title','chow','char.','medium','Last two strokes can be read either way.'),('Matsusaka ending','equivalens; dot–dash','equivalence; ellipsis','medium','Terminal compressed run and trailing punctuation.'),('Néron','Quasi-fonctions','Quasi fonctions','medium','Possible hyphen coincides with strike.'),('Rédaction','Mumf','Mumf.','medium','Possible point beneath crossing.'),('SGA 6 recipient','Dolotheo','Dolontho; Dolotho','low','Heavily crossed surname.'),('SGA 6 parenthesis','Manin; formel','Mumford','low','First word partly under zigzag; second weak.'),('Kleiman spelling','standart','standard','medium','t-like end crossed.'),('Deligne surname','Jussila','Jussita','low','Middle letters compressed and crossed.'),('Deligne letter','Oort; Piatetzki','Obstruction; O. Zariski; Piatezki','low','Short O-initial group unresolved; number of medial t strokes uncertain.'),('deleted prior name','Gabriel','no secure alternative','low','Overwritten locally.'),('categories line','Catégories; cofibrées; illegible 1','Catégorie; triangulées','low','Strong cancellation across every word.'),('conjecture name','Rosenlicht','no secure full alternative','medium','Some middle letters crossed.'),('SGA 7 range','à',':','low','Two detached small marks.')]:doubt(p,*args)
items=[('text','upper left','Deligne 2'),('deletion','after Deligne','(suite)'),('deletion','top right','Compliments Woodshole'),('deletion','second line','Mumford + Matsusaka; Am. J. Math. 1964'),('deletion','third line','Mumford : Abelian quotients of Teichmüller group'),('text','fourth line','Mumford : Some aspects of the Pb of Moduli (mimeo.)'),('deletion','fifth line','Lang Néron'),('display','upper middle','Matsusaka: three titles grouped by vertical line'),('text','Matsusaka line 1','chow of Jac. variety'),('text','Matsusaka line 2','A correction to ...'),('text','Matsusaka line 3','The criteri. for alg equivalens'),('deletion','below Matsusaka','Néron : Quasi-fonctions et hauteurs sur les V.A.'),('deletion','next line','Kleiman : notes pour SGA 6'),('deletion','next two lines','Grothendieck : lettre à Hartshorne du 25.9.67'),('display','below date','Weil / Andreotti, common vertical grouping with sur Torelli'),('deletion','Torelli group first name','Weil'),('text','Torelli group second name','Andreotti'),('deletion','next line','Rédaction Mumf lemme de Abhyankar'),('deletion','left and right','Artin; Kiehl sur th. de Frisch'),('deletion','next entry','Samuel; Papiers de Ramanan'),('text','centre left and right','Berthelot 1 ///; Gabriel : groupes formels'),('deletion','Berthelot number','(2)'),('deletion','Berthelot second line','Cartier : notes CR gr. form.'),('text','Berthelot third line','notes sur stratifications'),('deletion','Berthelot fourth line','notes sur groupe de BT et Cristaux'),('deletion','next entry','Artin; Kiehl Ausgezeichnete Ringe.'),('deletion','next two lines','Saavedra; Atiyah, Finiteness Theorems for compact Lie groups'),('deletion','next entry','Dolotheo; SGA 6 X (Manin formel)'),('deletion','below','B. Mazur; Correspondance avec Griffiths'),('deletion','Mazur second line','Notes Kleiman, conj. standart'),('deletion','lower block, left and first line','Deligne (suite)); Notes Jussila'),('deletion','lower block second line','Lettre : Oort - Piatetzki-Schapiro'),('deletion','lower block third line','Notes CR Gabriel Cartier, groupes formels.'),('deletion','local overwrite before Cartier','Gabriel'),('deletion','lower block fourth line','Notes Catégories cofibrées [unreadable word]'),('deletion','next entry','Murre; Conjecture sur Rosenlicht uniforme'),('deletion','next line','SGA 7 I à V'),('deletion','near foot','Rim; Thèse Gabriel'),('text','foot left','Quillen'),('deletion','Quillen first line','lettres à Verdier :'),('text','Quillen second line','Notes Verdier limite projective'),('text','last line','Notes Karoubi sur définition de K.')]
for k,pos,t in items:inventory(p,k,pos,t)
p['notation']=[['Bibliographic numerals','SGA 6 underlined X; SGA 7 capped I and V with doubtful separator.'],['Reminder strokes','Berthelot: cancelled (2), live 1, three oblique strokes; reproduce without interpreting.'],['Written capitals','CR, BT, V.A., K retained; no expansions in the text.'],['Grouped references','Matsusaka left vertical rule groups three titles; Weil/Andreotti share sur Torelli to the right.']]
p['hand']=[['Dots distinguish i from accented e','Compliments at top has a separate i dot. This is one observed token, not a global spelling rule.','H normalized to Compléments; C doubted both.'],['Final t versus d in English words','standart/standard remains unresolved here; t-like terminal upright is not enough under a crossing.','Neither spelling silently regularized.'],['Compressed title endings','criteri. and equivalens remain as written or marked; not completed to a known title.','H expands criteria and equivalence; C keeps alternatives.'],['Cancellations can span multiple recipients','Pencil zigzag crosses Artin/Samuel and the large middle group; names remain transcribed.','H leaves Samuel and Saavedra live.']]
p['abbreviations']=[['Pb','problème'],['mimeo.','mimeographed'],['Am. / Amer. J. Math.','American Journal of Mathematics (interpretive identification, not independently checked)'],['Jac.','Jacobian'],['criteri.','criterion / criteria, unresolved abbreviated form'],['alg','algebraic / algébrique'],['V.A.','variétés abéliennes'],['dim. coh.','dimension cohomologique'],['Var','variétés'],['Mumf','Mumford, probably'],['CR','Comptes rendus, probably'],['gr. form.','groupes formels'],['BT','Barsotti–Tate, probable expansion only'],['conj.','conjectures']]
p['notes']=['Continuation of the loan list, with Deligne, Artin, Samuel, Berthelot, Saavedra, B. Mazur, Murre, Rim and Quillen entries, plus one heavily crossed uncertain recipient. Names and title fragments are preserved without identifying works externally.', 'Two dates/numbers are explicit: 1964 in the journal reference and 25.9.67 for the Grothendieck letter to Hartshorne. The latter differs from H’s 21.9.67; the second digit is read from its bend, not from bibliographic expectation.', 'Technical-title corrections include Finiteness Theorems, SGA 6 X, and the abbreviated CR/gr. form./BT entries. They alter bibliographic or mathematical subject identification, but this sheet offers no proof to check. The author’s Conjecture label is retained. Archive number: 5; no manuscript title sheet or page count.']
save(p,tex)
print('Saved',p['filename'],len(p['changes']),'changes;',p['done'])
