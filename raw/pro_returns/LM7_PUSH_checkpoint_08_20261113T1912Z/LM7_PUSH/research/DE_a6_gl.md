# Actual full A6 / signed Ferrari common source

This work follows E48 and uses only the new `de_a6_gl_*` prefix. The
protected E48 source package and every earlier E38/E50 certificate remain
unchanged. A simultaneous old-boundary or G_L fibre-survival assertion is
not yet made here.

## Exact base and signed extension

The actual joint A6/A5 source has degree11010, with explicit point
intertwiners from the two original representations. Its complete order
certificate is `de_a6_a5_common_source.bin`; the discovery stdout has the
different stem `de_a6_a5_common_source_order.out`. The source order is

    2^249 3^104 5^78 7^8 11^3 13^2.

The quotient common to the two specified maps has order291600000. This
order does not itself identify its structure. The actual eight shared
transitive B-sets give a specified432-point common quotient of order1350,
with F image C15^2. Thus those shared sets retain only part of the complete
common quotient. `de_a6_gl_common_base.py` records both restriction maps
and every s/r intertwiner, keeping this exact limitation visible.

The full signed source G_L lies above its A5 base with an elementary
binary kernel of dimension44 in the2052-coordinate induced module. The
new exporter `de_a6_gl_prepare.py` retains all36 evaluation coordinates,
the exact SL2(F5), S5 and automorphism tables, and all original source
generators. It does not invoke the legacy runpy initializer. Its first
attempt stopped before writing data because the separate base binary had
been named with the stdout's `_order` suffix; correcting the literal
filename gave the successful complete export. No mathematical result was
inferred from that filename error.

`de_a6_gl_kernel.cpp` includes the unchanged Schreier engine and ports
the signed Ferrari multiplication to explicit byte arrays. The export
retains160 independent Python operation checks and132 full kernel-element
and conjugation comparisons. The C++ model passes all of them before
using the source certificate.

The program freshly replays the entire degree11010 stabilizer chain,
reconstructs every transversal with its actual original-generator word,
and then evaluates every one of its1154659 final Schreier relators in the
full signed Ferrari source. Its binary normal closure has dimension42.
All relators are evaluated, including the largest first orbit; the run
does not terminate merely when a provisional rank stabilizes. The final
run passed in404.946 seconds. The output retains the complete literal
word DAG and all42 original basis-word values.

The complete-kernel argument is the Schreier presentation itself. Every
strong-generator lift is an original source word, the original s,r are
among those generators, and the transversal rewrites supply all relations
of the base. Their actual lifted discrepancies therefore generate the
whole kernel normally. The recorded binary image is closed under both
original source generators, so it is exactly that normal image.

## Independent replay and the two retained coordinates

`de_a6_gl_kernel_replay.py` separately evaluates all required word-DAG
ancestors using NumPy permutations and the original Python signed group
collector. Every selected word is the identity in the full A6/A5 base and
has exactly its saved2052-coordinate binary value. All42 values are
independent, and all84 conjugates by s,r are checked again.

The actual E50 signed modular map identifies the old44-dimensional kernel
with a three-row map to the Q20 kernel over q2×q5. In that convention the
matrix is

    I + 10 [[a,b],[c,a]] modulo20.

Projective reduction modulo4 kills a and retains exactly b,c. The two
corresponding rows have rank2 on the old44-dimensional kernel, and the
new42-dimensional subspace is exactly their kernel. Thus the two missing
directions are the actual ordinary projective Q4=A2 coordinates.

This agrees with the separate source morphism: E48 supplies the ordinary
S120 quotient of the A6 source, and reduction of its exponent coordinates
modulo2 is the specified B/(F-prime F^2)=A2 map. Hence the A6 source already
retains Q4. The identification uses the two exact coordinate maps, not
only the dimension difference.

The complete joint G_A6/G_L order is the base order times2^42. Therefore
the maximum common quotient of these two specified source maps has order

    1166400000.

