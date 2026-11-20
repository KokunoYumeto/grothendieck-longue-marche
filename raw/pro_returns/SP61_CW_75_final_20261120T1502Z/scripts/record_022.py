from reading_support import *
tex=r'''\scanpage{22}
\textcircled{8} \unsure{digression|Digression} sur structures cubiques.

\[
 A\text{ anneau avec }2\ne0,\qquad n\in\mathbb{N}^{*}
\]

$\unsure{C|\mathcal{C}}$ \inserted{cat} modules libres \inserted{$E$} sur $A$, avec \deleted{famille} ens. de \inserted{$n$} sous-modules libres $E_i$ ($i\in I$, $\operatorname{card} I=n$) de somme directe $E$, et chaque $E_i$ muni d'une bi-base $\{e_i,f_i\}$ ($e_i\unsure{+}f_i=0$)

[ou encore, $E$ muni d'une partie $B$ de \inserted{card. $2n$} stable par $x\longmapsto-x$, et telle que un \textendash{} donc tt \textendash{} syst. de représentants de $B/\pm1$ dans $B$ soit une base]

\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=small]
 {}\arrow[d,"\wr"']\\ {}
\end{tikzcd}}
$C'$ cat. des ens \inserted{$B$} de cardinal $2n$ munis d'une rel. d'équivalence \deleted{\unsure{bi à|bi}} à orbites de card. $2$, ou encore muni d'une permutation $\sigma$ involution ($\sigma^{\unsure{2|\prime}}=\mathrm{id}$) sans pt fixe.

\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large]
 C\arrow[r]\& C' \quad\text{évident}\\
 C'\arrow[r]\& C\quad\text{: si }I=\deleted{\unsure{E}}B/\sigma,\ \text{on}
\end{tikzcd}}
considère $E=\bigoplus_{i\in I}E_i$, où $E_i=B_i\wedge_{\{\pm1\}}\deleted{\unsure{B|A}}D$ où $D$ est le $A$-module $A_g$ sur lequel $\pm1$ opère par homothetie
% archive sheet number: 21
'''
save_tex(22,tex)
doubts(22,[('heading','digression','Digression','medium','The small looped initial resembles the lower-case d elsewhere; capitalization is not securely distinguished.'),('first category letter','C','mathcal C','medium','The same cursive category C varies between looped and open forms; alphabet remains uncertain, not a new category.'),('bi-base relation','e_i+f_i=0','the short joining sign is faint','medium','Crop (1236,528,1541,630): the possible plus is crowded into the entry stroke of f; no other legible formula is supplied.'),('cancelled words before à orbites','bi à','bi','low','Crop (1060,1198,1256,1261): b-loop and i dot survive, but the later small loop/accent is crossed.'),('involution exponent','2','prime','medium','Crop (996,1391,1568,1493): raised bent stroke fits his reduced 2, but lacks a full baseline.'),('quotient numerator overwritten letter','E','unidentified old capital','low','Crop (1122,1756,1400,1844): B is live and clear; horizontal older strokes may be E.'),('twist cancelled factor','B','A','low','Crop (1460,1899,1663,2015): overwritten/cancelled capital is congested; live D is retained.')])
changes(22,[
('heading','Digression','Digression (doubtful)','digression | Digression','Top half: initial is a small looped ascending d-like form, unlike the broad D of the lower factor; case not certain.','medium',True,True,'abbreviation expanded or spelling modernised','yes',8,''),
('first category and later occurrences','mathcal C | C, then mixed alphabets','mathcal C throughout','C | mathcal C first; C and C′ thereafter','Halves: looped initial and more open arrow-node C recur for one category; plain C retained provisionally, with alphabet doubt at first occurrence.','medium',True,True,'misread symbol or index','no',1,''),
('inserted cat','cat','cat.','inserted cat','Top half: cat is raised, with no distinct terminal dot.','high',False,True,'abbreviation expanded or spelling modernised','no',8,''),
('E after modules libres','inserted E','E not marked as inserted','inserted E','Top half: E sits above the text baseline, separately inserted after libres.','high',False,True,'insertion or placement','no',6,''),
('n in opening display','mathbb N','bold N','mathbb N','Top half: doubled upright visible in the number-system letter.','high',False,True,'misread symbol or index','no',1,''),
('de card. 2n insertion','only card. 2n inserted','de card. 2n inserted (note)','baseline de, inserted card. 2n','Top half: de remains on the baseline after B; card. 2n is the raised addition.','high',False,True,'insertion or placement','no',6,''),
('vertical arrow decoration','sim | ?','wr','wr','Crop scan 022 (302,996,390,1089): a vertical S-shaped stroke, not a horizontal tilde or a dotted question mark.','high',True,False,'drawing or diagram','no',4,'The arrow is marked as an equivalence, not an authorial question.'),
('ens before inserted B','ens','ens.','ens','Bottom half: no independent dot after the final s.','high',False,True,'abbreviation expanded or spelling modernised','no',8,''),
('cancelled words before à orbites','bi à | bi','struck ill','deleted bi à | bi','Crop scan 022 (1060,1198,1256,1261): b ascender/loop and i dot remain; later loop/accent partially crossed.','low',False,True,'readable ink left as \\ill{}','yes',5,''),
('after permutation sigma','involutive | involutive.','involution','involution','Crop scan 022 (996,1391,1568,1493): ending has t stroke, i dot and low on ending; no v followed by e.','high',True,False,'misread word','no',2,'The source writes the noun involution after permutation, rather than the normalized adjective.'),
('quotient numerator','deleted E then B','B','deleted unsure E then B','Crop scan 022 (1122,1756,1400,1844): B has two live bowls over older horizontal strokes, provisionally E.','low',False,True,'omission','no',7,''),
('twist group position','wedge subscript {±1}','wedge superscript {±1}','wedge subscript {±1}','Crop scan 022 (1460,1899,1663,2015): brace group is below the vertex and below the factor baseline.','high',False,True,'misread symbol or index','no',1,''),
('twist factor','deleted B | A, then D','ellipsis; note of crossed unread symbol','deleted B | A, then D','Crop scan 022 (1460,1899,1663,2015): live outer D curve and stem survive around the cancelled interior; the following où D confirms the locally defined symbol.','medium',False,True,'omission','yes',5,'The contracted product has the written module factor D, not an editorial ellipsis.'),
('last word','homothétie | homothetie','homothéties','homothetie','Crop scan 022 (877,2107,1224,2204): singular ending e, no final s; no separate accent above the e is visible.','high',True,True,'abbreviation expanded or spelling modernised','no',8,'')])
inventory(22,[('text','top','⑧ digression sur structures cubiques.'),('display','below heading','A anneau avec 2≠0, n∈N*'),('text','upper definition','C cat modules libres E ... bi-base'),('insertion','above C definition','cat'),('insertion','after modules libres','E'),('deletion','after avec','famille'),('insertion','before sous-modules','n'),('text','bracketed reformulation','ou encore, E muni ... une base'),('insertion','after B de','card. 2n'),('diagram','between definitions','downward arrow marked wr'),('text','lower definition','C′ cat. des ens B ... sans pt fixe'),('insertion','after ens','B'),('deletion','before à orbites','bi à / bi'),('diagram','lower maps','C→C′ évident; C′→C : si I=B/σ, on'),('deletion','numerator B','old E-like capital'),('text','final construction','considère E=direct sum E_i ... homothetie'),('deletion','before factor D','B/A overwritten capital')])
append_md('SP61_CW_75_notes.md',r'''## Scan 022

Item ⑧ is headed “digression sur structures cubiques” (initial case uncertain). It relates a free A-module with n rank-one summands and opposite generators in each summand to a 2n-element set with a fixed-point-free involution. The inverse construction takes a direct sum of twists of the sign module. No date or authorial page count; pencil archive number 21.

**Mathematics and reading.** The assumption is exactly `2≠0`, not that 2 is invertible. For a basis vector in a free rank-one module this ensures e and −e are distinct; the paired-basis description is checked as S022-PAIR. The word after permutation is the noun “involution,” and the second occurrence of muni is singular despite the earlier munis. Neither agreement is repaired. The exponent of σ is most likely the reduced 2; a small prime-like outline remains an explicit visual doubt. The vertical decoration is a wavy equivalence sign, not an authorial question.

The twist’s group is written below the wedge and its factor D is visible despite an earlier cancelled capital. H’s ellipsis loses this factor. The subscript in A_g is a descending small g, consistent with the additive group interpretation; that interpretation does not change the notation. The construction on objects is checked in S022-PAIR. The page does not spell out the morphisms, so a fully specified equivalence of categories is not asserted as proved here.''')
append_md('SP61_CW_75_doubts.md',r'''### Scan 022 — certainty-only decisions

The cancelled upper word reads famille, the prefix sous- is present, and the bracket reads donc tt and dans B. The lower subscript is g, not capital G. The later D is legible. The small plus in the bi-base relation and the cancelled bi à remain doubtful after their single crops. The reduced exponent of σ is retained as 2 with prime as alternative; H's certainty alone does not settle it.
''')
append_md('SP61_CW_75_hand_log.md',r'''## Added on scan 022

- **A vertical wavy equivalence mark is not a question mark.** The left-hand S-shaped stroke beside the downward arrow has no dot. C's tilde/question alternatives are replaced by wr; this observation concerns this one decoration.
- **A short final on can look like ve.** The page has involution, where C preferred involutive. The i dot and low rounded ending support on; no general replacement of other endings is made.
- **Category C varies in its loop.** The first prose C is more looped than the arrow-node C. One category is meant throughout this page; plain C is used with an explicit alphabet doubt at its first occurrence. This supplements the same caution on scans 018–019.
- **The wedge's group can be very low.** Here {±1} is a subscript, unlike H's superscript. Each actual vertical placement remains separately checked.
''')
checks([('S022-PAIR','targeted proof check','Given a free module with rank-one summands and pairs ±e_i, 2≠0 makes each pair distinct because e_i is a basis vector. Conversely each two-element orbit B_i is a C2-torsor; its contracted product with the additive module A acted on by sign becomes a rank-one A-module after choosing either b_i. The other choice changes the resulting generator by sign, so the unordered pair is intrinsic. Direct sum over B/σ recovers the paired-basis data. This checks the object constructions; morphisms are not specified in the source.')])
assemble();log('scan 022 done')
print(checkpoint_due())
