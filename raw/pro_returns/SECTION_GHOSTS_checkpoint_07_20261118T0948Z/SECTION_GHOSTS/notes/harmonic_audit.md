# Harmonic audit: SQ A.134 dependency, A.137 and A.139

## Outcome and exact historical scope

The supplied A.137 and A.139 proofs were read in full. Their common input A.134, its mixed-exponent lemma A.90, and the named historical finite certificates are absent from the recovered source. This run reconstructs the needed theorem with the exact rational coefficients and the special local centres used by A.139, using a **new** finite initialization and a complete infinite refinement proof. No claim is made to have opened or rerun the historical list of 611 centres, its 1833 tests, or the absent A.90 source.

The six results E.160–E.165 in `sections/part_E_harmonic_audit.tex` prove:

1. Ordinary initial local points everywhere and six exact quadratic root-symbol products.
2. The exact root-stabilizer intersections for every refinement exponent divisible by four, including maximal abelian subfields.
3. A compatible mixed-exponent construction yielding the completed harmonic triple, with every fixed local centre eventually retained exactly and infinitely many private integral support primes in each coordinate.
4. Uniform values of the proper Brauer class on the genus-33 curve, excluding a rational point and any everywhere locally matching new squareclass at the puncture `c`.
5. The actual cyclic degree-eight genus-three cover, finite group of order 4096 and class eight, every local sheet, a central-extension descent without an arithmetic splitting, and the real-cusp comparison.
6. The larger actual quotient of order `2^136`, its faithful 128-vertex path-chain model, exact lower-central layers and nonzero weight-seventeen commutator.

Thus A.137 and A.139 are confirmed in the historical register as theorem statements reconstructed in this run. The confirmation concerns the stated **locally matching** sections. Neither theorem asserts that this pair has no unrestricted integral section of the same nilpotency class. The main all-depth ordinary-pair question remains unaffected.

E.163 does not audit the separate A.134 nomenclature for its “common field” or the canonical obstruction `gamma_(C,c)` from missing A.128. Those auxiliary formulations are unnecessary for A.137/A.139 and have not been silently certified.

## The arithmetic mechanism that replaces the missing A.90

Use `h=1/2`, `R=529/382`, `r=1119169`, `Q=139r=155564491`, and

`(a0,a1,ah)=(529/382,147/382,(13Q)^2/191)`.

The private valuations at 23, 3 and 13 are respectively 2, 1 and 2. The valuation at 191 is −1 in every coordinate. These four valuation tests remain unchanged under all fresh-prime fourth-power coefficient twists used in the recursion.

For the two simultaneous radicals at a boundary, the signed radical field meets the cyclotomic field in exactly

| Boundary | Intersection |
|---|---|
| 0 | `Q(sqrt(-1146),sqrt(-382))` |
| 1 | `Q(sqrt(382),sqrt(191*23*13*Q))` |
| h | `Q(sqrt(191),sqrt(-3))` |

For `4|m`, the relation lattices of the two radical exponents are `(m/2)Z²` at 0 and h, and `{(ma/4,mb/4):a+b even}` at 1. The extra quarter-product relation in the middle row is essential. Treating the two radicands as independent would give a wrong prime-selection condition.

The proof also establishes that the maximal abelian subfield of each complete splitting field is the chosen cyclotomic field. A positive real radical inside an abelian extension of Q has rational square; the private valuations then put every possible abelian Kummer eigenmonomial back into that cyclotomic field. This is an actual field-intersection argument, not an assumption that every CRT class meets a splitting set.

A CRT automorphism can fix the required roots precisely when it fixes the indicated biquadratic field. Consequently the recursion may prescribe its actual local unit residues without incorrectly imposing `q=1 mod m`. Its six compatibility characters are precisely the six global root-symbol products.

At 2 choose the root classes `(5,3,5) mod8`. The two negative symbols in coordinate0 cancel at the real place by taking its initial real root negative. The remaining negative dyadic symbol in coordinate1 cancels at139, by choosing that local root nonsquare. An early tentative note located this latter cancellation at17; exact calculation disproved that tentative bookkeeping, and the final proof and certificate correctly use139. All other symbols are positive.

The only initial nonunit roots are `v17(X1)=1` and `v457(Xh)=1`. The positive rational normalizers `(1,17,457)` remove them and preserve all six products by rational reciprocity. The first prime factors have signs `(−,+,+)`; later factors are positive. The coefficients themselves stay positive because their exponents are even.

At each step all previously frozen centres remain literally unchanged. At a new private prime, previously chosen coordinates have roots by its boundary Frobenius condition; subsequently chosen coordinates are forced to have residue1 by triangular congruences. Every other prime is handled by either an already retained local point or the uniform Weil bound. New roots are units everywhere and squares at the fixed character-ramification primes, so every subsequent root-symbol identity is individually trivial. This is the invariant that makes the induction continue indefinitely.

## Executed finite certificates

### `code/check_harmonic_audit.py` and `.json`

The code uses only exact Python integers, rational arithmetic, trial division and modular exponentiation. It passed all checks.

- All661 primes at most5000 outside the nine-prime exceptional set are checked. There are660 interior residue solutions and one smooth branch solution at457, above `T=h`.
- All nine special primes are checked directly, including exact `T2=31/2`, `T17=1+a1*17^4`, and `T139=Tr=h+ah`.
- The dyadic roots are certified modulo256 with derivative valuation2, preserving the specified classes modulo8 under strong Hensel lifting.
- Every odd special ratio has valuation divisible by4 and a fourth-power unit residue. The code retains an actual residue root with the required quadratic character.
- The complete nontrivial root-symbol list is: coordinate0 with both characters at2 and infinity, and coordinate1 with its second character at2 and139. All six global products are+1.
- It verifies primality of `r`, the exact product coefficient, `F(c)/a=-rho²`, `d/(2rho)=(1088951437/2)²`, both exceptional flipped sheets, and the residue-square statements used for the uniform Brauer evaluation.
- The initial large-prime argument is not delegated to code: `p+1−66sqrt(p)−64>0` for `p>5000`. The variable-exponent bound and infinite recursion are proved in the text.

