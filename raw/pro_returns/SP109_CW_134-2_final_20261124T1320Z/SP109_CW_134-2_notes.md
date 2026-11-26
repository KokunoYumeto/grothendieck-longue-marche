# Notes while reading

These notes concern only the supplied scans. Descriptions of claims do not certify those claims. Check events distinguish actual checks from statements merely carried as background.

## Sheets, headings and dates

The seventeen supplied scans reproduce seventeen handwritten sheets of mathematical discussion addressed to a correspondent. They are archive scans 153–169, with an apparent manuscript foliation from 8 to 24. Most folio numbers are clear, but scan 160 reads 15 with 16 retained as an alternative; the upper portions of the numbers read as 17 on scan 162 and 20 on scan 165 are clipped. This gives a sequence of seventeen folio positions, with those three readings explicitly marked as uncertain. The number 10 on scan 155 is clear; the upper part of its enclosing mark is clipped.

No composition date, signature, title sheet, or explicit statement of the total number of pages is visible in this selection. The following table records the headings and structural divisions actually present, together with short descriptions where there is no heading. There are no typescript sheets, letters by another writer, or administrative lists in this selection.

| Scan | Manuscript folio | Heading or structural division |
| --- | --- | --- |
| 153 | 8 | “Remarques”, items 1) and 2) |
| 154 | 9 | Item 3), inserted 4), B), and a cancelled doubtful C) |
| 155 | 10; enclosing mark partly clipped | C); construction of a complex of generalized Jacobians |
| 156 | 11 | Continuation of C), with a marginal universal-map discussion |
| 157 | 12 | Continuation of C), then D) |
| 158 | 13 | Continuation of D): global duality and the positive-characteristic curve case |
| 159 | 14 | Continuation of D): Serre duality |
| 160 | 15 or 16; 15 preferred | Continuation of D): boxed duality formula and “shift” annotation |
| 161 | 16 | Continuation of D): reductions and class-field interpretation |
| 162 | 17, uncertain and clipped | Continuation of D): Lang duality, arithmetic formula and exact triangle |
| 163 | 18 | E), “Corps de classes local” as a duality formula |
| 164 | 19 | “Remarques”, followed by a marker read a, with e or alpha alternatives |
| 165 | 20, uncertain and clipped | Continuation of the preceding remark, then b) and c) |
| 166 | 21 | d); (F), “Portée et limites de la topologie” fppf |
| 167 | 22 | Continuation of (F): crystalline comparison and slopes |
| 168 | 23 | Continuation of (F), then the correspondent’s question 7° |
| 169 | 24 | Continuation of the homotopy discussion and a triangle of objects |

Scan 154 recalls “Vers la fin des années 50” and inserts “(ou début des 60 ?)”. These are the author’s tentative dates for a recollection, not composition dates for the present sheets. Scan 155 refers to “le livre de Serre” and “son article sur le sujet” without supplying titles. Those works were not consulted. Other named results, lectures and writings are likewise reported from these pages; no external research was undertaken.

The supplied instructions identify the paper watermark as “EXTRA STRONG”. Watermark fragments, show-through and pale background specks are paper matter rather than manuscript text. No lost wording is reconstructed from them or from the continuity of the argument.

## Scope of the notes and checks

The page entries distinguish what the manuscript states or proposes from what this run actually checked. Describing a proposed duality, recalling an attributed theorem or reading its symbols is not a proof check. No duality theorem, construction or conjectural extension was independently proved here. The author’s qualifications are quoted in French; explanatory notes are in English.

Local notation checks identify ambiguous allographs only where the same page or an adjacent continuation fixes the object: for example the coefficient letter F, residue field k, fraction field K, degree i, or fundamental-group pi. They do not replace a clearly different authorial letter. Distinct plain and doubled R forms, visible primes, overwritten signs, incomplete delimiters and grammatical irregularities remain as written. Places are identified by item, paragraph, formula or manuscript line where available.

Four limited formal calculations are recorded in `local_consistency_checks.json`: complementary degrees on scan 158, addition of the geometric and Lang shifts on scan 162, addition of the local geometric and Lang shifts on scan 164, and the slope-interval contrast on scan 167. They assume the manuscript’s formulas and bounds and check only their arithmetic consistency. The identification of Ext degree zero with Hom on scans 159–160 is a notation-convention check, not a proof of either claimed duality. `CHECK_EVENTS.tsv` records the individual events and their actual scope.


