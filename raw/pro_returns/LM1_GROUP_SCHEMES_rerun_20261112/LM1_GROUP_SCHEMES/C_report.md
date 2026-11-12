# Part C research and computation record

| Request | Statements | Outcome |
|---|---|---|
| Item 2 | C.1, C.3–C.6, C.10 | refuted, with complete corrected theorem |
| Lead 1 | C.1, C.2, C.4–C.6, C.10 | refuted, with complete corrected theorem |
| C(a) | C.1–C.2 | proved |
| C(b) | C.3 | proved |
| C(c) | C.4–C.6 | refuted (centrality), with entire normal kernel determined |
| C(d) | C.2, C.7–C.9, C.11 | partly settled |
| C(e) | C.5–C.6, C.10 | proved |
| C(f) | C.3–C.6, C.10–C.11 | proved |

## Read and checked

The photograph of cote 140-3 scan 336 was opened and compared with the checked transcription in LM_C3-321-339. Context around scans 323–337 and the second-pass corrections was read. Scan 336 visibly has constant cyclic groups Z/n, not diagonalizable mu_n. It also visibly writes Gl(2), although all displayed generators have determinant one; the exact corrected image is SL2, with Gm cokernel for the literal GL2 comparison.

The attached Conrad PDF was extracted and read at Theorems 1.1, 3.2 and Appendix C Theorem C.1. Its author-hosted version was opened. The attached Brylinski–Deligne PDF was read at the Introduction and Theorem 7.2, which classify central extensions rather than the noncentral presentation kernel found here. Serre's official 1968–1969 Collège de France course report was opened at sections 1.1, 1.2 and 2.2. Section 1.2 is the exact cited theorem for a group acting on a tree with one edge as fundamental domain; C.9 proves the required arithmetic action and stabilizers for Z[1/2] and Z[1/3]. The Numdam metadata page for Serre's book was opened, but the whole PDF exceeded the browser's fetch limit. No unexamined theorem of that book is used as a proof substitute.

Searches included “Serre Trees SL2 Z[1/p] amalgam Gamma0(p) theorem” and targeted Numdam and author-hosted searches. No priority or novelty claim is made.

## Executed mathematics

Run `python code/C_presentations.py`. The run succeeded and every exact assertion passed. It writes `code/C_presentations.json`; its captured stdout is `code/C_presentations.out`.

The program enumerates every 2x2 matrix over F2, F3, F4, F5, F7, Z/4 and Z/9, checks determinants, computes closures under the named generators, and quotients GL2 by all unit scalars. It verifies the projective index against the square-class count. It also performs eight complete Todd–Coxeter enumerations for the abstract projective and special-linear point presentations for moduli 2, 3, 4, 5. All coset tables are retained, and every relator and inverse column is checked at every coset. The infinite cases are proved, not inferred from nontermination.

SymPy verifies the universal torus-conjugation relator and all four Gaussian-chart matrix identities over their universal Laurent rings. Rational counterexample words are checked exactly. The nilpotent scalar 1+e over F2[e]/e² and the Artin–Schreier element alpha³−alpha=1 over F27, and explicit unramified descent rings over Z/4 and Z/9 are checked by exact finite arithmetic.

## Corrections and conclusions

The literal sheaf sources are Gamma *_Z Ga and PSL2(Z) *_Z Ga. Their comparison maps have noncentral kernels over every nonempty base. A twelve-syllable universal kernel word and its twenty-four-syllable nontrivial commutator survive all faithfully flat extensions. Thus inverting six does not repair the presentation, and Steinberg/Matsumoto central K2 kernels do not describe this source.

Four explicit universal Gaussian-chart relation families normally generate the entire special-linear kernel. Their local normal-form proof works integrally, including nilpotents. The projective quotient additionally kills h(zeta) for all sections of mu2; in characteristic two this is stronger than killing the constant −I. GL2 is recovered by adjoining Gm with the explicit diagonal conjugation action.

The finite point presentations and the actual points of the sheaf pushout differ. In particular the abstract special-linear point presentation over F3 has order 24, while the actual sheaf A_SL(F3) contains an infinite-order kernel element obtained by Artin–Schreier descent. Both actual sheaf values over Z/4 are infinite, by an explicit unramified quadratic descent witness; a cubic unramified witness gives an additional infinite-order kernel element over Z/9 in the special-linear case. The program's finite coset tables are therefore labelled strictly as point presentations. Actual sheaf values over F2 and F4 are determined, and every finite-field value has the exact Frobenius-fixed amalgam description in C.8.

## Exact remaining work

C(d) is partly settled rather than declared complete: C.11 records the remaining simplification of the fixed subgroup `(SL2(F3) *_{C3} Fbar3^+)^Frob` and the complete descent calculations for sheaf points over Z/4 and Z/9. The proven infinite cyclic kernel subgroup, exact fixed-group formula, full matrix and point-presentation computations, and precise obstruction (nontrivial torsor descent of normal forms) are supplied. The smallest unresolved finite-field case is the special-linear sheaf value over F3 beyond the explicit invariant-group description. This is a limitation of this calculation, not a claim of a known open research problem.
