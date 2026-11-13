# A6 Ferrari refinements

## Completed lower targets: E.45

The finite model starts with the actual D.31 Cayley tables for A6 and
Aut(A6), not a class-name identification. `de_ferrari_a6_kernels.py`
checks all 1440 automorphisms on both generator edges of all 360 Cayley
vertices, partitions all 129600 ordered pairs into 124 Aut-orbits, and
finds 76320 generating pairs. The action is free on generating pairs,
giving 53 epikernels. The literal Nielsen kernel orbits have sizes
12,15,10,16. Complete actual automorphism transporters, including their
two outer bits, satisfy the braid relation before projection.

The two finite four-strand targets retain the kernel permutation (53
points) or kernel permutation and outer V4 coordinate (212 points).
The Ferrari free kernel is killed under these explicit maps, so c=a.
All six evaluation substitutions remain in the induced source. All six
B/F cosets are retained; the original degrees 1908/7632 compress
faithfully to432/798 using pointwise intertwiners for both s and r on
every discarded duplicate orbit. The upper-to-lower kernel has order
2^35, both in the source and the four-strand target, and its coordinates
prove that it is elementary abelian.

Let c0=2^40 3^21 5^10 7^6 11^3 13^2 and c1=2^35 c0.
For either source G, the complete image C of N-prime has order c_epsilon.
It is perfect and equals both the entire F-prime image and the image
of K6 intersect F-prime. Exact orders divided by c_epsilon are:

| Image | G | F | F-prime | N | N-prime | K6 | K6 intersect F-prime |
|---|---:|---:|---:|---:|---:|---:|---:|
| Quotient order | 5400 | 900 | 1 | 75 | 1 | 25 | 1 |

The maximal solvable quotient has the literal comparison
G/C = B/(F-prime F^30). This is proved by the exact order30 of x,y,
the order900 of the generated abelian F image, and equality of orders.
Likewise G/image(K6)=B/(F-prime F^6), order216. The order72 quotient
G/image(N) has not been identified with a modular group; such an
identification would be wrong here because its F image is abelian.
The N exponent-sum lattice has Smith diagonal(2,6).

Every retained D23 point extends: C is the entire F-prime image, so the
difference from any actual Galois value of the same multiplier belongs
to C. The joint N-prime image in a solvable old source and C is the
direct product. This gives a correction retaining the whole old point,
not a test of one representative. The exact common source quotient is
S6 of order216. Both new four-strand derived groups are perfect with
index2; the common four-strand quotient is actual braid exponent mod2.
All 864 E.24 points and every compatible multiplier lift1 mod72 survive.

For multiplier1 the new value may be made literally1. The image of H
in S30 is C10^2, so S30 factors through the old P20 stage. The exact
residual map R_H=intersection(H^[r]) -> C is onto, by nested compact
N-derived fibres. It preserves the entire E.42 boundary family at once.
On cofinal old sources containing P20, the original and corrected
joint source images both equal G_old fibre-product over S30 with G.
No joint-generation assertion with the nonsolvable SL2(F5) factor of
E.43 is made without computing its common quotient with this A6 source.

Actual completed runtimes: kernel construction and targets7.238s;
source permutation3.851s, outer16.975s; complete correction images
23.094s and172.219s; quotient/four-strand comparison30.982s.
Read-only `de_ferrari_a6_source_data.py` reconstructs the exact modular
graphs and all97 N words, comparing them word-for-word with the saved
SL2(F5) source certificate. It executes none of the old main programs
and rewrites no earlier file.

## Full inner/free target: model complete, source computation running

`de_ferrari_a6_model.py` uses all ten Sylow3 subgroups of the actual A6
as a faithful degree10 Aut(A6) action. It checks all1440 squared
composition pairs and all six nonidentity conjugacy-class normal
closures. The exact holomorph map is
(k,alpha) -> (Inn(k) alpha, alpha), represented on two degree10 blocks
per factor. This is faithful, and its projection to the saved outer
target is checked on every generator product. The full Ferrari target
has faithful degree1060, free image A6^53, Nielsen order
2^128 3^21 5^33 7^6 11^3 13^2, and target order
2^287 3^127 5^86 7^6 11^3 13^2. All six pure evaluation pairs now
fail to commute, as expected for these actual retained free coordinates.
The three Artin generators each have order60.

The first full model run completed all mathematical checks and the
Nielsen order calculation, then hit a metadata key-name error
(`four_strand_target_order` instead of `target_order` in the already
saved lower-target JSON). Its stdout is retained as
`de_ferrari_a6_model_failed_initial_field.out`. The corrected program
was run again from the start and passed in113.959s; active `.out`, JSON
and NPZ are its successful outputs. No negative mathematical claim was
drawn from the metadata error.

The full induced source starts at38160 permutation points. The exact
intertwiner compression retains55 transitive B-sets and faithful
degree9462. Its completed source-image order is
2^218 3^84 5^62 7^6 11^3 13^2. The literal x,y images both have order120;
their lower-target images have order30 under the explicit outer map.
The later complete perfectness and correction-image calculations are
recorded below. They now prove the full inner/free lift over the retained
D23 source; the simultaneous G_L comparison remains a separate task.