## Scan 153

The opening interprets $f^!(\Lambda_e)$ as a singular-chain complex on $X$ and $Rf_!(f^!\Lambda_e)$ as homology over $e$. Remark 1 says that no truncation is needed in any dimension. Remark 2 links this interpretation to biduality with dualizing complexes; for an autodual or Gorenstein coefficient such as $\mathbb Z/n\mathbb Z$, it proposes $K_e=\Lambda$ and $K_X=f^!(K_e)$.

**Reading and checks.** The opening $f:X$–$\operatorname{Spec}k=e$ supplies the local base notation, but does not establish a complete arrowhead. The separator between $K_e$ and $K_X$ remains a dash/punctuation/possible left-arrow ambiguity rather than an inferred map. The inner coefficient in $Rf_!(f^!\Lambda_e)$ retains its plain/doubled-Lambda uncertainty. At the clipped last line, the recurring coefficient notation supports Lambda rather than A, but the fragment remains marked. In remark 2, the ending favours singular “coefficient” although “les” and “envisagés” call for the plural; both readings remain. The page also says “du p\textsuperscript{t} de vue philosophie”, without the letters needed for “philosophique”. Neither grammar nor the duality interpretation supplies missing ink or balances the uncertain parentheses.

**Author’s qualifications.** The claim is framed “au moins du p\textsuperscript{t} de vue philosophie”, “du moins sous réserve de résolution des singularités”, and “mais Deligne m'a dit je crois qu'il sait le prouver sans ça”. The insertion retains the unresolved “sous|sans” before “condition de ‘constructibilité’”; its content is not settled from what a biduality theorem ought to require. These assertions were read for notation, not proved.

## Scan 154

Item 3 extends the discussion to coefficients such as $\mathbb Z_\ell$. Inserted item 4 proposes relative homology $\underline H_{*X/S}=Rf_!f^!(\Lambda_S)$ under cohomological local-triviality hypotheses, with a smooth morphism as an example. Section B discusses Artin–Mazur autoduality of a relative Jacobian and its use in a component-group duality statement for Néron models. The last paragraph begins a recollection of a Serre course.

**Reading and checks.** In item 3, the looped e-like coefficient subscript has a crossing foot and is identified as ell by the local coefficient-ring notation: $\mathbb Z_\ell$, not a newly introduced $\mathbb Z_e$. In item 4 and the final paragraph, the lowered and raised exclamation marks are read separately as $f_!$ and $f^!$. The map from $X$ to $S$ has a right terminal return without a secure full head, so its uncertainty remains despite the intended morphism. The cancelled digit before live SGA 7 remains a doubtful 3; the reference does not restore obscured strokes. The clipped final names and Jacobian ending remain marked.

**Author’s qualifications and date.** He writes “non publiée je crains !” about Jouanolou’s thesis, “Il faut les consulter pour les résultats précis”, “peut-être cela marche dès que”, and “en tous cas c'est OK”. The recollection is dated “Vers la fin des années 50” with the insertion “(ou début des 60 ?)”, not a composition date. None of the attributed results or references was independently verified.

## Scan 155

The page recalls cohomological formulations of class-field theory, intended to reduce an arithmetic base or residue field $k$ to the geometric case $\bar k$ by descent. It mentions correspondence with Serre and three proposed directions involving generalized residues and local generalized Jacobians. Section C explicitly starts with $X$ of finite type over $k$ and proposes a complex $J_{*X/k}$ of generalized Jacobians of length $\dim X$.

**Reading and checks.** In the descent paragraph the second base-field symbol has a separate bar; the text is not harmonized to two unbarred fields. In C), the star, $X/k$ and field letter all lie below the principal $J$. These local roles helped track the symbols but did not test the existence or descent assertions. The compressed inserted adjective before “(voir le livre de Serre)” remains “géométrique” with shorter alternatives; the expected terminology does not supply its concealed middle letters.

**Author’s qualifications and references.** About the letters he writes “je ne sais si j'en retrouverai des copies” and “je me rappelle”; about the programmes, “je ne suis jamais parvenu, malgré de nombreux essais, à accrocher une bonne volonté”. The page cites “le livre de Serre” and “son article sur le sujet” without titles. Neither was consulted. The folio is 10, with only the enclosing mark partly clipped.

