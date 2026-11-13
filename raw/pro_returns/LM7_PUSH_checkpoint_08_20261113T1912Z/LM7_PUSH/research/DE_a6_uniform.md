# E57: exact full A6 and uniform symplectic comparison

The statement is `sections/E_a6_uniform_agent.tex`. All E54 files remain
unchanged. New computation and provenance use `de_a6_uniform_*` only.

## Closed source maps

Let J=G_A6×_{Q30}G_L be the actual E54 source. Its perfect residual is
C_J=C_A6×_{A5^3}C_L. Put E=image_G(F′), P=image_G(N), and

    R0=E×_{A5^3}C_L,   R1=P′×_{A5^3}C_L.

The full H-commutator calculation is rank9 on the entire ternary layer
and rank6 on the binary layer, with every chosen column evaluated in
the complete solvable collector. R0 lies in the actual H image: the
specified Q30 coordinate has zero ordinary exponents modulo30, so
every compatible source lift belongs to H=F′F^3. The perfect C_J and
these two ranks give [image(H),R0]=R0. Compactness proves the exact map
R_nil(H)→R0 onto, with reverse inclusion from the actual F′ and signed
residual maps.

The finite abelianization of R0 has only2/3 primes, whereas the finite
abelian quotients of C_R=SL2(R)×V3(R) have primes at least5. Their actual
Goursat common quotient is therefore perfect. The central V3(R) image
then lies in the center of a finite quotient of SL2(R). E53 proves that
this center has exponent dividing2; the additive image is zero. This
ordering of the argument is essential: perfection is proved before the
center bound is applied.

The exact source power relation is x^120=y^120=1 in J. The new code
checks exact order120 in the full9462-point A6 source and exact order30
in all36 signed Ferrari coordinates. For the actual signed matrix map,
theta(x^120)=E21(240). The integral identity is

    [E21(t),E12(1)] = [[1−t,t],[−t²,1+t+t²]].

For t=240 the first five-adic layer is [[2,3],[0,3]], and three actual
conjugates span sl2(F5). At every p≥7 the upper-right entry is a unit.
The exact normal-subgroup argument of E53 therefore gives the whole
SL2(Zp) at p≥7 and the first principal congruence subgroup at5. The
retained signed mod5 map gives the reverse inclusion. Consequently

    rho_R(R_nil(H) ∩ ker J) = K_R,

with exactly the same K_R as E53. Intersecting with ker D23 retains it
by the proved disjoint-prime common-quotient argument, and intersecting
with the level5/7 kernels gives precisely K_R^35.

## Direct correction of every full E55 word

For I=gamma5(Nhat)∩R_nil(H), E52 gives rho_R(I)=SL2(R)×0 by iterated
H-commutators and compactness. E54 gives rho_J(I)=R1. The same x^120
commutator belongs to I∩ker J and gives its full matrix kernel. Hence
the actual joint I image is exactly

    R1 ×_{SL2(F5)} SL2(R),

where the first map is the specified G_L signed modular coordinate
and the second is reduction modulo5. This provides the exact onto map

    I ∩ ker G_L ∩ ker G_R → ker(P′→A5^3).

For any full old E55 word f55, the required A6 difference from the same
Galois word lies in P′ by the complete E48 old-kernel comparison and
has trivial A5^3 coordinate because the signed values already agree.
The displayed map corrects this difference while retaining the entire
old word value: D23, G_L, all symplectic congruence levels, and every
nilpotent H-boundary factor. The chosen subgroup fibre and the full
profinite commutator-word fibre are both printed explicitly in E57.

The actual common source is identified cofinally using the specified
quotient A_(2m)×_{A_(2g)}J_g, g=gcd(m,5), for finite E54 old sources
retaining P_(4m). The new kernel is the reduction of K_R. The corrected
old projection is onto by E54; Galois precomposition transports the
same residual image, and the separate corrected D23 condition leaves
the kernel image intact. This proves full joint generation. No source
kernel invariance is inferred from separate finite shadow generation.

## Uniform full target products

Both full Ferrari target triples have exact generator order60. A
nontrivial parabolic common quotient has one of the actual projective
SL2(Fp) simple quotient maps from E56. At p≥7 its standard braid
generator has order p, which contradicts the literal order60 relation.

At p=5 the complete new536-point action is the actual530-point A6
Nielsen image together with the6-point projective W quotient of the
transposed symplectic model. The exact row/column comparison is checked
in dimension4. The complete chain has219684 final relations and order
60 times the Nielsen order. Four actual braid words are identity on all
530 old points and generate the whole PSL2(F5) on the extra6 points.
They are independently evaluated from the retained word DAG. Thus the
specified map does not factor through the Nielsen target; any map from
the full A6 target to A5 first kills its perfect free A6^53 subgroup.

Every simple quotient of the actual TL/A6 subdirect target factors
through one projection, because its two projection kernels commute.
The p=5 map factors through neither projection: E50 excludes TL and
the new exact kernel words exclude the A6 target. Hence there is no
common parabolic quotient at any prime or precision. This gives the
full product with the symplectic stabilizer, retains the exact old S_L
solvable quotient for T23, and retains the A96 factor. The latter cannot
be a quotient of TL/A6, whose proved order has no factor17. E56 already
excludes A96 from the matrix factors. All corrected new target maps
are one and the same Galois precomposition.

## Executed certificates and preserved preliminary failures

`de_a6_uniform_comparison.py` passed in2.078 seconds. It independently
checks the full source power relations, full H ranks9/6, exact signed
matrix convention, polynomial commutator, level25 vector, and three
conjugate Lie vectors. It retains all chosen literal word columns.

The first invocation stopped at an assertion comparing the established
string encoding of a matrix with an integer list. The actual matrix was
already [[1,2],[0,1]], as independently printed. The complete script,
stdout and traceback are preserved as
`de_a6_uniform_failed_initial_encoding.*`. The comparison now explicitly
constructs the same SymPy matrix from the encoded entries.

The second invocation stopped at structural equality of an unexpanded
SymPy polynomial matrix; its lower-left entry was t−t(t+1). That script,
stdout and traceback are preserved as
`de_a6_uniform_failed_unexpanded_polynomial.*`. Exact polynomial expansion
now verifies the stated matrix identity. Neither preliminary run wrote
an accepted mathematical output or supported a negative conclusion.

`de_a6_uniform_target_prepare.py` retains the exact three source maps.
`de_a6_uniform_target.bin/.out` is the complete C++ chain, PASS5.827s.
`de_a6_uniform_target_certificate.py` independently replays every saved
word, the four pure-kernel words, their full60-element image, the exact
four-dimensional quotient matrices, and all six full target orders.
All earlier mathematical artifacts are protected by hashes.

The proof uses only the accepted exact comparisons in E48 and E52–56;
no new literature identification is substituted for the displayed maps.
This is a simultaneous quotient-family result. It makes no claim that
these finite targets or their specified inverse system are cofinal among
all finite quotients required for the full profinite GT problem.
