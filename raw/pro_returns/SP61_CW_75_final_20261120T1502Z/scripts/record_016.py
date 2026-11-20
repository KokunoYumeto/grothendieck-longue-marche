from reading_support import *
tex=r'''
\scanpage{16}
Polygône régulier (ou réalisation régulière d'un polygône combinatoire) : définitions possibles (cotés égaux, angles égaux, \inserted{\deleted{\unsure{il avait|il y avait|il suffit}} les deux,} transitivité groupe des symétries ...) Existence, unicité modulo homothétie : tout isom. combinatoire est induit par une unique similitude.

\figure{\begin{tikzpicture}[x=.8cm,y=.8cm]
\draw (0,0) -- (1.14,.66);
\draw (1.18,.70) -- (1.55,1.97);
\end{tikzpicture}}

Notion d'enveloppe affine (ou vectorielle) d'un polygône combinatoire ... sens précisé

Fonctorialité de $\overline{\underline{X\times_G Y\quad\text{p.r. à }(G,X,Y)}}$ ...

\[
\begin{aligned}
\unsure{P|\overline{P}}\times_G E={}^{P}\!\deleted{B}E=F
&\qquad\qquad &P&\quad G\text{-torseur}\\
&&E&\quad G\text{-ensemble}
\end{aligned}
\]

$P\longrightarrow\operatorname{Bij}(E,F)$ compatible aux opérations de $G$ à droite

\uline{NB} Si $G$ opère fidèlement sur $E$, $G$ opère ``sans pts fixes'' sur $\operatorname{Bij}(E,F)$ --- i.e. $\deleted{\unsure{y}}u.g=u$ $(g\in G,\ x\in B)$ implique $g=1$, ou encore les $G_u$ $(u\in B)$ sont réduits à $\{1\}$, ou encore $B$ est une somme de torseurs ... Dans ce cas\inserted{ et dans ce cas seulement}, $P\mathbin{\text{---}}\operatorname{Bij}(E,F)$ est injectif

\[
P\hookrightarrow\operatorname{Bij}(E,F)
\]

% slanted; the brace joins this label to the large bracket below.
\margin{$(G,E)$-structure\\sur un $F$\\\deleted{\illegible{1}}}
\noindent$\left[\begin{minipage}{.84\linewidth}
En tous les cas, $F\inserted{={}^{P}\!E}$ est muni de la structure suivante : donnée d'une orbite de $G$ dans $\operatorname{Bij}(E,F)$.
\end{minipage}\right.$

{\footnotesize [On verra que (si $G$ opère $\text{fid}^{\mathrm{t}}$ sur $E$) la donnée d'un \deleted{\unsure{ens|d'un}} \deleted{\unsure{$(G,E)$-st}} $F$ avec $(G,E)$-structure \unsure{équivaut à|équiv. à} celle d'un \unsure{$G$-torseur} \unsure{et applic$^{\mathrm{tn}}$}.]}

\uline{Corollaire} \unsure{de|du} $\unsure{\big[\,\mathbin{\text{---}}|\big[\,\longrightarrow}$ \unsure{toute structure}
% archive sheet number: 15
'''
save_tex(16,tex)
doubts(16,[
('definition, interlinear cancellation',r'\deleted{\unsure{il avait|il y avait|il suffit}}','il y avait; il suffit','low','The horizontal strike removes the medial strokes. The exposed ending is closer to -ait than -fit; no complete verb is recoverable.'),
('first product and recurring torsor letter',r'\unsure{P|\overline{P}}','barred P','medium','The broad horizontal cap may belong to the letter P; no T reading is retained because a lower loop is visible. This will be compared with later occurrences.'),
('NB, overwritten variable',r'\deleted{\unsure{y}}','unrecoverable older letter','low','A hooked descender remains below the live u.'),
('left margin below brace',r'\deleted{\illegible{1}}','—','low','Several intersecting strokes obliterate one cancelled word even in the rotated crop.'),
('foot addition, two deletions',r'\deleted{\unsure{ens|d\'un}} \deleted{\unsure{$(G,E)$-st}}',"d’un for the first; longer structure ending for the second",'low','Two crossed levels overlap the next baseline.'),
('foot addition, equivalence',r'\unsure{équivaut à|équiv. à}','équiv. à','low','The underlined Corollaire crosses the ending.'),
('foot addition, terminal words',r'\unsure{$G$-torseur} \unsure{et applic$^{\mathrm{tn}}$}','exact ending on applic uncertain','low','The final lower line and the corollary overlap.'),
('bottom corollary',r'\unsure{de|du} $\unsure{\big[\,\mathbin{\text{---}}|\big[\,\longrightarrow}$ \unsure{toute structure}','du; bracket plus arrow','low','The large corollary line runs beneath the foot addition; the introductory sign remains uncertain.')])
rows=[
('opening word','Polygône','Polygone','Polygône','Upper half: a short circumflex lies over the o.','high',False,True,'abbreviation expanded or spelling modernised','no','8',''),
('opening parenthesis, polygon','polygône','polygone','polygône','Upper half: the raised angular mark is retained.','high',False,True,'abbreviation expanded or spelling modernised','no','8',''),
('definition, cotés',r'\unsure{cotés|côtés}','côtés','cotés','Scan 016 crop (235, 165, 1616, 321): accent on é; no separate circumflex over o.','high',False,True,'abbreviation expanded or spelling modernised','no','8',''),
('definition, cancelled insertion',r'\deleted{\unsure{il suffit|il faut|il y avait}}',r'\struck{\ill{}}',r'\deleted{\unsure{il avait|il y avait|il suffit}}','Scan 016 crop (235, 165, 1616, 321): initial il and ending -ait survive; the strike obscures the middle. The insertion attaches after angles égaux.','low',True,True,r'readable ink left as \ill{}','yes','5',''),
('definition, group name','symétries','similitudes','symétries','Upper half: after sy the tall medial stroke and ending -tries fit symétries, without the successive stems of similitudes.','high',False,True,'misread word','no','2','The transitivity condition concerns the symmetry group, not the group of similitudes.'),
('uniqueness, abbreviation','isom.','isomorphisme','isom.','Upper half: short isom followed by a dot; the expanded ending is absent.','high',False,True,'abbreviation expanded or spelling modernised','no','8',''),
('left angle sketch','two separated segments','two segments joined at V','two separated segments','Whole image and upper half: a small white gap separates the two stroke ends; H drawing 01-5 joins them.','high',False,True,'drawing or diagram','no','4',''),
('envelope paragraph, polygon','polygône','polygone','polygône','Upper half: the raised mark above the o is present.','high',False,True,'abbreviation expanded or spelling modernised','no','8',''),
('envelope paragraph, last words',r'\unsure{sens} précisé',r'\uncertain{sans} précision','sens précisé','Scan 016 crop (1130, 672, 1540, 772): first word has e-like closed loop; last word ends in accented é, without -ion.','high',False,True,'misread word','yes','2',''),
('functoriality, phrase',r'\unsure{p.r.} à','par :','p.r. à','Upper half: the two abbreviated letters are separated by dots; the following a has a grave accent.','high',False,True,'abbreviation expanded or spelling modernised','no','8',''),
('functoriality, horizontal lines','separate rules above and below paragraph','emphasis over complete phrase','overline and underline around the product/triple expression','Upper half: two horizontal strokes bound the mathematical phrase; Fonctorialité de is to their left.','high',True,True,'other','no','10',''),
('product, overwritten letter',r'{}^P\deleted{\unsure{B}}E','{}^P E',r'{}^P\deleted{B}E','Scan 016 crop (224, 910, 750, 1033): two rounded chambers of B survive under the three long live bars of E.','high',False,True,'omission','no','3',''),
('equivariant map, final phrase','à droite',': droite','à droite','Upper half: a small grave accent belongs to the a, not a colon.','high',False,True,'misread word','no','2',''),
('NB, quotation marks',"``sans pts fixes\'\'",'« sans pts fixes »',"``sans pts fixes\'\'",'Lower half: small paired strokes, not guillemet chevrons.','high',False,True,'other','no','10',''),
('NB, equation',r'\deleted{\unsure{y}}\unsure{x|y}.g=\unsure{x|u}','u.g=u',r'\deleted{\unsure{y}}u.g=u','Scan 016 crop (570, 1434, 1500, 1623): both live variables have two rising stems and a trough; the old hooked descender survives under the first.','medium',True,True,'deletion state (struck given live or live given struck)','no','7','The live equation uses u while the following parenthesis clearly retains x; the mismatch is preserved.'),
('NB, parenthetical membership','x\\in B',r'u\in\operatorname{Bij}(E,F)',r'x\in B','Scan 016 crop (570, 1434, 1500, 1623): a distinctly crossed x and a single capital B; Bij(E,F) is absent at this place.','high',False,True,'misread symbol or index','no','1','Retains the actual bound-variable mismatch and the short symbol B.'),
('NB, stabilizers',r'G_x\ (x\in B)',r'G_u\ (u\in B)',r'G_u\ (u\in B)','Scan 016 crop (570, 1434, 1500, 1623): the subscript and parenthetical variable are low undulating u forms, distinct from the crossed x above.','medium',True,False,'misread symbol or index','no','1','Stabilizers are written with subscript u on this line.'),
('NB, first connective','ou encore','on a donc','ou encore','Lower half and action crop: ou followed by separated e-n-core strokes.','high',False,True,'misread word','no','2',''),
('NB, reduction phrase','sont réduits à',r'\ill{} :','sont réduits à','Lower half: sont at the end of one line; réduits and à begin the next.','high',False,True,r'readable ink left as \ill{}','yes','5',''),
('NB, second connective','ou encore',r'\ill{}','ou encore','Lower half: the same connective recurs after {1}.','high',False,True,r'readable ink left as \ill{}','yes','5',''),
('NB, decomposition','somme',r'\ill{}','somme','Lower half: s followed by two low humps and final e before de torseurs.','high',False,True,r'readable ink left as \ill{}','yes','5',''),
('NB, map before est injectif','P --- Bij(E,F)',r'P\to\operatorname{Bij}(E,F)','P --- Bij(E,F)','Lower half: the horizontal connector has no arrowhead, unlike both the earlier arrow and the hook below.','high',False,True,'misread symbol or index','no','1',''),
('margin, second line','sur ens F','sur un F','sur un F','Scan 016 crop (25, 1720, 435, 2076), rotated -25 degrees: short two-hump un with final upturn; no initial e and terminal s.','high',True,False,'misread word','no','2',''),
('margin, cancelled word',r'\deleted{\illegible{1}}','omitted',r'\deleted{\illegible{1}}','Scan 016 crop (25, 1720, 435, 2076): cancellation is present beneath the brace; its ink is physically obscured.','low',False,True,'omission','no','3',''),
('bracketed paragraph, opening and structure',r'En tous les cas, F\inserted{={}^P E} est muni de la structure suivante',r'F={}^P E \uncertain{est} muni de 2 structures; E -- dans les cas, F\ill{}',r'En tous les cas, F\inserted{={}^P E} est muni de la structure suivante','Scan 016 crop (226, 2030, 1638, 2199), plus lower half: the inserted ={}^P E sits above the baseline; a continuous sentence reads En tous les cas ... la structure suivante. The curl in la resembles 2 but is a word.','high',False,True,'insertion or placement','yes','6','There is one specified orbit structure; the apparent numeral 2 is la.'),
('foot addition, fid abbreviation',r'\unsure{\text{fid}^{\mathrm t}}','fid.',r'\text{fid}^{\mathrm t}','Scan 016 crop (738, 2188, 1658, 2333): a small raised t stands after fid.','medium',False,True,'abbreviation expanded or spelling modernised','no','8',''),
('foot addition, deleted levels and F',r"d'un \deleted{\unsure{ens|d'un}} \deleted{\unsure{$(G,E)$-st}} \unsure{F} avec",r"\struck{d'une $(G,E)$ \uncertain{structure}} \ill{} d'une",r"d'un \deleted{\unsure{ens|d'un}} \deleted{\unsure{$(G,E)$-st}} F avec",'Scan 016 crop (738, 2188, 1658, 2333): d’un remains live; two separate struck levels precede a clearly tall F and the word avec.','low',False,True,'deletion state (struck given live or live given struck)','yes','7',''),
('foot addition, final equivalence',r"\unsure{équivaut à|équiv. à} celle d'un \unsure{$G$-torseur} \unsure{et applic$^{\mathrm{tn}}$}",r"\ill{} équivaut à celle d'un torseur sous \uncertain{G} \ill{} \ill{}",r"\unsure{équivaut à|équiv. à} celle d'un \unsure{$G$-torseur} \unsure{et applic$^{\mathrm{tn}}$}",'Scan 016 crop (738, 2188, 1658, 2333): the G precedes the torsor word; et and applic with a raised ending are visible at right. Overlap prevents complete certainty.','low',False,True,r'readable ink left as \ill{}','yes','5',''),
('lowest line, corollary',r'\uline{Corollaire} \unsure{de|du} [--- \unsure{toute structure}','omitted',r'\uline{Corollaire} \unsure{de|du} [--- \unsure{toute structure}','Scan 016 crop (738, 2188, 1658, 2333): the larger underlined word Corollaire has its own baseline beneath the addition; following strokes continue the sentence at the foot.','low',False,True,'omission','no','3','')]
changes(16,rows)
inventory(16,[
('text','top','Polygône régulier ... unique similitude'),('insertion','above definition, after angles égaux','les deux,'),('deletion','start of interlinear insertion','il avait / il y avait / il suffit'),('drawing','left beside opening paragraph','two segments with small gap'),('text','upper middle',"Notion d’enveloppe affine ... sens précisé"),('text','upper middle, between horizontal strokes','Fonctorialité de X×G Y p.r. à (G,X,Y)'),('display','above fold','P×G E = {}^P E = F; P G-torseur; E G-ensemble'),('deletion','within displayed product','B overwritten by E'),('text','at fold','P→Bij(E,F) compatible aux opérations de G à droite'),('text','lower half','NB Si G opère fidèlement ... injectif'),('deletion','NB equation','older y under live u'),('insertion','above end of NB','et dans ce cas seulement'),('display','below NB','P hookrightarrow Bij(E,F)'),('margin note','lower left, slanted','(G,E)-structure sur un F'),('deletion','below marginal brace','one obscured word'),('text','bracket at foot','En tous les cas ... donnée d’une orbite'),('insertion','above F in bracket','={}^P E'),('text','small bracket at bottom','On verra que ... et applic raised tn'),('deletion','small bracket, first crossed level','ens / d’un'),('deletion','small bracket, second crossed level','(G,E)-st'),('text','lowest line','Corollaire de [--- toute structure')])
append_md('SP61_CW_75_notes.md',r'''## Scan 016

The opening discusses definitions and uniqueness of a regular polygon, then proposes an affine or vector envelope. The page turns to the contracted product and its map to `Bij(E,F)`, followed by the free action criterion and a description of a `(G,E)`-structure as a G-orbit of bijections. Title/topic: “Polygône régulier (ou réalisation régulière d’un polygône combinatoire)”; no authorial date or page count. Pencil archive number 15.

**Mathematics and reading.** In the NB, injectivity of a bijection u implies that `u.g=u` precisely when g lies in the kernel of the action on E; hence a faithful action gives a free action on the bijections. This short proof was checked (S016-NB). It supports the sense of “somme de torseurs”, but the actual words were read from the image. The displayed equation uses u, the parenthesis has a clearly crossed x, and the stabilizer line returns to u; this is preserved, not repaired. H’s “2 structures” would conflict with the following singular “suivante”; the crop independently shows the handwritten word “la”. The source’s capital B is retained even though H expands it to `Bij(E,F)`.

**Authorial reservation.** The small note begins “On verra que (si G opère fidᵗ sur E)”; its promised equivalence is not proved on this page. The final clause is crowded into the separate underlined corollary line and remains partly doubtful. No missing requirement is supplied from the expected torsor statement.''')
append_md('SP61_CW_75_doubts.md',r'''| P (possible barred form) | Broad cap and small lower loop in the standalone torsor letter; ordinary loop in left superscript. Initial unresolved `P|\overline P`; T excluded. | 016, product, map and key |
| Twisting | Left superscript P on E, right subscript G on the product; no prime or exclamation. | 016, product and insertion |
| u and x | u has a trough and rising stems; x in the parenthesis has crossed strokes. Preserve their local difference. | 016, NB |
| G, E, F, B | Plain capitals, not script or double-struck; older B is overwritten by E in the product. | 016 |
| Quotations | Two opening and two closing short strokes: ``sans pts fixes''. | 016, NB |

### Scan 016 — certainty-only decisions

C’s cotés, sens, p.r., G in the triple, G after Si, overwritten B, fidᵗ and the live F in the footnote are resolved in the forms printed in the page file. The cap on P remains unresolved; T is excluded by the visible loop. C’s bottom verb, terminal clause, corollary sign, two foot deletions, and obscured marginal cancellation remain doubtful. The older y in the NB remains doubtful. These certainty-only changes are not counted as substantive differences.
''')
append_md('SP61_CW_75_hand_log.md',r'''## Established on scan 016

- **Wide cap on P.** The standalone torsor letter has a long horizontal head and a low loop, unlike the ordinary small superscript P. It holds at the product, map, key and hook on this page. A bar versus an extended letter stroke remains open; C proposed P/barred P/T, H used P. T is excluded by the loop. Later pages must decide whether there is a distinct notation.
- **u can resemble a flattened x.** The NB has live u in `u.g=u` and the stabilizer line, while the first membership parenthesis has a clear crossed x. This is not a universal substitution: the two shapes coexist. C preferred x throughout; H read u but expanded the membership expression. Places: NB equation and `G_u (u∈B)`.
- **la resembles 2.** The tall joined l-a in “de la structure” has the silhouette of a numeral 2. It is a single occurrence here; H read “2 structures” and displaced the sentence.
- **Compressed words can retain only their ends.** In the foot addition, the middle of équivaut and the raised ending on applic overlap the corollary. This habit does not settle those readings. Both witnesses lose certainty here.
''')
checks([('S016-NB','targeted proof check','For a bijection u:E→F, u∘g=u iff g acts identically on E; thus the induced action on Bij(E,F) is free iff the action on E is faithful, provided Bij(E,F) is nonempty. This checks the NB’s setting where F is a torsor twist. The u/x inconsistency is preserved.')])
assemble();log('scan 016 done')
