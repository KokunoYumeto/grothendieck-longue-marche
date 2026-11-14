# Independent complete E76 proof and program read

Status: PASS. This is a mathematical proof and complete program-source audit, with inspection of the saved mathematical outputs. It is not an independent execution of the finite enumeration or source certificates. No peer source or output was edited.

The full statement and proof in `sections/E_wajnryb_surface_covers_agent.tex` were read, together with all seven mathematical programs listed below and their actual source/compression helpers. The earlier `E74_S4_initial_engine_metadata` directory is historical provenance; the final statement is E76.

## Exact free and surface maps

The displayed inverses prove that every chain generator and the additional four-branch twist is an actual automorphism of the free group on the named generators. The word `omega=v*iota(v)` uses the generator-inversion automorphism `iota`; its second half is not the reverse of the first half. Pairing its oppositely oriented edges identifies all vertices and gives one face and 2g edges. The Euler characteristic is 2-2g, so its attaching map is the stated closed oriented surface presentation.

Every automorphism preserves this literal boundary word. Consequently it descends through the actual normal-closure quotient defining the surface group. The boundary-twist equality is checked by literal reduced words, with the positive inner conjugation retained; quotienting by the boundary kills that exact inner automorphism. The complete A/B/C/C-prime relations are checked as free automorphisms in the stated genera before applying any finite quotient.

The composition convention is also exact. If `a*b` means `a` after `b` on the free group, then precomposition sends a representation rho to rho composed with a, and point permutations multiply as `p(ab)=p(b)[p(a)]`. Simultaneous postcomposition by a target automorphism commutes with precomposition. Hence the finite action on epimorphism/Aut-orbits is well-defined, and the saved inverse permutations have the printed orientation.

## Exhaustive finite cover sets

For S3 the code enumerates every tuple, evaluates the surface relation, and checks generation. Every S3 automorphism permutes its three involutions; these generate S3, so there are at most six automorphisms. The six distinct inner automorphisms attain this bound. Thus the literal six-element orbit computation is the full Aut-orbit computation. Epimorphic tuples have trivial automorphism stabilizer. The outputs have 60 orbits in genus two and 2520 in genus three.

For S4, the Cayley propagation runs over all 36 admissible images of the specified transposition/four-cycle generating pair. Every candidate is checked on all generator edges; exactly 24 bijective homomorphisms survive and coincide with the inner automorphisms. The full subgroup enumeration has 30 subgroups and all eight maximal proper subgroups, with orders 6,6,6,6,8,8,8,12. These literal subsets provide the complete epimorphism test. Every one of the 24^4 tuples is tested. The result has 900 Aut-orbits, retaining both target orbits of lengths 540 and 360. The independent two-handle count agrees with the literal polygon relation count.

## Entire induced source and whole fibres

Every evaluation pair is the printed word pair `(y_i,a_i^2)` in the old finite target. The `Source` helper uses the actual six B/F cosets, the actual fixed Schreier section and the exact word `t_q b t_(qb)^-1`. The root coordinate recovers both original free generators. Its right wreath-product law is checked against the full permutation arrays for all source-generator products. Faithful compression discards an orbit only with a saved intertwiner for both source generators, so the original target evaluations are recoverable.

All 97 named N generators are evaluated in every source. Every sixth power and every pair commutator is identity. Their image is therefore abelian of exponent dividing six, which kills the complete closed subgroup N-prime N^6, and proves factorization through the actual G6. This is a whole-kernel assertion, not a selected-word inference.

The fibre programs retain the exact E17 words and their zero exponent sums. All 37 original correction/basis words have identity value in the new sources, and the entire G6-kernel factorization retains every further correction in the stated word coset. The first and seventy-third powers of every target generator agree; the finite periods six and twelve supply every multiplier lift congruent to one modulo 72. Thus all 864 old finite parameters have the asserted literal evaluation values.

For generation, each saved point intertwiner is verified on every target point and every old/corrected generator. It makes the corrected group conjugate in the full symmetric group to the old target. Separately, every corrected generator is a literal word in the old target generators; this proves subgroup inclusion. Finite equal order then proves equality with the full old target. Both ingredients are present, including the two-orbit S4 handling. No target-kernel invariance is inferred from a numerical order alone.

All three tests have exactly three corrected generator tuples among the 24 origins. The result remains a complete finite source/fibre comparison; it assigns no value to the full-GT character in E65.

## Read-only source hashes

| Program | SHA256 |
|---|---|
| `de_wajnryb_free_model.py` | `75818812474ba6682a8b9a5df004aefc54dc7020e52fcdcde8fe55fc7d90b964` |
| `de_wajnryb_s3_model.py` | `eed3174e840d3da39cb650616c356b895522b646561c005ad71e166815c0bdf0` |
| `de_wajnryb_s4_model.py` | `51cbff5b14f5f436bc4853ef75c639821362916d935f027def48857912346719` |
| `de_wajnryb_s3_source.py` | `d6aabdf87af0e06cf9c582388ff69d2edac78de11863e96bcd9ac37fa385872c` |
| `de_wajnryb_s3_fibres.py` | `6634453764dafb37c5511d0b4ac914f68dc65b74856a1a018d04dc152ff52b40` |
| `de_wajnryb_s4_source.py` | `184b2a54fdd824ae373896e4e5f778873edd91c59b707cd8d9da98b9d9b51016` |
| `de_wajnryb_s4_fibres.py` | `1910b4184ac6def837f3ed9911696291ac4d68870750d776a2cea6af762a1ec5` |

No new mathematical correction was required. The final proof already contains both the elementary S3-automorphism bound and the old-target inclusion needed in its generation argument.
