from reading_support import *
tex=r'''
\scanpage{17}
sur $E$ invariante par $G$ est transportée sur $F$.

(Ex : structures de groupe, d'anneau, de module sur un anneau fixé, d'espace top. etc ...)

Cas de plusieurs ens de base $(E_i)_{i\in I}$ \deleted{\unsure{$E$ muni}} muni d'une structure mixte (p.ex. module $E$ sur anneau $A$, $G$ opère sur $(A,E)$) alors $({\scriptstyle\unsure{1|\prime}}{}^{\unsure{P|\overline P}}\!E_i)_{i\in I}$ sont munis de la structure correspondante.

\deleted{\uline{\unsure{NB}}}

\uline{\deleted{\unsure{M}}Applications}\quad \deleted{\unsure{Méth.|Mét.}}\inserted{\tikz[baseline=(n.base)]\node[draw,circle,inner sep=1.2pt] (n) {1};} Yoga : structures isomorphes : Une \inserted{str} donnée $E$ $\longleftrightarrow$ torseurs sous $G=\operatorname{Aut}(E)$

\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=1.1em,column sep=1.15em]
F \arrow[r,maps to] \& \operatorname{Isom}_{\mathcal C}(E,F)=\overline P\\
{}^{P}\!E=P\times_G E \& P \arrow[l,maps to]
\end{tikzcd}}

\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=1.15em,row sep=.4em]
F \arrow[r,maps to] \& P^{\unsure{\cdots}}\arrow[d,dash]\arrow[r,maps to] \& P\times_G E\arrow[r,"{\overset{?}{\sim}}"] \& F\\
\& \operatorname{Isom}_{\mathcal C}(E,F) \& \&
\end{tikzcd}}

\[
\begin{aligned}
P\times E&\longrightarrow F\\
\operatorname{Isom}(E,F)\times E&\mathbin{\text{---}} F
  & (u,x)&\ \unsure{\mathrel{\vdash\!\!-\!\dashv}|\longmapsto}\ u(x)\\
&& (ug)(x)&=u(gx)\qquad\text{ok}
\end{aligned}
\]

\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=.65em,column sep=.85em]
P\arrow[r] \& F=P\times_G E\arrow[r,maps to] \& \operatorname{Isom}_{\mathcal C}(E,F) \& P\arrow[l,"\sim"']\\
\& \& i_u:x\longmapsto u*x \& \unsure{u|x}\arrow[l,maps to]
\end{tikzcd}}

\[
\deleted{(ug}\,i_{ug}=i_u.g\qquad\text{i.e.}\quad ug*x=u*gx\quad\text{ok}
\]
% archive sheet number: 16
'''
save_tex(17,tex)
doubts(17,[
('first family, deletion',r'\deleted{\unsure{$E$ muni}}','ending partly struck','low','E and low m/u/i strokes survive, but the strike hides the medial letters.'),
('second family, isolated small stroke',r'\unsure{1|\prime}','prime; residual pen stroke','low','A separate hooked upright remains before the raised P; its role cannot be established from this sheet.'),
('second family, recurring cap on P',r'\unsure{P|\overline P}','barred P','medium','The cap touches the loop here; the first Isom result has a definitely detached bar, preserved separately.'),
('cancelled heading marks',r'\deleted{\uline{\unsure{NB}}}; \deleted{\unsure{M}}; \deleted{\unsure{Méth.|Mét.}}','Mét. for Méth.','low','The cancellations leave only parts of the original letters.'),
('above P in middle composite',r'P^{\unsure{\cdots}}','faint residual strokes','low','Several tiny separated marks have no recoverable letter sequence.'),
('evaluation element connector',r'\unsure{\mathrel{\vdash\!\!-\!\dashv}|\longmapsto}','mapsto','medium','A short vertical nub closes the horizontal line; no complete arrowhead is visible.'),
('last element assignment, source',r'\unsure{u|x}','x','low','The heavy letter has intersecting strokes; target i_u favours u but does not settle the ink.')])
changes(17,[
('opening continuation','est transportée','se transporte','est transportée','Upper half: est precedes transportée; a final accented e is visible.','high',False,True,'misread word','no','2',''),
('family paragraph, abbreviation','ens','ens.','ens','Upper half: no dot follows the low ens before de base.','high',False,True,'abbreviation expanded or spelling modernised','no','8',''),
('family paragraph, cancellation',r'\deleted{\unsure{$E$ muni}}',r'\struck{\ill{}}',r'\deleted{\unsure{$E$ muni}}','Scan 017 crop (1315, 373, 1630, 493): the three bars of E remain above the low struck word; parts of muni survive.','low',False,True,r'readable ink left as \ill{}','yes','5',''),
('family paragraph, agreement',r'\unsure{muni|munis}','munis','muni','Scan 017 crop (300, 469, 1040, 561): the word ends with the dotted i and no trailing s.','high',False,True,'misread word','no','2','The singular-looking muni is retained with the plural family, despite the later sont munis.'),
('mixed structure example','G opère sur (A,E)','le couple (A,E)','G opère sur (A,E)','Upper half: capital G, descending p of opère and short sur precede the parenthesized pair.','high',False,True,'misread word','no','2','Restores the stated group action on the pair, omitted by the alternative reading.'),
('second family, extra stroke',r'{\scriptstyle\unsure{1|\prime}}{}^{\unsure{P|\overline P|T}}E_i',r'{}^P E_i',r'{\scriptstyle\unsure{1|\prime}}{}^{\unsure{P|\overline P}}E_i','Scan 017 crop (520, 660, 765, 785): an isolated hooked upright is distinct from the large opening parenthesis and the P.','low',False,True,'omission','no','3',''),
('cancelled NB',r'\deleted{\uline{\unsure{NB}}}',r'\struck{\ill{}}',r'\deleted{\uline{\unsure{NB}}}','Scan 017 crop (430, 761, 1120, 1178): a final B-like double loop and an underline survive the crossing strokes.','low',False,True,r'readable ink left as \ill{}','yes','5',''),
('Applications initial overtyping',r'\deleted{\unsure{M}}Applications','Applications',r'\deleted{\unsure{M}}Applications','Scan 017 crop (430, 761, 1120, 1178): angled M-like strokes remain inside the live A.','low',False,True,'omission','no','3',''),
('heading, cancelled word',r'\deleted{\unsure{Méth.|Mét.}}',r'\struck{\ill{}}',r'\deleted{\unsure{Méth.|Mét.}}','Scan 017 crop (430, 761, 1120, 1178): initial M and a tall medial stem survive; ending remains uncertain.','low',False,True,r'readable ink left as \ill{}','yes','5',''),
('Yoga, structured object','Une \\inserted{\\unsure{str}} donnée E',r'\uncertain{les} (\uncertain{str}) données E',r'Une \inserted{str} donnée E','Scan 017 crop (430, 761, 1120, 1178), plus upper half: large U starts Une; donnée has no plural s; the raised str is attached by a curved insertion stroke, without literal parentheses.','high',False,True,'misread word','yes','2',''),
('first Isom subscript',r'\unsure{e|C|G|\mathcal C}',r'\mathcal C',r'\mathcal C','Scan 017 crop (756, 1296, 1246, 1428): outer C curve ends at lower right; the inward top curl makes it resemble e. The two later category subscripts are open versions of this sign.','medium',True,False,'misread symbol or index','no','1','Reads the repeated category subscript consistently as calligraphic C, not an isolated e.'),
('first Isom result',r'\unsure{\overline P|P}','P',r'\overline P','Scan 017 crop (756, 1296, 1246, 1428): white space separates the horizontal bar from the P loop.','high',False,True,'misread symbol or index','no','1',''),
('reverse construction, twist',r'{}^P E','P_E',r'{}^P E','Lower half: P is raised to the left of E, not a baseline P with E subscript.','high',False,True,'misread symbol or index','no','1','Restores left superscript notation for the twisted object.'),
('reverse construction, arrow',r'P\longmapsto {}^P E','left arrow without source bar','leftward mapsto from P','Lower half: arrowhead at the left and a short vertical bar at the right end.','high',False,True,'drawing or diagram','no','4',''),
('middle composite, marks above P',r'P^{\unsure{\cdots}}','omitted',r'P^{\unsure{\cdots}}','Scan 017 crop (380, 1588, 795, 1759): faint but real raised marks remain above and to the right of P.','low',False,True,'omission','no','3',''),
('middle composite, Isom subscript','C',r'\mathcal C',r'\mathcal C','Scan 017 crop (380, 1588, 795, 1759): small open curved C, read with the curled first occurrence as one recurring category notation.','medium',True,False,'misread symbol or index','no','1',''),
('evaluation, object connector','Isom(E,F)×E --- F',r'\operatorname{Isom}(E,F)\times E\to F','Isom(E,F)×E --- F','Lower half and scan 017 crop (934, 1827, 1648, 2017): a simple horizontal stroke ends without an arrowhead.','high',False,True,'misread symbol or index','no','1',''),
('evaluation, element connector',r'\unsure{\vdash--\dashv|\longmapsto}',r'\longmapsto',r'\unsure{\vdash--\dashv|\longmapsto}','Scan 017 crop (934, 1827, 1648, 2017): transverse strokes at both ends; a reduced arrowhead remains a possible alternative.','medium',False,True,'misread symbol or index','no','1',''),
('lower composite, Isom subscript','C',r'\mathcal C',r'\mathcal C','Lower half: the same open category C below Isom is used a third time; no G downstroke.','medium',True,False,'misread symbol or index','no','1',''),
('last element assignment, connector','leftward mapsto',r'\longleftrightarrow','leftward mapsto','Scan 017 crop (801, 2127, 1340, 2307): open arrowhead on the left; the short right stroke is a vertical source bar.','high',False,True,'drawing or diagram','no','4',''),
('final cancelled attempt',r'\deleted{\unsure{(ug}}',r'\struck{i_{ug}}',r'\deleted{(ug}','Scan 017 crop (801, 2127, 1340, 2307): opening parenthesis and baseline ug are crossed; no initial dotted i.','high',False,True,'misread symbol or index','no','1','')])
inventory(17,[('text','top continuation','sur E invariante par G est transportée sur F'),('text','top examples','Ex : structures de groupe ... espace top.'),('text','upper paragraph','Cas de plusieurs ens de base ... correspondante'),('deletion','right after first family','E muni'),('deletion','above heading','underlined NB'),('text','middle heading','Applications; circled 1; Yoga ... Aut(E)'),('deletion','inside Applications initial','M beneath A'),('deletion','beside heading','Méth. / Mét.'),('insertion','above cancelled heading word','circled 1'),('insertion','above donnée','str'),('diagram','first two assignments','F maps to Isom_C(E,F); P maps to {}^P E'),('diagram','middle composite','F to P to P×G E to F; Isom_C label below P; ? over tilde'),('display','evaluation block','P×E→F; Isom(E,F)×E---F; (u,x) connector u(x); (ug)(x)=u(gx) ok'),('diagram','bottom composite','P to F to Isom_C(E,F) from P; i_u element assignment'),('display','lowest equality','i_ug=i_u.g; ug*x=u*gx ok'),('deletion','before lowest equality','(ug')])
append_md('SP61_CW_75_notes.md',r'''## Scan 017

The opening completes scan 016’s corollary: a G-invariant structure on E is transported to F. Examples include group, ring, module and topological structures; the extension to several underlying sets uses a mixed structure. “Applications”, circled 1, “Yoga” introduces the correspondence between structures isomorphic to E and torsors under `G=Aut(E)`. No date or page count; pencil archive number 16.

**Mathematics and reading.** The first Isom subscript has an inward curl that looks like e, while the two later copies are open C forms. The repeated category role and matching curves justify reading the three as `\mathcal C`; the alphabet choice is medium confidence. The return object is `{}^P E`, with P above and left, rather than H’s `P_E`. The written singular “muni” is preserved. A hooked stroke before the twisted family remains unassigned (`1|prime`) instead of being silently removed. A detached bar above the first Isom result is explicit; the broad attached caps elsewhere remain a separate paleographic doubt.

**Checks on the page.** The map `P×_G E→F` carries a source question mark over its isomorphism sign. The next calculation `(ug)(x)=u(gx)` ends “ok”; it makes evaluation well defined on the contracted product. The final `i_{ug}=i_u.g`, explained as `ug*x=u*gx`, also ends “ok”. Both identities were checked directly in this run (S017-EVAL, S017-I). They support the two constructions, but do not justify replacing plain or bar-ended drawn connectors with ordinary arrows.
''')
append_md('SP61_CW_75_doubts.md',r'''### Scan 017 — notation and certainty decisions

`\mathcal C` is the repeated category subscript on the three Isom expressions. Its first form curls inward like e; subsequent forms are open. The first Isom result has a detached bar, so it is `\overline P`; attached broad-cap P forms retain the page’s initial doubt. The left superscript is P, not T. C’s muni is resolved without a final s; raised str is clear; `(ug)(x)` has x; the middle F-to-P connector has a reduced but visible head and source bar; the final cancelled `(ug` is legible. The seven remaining doubt loci are retained in remaining_doubts.tsv. These certainty-only decisions do not create change rows.
''')
append_md('SP61_CW_75_hand_log.md',r'''## Added on scan 017

- **Curled category C.** The first Isom subscript has a strongly inward upper curl and can look like e; the next two are open. Across these three occurrences the notation is read `\mathcal C`. C’s first candidate was e, and its two later forms were plain C; H consistently supplied calligraphic C. This is an interpretation of the recurrent letter, not a silent correction of an isolated e.
- **P caps are not uniformly separable.** One bar above P is detached at the first Isom result; all other caps on scans 016–017 touch or nearly touch the letter. The one clear bar is retained explicitly. The P/barred-P ambiguity of the other forms is not claimed to be settled.
- **Cursive x can look like n.** In `(u,x)` and `(ug)(x)` the first crossing stroke is rounded; the clearer x in `u(x)` and `gx` fixes the repeated variable. This holds in the evaluation block only, not as a universal substitution. C marked `(ug)(x)` doubtful; both witnesses read x in the ordered pair.
- **Source bars versus arrowheads.** The leftward assignment to i_u has a straight transverse source bar at right, not a second arrowhead. H made it bidirectional. The evaluation connector has a small closing nub instead of a clear arrowhead and remains doubtful.
''')
checks([('S017-EVAL','targeted proof check','Evaluation [u,x]↦u(x) respects (ug,x)~(u,gx) because (ug)(x)=u(gx). With a chosen isomorphism E→F it is bijective. This checks the questioned evaluation isomorphism in the stated G=Aut(E) setting.'),('S017-I','targeted proof check','For i_u(x)=[u,x], i_ug(x)=[ug,x]=[u,gx]=(i_u.g)(x); thus u↦i_u is G-equivariant. After choosing a torsor element it is a bijection onto Isom(E,P×_G E).')])
assemble();log('scan 017 done')
