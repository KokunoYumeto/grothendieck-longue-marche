from records import *
p=page('162-1',7)
tex=r'''\scanpage{7}
\uline{Szpiro}

\(\left\Vert\begin{array}{@{}p{.91\linewidth}@{}}Notes de moi et \unsure{Bass|Bon} sur \unsure{caractérisation|caracterisation} des Gorenstein\\Notes sur $\exists$ complexe dualisant en dim 1\end{array}\right.\)

Notes SGA 7

\deleted{Notes sur dualité de Poincaré en coh. de Hodge des variétés alg. singulières (A) à (E)).}

\deleted{\uline{Hartshorne}\qquad SGA 2}

\deleted{\unsure{R|K} Livre Verdier}

\uline{Balasko}

\deleted{Notes}\quad\(\left\{\begin{array}{l}\text{\deleted{$\underline{NS}_{X/S}\unsure{\mathbin{-\!\circ}|\to}\underline{NS}_{B/S}$ etc}}\\\text{\deleted{produit de convolution sur VA}}\end{array}\right.\)

\deleted{3 Articles de Rim-Buchsbaum}

\deleted{Notes EGA V sur idéaux de Fitting}

\deleted{\uline{Giraud}\qquad Notes Cartier sur vecteurs de Witt.}

\deleted{\uline{Theodoros}}\qquad \deleted{Bourbaki}\ \(\left\{\begin{array}{l}\text{\deleted{Top. Gén. $\overline{\underline{\mathrm I}}$}}\\\text{\deleted{\unsure{Ens|Ets} $\overline{\underline{\mathrm I}}$}}\end{array}\right.\)

Poenaru\qquad Atiyah-Hirzebruch, über Cohomologieoperationen\unsure{-|\ldots} \unsure{---|\ldots}

Stolzenberg : revue livre Bishop \ldots

\deleted{Bardach (suite)\qquad 2 articles d'Artin sur singularités rationnelles}

\deleted{\unsure{Houzel|Housder}\qquad Artin : a) Contractions\quad b) Foncteurs représentables}

Saint Donat 1\qquad SGA 5 $\overline{\underline{\mathrm{IV}}}$ (Notes Jouanolou)

\deleted{SGA 7 $\overline{\underline{\mathrm I}}$ à $\overline{\underline{\mathrm V}}$ (\unsure{1 à|I à|en} \unsure{microfiches|microfilms})}

Livre Mumford VA

Notes Deligne\qquad \(\left\{\begin{array}{@{}p{.67\linewidth}@{}}sur th. de Lefschetz vache\\sur conj pour courbes rel. (cf SGA 4 $\overline{\underline{\mathrm{XVIII}}}$)\end{array}\right.\)

% archive sheet number: 6
\clearpage
'''
def c(place,C,H,F,S,K='misread word',conf='high',a='CH',m='no'):change(p,place,C,H,F,S,K,conf,a,m)
c('Szpiro / collaborator','Bass',r'\uncertain{Bou.}',r'\unsure{Bass|Bon}','Crop 162-1/007 (645,43,1180,117): B and a compact round letter followed by two short joined turns; no terminal point. Bass remains favored but not certain.','misread word','medium','H','yes')
c('Szpiro / dimension','dim 1','dimension 1','dim 1','Half a: short dim with no point before the numeral 1.','abbreviation expanded or spelling modernised','high','H')
c('Poincaré title abbreviations','coh.; alg.','cohomologie; algébriques','coh.; alg.','Half a: abbreviated words have visible points; not the expanded words.','abbreviation expanded or spelling modernised','high','H')
c('Poincaré parenthesis','(A) à (E)).','((A) à (E))','(A) à (E)).','Half a: one opening parenthesis before A, two closing curves after E, then a point.','other','high','H')
c('before Livre Verdier',r'\unsure{R|K}','absent',r'\unsure{R|K} (within cancellation)','Half a: local dark overwritten letter before Livre, with a vertical and a diagonal leg. It is not silently discarded.','omission','low','H')
c('recipient underlines','underlined Szpiro, Hartshorne, Balasko, Giraud, Theodoros','bold names without recorded underlines','source underlines retained','Halves a/b: separate thin lines below the names; where cancelled, an independent line also crosses the baseline.','other','high','H')
c('Balasko formula',r'\underline{NS}_{X/S}\unsure{-\!\circ|\to}\underline{NS}_{B/S}',r'NS_{X/S}\to NS_{B/S}',r'\underline{NS}_{X/S}\unsure{-\!\circ|\to}\underline{NS}_{B/S}','Crop 162-1/007 (660,612,1080,701): both NS groups have short separate underlines and X/S, B/S below; connector terminates in a closed loop, not a clearly open arrowhead.','misread symbol or index','medium','H')
c('Balasko / VA punctuation','etc; VA','etc.; V.A.','etc; VA','Half a: no point after etc and no points between VA.','abbreviation expanded or spelling modernised','high','H')
c('Balasko / Articles capital','3 Articles','3 articles','3 Articles','Half a: tall A with cross stroke after 3.','other','high','H')
c('Giraud terminal punctuation','Witt.','Witt','Witt.','Half b: separate point after Witt.','other','high','H')
c('Bourbaki recipient',r'\unsure{Theodoros|Theodorov|Theodores}',r'\uncertain{Theodorou}','Theodoros','Crop 162-1/007 (210,1498,457,1598): Theodo followed by r, rounded o and hooked terminal s.','misread word','high','H','yes')
c('Bourbaki second title',r'\unsure{Ens|Ets} I','Alg. I',r'\unsure{Ens|Ets} I','Crop 162-1/007 (780,1465,1065,1580): initial E has a lower horizontal; no A, l, or g descender. Middle n/t remains crossed.','misread word','medium','H')
c('Bourbaki first title case','Top. Gén. I','Top. gén. I','Top. Gén. I','Same crop (780,1465,1065,1580): large G-initial group, with upper accent stroke; numeral has cap and foot.','other','high','H')
c('Poenaru German compound',r'\unsure{Cohomologieoperationen|Cohomologie-operationen}','Cohomologie-Operationen','Cohomologieoperationen','Crop 162-1/007 (1050,1588,1653,1688): continuous letters through -gieoperationen, no hyphen or second capital O.','abbreviation expanded or spelling modernised','high','H')
c('Poenaru trailing marks',r'\unsure{-|...} \unsure{---|...}',r'\ill',r'\unsure{-|\ldots} \unsure{---|\ldots}','Same crop (1050,1588,1653,1688): short horizontal at right edge and a lower row of faint short marks; no readable word occupies the position.','text not on the page','medium','H','yes')
c('Stolzenberg / du and ending','revue livre Bishop ...',r'revue \add{du} livre Bishop \ill','revue livre Bishop ...','Half b: no du or insertion sign between revue and livre; three short points follow Bishop.','text not on the page','high','H','yes')
c('Bardach recipient',r'\unsure{Bardach|Bredach|Bardaeh}',r'Boutot','Bardach','Half b: B-ar-d-ach agrees in stroke sequence with the clearer Bardach on 162-1/005; final tall h visible.','misread word','high','H')
c('Bardach suite deletion','(suite) struck','(suite) live','(suite) struck','Half b: cancellation runs continuously through the parenthesized qualification.','deletion state (struck given live or live given struck)','high','H')
c('Artin recipient',r'\unsure{Houzel|Houzels|Housder}','Horrocks',r'\unsure{Houzel|Housder}','Crop 162-1/007 (205,1900,925,1965): H-ou and a compact z/e/l-like ending; no secure double r or c-k sequence.','misread word','medium','H')
c('Artin two items',r'a) \unsure{Contractions|Constructions} b) Foncteurs représentables',r'\ill foncteurs représentables','a) Contractions b) Foncteurs représentables','Same crop (205,1900,925,1965) with half b: light a), Contractions with t-r-a sequence, separate b) and capital F begin the second title.','readable ink left as \\ill{}','high','H','yes')
c('Saint Donat / source parentheses','(Notes Jouanolou)','supplied (notes Jouanolou)','(Notes Jouanolou)','Half b: both parenthesis curves are drawn; Notes starts with a capital N. These are source punctuation, not editorial supplementation.','other','high','H')
c('Saint Donat / SGA 7 range and qualification',r'SGA 7 I à V (\unsure{1 à|I à|en} \unsure{microfiches|microfilms})',r'SGA 7 I ... V',r'SGA 7 I à V (\unsure{1 à|I à|en} \unsure{microfiches|microfilms})','Crop 162-1/007 (598,1993,1183,2058): small à between I and V; long parenthesis follows V, heavily cancelled, with upper strokes compatible with microfiches/microfilms.','omission','low','H')
c('Mumford abbreviation','VA','V.A.','VA','Half b: two adjacent capitals without points.','abbreviation expanded or spelling modernised','high','H')
c('Deligne notes / two lines',r'sur th. de Lefschetz \unsure{vache}; sur \unsure{conj|conj.} pour courbes rel. (cf SGA 4 XVIII)','th. de Lefschetz vache sur anneau pour courbes elliptiques (cf. SGA 4 XVIII)','sur th. de Lefschetz vache; sur conj pour courbes rel. (cf SGA 4 XVIII)','Crop 162-1/007 (1020,2044,1645,2137): left brace separates two lines, each beginning sur; second has conj with j descender, then courbes rel.; no anneau or elliptiques. cf has no point.','misread word','high','H')
for args in [('Szpiro name','Bass confident','Bass|Bon doubtful','Compact joined ending warrants doubt; the expected collaborator does not decide it.'),('characterisation accent','caractérisation|caracterisation','retained','Small raised mark cannot be cleanly separated from nearby dots.'),('before Livre','R|K','retained','Local scribble consumes the letter.'),('NS connector','-circle|arrow','retained','Closed terminal loop remains; do not force a map from context.'),('Theodoros','Theodoros|Theodorov|Theodores','Theodoros resolved','Final o and hooked s distinct.'),('Ens','Ens|Ets','retained','Crossing masks middle letter.'),('German compound','with/without hyphen','without hyphen','No detached connecting hyphen or capital O.'),('German end marks','dash|dots; dashes|dots','retained','Faint short marks.'),('Bardach','Bardach|Bredach|Bardaeh','Bardach resolved','Consistent with clearer 005 token and separately confirmed here.'),('Houzel','Houzel|Houzels|Housder','Houzel|Housder retained','No separate final s; centre still uncertain.'),('Artin title','Contractions|Constructions','Contractions resolved','Visible t-r-a group.'),('Saint Donat','Donat|Donats','Donat resolved','Terminal t flourish, no separate s.'),('microfiche qualification','1 à|I à|en; microfiches|microfilms','retained','Baseline is hidden under two heavy cancellations.'),('Deligne / vache','vache','resolved','Five letters v-a-c-h-e are legible and retained despite unusual wording.'),('Deligne / conj','conj|conj.','conj','No distinct point after j; terminal loop is its descender.')]:certainty(p,*args)
for args in [('first collaborator','Bass','Bon','medium','Compact joined final strokes.'),('first title accent','caractérisation','caracterisation','medium','Raised mark does not securely identify acute accent.'),('before Livre Verdier','R','K','low','Overwritten letter.'),('Balasko connector','-circle','right arrow','medium','Closed loop could be a very small arrowhead.'),('Bourbaki abbreviation','Ens','Ets','medium','Middle letter struck.'),('German end marks','dash; short dashes','ellipsis marks','low','Faint terminal and lower traces.'),('Artin recipient','Houzel','Housder','medium','Crossed surname ending.'),('SGA 7 parenthesis','1 à microfiches','I à; en; microfilms','low','Two dark horizontal strikes conceal most lower strokes.')]:doubt(p,*args)
for k,pos,t in [('text','top left','Szpiro'),('display','top right, paired rule','Notes de moi et Bass sur caractérisation des Gorenstein / Notes sur exists complexe dualisant en dim 1'),('text','top right next line','Notes SGA 7'),('deletion','next two lines','Notes sur dualité de Poincaré en coh. de Hodge ... (A) à (E)).'),('deletion','upper quarter','Hartshorne; SGA 2'),('deletion','Hartshorne second line','R/K Livre Verdier'),('text','middle left','Balasko'),('display','middle right brace','NS_X/S -circle NS_B/S etc / produit de convolution sur VA'),('deletion','Balasko braced block','Notes; underlined NS terms; produit de convolution'),('deletion','next line','3 Articles de Rim-Buchsbaum'),('deletion','next line','Notes EGA V sur idéaux de Fitting'),('deletion','lower half','Giraud; Notes Cartier sur vecteurs de Witt.'),('deletion','next recipient','Theodoros; Bourbaki'),('display','beside Bourbaki','Top. Gén. I / Ens I'),('deletion','Bourbaki brace','Top. Gén. I / Ens I'),('text','next entry','Poenaru; Atiyah-Hirzebruch, über Cohomologieoperationen and trailing marks'),('text','next line','Stolzenberg : revue livre Bishop ...'),('deletion','next entry','Bardach (suite); 2 articles d’Artin sur singularités rationnelles'),('deletion','near foot','Houzel; Artin : a) Contractions b) Foncteurs représentables'),('text','near foot','Saint Donat 1; SGA 5 IV (Notes Jouanolou)'),('deletion','next line','SGA 7 I à V (1 à microfiches)'),('text','bottom','Livre Mumford VA'),('text','bottom left','Notes Deligne'),('display','bottom right brace','sur th. de Lefschetz vache / sur conj pour courbes rel. (cf SGA 4 XVIII)')]:inventory(p,k,pos,t)
p['notation']=[['Existence sign','Szpiro line 2 has reversed E with three short bars: exists, not a numeral.'],['NS expression','Underlined NS with X/S and B/S subscripts; -circle|arrow uncertain.'],['Roman references','I, IV, V, XVIII with caps and feet; no primes or exclamation marks.'],['Explicit grouping','Double vertical rule groups first two Szpiro titles; braces group Balasko, Bourbaki and bottom Deligne entries.']]
p['hand']=[['Bardach recurring surname','Read on 162-1/005 and 007; a-r-d-a-c-h confirmed at both occurrences.','H: Boutot here; C offered Bredach/Bardaeh.'],['Terminal arrow-like loop','One connector in NS expression; closed head survives. No recurring-arrow rule established.','H assumes a conventional right arrow; C and final retain ambiguity.'],['Small abbreviation Ens/Ets','One crossed token; E certain, middle letter unresolved.','H reads Alg., which does not match the initial.'],['Unusual source word vache','One legible token at bottom after Lefschetz. No correction or external identification made.','C doubts removed; H joins separate lines and expands rel. to elliptiques.']]
p['abbreviations']=[['dim','dimension'],['coh.','cohomologie'],['alg.','algébriques'],['NS','Néron–Severi, probable subject identification only'],['VA','variétés abéliennes'],['Top. Gén.','topologie générale'],['Ens / Ets','ensembles, if Ens; Ets unresolved'],['conj','conjecture(s)'],['rel.','relatives, probably'],['cf','confer']]
p['notes']=['Loan-list entries concern dualizing complexes, Gorenstein characterizations, Hodge duality, Néron–Severi-type notation, Bourbaki volumes, and references attributed to Artin and Deligne. No argument for any of these subjects is supplied.', 'The NS connector was reconsidered because the adjacent objects could suggest a map. The surviving closed head is insufficient to force an arrow; -circle and right arrow remain alternatives. Likewise the ink vache after Lefschetz is retained, and courbes rel. is not expanded to elliptiques.', 'Source grouping matters: two Deligne notes stand under a brace, each beginning sur. No authorial proof-check phrase, date, title sheet or page count occurs. The source has the unbalanced-looking (A) à (E)). punctuation; archive number 6 is a comment only.']
save(p,tex)
print('Saved',p['filename'],len(p['changes']),'changes;',p['done'])