### `code/check_harmonic_large_quotient.py` and `.json`

The quotient itself has `2^136` elements and is not enumerated. The exact faithful chain representation uses128 vertices and256 edges overF2. The boundary matrix has rank127, hence its cycle space has dimension129.

The deck group is `(C4)^2 ⋊ C8`, where odd powers of the last generator swap the first two coordinates. The kernel is exactly `H/closure(H²[H,H])`, by the fundamental cycles of a spanning tree. The four weight-four seed commutators normally generate the fourth lower-central subgroup. Thereafter the exact recurrence is `M_(j+1)=(x−1)M_j+(y−1)M_j`.

The executed dimensions for classes4 through18 are

`124,121,115,107,97,85,71,55,41,29,19,11,5,2,0`.

Starting with `[x,y]` and successively commuting with `xxxxyxyxyyyyyyy` gives the sum of all128 x-edges, nonzero. This was evaluated both by the kernel recurrence and by multiplying the full expanded word in the faithful semidirect product. The unreduced word has length196606 and SHA256

`3e8f023407c75f7d79955cbbb7bde75ce31670d5a1241a6e56d04c6ec58fc5c0`.

This establishes exact class17; the augmentation-ideal nilpotency index alone would only provide an upper bound and was not substituted for this calculation.

## Primary sources opened and exact locators

The standard inputs are narrow; all new field intersections, constants, finite groups and infinite constructions are proved in the current text.

| Source | Exact use and locator | URL and retrieval reference |
|---|---|---|
| Milne, *Fields and Galois Theory*, v5.10 (September2022) | Theorem5.30 and Remark5.32, printedpp75–76; perfect Kummer pairing and eigenmonomial field description | https://www.jmilne.org/math/CourseNotes/FT.pdf ; `turn596689933view0`, `turn918571783view2` |
| Milne, *Algebraic Number Theory*, v3.08 (19July2020) | Theorem8.31, printedp147; Chebotarev for an actual conjugacy class in the compositum | https://www.jmilne.org/math/CourseNotes/ANT.pdf ; `turn596689933view1`, `turn918571783view3` |
| Milne, *Class Field Theory*, v4.03 (6August2020) | VIII§5.8–5.10, printedpp246–247, and dyadic formula p248; III§4pp110–115; rational Hilbert reciprocity and exact local symbols | https://www.jmilne.org/math/CourseNotes/CFT.pdf ; `turn918571783view1`, `turn848023079view0`, `turn848023079view1`, `turn272775791view0` |
| Deligne1974, *La conjecture de Weil:I* | Formula(1.5.1)p275 and Theorem(1.6)p276; smooth-projective curve count, subtracting the explicitly counted boundary | https://www.numdam.org/item/10.1007/BF02684373.pdf ; `turn918571783view0`, `turn848023079view2`, `turn848023079view3` |
| Milne, *Lectures on Étale Cohomology*, v2.21 (22March2013) | Theorem14.9 and Remark14.10pp96–97; Proposition14.12p97; Theorem21.1p130; geometric vanishing and arithmetic group/étale comparison without a section | https://www.jmilne.org/math/CourseNotes/LEC.pdf ; `turn645125004view0`, `turn325969975view0`, `turn325969975view3` |
| Colliot-Thélène, AWS2015 notes, revised30May2015 | §4.4p20 residue exact sequence; §3.2 and Theorem3.4pp14–15 continuity and Brauer reciprocity | https://www.imo.universite-paris-saclay.fr/~jean-louis.colliot-thelene/AWS30MAI2015.pdf ; `turn977470022view0`, `turn915128779view0`, `turn915128779view1` |

Existing bibliography keys `RootMilneFT`, `CohMilneANT`, `RootMilneCFT`, `RootDeligne1974` were reused. New keys `LitMilneLEC2013` and `LitColliotThelene2015AWS` are written in `notes/literature_references.bib` with verified version and locator notes.

Search/access log: searched `Colliot Thelene Skorobogatov Brauer Grothendieck group purity curve residue exact sequence pdf theorem3.7.2`; retrieved the primary author-book cached passage, but direct author PDF links returned404. Opened the Springer2021 book record and verified metadata only. It was not used as an opened theorem source. Then opened Colliot-Thélène's author homepage, followed its AWS2015 link, and read the needed residue exact sequence there. The inaccessible book is not a new bibliography dependency.

## Independent reviews

- Parent full-read E.160–E.162: positive, including relation lattice, monomial basis, signed CRT step and full limits.
- Cohomology sibling full-read E.160–E.162 and independent certificate rerun: positive; exact signed fields, maximal-abelian argument, sequential new-prime conditions and root-symbol reset checked.
- Parent full-read E.163–E.164: positive, including all flipped sheets, nonsplit central descent and real-cusp pullback.
- Cohomology sibling full-read E.165 and independent code rerun: positive; exact normal-generation and module recurrence checked, dimensions and word SHA reproduced.
- Parent full-read E.165 and code read/rerun: positive; exact deck group, cycle rank129, faithful path kernel, four-seed normal generation, right-augmentation recurrence, all dimensions and the individual weight17 witness checked.

The historical register and its generator now mark A.137/A.139 confirmed, with explicit replacement-initialization wording. The register remains90 rows:83confirmed,2repaired,5pending at the time of this update. No unrelated row was changed.
