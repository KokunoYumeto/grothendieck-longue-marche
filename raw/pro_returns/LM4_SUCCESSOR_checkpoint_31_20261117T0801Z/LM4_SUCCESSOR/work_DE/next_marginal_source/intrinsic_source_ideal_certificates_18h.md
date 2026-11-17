# Infinite generation and finite positive source-ideal certificates

This note concerns the actual discrete source and the intrinsic diagonal
module of B91--B92. It does not identify a completed infinite-basis
module, solve the marginal source equality, or infer a negative result
from a finite orbit truncation.

## 1. The actual source and ambient free groups

The corrected common paired marking gives the literal one-sided fiber
retraction F13 -> F5. Write the eight deleted free generators as a_j
and the five retained generators as t_i. Thus

    F13 = F(a_1,...,a_8) * F(t_1,...,t_5),
    R = ker(F13 -> F5).

The standard rose-cover Schreier basis of R is

    { t a_j t^-1 : t in F5, 1<=j<=8 }.

Here t is its literal reduced word in the retained free factor. It
follows directly that R_ab is the direct sum of copies of Z indexed by
F5 times {1,...,8}; equivalently R_ab is Z[F5]^8 as a retained-deck
module. In particular its abelian group rank is infinite.

The actual source package symmetric_full_source_data.json specifies
eight seed words s_j in R and eleven source operators gamma_i on F13.
The explicit rank47 cover and28 basis fillings independently prove

    I = < gamma_w(s_j) : w in F11, 1<=j<=8 >.

The source map F19 -> F11 is a literal free-factor retraction, so this
is subgroup generation, not an ambient normal-closure replacement.

The inherited LM4 F21 normal-generation comparison, transported through
F22 and the actual source/ambient cover comparison in B78, proves that
I normally generates R internally. This same discrete comparison is
the input already audited in B90. Passing to R_ab makes normal
conjugation trivial, hence the map I_ab -> R_ab is surjective.

## 2. Exact obstruction to global finite stabilization

There is no finitely generated subgroup J of R which contains all eight
actual seeds and is stable under all eleven operators and their inverses.
Indeed stability would give I subset J. Since I normally generates R,
the image of J in R_ab would be all of R_ab. But the image of a finitely
generated group in an abelian group is finitely generated, contrary to
the explicit infinite-rank Schreier calculation above.

In particular I itself is not finitely generated. A finite folding
algorithm cannot legitimately terminate with a finite globally stable
subgroup equal to I. This is a theorem about this actual source, not a
heuristic about the expected size of an orbit computation.

It does not rule out a finite controlled block stable under a specified
proper subset of operators. Such a block can be useful for individual
positive membership certificates, provided its stability is checked
literally on a generating set in both signed directions.

## 3. Intrinsic diagonal values avoid a presentation-kernel identification

Let P and Lbar be the actual modules of B91. An explicit finite chain
v in Lbar, expressed as a finite sum of actual node columns and their
certified old-base/deck translates, is a genuine input for the intrinsic
map H1(C2,Lbar) -> H1(C2,P) when F(v)=-v is checked on every full cell
and coefficient. Its diagonal Tate value psi lies in U. Thus psi modulo
J_I is an actual element of im(kappa), without identifying the kernel
of the stored common-whisker presentation with B92's chosen kernel Z2.

The two common-whisker repeated-column relations alone do not supply
such an anti-invariant v or a nonzero kappa value. Their symmetrized
kernel witnesses are norms. An equivariant induced common refinement
can supply an honest H2 representative when needed; it does not justify
literal equality of the two original presentation kernels.

## 4. A finite certificate that one diagonal value is zero

By definition

    J_I = sum_{i in I} F2[R](i-1).

The quotient F2[R]/J_I is the permutation module on the left cosets
rI. For a finite-support psi, membership in J_I means that the sum of
its coefficients in each actual coset is zero. The support elements
are words in R, hence may be compared in the ambient free group F13
using the explicit Schreier expansion above.

Choose finitely many actual orbit words u_k in I, each accompanied by
a literal source witness. Put J0=<u_1,...,u_m>. A weighted folding of
these words in F13 can return a word in the u_k for any certified
membership r^-1 s in J0. Every returned word must be checked by direct
free substitution; no rank or finite-orbit inference replaces that
check.

Partition the finite support of psi by the certified J0 coset relation.
If every block has even F2 coefficient sum, choose a representative r
in each block. For every other support element s in that block, the
certificate gives i=r^-1 s in J0 subset I. Pairing the support terms
then gives the explicit finite identity

    psi = sum r (i-1),  with every i supplied by a source word.

This proves psi=0 modulo J_I. It is an exact positive certificate even
though J0 is only a small subgroup of I. A failed membership or parity
test in J0 proves nothing about the corresponding test in I.

## 5. Source words and action convention

Label the actual source free basis by eleven heads h_i and eight seeds
s_j. Geometric source push is gamma_i(x)=h_i^-1 x h_i. An orbit seed
therefore has the source witness obtained by the same signed conjugation
word. Products and inverses of certified orbit seeds remain literal
F19 words in the retraction kernel. They can be independently evaluated
using the eleven stored F13 actions and their inverses; the head word
must reduce to1. This fixes the chronology and prevents an implicit
change to the other conjugation convention.

The old weighted_stallings.py module returns explicit words in its
supplied finite generators and checks every answer by substitution.
It may be used with actual source witnesses attached to those
generators. No new orbit search or finite quotient census is launched
by this protocol. A negative diagonal result requires a genuine full
source-coset separator or another complete argument, not failure of
this finite positive-certificate procedure.

## 6. No finite left-ideal stabilization

The actual source ideal J_I is not finitely generated as a left
F2[R]-ideal. More strongly, no left submodule U of the augmentation
ideal I_F2[R] containing J_I can be finitely generated.

To prove this, suppose U is generated by finitely many augmentation-zero
polynomials f_j. Each has finite support. Choose one support word b_j
for each nonzero polynomial. The augmentation-zero condition expresses
f_j as a sum of differences a-b_j. Each difference equals
b_j(b_j^{-1}a-1). Let H be the subgroup generated by the finitely many
support differences b_j^{-1}a. Then every f_j belongs to J_H, whence

    J_I subset U subset J_H.

The quotient F2[R]/J_H is the permutation module on left cosets rH.
For each i in I, the vanishing of i-1 in that quotient forces iH=H,
so I is contained in H. But the image of a finitely generated H in
R_ab is finitely generated, whereas the actual image of I is the whole
infinite-rank R_ab=Z[F5]^8. This is a contradiction.

In particular, the four-source ideal J4 in B94 and the eight-source
ideal J4+alpha0(J4) in B95 are strictly smaller than J_I. This does not
produce a nonzero obstruction modulo J_I; those computed values still
vanish there. It rules out finite global stabilization of the full
cohomology image as an F2[R]-left ideal. It does not rule out a finite
recursive specification involving all actual base automorphisms, nor
a uniform proof for their infinite orbit.