The signed source extension, its kernel, and its actual Q4 quotient map
are retained in `de_a6_gl_kernel*.json/.npz`. The actual maximum common
quotient is now identified by the literal maps below.

## The smaller-source comparison and its exact failure

The separate smaller E45 kernel-permutation source calculation is
complete. `de_a6_gl_lower_chain.bin` certifies its actual joint source
with G_A on2310 points, retaining all128833 final Schreier relations.
The same full signed lift procedure gives kernel dimension42. The
actual common quotient has order1350 for G_A, and5400 for G_L. Thus the
actual full G_A6/G_L joint image has index216000 in the fibre product
built using this smaller A6 source. The smaller quotient does not
contain the entire common component, as proved by this actual projection
and index computation. No old-word fibre exclusion follows from that
failed factorization.

The preliminary Python/SymPy attempt is preserved as
`de_a6_gl_lower_failed_initial_field.py/.out/.err/.json`. It completed
the group-order call but then requested the wrong metadata key
`induced_B_image_order`; the available lower-source key was
`source_image_order`. That attempt supplies no accepted certificate.
The authoritative calculation is the separate complete C++ chain and
lift, followed by `de_a6_gl_lower_compare.py/.out/.json`.

## Three literal shared source epikernels and the entire common quotient

`de_a6_gl_epikernels_prepare.py` constructs the actual B-induced action
for each of the19 Aut(A5)-orbits of epimorphisms from the original source
F=F(x,y) to A5. Every block has30 points, with six explicit Schreier
cosets and five A5 points. The construction checks the literal source
x,y values on the root coset and both B torsion relations.

`de_a6_gl_epikernels.cpp` then checks every complete source-presentation
relator, without stopping after a stable preliminary answer:

| Source | Complete relations | Factoring source epikernels |
|---|---:|---|
| full G_A6 | 865049 | 4,12,18 |
| G_A | 23945 | 0,2,4,10,12,16,18 |

The actual common epikernels4,12,18 form one B orbit. The single induced
block4 has six coset epikernels12,18,4,18,4,12. Its B image has order
6·60^3 and its F image is A5^3. The three maps are the specified
generating-pair maps from the saved exhaustive A5 model, with the root
coset convention checked explicitly.

`de_a6_gl_common_quotient.py/.out/.json/.npz` adjoins the B-induced cyclic
character given by the ordinary x exponent modulo m. Its six conjugate
characters retain the whole ordinary F abelianization modulo m; the
program checks commuting x,y images, their exact orders m, and pure
image order m^2. The resulting literal B image Q_m has:

| m | Degree | Order | Pure image | F-prime image |
|---:|---:|---:|---|---|
| 15 | 120 | 291600000 | A5^3 × (Z/15)^2 | A5^3 |
| 30 | 210 | 1166400000 | A5^3 × (Z/30)^2 | A5^3 |

The maps from G_A6 and G_A to Q_15 are supplied by the complete
epikernel factorizations and their already proved ordinary exponent
quotients. The maps from G_A6 and G_L to Q_30 use the same epikernel
maps (G_L projects to G_A) and their ordinary exponent quotients modulo
120 and30. Their B generators are literally the same s,r images.
The independently certified whole joint-source orders show that each
specified Q_m has the full maximum-common-quotient order. Consequently
the actual joint images are exactly the fibre products over these
specified maps. An explicit point map also verifies Q_30→Q_15.

The same new program independently replays every saved negative
epikernel witness in both its full source permutation representation
and the19 induced A5 blocks. Each is the source identity and remains
nontrivial in every epikernel it was recorded to reject. These selected
negative replays are separate from the complete positive all-relator
tests. The new common-quotient program passed in0.880 seconds.

## Complete central pullback and the joint perfect residual

The same positive-root scalar on every old word is already proved in
`de_ferrari_a6_kummer_labels.py`. The complete common correction image,
including its perfect and central layers, is now proved below. The scalar
agreement is not used as a substitute for that map.

