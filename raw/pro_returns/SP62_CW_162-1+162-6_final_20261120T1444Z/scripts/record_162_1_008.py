from records import *
p=page('162-1',8)
tex=r'''\scanpage{8}
\reversemarginpar
Berthelot 2

% slanted
\margin{\uline{redemander}}

\(\left\{\vcenter{\hbox{\begin{minipage}{.89\linewidth}
Deligne \(\left\{\begin{array}{@{}p{.75\linewidth}@{}}\deleted{Structure à l'$\infty$ des \unsure{éqs|éqns} P.F.}\\\deleted{lettre à Leray et Washnitzer}\end{array}\right.\)

Katz\quad \(\left\vert\begin{array}{@{}p{.79\linewidth}@{}}Th. de Dwork (2 papiers)\\Theory of regular singular points\\\unsure{Nilpotence|Nilpotent} connection of Gauss Manin\par\hfill(2 papiers)\\Th. de monodromie \unsure{vs.|v.|cr.} Berthelot\end{array}\right.\)

Grothendieck : Torsion en ch. cristalline.

Petit papier Deligne sur prémorphismes de sites.

Papiers Deligne : Sém Harvard

SGA 5 $\overline{\underline{\unsure{\mathrm{VII}|\mathrm{XII}}}}$ \S\S\ 1,10 (Jouanolou)

Notes Katz connexions intégrables (MA)
\end{minipage}}}\right.\)

Illusie \deleted{\illegible{1}}\qquad lettre à Giraud sur obstructions aux rel. de groupes lisses.

Papier Mazur-Roberts sur char. d'E-P.

% slanted
\margin{\tikz[baseline=(t.base)]{\node[inner sep=1pt] (t) {\deleted{\uline{redemander}}};\draw (t.center) ellipse [x radius=2.6em,y radius=.65em];}}

\deleted{2 \uwave{paquets notes sur opérations de Cartier}}

Notes sur th. de Deligne sur ``torseurs universels''.

\deleted{SGA\deleted{4} 6 $\overline{\underline{\mathrm I}}\ \overline{\underline{\mathrm {II}}}\ \overline{\underline{\mathrm {III}}}$ pour révision}

Serre : variétés qui ne se relèvent pas en \inserted{\uline{car. 0}}

Seydi\qquad Notes sur \unsure{lemme|lemmes} Hironaka

\deleted{Thèse Verdier} sur morphismes univ. ouverts

\uline{Thomas} 1\qquad Papiers \unsure{Lindenstrausss|Lindenstrauss}, Pelczynski etc

Survey de Lindenstrauss \unsure{---|--}

\uline{Jurchescu}\qquad Knorr, Finitude, $\overline{\underline{\mathrm I}}$, $\overline{\underline{\mathrm {II}}}$.

Petit livre sur finitude

Goldschmidt\qquad \unsure{Brieskorn|Brishorn} $\{$singularités rationnelles - - - -$\}$

\deleted{Grauert}\qquad \deleted{Artin, alg. of formal moduli $\overline{\underline{\mathrm I}}$,$\overline{\underline{\mathrm {II}}}$}

% archive sheet number: 7
\clearpage
\normalmarginpar
'''
def c(place,C,H,F,S,K='misread word',conf='high',a='CH',m='no'):change(p,place,C,H,F,S,K,conf,a,m)
c('Deligne / first title',r'Structure à l’infini des \unsure{éqs|éqns|éqn} P.F.',r'Structure : l’infini des \ill P.F.',r'Structure à l’infini des \unsure{éqs|éqns} P.F.','Crop 162-1/008 (790,21,1550,111): low a-like oval with a separate grave-like stroke; short é/q/s-or-n group before P.F., not a missing full word.','readable ink left as \\ill{}','medium','H','yes')
c('Deligne / letter names',r'\unsure{Leray|Levy} et \unsure{Washnitzer|Washnitsar}',r'Tate et \uncertain{Washington}','Leray et Washnitzer','Same crop (790,21,1550,111): L-e-r-a-y and W-a-sh-n-i-t-z-e-r survive through the line.','misread word','high','H','yes')
c('Katz / third title',r'\unsure{Nilpotence|Nilpotent|Nilpotens} \unsure{connection|connexion} of Gauss Manin',r'Nilpotent connections et Gauss–Manin',r'\unsure{Nilpotence|Nilpotent} connection of Gauss Manin','Crop 162-1/008 (745,208,1650,346): first ending compressed, -ence favored; connection is singular and has ct; descending f makes of, not et. No hyphen between Gauss and Manin.','misread word','medium','H')
c('Katz / paper count','(2 papiers)',r'(2 \uncertain{versions})','(2 papiers)','Same crop (745,208,1650,346): p descenders and a dotted i; papiers, not versions.','misread word','high','H','yes')
c('Katz / monodromy abbreviation',r'\unsure{cr.|v.|vs.}',r'remis à',r'\unsure{vs.|v.|cr.}','Crop 162-1/008 (1200,309,1630,393): two small joined turns and a point before Berthelot; no full words remis à.','abbreviation expanded or spelling modernised','low','CH')
c('Grothendieck / abbreviation',r'\unsure{coh.|ch.}','cohomologie','ch.','Crop 162-1/008 (1135,389,1530,453): one c-shaped oval followed immediately by h and point; no separate o.','abbreviation expanded or spelling modernised','high','CH')
c('Harvard abbreviation',r'\unsure{Sém|Sém.|Séries}','Sém.','Sém','Half a: S, accented é and low m; no separate stop after the word.','other','high','H')
c('SGA 5 numeral',r'\unsure{XII|VII} capped, live','XII struck',r'\unsure{VII|XII} capped, live','Crop 162-1/008 (595,545,1480,634): first form looks like V with a dark overtrace, followed by II. Cap and foot do not run through the centre as a cancellation would. XII remains possible.','misread symbol or index','medium','CH')
c('SGA 5 sections','§§ 1,10','§§ 9, 10','§§ 1,10','Same crop (595,545,1480,634): first digit has an angular entry and long upright ending on a foot, without a 9 loop.','misread symbol or index','high','H')
c('SGA 5 parenthesis','(Jouanolou)',r'added/supplied (\ill)','(Jouanolou)','Same crop (595,545,1480,634): full J-ou-an-ou-l-ou and both written parentheses visible.','readable ink left as \\ill{}','high','H','yes')
c('Notes Katz suffix',r'\unsure{MA|MS}','MS','MA','Same crop (595,545,1480,634): final letter has two diagonals and lower apex-like connection of A, not an S curve.','misread symbol or index','high','H')
c('Giraud letter / abbreviation','rel.','relèvements','rel.','Half a: three-letter abbreviation and point before de.','abbreviation expanded or spelling modernised','high','H')
c('Giraud letter / group adjective','groupes lisses',r'groupes \uncertain{discrets}','groupes lisses','Half a: l-i-ss-es, with no initial d or cr group; final source point retained.','misread word','high','H','yes')
c('Mazur–Roberts subject',r'\unsure{char.|chr.|car.} d’E-P.','cohomologie d’E.-P.','char. d’E-P.','Crop 162-1/008 (1025,676,1392,731): c, tall h, separate a/r group and point; no point after E before hyphen.','abbreviation expanded or spelling modernised','high','H')
c('Cartier / marginal reminder','circled, underlined, struck redemander','circled redemander, no cancellation recorded','circled, underlined, struck redemander','Half a: two oblique strokes pass across the slanted word inside a light oval; underline is separate.','deletion state (struck given live or live given struck)','high','H')
c('Deligne / universal objects','``torseurs universels’’','« diviseurs universels »','``torseurs universels’’','Half a: tall t followed by o-r-seurs; no div- letters. Double high marks are paired quotation strokes, not drawn guillemets.','misread word','high','H')
c('SGA 6 / corrected digit',r'SGA\unsure{4|5} 6','SGA struck 4 then 6',r'SGA\deleted{4} 6, within whole-line deletion','Crop 162-1/008 (571,829,1180,904): the small 4 is separately retraced/cancelled beside the more open 6; whole line also cancelled.','deletion state (struck given live or live given struck)','medium','C')
c('SGA 6 / middle numeral and qualification','I II III pour révision','I, III, première rédaction','I II III pour révision','Same crop (571,829,1180,904): three capped numeral groups; the middle has two uprights; p-o-u-r then révision, not première rédaction.','misread symbol or index','high','H')
c('Serre / inserted condition',r'en \inserted{\uline{car. 0}}',r'(car. 0) attached to preceding SGA entry; en \ill',r'en \inserted{\uline{car. 0}}','Half a: car. 0 sits above the right-hand en of Serre’s line; bent connector returns to that line, not to SGA.','insertion or placement','high','H','yes')
c('Seydi / univ.','univ.','universellement','univ.','Half b: short u-n-i-v and point, not a full adverb.','abbreviation expanded or spelling modernised','high','H')
c('Thomas / first surname',r'\unsure{Lindenstrausss|Lindenstrauss}','Lindenstrauss',r'\unsure{Lindenstrausss|Lindenstrauss}','Crop 162-1/008 (666,1426,995,1506): three final s-like uprights appear after au, but one could belong to a retrace. The following occurrence is shorter.','misread word','medium','H')
c('Thomas / second surname and etc','Pelczynski etc','Pełczyński etc.','Pelczynski etc','Half b: no stroke across l or acute over n; etc has no separate point.','abbreviation expanded or spelling modernised','high','H')
c('Survey ending',r'\unsure{---|--}',r'\ill',r'\unsure{---|--}','Half b: only short horizontal traces after Lindenstrauss, no word.','text not on the page','medium','H','yes')
c('Knorr recipient',r'\uline{\unsure{Jurchescu|Jurechescu}}',r'\uncertain{Zuckerman}',r'\uline{Jurchescu}','Half b: initial long descending J, u-r-c-h-e-s-c-u; an independent underline.','misread word','high','H','yes')
c('Goldschmidt / braced ending',r'Brieskorn {singularités rationnelles \unsure{- - - -|....}}',r'Brieskorn : singularités rationnelles \ill',r'\unsure{Brieskorn|Brishorn} {singularités rationnelles - - - -}','Half b and name crop (607,1830,808,1913): source braces enclose the subject and four horizontal short marks; no colon before the opening brace. Internal surname letters remain compressed.','drawing or diagram','medium','H','yes')
c('bottom recipient',r'\unsure{Grauert|Grammont}',r'\ill','Grauert','Half b: G-r-a-u-e-r-t visible beneath cancellation.','readable ink left as \\ill{}','high','H','yes')
c('Artin title abbreviation','alg. of formal moduli','Algebraization of formal moduli','alg. of formal moduli','Half b: lower-case a-l-g and point, not the full title word; dotted final i in moduli.','abbreviation expanded or spelling modernised','high','H')
c('underlines and terminal punctuation','underlined redemander (top), Thomas; source points after cristalline, sites, universels, Knorr reference','underlines/source points not recorded at these places','underlines and source points retained','Halves a/b: short rules beneath the named words and separate final dots are visible; neither invented italics nor sentence punctuation is added.','other','high','H')
for args in [('Deligne abbreviation','éqs|éqns|éqn','éqs|éqns retained','Final short s-like stroke; internal n uncertain.'),('letter names','Leray|Levy; Washnitzer|Washnitsar','Leray; Washnitzer resolved','Top crop shows letter sequence through crossing.'),('Katz title','Nilpotence|Nilpotent|Nilpotens; connection|connexion','Nilpotence|Nilpotent; connection','First ending weak; ct and singular final n clear in second word.'),('Grothendieck','Grothendieck|Guillemaud','Grothendieck resolved','Half a has th-end-ieck sequence.'),('prémorphismes','prémorphismes|prémorphisme','prémorphismes','Final s before space and de sites.'),('Harvard','Sém|Sém.|Séries','Sém','Three-letter abbreviated group with no point.'),('Notes Katz','MA|MS','MA','Angular A.'),('Illusie cancelled word','illegible 1','illegible 1 retained','Crop (340,637,524,698) is filled by multiple dark retraces; no complete word can be recovered.'),('Mazur','char.|chr.|car.','char.','Separate h and a survive.'),('Cartier','opérations|opération','opérations','Terminal small s visible before de.'),('Seydi','lemme|lemmes','retained','Crop (468,1123,947,1189): trailing turn could be final e or es.'),('Lindenstrausss','extra s|normal spelling','retained','Three final hooks may include a retrace.'),('Survey marks','---|--','retained','Faint horizontal traces.'),('Jurchescu','Jurchescu|Jurechescu','Jurchescu','No additional e before ch.'),('Brieskorn','Brieskorn|Brishorn','retained','Crop shows ambiguous medial high stem.'),('Goldschmidt marks','four dashes|dots','four short dashes','Each is elongated horizontally.'),('bottom','Grauert|Grammont; moduli|modulé','Grauert; moduli','Half b settles name and dotted i.')]:certainty(p,*args)
for args in [('Deligne abbreviation','éqs','éqns','medium','Crossing through the middle.'),('Katz adjective','Nilpotence','Nilpotent','medium','Final letters compressed; English expectation does not decide.'),('Katz monodromy','vs.','v.; cr.','low','Very small abbreviation before Berthelot.'),('SGA 5 numeral','VII','XII','medium','First diagonal is overtraced.'),('Illusie word','illegible 1','no secure reading','low','Dense retracing physically hides a word.'),('Seydi note','lemme','lemmes','medium','Terminal curve not decisive.'),('Thomas name','Lindenstrausss','Lindenstrauss','medium','Possible extra s or retracing.'),('Survey marks','---','--','medium','Faint short lines.'),('Goldschmidt name','Brieskorn','Brishorn','medium','Compressed medial letters.')]:doubt(p,*args)
for k,pos,t in [('text','top left','Berthelot 2'),('margin note','left oblique, beside upper brace','redemander underlined'),('display','upper right outer brace','Deligne, Katz, Grothendieck and further references grouped'),('display','Deligne small brace','Structure à l’infini ... / lettre à Leray et Washnitzer'),('deletion','Deligne line 1','Structure à l’infini des éqs P.F.'),('deletion','Deligne line 2','lettre à Leray et Washnitzer'),('display','Katz vertical grouping','Th. de Dwork / Theory of regular singular points / Nilpotence connection / Th. de monodromie'),('text','Katz line 1','Th. de Dwork (2 papiers)'),('text','Katz line 2','Theory of regular singular points'),('text','Katz line 3 and continuation','Nilpotence connection of Gauss Manin (2 papiers)'),('text','Katz line 4','Th. de monodromie vs. Berthelot'),('text','under Katz','Grothendieck : Torsion en ch. cristalline.'),('text','next line','Petit papier Deligne sur prémorphismes de sites.'),('text','next line','Papiers Deligne : Sém Harvard'),('text','next line','SGA 5 VII §§ 1,10 (Jouanolou)'),('text','last of upper brace','Notes Katz connexions intégrables (MA)'),('text','middle','Illusie; lettre à Giraud sur obstructions aux rel. de groupes lisses.'),('deletion','after Illusie','one unreadable crossed word'),('text','next line','Papier Mazur-Roberts sur char. d’E-P.'),('margin note','left beside Cartier entry','circled underlined redemander'),('deletion','same marginal oval','redemander'),('deletion','Cartier line','2 paquets notes sur opérations de Cartier'),('text','next line','Notes sur th. de Deligne sur torseurs universels'),('deletion','next line','SGA4 6 I II III pour révision'),('deletion','within SGA correction','4'),('text','following line','Serre : variétés qui ne se relèvent pas en'),('insertion','above right end of Serre line','car. 0, underlined'),('text','middle lower','Seydi; Notes sur lemme Hironaka'),('deletion','next line opening','Thèse Verdier'),('text','continuation','sur morphismes univ. ouverts'),('text','lower third','Thomas 1; Papiers Lindenstrausss, Pelczynski etc'),('text','next line','Survey de Lindenstrauss ---'),('text','next entry','Jurchescu; Knorr, Finitude, I, II.'),('text','next line','Petit livre sur finitude'),('text','next entry','Goldschmidt; Brieskorn'),('display','right of Brieskorn','braced singularités rationnelles and four dashes'),('deletion','foot','Grauert; Artin, alg. of formal moduli I,II')]:inventory(p,k,pos,t)
p['notation']=[['Infinity sign','Deligne title: horizontal figure-eight after l’, retained as infinity.'],['Section notation','Two section signs, 1,10 with comma; Roman VII|XII remains marked.'],['Corrected SGA reference','Cancelled 4 replaced by 6, then I II III; whole entry later struck.'],['Quotation marks','Two upper strokes on either side of torseurs universels: double backtick/apostrophe encoding.'],['Inserted characteristic','car. 0 above line belongs after Serre’s en, with underline.']]
p['hand']=[['Capital A versus S','MA in Notes Katz: angular final letter with no S curve; this occurrence is settled.','H MS; C had MA|MS.'],['Short ch. abbreviation','Torsion en ch. cristalline has c immediately joined to h, no separately written o.','C preferred coh.; H expanded cohomologie.'],['Retouched Roman initial','SGA 5 VII|XII: cap and foot plus dark overtrace; no cancellation across centre.','H marked XII struck; C preferred XII.'],['Letter s and retracing','First Lindenstrausss may have extra s; next occurrence reads Lindenstrauss. Scope limited to these two tokens.','H normalizes first; final preserves uncertainty.']]
p['abbreviations']=[['éqs / éqns','équations'],['P.F.','Picard–Fuchs'],['ch.','cohomologie, likely'],['Sém','séminaire'],['MA','unresolved initials'],['rel.','relèvements'],['char. d’E-P.','caractéristique d’Euler–Poincaré, probable expansion'],['car. 0','caractéristique zéro'],['univ.','universellement'],['alg.','algebraization in this English title, probable expansion only']]
p['notes']=['Loan list dominated by Berthelot and Illusie, followed by Seydi, Thomas, Jurchescu, Goldschmidt and Grauert. Two marginal redemander reminders are source instructions to the list’s author; the lower one is circled and cancelled.', 'The source reads groupes lisses, torseurs universels, char. d’E-P., and I II III pour révision. These are corrected subject labels or references, not proofs of the corresponding results. The raised car. 0 belongs to Serre’s variétés qui ne se relèvent pas en, not to the cancelled SGA entry.', 'No proof is supplied for the Serre reference and none is reconstructed. The SGA 5 chapter numeral, Katz adjective and abbreviation, first Lindenstrauss spelling and one fully overstruck Illusie word remain uncertain. Archive number 7; no date, title sheet or page count.']
save(p,tex)
print('Saved',p['filename'],len(p['changes']),'changes;',p['done'])
