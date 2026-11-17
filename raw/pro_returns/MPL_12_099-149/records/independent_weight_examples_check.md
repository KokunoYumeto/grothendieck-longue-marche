# Independent check of two proposed weight counterexamples

Research-only check, 2026-11-17, after transcription freeze. No frozen file changed. These examples were proposed by the weights researcher; this record independently checks degrees, twists, hypotheses, and descent. **Verdict: both examples work**, with the notation and scope qualifications below. No claim of novelty is made.

## V1 — Split multiplicative elliptic degeneration

**Manuscript witness:** cote 12, scan 120, coefficient question “poids ≤ 2 Inf(i,n)+j ?”; compare scan 113's definition of strictly special as a direct factor of a smooth projective higher direct image. **Kind:** own idea / counterexample check. **Confidence:** high, because the tame-inertia complex explicitly calculates the stalk and its Frobenius eigenvalue. **Context search:** `strictement | poids | immersion | coefficients` → `context/hua_project/12.modern.tex`, “Le cas d'une immersion : les feuilles de calcul (pages 115, 117 et 119)” and “Le point 2) : coefficients strictement spéciaux (page 121)”; `context/notes/RESULTS_STATE.md`, Hua finding `12-immersion-level-bound`. **Relation:** contradicts the unrestricted extension to varying pure coefficients, not the constant-coefficient immersion bound; this does not change any RS status or frozen reading.

Let k=F_q have odd characteristic, with −1 a square, and let π:E→U be the Legendre elliptic scheme y²=x(x−1)(x−t) over U=P¹_k−{0,1,∞}, with open immersion a:U→P¹_k and F=R¹π_*Q_l for l≠char(k); F is itself a smooth projective higher direct image, hence fits the “strictement spécial” requirement, and is pure of weight j=1. At t=0, the special cubic y²=x²(x−1) has rational distinct tangent directions, so the elliptic degeneration is split multiplicative and the local H¹ representation V has 0→Q_l→V→Q_l(−1)→0 with nontrivial unipotent tame inertia, whence V^I=Q_l and V_I=Q_l(−1). The tame cohomology formula gives (R¹a_*F)_0=H¹(I,V)=V_I(−1)=Q_l(−2), on which geometric Frobenius acts by q², so the output weight is 4 although i=n=j=1 would give the written upper bound 3. Thus the coefficient extension is false in this ordinary-direct-image interpretation even for a smooth base curve and an elliptic smooth projective family.

**Notation correction.** The notation `(V/NV)(−1)` is safe only after a chosen tame parameter turns monodromy into an underlying endomorphism; intrinsically, one may write `H¹(I,V)=V_I(−1)` or `coker(N:V→V(−1))`. This avoids mixing the Tate twist built into N with the additional twist in tame group cohomology. The signs here use geometric Frobenius and Q_l(1) of weight −2, matching the convention explicit in scan 111.

### Compact-support counterpart

The same family gives a precise failure of a proposed lower bound by the coefficient weight alone: geometric monodromy is SL₂, so H⁰(U_kbar,F)=0, and the sheaf sequence 0→a_!F→a_*F→i_*i^*a_*F→0 gives an injection H⁰(D_kbar,i^*a_*F)→H¹_c(U_kbar,F). At both t=0 and t=1 the split multiplicative invariant line is Q_l of weight 0, so at least Q_l² injects into H¹_c, despite F having weight 1. The geometric monodromy and unipotent local blocks are stated in Katz's *Convolution and Equidistribution*, Chapter 15, p. 77; the boundary invariant calculation is the same local calculation above. This is a separate coefficient example and should not be described as disproving the usual constant-coefficient smooth-variety lower bound.

## V2 — An E₂ top-weight term killed by d₂