## Scan 156

The recalled $J_*$ is a complex of proalgebraic groups over $k$, affine except for $J_0$, whose abelian part is related to the Albanese. A marginal continuation describes a universal map $X\to\underline H_0$ and, for connected $X$, an extension of $\mathbb Z$ by a connected proalgebraic group. The body proposes construction through local schemes and writes $H^i(X,G_X)\simeq\mathbb{E}\mathrm{xt}^i(J_{*X/k},G)$, then revises the coefficient and topology restrictions.

**Reading and checks.** In the display, the dotted superscript is $i$, the doubled E is visible, and the starred $J$ index names the complex. In the later construction clause, a live dotted $i$ overwrites an uncertain star-like earlier index; it is not replaced by the display’s star. The next page’s reference to $(*)$ does not resolve this page’s overwritten formula label, still alpha)/a)/(*). The marginal opening is physically lost and has no defensible word count. The final “sig-” remains incomplete. These are notation and correction-state readings, not a verification of the Ext identity.

**Author’s qualifications.** They include “si je me rappelle bien”, “Il est possible qu'en un premier temps, je me limitais au cas $X$ lisse”, “mais pour quels coefficients ?”, and “Je pense que je devais”. The revised Zariski restriction carries “(malédiction !)”; the cancelled restriction to connected $G$ carries “(brr !)”. He says that étale cohomology would be needed later and the construction modified; the written “coh etale” remains unaccented and unexpanded.

## Scan 157

The continuation recalls using hyper-Ext in a derived category not yet formally developed, and proposes a present fppf construction of $J_{*X/k}$ with no cohomological-degree restriction. In contrast with the earlier length $\dim X$ on 155, the NB extends the complex to $2n$ and tentatively makes its components dimension zero for $i>n$. It proposes base change only in the derived category. Section D starts a smooth separated scheme over $k$, relative dimension $d$, and a positive integer $n$; the continuing sentence begins the case in which $n$ is prime to the characteristic.

**Reading and checks.** The open cup with an upper-right tick in “le dim $i$”, $J_i$ and $i>n$ is the same degree $i$, unlike the closed zero in “dim $0$”; the hyper-Ext superscript is also $i$, not a prime. This settles allographs without proving the dimension claim. The expected finite-type abbreviation is “t.f.”, but the first glyph after “séparé de” is V-shaped: V.f. remains first, with T.f./t.f. alternatives. The overwritten opening retains live $X:/k$ and a cancelled $f$; its colon is not removed to make standard $X/k$. The written “le dim” is not regularized.

**Author’s qualifications.** He writes “J'ai bien l'impression”, “pour heuristiques qu'elles furent”, “en coh fppf disons”, “Il est possible néanmoins”, and “Je crois bien”. The smoothness assumption is “pour simplifier”. The reference $(*)$ is preserved without deciding the uncertain label on 156.

## Scan 158

The page states global duality for coefficients annihilated by $n$, gives paired $Rf_!$/$Rf_*$ examples, and writes a perfect pairing in complementary degrees $i$ and $2d-i$, with tensor twist $\mu_n^{\otimes d}$. It then contrasts the difficulty in characteristic $p$ for $d>1$ with the smooth-curve case $d=1$, citing the coefficients $\mathbb Z/p\mathbb Z$, $\mu_p$ and $\alpha_p$, and extends the discussion to twisted coefficients and noncomplete curves with continuous ind-proalgebraic cohomology.

**Reading and checks.** The displayed degree is $2d-i$, with dotted $i$, not an extra numeral; the characteristic statement’s reduced letter is the same base field $k$ as on 157. The inner R of the displayed Hom has two stems, while the inline Hom’s R is plain; those visible alphabet differences are retained. Both overwritten lower stars are distinguished from the live exclamation marks. The final $F'$ has a separate prime that the preceding discussion does not license erasing. The added “est” contains no written $n$, and “il semble que tout s'écroule” is live beneath its insertion guide. The only formal calculation checks $i+(2d-i)=2d$, giving total degree 2 when $d=1$ (`158-complementary-degrees` in `local_consistency_checks.json`); it does not prove duality or perfectness.

