# Faithful boundary models for the full relation module and its Tate class

Research proof, checkpoint20. This is an exact change of representation,
not a vanishing result or an overlap computation. All modules and
automorphisms refer to the actual paired marking of B91–B99.

## 1. Actual free groups and coefficient group

Let W=F(p1,...,p21). The retained generators have indices
(1,4,9,14,19), identified in that order with the basis y1,...,y5 of
T. The deleted A slots are J={2,3,5,6,7,8,10,11}; their B partners
have indices i+10. The actual involution swaps each A/B pair, inverts
y1, and exchanges y2/y4 and y3/y5. Write beta for its action on T.

The retained splitting is the actual free-product splitting of W.
Its kernel is R_A * R_B. Use the common basis

 x_(g,i)=g a_i g^-1, g in T, i in J,

on the A factor. On B use beta of the physical retained whisker, as in
B94, so F exchanges the two factors with identical common labels.
Conjugation by t in T acts by tau_t(x_(g,i))=x_(tg,i) on A and
tau_beta(t) on B. Thus

 G=(R_A times R_B) semidirect T,
 (u,v,t)(a,b,s)=(u tau_t(a),v tau_beta(t)(b),ts),
 F(u,v,t)=(v,u,beta(t)).

This is the actual quotient of W obtained by killing all mixed
commutators. Put N=ker(W->G), Omega=Z[G]. The product-tree square
module P of B91 is naturally N_ab: the E-cover of the generic
free-product graph has cycle group N_ab, and filling its product
squares gives the contractible product of the two Cayley trees.

## 2. The uncollapsed21-row model

The actual G-cover of the21-generator rose has vertex set G and
positive edges (g,j) from g to g*p_j_bar. Its cellular chains are

 C1_full=Omega^21 -> C0_full=Omega,
 d_full(e_j)=p_j_bar-1.

It is a graph with fundamental group N, so

 P = N_ab = H1(cover) = ker(d_full).                      (1)

For a literal word w in N, its complete cycle is the evaluated Fox
chain: a positive letter contributes its preceding G prefix to that
letter row; a negative letter contributes minus its following prefix.
This has size at most the word length before collection and retains
all retained-generator contributions.

Every actual old or source automorphism alpha of W preserves N,
because it preserves the two peripheral-family filling kernels (or
exchanges them in the case F). Let alpha_G be its actual induced
automorphism of G. The21 actual words alpha(p_j) give the genuine
semilinear chain map

 a e_j -> alpha_G(a) * Fox_G(alpha(p_j)).                 (2)

The Fox product identity D(uv)=D(u)+u_bar D(v) proves the chain rule.
The stored inverse word automorphism supplies its inverse chain map.
This is a finite21-by21 operator description with all mixed retained
conjugators present. It is not the action inferred only from the two
quotient-factor automorphisms.

## 3. Collapse the actual retained forest

The five retained edge types form a forest in the cover. Each component
has vertices gT and is the Cayley tree of the freely embedded T, using
right multiplication by its five basis elements. Collapse these
components. The vertex set becomes G/T, identified with E=R_A times R_B;
the nonretained edges remain the16 types A_i,B_i. The chain model is

 C1_col=Omega^16 -> C0_col=Z[G/T]=Z[E].                   (3)

The quotient is G-equivariant. It is not a G-homotopy equivalence of
spaces: the collapsed vertices acquire T stabilizers. What is used is
the exact G-equivariant isomorphism on cycle groups. The retained
forest boundary is injective, with image ker(Omega->Z[G/T]).
Therefore each collapsed cycle has a unique retained-forest completion
to a full21-row cycle. Projection and this completion identify the
kernels of (1) and (3), including their full G and F actions.

An A edge at vertex(a,b), with common generator x_(g,i), has the unique
normal form

 (a,b,g) * A_i.

A B edge at(a,b), with common generator x_(h,j), has the unique form

 (a,b,beta(h)) * B_j.                                   (4)

The coefficient is forced by the edge's initial vertex and retained
generator label. In particular G acts freely on oriented edges, and
the16 rows are genuinely Omega-free. Its action on vertices is

 (u,v,t) dot(a,b)=(u tau_t(a),v tau_beta(t)(b)).

The collapsed graph is exactly the one-skeleton of T_A times T_B.
That product is contractible and has dimension two. Its square boundary
therefore gives a G- and F-equivariant injection

 j=partial2:P -> Omega^16,

with image ker(d_col). This proves equality of complete chains from
equality of their boundaries; there are no hidden finite2-cycles in
the product of trees.

The existence of a free Omega-rank64 submodule of this rank16 ambient
module is not contradictory. Omega is a noncommutative group ring,
and no dimension argument over a field, Ore localization, or presumed
flat field of fractions is being used.

## 4. Exact involution and Tate extraction in16 rows

The actual involution exchanges the two positive edge directions:

 F(a*A_i)=F(a)*B_i,   F(a*B_i)=F(a)*A_i.                 (5)

Hence the underlying abelian C2-module C1_col is a direct sum of
two-element permutation orbits and has zero Tate cohomology in every
degree. Let I_vert=ker(Z[E]->Z). The exact sequence

 0 -> P -> C1_col -> I_vert -> 0                        (6)

identifies H1(C2,P) with Tate H0(C2,I_vert). On vertices F swaps the
two R coordinates. The fixed vertices are precisely(a,a), a in R.
The elementary permutation-module calculation identifies

 Tate H0(C2,I_vert) = ker(F2[R]->F2).                    (7)

For an actual integral anti-chain u in P, put v=j(u). Check the exact
equation F(v)=-v. Let h be the A-edge part of v. Then

 v=h-F(h),    q=d_col(h),    F(q)=q.                     (8)

