# Cote 11 and the lefschetzien correspondence rings: research evidence

Prepared after the transcription freeze of 2026-11-15 19:37:25 UTC. This file uses the frozen TeX fragments only; no manuscript image was opened by this support agent and no frozen file was edited. `context/README.md` and `context/notes/RESULTS_STATE.md` were read first. The supplied cote-16 transcription and its notes remain first-pass claims: their uncertainty macros matter, and their assertions have not acquired reviewed status through this comparison.

## Direct answer supported by the supplied witnesses

Cote 11 supplies an explicit category of kernels and its action on the coefficient objects. Its definition is `Hom_{V^A}(X,Y)=A(X×Y)` (11/003), its graph map is `f ↦ Γ_{f*}(1)` (11/009), and its realization is `u ↦ [x ↦ p_{2*}(u p_1^*x)]` (11/011–013). Stable systems `A′` select subsets of these kernels, with closure under the same pullbacks, pushforwards and products (11/021–025). These are concrete maps connecting the category to rings of operators of the kind introduced in cote 16/003; the comparison does not rest on a separation between “rings” and “categories.”

For a chosen object X, write

\[
\rho_X:A'(X\times X)\longrightarrow\operatorname{End}(A(X)),\qquad
\rho_X(u)(x)=p_{2*}(u\,p_1^*x),\qquad
E_X=\operatorname{im}(\rho_X).
\]

This is the exact realization map to use when comparing the convolution ring of kernels with an operator ring. Its kernel has the explicit description `u` such that `p_{2*}(u p_1^*x)=0` for every `x`; this record does not discard that kernel or assert injectivity for the general data of 11/003. The manuscript asserts functoriality and supplies the calculation in 11/013, while its graded sign cautions and uncertain final projection index remain part of the frozen evidence.

Cote 16/015–018 then specifies a further pointed ring map `Φ → E`, carrying the universal Lefschetz element and projectors to the selected `L` and `π_i`. Cote 16/016 calls the prescribed projector images “condition essentielle !”, and 16/017 retracts uniqueness from L alone with “Non” and the requirement “L et les π_i”. The handwritten pages of cote 11 contain no occurrence of the words Lefschetz/motives or the symbols capital `Λ`, capital `Φ`, nor the terms projector/idempotent/Tate/Karoubian in the case-sensitive, word-bounded searches saved in `motivic_bridge_current_searches.json`; that bounded textual finding does not assert an absence of mathematical relations.

**Answer to the planning question:** the present pages make the kernel-to-operator bridge and stable coefficient systems explicit, but they do not exhibit a construction of the category of motives from the particular maps `Φ→E` of cote 16. The supplied evidence requires the comparison to retain the chosen correspondence classes, degree conventions, projectors and Lefschetz inverses, together with any passage to summands and twists; 11/003–025 writes the correspondence category, whereas 16/049 explicitly names the semisimple motivic programme. This adds substantial construction data to the first-pass ledger leads that had only an already-given motivic category in cotes 14, 15 and 18.

## Exact comparisons and proof checks

### Stable-system inclusion

For the stable system written on 11/021, the inclusion has the object map `X↦X` and arrow map

\[
\iota_{X,Y}:A'(X\times Y)\hookrightarrow A(X\times Y),\qquad u\mapsto u.
\]

Use `p_{XY},p_{YZ},p_{XZ}` here for the named coordinate projections of `X×Y×Z`; this identifies each projection independently of the differing numerical labels retained in the diplomatic text. The comparison of composition is the literal calculation

