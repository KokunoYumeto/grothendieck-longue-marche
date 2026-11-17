# Independent mathematical audit of cote 122

Research-phase audit only. No frozen transcription file was altered. All source locators below refer to `MPL_122/pages/MPL_122_122_scanNNN.tex`; `L` numbers are physical lines in those frozen files, not reconstructed manuscript lineation. These are conditional mathematical deductions, not new readings of the scans and not evidence that the manuscript supplied the necessary hypotheses.

## A. Derived invariants and the extra degree

**Witnesses:** scan 020:L9–20 (application of derived invariants and the circle splitting); scan 022:L20–42 (perfectness, equivariant `u`, unresolved transposition sign); scan 024:L13–23 (the `−2n−1` shift and explicit request to verify commutation).

Let Λ be a commutative ring, let K be a bounded complex perfect over Λ, and let T be its invertible monodromy action. Put D(K)=RHomΛ(K,Λ), with the contragredient action S=(T⁻¹)∨. For the infinite cyclic group, the usual two-term resolution gives

\[
R\Gamma(\mathbf Z,K)\simeq\operatorname{Cone}(T-1:K\to K)[-1].
\]

For a module in degree zero this is the complex `[K → K]` in degrees 0 and 1, up to the harmless cone differential convention. Its dual lies in degrees −1 and 0, so shifting the dual by −1 returns it to degrees 0 and 1. Since

\[
S-1=-S(T^\vee-1),
\]

the dual differential differs from the differential for the contragredient action by an invertible factor. Thus, with the orientation of the circle fixed,

\[
R\Gamma(\mathbf Z,DK)\simeq D(R\Gamma(\mathbf Z,K))[-1],
\qquad
R\Gamma(\mathbf Z,DK[-2n])\simeq D(R\Gamma(\mathbf Z,K))[-2n-1].
\]

This supports the displayed shift in scan 024. It is not literal unshifted commutation. It also does not determine the signs in a chosen morphism of triangles, and it is not an automatic assertion for arbitrary profinite inertia, coefficient categories, or nonperfect complexes.

**Suggested note (own idea; high confidence, explicit cone computation):** “Compute derived cyclic invariants by `Cone(T−1)[−1]`, and give the dual the contragredient action `(T⁻¹)∨`. Dualising changes the two-term degrees by one and yields `RΓ(ℤ,K∨) ≃ RΓ(ℤ,K)∨[−1]`, explaining the manuscript’s `−2n−1`. The calculation fixes this degree shift, while the triangle signs and an algebraic inertia analogue remain separate questions.”

### Equivariant versus forgotten u

**Witness:** scan 022:L26–40.

Perfectness gives `RHomΛ(DK,K) ≃ K ⊗ᴸΛ K`, with its induced action. Consequently

\[
\operatorname{Hom}_{D(\Lambda[\mathbf Z])}(DK[-2n],K)
\simeq H^{2n}\bigl(R\Gamma(\mathbf Z,K\otimes^L_\Lambda K)\bigr).
\]

The ordinary `H²ⁿ(K ⊗ᴸ K)` on the page can describe the forgotten class, but does not itself encode the full equivariant lift. For an infinite cyclic group the two-column spectral sequence yields

\[
0\to H^1(\mathbf Z,H^{2n-1}(K\otimes^L K))
\to H^{2n}(\mathbf Z,K\otimes^L K)
\to H^0(\mathbf Z,H^{2n}(K\otimes^L K))\to0.
\]

Thus an invariant ordinary class may admit more than one equivariant lift; an ordinary class need not even be invariant. This is a precise research distinction, not a reason to alter the frozen transcription.

### Coefficient and twist cautions

Perfectness alone does not make `Hⁱ(DK)=HomΛ(H⁻ⁱK,Λ)`: derived duality can have Ext contributions. A field, suitable self-injective coefficient ring, or explicit torsion-freeness/derived bookkeeping is needed for the groupwise dual notation used below. Under the convention `D=RHomΛ(−,Λ)` and a trace `RΓc(M,Λ(n))[2n]→Λ`, the corresponding formula is `RΓc(M,Λ)≃D(RΓ(M,Λ))(-n)[-2n]`; the twist is **−n** with this convention. This last sentence is a conditional calculation from the stated trace convention, not a claim that the manuscript specifies an étale trace formalism.

