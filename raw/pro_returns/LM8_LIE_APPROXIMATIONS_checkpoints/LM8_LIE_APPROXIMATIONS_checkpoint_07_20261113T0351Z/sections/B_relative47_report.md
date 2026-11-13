# Relative S3 compatibility for §47

**The associated-graded problem is solved. The prescribed profinite word equation remains unresolved.** The advance is a surjectivity theorem in every positive weight, together with exact dimensions and complete rational rank-two basis checks through weight nine. The theorem retains the correct rank-seven relative source.

## Files and anchors

The manuscript supplement is `sections/B_relative47.tex`, with identifiers B.25–B.28. The corresponding references, result ledger, coverage ledger, and reading ledger have the same prefix. The computation is `code/b_relative47.py`, with its executed `.out`, exact `.json` certificates, and `.csv` dimension table. Its metadata generator is `code/b_relative47_metadata.py`.

The source anchors are §47, cote 140-3, folios 415–420, scans 229–240, especially equations (14), (15), (20), and (30). The supplied LM2 return B.m3, E.3–E.4, and B.g12 was read directly. The current background scan folders do not contain the original cote-140-3 images; opening the external original PDF failed, and a hanging download was cancelled. This return therefore does not claim a fresh image inspection. Its mathematical results define the relevant maps explicitly and prove their properties independently of a manuscript transcription.

Hain (1998), §1, printed pp. 47–48, was opened in the primary Numdam PDF. It supplies the precise definition of relative completion; its discussion explicitly includes finite reductive quotients. The finite-index radical assertion and the lifting theorem are proved here, with the former also matching B.8.

## The two maps remain distinct

Let B=C2*C3 and p:B→S3. Its kernel K is free of rank two. The level-two inclusion sends the abstract free basis X,Y to (rs)^2,(sr)^2 in K. The quotient φ instead sends X,Y,Z to s,sr,r^−1. These are different maps.

The composite v=pφ has kernel N of rank seven. Relative completion of B has radical U(K)=U2, whereas relative completion of F2 with respect to v has radical U(N)=U7. The quotient induces a relative map that is the identity on S3, with radical map d:N→K. The absolute comparison has radical map c:N→F2. Identifying U(K) with U(F2) by the level-two inclusion does not identify c with d.

The common source is the eight-punctured sphere obtained from the degree-six rational map

`T(λ)=27λ²(1−λ)²/[4(1−λ+λ²)³]`.

There are three A punctures above 1, three B punctures above 0, and two C punctures above infinity. The covering map sends their homology classes to 2X,2Y,3Z. Filling the A and C punctures sends the three B classes to X,Y,Z and the other five to zero. The source H1 representation is `2·trivial + sign + 2·standard`; the joint projection has kernel `sign + standard`. Both matrices and the Belyi factorization were checked exactly.

## The all-weight lifting theorem

The precise map is

`R_n: sder_out(L7)_n^{S3} → sder_out(L2)_n × sder_out(L2)_n^{S3}`.

Every source derivation is tangential at all eight punctures. Equivariance ensures descent through the covering map: that map is the maximal free-Lie quotient with trivial deck action. Tangentiality ensures descent through filling. These statements make R_n well defined modulo inner derivations.

For an arbitrary base special outer derivation a, the cabling construction substitutes A_sum/6 and B_sum/6 into each of its three peripheral conjugators, using the same conjugator on every puncture of a cluster. The sum relation is preserved because the three cluster sums satisfy the tripod relation. Its two projections are exactly (a,0).

For a target invariant b, first choose an invariant representative and make the sum of its three conjugators zero. Change its inner representative to fix the third puncture. Extend this derivation using only B0,B1, fixing the other six punctures, and average over the deck group. The total peripheral relation remains zero. The cover projection vanishes since both B0 and B1 become 2Y, and a homogeneous Lie polynomial of degree at least two in one generator vanishes. The averaged target inner discrepancy vanishes by the zero-sum conjugator normalization. The pair of projections is therefore (0,b).

The two constructions prove surjectivity for every positive n. Degree one has zero rank-two outer targets and needs no special lifting argument. Thus C(q)+T(q) is compatible for every special invariant q. If q is nonzero, C(q) has the same absolute projection but is incompatible. The ambiguity persists after quotienting by inner derivations.

## Exact computation through weight nine

| n | Source invariants s | Base special a | Target invariants t | Joint kernel | Compatible source |
|---|---:|---:|---:|---:|---:|
| 1 | 4 | 0 | 0 | 4 | 4 |
| 2 | 5 | 0 | 0 | 5 | 5 |
| 3 | 38 | 1 | 1 | 36 | 37 |
| 4 | 120 | 0 | 0 | 120 | 120 |
| 5 | 693 | 3 | 1 | 689 | 690 |
| 6 | 3163 | 0 | 0 | 3163 | 3163 |
| 7 | 17356 | 6 | 2 | 17348 | 17350 |
| 8 | 92930 | 4 | 1 | 92925 | 92926 |
| 9 | 524166 | 13 | 4 | 524149 | 524153 |

The compatible image has dimension t. The joint kernel has dimension s−a−t, and the compatible relative source has dimension s−a. These follow from the proved surjectivity, not from a conjectural matrix rank.

Source dimensions use the exact equivariant Witt formula and the special-derivation exact sequence. The first-degree peripheral centralizer subtraction is retained. This computation does not construct huge rank-seven Lie matrices and does not infer exact ranks from random or finite-field samples.

Every rank-two special invariant basis vector through degree nine is independently reconstructed by exact rational row reduction. For each, the program verifies the antisymmetry and special equation, constructs the averaged zero-sum equivariant conjugators, and checks both projections of both lifts. The explicit q7 from B.12 is also checked with its actual Lyndon coefficients. The certificates are retained as rational associative-word coefficients. These checks exhaust the indicated finite-dimensional rational target spaces. Source tangentiality and the eight-puncture relation are proved symbolically in B.26 for all weights.

## What this does and does not resolve

LM2 E.4 correctly observes that the absolute unipotent completion of C2*C3 is trivial. Retaining S3 corrects that problem, but also changes the source radical from rank two to rank seven. B.25 makes that correction explicit, and B.26–B.27 solve the resulting existential associated-graded compatibility problem. Thus q7 passes this particular test even though its pentagon defect is nonzero by B.12.

In the literal profinite equation, a given automorphism of F2 induces a particular action on its open subgroup N. Its relative action is not chosen freely after the absolute action is known. The q7 leading term alone does not provide that relative action. The existence of compatible and incompatible graded lifts with the same absolute projection makes this distinction explicit.

The pro-ell lifts of q7 in B.12 do not supply a full profinite word. For ell≥5 the quotient F2→S3 does not factor through the absolute pro-ell completion, so that word cannot simply be evaluated there. No full profinite lift of q7 is constructed by this supplement.

The remaining task is to compute the actual induced rank-seven action from a full profinite word, or prove an additional reconstruction theorem that determines it. Only then can one evaluate the normalized equation ξ=(φ(ξ)σ(φ(ξ))^−1)x^ν on that prescribed action, or compare all pentagon solutions with it. No assertion of simultaneous filtered peripheral formality, integration to a prescribed profinite action, or automatic full §47 compatibility is made. B.28 records this residual as Open in the scope of this audit.
