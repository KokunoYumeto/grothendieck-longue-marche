# E.64 — Every adjacent complex norm over seventeen

Status: Proved. Independent root full-proof and fresh copied-source GP/Python audit PASS. All63 GP records and every JSON value agree. Root freshly opened the complete Lemmermeyer proof; the new Milne fetch timed out, so the already-opened exact source passages are retained without claiming a fresh root read.

## Evaluated norm images

The actual tower is L_d=Q(zeta3,beta_d), beta_d^(3^d)=17zeta3, with beta_(d+1)^3=beta_d. Every adjacent extension is cyclic cubic. The shifted absolute polynomial is Eisenstein at3, with constant273, so each field has a unique prime above3. Eisenstein at17 supplies the other unique ramified prime and its compatible uniformizer.

For every prime q away from3 and17, the finite residue beta_d^((Nq−1)/3) determines whether q splits or is inert. At an inert prime the target valuation must be divisible by3. At17 the unit obtained by removing the beta_d valuation must have cube residue inF289. These conditions are both necessary and sufficient for a global norm: reciprocity supplies the one remaining local condition at3, and the opened Hasse norm theorem then applies to the cyclic extension.

The norm cokernel is explicitly the direct sum ofF3 at17 and at all inert primes away from3. Surjectivity follows from the actual relative Brauer exact sequence, with the coordinate at3 chosen to make the sum of local invariants zero. The displayed finite residue coordinates are isomorphisms of the corresponding local norm quotients.

## Both completed Hilbert90 directions

The proof keeps three exact comparisons separate:

1. Complete the exact sequence with kernel the ordinary norm-one group and quotient the ordinary norm image.
2. Identify that image's completion with its actual subgroup in the target completion, using the inclusion of all cubes.
3. Complete the Hilbert90 sequence with kernel the base multiplicative group and quotient the ordinary norm-one group.

For an exact abelian sequence C→B→D and bounded three-primary torsion inD, the inclusion C intersect3^(n+r)B inside3^nC proves the required cofinality. Quotient kernels have surjective transition maps. Thus the completed norm kernel is exactly the image of sigma−1, and the completed invariants are exactly the included base completion.

The norm-one group's three-primary torsion ismu3 and its free rank is countably infinite. Each nonempty completed norm fiber is thereforemu3 times the explicitly defined restricted sequence group inZ3. Its actual map uses a chosen basis of ordinary norm-one elements and the convergent product of their three-adic powers. The completion has infinite discrete quotients and is not asserted to be compact.

## Next fixed class group

The E57 fundamental units have residues zeta3 squared at17; zeta3 itself also has cube residue inF289. Hence all base ordinary units are norms of elements in the next field. With the certified base class number9 and the two ramified primes, Lemmermeyer's ambiguous formula gives an exact fixed class-group order27.

The unit-norm quotient remains in the actual exact sequence from ambiguous to strongly ambiguous classes. No surjectivity of the ordinary unit norm is inferred from element-norm surjectivity.

## Executed certificates

The GP program uses the official PARI2.19.0 executable already built forE52. It certifies the degree-six class group and fundamental units and computes the exact prime fields of degrees2,6,18. For58 prime ideals above rational primes through97, it checks the finite cubic residue against the actual prime contractions under beta1=beta2^3. There are13 split and45 inert prime records.

The independent standard-library Python program checks all58 finite residue fields,1508 finite-field norm identities,124 characteristic-zero norm identities in the actual degree-eighteen field, and six exact Eisenstein polynomial expansions. It separately checks the unit residues and the96-element cube image inF289.

The first GP serialization used the raw finite-field object's print form instead of its polynomial accessor. Its successful arithmetic output is retained as e_complex_norm_criterion_raw_ff.out; the accessor probe is also retained. The corrected certificate uses explicit coefficient arrays and passes the independent reconstruction.

## Exact scope

These norms are the complex component of the actual positional H transition fromE46/E62. The product of pure and complex norm maps commutes with the total norm toQ, so the actual J condition is preserved. Every adjacent complex norm image and fiber is evaluated. The full global compatible inverse limit still requires the pure-factor maps and compatible choices through all levels. No automatic compatibility of separately nonempty fibers is asserted.
