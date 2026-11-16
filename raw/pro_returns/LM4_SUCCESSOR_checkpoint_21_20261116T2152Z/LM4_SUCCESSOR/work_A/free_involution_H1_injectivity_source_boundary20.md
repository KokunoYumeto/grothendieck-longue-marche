# The exact nonlinear consequence of an actual free mixed kernel

Research, 16 November 2026. No freeness assertion for the actual group M
is made here. This records the precise consequence of that still-open
hypothesis, including the arbitrary-rank issue and the source boundary.

## 1. Canonical-basis input and source status

The Dyer--Scott canonical involution basis has fixed generators U,
exchanged pairs z,z', and blocks {x} union Y_x, with

    F(u)=u, F(z)=z', F(z')=z,
    F(x)=x^-1, F(y)=x y x^-1 for y in Y_x.

The original paper is Dyer, J. L., and Scott, G. P. (1975), Periodic
automorphisms of free groups, Communications in Algebra, 3(3), 195--201,
https://doi.org/10.1080/00927877508822042. Its publisher metadata was
opened and verified, but its PDF returned HTTP403 in this session.
Accordingly this note does not label the original proof as read.

The exact arbitrary-rank statement was independently opened in the
primary research paper Tolstykh, V., The automorphism tower of a free
group, arXiv:math/9711203, https://arxiv.org/pdf/math/9711203, Theorem2.1,
printedp3, explicitly referring to Dyer--Scott p199. Its introduction
and notation explicitly allow arbitrary nonabelian free rank. The
following implication is proved directly from that canonical-basis
statement; no later classification is assumed.

Retrieval records: original publisher metadata turn903search0 and
turn904search1; original PDF failure turn905view0; the full Tolstykh
primary PDF and exact basis statement turn904view0. No bibliography
entry or formal theorem is added on this source review alone.

## 2. Nonabelian cohomology from the normal forms

Let L be a free group with a basis of the displayed form and let
E=L semidirect <t>, t^2=1, t l t=F(l). Nonabelian H1(C2,L) is the
set of L-conjugacy classes of the involutions lying outside L.
Full E-conjugacy gives the same equivalence on these involutions:
an outside conjugator can be multiplied by the involution being
conjugated to obtain an inside conjugator with the same effect.

Decompose L as the free product of its invariant canonical blocks.
The extension E is the star amalgam of their extensions over the
common subgroup <t>. A finite-order element in such an amalgam is
conjugate into one of its vertex groups, by the elementary reduced-word
normal form. Every element and every such argument uses only finitely
many factors, so no finite-rank assumption is needed at this step.

For the fixed U block, its extension is F(U) times C2 and has only
the conjugacy class of t among its involutions. For an exchanged pair,
eliminate z'=tzt to identify its extension with <z> * <t>; again t
is its only involution class.

For the block L_x=F(x,Y_x), set j=x^-1 t. The defining equations give
j^2=1 and [j,y]=1 for all y in Y_x. Conversely x=t j recovers the
original relations. Hence

    L_x semidirect C2 = <t> * (<j> times F(Y_x)).

Its involutions have exactly the two classes represented by t and j.
The amalgam normal form keeps the new j classes from distinct x blocks
distinct; only the shared edge class t is identified. Consequently

    H1(C2,L) = {basepoint} disjoint-union {one class for each x}.

The same statements cover rank0 or rank1 directly, without the
nonabelian-rank formulation of the external basis theorem.

## 3. Abelianization detects all those classes

On L_ab, the fixed generators and the Y_x have positive action, the
exchanged pairs are induced modules, and each x is a negative rank-one
summand. Therefore

    H1(C2,L_ab) = direct-sum_x F2*x.

The basepoint maps to zero, and the class of x^-1 t maps to the
single nonzero basis vector x. These images are all distinct. Thus

    H1(C2,L) -> H1(C2,L_ab)

is injective. Its image is zero together with the individual basis
vectors in this canonical description; it is generally not all of
the vector space.

## 4. Application and exact remaining hypothesis

If the actual filled mixed group M were proved free, this injectivity
would apply to its actual involution. It would remove a nonabelian
fixed-lifting defect whose abelian class is zero, for the corresponding
actual extension and fixed target. It would not by itself show that
the abelian obstruction kappa vanishes or supply the full profinite
comparison.

At present only N_gen, before nodal filling, is proved free. Every
actual transported node relator is individually primitive in N_gen:
a local mixed commutator is a comb-basis generator, and the actual
colored-whisker automorphism preserves the two family filling kernels
and hence N_gen. Its restriction therefore preserves primitivity.
This argument applies to all actual old/source translates as well.

Individual primitivity does not make the entire transported family a
simultaneous part of a free basis. The actual quotient M still includes
the whole operator orbit, not just the128 printed seed relators.
Neither its freeness nor nonfreeness is concluded here.