The initial SymPy source-order search was interrupted after its faithful
compression had finished. Its interrupted stdout is retained. Two
subsequent exact C++ discovery searches with the original point order
were also interrupted for runtime, retaining their logs. Reordering the
55 transitive B-sets by decreasing size is an exact point conjugacy,
saved with its inverse, and substantially speeds up the same group
calculation. The completed `de_a6_schreier_full_ordered.out` search took
300.932 seconds and saved303 actual strong-generator words in a7300-node
word DAG. Its final complete check sifts865049 Schreier relations.
`de_a6_schreier_full_ordered_replay.out` independently rebuilds the
stabilizer chain, checks every literal word and every final Schreier
relation, and has passed in115.018 seconds. The separately implemented
NumPy word-DAG replay also passed. The new source-verification script
reconstructs all36 induced coordinates and checks every compression
intertwiner, the final point conjugacy, and equality of the original
certificate generators with the actual source images.

The exact engine `de_a6_schreier.cpp` supplies full final Schreier
checks, literal input-word certificates, and derived-subgroup certificates
with all commutator and normal-conjugation checks. Controls include S4,
A5, C2^2, both already-audited lower A6 sources, their N-prime images,
and their perfect correction groups. Each control was replayed from its
certificate. Neither a heuristic group-order estimate nor equality of
orders is used to identify an unspecified comparison morphism.

The actual full N image was computed from all97 literal basis words,
with six selected words and every original retained by exact sifting.
Its index in G is72. The exact normal-coset program
`de_a6_quotient.cpp` checks every conjugate of every strong generator,
and compares canonical cosets as full permutation arrays; hashes only
select a comparison bucket. Its quotient is connected to the specified
576-element modular Q by all1152 Cayley-generator edges. The pure
quotient has order12 and commuting x,y, proving the actual equality
G/image(N)=B/(F-prime N), with the ordinary exponent lattice
L=[[6,4],[0,2]]Z^2. In particular image(F-prime) lies in image(N).

The independently computed entire F-prime image has order
2^211 3^81 5^60 7^6 11^3 13^2 and index86400. Because the actual x,y
have order120, its ordinary pure abelian quotient is exactly
(Z/120)^2, with the specified x,y exponent coordinates. This proves
the actual quotient G/image(F-prime)=S120=B/(F-prime F^120).
This abelian calculation alone does not establish perfectness. The later
derived-word certificate establishes the perfect residual separately.

`de_ferrari_a6_abelian_compare.py` supplies integral multiplication for
S_m using the six actual B/F coset representatives, their conjugation
matrices and their exact extension cocycle. It also proves the literal
D23→S24 map. E.24's complete binary K6 image has dimensions9 and7 for
the full image and its F-prime part. Its quotient map is verified
against all97 sixth-power columns, giving the ordinary exponent map
(6L)/(12L). Every D23 kernel word therefore has exponent vector in
12L, which is contained in24Z^2. This gives an actual quotient map,
not just a group of a matching order. The H image in S120 is C40^2,
so S120 factors through the specified boundary target B/(H-prime H^40).
The first run of this small comparison script passed the lattice
calculations then used the wrong metadata key F_generator_orders;
the supplied key is F_image_orders. Its stdout is retained under
`de_ferrari_a6_abelian_compare_failed_initial_field.out`. The corrected
script reran from the start and passed; no negative mathematical claim
was drawn from the key error.

The four-strand target's maximal solvable quotient is already settled.
The actual degree530 Nielsen image has derived index2 and a perfect
derived subgroup, proved by complete first/second derived certificates
with linked original-word DAGs. The free kernel A6^53 is perfect, so
the full target also has perfect derived subgroup and actual braid
exponent quotient C2. Its full twist (abc)^4 has order20, and its
three-strand full twist (ab)^3 has order40. The exact elements,
centrality check and all nested certificate comparisons are saved in
`de_ferrari_a6_target_derived.py` and its outputs.

## Primary-source search and precise comparison

Opened Guillot, arXiv1407.3112 (the25-page author revision), Lemma2.1,
Theorem4.9 and Theorem5.2. Theorem5.2, printedp18, computes the author's
finite group GT1(PSL2(F9)) as C2^12 times D8. The universal epikernel
product in Lemma2.1 is the product used here, but our finite maps are
the explicit B4 Ferrari map and its 36-coordinate induced B source.
The theorem computing an automorphism centralizer is not substituted
for either of these source maps. Search/open refs:turn436view0,
turn437view0; exact primary URL https://arxiv.org/pdf/1407.3112.

Also opened Guillot arXiv1604.04415v1, Theorem1.1 and Sections2,4, and
the author's publication list. The journal link redirected to a page
unavailable to the search tool. The general theorem is not used in
E.45's proof. Its v1 text's particular diagonal representative in4.2
would require checking for square fields before use; our construction
retains actual automorphism tables and does not use that representative.
Primary refs:turn427view0,turn430view0,turn436view3,turn437view1;
https://arxiv.org/pdf/1604.04415 and
https://www.math.unistra.fr/~guillot/research.html.

