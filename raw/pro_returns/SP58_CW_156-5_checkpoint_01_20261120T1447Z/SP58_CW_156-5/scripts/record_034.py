from records import commit
tex=r'''\cotefile{156-5}
\scanpage{34}\mspage{33}
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small]
I' \arrow[d,"\varphi"',"\text{surj.}"] \& \hookleftarrow \& J'=\varphi^{-1}(J)\arrow[d] \& \& I'^{*}\arrow[d,"{\varphi^{*}=\varphi\mid I'^{*}}"]\\
I \& \hookleftarrow \& J\ \text{partie f.} \& \text{d'où} \& I^{*} \& \begin{gathered}\text{\deleted{\unsure{croiss.|surj.}}}\\ \text{surjectif}\end{gathered}
\end{tikzcd}}

et on a
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large]
U\arrow[r,"p'","\text{surj}"']\arrow[rr,bend right=23,"p" description,"\text{surj}"'] \& I'^{*}\arrow[r,"\varphi^{*}","\text{surj}"'] \& I^{*}
\end{tikzcd}}
% slanted
\margin{Attention, $\varphi^{*}$ bijectif n'implique pas néc. $\varphi^{*}$ iso !!! Mais $=$ on suppose $\varphi^{*}$ iso, ça n'implique pas a), cf plus bas.}
les \deleted{$A$} strates ouvertes de $F'$ qui sont \deleted{dans} \inserted{$\subset$} $U$ (i.e. pour \deleted{dans} $\in G'$) sont les fibres de $U\xrightarrow{p'}\unsure{I^{*\alpha}|I^{**}|I'^{*}}$, les strates ouvertes de $F$ qui sont $\subset U$ (i.e. pour $\in G$) sont les fibres de $U\xrightarrow{p}I^{*}$.

La condition b) dit que $\varphi^{*}$ est bijective,
La condition c) dit que les \deleted{\unsure{s}}fibres de $p$ (ce sont les $A^\circ$ pour $A\in F\setminus G$) sont des fibres pour $p'$. C'est \deleted{éq} visiblement équivalent.

\deleted{D'autre part,}

D'autre part, que dit d) ? Notons \inserted{(on l'a \unsure{pr. entre|prouvé} pour $F'\ll F$)\deleted{$A\in F$})} que pour $A\in F$\deleted{\illegible{1}}, on a $A\in F'$ sss $A^{\circ(F)}$ est une strate ouverte de $F'$ (cf lemme déjà prouvé, \inserted{qu'on donnera} plus bas). Donc d) dit que pour $\forall\,A_i\in F\setminus G=I^{*}$, \deleted{\unsure{j}} la \inserted{$F$-}strate $p^{-1}(\{\deleted{\unsure{A}}i\})$\inserted{$\subset U$} est une \inserted{$F'$-}strate \deleted{de $p$} de $U$. Donc cela \unsure{équiv. à visiblement à|équiv. visiblement à} $p$ bijectif.

Donc on a
\[b\Longleftrightarrow c\Longleftrightarrow d\]

Montrons que c'est équiv. à a. Soit

\deleted{$F''$ comme ds a), d'où $I''$, et sur} \deleted{\unsure{$S=|F$}}

\deleted{$S=|F|=|F'|=|F''|$, on a}

\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,execute at end picture={\draw (\tikzcdmatrixname-1-1.north west) -- (\tikzcdmatrixname-2-1.south west); \draw (\tikzcdmatrixname-1-2.north west) -- (\tikzcdmatrixname-2-2.south east); \draw (\tikzcdmatrixname-1-3.north east) -- (\tikzcdmatrixname-2-3.south east);}]
\deleted{S}\arrow[r]\arrow[d]\arrow[rr,bend left=18,"\deleted{\varphi}"] \& \deleted{I''}\arrow[r,"\deleted{\varphi''}"]\arrow[d] \& \deleted{I}\arrow[d]\\
\deleted{|G'|=|G|=T}\arrow[r] \& \deleted{\unsure{J''|J'}}\arrow[r] \& \deleted{J}
\end{tikzcd}}
'''
# place, C, H, final, physical evidence, H-kind, confidence, against C, against H, H doubt, consequential note
changes=[
('top square, horizontal maps',r'\hookleftarrow (upper doubtful)',r'headless line labelled \supset',r'\hookleftarrow in both rows','034 crop top_arrows (460,55,860,270): the right end returns upward as a hook; upper left end is an arrowhead, lower left end retraced.','drawing or diagram','high',False,True,False,''),
('upper right cancelled word',r'\unsure{croiss.|surj.}','bijectif.',r'\deleted{\unsure{croiss.|surj.}}','034 crop crossed_word (1425,130,1650,290): rounded opening, joined short uprights and two terminal curves; no secure bijectif sequence. Overstrike partly merges the first letters.','misread word','low',False,True,False,''),
('slanted margin, first sentence','Attention, φ* bijectif n’implique pas néc. φ* iso !!!','Attention, φ* bijectif, φ* pas néc. iso !!!','Attention, φ* bijectif n’implique pas néc. φ* iso !!!','034 crop margin (18,350,570,1570), rotated −47°: n’implique is written across the upper right of the note; next line continues pas néc.','omission','high',False,True,False,''),
('slanted margin, second sentence',r'Mais \unsure{si|=} on suppose φ* iso, ça n’implique pas a), cf plus bas.','Mais on va supposer φ* iso, [ill.] [ill.] plus bas.','Mais = on suppose φ* iso, ça n’implique pas a), cf plus bas.','Same margin crop: two parallel horizontal strokes after Mais; on suppose, ça n’implique pas a), cf are readable.','readable ink left as \\ill{}','high',True,True,True,'The marginal objection explicitly says that even an isomorphism φ* does not imply a).'),
('first stratum parenthesis, cancelled word',r'\deleted{\unsure{dans}}','omitted',r'\deleted{dans}','034 crop strata (270,495,1620,850): a short word beginning d is crossed by a horizontal stroke immediately before ∈G′.','omission','high',False,True,False,''),
('first stratum parenthesis, membership',r'\in\unsure{G\prime|G_1\prime}',r'\in F\prime\setminus G\prime',r'\in G\prime','Same strata crop: a small ∈ followed directly by G and one high prime; there is no F′ or difference sign.','misread symbol or index','high',False,True,False,'Keep ∈G′ as written despite the complementary-stratum context; H supplies F′∖G′.'),
('first inline p′ target',r'I^{\unsure{*\alpha|**}}',r'I\prime{}^*',r'\unsure{I^{*\alpha}|I^{**}|I\prime{}^*}','Same strata crop: two crowded raised shapes after I; the second curls back on itself. Its identity remains unresolved.','misread symbol or index','low',False,True,False,''),
('second stratum parenthesis',r'\in G',r'\notin G',r'\in G','Same strata crop: open membership curve with middle bar, without a diagonal negation stroke.','misread symbol or index','high',False,True,False,'Keep the second ∈G; do not replace it by the mathematically expected nonmembership.'),
('condition c), before fibres',r'\deleted{\unsure{s}}','omitted',r'\deleted{\unsure{s}}','Upper half, y930–1025: a small s-like abandoned start is overwritten at the left of fibres.','omission','low',False,True,False,''),
('condition c), before visiblement',r'\deleted{\unsure{éq}}','omitted',r'\deleted{éq}','Upper half, y1090–1160: éq is visible between C’est and visiblement and is cancelled.','omission','medium',False,True,False,''),
('insertion above Notons que, opening',r'on l’a \unsure{pr. entre|prouvé} pour F′≪F','On a vu [ill.] que pour F′≪F',r'on l’a \unsure{pr. entre|prouvé} pour F′≪F','034 crop insertion (1160,1155,1660,1310): on l’a and pour are visible, the abbreviated middle remains ambiguous. A surrounding connector attaches the addition before que.','misread word','low',False,True,True,''),
('same insertion, cancelled ending',r'\deleted{\unsure{et là}}',r'\struck{\ill{}}',r'\deleted{$A\in F$}','Same insertion crop: diagonal-legged A, membership curve and clear F survive beneath the strike; followed by a closing parenthesis.','misread symbol or index','medium',True,True,True,''),
('criterion A∈F′', 'sss','ssi','sss','Lower half, y1345–1400: three repeated s-shaped curves; no final dotted upright.','abbreviation expanded or spelling modernised','high',False,True,False,''),
('lemma parenthesis, interlinear continuation',r'\inserted{qu’on donnera}',r'qui \uncertain{sera donné}',r'\inserted{qu’on donnera}','034 crop donnera (220,1440,665,1605): qu’on followed by donnera, written above plus bas with an insertion curve.','misread word','high',False,True,True,''),
('after I*, before la strate',r'\deleted{\unsure{j}}','omitted',r'\deleted{\unsure{j}}','034 crop inverse_image (670,1490,1655,1755): isolated upright/descender with a cancelling touch before la. Letter remains uncertain.','omission','low',False,True,False,''),
('inverse-image argument',r'p^{-1}(\{\deleted{\unsure{A}}i\})',r'p^{-1}(i)',r'p^{-1}(\{\deleted{\unsure{A}}i\})','Same inverse_image crop: braces inside the parentheses, a crowded cancelled A-like letter, and an i put above it with dot.','omission','medium',False,True,False,''),
('before de U',r'\deleted{\unsure{de p}}','omitted',r'\deleted{de $p$}','Lower half and crop p_bijectif (290,1720,685,1850), upper edge: de p is crossed by a heavy horizontal stroke; following de U is live.','omission','medium',False,True,False,''),
('line before p bijectif',r'\unsure{équiv. à visiblmt|équiv. visiblement à}','équivaut visiblement [ill.]',r'\unsure{équiv. à visiblement à|équiv. visiblement à}','034 crop inverse_image (670,1490,1655,1755): abbreviated équiv., a small possibly abandoned à, the long visiblement, and a final à; the first à remains doubtful.','abbreviation expanded or spelling modernised','medium',True,True,True,''),
('p bijectif', 'live p bijectif','p bijectif said to be biffé','live p bijectif','034 crop p_bijectif (290,1720,685,1850): the long curves belong to j and f; no separate stroke cancels the expression.','deletion state (struck given live or live given struck)','high',False,True,True,'The text itself says p bijectif, apparently for φ* bijectif; the slip is retained.'),
('cancelled foot, comme ds a)',r'comme \unsure{ds} a)','comme dans a)','comme ds a)','034 crop cancelled_footer (290,1880,1635,2060): the short d–s form has no intervening an.','abbreviation expanded or spelling modernised','high',False,True,False,''),
('cancelled foot, after I″',r'\unsure{df} sur',r'et \uncertain{soit}','et sur','Same cancelled_footer crop: small looped e then crossed upright t; following sur ends with a rising curve, not the t of soit.','misread word','high',True,True,True,''),
('cancelled equality, continuation','on a','omitted','on a','Lower half just above bottom diagram: on a follows the equality on the same crossed line.','omission','high',False,True,False,''),
('cancelled bottom diagram, vertical arrows','downward','upward hooks','downward arrows','Whole page and lower half: all three vertical shafts terminate in downward points above T, J″ and J.','drawing or diagram','high',False,True,False,'The cancelled factorisation diagram has downward vertical maps, as drawn.')]
inv=[('text','top centre','33'),('diagram','top','I′, J′=φ⁻¹(J); I, J; φ*'),('deletion','top right','croiss./surj.'),('text','upper','et on a'),('diagram','upper','U → I′* → I*; p′, φ*, p'),('margin note','left, slanted','Attention, φ* bijectif'),('text','upper middle','les A strates ouvertes de F′'),('deletion','same paragraph','A; dans; dans'),('insertion','above sont ... U','⊂'),('text','middle','La condition b) ... La condition c)'),('deletion','condition c)','s; éq'),('deletion','middle','D’autre part,'),('text','lower middle','D’autre part, que dit d) ?'),('insertion','above Notons que','on l’a pr. ... pour F′≪F'),('deletion','in insertion','A∈F'),('deletion','after A∈F','one unreadable word'),('insertion','lemma parenthesis','qu’on donnera'),('insertion','stratum sentence','F-; ⊂U; F′-'),('deletion','stratum sentence','j; A in inverse image; de p'),('display','lower','b ⇔ c ⇔ d'),('text','lower','Montrons que c’est équiv. à a. Soit'),('deletion','foot','F″ comme ds a) ... et sur; S=|F'),('deletion','foot','S=|F|=|F′|=|F″|, on a'),('diagram','foot, cancelled','S → I″ → I; |G′|=|G|=T → J″ → J')]
notes='''### 034-N1 — What the page does

Continues the equivalence of conditions b), c), d) for strata over the complement, with surjections U → I′* → I*. It begins a comparison with a), then cancels the factorisation argument at the foot. The slanted note warns: “Attention, φ* bijectif n’implique pas néc. φ* iso !!!” and “Mais = on suppose φ* iso, ça n’implique pas a), cf plus bas.” This is an explicit objection, not a completed proof of a).

### 034-N2 — Mathematics that directed inspection

The fibres in U concern the complement of G, so the two parenthetical ∈G′ and ∈G were checked particularly closely. They are membership signs in the ink and remain unchanged; H’s complement/nonmembership readings would repair the argument. Similarly the conclusion really reads “p bijectif” and is not struck: the relevant bijectivity in the preceding two conditions is that of φ*, so this appears to be a slip. No extra prime is supplied in the crowded first inline target. These observations diagnose a mismatch; they are not a proof of the unquoted preceding proposition.

A targeted set-theoretic check: for surjections p′:U→I′* and φ*:I′*→I*, with p=φ*∘p′, every p-fibre is a p′-fibre iff φ* is injective, hence bijective. If φ*(x)=φ*(y), choose preimages of x,y under p′; equality of the relevant fibre with one p′-fibre forces x=y. The converse follows by taking inverse images of singleton fibres. This verifies only the equivalence as formulated in this page’s b), c) discussion, independently of the mistaken ∈ parentheticals.

Pagination: manuscript 33. No date, title sheet or page total on this scan.'''
doubts=r'''### Remaining readings

| Place | Reading | Alternatives | Confidence |
|---|---|---|---|
| cancelled top-right word | croiss. | surj. | low |
| first p′ target | I^{*\alpha} | I^{**}; I′* | low |
| cancelled start before fibres | s | no secure longer reading | low |
| interlinear note | pr. entre | prouvé | low |
| after A∈F | \illegible{1}, cancelled | no defensible letters through hatching | low |
| before la F-strate | cancelled j | a discarded pen start | low |
| inverse-image argument | cancelled A, then i | underlying letter uncertain | low |
| final equivalence sentence | équiv. à visiblement à | équiv. visiblement à | medium |
| separately cancelled S=|F | S=|F | incomplete ending | low |
| bottom diagram | J″ | J′ | low |

C certainty-only decisions: the hook, d’où, Attention, néc., cancelled A, strates, both cancelled dans, G′ (no subscript 1), cancelled éq, Notons, superscript (F), cancelled de p, cela without accent, and ds are resolved from the halves/crops; the ten remaining loci above stay marked. The equals sign, cancelled A∈F, phrase at the final equivalence and et sur have substantive records in the changes log. All 28 entries of C’s scan-034 doubt register were addressed; compound loci are grouped here.

Slips retained: ∈G′, ∈G and p bijectif; see 034-N2.'''
hand='''The raised star is commonly a small angular k-like mark (I*, I′*, φ*) rather than a symmetric asterisk. It holds at the clear occurrences on this sheet; the crowded inline target has an additional unresolved mark. I has heavy top and bottom bars, while J has a left-curved foot: the apparent doubled stroke on the upper J′ is retracing, not evidence for a separate alphabet. Both witnesses retain ordinary capitals. The shorthand = after “Mais” consists of two horizontal strokes and stands where “même” would read naturally; C offered si and H omitted it. The long descenders of j and f can resemble a cancellation: H took the live “p bijectif” as struck. These are page-local observations to compare on subsequent sheets.'''
commit(34,tex,changes,inv,notes,doubts,hand,notation='I, J and their primes; F, G and their primes; φ with a looped descending stem; p has a compact bowl and descender. Superscript * is angular; ° is a small open circle. Hooked inclusions and plain arrows are distinct. Quotation convention not yet exemplified.',abbr='surj. = surjectif; partie f. = partie fermée; néc. = nécessairement; iso = isomorphisme/isomorphe; cf = confer; sss = si et seulement si; équiv. = équivalent; ds = dans; = in prose probably même.',checks=[('034-N2-fibres','targeted proof check','Verified the elementary equivalence between singleton φ*-fibres and the p/p′ fibre condition, assuming the displayed surjections; does not validate a).')])
