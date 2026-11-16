# Root audit of C31: finite source, integral obstruction, and full lift

The full candidate `notes/pbc_C31_draft.tex`, SHA256
`6899064c339ce08628caa98b84ba1f6d9ae6447212aec17c91ddd62eb114cbee`,
has been read in full. The mathematical argument passes. Its registration
still awaits the separately running root replay of the complete G86 DAG
and literal original-row identity. The new permutation-to-pc replay has
completed successfully; it is not a pending mathematical assertion.

## Exact claim and domain

The three continuous characters are defined on the full gentle group by
composition of the already constructed continuous endomorphism D with
the already constructed quadratic character Delta. The new map to C2^3
is onto already on the multiplier-one subgroup. This is the correctly
typed stronger claim: the full specified Galois image need not lie in
the multiplier-one subgroup. D fixes that full image, and Delta is zero
on it, so all three full-group characters descend to its arithmetic
normal quotient. Neither independence of all further iterates nor a
new assertion about the pentagon subgroup follows.

## Actual finite group and source presentation

The finite object is the image of the actual two modular permutations
on 2,592 points, not an abstract guessed pc presentation. The six next
level evaluations and six signed first-level evaluations are made on
the same free source. Their tuple belongs to the derived word image,
and the comparison to the pure subgroup of the induced modular image
is bijective. Thus its residue f2 is an actual derived word. The six
kernels are permuted by the geometric S3 up to inner automorphisms;
their intersection is normal in the actual modular source.

I read all of `code/pbc_verify_iterated_source_permutations.py`. Its
generated finite-only GAP program reconstructs the permutation group
and bijective pcp map before any Schur computation. The old cached pc
generators are mapped back by that isomorphism. Every one of their 176
power and 15,400 conjugation relations is checked as a permutation.
The recorded triangular change then gives the adapted generators;
they generate the same actual group, and every adapted relation is
checked as a permutation as well. The relative orders and their
product are the actual group order. The usual collection bound and
the epimorphism onto this group therefore certify the complete
presentation, not just a list of valid relations in an unknown cover.

The same execution checks the marked s, r, f2, both images, both frame
conventions, and the purity and commutation of all 71 involutory and
nine cubic centralizers. In particular r=g1, s=g2, the left s-frame
is g7, and the left r-frame is g5. The author execution exited zero
after 445.64 seconds. Its generated GAP hash is
`63ec773502277ff1f52eabd153c233a3b7f8571cffa2de62ef400d27819385b8`,
and stdout hash is
`ec4685847bb8da8b27ab0b50119e93b6677a7f8ee6b359231b46efd02be5f1c8`.
The old Schur memory failure is irrelevant to this completed finite
comparison and remains retained. I have not claimed to rerun this
additional seven-minute permutation calculation independently.

## Integral Hopf obstruction and the original frames

For the free discrete group on the 176 marked generators, centralizing
its relation kernel gives H and its finitely generated abelian kernel
K. The Hopf sequence identifies K intersect H' with H2(G,Z).
The quotient embeds in the free abelianization, so this is exactly the
torsion of K. Each of the three recorded word differences is central;
their sum telescopes to the actual framed product error T. Its free
abelianization is zero, independently of a numerical collection.

Changing the s-frame on the right by a finite s-centralizer adds its
central commutator with s. This is well-defined independently of its
lift because K is central, is additive in the centralizer, and is
killed by two because s^2 is central. The corresponding r-map is
killed by three. C42's actual homology isomorphism and original-row
identity therefore kill the original three-primary part of T; the
extra coefficient three on a cubic commutator is literally zero.

The G86 computation is applied to the actual quotient of this same
source. C43's split homology surjection transfers C42's bound 2^14
to its two-primary multiplier. In a finitely generated abelian K86,
two-primary torsion killed by 2^14 intersects 2^14 K86 trivially:
the free part contributes no torsion, and the odd torsion cannot
contribute a two-primary element. The corrected target is indeed
two-primary because C42 has already killed its three-part.

The fresh DAG uses standard GAP recollections, not the rejected native
vectors. Its literal final identity contains only the target, genuine
s-frame rows, and original consistency/power identities. All coordinate
and modulus leaves are replaced by explicit original-row Bezout
combinations. The mathematical deduction requires no completeness of
the searched relation lattice. The final 6,446 original leaves were
recollected successfully in GAP. A root rerun is separately recorded.

The odd correction coefficients select, in the original basis,
6,16,27,35,39,41,43,49,53,55,63,65,72,79,80,85. The correction is
the displayed increasing product on the right of g7; g5 is unchanged.
Ordering is explicit, and its effect is additive in the central
commutator group. No independent power correction or cubic-frame
correction survives in the final witness.

## The two original coordinates lost by the quotient

The complete proof and source audit of the top covers is retained in
`notes/root_C31_top_two_covers_audit.md`. C43 identifies the kernel of
the natural homology map with the canonical wedge coinvariants C2^2.
The two actual central extensions restrict to the two independent
commutator forms on this kernel. Their quadratic refinements can
differ by Ext classes without changing that restriction; an inflated
quotient extension vanishes on the kernel. This proves that the two
evaluations detect every remaining element, rather than merely giving
two arbitrary functionals on an unspecified Schur cover.