## E48: full source, every old fibre, and the exact Kummer bridge

The completed statement is `sections/E_a6_full_agent.tex`; its complete
replay and dependency map is `research/DE_a6_replay.md`. Write P=image(N),
E=image(F-prime), E1=image(F-double-prime). The actual source maps now give

- image(F)/E = (Z/120)^2, using ordinary x,y exponent sums;
- E/E1 = F3^9, with nine literal commutator-word basis values;
- E1/C = F2^6, with six literal nested derived words;
- C perfect and normal, of order 2^205 3^72 5^60 7^6 11^3 13^2;
- G/C of order108839116800, the maximum solvable quotient of this source.

The final perfection proof uses the derived group of ten specified words
inside C. Its full Schreier certificate has the same order as C, and its
literal membership flags prove containment in C-prime. The completed
720615-relation check was freshly replayed in112.917 seconds. Normality
under the actual source s,r was checked on all664 strong-generator
conjugates. Thus equality of group orders is used only after the actual
inclusions and maps have been proved.

The complete old correction image is exactly

    rho(ker(D23) intersect F-prime) = P-prime = rho(gamma5 N).

This uses every one of the6668 normal relators from the old ternary
source, the entire18-dimensional K6-intersect-F-prime image, and the
whole binary source. Six squared literal relators span the required
ternary image, and six actual gamma5 words give the whole binary layer.
Their expanded word lengths are4746,4754,4682,4682,6440,6438. All six were
independently evaluated in both old collectors, retaining all36 induced
components. The normal action on the ternary image has full rank6;
perfectness supplies the remaining C layer. Consequently the image of
every gamma_j(N), j>=2, is the same P-prime.

The actual three-dimensional quotient E/P-prime is printed as the matrix
Q3 in E48.13. On the complete norm kernel it has the exact value
(2,1,0)^t c2, where c2 is the y-coefficient in the actual index-two cover
with Schreier generators x^2,y,xyx^-1. Its commutator coefficient is
c2([x,y])=-1. Nakamura--Schneps equation(2.4), Lemma2.3 in the author PDF
gives c2(f_sigma)=+kappa2(sigma) in the positive-root convention. The
primary text was reopened directly; the exact reference is author PDF
page9/index8, not an inferred journal page.

The complete solvable fibre computation retains all27 ternary norm
points and all binary lifts. There are54 full norm values,48 generating,
for each compatible multiplier residue. For each fixed old point there
are18 norm lifts,16 generating. All8496 defining-relation substitutions
were checked for the48 generating maps, proving automorphisms of G/C
only. The compatible power period is720, with residues
1,73,217,289,361,433,577,649; the halved exponents, all old periods, and
the new order60 braid generators are retained explicitly.

All864 old points occur, with each scalar value0,1,2 appearing288 times.
Restricting the new f-value to the identity reaches only288 of them.
That restriction was never an exclusion of the other576 fibres: their
complete affine corrections are now retained and realized. Since the
positive-root cubic Kummer character is onto on the cyclotomic kernel,
one can select an actual Galois element of the prescribed full multiplier
with the required scalar. The difference of its new source value from
the old word lies in P-prime and has an actual gamma5(N) preimage. This
proves the full new Galois comparison while retaining D23 literally.

Common-source generation is proved on the actual image of B in D23×G.
The old N image is nilpotent and retains N-ab/6; the new stable lower
central image is P-prime. Goursat gives the pure P-prime subgroup, and
the actual rank97 Frattini maps at2 and3 together with the ordinary
C5^2 exponent map give the complete common N image. The Q576 quotient
is retained by its actual cusp-gauge map. No invariance of the D23
kernel or of the full G kernel is assumed. The four-strand common target
is the actual T23×_(C2)T6, since the new target has perfect derived group
and braid-parity maximum solvable quotient.

The same literal-word scalar comparison against the E38 modular
matrices is now complete: the24 labels are
(0,0,0,0,1,1,1,1,2,2,2,2,2,2,2,2,0,0,0,0,1,1,1,1).
All six ternary and seven binary fibre directions have zero coefficient
and identity signed modular value. `de_ferrari_a6_kummer_labels.py`
therefore checks all864 values against the same positive-root kappa2
normalization. This establishes equality on these specified fibres; it
does not replace the actual combined-source morphism needed to retain
G_L and the later boundary refinements simultaneously.

## Remaining actual combined-source comparison

The separate A6/A5 joint source has been faithfully compressed from the
two specified source representations and has order
2^249 3^104 5^78 7^8 11^3 13^2. Its common quotient therefore has order
291600000. The certificate retains the literal paired source generators.
The abstract structure and the compatible kernel maps of this common
quotient have not yet been identified. No joint G_L lifting theorem is
inferred from its order or from the shared scalar alone. The E48 package
is stable for independent root replay; new combined-source work uses the
prefix `de_a6_gl_`.
