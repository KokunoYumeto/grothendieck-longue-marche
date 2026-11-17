# Independent root review of A.47

Reviewed 2026-11-16 05:07–05:10 UTC against the complete working proof,
the existing formal proofs of A.40 and A.43, and the exact program.

## Outcome

The proposed finite-family theorem passes review. Its scope is the actual
regular-head refinement and its first scalar central refinement. It proves
neither cofinality nor the existence of a full involution of parity one.

## Points checked

1. The natural even-weight module of degree nine over F2 is simple. For any
   nonzero even-weight vector, a three-cycle meeting its support and its
   complement gives a weight-two difference. All pair-vectors span the module.
   Since nine is odd, the full permutation module is the direct sum of the
   trivial module and this eight-dimensional module. Shapiro and the
   perfectness of A8 and A9 give H1(A9,V)=0.
2. We read and reran `work_A/check_A47_affine_A9.py`. It verified the
   order-seven equations, the exact head order 181440, all 256 possible
   coboundaries, and simplicity. There are 1024 admissible lift pairs and
   256 coboundaries. The chosen lift pair is not a coboundary, so the
   generated subgroup cannot be a complement. Simplicity then gives the
   full group 2^8:A9. No enumeration of that larger group is being claimed.
3. The joint kernel over one simple head is a submodule of a finite direct
   sum of nontrivial simple modules. Such a module is semisimple even though
   the group algebra in this characteristic is not semisimple. Its
   submodules have no trivial quotient or invariants. The joint bundle is
   consequently perfect and centerless; its splitting is unnecessary.
4. A common nontrivial quotient of distinct bundles would be perfect and
   would have a nonabelian simple quotient A9. A map from a product of
   perfect bundles onto A9 factors through one bundle, since the factor
   images are commuting normal subgroups. This identifies two head
   kernels, contradicting their distinctness. Thus the stated product
   independence is valid, including the induction step.
5. The A5 support orbits are regular. The actual induced wreath maps
   therefore give the claimed quotient of Pi, with its finite invariant
   family of kernels. The image of R is all of M: the quotient M/q(R)
   has no A9 composition factor because it is a quotient of K/R, yet
   it is perfect and has only A9 and cyclic-two composition factors.
   It must be trivial.
6. The proofs of A.40 and A.43 require finite perfect centerless bundles
   and regular permutation orbits, not simple bundles. The canonical
   finite perfect central-cover image, the use of R=[R,Pi], the actual
   section over C, literal cusp fixation, and preservation of the
   specified C-frames therefore apply. The next scalar central refinement
   stabilizes by the same perfectness argument.
7. For the general affine-family variant, differing identifications of a
   simple head may twist the module by automorphisms of that head. The
   argument uses a direct sum of these nontrivial simple twists, so it does
   not require every module to be invariant under every outer automorphism.

The regular-head condition remains material. The separate orbit-one
construction requires a different proof of its actual central extension.
