from save_page import save
tex=r'''
\scanpage{7}
\mspage{5}

\uline{pg60}\quad Je n'ai ps confiance en ``il est immédiat'' de 6.4.
\margin{\figure{\begin{tikzpicture}[baseline=(t.base)]\node[align=left] (t) {c'est pourtant\\trivial};\draw[rotate=25] (0,0) ellipse (1.06 and 0.50);\end{tikzpicture}}}

\uline{pg61, 61 bis} : Je n'ai pas lu.

Il me semble qu'il doit être possible de définir, à isogénie près, des ``parties finies'' et ``parties toriques'', ayant le bon rang --
\margin{\figure{\begin{tikzpicture}[baseline=(t.base)]\node[align=left] (t) {non, mon\\argument\\marche};\draw[rotate=25] (0,0) ellipse (0.91 and 0.63);\draw (1.05,0.70) .. controls (0.66,0.15) and (0.66,-0.25) .. (0.87,-0.36);\end{tikzpicture}}}

\uline{pg\unsure{64|67}/\unsure{bis}} : \deleted{\unsure{voir}} (réf. à Serre pour l'insép. \unsure{de $\ell$} ligne 11 ?)

Un peu malhonnête d'être si bref, car 6.6 est utilisé en 5.13.
\margin{\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) {que faire ?};\draw[rotate=12] (0,0) ellipse (0.65 and 0.31);\end{tikzpicture}}}

\figure{\begin{tikzpicture}\draw (0,0)--(12,0);\draw (0,-0.08)--(12,-0.08);\draw (0,-0.16)--(12,-0.16);\end{tikzpicture}}

\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) {7};\draw (0,0) ellipse (0.27 and 0.25);\end{tikzpicture}}
\uline{p65}.\quad $A_0$ n'est pas défini\margin{si}

\uline{p.67}\quad (7.1.4)\quad français --
\margin{\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) {?};\draw (0,0) ellipse (0.29 and 0.40);\end{tikzpicture}}}

\figure{\begin{tikzpicture}\draw (0,0)--(12,0);\draw (0,-0.08)--(12,-0.08);\draw (0,-0.16)--(12,-0.16);\end{tikzpicture}}

\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) {8};\draw (0,0) ellipse (0.15 and 0.24);\end{tikzpicture}}

\figure{\begin{tikzpicture}\draw (0,0)--(12,0);\draw (0,-0.07)--(12,-0.07);\draw (0,-0.14)--(12,-0.14);\end{tikzpicture}}

\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) {9};\draw (0,0) ellipse (0.16 and 0.25);\end{tikzpicture}}
\uline{p80}\quad 9.2.3\quad $u$ plutôt que $u(\unsure{g|q})$

\uline{p82}\quad (9.3.3)\quad $+$ compatibilité avec $R$ ? --

\uline{p87}\quad 9.4.\quad $S$ \uuline{strictement} hensélien ? (on le suppose en p88, $\ell-9$)

pas d'hyp. d'excellence ?

\uline{p91} : 9.5.8.\quad Ne mettrais-tu pas une génuflexion ``\unsure{au|en} signe près''.

\uline{pg92 bis}\quad $S$ est-il strictement hensélien ?

\figure{\begin{tikzpicture}\draw (0,0)--(12,0);\draw (0,-0.08)--(12,-0.08);\draw (0,-0.16)--(12,-0.16);\end{tikzpicture}}

\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) {10};\draw (0,0) ellipse (0.26 and 0.25);\end{tikzpicture}}
\uline{pg98}\quad 10.5.3.\quad Une extension de $K$ (qui ici est infini) est-elle requise ??

10.5.4.\quad Dire \uline{où} on fera ces vérifications --

\margin{6}
'''
e=[('text','upper right','5'),('text','top pg60','Je n’ai ps confiance'),('margin note','upper left pencil','c’est pourtant trivial'),('drawing','upper left','oval around pencil reply'),('text','upper pg61,61bis','Je n’ai pas lu'),('text','upper paragraph','Il me semble qu’il doit être possible'),('margin note','left beside paragraph','non, mon argument marche'),('drawing','left beside paragraph','oval and curved attachment stroke'),('text','upper pg64/bis','réf. à Serre pour l’insép.'),('deletion','before Serre parenthesis','voir uncertain'),('text','upper last line','Un peu malhonnête d’être si bref'),('margin note','left beside last line','que faire ?'),('drawing','left beside last line','oval around que faire ?'),('drawing','divider before 7','three horizontal strokes'),('drawing','section number','circled 7'),('text','middle p65','A_0 n’est pas défini'),('margin note','right of p65 note','si'),('text','middle p67 (7.1.4)','français'),('margin note','left of p67','?'),('drawing','left of p67','oval around ?'),('drawing','divider before 8','three horizontal strokes'),('drawing','empty section number','circled 8'),('drawing','divider before 9','three horizontal strokes'),('drawing','section number','circled 9'),('text','lower p80','u plutôt que u(g)'),('text','lower p82','+ compatibilité avec R ?'),('text','lower p87','S strictement hensélien ?'),('text','lower following line','pas d’hyp. d’excellence ?'),('text','lower p91','Ne mettrais-tu pas une génuflexion'),('text','lower pg92 bis','S est-il strictement hensélien ?'),('drawing','divider before 10','three horizontal strokes'),('drawing','section number','circled 10'),('text','bottom pg98 10.5.3','Une extension de K'),('text','bottom 10.5.4','Dire où on fera ces vérifications'),('margin note','bottom left pencil','6')]
d=[{'line':'upper reference after finite/toric parts','reading':'pg64/bis','alternatives':'pg67/bis; overwritten digits','confidence':'low'},{'line':'same reference, deletion','reading':'voir','alternatives':'one cancelled word','confidence':'low'},{'line':'Serre parenthesis','reading':'de ell','alternatives':'de l / se l; very compressed','confidence':'low'},{'line':'p80 9.2.3','reading':'u(g)','alternatives':'u(q)','confidence':'medium'},{'line':'p91 9.5.8','reading':'au signe près','alternatives':'en signe près','confidence':'medium'}]
save(7,tex,e,d,'Explicit lack of confidence in “il est immédiat” (6.4), answered “c’est pourtant trivial”; pages 61 and 61bis explicitly unread. Expectation: finite and toric parts up to isogeny of the right ranks; margin “non, mon argument marche”. Request for Serre reference concerning inseparability; brevity of 6.6 questioned because used in 5.13. Hypotheses: strict henselianity / excellence; compatibility with R; sign ambiguity in 9.5.8; unnecessary extension of infinite K? Request to state where verifications of 10.5.4 will be done. Section 8 carries a heading but no accompanying text; preserve as empty section, not missing transcription.')
