# Independent review of the residual-level criterion

Reviewer: topos agent. Date: 14 November 2026. Scope: Section 3 of
`D_all_prime_compatibility_gap.md`, with the exclusions in Sections 4–6.
The integrated D.30 and D.31 files were not changed.

The conditional equivalence passes review. In particular, the hypothesis
is a single bound (N_\ell\mid N\) for infinitely many coefficient primes
at which the actual local elliptic curve has good reduction. A finite
conductor for each residual representation separately does not provide
this bound.

I reopened the author text of Helm–Voloch, Proposition 6, author pp.6–7
(`tmp/D_HelmVoloch2011.txt`, the paragraphs beginning with the finite-flat
calculation and ending with the repeated eigenform). It gives the precise
local distinction needed here: if the good elliptic reduction is
supersingular, its residual representation over (\mathbf Q_\ell\) is
absolutely irreducible; if it is ordinary, its two inertia characters are
(1,\bar\chi_\ell). Thus a globally absolutely reducible residual
representation is in the ordinary case, and one can choose its first
character unramified at (\ell). This explicitly justifies the candidate's
finite-flat sentence even when reducibility is only visible over
\(\overline{\mathbf F}_\ell\). It is useful to retain this explanation;
finite-flatness alone should not be paraphrased as saying that every
inertia representation splits into two niveau-one characters.

The conductor comparison for the resulting character, the fixed prime
\(p\equiv1\pmod N\) in the density-one good set, and the Hasse contradiction
then give absolute irreducibility for all but finitely many members of the
chosen infinite set. Serre weight two and the fixed level bound give a
finite set of possible eigenforms. Equality of an algebraic integer with
the same rational integer modulo infinitely many distinct residue
characteristics forces equality, and density-one Chebotarev with
semisimplicity gives the rational representation comparison.

For the converse, the invariant sublattice is saturated and wild inertia
at (p\ne\ell) has finite image of order prime to \(\ell\), so reduction
cannot increase either the tame codimension term or the Swan term.
This supplies a bound for every integral stable lattice, not only a
selected elliptic Tate lattice.

The note correctly leaves the uniform bound unproved. Its factorial
cuspidal example is globally reducible and violates the ordinary elliptic
Hasse traces on the density-one good set. It is therefore not a
counterexample to the proposed statement for noncuspidal sections. The
finite-cusp issue after D.30 is also retained explicitly.

Primary source reopened: Helm, D., & Voloch, J. F. (2011). *Finite descent
obstruction on curves and modularity*. Bulletin of the London Mathematical
Society, 43(4), 805–810. Author PDF,
https://web.ma.utexas.edu/users/voloch/Preprints/modularity.pdf,
Proposition 6, author pp.6–7. No additional unconditional finite-ramification
theorem is inferred.
