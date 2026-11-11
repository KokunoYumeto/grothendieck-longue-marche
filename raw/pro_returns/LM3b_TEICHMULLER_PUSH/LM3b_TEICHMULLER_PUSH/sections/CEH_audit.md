# Audit for Parts C, E and H(a)

## Primary texts read

We opened the supplied Boggi congruence-topologies paper, Boggi's 22 April 2026 automorphisms preprint, Boggi–Funar's curve/pants paper, Boggi–Zalesskii's restricted Magnus paper, Minamide–Nakamura's braid-automorphism paper, Nakamura–Schneps's refined-GT paper, and Hatcher–Lochak–Schneps. For Hatcher–Lochak–Schneps the embedded-font text extraction was unreadable, so supplied PDF pages 3–6 were rendered and inspected. We also opened the supplied Harbater–Schneps text and the prior LM3 reductions, using the latter only where the current prompt permits citation of established statements.

The web searches were: Boggi automorphisms and congruence-kernel statements; profinite normalizers of finite subgroups; genus-three congruence kernels; and exact bibliographic metadata. They located an additional primary result: Boggi–Zalesskii, *Finite subgroups of the profinite completion of good groups*, BLMS 57 (2025), 236–255, DOI 10.1112/blms.13193. We opened arXiv:2406.08639v2 and the publisher metadata. Its finite-p-subgroup normalizer theorem supplies C.3. We claim no priority for that application. We also opened Kent's *Congruence kernels around affine curves* (2014) to check whether centrality of the entire genus-three congruence kernel was known from the cited centralizer results; the final centralizer equality H.1 is proved directly, not borrowed from a broader assertion in that paper.

Manuscript scans 355 and 356 were visually inspected. Scans 361–363 were read in the supplied transcription; scan 363 is not present among the image files. The mathematical type-check at scan 361 favors the upstairs symbol in its normalizer. The free-rank formula supports the plus sign at scan 363. Neither is represented as a settled handwritten reading. The folio ambiguity 166/168 at scan 328 is immaterial to E.8.

## Executed computations

`python deliverable/code/ceh_checks.py` ran successfully. It uses only SymPy plus the independently written `ab_lie.py` module. It computes:

- rational deck characters for the rank-three and rank-five special-derivation spaces through degree four;
- a direct degree-three matrix calculation for the index-two deck action, with ambient dimension six, fixed dimension four, geometric dimension two, and combined rank five;
- exact cellular/Fox-chain calculations modulo three on a genus-five double cover of a genus-three surface, showing that a separating twist acts with rank one unipotent part of order three on ten-dimensional homology;
- the two-element sign-coherence calculation distinguishing two unrelated forgetting arrows from two arrows related by coherent relabelling.

`ceh_checks.json` contains the complete output, including the deck matrix and the 12-by-12 chain matrix. The rational deck computation alone is not a certificate about the full pro-2 factorization.

We subsequently obtained the required finite certificate for the index-two pro-2 cover. These commands were executed successfully:

```sh
g++ -std=c++17 -O3 deliverable/code/ceh_pro2_cover.cpp -o tmp/ceh/ceh_pro2_cover
tmp/ceh/ceh_pro2_cover deliverable/code/ceh_pro2_certificates.json > deliverable/code/ceh_pro2_cover.out
python deliverable/code/ceh_pro2_verify.py > deliverable/code/ceh_pro2_verify.out
```

The finite quotient is the free-group image in the units of the explicitly defined 121-dimensional truncated noncommutative algebra over F2; its kernel is fully characteristic by substitution. The C++ program represents polynomials by 128-bit integers and closes the two geometric Artin-twist automorphisms. Their based image has order 128 and their deck-conjugation orbit has 64 elements. For each candidate it solves a 39-variable F2 linear system allowing every truncated unit as a possible inner conjugator. Of the 64 integral degree-three candidates, 32 have no such intertwiner to any geometric deck conjugate. The first is the special derivation with conjugators [[X,Y],Y], [X,[X,Y]], 0. A.1 supplies its actual pro-2 lift without changing this finite image.