## B. Pairing degrees and the middle exact sequence

### The λ and μ targets

**Witness:** scan 024:L35–49.

If W₀ is an oriented closed manifold of dimension `2n−1`, a map `α:Hⁱ(P)→Hⁱ(W₀)` pairs with `H²ⁿ⁻¹⁻ⁱ(W₀)`, giving the degree `2n−1` pairing μ. A map `β:Hⁱ(P)→Hⁱ⁻¹(W₀)` instead pairs with `H²ⁿ⁻ⁱ(W₀)`, giving the degree `2n` pairing λ. The displayed λ/μ shifts are therefore mutually consistent with the respective identifications with β/α. Identifying the actual maps requires more than this degree check.

### Correct successor term

**Witnesses:** scan 022:L34–40 (the triangle); scan 030:L32–36 (the ambiguous successor exponent); scan 032:L6–17 (live comparisons and middle sequence).

Assume M is a compact oriented `2n`-manifold with boundary W₀ and coefficients for which groupwise duality is valid. The pair triangle gives

\[
\cdots\to H^{2n-i}(M)^\vee\to H^i(M)\to H^i(W_0)
\to H^{2n-i-1}(M)^\vee\to H^{i+1}(M)\to\cdots.
\]

The exponent of the successor dual is **`2n−i−1`**, because it is `Hⁱ⁺¹(DK[-2n])`. This explains the mathematical attraction of the alternative minus sign at scan 030:L33 without replacing the ink-priority plus sign.

Assume additionally `Hʲ(M)=0` for `j>n`. The portion at the two middle degrees is

\[
0\to A\to B\to C\xrightarrow{u}D\to E\to F\to0,
\]

where

| Letter | Group |
|---|---|
| A | `Hⁿ⁻¹(M)` |
| B | `Hⁿ⁻¹(W₀)` |
| C | `Hⁿ(M)∨` |
| D | `Hⁿ(M)` |
| E | `Hⁿ(W₀)` |
| F | `Hⁿ⁻¹(M)∨` |

These are the six potentially nonzero terms of the live sequence at scan 032:L15–16. The manuscript labels `B→C` “surj”; if that label and exactness are both retained literally, `u=0`. There is no general formal reason for that surjectivity, so it is a substantive point to check, not a harmless label. The larger proposed sequence at scan 032:L24–31 is entirely cancelled and cannot supply an additional settled theorem.

### Exactly what unimodularity would characterise

**Witnesses:** scan 028:L16–20 (ambient W criterion); scan 032:L13–22 and L24–31 (middle terms and cancellations); scan 034:L2–24 (special-fibre notation).

If `A=Hⁿ⁻¹(M)` is not known to vanish, even an isomorphism u leaves `B≃A` and `E≃A∨`; it does not force the link’s middle cohomology to vanish. Under the stronger assumptions that `n≥2`, M is compact and oriented, its boundary W₀ is connected, and its reduced integral cohomology is finite free and concentrated in degree n, the pair sequence becomes

\[
0\to H^{n-1}(W_0)\to H^n(M)^\vee
\xrightarrow{u}H^n(M)\to H^n(W_0)\to0.
\]

All other reduced boundary cohomology outside its top degree then vanishes by the same pair sequence. It follows that **W₀**, the boundary/link, is an integral homology sphere exactly when the middle integral pairing u is unimodular. Over a field the analogous statement uses nondegeneracy. The ambient manifold **W** is a different object: the criterion written at scan 028 is expressed through restriction/Gysin maps for `W−W₀`, and the pages do not identify that criterion with unimodularity of u. The stronger fibre vanishing required here is not established by the statements retaining `Hⁿ⁻¹(M)` in scan 032.

**Suggested note (own idea; high confidence under the listed additional assumptions):** “If the reduced integral cohomology of the page is finite free and concentrated in degree n, the pair sequence identifies the two middle link groups with the kernel and cokernel of u. Hence the link W₀ is an integral homology sphere exactly when u is unimodular. This is a conditional boundary criterion, not a criterion for ambient W, and it uses stronger vanishing than the manuscript has yet obtained.”

## C. What the limit argument has to supply

**Witnesses:** scan 028:L40–41; scan 030:L26–30 (“par passage à la limite”).

For the cyclic action, the two-term model gives

