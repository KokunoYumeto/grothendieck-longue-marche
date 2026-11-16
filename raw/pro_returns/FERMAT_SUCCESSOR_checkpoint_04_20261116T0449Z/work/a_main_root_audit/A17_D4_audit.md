# Independent audit of root A.17 and D.4

Audited 16 November 2026. No mathematical defect found. A notation
translation in the historical transcription should be made explicit.

## A.17 torus quotient

The power-map square with the torus is cartesian on schemes. The
tripod-to-torus map identifies geometric abelianization with the
cocharacter module `Zhat(1) tensor (Z³/Z(1,1,1))`. Its restriction to
the Fermat subgroup has kernel exactly `F'` and image the entire target
torus module, because multiplication by n identifies that module with
`n F^ab`. Surjectivity on both geometric kernel and arithmetic quotient
gives the arithmetic extension comparison. Permuting the coordinates
preserves this square and fixes `[1:1:1]`, so the equivariant splitting
is a genuine splitting of this quotient.

The completed-cohomology step is valid. On a divisible countable cofinal
sequence, the groups `H0(Q,mu_n)` are finite and hence Mittag–Leffler.
Thus there is no inverse-limit degree-one defect. The invariant Tate
module is zero, so inflation–restriction gives exactly the S3-invariant
part of the Kummer H1 group. For every abelian group M, including its
2- and 3-torsion, `(M³/diag M)^S3=0`: a transposition changes a lift by
`(b−a,a−b,0)`; if this is diagonal then its third coordinate forces the
diagonal element to be zero, so a=b. A second transposition gives a=c.
This is not an invalid averaging argument at2 or3. Zero invariants also
give uniqueness of the geometric conjugator. No full extension splitting
is inferred.

## D.4 local radicals and the prime two

Independently opened Milne's complete primary Class Field Theory v4.03,
I Theorem4.8 and Corollary4.12, printed pp47–48. Local Kronecker–Weber
does identify `Q_l^nr(mu_l∞)=Q_l^ab`, and hence
`I_l^+=G_(Q_l^ab)` with the specified decomposition group.

If an l^n-th root of a lies in the abelian extension, its finite Kummer
cocycle factors through the abelianized local Galois group. Commuting two
elements yields the displayed identity. For odd l, a cyclotomic value2
exists and makes the cocycle a coboundary, proving that a was already an
l^n-th power in Q_l. For l=2, a cyclotomic value−1 makes twice the
cocycle a coboundary; this is exactly
`a in ±(Q2×)^(2^(n−1))`. Conversely its radical is a product of a square
root and a root of unity, both abelian. Thus no factor at2 is omitted.

The finite-level Kummer annihilator is the orthogonal of the span of
the valuation and logarithm vectors, with both multiplied by2 at2.
Perfect finite-module duality works even when these vectors do not form
a free submodule. The actual image is compact, and the proposed
rank-at-most-two lattice is compact, so equality of all reductions gives
equality in the inverse limit. The logarithmic exponents are correct:
`v_l(d)=v_l(p^(l−1)−1)−1` for odd l, and
`v2(d)=v2(p²−1)−3`, followed by the extra factor2 in the image, at2.
This handles p=l and the Wieferich cases.

The root's exact finite program was replayed in this separate directory:
all120 single cases and all6 joint cases passed. The replay outputs are
`a_main_root_kummer_replay.out` and `root_local_kummer.json`.
The finite unit moduli are sufficient: l^(n+1) for odd l and
2^(n+1) for the radical criterion at2; the logarithm representative at2
is computed modulo2^(n+2), giving d modulo2^n.

## Historical convention

The actual supplied transcription, scan167 equation(357), labels
`T_infinity(G_m)` with the twist `(-1)`; this is retained in
equations(358)–(365). The modern convention in the paper is `(1)`.
Therefore D.3/D.4 should explicitly say that they translate that label,
rather than silently treating the transcription as modern Tate notation.
On the cyclotomic kernel the coefficients have trivial action either
way, and the underlying Kummer maps and their computed indices are
unchanged. This is a convention clarification, not a mathematical
counterexample to D.4.
