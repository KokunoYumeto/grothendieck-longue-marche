from reading_support import *
save_tex(25,r'''\scanpage{25}
\uline{Orientations}

a) Vectoriel réel $E$ de dim finie $n$. La donnée de $E$ équivaut à celle du torseur à dr.
\[
 P=\operatorname{Isom}(\mathbb R^n,E)\simeq\operatorname{bases}(E)
\]
sous
\[
 G=\operatorname{Gl}(n,\mathbb R).
\]

On a un hom
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small]
 G=\operatorname{Gl}(n,\deleted{\unsure{R|k}}\mathbb R)\arrow[rr,"s"]\arrow[dr,"\det"']
 \& {} \& \{\pm1\} \& u\longmapsto\deleted{\det}\,\operatorname{sgn}\det u\\
 {} \& \mathbb R^{\ast}\arrow[ur,"\operatorname{sgn}"'] \& {}
 \& \text{noyau }\operatorname{Gl}^+(n,\mathbb R)\,,
\end{tikzcd}}
et
\[
 \omega_E=P\times_G\{\pm1,s\}\simeq P/\operatorname{Gl}^+(n,R)
\]
est l'ens des orientations de $E$.

b) Module \inserted{\unsure{quadratique|quadratiques}} libre \deleted{\unsure{quadr.|point}} \inserted{$E$} sur un anneau comm. $k$ \unsure{(où|où} $2$ est inversible [$\exists$ base orthonormale, $\deleted{\unsure{Q(e_i,e|Q(e_i,e_j)}} e_i^2=1$, $e_i e_j=0$ si $i\ne j$]

La donnée de $E$ de rang $n$ équivaut à celle du tors à droite
\[
 P=\operatorname{Isom}_{k\text{-quadr.}}(k^n,E)\simeq\text{bases orthon.}(E)
\]
sous
\[
 G=\operatorname{O}(n,k)=\operatorname{Aut}_{k\text{-quadr}}(k^n,Q_n)\subset\operatorname{Gl}(n\unsure{.|,}k)
\]

\unsure{Or|On} ici
\[
 G=\operatorname{O}(n,k)\xrightarrow{\substack{\det=s\\\unsure{\deleted{\operatorname{sgn}}}}}\{\pm1\}\qquad(\text{noyau }\operatorname{SO}(n,k))
\]
et l'ens des orientations de $E$ est (par définition)
\[
 \omega_E=P\times_G(\pm1,s)\simeq P/\operatorname{SO}(n,k).
\]

\uline{Compatibilité} \uline{entre a) et b)} Résulte de la transitivité de l'opération d'ext. du groupe d'opérateurs dans un torseur, et du diagramme comm.
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large]
 \operatorname{O}(n,k)\arrow[r,hook,"\mathrm{incl}"]\arrow[rr,bend right=19,"\det"] \& \operatorname{Gl}(n,k)\arrow[r,"\operatorname{sgn}\det"] \& \{\pm1\}
\end{tikzcd}}
% archive sheet number: 24
''')
doubts(25,[('top diagram overwritten scalar','R','k','low','Crop (635,496,684,565): earlier strokes intersect the live double-stem R; old R versus k remains uncertain.'),('inserted adjective in b)','quadratique','quadratiques','medium','Crop (462,864,735,924): last flourish could include s, although Module and libre are visibly singular.'),('cancelled word under E','quadr.','point','low','Crop (611,912,738,1000): long descender and later ascender survive, but the medial strokes are buried.'),('before 2 est inversible','(où','où','medium','Crop (1447,909,1514,973): a long curved initial joins the o; separate opening parenthesis is plausible, with no round closer visible.'),('cancelled quadratic formula','Q(e_i,e','Q(e_i,e_j','low','Crop (1111,985,1281,1049): Q, opening bracket and two e-like letters survive; final index is not securely present.'),('Gl inclusion arguments','n.k','n,k','medium','Crop (1460,1331,1649,1416): a small round low mark between n and k, without a secure descending comma stroke.'),('before orthogonal determinant','Or','On','medium','Crop (274,1462,440,1523): short shoulder after O could be r or n; sentence does not settle the glyph.'),('below det=s label','possible deleted sgn','ink smear without recoverable characters','low','Crop (811,1498,942,1562): small partly crossed-looking group below the live label and above the shaft; tentative sgn is explicitly doubtful, including its status as deleted text.')])
changes(25,[
('a), dim','dim','dim.','dim','Top half: no separate stop after the abbreviation.','high',False,True,'abbreviation expanded or spelling modernised','no',8,''),
('real scalars, repeated','double-stem R except plain final quotient R','bold R throughout','mathbb R where doubled; plain R in first quotient','Top half: duplicated stems distinguish the real-number glyphs; the R in P/Gl⁺(n,R) has a single stem.','high',False,True,'misread symbol or index','no',1,''),
('before top diagram','hom','hom.','hom','Top half: word ends after m without an independent point.','high',False,True,'abbreviation expanded or spelling modernised','no',8,''),
('top diagram source scalar','deleted R | k then mathbb R','mathbb R only','deleted R | k then mathbb R','Crop scan 025 (635,496,684,565): crossed older diagonal/loop within the live double-stem R.','low',False,True,'omission','no',7,''),
('first orientation sentence','ens','ens.','ens','Top half: no independent terminal period after ens.','high',False,True,'abbreviation expanded or spelling modernised','no',8,''),
('b), opening number','Module ... libre','Modules ... libres','Module ... libre','Top half: both baseline words end without s. The raised adjective has a separately doubtful ending.','high',False,True,'misread word','no',2,''),
('b), raised adjective','quadratique | quadratiques','quadratiques','quadratique | quadratiques','Crop scan 025 (462,864,735,924): final low flourish cannot securely be called a plural s; it is attached by the insertion guide above libre.','medium',False,True,'misread word','no',2,''),
('b), old word before E','deleted quadr. | point','deleted ill','deleted quadr. | point','Crop scan 025 (611,912,738,1000): first descender, later upright and short terminal stroke survive through the strike.','low',False,True,'readable ink left as \\ill{}','yes',5,''),
('b), où','(où | où','où','(où | où','Crop scan 025 (1447,909,1514,973): tall left opening curve is distinct above the small o loop; no matching closer is supplied.','medium',False,True,'omission','no',3,''),
('cancelled quadratic expression','Q(e_i,e | Q(e_i,e_j','deleted ill','Q(e_i,e | Q(e_i,e_j','Crop scan 025 (1111,985,1281,1049): readable Q, opening round bracket and e groups; rightmost index remains obscured.','low',False,True,'readable ink left as \\ill{}','yes',5,''),
('after orthonormality bracket','no period','period','no period','Top half: the square bracket closes against the edge without a separate dot.','high',False,True,'text not on the page','no',9,''),
('before quadratic frame display','tors','tors.','tors','Halves overlap: no dot between tors and à droite.','high',False,True,'abbreviation expanded or spelling modernised','no',8,''),
('Aut subscript','k-quadr','k-quadr.','k-quadr','Bottom half: unlike the Isom qualifier above, this qualifier has no independent terminal point.','high',False,True,'abbreviation expanded or spelling modernised','no',8,''),
('Gl inclusion arguments','n comma | period k','n,k','n period | comma k','Crop scan 025 (1460,1331,1649,1416): low rounded point, no secure comma tail.','medium',True,True,'misread symbol or index','no',1,''),
('below orthogonal det=s','no earlier label','no earlier label','unsure deleted sgn','Crop scan 025 (811,1498,942,1562): a short dark group with small curves lies between det=s and the shaft. Possibly an earlier sgn; possibly smear. Both text and cancellation status remain explicitly doubtful.','low',True,True,'omission','no',3,''),
('second orientation sentence','ens','ens.','ens','Bottom half: no terminal stop after ens.','high',False,True,'abbreviation expanded or spelling modernised','no',8,''),
('par définition','parenthesized','not parenthesized','(par définition)','Bottom half: a leading upright/curve before par and round closer after définition.','high',False,True,'omission','no',3,''),
('compatibility heading','underlined in two spans','italic phrase','underlined Compatibilité and entre a) et b)','Bottom half: two distinct horizontal underline segments; same words retained.','high',False,True,'other','no',10,'')])
inventory(25,[('text','heading','Orientations'),('text','a) opening','Vectoriel réel E de dim finie n ... dr.'),('display','first frames','P=Isom(R^n,E) ≃ bases(E)'),('text','before G','sous'),('display','first group','G=Gl(n,R)'),('text','above triangle','On a un hom'),('diagram','top triangle','G=Gl(n,R)→{±1}; det via R* then sgn'),('deletion','triangle source scalar','old R/k'),('display','right of triangle','u mapsto deleted det sgn det u; noyau Gl⁺'),('deletion','after u mapsto','det'),('text','before quotient','et'),('display','first orientation set','ω_E=P×_G{±1,s} ≃ P/Gl⁺(n,R)'),('text','under first quotient','est l’ens des orientations de E'),('text','b) opening','Module quadratique libre E ... inversible'),('insertion','above libre','quadratique(s)'),('deletion','under E','quadr./point'),('insertion','before sur','E'),('text','bracket','exists base orthonormale ... i≠j'),('deletion','bracket formula','Q(e_i,e ...'),('text','before second frames','La donnée de E de rang n ... à droite'),('display','quadratic frames','P=Isom_k-quadr.(k^n,E) ≃ bases orthon.(E)'),('text','before orthogonal group','sous'),('display','orthogonal group','G=O(n,k)=Aut_k-quadr(k^n,Q_n) subset Gl(n,k)'),('text','before determinant','Or/On ici'),('display','determinant','G=O(n,k)→{±1}, det=s; noyau SO(n,k)'),('deletion','possible prior arrow label','unsure sgn, possibly smear'),('text','before second quotient','et l’ens des orientations de E est (par définition)'),('display','second orientation set','ω_E=P×_G(±1,s) ≃ P/SO(n,k)'),('text','bottom explanation','Compatibilité entre a) et b) ... diagramme comm.'),('diagram','bottom','O(n,k) hook to Gl(n,k), sgn det to {±1}, curved det arrow')])
append_md('SP61_CW_75_notes.md',r'''## Scan 025

The underlined heading is “Orientations.” Part a) uses the frame torsor of a real vector space and sign of determinant. Part b) treats a free quadratic module over a commutative ring with 2 invertible and writes an orthonormal-basis condition. It defines orientations through determinant and the special orthogonal subgroup. The final paragraph claims compatibility by extension of the operator group and a diagram. No date or authorial page count; pencil archive number 24.

**Mathematics and reading.** The upper diagram has R* with a star, a cancelled det before the live sgn det, and an overwritten scalar at its source. The first orientation formula uses braces {±1,s}; the second uses parentheses (±1,s). The last subscript ω_E is E: its short bottom arm is visible in the crop. The final diagram really has k at both groups and sgn det on its second arrow; k is not replaced by R to make the diagram meaningful.

S025-REAL checks the usual real, positive-rank formula. In b), an orthonormal basis is an additional written condition; it does not follow just from 2 being invertible (for example, the one-dimensional quadratic form 2x² over Q has no unit vector in Q). The page's map to the literal two-element group {±1} needs a restriction or interpretation: over k=R×R an orthogonal determinant can be (1,−1). S025-RING records this counterexample, and S025-MU2 records the correct determinant target. The compatibility diagram is checked only after specializing to R (S025-COMPAT); no sign homomorphism on an arbitrary commutative ring is supplied.

The possible old sgn under det=s is extremely insecure: the page is smudged at that formula. It is retained with an explicit doubt covering both the reading and its apparent cancellation. The possible opening parenthesis before où is not completed by an invented closing parenthesis. The reduced two-mark à in the prose resembles the doubtful mark on scan 024; the second reading will compare these occurrences as one handwriting habit.''')
append_md('SP61_CW_75_doubts.md',r'''### Scan 025 — certainty-only decisions

The top scalar exponent is an asterisk, the cancelled word after u mapsto is det, and the detached mark below noyau is a comma. The second orientation subscript is E with a short but real bottom arm. Both bottom-diagram coefficient letters are k. The adjective ending, old word under E, old Q expression, possible opening parenthesis, Or/On, and inclusion separator remain doubtful. The small possible prior arrow label is the least secure new reading on this page.
''')
append_md('SP61_CW_75_hand_log.md',r'''## Added on scan 025

- **E may have a very short bottom arm.** The second ω_E initially resembles ω_F, but the crop shows a third arm. The upper ω_E has a more rounded form. Neither is replaced by F on grammatical expectation alone.
- **Punctuation on abbreviations is not automatic.** Dim, hom, ens, tors and the Aut qualifier quadr have no separate stop here; Isom's quadr. and bases orthon. do. H regularly adds stops. The same caution applies across the run.
- **Two detached ticks can stand for à.** The à before celle and before direction words is reduced almost to an accent and short lower stroke. This recurring form is relevant to the uncertainty on scan 024; it is not a rule for every pair of dots.
- **A smudge can imitate an earlier label.** The small dark group beneath det=s may be a cancelled sgn, but that is not certain. It is not used to infer a general cancellation habit.
''')
checks([('S025-REAL','targeted proof check','For n≥1 and a real n-dimensional vector space E, the frame set P is a right GL_n(R)-torsor by precomposition. Sign of determinant is a surjective homomorphism with kernel GL_n^+(R). For any surjective homomorphism G→H, P×_G H identifies with P/ker via [p,h]↦p g ker for a lift g of h. Thus the displayed two-element orientation torsor equals the quotient. Positive rank is used for surjectivity; no n>0 is inserted into the source.'),('S025-ORTHONORMAL','targeted proof check','The bracket is read as an additional existence condition. Invertibility of 2 alone does not imply it: for Q with form q(x)=2x², q(x)=1 would require a rational square root of 1/2, impossible by the parity argument for sqrt(2). This observation does not turn the manuscript bracket into a claim of automatic existence.'),('S025-RING','refuted, with the refined statement\'s id','Literal assertion det:O(n,k)→the two global values {1,−1} for arbitrary commutative k with 2 invertible is false. For k=R×R and n=1, u=(1,−1) satisfies u²=1, so u is orthogonal, but its determinant is neither global 1=(1,1) nor global −1=(−1,−1). Refined statement: S025-MU2.'),('S025-MU2','targeted proof check','From A^t A=I over a commutative ring, determinant gives det(A)²=1. Thus determinant lands in mu_2(k), with kernel det=1, the special orthogonal group. If the ring is connected and 2 is invertible, any u²=1 gives the idempotent (1+u)/2, hence u=±1. Alternatively {±1} may be intended as a group-scheme/sheaf notation; the page does not specify such an interpretation.'),('S025-COMPAT','targeted proof check','For k=R and A orthogonal, det A is ±1, so sgn(det A)=det A. This verifies the bottom triangle in that specialization. Extension of torsors is associative by the balanced-product map [[p,g],h]↦[p,gh], already checked as S020-ASSOC. The page writes k, and the general-ring sign arrow is not defined by the supplied text.')])
assemble();log('scan 025 done')
print(checkpoint_due())