\[
0\to\operatorname{coker}(T-1:H^{i-1}K\to H^{i-1}K)
\to H^iR\Gamma(\mathbf Z,K)
\to\ker(T-1:H^iK\to H^iK)\to0.
\]

It is therefore possible for the cohomology of the total mapping torus to vanish although the fibre has nonzero cohomology. The elementary abstract example `V=ℚ`, `T=2` has zero invariants and coinvariants, and `Tᵐ−1` remains invertible for every positive integer m. It disproves an unrestricted inference from these mapping-torus groups to the fibre groups, but it does not refute an unspecified **limit** argument with different coefficient assumptions.

For a finite coefficient module an automorphism has finite order, so a finite cyclic cover can kill its monodromy. The transition maps and the treatment of the residual degree-one group-cohomology term still have to be supplied before identifying a filtered limit with fibre cohomology. The manuscript does not specify that system at this point; recovering it is the right next question, rather than replacing “par passage à la limite” by an argument about just one mapping torus.

## D. The unfinished regular-sequence example

**Witness:** scan 035:L2–9; the entire example, including `Q=`, lies inside `\deleted{...}`. The live claim is only that certain finiteness conditions “ne semblent pas stables par conoyaux,” with a dual kernel statement.

The following check takes place in ordinary modules over a commutative ring A. It does not assume that the uncertain category symbols on the page have been deciphered.

Assume f is a non-zero-divisor on M and g is a non-zero-divisor on `M/fM`. Then:

1. The map `M/fⁿM→M_f/M`, sending `m mod fⁿM` to `m/fⁿ mod M`, is injective. If the latter is zero, `fᵏ(m−fⁿx)=0` for some k, so f-regularity implies `m=fⁿx`.
2. For `n≥m`, the transition `M/fᵐM→M/fⁿM` by multiplication by `fⁿ⁻ᵐ` is injective, again by cancellation of powers of f. Every fraction has a power-of-f denominator, proving `colim M/fⁿM≃P=M_f/M` exactly as displayed.
3. Multiplication by f on P is surjective, and `ker(f:P→P)≃M/fM`. Every element of P is killed by some power of f. If P is nonzero, these facts imply P is not finitely generated as an ordinary A-module: finitely many f-power-torsion generators would give a single power fᴺ killing P, contradicting `fᴺP=P≠0`.
4. The filtration of `M/fⁿM` has successive quotients `fʲM/fʲ⁺¹M≃M/fM`. Induction therefore shows that g acts injectively on each `M/fⁿM`, and hence on their filtered colimit P.
5. One possible continuation would be `Q=P/gP`. In that case `Q≃(M/gM)_f/(M/gM)`; f is regular on `M/gM`, because `fm=gn` implies, modulo f, `n=fn′`, and then cancellation of f gives `m=gn′`. This continuation still has the same kind of displayed inductive presentation, so it cannot on its own be advertised as a counterexample to the unspecified adic finiteness condition.

Point 5 is a deliberately labelled possible continuation, not a proposed reading of the unfinished `Q=`. Another construction might have been intended; the cancellation prevents choosing one on the author’s behalf. In particular, ordinary non-finite-generation of P does not refute a finiteness condition formulated on the terms or structure of an inductive system.

**Suggested note (own idea; high confidence for modules, low confidence about intended application):** “For an ordinary module and an M-regular pair `(f,g)`, the displayed transition maps are injective, and g remains injective on their colimit `P=M_f/M`. The module P is f-divisible and elementwise f-power torsion, so a nonzero P is not finitely generated as an ordinary module. These checks validate part of the cancelled construction, but the unfinished `Q=` and the missing definition of the adic finiteness class prevent extracting a completed counterexample.”

## E. Check of the parent draft

At the time of this audit, draft notes RN020, RN023, RN034, RN036, and RN040 were checked. Their equivariant hypercohomology distinction, cyclic-duality shift, `T=2` caveat, successor exponent, and conditional link/unimodularity criterion are correct with the hypotheses they state. RN040 properly distinguishes W₀ from W and does not claim that the necessary stronger vanishing is present in the manuscript.

Confidence summary: high for the cone computation, the groupwise exact-sequence degree under its coefficient hypotheses, the conditional boundary criterion, and the module calculations; no claim to have settled the manuscript’s triangle signs, algebraic realisation, limit comparison, or final finiteness assertion.
