# E.103: complete odd-primary quartic abelian sections

## Result and exact source

The statement treats the plus Fermat quartic `x^4+y^4+z^4=0`, with the twelve coordinate cusps removed. For every odd prime, and simultaneously for the prime-to-two product of coefficient rings, it constructs an actual section of the arithmetic abelian extension. The construction is a four-coset formula applied to the actual tangential section over `F=Q(zeta_8)`. It is defined in the original extension, is independent of a chosen lift, and is continuous on each of the four open cosets. The displayed torus-module section then moves this origin to toric value zero.

Relative to that origin, the full geometric-conjugacy section space is

`(completed F^*)^2 x ker(Norm F/Q) x R^3`.

The actual coordinate-unit map is `(a,b,k,e) -> (Norm(a),Norm(b))`. It is onto, and the complete fibre over any prescribed toric pair is `ker(Norm)^3 x R^3`. Both directions are given by the literal norm section and division by its values. For the Fermat covering coordinate `t=-(x/z)^4`, the corresponding Kummer pair is four times this map.

## Coefficient comparisons and evaluated factors

The three homogeneous degree-four maps to `E_+: y^2=x^3+x` satisfy `Phi Psi=Psi Phi=[4]`; their differentials are an explicit basis. The generalized Jacobian extension is killed by four through the unique map `j` with `p j=[4]`. These identities supply the actual odd Tate splitting and its inverse, including all factors of four and sixteen. The eleven-dimensional torus splitting and inverse are retained as exact rational matrices with denominators powers of two, and all four Galois permutations are checked.

The elliptic factors are evaluated rather than left as named cohomology groups. The explicit two-isogeny to `y^2=x^3-4x` identifies the L-functions. The original Martin--Ono eta-product formula gives a positive Mellin integral at one. An elementary two-isogeny descent proves algebraic rank zero and rational torsion `C2`. Ciperiani--Stix Theorem 18(2) then gives the maximal divisible Weil--Chatelet group `Q/Z`. A fixed isomorphism to that subgroup, followed by the compatible Kummer inverses, gives each odd Tate cohomology factor exactly `R`, with its actual inverse map and topology.

The Shapiro map is written at cochain level, with the inverse, coboundary sign and literal norm trace. The field has class number one and units `mu_8 x <1+sqrt(2)>`. Thus the whole section space is `R^6 x restricted_sequences(I,R)` and each toric fibre is `R^6 x restricted_sequences(I',R)`. The primewise multiplicities are respectively `2,11,5` and `0,9,3`, for the prime two, primes one modulo eight, and the remaining odd primes. The topology is uniform congruence convergence of the prime-indexed sequences; arbitrary product topology is not substituted.

All rational abelian coefficient pushouts, including the two-adic one, are also evaluated. Compactness of the Galois source bounds every continuous rational cocycle, proving the exact scalar-extension map on cohomology. Their spaces are `Q_l^6 x c_0(I,Q_l)` and the corresponding fibres use `I'`. The real obstruction of E.18 is transported explicitly under rationalization. Integral section targets retaining the two-primary abelian quotient remain empty. No odd nonabelian lift is inferred from these coefficient computations.

## Primary-source evidence

The owned source-evidence ledger records the opened original Martin--Ono theorem and proof, the full Fite--Lorenzo Garcia--Sutherland Proposition 3.1 and homogeneous map, Milne's ideal-class Minkowski bound, and the exact Ciperiani--Stix Theorem 18(2). The separate prime restrictions on its Tate--Shafarevich direct-sum assertion are not used. The Martin--Ono publisher endpoint that returned an access failure is not represented as opened; the official author PDF and publication record are the evidence. Raw third-party papers are excluded from the deliverable.

## Executed certificate

The Python certificate and its owned PARI source verify:

- all nine affine basepoint charts, the three differential pullbacks, the degree-four character identities, both two-isogenies and their inverse square-coordinate formulas;
- the eleven-dimensional torus maps and every Galois permutation;
- 53 actual cyclotomic prime factorizations and 128 eta-series/elliptic coefficient comparisons;
- 10,000 finite-coset average identities, 400 section products, 2,000 Shapiro cocycle identities, 500 inverse comparisons and 2,000 trace comparisons;
- 3,072 norm-coordinate inverses and 1,746 completion transitions;
- unconditional PARI field certification, class number one, elliptic rank bounds `[0,0]` and torsion order two.

A fresh author rebuild from copied owned Python and GP sources reproduced the entire Python stdout, GP stdout and JSON byte for byte, without omitting fields. The exact hashes and comparisons are retained in `e_quartic_odd_author_rebuild.json`. The initial JSON-serialization failure concerned a SymPy integer object and was corrected by an explicit integer conversion; it did not change a mathematical assertion or output value.

## Proof and visual checks

The standalone seven-page section compiled with the existing local LuaLaTeX runtime, with no overfull boxes, undefined references or missing characters. All seven rendered pages were actually inspected at 90 dpi: equations, tables, references and margins are legible, with no clipping, overlaps or missing text. The exact image and PDF hashes are in `e_quartic_odd_visual.json`.

Root has independently read the complete proof and both programs, and independently opened the four primary references. Its fresh copied-source rebuild follows this author freeze; this report does not claim that later execution has already occurred.

## Remaining original scope

This completes the displayed quartic odd-abelian and rational-abelian coefficient targets and all their toric fibres. The actual odd intrinsic class-two and higher geometric quotients remain the next target within E.23. The four-coset abelian average is not assumed to provide a nonabelian section; its central lifting class must be computed in the actual next extension.

## Completed independent verification

E.103 computes the unrestricted global odd-primary and prime-to-two abelian section spaces of the plus quartic, and the rational abelian pushouts at every prime. The actual degree-four coset section, integral isogeny inverses and evaluated elliptic cohomology give free factor R^6 and restricted prime multiplicities2,11,5. The exact toric norm map is onto, with fibre multiplicities0,9,3 and free factor R^6. The higher odd-primary and rational nonabelian targets retain their actual lifting questions; full profinite source section sets retaining the two-primary abelian obstruction remain empty.

Root read the complete proof and all owned mathematical source programs and ran a complete copied reconstruction. The exact verification record is ledger/root_e103_audit.json. Every complete stdout and JSON byte agrees without exclusions.
Root independently opened and checked all four primary theorem inputs and their precise use in the proof.