The next completed computation is the full pullback of the specified map
C_A6→A5^3 along SL2(F5)^3→A5^3. It retains every central sign and every
choice of sign on the ten actual C_A6 generators. The new exporter
`de_a6_gl_central_prepare.py` expands all nested C_A6 generator records
into one literal F-word DAG and independently evaluates those words in
the full9462-point A6 source before exporting their three SL2 values.
The complete test adds every original-generator-to-normal-form relation
to the complete Schreier presentation; this is necessary because the
underlying accepted chain was constructed in derived mode.

The primary universal-cover input has been opened in Steinberg,
*Lectures on Chevalley Groups*, §7, Theorem10 and Corollary2(b). The
original Yale notes are at
https://www.math.utah.edu/~ptrapa/math-library/steinberg/steinberg-yale-notes.pdf
(PDF indices88–89 contain Corollary2 and its explicit SL_n→PSL_n example).
For the field F5 the stated exceptions do not apply, so the actual
SL2(F5)→PSL2(F5)=A5 map is universal. The model's PSL2→A5 map is the
literal conjugation action on the five Klein-four subgroups, already
verified in the signed Ferrari model. The direct product of these
three universal maps is universal: images of distinct perfect factors
in any central extension commute, since their cross commutator is
central and factors through their abelianizations.

The complete `de_a6_gl_central.cpp` run passed in220.675 seconds. It
freshly replays the accepted perfect-source chain, evaluates all720615
Schreier relators, and retains all10 original-generator-to-normal-form
relations. The full abelian relation matrix has13 columns:10 original
generator exponent columns and3 central coordinates. Its rank is13.
The independent replay checks all13 selected identity words in the full
source and checks every lifted value by direct2-by-2 matrix arithmetic.
The last three rows have zero original-generator exponents and central
matrix [[1,1,0],[0,0,1],[0,1,1]], of determinant1 modulo2.

There are30 independent binary generator-sign choices, or2^30 choices
in total. The raw complete-run field `original_generator_sign_freedoms:10`
counts the10 generator slots; it is not the binary dimension. That raw
certificate is unchanged. The separate `de_a6_gl_central_signs` certificate
checks all30 elementary column operations (e,z)↦(e,z+eD), where D has10
rows and3 columns. This makes the complete sign scope explicit without
rewriting the original result.

Writing A=A5^3, U=SL2(F5)^3 and C for the full A6 perfect residual, the
full pullback Ctilde=C×_A U is perfect. Since C is perfect, Ctilde's
abelianization is generated by its exponent-two center; the rank13
calculation therefore proves integral perfection. For K=ker(C→A), the
quotient C/[C,K] is a perfect central extension of A. The universal map
U→C/[C,K] is onto because its image together with the center is the whole
perfect group. The actual homomorphism

    Ctilde → K/[C,K],   (g,u) ↦ gbar·phi(u)^(-1)

is onto. Its values are central; (g,1), g∈K, gives surjectivity. Perfection
of Ctilde yields K=[C,K]. It follows directly that

    C_J = C ×_A C_L

is perfect: its derived group projects onto C_L and contains K. The exact
solvable quotient is (G/C)×_{B/(F′F^30)}(G_L/C_L), with the actual ordinary
exponent maps retained. Arithmetic independently read and approved this
central-extension argument and the complete generator-sign comparison.

## Full nilpotent-boundary correction image and joint generation

The exact image of gamma_j(N) in the actual joint source, for every j≥2,
is R1=P′×_A C_L. Here P=image_G(N). The signed source retains Q576=B/N,
and image_GL(N)/C_L maps isomorphically to L/30Z² through ordinary
exponents, with order75. Consequently the joint N image modulo C_J is
exactly P/C; the accepted equality gamma_j(P)=P′ gives the stated map.

`de_a6_gl_boundary.py/.out/.json/.npz` passed in1.180 seconds. It supplies
literal gamma5(N) preimages of the whole ternary rank6 submodule and
retains all six accepted binary words. The actual H elements x³,y³ and
the nine specified F′ words give rank6 on the ternary layer and rank6
on the binary layer. The full ternary H-commutator matrix also has rank9.
Thus [image(H),R1]=R1, including its perfect subgroup C_J.

