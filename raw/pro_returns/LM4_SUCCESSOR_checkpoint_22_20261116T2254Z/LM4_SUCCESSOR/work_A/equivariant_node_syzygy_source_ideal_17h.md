# Actual equivariant node module and the residual syzygy map

Research after accepted B90/B91. This refines the exact discrete criterion;
it does not assert vanishing of the new map, a compact coefficient
identification, or the full source-kernel equality.

## 1. Actual equivariant transports and node indexing

Retain all B91 groups. Write F for the based involution and R=R_A, with
R_B identified by F. On the universal base cover choose the analytic branch

    a(q)=1+sqrt(1-q), b(q)=1-sqrt(1-q)

which has a(q*)=399/200. Then a+b=2, ab=q and the actual Möbius coordinate

    z=(v-a)/(v-b)

satisfies F(z)=-z, since F(v)=(v-q)/(v-1) and
(F(v)-a)/(F(v)-b)=((1-a)/(1-b))*(v-a)/(v-b).
This is an exact coordinate on the original sphere family over the base
cover. It fixes the chosen source at z=0 and the other fixed sheet at
z=infinity.

On each compact regular base path, the finite old and new puncture
trajectories are a configuration invariant under z->-z. An ambient isotopy
of this finite configuration may be chosen equivariantly: choose moving
vector fields near the punctures, extend them with compact support, and
average under the fixed involution. The field at the paired puncture is
then the paired velocity, so averaging preserves every specified motion.
Take the fields zero at the two fixed sections. Lift the isotopy to the
universal old-fiber cover at the chosen fixed source point. Uniqueness of
the lift makes it commute with the chosen lifted F. This is applied only
on compact regular paths, where no puncture has collided with a fixed
section. The covering-local finite nodal model of B91 handles endpoints.

The fixed locus of the chosen F on Xtilde is exactly the chosen S0tilde.
Indeed a fixed point lies above S0. After lifting a path in S0 back to the
basepoint, it gives a deck element g fixed by F. B87 says Q^F=H_b, so
that lift belongs to the same chosen S0 component. Thus a lifted node is
F-fixed exactly when it is an actual intersection with S0tilde. Such
points are precisely the punctures of Stilde=S0tilde minus Atilde.

Choose compatible planar peripheral-tree paths in the simply connected
S0tilde to these punctures. The punctured Stilde is the pullback of S
associated with ker(pi1(S)->pi1(S0)). The paths give a free meridian basis
of pi1(Stilde).
Their images generate the actual source kernel I in R. These whiskers
are fixed pointwise by F.

For completeness choose the source peripheral paths avoiding all other
critical base values, and extend them on successive compact disks to one
common peripheral tree for ALL critical values. The added base points
are not punctures of the source, so the source basis is retained. Paired
fiber whiskers at the nonfixed nodes are taken over that same tree. This
preserves B91's complete actual van Kampen marking and does not replace
it by independently based lassos.

At a fixed node the two local branches are exchanged and the based local
relator is

    r_v=[p_v,F(p_v)].

The local positive source meridian is p_v F(p_v); its image in the first
factor is a_v, where the image of p_v in E is (a_v,1). The local basepoint
may lie on the diagonal source in the nearby fiber; the actual local
normal-crossing complement is Z^2, so its kernel relation is still this
commutator. No F-fixed section through the deleted node is required.
Explicitly take the actual local model {z^2-t^2!=0}, with F(z,t)=(-z,t)
and source z=0. Its source base lasso t around0 winds once positively in
both branch coordinates z-t and z+t, so it is the product ab in the
local normal-crossing group. The source is not a section of the complement
across t=0. Eliminating that lasso using a regular local section gives
the same relation [a,b]; it does not declare the source lasso trivial.
The source whisker ends at the common nearby point (z,t)=(0,epsilon),
not at the deleted node. Choose its two meridian arcs as literal F-images.
The source whisker is pointwise fixed, and the generic-fiber transport is
equivariant, so both words have exactly the same actual based whisker.
The local abelian comparison is then mapped globally by that based map;
no additional conjugator survives.

For all nonfixed lifted nodes choose one whisker and use its F-image for
the mate. Order every relator with its A meridian first and B meridian
second. Its paired relator is then the inverse F-image. These choices
are compatible with the paired generic-fiber basis through the actual
equivariant transports just constructed. Hence

    F(r_v)=r_{F(v)}^{-1}

literally in the marked generic free group, including the fixed-node
case. No unknown additional conjugator is discarded.

