# Finite-checks literature and exact boundaries

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 18 November 2026. The runtime does not separately expose the effort setting. No priority is claimed.

## Sources actually opened

1. Bellingeri, P. (2004). On presentations of surface braid groups. *Journal of Algebra, 274*, 543–563. arXiv:math/0110129v2 (5 February 2003), primary PDF https://arxiv.org/pdf/math/0110129. Theorem 1.2, printed page 2, was opened and checked. Its hypotheses are a closed orientable surface of genus at least one and the surface braid group on n strings. For n=g=2 it gives precisely the four same-generator relations, four mixed different-handle relations, two same-handle relations and one surface relation used in A.51. The commutator convention is aba^{-1}b^{-1}. The source does not supply the new relative completion or finite quotient; those are proved locally.

2. Lercier, R., Ritzenthaler, C., Rovetta, F., & Sijsling, J. (2014). Parametrizing the moduli space of curves and applications to smooth plane quartics over finite fields. *LMS Journal of Computation and Mathematics, 17*(Suppl. A), 128–147. https://doi.org/10.1112/S146115701400031X. Primary full text https://arxiv.org/html/1403.0562v4 opened; Theorem 3.3 and Section 5.4 inspected. The representative-family theorem assumes characteristic zero or at least seven. The implementation data discussed in Section 5.4 cover prime fields 11 through 53. Thus this source cannot be cited as an exhaustive F3/F5 census. Its Theorem 3.1 has characteristic at least five for automorphism classification, a different and weaker use. The attached earlier return's explicit pointed normal forms were independently reconstructed instead.

3. The primary project https://github.com/RationalPoint/excessive was opened while searching for a genus-three census. Its excessive/pointless-curve computations do not supply the all-pointed-curve witness census required here.

4. Ozman, E., Pries, R., & Weir, C. (2021 version). The boundary of the p-rank 0 stratum of the moduli space of cyclic covers of the projective line. https://arxiv.org/abs/1907.05684. Only its primary abstract page was opened. The abstract describes general p-rank strata and a trielliptic existence result for odd p congruent to two modulo three. No theorem from it is used in B.82, and no claim is made to have checked its full proofs.

## Literature searches made

- `plane quartic curves finite fields F3 F5 complete census database genus 3 curves`
- `smooth plane quartics over F_3 F_5 enumeration isomorphism classes database`
- `Lercier Ritzenthaler Rovetta Sijsling smooth plane quartics database F3 F5 files 2015`
- `cyclic covers degree 7 supersingular characteristic 2 branch points F8`
- `supersingular factors cyclic degree seven covers projective line characteristic two`
- `"cyclic" "seven" "supersingular" "characteristic two"`
- `"degree 7" "supersingular" "characteristic 2"`

Two independent search engines were used for the quartic census and cyclic-seven literature checks. No located primary source supplied either the claimed universal B6 answer or the exact finite rational-branch exclusion in B.82. This is a search report, not a priority assertion.

## Exact remaining boundaries

- S2 is proved by the independent F8 Lang-cover certificate. The class-number and geometric deck argument do not use A1 or the unproved converse to a criterion. The section interpretation uses only the forward path-lifting/Kummer implication, assigned B.68 by the parent.
- S3 is proved by a fully specified finite quotient of order 9·5^40, verified by independent methods. The five-kernel has exponent five and exact nilpotency class three; its lower central Lie dimensions are 40,24,4,0. The linear shear span is four-dimensional, not eight-dimensional.
- S6 is complete for the four requested finite assertions. It does not replace the separate geometric/profinite proof checks. For A.12 the blind independent implementation starts from the geometric transvections; the original Schreier derivation was separately rerun.
- B6: all 364 cubic characters of the specified F5 quartic are settled, with 96 witnesses. Least-prime-first means prime three and extension degree eight. First-field-first means extension degree three and prime thirteen, from B.34. These are different minimizations.
- B6: the complete pointed F3/F5 input census and all smallest-prime first character fields are now certified. Character existence alone does not imply a class-number witness. No covering Cartier action has been computed for all the high-degree character fields. The census also does not cover quartics lacking a point over the original base field. Neither the full witness table over every extension nor the possible geometric realization of a nonabelian-only obstruction is asserted.
- B5: B.82 exhausts the cyclic-seven family with at most seven branch points in P1(F8), including all geometric twists. The proof certifies that the list of eight supersingular minimal polynomials is complete in this degree range. Branch sets of eight or nine rational points, branch fields larger than F8 and arbitrary prime-to-two correspondences remain outside it. This does not settle the universal B5 statement.

## Reproducibility

New Python code uses Python 3 with NumPy and SymPy. `s2_f8_witness.py` additionally uses python-flint 0.9.0; the independent `verify_newcerts.py` S2 verifier uses plain integer arithmetic. C++ census programs compile with a C++17 compiler, for example `g++ -O3 -std=c++17`. The complete scripts, inputs and outputs are in the own `code/` directory. The supplied-program reruns are separately classified in `carried_reruns/RERUN_LEDGER.json`; their source hashes identify the unchanged inputs in the original archive. Those supplied programs are not described as independently reimplemented.
