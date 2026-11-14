# Independent audit of D.58

**Result: PASS.** I read the entire written proof, metadata, and executable certificate, and reran `work/part_c/code/torus_negative_involution_d58.py` successfully. The independent stdout is `work/part_a/d58_audit_stdout.txt`.

## Full proof checks

The mod-two identity case really has an integral plus/minus decomposition of the actual cohomology module: `(I-D)/2` is integral and idempotent, and its image and kernel have rank one because the characteristic-zero eigenvalues are opposite. No free-basis change is inferred.

The explicit mod-four cochains give `a²=0` and `b²=u b`. The split extension makes both invariant degree-one characters extend, so the two-row Hochschild–Serre spectral sequence collapses. Multiplication by `u` is an isomorphism from degree one onward, with the stated three-dimensional basis. Writing `ab=epsilon u a+delta u b` after restriction to the chosen section, associativity and independence of `u²a,u²b` force `delta=0`. The displayed map to dual numbers times `F2` respects all products and is a linear isomorphism for both values of `epsilon`.

In the nonidentity mod-two case, the actual dual module is the regular two-dimensional module. Its positive-degree cyclic cohomology vanishes, the invariant character extends, and high cohomology is exactly `F2 u^n`. Restriction to the chosen section then forces both `u chi` and `chi²` to vanish.

The full Brown restriction hypotheses are retained: an open subgroup of finite mod-two cohomological dimension and no `C2×C2`, since any finite subgroup injects into the quotient `C2`. Each actual normalizer is `C_F(S)×S`. The finite high-degree source and dense restriction map give the full product isomorphism, and localization preserves the cup-product restrictions. The factors are local rings with square-zero maximal ideals `H1(C_F(S),F2)u^{-1}`. Comparing their primitive idempotents and nilpotent dimensions with the two explicitly computed rings gives the exact section counts and the fixed-group cohomology dimensions. The proof never deduces full triviality or procyclicity from those dimensions.

The two residue-field evaluations in the split case differ on `b`; `a` vanishes on every involution because its square is zero. Thus equal abelian character values really do force the two cusp reflections into the same full section class. The replacement of an extension conjugator by an element of `F` uses the unique element of the source section with the same quotient label and preserves the conjugated subgroup.

The cusp normalizer surjects onto the quotient through the exact peripheral-preservation map and has kernel the stated full cusp group. Global multiplier `-1` makes its square parameter satisfy `2 kappa=0` in `Zhat`, hence the parameter is zero. Its two internal classes are the two cosets modulo `2 Zhat`; their images in `E_b` have equal abelian characters because `c=[x,y]`. The actual `F`-conjugacy therefore gives `g v g^{-1}=c v` and the exact commutator equation `c=g(v g v^{-1})^{-1}`.

## Executed checks

The certificate rerun passed all 16,384 finite cochain-pair comparisons, all four cyclic module cases, both eight-element localized ring isomorphisms (64 product comparisons and 512 associativity comparisons each), and the exact free-word cusp equations in both geometric examples. These support the displayed identities; the section classification itself is established by the full cohomological argument.

No correction is required.