Its Tate coordinate is the finite group-ring element

   sum_a (coefficient of vertex(a,a) in q modulo2) * a.  (9)

The sum has augmentation zero. Formula (9) is exactly the connecting
map of (6), with a harmless minus sign killed in its exponent-two
target. It retains every actual R word and every transported coefficient.

For calibration, a square made from the two root paths1->a has A-edge
part H(a,1)-H(a,a). Its vertex boundary has diagonal coefficients
-1 at1 and -1 at a; (9) is a-1 in characteristic two. Translating by
the diagonal a^-1 gives the established right-defect coordinate a^-1-1.
This explicitly matches the left/right endpoint convention.

One may also extract the class in21 rows. The paired rows are exchanged;
the remaining inverted y1 row has action e_g -> -e_(F(g)y1^-1).
It has no fixed coefficient index, since beta(t)y1^-1=t would conjugate
the two distinct cone involutions in T semidirect C2=C2*C2*F2.
Thus its signed basis also consists of two-element orbits. The
21-row chain module is Tate-acyclic as well. The16-row A-half in (8)
is simply a more convenient canonical choice.

## 5. The entire orbit-sum kernel is preserved

Let D_old be the actual direct sum of formal translated node modules
of B96, or use the preferred source-orbit sum of the full block
L8=L_ret direct-sum alpha_b^-1 L_ret. Compose its genuine column map
with (1) or (3). Since both boundary representations are injective,

 ker(D_old->P)=ker(D_old->Omega^21)=ker(D_old->Omega^16). (10)

This equality concerns the whole actual relation kernel, not only
pairwise column equality. The source Fox matrices (2) supply exact
uniform operators on the full21-row model. A general old operator
need not preserve the retained forest. Its action on a16-row cycle
is therefore: restore the unique retained completion, apply (2), and
project. No naive16-by16 extension to every edge is asserted.

For a finite actual formal cell chain p, compile its complete boundary
v. The equality F(v)=-v proves that (1+F)p belongs to the actual
relation kernel, by (10). Formula (9) then computes the exact B92
edge value before quotienting by J_I. A finite positive source-ideal
certificate may prove this value zero. Without such a certificate or
an actual separation theorem, a nonzero displayed polynomial is not
a nonzero class modulo J_I.

These representations do not prove that every orbit relation has been
generated by a finite list, that H2(M) vanishes, that kappa is zero or
nonzero, or that the nonlinear/compact fixed lifts exist. They give
faithful finite-support coordinates and genuine finite source operators
for investigating those questions without a huge square expansion.

## 6. A finite free complex retaining the entire source orbit

There is a useful stronger packaging of the same actual data. Pass to
the even old-base double cover. Its retained base has free group S=F11,
with the eleven actual fixed-source lifts as specified generators.
Write psi_i for their actual geometric pushes, using the convention

  s_i^-1 x_j s_i = psi_i(x_j).

The prefilled graph bundle has group W semidirect S. Its quotient by N
is the actual group P_even=G semidirect S, with that displayed convention;
if the usual left-conjugation convention is used instead, the acting
automorphism is psi_i^-1. No sign is hidden by the semidirect notation.

The finite relative nodal model of B102 gives a two-dimensional CW
model of the actual even cover of Z. Start with the21-generator fiber
graph over the11-generator old-base graph. Its mapping cylinders
contribute21*11 two-cells. The36 lifted critical disks contribute128
actual node two-cells, one for each original cell and its audited
opposite-sheet translate. Their extending regular-section base lassos
are eliminated by the relative local models. At a fixed node the
source peripheral becomes its actual fiber product ab; it is not
silently discarded. The cell counts are therefore

  C0:1,   C1:21+11=32,   C2:21*11+128=359,

and the Euler characteristic is328. The Euler count is a consistency
check; the relative local comparison, rather than this count, proves
the CW model. A independently checked this finite gluing argument.

All node relators lie in N, so the quotient by the actual mixed kernel
after their filling is exactly P_even. Its cover has fundamental group
M and is the same cover C_E studied in B102, now viewed with its larger
deck group. Put Lambda=Z[P_even]. Its cellular chains are the finite
free complex

  Lambda^359 -> Lambda^32 -> Lambda.                    (11)

The first21 one-cells have boundary x_j_bar-1 and the last11 have
boundary s_i-1. For the mapping-torus face

  s_i^-1 x_j s_i psi_i(x_j)^-1,

the exact Fox boundary is

  s_i^-1 e_j - Fox_G(psi_i(x_j))
       + s_i^-1(x_j_bar-1)e_(s_i).                      (12)

The order of the coefficients is essential. Applying the one-boundary
to (12) gives s_i^-1 x_j_bar s_i-psi_i(x_j)_bar=0, so the formula
agrees with the actual conjugation convention. A node face has its
complete21-row Fox cycle and zero entries in the11 base rows.
Its opposite-sheet counterpart is the actual audited odd pullback,
as in L8; no independent choice of a conjugator is made.

The universal-base nodal model of B102 and the finite model (11) are
models of the same actual cover. The retained and base tree expansions
give the compatible chain comparison. In particular H2 of (11) is
the full Z2 with its larger deck action, not the kernel of a truncated
old-word orbit. The eleven finite source Fox matrices supply all
source translates algebraically through Lambda.

This does not assert that the kernel of the finite matrix is finitely
generated, that Lambda is Noetherian, that a finite orbit calculation
is exhaustive, or that a field-rank argument is valid. It also does
not erase the separate nonspherical quotient H2(M). It replaces an
infinite orbit list by an actual finite cellular presentation with
the complete coefficient group and all genuine source operators.