Starting with I0=gamma5(Nhat) and I_(n+1)=[Hhat,I_n], every actual finite
image is R1. Compactness in the nested fibres proves the exact closed
source surjection

    I=gamma5(Nhat) ∩ R_nil(H) → R1.

Hence I∩ker(rho_L) reaches ker(P′→A). This corrects the A6 value to the
same actual Galois value already used for G_L while retaining D23 and
every specified nilpotent H-boundary value. The full finite864 family is
retained; for multiplier one, the432-point boundary family and all of
its admitted E43/E44/E47 coordinates are retained simultaneously.

Joint source generation is proved on actual finite common sources. In
the quotient by R1, the actual N image embeds into S_N×P/P′. The kernel
over the old S_N is central abelian. It has possible primes2,3,5 only.
The retained actual N_ab/p map in D23 removes every2/3 quotient, and the
five-part of P/P′ is the ordinary Fab/5 coordinate already retained by
G_L/C_L. Thus the corrected N image is full, and the actual Q576 map
gives full B-image generation. This argument does not assume S_N is
nilpotent. The same Galois automorphism preserves both H and N by the
literal ordinary exponent and Q576 comparisons, so it preserves I and
the corrected image contains all of R1. Arithmetic independently read
and approved this exact generation argument.

The retained boundary family here consists of the specified H-nilpotent
quotients in E43/E44/E47 and the full relative pro-p H factors, p≥5, of
E42. No claim about the arbitrary mixed prime-to-six N-kernel family of
E20, nor the new E53/E55 symplectic family, is inferred from this result.

## Exact common four-strand target

The literal joint free image is A6^53×SL2(F5)^19×C2². The two perfect
products have no nontrivial common quotient through their specified free
maps; their composition factors are A6 and respectively A5,C2. The two
global binary characters give the final direct factor.

After killing the perfect free product A6^53×SL2(F5)^19, the actual
joint target is faithful on781 points:530 from the A6 Nielsen action
and251 from the signed quotient, retaining all binary cross terms.
The complete chain indices are1,2,6,96,96; their complete relation counts
are421070,491742,543926,377977,399945. All later input mixtures are actual
retained words in the preceding subgroup. Equal orders in the last two
steps, with the exact derived-word inclusion, prove that the index96
subgroup is perfect. Its747 original-generator conjugations prove
normality. The independent NumPy certificate replays all nested words
and shows that this subgroup is killed by the literal old S_L map.
It is therefore exactly the kernel of that96-element quotient.

Thus the full joint target has maximum solvable quotient the specified
S_L, and order2^403·3^163·5^117·7^8·11^3·13². Both the actual and corrected
common target with the old solvable T23 are exactly

    T23 ×_{S_L} T_{L,A6}.

The new triples jointly match the same Galois precomposition, so all
target maps are onto and all original identities and old target values
are retained. `de_a6_gl_target_certificate.py` passed in0.404 seconds;
the separate complete C++ certificates and normality check remain the
full presentation checks.

## Prefreeze editorial history and scope

The statement is `sections/E_a6_joint_agent.tex`, E54. Before freezing,
the three single-backslash gathered row endings in E54.1, E54.3 and
E54.19 were replaced by proper row separators. The exact new target
statement E54.6a and proof E54.22–24 were then included. The earlier draft
is recorded as `DE_a6_gl_before_target_reconstructed.tex`: preservation
was requested after the edit, so it was reconstructed by reversing only
that recorded patch. It is explicitly not represented as a separately
saved original byte stream. `DE_a6_gl_prefreeze_changes.json` records
this provenance and the before/after hashes.

Root independently opened and verified the primary Steinberg theorem
and corollary on13 November2026. The bib entry DE_Steinberg1967 is in
`DE_Steinberg.bib`. The full replay sequence and protected dependency
hashes are in `DE_a6_gl_replay.md` and `code/de_a6_gl_manifest.json`.
The accepted E48 files and earlier failed attempts remain unchanged.