**Author’s qualifications.** He writes “du moins modulo un shift d'amplitude $2d$”, “il semble que tout s'écroule”, “pourvu qu'on l'énonce avec soin !”, and “on se convainc que ça marche toujours.!”. The final warning begins “Simplement il faut faire attention”. The clipped last group description remains marked.

## Scan 159

The opening relates the abelian fundamental group and $H^1(X,\mathbb Z/p^n\mathbb Z)$ for noncomplete $X$. The body attributes to Serre a duality of connected commutative unipotent groups modulo radical isogeny, using $G'=\operatorname{Ext}^1(G,\mathbb Q/\mathbb Z)$ with a quasi-algebraic structure, the normalization for $\mathbb G_a$, and $G\simeq\Delta\Delta G$. It extends the duality to ind-pro-groups over arbitrary base fields of characteristic $p>0$, contrasts it with Ext degree zero for finite étale groups, and proposes joining the dualities in a derived category.

**Reading and checks.** In the opening, the tall pi form has a curved right foot and names the abelian fundamental group, so it is $\pi$, not a separate capital-Pi object. The barred abbreviation is $\bar m$, compared with the full m in “mod”; it remains abbreviated. The predicate “continue|infinie” stays unresolved, since the mathematical claim does not choose its letters. The inner additive-group letter has an independent internal stroke and is $\mathbb G_a$. The written Ext degrees are 1 and 0. Comparison with the derived Hom definition on 160 confirms the degree-zero convention $\operatorname{Ext}^0=\operatorname{Hom}$; this does not establish either asserted duality. The singular “étale” after “groupes finis” remains as written.

**Author’s qualifications.** They are “sans jamais l'écrire, je crois”, “sur $k$ alg clos, disons”, “de façon unique sans doute”, and “pas nec alg. clos”. Both surname occurrences retain the same Pontrjagin/Pontryagin uncertainty; published spelling was not consulted.

## Scan 160

The defining assignment $G\mapsto\Delta G=\mathbb R\underline{\mathrm{Hom}}(G,\mathbb Q/\mathbb Z)$ is called cohomological Serre duality. The proposed coefficient category consists, up to limiting operations, of extensions of étale groups by connected unipotent groups. Passing to $\mathbb Q/\mathbb Z$ and $\mu_\infty$ leads to the boxed identity $\Delta(Rf_!(F))\simeq Rf_*(DF[2])$ and a contrast between Cartier duality “above” and Serre duality “below”.

**Reading and checks.** The initial R is doubled; the later R letters are plain. The field subscript in $f^!(\mathbb Q/\mathbb Z)_k=(\mu_\infty)_X$ is the locally fixed $k$. The annotation arrow rises from the $[2]$ region toward “shift”; it is not an arrow into the formula. The limiting-operations phrase remains “passages|p.n.g” followed by “à|;”, without manufacturing extra words or punctuation. The map formulas were tracked for notation, not proved; the separate arithmetic comparison with Lang’s shift is reported under 162. No closing quotation marks are supplied after “en haut”. The manuscript folio remains 15|16, with 15 preferred from the upper horizontal stroke, not settled by sequence.

**Author’s qualifications.** The asserted autoduality is conditional: “si on se place dans une catégorie dérivée”. The alternative $R\underline{\mathrm{Hom}}(F,\mathbb G_m)$ ends “au choix ?”. He then writes “La validité de la formule de dualité ne fait aucun doute”, while beginning to describe the remaining work. That is his assurance, not a proof performed in this run.

## Scan 161

The page locates the remaining work in specifying coefficient categories and duality functors, then proposes reduction to $\mathbb Z/p\mathbb Z$, $\mu_p$ and $\alpha_p$ on a smooth complete $X$. It interprets $R^1f_*(G_X)$ through extensions of a generalized Jacobian, relating the formula to geometric class-field theory. For finite $k$, it invokes Lang’s device and begins a relation between the arithmetic fundamental group of a smooth connected commutative group $J$ and $H^0(k,J)=J(k)$.

**Reading and checks.** At the opening, the live functors are D and Delta over uncertain earlier Delta and D, respectively; the older strokes are not doubled alphabets. The exponent in $(\mathbb Z/p^{n|m}\mathbb Z)_k$ remains unresolved: an arbitrary-power coefficient does not distinguish its compressed n/m. The two field slots in $H^0(k,J)=J(k)$ name the declared $k$, and the arithmetic pi notation continues onto 162. The final “groupe con” is clipped and is not completed from the following sheet. The visible “standart” and unaccented “arithmetique” are preserved.

