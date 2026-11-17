# Independent post-freeze algebraic checks

Requested by the root transcriber after the transcription freeze. No images opened; no transcription or supplied context altered. These are conditional algebraic deductions from the frozen expressions, not decisions between handwriting alternatives.

## 1. Power maps on the nonsplit conic

Let `C/Q` be `x²+y²+z²=0`, let `K=Q(i)`, and put `u=(y−ix)/z` in `K(C)`. If σ is the nontrivial element of `Gal(K/Q)`, fixing x,y,z, then

\[
u\,\sigma(u)=\frac{y^2+x^2}{z^2}=-1,
\qquad \sigma(u)=-u^{-1}.
\]

This is the **semilinear action on rational functions**; the corresponding real structure on the coordinate of complex points is `u↦−1/bar u`.

The coordinate really identifies `C_K` with `P¹_K`: one inverse parametrization is

\[
[U:V]\longmapsto[i(U^2+V^2):U^2-V^2:2UV],
\qquad u=U/V.
\]

For a positive integer n, the map `f_n` defined over K by `f_n^*(u)=u^n` descends to the **given Q-form C** precisely when its pullback commutes with σ. On the generator u the two composites are

\[
\sigma f_n^*(u)=(-1)^n u^{-n},
\qquad f_n^*\sigma(u)=-u^{-n}.
\]

They agree exactly for **odd n**. This proves the root's conditional claim for all positive degrees, not just the cubic.

### Cubic and global formulas

The frozen scan049, lines4–10, gives

\[
X=-x(x^2-3y^2),\quad Y=y(y^2-3x^2),\quad Z=z^3.
\]

Directly, `Y−iX=(y−ix)^3`, so the induced u coordinate is exactly `u³`; there is no remaining sign discrepancy. These homogeneous polynomials have no common zero on C: a common zero requires z=0, and then y²=−x² gives `X=−4x³`, forcing x=y=0, which is not a projective point. Thus the cubic formula is a morphism on the entire conic.

More generally, define rational-coefficient homogeneous polynomials X_n,Y_n by

\[
Y_n-iX_n=(y-ix)^n,\qquad Z_n=z^n.
\]

Then `X_n²+Y_n²=(−z²)^n` on C. For odd n the triple lies on C, whereas for even n it lies on the **split** conic `X_n²+Y_n²−Z_n²=0`. This also explains why a quadratic expression can be rational over Q yet fail to be a self-map of the nonsplit conic; frozen scan051 lines53–60 explicitly verifies the split-sign equation, and lines63–65 labels a separate map “n impair.” The exact assignment of these objects to all arrows of the handwritten diagram remains a reading matter.

### Edge cases and limits

- n=1 is the identity. Nonzero negative integral n give degree |n| maps and obey the same parity calculation, if that extension of the question is desired.
- n=0 is a constant map to `u=1`, not an embedding of function fields. It does not descend: that point is not fixed by `u↦−1/bar u`. Keep the main assertion stated for positive-degree maps.
- The criterion is for this specified power map on this specified Q-form. It is not, by itself, a classification of all maps, all twists, or all possible changes of source/target coordinates.
- Characteristic zero matters to the displayed sign distinction; it should not be silently transferred to characteristic2.

### Is the argument already in the supplied context?

`context/hua_project/138.modern.tex`, subsection **“Les endomorphismes de la conique (pages48 à54)”**, lines970–1004, explicitly gives the coordinate u over Q(i), the power-map interpretation, the cubic, and the distinction between the plus-sign and split-sign conics. Lines990–995 answer the rational-function question “oui” but do **not** state `σ(u)=−1/u` or the odd-n descent criterion. The present calculation therefore **adds the ground-field/descent qualification** to Hua's account; the coordinate and cubic themselves must be credited to the supplied reading and the actual frozen source.

Searches made in the supplied context: `impair|antipod|descente|conjugaison` in Hua; `conique|impair` in all four LM source transcriptions; `y ?- ?i ?x|y ?\+ ?i ?x|y-ix|y\+ix|puissance.*[nN]` and `puissance.*impaire|endomorph.*conique` across context TeX/Markdown. No explicit version of the odd-power descent calculation was located. This is a bounded search result, not an assertion that no equivalent fact occurs anywhere in the archive.

## 2. The q-start1 reversal: general proof and the difference between Aut and Out

Let

\[
L_\nu=\langle\lambda_0,\ldots,\lambda_\nu\mid
\lambda_0\lambda_1\cdots\lambda_\nu=1\rangle,
\quad a=\lambda_0,\quad P_j=\lambda_1\cdots\lambda_j,
\quad P_0=1.
\]

Then `P_ν=a⁻¹`. Take the frozen scan085 line22's **conditional lower-index1 reading**, `q_j=P_(j−1)`. The inserted tuple in lines19–21 gives, uniformly for `1≤i≤ν`,

\[
t(a)=a,\qquad
t(\lambda_i)=q_j\lambda_jq_j^{-1}
=P_jP_{j-1}^{-1},\quad j=\nu+1-i.
\]

This includes the last tuple entry `t(λ_ν)=λ₁` because `q₁=P₀=1`. Its image of the relator telescopes:

