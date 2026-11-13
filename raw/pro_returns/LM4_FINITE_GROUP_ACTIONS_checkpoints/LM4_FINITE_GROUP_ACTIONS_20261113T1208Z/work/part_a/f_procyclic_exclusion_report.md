# F.10 — the concrete forgetting kernel has no centralizer direction

For the geometric `A5` on the twelve-punctured sphere, the procyclic closure of every nonidentity discrete pure mapping class meets the actual completed `A5` centralizer trivially. In particular, the full `Zhat` subgroup constructed in F.9 is excluded from the residual centralizer, even though all thirty-six forgetting constraints kill it. For that word, the single involution `beta=(12)(45)` detects the entire procyclic direction.

The argument supplies actual finite quotients. The exact configuration homeomorphism `Conf_(n-1)(C) = C × C* × M_(0,n)` embeds the pure sphere mapping class group as a direct factor of the pure plane braid group. Artin's faithful action and integral truncated Magnus substitutions give a separating family of upper unitriangular integer representations. Injectivity of the Magnus expansion is proved directly by the coefficient of the monomial formed from the successive maximal syllables of a reduced word.

One truncation separates a discrete `x` from its conjugate by an element of `A5`: such an element exists because the discrete `A5` centralizer is trivial. Taking blocks indexed by `A5` makes the finite group act by its actual left-regular block permutation. Reducing this integral representation modulo `p^k` gives finite quotients of the actual finite-index semidirect product `PΓ_(0,12)⋊A5`, hence continuous representations of its full completion.

The unipotent logarithm is a finite rational matrix polynomial. For every prime `p`, the image of `x^u` is `exp(u_p log R(x))`. Centrality forces `u_p` times the same nonzero rational logarithm commutator to be zero in `Q_p`; all coordinates `u_p` therefore vanish. This proves the full profinite assertion without assuming any correspondence between an unspecified lower-central quotient and the full completion.

The F.9 word belongs to the actual discrete `A4` centralizer: it is the monodromy of the full orbit map in F.7.8 before forgetting. The text now specifies the algebraic icosahedral basepoint, the exact Möbius matrix of `beta`, and the polygonal transport path to F.9's `b=5+4i`. Equivariant transport preserves the specified `A4`. The executed exact matrix certificate verifies the resulting `A5` labels. `A4` and this transported `beta` generate `A5`. Thus `beta` already fails to commute with the discrete word, and the representation argument excludes every nonzero profinite power.

No covering statement about arbitrary profinite elements by closures of discrete cyclic subgroups is asserted. The whole residual centralizer remains open.

## Executed formula certificate

`code/procyclic_magnus_f10.py` and its JSON/stdout pass all assertions. The program checks the maximal-syllable coefficient on 484 nonempty reduced words; actual pure Artin automorphisms on the degree-three rank-40 tensor algebra; eleven exact logarithm/exponential power identities; 180 block-conjugation and 60 block-product identities for the actual A5 action on `Inn(F5)`; and finite power reductions modulo `p^2` for `p=2,3,5,7,11`. Its scope is precisely the displayed formulas. It does not claim to compute a separating tensor degree for the F.9 word.

## The separate six-point attack

`code/second_a4_c3_attack.py` and its JSON/stdout preserve the exact common-`C3` quotient model, the actual `A5` Möbius matrices and vertex labels, and the explicit algebraic basepoint path. These executed checks passed 180 matrix generator checks and 720 vertex-label checks. The model supplies the exact based involution on the six-punctured quotient, not an arbitrary matrix conjugator.

The auxiliary files `f9_c3_johnson_probe.py`, JSON, and stdout use numerical crossing discovery followed by exact integral Magnus calculations. They currently find that the first nonzero outer Johnson class of the F.9 word is invariant under the induced involution. This is a negative exploratory outcome, and those files remain explicitly labelled as discovery. They do not provide an exact smaller separating quotient and are not inputs to F.10.