**Author’s qualifications.** His confidence is expressed as “consiste certainement”, “la validité de la formule doit résulter sans difficulté des dévissages habituels”, and the NB “le cas des coeff. premiers à la car. est déjà connu.” These are an outline and an assertion of known background, not a reduction proof checked here.

## Scan 162

The page recasts the preceding arithmetic fundamental-group relation as Lang duality, $\Delta_0\mathbb R\Gamma_k(J^*)\simeq\mathbb R\Gamma_k(\Delta J^*[1])$, then proposes an arithmetic class-field formula with shift $[3]$. It warns that continuous coefficients such as $\alpha_p$ require care in defining $Rf_!$ for noncomplete $X$, and demands an exact triangle involving an admissible extension on a compactification and its formal completion.

**Reading and checks.** In the opening formula, the preceding sheet’s explicit arithmetic notation fixes $\pi_1^{ar}$, rather than capital Pi or “or”. The two reduced h-like Gamma subscripts identify the same declared base field $k$ as the clearer left subscript. In the boxed formula, two left parentheses but only one right parenthesis occur before the equivalence; the unmatched outer parenthesis is preserved. The triangle keeps the stacked hat and tilde, the star/plus doubt on the right-hand $f$, and the bar/arrow-head doubt on the horizontal edge. Intended exactness does not settle those strokes. The formal calculation $2+1=3$ compares the geometric shift on 160 with the Lang shift here (`162-shift-arithmetic`); it assumes both formulas and proves neither.

**Author’s qualifications.** His caution is “il faut faire attention dans la définition de $Rf_!(F)$”, followed by “il faut avoir un triangle exact”. No separate “?” or “sauf erreur” is attached to the two displayed dualities. The folio is read as 17 but remains uncertain because its upper portion is clipped.

## Scan 163

The opening identifies $\widehat{\widetilde F}$ as the formal completion along the finite set $\widetilde X-X$ and links it to local class-field theory. Section E, “Corps de classes local”, takes a complete discrete valuation ring $V$, residue field $k$ and fraction field $K$, under the stated alternative hypotheses on $k$. Starting with finite coefficients F, it proposes a coefficient category over $k$, a functor $F\mapsto\mathbb R\underline\Gamma_K(F)$, and the compatibility $R\Gamma_K(F)\simeq R\Gamma_k(R\underline\Gamma_K(F))$.

**Reading and checks.** In the parenthetical $V\simeq k[[T]]$ (line 9) and the final outer Gamma index (line 22), the one-shoulder glyph is the same residue-field $k$ defined nearby and written with distinct arms in $k\subset V$. The fraction field is explicitly K; the curved K indices do not introduce kappa. These local allograph comparisons resolve k/h and K/kappa without proving the power-series or functor assertions. The barred m after “sans doute la” (line 17) matches the abbreviation on 159 and is not expanded. The mapping has doubled R and a colon; all R letters in the final identity are plain, and only its inner Gamma is underlined.

**Author’s qualifications.** He writes “C'est ici, sauf erreur”, “Pour fixer les idées et être sur un terrain solide”, the insertion “d'abord”, and “sans doute la” followed by the barred-m abbreviation “que dans D)”. These reservations remain distinct from a proof of the proposed compatibility.

## Scan 164

The opening assigns algebraic ind-pro-group structures to $H^0(K,F),H^1(K,F),\ldots$ and gives the ring scheme associated with V and the Greenberg functor a central role. It proposes local geometric duality with shift $[1]$, then a finite-residue-field formula with shift $[2]$ via Lang, encompassing geometric and arithmetic local class-field theory. “Remarques” begins a statement about coefficients prime to the residue characteristic.

**Reading and checks.** The reduced initial field letter is the residue-field $k$ fixed on 163 and repeated more fully here; all four Gamma indices are the fraction-field K. The geometric formula underlines Gamma alone, while the arithmetic formula does not. Small separate points beside two K indices remain doubtful marks, without an inferred operation. The wave over Delta-zero and the possible earlier 1 overwritten by the live 2 also remain doubtful. The formal calculation $1+1=2$ combines the written local geometric and Lang shifts (`164-shift-arithmetic`); it neither identifies the obscured earlier numeral nor establishes either duality. In the line introducing the first formula, the visible ve ending gives “s'écrive”, whereas the sentence would normally suggest “s'écrira”; the author’s form is retained.

