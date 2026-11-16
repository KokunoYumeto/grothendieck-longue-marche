# Independent audit of A.57

**Result: PASS.** Read the complete separate candidate notes/fgh_A57_draft.tex and reran its certificate. The new rank-one argument was checked independently from the already approved A.56. It correctly completes the potential-good-curve normalizer criterion at every special p-rank, including coefficient prime two.

## Primary statements checked

Raynaud's original Theorem 1 and Proposition 1 on printed pages 179–180 were independently read from https://page-one.springer.com/pdf/preview/10.1007/978-0-8176-4576-2_7 , source turn883view0. Proposition 1 applies to the nilpotent Galois normalization over a regular base when its branch divisor is geometrically unibranch. Its first part gives geometric unibranchness upstairs; its second part gives constant component inertia and an étale inertia quotient near the component image. The draft proves the extra global conditions needed to use that local conclusion.

Independently opened Richard Crew's original paper at https://www.numdam.org/item/CM_1984__52_1_31_0.pdf , references turn909view0–1, and actually viewed the image of printed page 36, reference turn910view0. Corollary 1.8 and equation (1.8.2) give the stated unramified p-group p-rank formula. The cover to which it is applied is genuinely finite étale, connected and Galois; no formula for general ramified covers is substituted.

## Geometric connectedness and the global quotient

The proof first extends to a semistable source and then computes geometrically after the completed unramified extension. The normalization remains finite over the smooth proper base and its generic fibre remains geometrically connected. Its global functions form a finite integral R-algebra inside the generic field K, hence equal R. Stein factorization makes its special fibre connected. These arguments continue after the stated base changes and establish geometric connectedness.

If ramification is present, purity on the regular surface places its reduced branch support on the whole smooth irreducible vertical fibre. Raynaud then makes the reduced inverse image geometrically unibranch. A connected noetherian locally irreducible space has only one irreducible component. Thus its decomposition group is all G, and the constant inertia subgroup is normal in G. The quotient by inertia is étale near its entire special fibre, not merely a generic point; it is also étale on the generic fibre. This proves étaleness everywhere, which is the essential global step.

The unique main normalization is radicial over the smooth special inertia quotient. It has the same p-rank. The proof correctly avoids identifying the radicial degree with the full inertia order, so possible vertical multiplicities introduce no missing hypothesis. The unramified Deuring–Shafarevich calculation makes this main p-rank one. Raynaud's exceptional components have p-rank zero and the dual graph is a tree. Hence the good special covering Jacobian has p-rank one. Norm/pullback gives the old/new isogeny decomposition, and its Prym has p-rank zero. A.46 excludes every stable rational line in that Prym.

## Integral detector and arithmetic application

In genus at least two, the primitive vector's perpendicular space contains a vector outside its own line, even modulo two. Perfect integral duality lifts it to an exactly perpendicular primitive vector. Its finite torsion character defines an actual connected cyclic p^n cover after finite number-field descent; no special-order condition is required now. For n above the original vector's divisibility, the original vector is outside the Poincaré-dual line modulo p^n. The same generator of the actual normalized subgroup lifts to the covering group, with an arithmetic normalizer still having open image. Its stable proper line has zero Prym projection, hence is an integral deck invariant. The previously checked integral Schreier pushforward contradicts the Poincaré-dual separation.

For a degree-d cover of the specified punctured elliptic curve, the prime-to-p Galois-closure argument of A.56 applies to every odd p>d; it had no intrinsic congruence restriction. The new rank-one result removes the earlier arithmetic congruence condition. Genus one is covered by the cited existing isogeny criterion, and d=1, p=2 is separately covered by that original criterion. The final statement therefore really has all primes p>d and no extra unspecified exceptional set.

## Executed certificate and limitations

Command: python LM8_PUSH/notes/fgh_A57_certificate.py

The run returned PASS for all listed perpendicular-space checks in genera two and three over F2, F3 and F5, 40 divisible integral detector examples, 24 rank-one p-rank/Prym arithmetic checks, and all degree bounds d=1 through 32 against primes below 200. The uniform theorem follows from the structural proof rather than these finite ranges.

No mathematical correction is needed. The retained hypothesis is potentially good reduction of the proper curve, not only its Jacobian. No full fixed-subgroup comparison, cofinal refinement, or extraction of a root of the normalized generator is claimed.