Both evaluated total targets and every permitted frame correction
are zero. The second form has individual values (1,0,1), which sum
to zero; these are not all individually zero. The form of rank 36
is degenerate, and its cover is not called extraspecial. The
Q-coordinate is retained even if its action on A is not faithful.
The explicit original-group section and all 83 underlying finite
word equalities have separate completed source replays. Consequently
the exact corrected original T is zero at two and three, hence
integrally: no other primary torsion occurs for this finite G.

## From the free presentation to the actual modular centralization

Let L be the subgroup of H generated by g2 and g1. Since their finite
images generate G, H=LK and H'=L'. Their two distinct coordinate
vectors in H abelianized are independent; the epimorphism Z^2 to
L abelianized is therefore an isomorphism. The actual free two-source
centralization maps onto L. It is the identity on the Hopf multiplier
by naturality and an isomorphism on abelianizations. Its kernel is
therefore both contained in the multiplier and trivial there. This
proves the asserted isomorphism, including the source map.

The two central elements g2^2 and g1^3 have independent nonzero
abelian vectors, so their subgroup intersects H' trivially. Killing
them and completing gives exactly Gamma/[N,Gamma]. Equivalently,
H2(Gamma)=0 and Gamma abelianized to G abelianized is an isomorphism,
so the kernel is the finite Hopf multiplier. Finiteness removes any
completion ambiguity. This is the actual modular centralization,
not an arbitrary central cover chosen after the fact.

Every displayed corrected frame in H can be replaced by an L-element
with the same finite image because H=LK. The difference is central,
so conjugation is unchanged; its finite purity is retained. The exact
product identity now gives Gamma to E fixing sr. It sends N into the
central kernel, hence kills [N,Gamma] and factors through E. Its
kernel action is H2(alpha) by Hopf naturality. Since alpha is a finite
automorphism, the induced endomorphism is an automorphism on kernel
and quotient and thus on E.

I reread P3's full finite trace/count/compactness proof, B11, and the
explicit arbitrary-normal modular argument in C40. The required
auxiliary source maps send N centrally and factor through this E;
precomposition with its actual peripheral automorphism retains the
three frame coordinates. The subgroup counts use only normality,
and the modular classes already enforce the square/cube relations.
The cofinal finite conditions and compactness give a full peripheral
automorphism, with generation in every finite quotient. Hopficity
then gives a genuine automorphism. The prescribed identity cusp
frame allows an inner correction from N making sr fixed literally.
This is the necessary full profinite inference; mere finite survival
would not suffice.

## Both normalizations and the two descents

The finite pure abelianization is C12^2 but the pure inertia orders
are 24. The first normalizing exponent a lies in 12 Zhat, so its
old-marking change is y^(-a) f2 x^a and can be nontrivial in G.
It is nevertheless invisible in every first signed detector, whose
three peripheral orders divide 12. The actual descended-frame
formula therefore makes Delta D zero.

In the G1 evaluations, s1^a and r1^a are one. The first value is
tau1^(-a) beta1. For the cycle product, the exact cancellation
rho(y^(-a) f2 x^a) y^(-a) f2 x^a =
z^(-a) rho(f2) f2 x^a makes its value unchanged, u1.
Thus both descended frames acquire the same left factor
tau1^(-a). It centralizes the cusp and has a full pure lift because
a is even. Conjugating the full descended representative by tau^a
removes it and restores both C27 frames exactly. This preserves
the actual outer class and is stronger than equality of finite
automorphisms alone. Root's independent normalization certificate
checks both residues a=0,12 modulo 24 and all six coordinates.

The second normalization is different: G1 has both pure
abelianization C12^2 and inertia order 12. The next correcting
exponent is divisible by 12 and is genuinely invisible there.
The normalized first descent consequently retains C27's actual
six residues. I reread C27's signed ambiguity calculation; its
two allowed signs give the same equianharmonic bit one and Gaussian
bit zero. Hence Delta D^2 is one.

Finally the already constructed vectors (1,0,0), (b,1,c), and
(d,0,1) have determinant one over F2 for every b,c,d. They prove
the asserted surjectivity without claiming unknown individual
Delta-values. This completes the written mathematical audit.

## Preservation and remaining execution gate

The failed native collection, all stopped calculations and all old
source files remain. The successful trace has a separately verified
complete decoded-byte restoration; storage correctness is not used
as a substitute for its original-row mathematical replay. The root
full DAG expansion has matched all mathematical fields already;
the final literal GAP replay is still running when this note is
first written. Its final result will be appended, without erasing
this contemporaneous gate record.

## Final independent execution gate: PASS

At 23:23 UTC the root rerun exited zero. It expanded all 8,975,109
DAG nodes and independently recollected all 6,446 final original
leaves in GAP. Every mathematical JSON field matches the author
certificate; the generated GAP program is byte-identical and stdout
is identical after normalizing only runtime integers. Root's final
literal certificate hash is
`4852ade46aebe9e46869e4ad0934144902a27551178a1187b83882ee3088dda1`.
The entire mathematical and execution audit is therefore PASS.

The independent standard-trace restoration also exited zero and
reproduced all 355,295,349 decoded bytes with SHA256
`1a2ae63a7a1a3351e86f1f71a7d491d87418d79dcbb0d8ddbf3cbaccc11499a2`.
The full historical restoration of checkpoint13 reproduced all
2,842 archive entries exactly. These are preservation checks,
separate from the mathematical proof gates.