**Manuscript witness:** cote 12, scan 120, “poids 2n s'identifie avec” E₂^{2(i−n),2n−i}; compare scan 118's same bidegree. **Kind:** own idea / counterexample check. **Confidence:** high, because the complete relevant E₂ terms and the abutment are determined by normal-crossing local cohomology and purity. **Context search:** `E_2 | poids | immersion | dégén` → `context/hua_project/12.modern.tex`, “Le cas d'une immersion : les feuilles de calcul (pages 115, 117 et 119)”; `context/notes/RESULTS_STATE.md`, Hua finding `12-immersion-level-bound`. **Relation:** contradicts an unconditional E₂=top-weight-abutment identification, while leaving the upper bound itself intact; no novelty or RS status upgrade is asserted.

Take a:A²_k−{0}→A²_k, blow up 0, then blow up one k-rational point on the first exceptional P¹, and write h:Y→A²_k for the composite and b:U→Y for the open complement, so a=h∘b and D=Y−U is two k-rational P¹'s meeting transversely at a k-rational point. The normal-crossing formula gives R¹b_*Q_l=(Q_{D₁}⊕Q_{D₂})(−1), R²b_*Q_l=Q_{D₁∩D₂}(−2), so at 0 the Leray term E₂^{0,2}=Q_l(−2) is nonzero and E₂^{2,1}=Q_l(−2)². Purity for the codimension-two origin gives R²a_*Q_l=0 and R³a_*Q_l=Q_l(−2), forcing d₂:E₂^{0,2}→E₂^{2,1} to be injective, since there is no incoming differential and every possible later outgoing target vanishes. Here n=i=2, so E₂^{2(i−n),2n−i}=E₂^{0,2} is exactly the written candidate of weight 2n=4, yet its E∞ piece is zero.

### Complete relevant stalk table

All terms below are geometric stalks at 0 with their F_q-action; omitted terms are zero.

| (p,q) | E₂^{p,q} | Weight | Total degree |
|---|---|---:|---:|
| (0,0) | Q_l | 0 | 0 |
| (2,0) | Q_l(−1)² | 2 | 2 |
| (0,1) | Q_l(−1)² | 2 | 1 |
| (2,1) | Q_l(−2)² | 4 | 3 |
| (0,2) | Q_l(−2) | 4 | 2 |

The map d₂^{0,1} is an isomorphism (in geometric bases the exceptional intersection matrix is [[−2,1],[1,−1]], determinant 1), and d₂^{0,2} has rank one; the surviving quotient at (2,1) is Q_l(−2), giving R³a_*Q_l. The latter rank conclusion needs no sign convention for the Gysin map, though with orientations its two components have opposite signs. Both sides of d₂^{0,2} have weight 4, so purity supplies no reason for this differential to vanish. Every center, component, and crossing is defined over F_q; there is no hidden extension-of-scalars issue.

## Verified primary sources for the check

- Katz, N. M. (2012). *Convolution and equidistribution: Sato–Tate theorems for finite-field Mellin transforms* (Annals of Mathematics Studies, Vol. 180). Princeton University Press. Chapter 15, p. 77, author-hosted manuscript: https://web.math.princeton.edu/~nmk/mellin357.pdf . Verified source ref: `turn410813417view0` (title `turn172431317view0`; publication metadata `turn203528644search7`). It supplies the Legendre family, purity, SL₂ geometric monodromy, and local unipotent blocks; the local weight-4 and compact-support counterexamples are the explicit deductions above.
- Riou, J. (2010, December 7). *Théorème d'annulation, d'après S. Saito & K. Sato*. https://www.imo.universite-paris-saclay.fr/~joel.riou/doc/annulation.pdf . Verified source ref: `turn503605167view0`, Theorem 2.1 (purity), Proposition 2.3 (normal-crossing higher direct images), and the displayed Leray sequence following Corollary 2.5. The double-blowup computation is an independent application, not an example quoted from Riou.

## M01 qualification corrected

In `records/research_context_motives.md`, M01 now has kind “unpursued implication / qualification,” explicitly retaining “ou le cas échéant” and avoiding an unsupported claim that the first formulation was withdrawn.