The file `ceh_pro2_certificates.json` records 64 explicit dual inconsistency certificates for that witness, one for every geometric deck conjugate. The independent Python verifier uses sets of literal words, reconstructs the candidate from group commutators, independently closes the geometric image and deck orbit, and checks the recorded row sums giving 0=1. It does not call the C++ code or repeat Gaussian elimination. All 64 certificates passed. `ceh_pro2_verification.json` records the complete verification metadata and certificate SHA-256. The certificate is stronger than an enumeration of actual inner group conjugators because it excludes all units with constant term one. We do not claim to enumerate the full automorphism group of the finite quotient.

## Substantive corrections and advances

The index-two covering is not characteristic. The image of restriction in an automorphism group is the inverse image of a deck normalizer, while the deck-normalizer quotient describes an outer automorphism group. Both test-cover maps on prediscretization cosets are injective in the full profinite and pro-2 settings. For the pro-2 assertion, we checked Boggi2020 Corollary5.4(ii) identifying the PURE genus-zero congruence closure with its pro-2 completion, then proved the required cohomology comparison for the full labelled-permutation extension by two Lyndon–Hochschild–Serre inductions. The comparison extends from finite to all discrete modules by FP-infinity and filtered colimits. This verifies the precise hypothesis of Boggi–Zalesskii2025 TheoremA/4.3 for the arbitrary dense embedding into the geometric pro-2 closure. It gives the geometric normalizer descent needed here.

Surjectivity is refuted for the index-two pro-2 cover by the finite certificate above. C.10 transfers that obstruction to the characteristic degree-four pro-2 cover through its intermediate index-two subgroup. Geometric lifts of the downstairs S3 act as all automorphisms of D4, allowing both putative factors to be adjusted to normalize the intermediate deck subgroup and descend. This would contradict C.5. No rank-five nilpotent enumeration was performed or claimed. Only the two full profinite surjectivity cases remain unresolved.

The elliptic involution comparisons require orbifold groups: cone points cannot be replaced by ordinary cusps without changing the upstairs curve. The open elliptic forgetting arrow has automorphism 2-group with pi_0=GT and pi_1=1; the full boundary pair also has pi_1=1. Its full pi_0 comparison remains conditional on a stated boundary-coherence assertion. The center C2 at the one-point elliptic level does not by itself create a surviving pi_1 after forgetting compatibility is imposed.

Boggi's full procongruence outer-tower theorem is reduced to Grothendieck's kernel and inertia language. It does not remove arbitrary finite-cover maps or quilt/base-point conditions from the separate comparison problems. The automatic-inertia step at the universal-curve group PΓ(1,3) remains explicit.

The genus-three kernel is isomorphic to the centralizer of the closed-surface fibre in the profinite one-point mapping class group. A concrete characteristic quotient π/L of order 64·3^258 gives a congruence representation which detects a separating twist, and hence contains information beyond the base symplectic representation. This does not prove the congruence subgroup property: all finite-cover homology representations factor through congruence quotients by construction.

## Remaining obligations

C.9 leaves the full profinite deck-normalizer/geometric factorization unresolved for both covers. Lifting the special pro-2 automorphism from C.5 to a full profinite peripheral automorphism is the exact missing route for carrying that certificate further. C.7 leaves the extension from normalizing the liftable geometric subgroup to normalizing the full upstairs geometric subgroup unresolved. E.9 leaves automatic nonseparating inertia unresolved; E.4 leaves coherent elliptic boundary pi_0 unresolved. H.5 retains C(3,0)=1 and the centrality/torsion questions without silently importing procongruence assertions. No quantum representation quotient was constructed.

## Independent cross-review of D and G

We independently checked D.1–D.3 against Nakamura's 1994 paper, pp. 94–97, Theorem 2.1.1 and Lemma 2.1.4. Their scope includes every nontrivial element in the full geometric profinite group, including an element supported at one prime. Boggi–Zalesskii's Proposition 3.6 permits every nonzero profinite exponent and peripheral simple curves, so the single-prime centralizer step is applicable even for one cusp. We found no mathematical gap in the determinant, finite-twist recognition, or uniqueness proofs. We also read manuscript 019, Proposition 5.2, pp. 13–15: its conclusion requires a connected curve over k, not geometric connectedness, and G.2 matches that scope. The whole-inverse-image division-cover argument, slope-one character, and trimmed-annulus estimate were checked; no gap was identified in that targeted proposition.
