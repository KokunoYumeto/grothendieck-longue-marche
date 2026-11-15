# Supplement: explicit correspondence maps and completion data

This supplement expands MB01–MB12 in `motivic_research_entries.json`. Current citations are to `11.pdf`, scans 003–036, through the frozen fragments `pages/MPL_11_002-042_11_scanNNN.tex`; cote-16 citations are to `context/MPL_16+47+54+44_transcription.tex`. That context transcription and its notes retain their first-pass status and all recorded uncertainty marks. The constructions labelled editorial below are supplied comparisons, not unrecorded arguments attributed to the manuscript.

## Kernels, realization, and the selected Lefschetz map

Cote 11 supplies an explicit category of kernels and its action on the coefficient objects. Its definition is `Hom_{V^A}(X,Y)=A(X×Y)` (11/003), its graph map is `f ↦ Γ_{f*}(1)` (11/009), and its realization is `u ↦ [x ↦ p_{2*}(u p_1^*x)]` (11/011–013). Stable systems `A′` select subsets of these kernels, with closure under the same pullbacks, pushforwards and products (11/021–025). These are concrete maps connecting the category to rings of operators of the kind introduced in cote 16/003; the comparison does not rest on a separation between “rings” and “categories.”

For a chosen object X, write

\[
\rho_X:A'(X\times X)\longrightarrow\operatorname{End}(A(X)),\qquad
\rho_X(u)(x)=p_{2*}(u\,p_1^*x),\qquad
E_X=\operatorname{im}(\rho_X).
\]

This is the exact realization map to use when comparing the convolution ring of kernels with an operator ring. Its kernel has the explicit description `u` such that `p_{2*}(u p_1^*x)=0` for every `x`; this record does not discard that kernel or assert injectivity for the general data of 11/003. The manuscript asserts functoriality and supplies the calculation in 11/013, while its graded sign cautions and uncertain final projection index remain part of the frozen evidence.

Cote 16/015–018 then specifies a further pointed ring map `Φ → E`, carrying the universal Lefschetz element and projectors to the selected `L` and `π_i`. Cote 16/016 calls the prescribed projector images “condition essentielle !”, and 16/017 retracts uniqueness from L alone with “Non” and the requirement “L et les π_i”.

## Stable-system inclusion

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

## Mixed morphisms as corners

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

## Degree transport

In the Poincaré tensor model of 11/027–031, the trace degrees add under tensor product. For a homogeneous kernel `u` of degree `q` on `X×Y`, the projection formula for its action gives output degree `deg(x)+q−d(X)`: `p_1^*` preserves degree, multiplication adds `q`, and `p_{2*}` has degree `−d(X)` under the degree convention stated at the end of 11/036. Thus the operator degree transported into the notation of cote 16/003 is `ν=q−d(X)`, not the unshifted kernel degree `q`; the diagonal kernel of degree `d(X)` acts in degree zero. The proof compares only degree bookkeeping and leaves the source's separate sign issues intact.

## The literal-set problem in 11/023

The source says the smallest stable system is often “identique à `\unsure{l'ens}` des `f_*(1_Y)`” and invokes resolution of singularities. The geometric map suggested by that clause is the composite `f:Ẑ→Z→X` from a smooth projective resolution of an integral subvariety: the generic degree is one, so the proper pushforward of its fundamental cycle is `[Z]`. This identifies the intended cycle generators, but it does not supply additive negatives or coefficient multiples as *individual* pushforwards of units.

There is a concrete point test. Take `X=Spec C` and ordinary Chow classes with rational coefficients (or their rational cycle-class images). The pushforward of the unit of a positive-dimensional smooth projective Y is zero; for a zero-dimensional Y consisting of r points it is `r∈Z_{≥0}⊂Q`. The set of values is therefore `Z_{≥0}` (including zero through positive-dimensional Y), while a unital subring contains `−1`; the comparison map is the actual proper-degree map `Y↦deg(Y)` and the inclusion `Z_{≥0}→Q`. The formula for proper pushforward was checked in the primary Stacks reference 0AZC. The manuscript's preceding multiplicative-monoid discussion on 11/019 may bear on the intended meaning, so the result is a reading/claim question about the literal set-versus-additive-closure wording, not an alteration of `l’ens` in the frozen transcription.

## Completion maps in the reference construction

For a concrete comparison use even grading `A^{2r}(T)=CH^r(T)_Q`; the map between the two gradings is explicitly `r↦2r`. The graded correspondence piece of operator codimension-degree r is `CH^{dim X+r}(X×Y)_Q`, with the same pull–multiply–push composition. Stacks 0FG9 then uses objects `(X,p,m)` and morphisms `q∘Corr^{n−m}(X,Y)∘p`, with idempotent p and integer m. The untwisted degree-zero inclusion is explicitly `X↦(X,Δ_X,0)` and `u↦u` on `Corr^0(X,Y)`; its compositions remain the displayed pull–multiply–push compositions. A homogeneous kernel of codimension `dim X+s` lies in `Corr^s(X,Y)` and therefore represents a morphism `(X,Δ_X,0)→(Y,Δ_Y,s)` in these same conventions. These formulas give the precise reference construction to compare with 11/003's full `A(X×Y)` and its unchanged variety objects. Only the construction and its maps are used here; no modern semisimplicity theorem is imported to settle the manuscript's claims.

## Primary construction references and scope

The [Stacks Project, Correspondences, Tag 0FFZ](https://stacks.math.columbia.edu/tag/0FFZ) supplies the displayed codimension-degree pieces and pull–multiply–push composition; in the even-graded specialization the two written factor orders agree by commutativity. [Chow motives, Tag 0FG9](https://stacks.math.columbia.edu/tag/0FG9) supplies the stated objects, idempotent corners, integer twists, and composition. [Proper pushforward, Tag 0AZC](https://stacks.math.columbia.edu/tag/0AZC) supplies the generic-degree rule used in the resolution map and point calculation.

These references support the explicit constructions being compared. The supplied ledger's modern-semisimplicity question **WG2 §2.3 #7** remains an unchecked planning item, and the related **MPL_14_087-132 M09** remains a first-pass lead; no semisimplicity theorem has been imported. MB13's separate comparison with Hua's declared simplicial-equivalence statement is recorded with its qualifications and unresolved card status in `hua_full_card_check.md`, and no proof verification is claimed there.
