# Independent audit of D.75

**Result: PASS.** I read the full staged proof and metadata in `work/part_c/d75.tex` and `d75_result.json`, compared the one-cusp substitutions with the audited D74 coefficient proof, and reread the exact D60 character, D61 normalization/boundary-generation maps, and D62 centralizer coordinates and all-unit continuation.

## The actual one-cusp pair and duplicated boundary map

The specified negative extension retains the actual commutator cusp `c`, reflection `v`, and quotient to `C2`. Its normalizer `D` is identified with the full dihedral group by the stated exponent and quotient-label inverse maps. Its two local reflection classes have self-normalizers and fuse through the actual D58 element `g` in `F`.

The restriction `F/L -> E/D` is an actual equivariant homeomorphism, and the transported extra action is exactly `e(fL)=efv^{-u(e)}L`. Hence the single-coset augmentation kernel restricts to the completed genus-one, one-boundary surface pair. The proof retains that pair rather than identifying its boundary with a pants cusp system.

The same continuous-Hom exact sequence and ordinary extension spectral sequences used in D74 apply to this module. Full surface-pair duality gives the same two dual fibre rows, with the actual mod-two orientation line and evaluation pairing. Thus the two positive-column `d2` maps are adjoints and have equal rank. Periodicity and the literal relative long exact sequence give the half-boundary rank without assuming either transgression vanishes.

Brown's full finite-coefficient hypotheses hold for both `E` and its actual peripheral normalizer. D58 supplies the one or two global section classes, while both boundary occurrences belong to the cusp class. Transport by the identity and the specified `g`, with the displayed coefficient action, identifies boundary restriction exactly with `(a,a_other) -> (r_S a,r_S a)`. The additional global normalizer factor, when present, has no boundary occurrence. Consequently the half-rank identity forces `r_S` to be onto.

The finite coset module detects any nontrivial element of the full cusp fixed subgroup: its two distinct fixed singleton cosets produce a moved cohomology class, whereas the restriction image is fixed by the cusp centralizer. This is the same literal transport argument checked in D74. It proves `C_F(v)=1`, not merely vanishing of its pro-2 image or first cohomology. The full peripheral dihedral conjugacy and D58 fusion then give the statement for every cusp reflection.

## Unique transporter and every unit exponent

The two displayed half-exponents belong to `Zhat`: a full unit is odd in the dyadic coordinate, and division by two is available at every odd prime. Direct substitution gives

- `c^((mu-1)/2) g` sends `v` to `c^mu v`;
- `c^((mu+1)/2) g^{-1}` sends `cv` to `c^mu(cv)`.

Their respective source reflection centralizers are trivial, so each entire transporter set is the stated singleton. This also gives uniqueness of `g`. Since the cusp is a commutator, their homology is exactly `+[g]` and `-[g]`, independent of the unit. D59 supplies its full primitive fixed-line generator; no free-basis primitivity is substituted.

The equation `[a,v_i]=c^mu` gives the exact action `alpha_i(a)=c^{-mu}a`. D62 therefore applies to every singleton element. An outside element `h v_i` centralizes `a` exactly when `h(c^{-mu}a)h^{-1}=a`, proving the displayed conjugacy criterion with its original cusp power.

## Full centralizer coordinates and standard extension maps

The kernel of the parity map on `C_E(a)` is precisely `overline{<a>} = Zhat` by D62. Any outside centralizer element has square `a^kappa`, giving the complete two-coset coordinates retained in D75.

In the two-section-class case, D60's normalized torsion quotient has `chi(g)=1`, so `chi(a)=(-1)^i` and `2chi(t)=(-1)^i kappa`. The dyadic coordinate of `kappa` is even. The unique outside commuting involution is `a^{-kappa/2}t`. It cannot be in the cusp class because every cusp-class involution now has trivial fixed group and `a` is nonidentity.

In the one-section-class case every outside involution is in that cusp class, so the dyadic coordinate of `kappa` is odd. The specified odd-prime corrections make `kappa'` a full unit while preserving that dyadic coordinate. The full power `z=(a^b t)^(kappa'^{-1})` satisfies `z^2=a`, lies outside `F`, and generates the full centralizer. The inverse power and the two-coset coordinates prove the generation statement; injectivity of multiplication by two in its `Zhat` coordinate proves uniqueness of the root.

For the two-class model, `X -> a`, `Y -> v_i w` gives `[X,Y]=[a,v_i]=c^mu` because `a` commutes with `w`. Conjugation by `v_i` has the exact D61 standard action. For the one-class model, `X -> z v_i`, `Y -> v_i z` gives `XY=z^2=a`, hence again `[X,Y]=[a,v_i]=c^mu`, and `v_i` interchanges the basis images. D61's actual full boundary test makes both kernel homomorphisms isomorphisms. Their inverse kernel maps and the specified parity-one reflection give the full extension inverses.

Conversely D61's exact cusp/reflection normalization supplies a full unit and one of the two literal reflection labels for every peripheral conjugator. Its image of `X` or `XY` is the unique singleton just proved, and the other reflection or the image of `Xv_0` supplies the required outside centralizer element. This proves both directions of D75.5 for the entire original conjugator problem.

## Real projectivity and scope

In the one-class case every involution is now self-centralizing. The actual free profinite subgroup is open projective of index two, and the involution set is the closed square-one locus intersected with the clopen nontrivial quotient coset. These are the stated hypotheses of the Haran characterization already sourced in D74. In the two-class case the proof retains the other fixed group's D59 first cohomology and onto fixed-line map and makes no procyclic recognition claim.

The exact conjugacy equation D75.5 remains an existence question. The proof establishes full centralizer triviality, singleton transporters and the precise standard-model equivalence, and does not infer that equation from transporter uniqueness. No new finite computation or external source is required for these substitutions beyond the accepted D74 and the explicitly reread D58–D62 inputs.