**Author’s qualifications.** They include “sortant immédiatement des exemples élémentaires”, “pour $k$ alg clos disons”, and “la formule est très facile et bien connue”. No explicit reservation accompanies either displayed formula. The final item marker remains a/e/alpha rather than being fixed from the subsequent b) and c).

## Scan 165

The continuation presents the induction identity $i^!(D_SF)=D_s(i^*(F))$ for the inclusion $s=\operatorname{Spec}k$ into $S=\operatorname{Spec}V$. It singles out p-primary coefficients and unequal characteristics as the remaining difficulty. Remark b composes $Rj_*$ with a cohomological Greenberg-type functor. Remark c limits the author’s explicit assurance to finite coefficients, then proposes a broader group-scheme statement and begins a recollection of a formula.

**Reading and checks.** In the complete induction display, the open rounded left coefficient has no secure closed P bowl and is the same F explicitly used on the right; no P has been introduced. In $p=\operatorname{car}k>0$, the reduced field letter matches the distinct-arm k in “Spec k”. These are local allograph checks, not proof of the induction identity. Both inclusion-map endpoints retain bar/arrow uncertainty. “formalisme” is one live retouched word, not an additional recoverable cancellation. Only “nis” in “finis” is underlined. At the end, the ink favours “un” although grammar with “souvenance” calls for “une”; both remain. The final e of “formule” reaches a fold and stays marked. The clipped folio remains 20 with doubt.

**Author’s qualifications.** He writes “c'est pour ceux-là que je suis sûr de mon fait”, “Mais il est certainement vrai”, inserts “(avec quelques fibres dégénérées dans (D) ?)”, and concludes “mais je n'ai jamais tiré cette question entièrement au clair, même heuristiquement”. His recollection is explicitly a “vague souvenance”.

## Scan 166

The page proposes a comparison between $H^1(K,F)$ and $\operatorname{Ext}^1_{k\text{-}\mathrm{gr}}(G',\mathbb Q/\mathbb Z)$, where F is an abelian scheme, F' its dual, and G' the proalgebraic group attached to the latter’s Néron model. A marginal continuation suggests that the earlier Néron-model conjecture should follow from local duality. After d), section (F), “Portée et limites de la topologie” fppf, recalls the hope of obtaining p-adic Weil cohomology from fppf cohomology with discrete and continuous coefficients.

**Reading and checks.** The two opening field letters are resolved as k by the distinct-arm k in the complete Ext subscript: they name the same residue field. The subscript is gr, with neither a terminal p nor a stop. The question mark belongs above the comparison sign. Before F in line 2, the tall ascender and basal oval support d; the compressed following stroke permits e, so “de” precedes di/si/d' alternatives. The expected conditional “si” does not replace that ink. The complete rotated margin confirms a continuation of “En principe, la”; “conj|conj.” and “mentionnée” remain uncertain. In the three n-to-infinity signs, the first two have source bars and the third does not; their right returns are not completed as arrowheads. The lower verb (line 22) remains “devait|devrait”, without selecting a tense from the argument. No comparison theorem or cohomology construction was proved.

**Author’s qualifications.** The display carries “?” and “(NB sans aucune garantie)”; the opening includes “si $k$ alg clos disons”. The margin says “En principe” and “devrait sortir de la machine de dualité locale”; d) asks “Tu pourrais demander à Deligne s'il n'a pas approfondi les questions (D) et (E) dernièrement.” The later hope was one “que j'essayais en vain de préciser”.

## Scan 167

The page contrasts the earlier hope for homology with crystalline cohomology, attributed by an insertion to Berthelot. It says that fppf cohomology with algebraic-group coefficients captures only a small part of crystalline cohomology, using the additional semilinear Frobenius structure over the Witt vectors. The captured portion has slope at most 1, against a stated possible range from 0 to i; the last clause starts the explanation for $i=1$.