## 2. Equivariant free node module

Let P_node be the free Z[E]-module on these based lifted nodes. Let P be
the product-tree module of B91. Here the node indices are those in the
universal filled-surface cover Xtilde. The separate E coefficient indexes
the lifts of their attaching cells in the E cover, not another copy of
the physical node set. Define

    d:P_node -> P,     e_v -> z_{r_v},
    F(e_v)=-e_{F(v)},

with F semilinear on E by exchanging its two factors. This is an actual
equivariant map and its image is Lbar. Put Z2=ker d.

As an abelian signed permutation module, P_node has basis (e,v),
e in E, with negative exchange of e and v. Its fixed-index basis elements
are EXACTLY those with v a fixed node and e=(g,F(g)) diagonal. All other
indices occur in two-element orbits. Therefore

    H^1(C2,P_node) = direct_sum_(fixed nodes v) F2[R],
    H^2(C2,P_node) = 0.

This is a statement about ordinary group cohomology of the discrete
finite-support modules. The R action is diagonal left multiplication.

## 3. Image of a fixed-node column is the actual source meridian

For a fixed node write p=n a in the generic free product, with n in N
and a in its pure first free factor. Its E-image is (a,1), and put b=F(a).
In N_ab=P, the elementary commutator expansion gives

    z_[p,Fp]
      = z_[a,b] + (1-b)[n] + (a-1)F[n]
      = z_[a,b] + (1-F)((1-b)[n]).

The added term is a C2 coboundary. The pure rectangle z_[a,b] represents
a-1 under the natural H^1(C2,P)=I_F2[R] of B91. Thus the fixed-node
generator maps to a_v-1, exactly the first-coordinate image of the
positive source meridian. Its diagonal translates map to g(a_v-1).

Since these source puncture meridians generate I, the image is precisely

    J_I = sum_(i in I) F2[R](i-1)
        = im[H^1(C2,P_node)->H^1(C2,P)].

This identifies the free-node contribution, but not all of U.

## 4. Canonical remaining syzygy map

The exact equivariant sequence

    0 -> Z2 -> P_node -> Lbar -> 0

has H^2(C2,P_node)=0. Hence its connecting map
H^1(C2,Lbar)->H^2(C2,Z2) is onto, with kernel the image of
H^1(C2,P_node). Composing any lift through this surjection with the
map to H^1(C2,P), and then quotienting by J_I, defines a canonical
R-linear map

    kappa:H^2(C2,Z2) -> I_F2[R]/J_I,

whose image is U/J_I, for the actual U of B91. Equivalently the target is
the augmentation submodule of the permutation module F2[R/I].

There is an explicit representative formula. Represent a class in H^2
by z in Z2 with Fz=z, modulo norms. Since H^2(P_node)=0, choose p with

    z=(1+F)p.

Then d(p) is anti-invariant in P, and

    kappa([z]) = diagonal_Tate_class(d(p)) modulo J_I.

Changing p by an anti-invariant node chain changes this by J_I.
Changing z by a norm from Z2 does not change d(p). This proves
well-definedness directly and keeps the actual syzygies in the formula.

The exact RIGHT-defect criterion now reads:

    (r,F(r)) has a fixed lift in K_s/[M,M]
        iff r^{-1}I-I belongs to im(kappa) in F2[R/I].

All targets from I have zero class. If kappa vanishes then the projected
fixed subgroup of Gamma/[M,M] in G1 is exactly the actual source image H:
multiply any target above H_b by an actual fixed source lift of its head,
and apply the displayed criterion in R.

Vanishing is sufficient, not asserted and not logically necessary for
that projected subgroup equality: a nonzero submodule of the augmentation
module might contain no individual difference of two distinct coset basis
vectors. The exact membership criterion is the proved comparison.

## 5. Current scope

The finite actual braid/Fox columns being computed by CE use a common far
Schreier marking. They can be converted to the paired marking by the
actual involution and transports; no already-computed full syzygy module
or kappa is claimed here. This note does not assume Z aspherical, does not
replace its transported node words by a graph product, and does not
identify its full compact coefficient completion.

In particular normal generation of I inside R gives the surjection on
abelianizations used in B90. It does not turn this LEFT ideal into the
augmentation ideal, and does not force the crossed obstruction to vanish.
The remaining object is the displayed actual syzygy transfer into the
source-coset augmentation module, together with the separate nonlinear
kernel [M,M].