\[
\iota_{X,Z}(v\circ_{A'}u)
=p_{XZ*}\bigl(p_{YZ}^{*}\iota_{Y,Z}(v)\;p_{XY}^{*}\iota_{X,Y}(u)\bigr)
=\iota_{Y,Z}(v)\circ_A\iota_{X,Y}(u),
\]

because all three operations on `A′` are restrictions of the displayed operations on `A`. The identity is the same diagonal class `δ_{X*}(1)` (11/007), which belongs to the stable system by the unit and graph clauses of 11/021. External products are preserved by the identical restriction argument. This establishes the exact inclusion being compared, without equating `A′(X×X)`, its operator image, or the universal ring `Φ`.

### Mixed morphisms as corners

For the formal additive enlargement of the algebra-valued correspondence category, form

\[
R_{X,Y}=\begin{pmatrix}
A'(X\times X)&A'(Y\times X)\\
A'(X\times Y)&A'(Y\times Y)
\end{pmatrix},\quad
e_X=\begin{pmatrix}\Delta_X&0\\0&0\end{pmatrix},\quad
e_Y=\begin{pmatrix}0&0\\0&\Delta_Y\end{pmatrix}.
\]

Matrix multiplication uses the given convolution compositions. The exact map

\[
A'(X\times Y)\longrightarrow e_YR_{X,Y}e_X,
\qquad u\longmapsto\begin{pmatrix}0&0\\u&0\end{pmatrix}
\]

has inverse “take the lower-left entry”; multiplication of compatible such matrices gives the convolution of their nonzero entries. Cote 16/004 already writes the related corner decomposition `E=⊕_{i,j}π_jEπ_i`. Here the corner labels index the two chosen objects, while 16/004 explicitly indexes graded pieces of a module; the two maps and their idempotents specify the relationship rather than treating one indexing as a silent relabelling of the other. This formal additive construction is an editorial comparison, not a claim that the author carried it out in the selected cote-11 pages.

### Degree transport

In the Poincaré tensor model of 11/027–031, the trace degrees add under tensor product. For a homogeneous kernel `u` of degree `q` on `X×Y`, the projection formula for its action gives output degree `deg(x)+q−d(X)`: `p_1^*` preserves degree, multiplication adds `q`, and `p_{2*}` has degree `−d(X)` under the degree convention stated at the end of 11/036. Thus the operator degree transported into the notation of cote 16/003 is `ν=q−d(X)`, not the unshifted kernel degree `q`; the diagonal kernel of degree `d(X)` acts in degree zero. The proof compares only degree bookkeeping and leaves the source's separate sign issues intact.

### The literal-set problem in 11/023

The source says the smallest stable system is often “identique à `\unsure{l'ens}` des `f_*(1_Y)`” and invokes resolution of singularities. The geometric map suggested by that clause is the composite `f:Ẑ→Z→X` from a smooth projective resolution of an integral subvariety: the generic degree is one, so the proper pushforward of its fundamental cycle is `[Z]`. This identifies the intended cycle generators, but it does not supply additive negatives or coefficient multiples as *individual* pushforwards of units.

There is a concrete point test. Take `X=Spec C` and ordinary Chow classes with rational coefficients (or their rational cycle-class images). The pushforward of the unit of a positive-dimensional smooth projective Y is zero; for a zero-dimensional Y consisting of r points it is `r∈Z_{≥0}⊂Q`. The set of values is therefore `Z_{≥0}` (including zero through positive-dimensional Y), while a unital subring contains `−1`; the comparison map is the actual proper-degree map `Y↦deg(Y)` and the inclusion `Z_{≥0}→Q`. The formula for proper pushforward was checked in the primary Stacks reference 0AZC. The manuscript's preceding multiplicative-monoid discussion on 11/019 may bear on the intended meaning, so the result is a reading/claim question about the literal set-versus-additive-closure wording, not an alteration of `l’ens` in the frozen transcription.

### Completion in a verified reference

For a concrete comparison use even grading `A^{2r}(T)=CH^r(T)_Q`; the map between the two gradings is explicitly `r↦2r`. The graded correspondence piece of operator codimension-degree r is `CH^{dim X+r}(X×Y)_Q`, with the same pull–multiply–push composition. Stacks 0FG9 then uses objects `(X,p,m)` and morphisms `q∘Corr^{n−m}(X,Y)∘p`, with idempotent p and integer m. This gives the precise reference construction to compare with 11/003's full `A(X×Y)` and its unchanged variety objects. Only the construction and its maps are used here; no modern semisimplicity theorem is imported to settle the manuscript's claims.

## Note candidates (each entry one to four sentences)

All current witnesses refer to archive file `11.pdf` and the corresponding frozen fragment `pages/MPL_11_002-042_11_scanNNN.tex`. The shorthand **CT** below means `MPL_16+47+54+44_transcription.tex`; **CN** means `MPL_16+47+54+44_notes.md`. Full search results for each candidate are saved in `motivic_bridge_context_searches.json`. The context search includes CT, CN and the supplied results ledger; a matching earlier research note is treated as a lead.

### MB01 — Cote 11, scans 003 and 011–013 — unpursued implication

“On va définir une nouvelle catégorie” is made concrete by `Hom(X,Y)=A(X×Y)` and the action `ρ_{X,Y}(u)(x)=p_{2*}(u p_1^*x)`, so `E_X=im ρ_{X,X}` is the precise operator-ring comparison. Searching `endomorphismes | correspondances | End` finds CT16/003 and CT16/018; cote 11 **adds** the mixed-object kernels and their realization map to those ring descriptions. This bears on **WG2 §2.4 #3** [unchecked question/plan] and **MPL_14_087-132 M01** [first-pass research-note lead], without identifying the kernel of ρ with zero or identifying `E_X` with the image of `Φ`.

### MB02 — Cote 11, scan 021 — unpursued implication

The words “les A′(X)⊂A(X)” give the identity-on-objects arrow inclusion `u↦u`, and its preservation of convolution follows from `ι(v∘u)=p_{XZ*}(p_{YZ}^*ι(v)p_{XY}^*ι(u))=ι(v)∘ι(u)` using the restricted operations. Searching `sous-anneau | sous-algèbre | sous-catégor` finds CT16/003 and CT16/007; this **adds** an explicit functor selecting kernels to the context's subring-of-endomorphisms setup. The rewritten marginal classification of subcategories remains a source claim with difficult wording, and the proposed more general equivalence is expressly postponed. This bears on **WG2 §2.4 #3** [unchecked question/plan] and **MPL_14_087-132 M01** [first-pass lead].

### MB03 — Cote 11, scan 023 — unproved claim

The phrase “du moins si on admet la résolution des singularités” directs the generation claim toward `f:Ẑ→Z→X` and `f_*1=cl[Z]` for a degree-one resolution map; the required generation argument must track addition and coefficients as well as the individual generators. Searching `résolution | singularités | algebraic correspondance class | algébrique` finds the algebraic-correspondence realization statements in CT16/048–049, but no matching resolution-based formula for `A_sp`; cote 11 **adds** that proposed generating mechanism. This bears on **WG2 §2.4 #3** [unchecked question/plan] and **MPL_15_195-228+18_002-017 M07** [first-pass lead concerning algebraic correspondences], rather than settling the ledger's motivic comparison.

### MB04 — Cote 11, scans 019 and 023 — own idea; reading question

For the literal “l’ens des f_*(1_Y)”, the point calculation `X=Spec C`, `f_*1=0` for positive-dimensional Y and `f_*1=r≥0` for r points gives the exact map into `Q`, whereas the source's unital-subring language requires `−1`. Thus the proposed set equality needs an additive-closure reading or another explicit convention; the text on 019 about using “seulement leur structure de monoïde” is a relevant internal clue, and neither phrase has been changed in the frozen text. Searching `A_sp | ss-foncteur | résolution | singularités | algebraic correspondance class` finds no matching formulation in CT and leads back to CT16/048–049; this **adds** a concrete test to **WG2 §2.4 #3** [unchecked question/plan]. **Confidence: high in the proper-degree calculation, lower in the author's intended closure convention**, because `l’ens` is itself an uncertain reading and the preceding pages change the level of algebraic structure.

### MB05 — Cote 11, scans 023–025 — unpursued implication

“Une application … est dite de type A′” means an actual kernel `u∈A′(X_1×⋯×X_n×X)` acting on an external product, and the subsequent composition and product calculations give the declared recipe for the stable system generated by the `E_X`. Searching `multiplication | produit | anneau` finds CT16/015's multiplication table and CT16/018's ring definition; cote 11 **adds** mixed-object multilinear closure operations to those single-ring calculations. This bears on **WG2 §2.4 #3** and **WG2 §6. #9** [both unchecked question/plan entries]; no equality between this closure and the particular universal image `Φ→E` is written here.

### MB06 — Cote 11, scans 015–017 — self-flagged; unpursued implication

“vérifier que c’est multiplicatif!” and “mod. signe!” accompany the transpose construction, and the live adjointness argument explicitly inserts “si u central”. Searching `transposition | dualité | dual | transpose` finds CT16/018's opposite-ring/transposition passage and CT16/048–049's algebraic duality argument; cote 11 **adds** the kernel formula and the trace compatibility that make the comparison testable. The even cycle-class specialization supplies the explicit commuting factor `(-1)^{(2r)m}=1` for a class of degree `2r` against one of degree `m`, thereby checking the source's centrality clause in that specialization; the general comparison must still retain the written graded-order restrictions at `ρ(su)` versus the trace transpose of `ρ(u)`. This bears on **MPL_14_002-044 A36** and **MPL_14_087-132 M09** [both first-pass leads] and **WG2 §2.4 #3** [unchecked question/plan].

### MB07 — Cote 11, scans 027, 029, 031 and 036 — unpursued implication

The degree rule “d(B)−d(A)” transports a kernel of degree q to an operator of degree `q−d(X)`: pullback preserves degree, multiplication adds q, and projection pushforward subtracts `d(X)`. Searching `graduation | pi_i | degré` finds CT16/003's `End^(ν)(M)=Σ Hom(M^i,M^{i+ν})` and CT16/016–017's chosen projectors; cote 11 **adds** the explicit degree transport needed for that operator-ring comparison. Its retraction “Mais c’est faux” on 029 and even-degree restriction on 031 remain part of the comparison, so the degree calculation supplies no resolution of the remaining signs. This bears on **MPL_14_087-132 M05**, **MPL_15_195-228+18_002-017 M03** [first-pass leads], and **WG2 §2.4 #3** [unchecked question/plan].

### MB08 — Cote 11, scans 003, 021 and 023 — unpursued implication

The category and stable kernels provide the map into operators, while the proposed relation to the named lefschetzien rings requires the specific images `L` and `π_i` in `Φ→E`. Searching `Phi | Lefschetzien | condition essentielle` finds CT16/015–018, including “condition essentielle !” and the retracted uniqueness question answered “Non”; cote 11 **adds** a possible source of the operator rings but does not write those chosen images. This sharpens **WG2 §2.4 #3** and **WG2 §6. #9** [unchecked question/plan entries] and **MPL_14_087-132 M01** [first-pass lead] by identifying the maps to be compared rather than declaring whole categories equivalent.

### MB09 — Cote 11, scans 003, 021–025 — unpursued implication

“Ob V^A=Ob V” fixes the objects of the written construction, and the precise published comparison uses the even-graded specialization `A^{2r}(T)=CH^r(T)_Q`, followed by the objects `(X,p,m)` and morphisms `q∘Corr^{n−m}(X,Y)∘p` of Stacks 0FG9. Searching `motives | semi-simple | projecteurs | projector` finds CT16/049's “category of motives which is semi-simple !” and CN16:49:4; the current pages **add** the preceding correspondence construction, while summands and twists in this comparison are supplied by the cited reference rather than by a sentence of cote 11. This bears on **WG2 §2.4 #3** [unchecked question/plan], **MPL_14_002-044 M01**, **MPL_15_195-228+18_002-017 M01**, and **MPL_14_087-132 M01** [first-pass leads].

### MB10 — Cote 11, scans 003 and 021 — own idea

The formal additive enlargement gives the exact corner isomorphism `A′(X×Y)→e_Y R_{X,Y} e_X`, `u↦[[0,0],[u,0]]`, whose inverse takes the lower-left entry, and compatible matrix products reproduce convolution. Searching `pi_j…E | pr_{i,j} | modules sur` finds CT16/004's `E=⊕π_jEπ_i`; this **adds** an explicit multi-object comparison to the context's graded-module corner decomposition, with both index sets and both maps stated. It bears on **WG2 §2.4 #3** [unchecked question/plan] and **MPL_14_087-132 M01** [first-pass lead]. **Confidence: high in the matrix calculation**, because the two entry maps are inverse and the multiplication is written explicitly; this is an editorial construction, not an attribution of an unrecorded argument to the author.

### MB11 — Cote 11, scans 017 and 019 — unpursued implication

“On n’a jamais … utilisé la structure additive” records the precise forgetful operation from the algebra-valued data to the retained multiplication, unit, pullback and pushforward operations used in the preceding formulas. Searching `anneau | motives | semi-simple` finds CT16/018's ring structure and CT16/049's request for semisimplicity; cote 11 **adds** a record of which operations its initial calculation uses, without giving the additive splitting argument requested on 16/049. This bears on **WG2 §2.4 #3**, **WG2 §2.3 #7** [unchecked question/plan entries], and **MPL_14_087-132 M09** [first-pass lead]; none of those statuses is upgraded here.

### MB12 — Cote 11, scans 017, 021 and 023 — unpursued implication

The graph, transpose and stable-system formulas identify a concrete source of operator subrings to compare with cote 16/051's “anneau d’endomorphismes … stable par composantes homogènes … par transposition”. Searching `algébrique | algebraic | inverse | correspondance` locates CT16/051, 053 and 055, where specified inverse operators `u_i` lead to projectors through the displayed inverse-operator compositions (the index on `u_k` has a `k|n` doubt in CT); cote 11 **adds** kernel-level closure data to that reconstruction. The remaining comparison must explicitly supply homogeneous-component stability, the selected polarization and those inverses in the image of `ρ_X`, rather than supplying them from the word “stable”. This bears on **WG2 §6. #9** and **WG2 §2.4 #3** [unchecked question/plan entries] and **MPL_14_087-132 M01** [first-pass lead].

## Primary references actually checked

1. The Stacks Project, Section 45.3, **Correspondences**, Tag **0FFZ**, definitions and Lemma 45.3.1: <https://stacks.math.columbia.edu/tag/0FFZ>. Tool reference `turn7view1` (also `turn7search2`); inspected source has 201 lines, definitions at lines 18–38. Used for the exact degree piece and convolution formula; source convention places the first kernel before the second, agreeing with the even-graded specialization by commutativity.
2. The Stacks Project, Section 45.4, **Chow motives**, Tag **0FG9**, definition and Lemmas 45.4.1–45.4.3: <https://stacks.math.columbia.edu/tag/0FG9>. Tool reference `turn7view0` (also `turn7search0`); inspected definition at lines 18–34 and tensor/summand construction at lines 36–69. Used only for the explicitly displayed summands and twists comparison. Keep the final discussion of this source compact and avoid repeating its definition in multiple sections.
3. The Stacks Project, Section 43.6, **Proper pushforward**, Tag **0AZC**: <https://stacks.math.columbia.edu/tag/0AZC>. Tool reference `turn17view0`; inspected definition at lines 18–23. Used for the generic-degree computation and concrete point test.

Root must reopen the URLs or refs before using their citation IDs in the final response. No Jannsen theorem was imported: the relevant modern-semisimplicity item remains **WG2 §2.3 #7**, an unchecked planning entry, alongside the first-pass lead **MPL_14_087-132 M09**. The reviewed LM7_PUSH entry in the supplied ledger addresses modular descent and was not used as evidence for any motivic statement.

## Search and provenance cautions

- The CT search is across all four supplied cotes, not only cote 16; the note candidates identify the relevant selected matches explicitly.
- The small phrase on 11/023 is frozen as `\unsure{l'ens}`, so MB04 is an explicit challenge to the literal proposed reading/statement, not a confident claim about an unseen word.
- Cote 16/051's lowering-like operator is itself transcribed with an uncertain mark following L; this record quotes its inverse-operator/projector calculation without silently replacing that printed L by Λ.
- The source's all-degree Hom space and the operator degree are related by the displayed degree map. A simple renaming of all `A(X×Y)` as degree-zero motivic morphisms has not been made.
- The current-word searches were repeated case-sensitively with word boundaries after a preliminary case-insensitive search had matched lower-case `lambda` and the substring `tate` inside `constate`; only the corrected zero-result record is used for the bounded textual conclusion.