**Reading and checks.** All three field slots are k, identified with the established base and the distinct-arm k on 166. The crystalline subscript remains cris/crs. At lines 16–17, de/des and module/modules remain doubtful; the complete parenthetical context shows an initial m, not a W-prefix. The extra low rises before the apostrophe favour literal “les' anneau”, while grammar suggests “l'anneau”. The earlier “lié” has one final e although “La construction” requires “liée”. At line 23, the open second letter resolves “Ce explique”; grammar would suggest “Cela” or “Ça”, neither supplied. The Frobenius label’s curve is attached to F, not a separate tilde; the shaft endpoint remains uncertain. The opening reference is explicitly “(B)”, although the complex construction is under C) on 155 and B) on 154 concerns Jacobian autoduality. This is a possible reference slip without a certain emendation.

The limited calculation intersects $[0,i]$ with slopes $\leq1$: it covers $[0,1]$ when $i=1$ but excludes $(1,2]$ when $i=2$ (`167-slope-intervals`). This checks only the numerical contrast; realization of all slopes at most 1 is still called a conjecture on 168. The faint point after $i=1$ remains doubtful despite the continuing sentence.

**Author’s qualifications.** He writes “l'homologie donnerait peut-être ce que la cohomologie nous cèle !”, restricts the crystalline assertion by “du moins” to projective smooth X, and introduces the comparison conditionally: “Si on l'utilise comme une sorte d'étalon sûr”.

## Scan 168

The continuation reports successful recovery of a correct $H^1$ through fppf, but unsuccessful attempts already for $H^2$. It explicitly conjectures that the entire slope-at-most-one part of crystalline $H^i$ comes from fppf. After the three-stroke separator, the response to the correspondent’s question $7^\circ$ distinguishes homotopical algebra on a topos using semi-simplicial sheaves and champs from a viewpoint in which the rich topos structure virtually disappears.

**Reading and checks.** The exponents 1 and 2 are undotted numerals, whereas the crystalline degree i has its own dot. The inequality has a separate lower bar and reads $\leq1$. These notation readings are consistent with the limited interval calculation reported on 167; they do not verify either the fppf realization claim or the reported failures. The preferred “tous genre” now retains both tous/tout and genre/genres doubts; grammatical agreement would allow “tout genre” or “tous genres”, but cannot select their strokes. The colon after fppf is resolved from two aligned ink marks. A second point after “question.” remains doubtful, while the final comma after “virtuellement” has a readable body despite its edge-clipped tip. The ordinal 7° is a reference to a question, not a page count or a date.

**Author’s qualifications.** He says “À vrai dire, on conjecture”, “j'ai perdu complètement contact avec ces questions”, and that Mazur, Katz, Messing and Deligne “devraient être au courant du point où en est la question”. The homotopy discussion begins “Ta question $7^{\circ}$ semble indiquer” and “Sans doute tu dois confondre”. No external status check was made.

## Scan 169

The final sheet considers what survives of a topos in a homotopy or pro-homotopy category: homotopy groups and cohomology with constant or twisted coefficients, followed by locally constant n-champs, abelian chain complexes of length n and hypercohomology. It asserts that a homotopy equivalence induces an $(n+1)$-equivalence of the corresponding n-champ categories. The final triangle relates topos/spaces or semi-simplicial sets modulo n-homotopy, n-groupoids, and special n-categories.

**Reading and checks.** The curved-right-leg symbol is $\pi_i$, with dotted i rather than numeral 1. In the inline map, f overlaps the shaft near its right end; its semantic role does not establish an obscured arrowhead or move the label. In $(n+1)$, the crossing horizontal and vertical strokes give plus, and the numeral 1 is clear. The top node’s raised 1, slash and lowered 2 preserve the half-simplicial abbreviation. All three edges have heads at both ends, recording geometry without proving mutual determination. Before “constants”, the clear singular t ending remains, while a separate dark mark over the first e supports “coéfficient|coefficient”. The later singular “constant” and “loc. constant” also remain despite neighbouring plurals. The phrase is literally “localisation à brin de zinc”; no conventional expression is substituted. Inserted “chaines” has an i dot, not a circumflex. Accent or ending doubts remain in catégorie, abéliens and espace, and the inserted demonstrative remains ce/ca. The Objets quotation marks and lower-node abbreviations remain unresolved.

**Author’s qualifications.** The initial account is “à première vue”, with “ou à la rigueur constant tordus”. The question “que reste-t-il encore à ce pauvre $X$” introduces the more detailed investigation. No equivalence theorem or categorical classification was proved.
