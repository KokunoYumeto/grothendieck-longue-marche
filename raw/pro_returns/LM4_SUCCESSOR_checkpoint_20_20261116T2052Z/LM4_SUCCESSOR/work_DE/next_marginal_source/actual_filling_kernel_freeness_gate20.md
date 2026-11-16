# The actual one-family filling kernel: exact geometric freeness gate

Research audit, 16 November 2026, checkpoint 20 cycle. The actual
freeness of N_A, or of its subgroup M, remains open.

## 1. The divisor section that must actually be controlled

Retain X, A, B=F(A), Y=X minus A, V=X minus B, and
Z=X minus (A union B) from the symmetric-deletion proof. Here
`N_A=ker(pi1(Z)->pi1(V))`. The surface V is the actual F13-by-F6
bundle over `B0=C* minus mu5`; it is aspherical. The eight components
of A are mutually disjoint in X. Each A-component intersects the
other family in exactly eight distinct points. These facts are
geometric input, not a freeness theorem.

For example, A_v(u) is parameterized by `(v,w)=(u,q/u)`. Its
intersection with V is exactly B0 minus eight additional, distinct
node values. Consequently its fundamental group is F14. Applying the
actual involution identifies its map to V with the following actual
section of Y over that punctured base:

    q |-> ((u-q)/(u-1), q(u-1)/(u-q)).                 (1)

The product of the two coordinates in (1) is q. The six old base
generators therefore inject in pi1(Y) under this section: their
composition with the q projection is the identity on the chosen F6
splitting. Every possible kernel of this F14-to-pi1(Y) map lies in
the normal closure of the eight new puncture meridians. Those
meridians individually map to actual meridians of the removed A
components. Injectivity of their entire free orbit family is a
separate statement and is not supplied by the base projection.

In particular, B101's nontrivial kernels after filling the four old
q holes to X0 do not prove noninjectivity of (1). An old-base word
nontrivial in F6 cannot lie in this actual section kernel, regardless
of its subsequent image in the smaller filled base.

## 2. What a free-kernel proof would have to add

The cover of Z associated to N_A is the complement of all lifted A
components in the contractible universal cover of V. Its fundamental
group is N_A. A genuine deformation to a graph, or an explicit free
meridian normal form for this complement, would prove N_A free and
hence M free. Contractibility of the ambient cover alone does not
give such a deformation.

Even the preliminary assertion that every lifted A-component is
simply connected requires injectivity of the actual punctured section
map (1), which has not been established. If that assertion were
proved, a simultaneous unknottedness/graph-complement argument would
still be needed: no theorem identifying complements of arbitrary
contractible codimension-two submanifolds with a wedge of meridian
circles is being used. The components are graphs only over the base
with their eight collision values removed; at those values their ends
approach the removed B punctures. They are not eight disjoint sections
of the entire one-sided bundle over B0.

Equivalently, write the paired generic group as
`W=F(A)*F(B,T)` and put `Q_A=F(B,T)=F13`. Before node filling the
one-family kernel `K_A=ker(W->Q_A)` has the literal free basis
`y a_i y^-1`, for y in Q_A and a_i one of the eight A generators.
On the actual even-base model, the filled N_A is

    K_A / normal_closure_K_A({h r_nu h^-1:
                       h in W semidirect S, 1<=nu<=128}),

where all the conjugates lie in K_A because the one-sided filling
annihilates the actual node relations. The finite even base changes
neither this kernel nor the completed family of relations: both
sheets' critical disks are included. This quotient is a group
quotient, not an abelian relation-module quotient.

A sufficient algebraic criterion
would be a single free basis of this generic kernel and a subset of
that basis whose normal closure is exactly the full actual node
relation normal subgroup. The corresponding remaining basis elements
would then freely generate N_A. A compatible infinite Nielsen
elimination with a proved inverse and well-founded dependency order
would provide the same conclusion. Neither criterion follows from
individual primitivity of all displayed relations.

The analogous quotient for the mixed kernel is

    M=N_gen / normal_closure(all actual W/source translates
                            of all 128 node relators).

CE's exact nonlinear comb basis identifies N_gen and every printed
relator as an actual free word. Its 128 individual primitive witnesses
are useful but do not provide a simultaneous basis for this entire
normal closure. Different operator translates can reuse the same
elimination letter, and their transported conjugators must be retained.
The complete source-orbit relation kernel from B104.8 records precisely
why no finite primitive-list argument is sufficient.

## 3. A checked literature boundary

I opened the primary author paper:

Papadima, S., & Suciu, A. I. (2002). *Higher homotopy groups of
complements of complex hyperplane arrangements* (arXiv:math/0002251v4),
Sections 4.4–4.8, pp. 12–14.
https://arxiv.org/pdf/math/0002251

Its hypersolvable deformation theorem gives iterated free-group
extensions for hyperplane arrangements satisfying the actual solvable
extension conditions. Those hypotheses are not established here.
Our retained divisor includes four conics. Even the proposed direct
addition of the new parallel lines fails the old-line closure
condition: in the projective coordinates of the symmetric note, the
old lines x=z, x=-z and z=0 meet at [0:1:0], and every new line
x=x_u z passes through that same old multiple point. Thus that direct
one-step application is unavailable even after discarding the conics.
This does not exclude a different proved comparison or composition
series; none has been constructed.

The ordinary fibre-type bundle theorem cannot be applied to Z's
q projection across the actual A/B nodes. Its generic fibre loses a
puncture at each node. The individual one-sided bundles are valid,
but their two-family complement is not inferred to be a bundle.

## 4. Relation to the actual torus sphere

B100/B105's Z3 subgroup and nonzero attaching sphere are compatible
with a hypothetical free N_A: the displayed Z3 meets N_A in the
single A-meridian direction. They therefore do not refute N_A or M
freeness. Conversely, B105's nonzero spherical image supplies no
graph model for N_A and does not exhaust the actual second homology.

The precise remaining structural target is the full meridian relation
family in Section 2, or an actual graph model of the stated covering
complement. Neither freeness nor nonfreeness is concluded.

## 5. Exact reflection-chart incidence for a possible relative comparison

In root's actual coordinates

    v=(a+1)/(b+1),  w=(a-1)/(b-1),  F(a,b)=(a,-b),

the eight A lines and their eight F-images have equations

    A_u^epsilon: a-u*b=epsilon*(u-1),
    B_t^delta:   a+t*b=delta*(t-1),

where u,t range over mu5 minus1 and epsilon,delta are +1 or -1.
Their common point has

    b=(delta*(t-1)-epsilon*(u-1))/(u+t).

The denominator cannot vanish because -1 is not a fifth root of
unity. Thus every cross-family intersection is affine. The two
families' points at infinity are [u:1:0] and [-t:1:0], respectively,
and these sets are disjoint. The already checked64 actual mixed
nodes therefore account for the entire affine degree8-by-degree8
intersection count, with no unrecorded shared infinity point.

Internal incidences remain substantial. The four A_v lines concur
at(-1,-1), the four A_w lines at(1,1), and the pair with the same u
is parallel. The F-image pencils concur at the other two corners.
All these corners belong to the retained boundary; the remaining
internal intersections likewise occur on retained divisors. A
deformation of only the16 new lines does not automatically preserve
these incidences with the old boundary D.

Root is separately auditing the original Oka--Sakamoto product
theorem. The maximum cross-intersection count is verified here; no
relative version with D retained is asserted. The previously proved
retained-hyperbola countermodel already excludes an automatic
relative product inference from that count alone. Any useful
application must provide the actual relative deformation or group
comparison with D, beyond this exact incidence calculation.