\[
a\,(P_\nu P_{\nu-1}^{-1})
(P_{\nu-1}P_{\nu-2}^{-1})\cdots(P_1P_0^{-1})
=aP_\nu=1.
\]

More generally,

\[
t(P_k)=P_\nu P_{\nu-k}^{-1}=a^{-1}P_{\nu-k}^{-1}.
\]

Applying t to the image of λ_i now yields

\[
\begin{aligned}
t^2(\lambda_i)
&=t(P_{\nu+1-i})\,t(P_{\nu-i})^{-1}\\
&=(a^{-1}P_{i-1}^{-1})(a^{-1}P_i^{-1})^{-1}\\
&=a^{-1}\lambda_i a.
\end{aligned}
\]

Consequently `t²=Inn(a⁻¹)` with the convention `Inn(c)(g)=cgc⁻¹`. In particular t is an automorphism: it commutes with `Inn(a)` since it fixes a, and `Inn(a)∘t` is its inverse. These word identities also extend to the free profinite completion, with a continuous inverse; this follows from the finite-word maps and their explicit inverse, not from a numerical test in finitely many ranks.

### Rank2 calculation and order

For ν=2 put `a=λ₀,b=λ₁`, so `λ₂=(ab)⁻¹=b⁻¹a⁻¹` and `q₂=b`. Then

\[
t(a)=a,\quad
t(b)=b\lambda_2b^{-1}=a^{-1}b^{-1},\quad
t^2(b)=a^{-1}ba.
\]

For ν≥2, a is noncentral, so **this representative is not an involution in Aut**. Its **outer class** is an involution, and has exact order2: its induced reversal on the distinct peripheral abelianization classes is nontrivial. For ν=1 the group is cyclic and the displayed map is the identity, so “an outer element of exact order2” needs ν≥2. The free/profinite square identity does not establish that the stated map is the geometrically intended lift, or prove the subsequent Galois commutation identities.

This distinction is material to the source: frozen scan085 lines9–13 writes an operation of Z/2 into the automorphism-level object `tilde A_ν`; the lower-index1 formula corrects the relator obstruction but **does not by itself furnish an actual Z/2→Aut homomorphism**. The natural geometric operation after moving the basepoint is an outer action. A final note should preserve this issue and the margin “vérifier ?,” rather than call the uncertain formula fully verified.

### The q-start0 alternative

For the lower-index0 alternative, `g_j=aP_(j−1)`. Each interior image is `Inn(a)` of the corresponding q-start1 image, but the tuple's last entry remains λ₁ rather than `aλ₁a⁻¹`. Thus the full proposed relator image is

\[
a\lambda_1^{-1}a^{-1}\lambda_1,
\]

nontrivial for ν≥2. This is exactly the obstruction already identified by Hua, lines1358–1364; it must be stated conditionally because the frozen lower index is `unsure{0|1}`. ν=1 has no such interior term, and should not be included in the obstruction claim.

### Relation to Hua's replacement lift

`context/hua_project/138.modern.tex`, lines1348–1367, gives another replacement lift

\[
t_H(\lambda_i)=h_i\lambda_jh_i^{-1},\quad
j=\nu+1-i,\quad h_i=(\lambda_{j+1}\cdots\lambda_\nu)^{-1}.
\]

Since `P_ν=a⁻¹`, one has `h_i=aP_j`; conjugation of λ_j by P_j equals conjugation by `P_(j−1)`. Therefore

\[
t_H=\operatorname{Inn}(a)\circ t,
\qquad t_H^2=\operatorname{Inn}(a).
\]

The two lifts have **the same outer class**. Hua already supplies the relator-preserving replacement and the q-start0 obstruction, and expressly says neither displayed lift is derived from the geometry of `z↦1/z`, which moves basepoint0. The root's calculation **adds the exact square and the direct validation of the frozen lower-index1 alternative**, rather than discovering a new outer reversal.

Context searches: exact `q_i` in the four LM transcription files and supplied Esquisse; `renvers.*ordre circulaire|renvers.*ordre.*lacets|ordre.*renvers` across context. The only directly matching reversal formula located was Hua lines1348–1367. `LM_140-1_text.tex`, scan21 lines1203–1223, has a globally cancelled general peripheral-conjugator draft `u(l_i)=q_i l_(σ(i))q_i⁻¹`, but no exact replacement for this reversal lift.

## Suggested concise conclusions for the root's notes

1. **Own conditional deduction:** On `x²+y²+z²=0`, coefficient conjugation sends `(y−ix)/z` to its negative reciprocal, so the specified power map descends from Q(i) to the given Q-conic exactly for odd positive degree. This adds a field-of-definition qualification to Hua's conic subsection and supplies a possible explanation of “n impair” without identifying every uncertain arrow.
2. **Conditional verification / unresolved lift question:** The q-start1 reading preserves the relator and has square `Inn(λ₀⁻¹)`; q-start0 produces Hua's nontrivial commutator. The former is therefore a valid outer involution for ν≥2, but not the strict automorphism-level involution apparently advertised, so the manuscript's “vérifier ?” retains a real issue.
