# Independent audit of the full intersection Alexander presentation

2026-11-16, after checkpoint16. Reviewer: DE.
Input read in full: work_A/symmetric_full_intersection_Alexander_module_16h.md.
Result: PASS for the discrete presentation and its exact module model, with
the finite-cover justification below. No fixed-lifting or asphericity
conclusion is included in this audit.

## 1. Finite geometric model before passing to the filled universal cover

Use q=vw and the old base B=C*\mu5. On the sphere with coordinate v,
the old punctures are 0,1,q,+sqrt(q),-sqrt(q),infinity. The sixteen added
punctures, for u in mu5\{1}, are

    u, q/u, (u-q)/(u-1), q(1-u)/(q-u).

The first eight belong to A and the second eight to F(A). The only poles
in these functions occur at excluded base values. The two square roots
can be chosen continuously on any disk in the universal base. The exact
geometry certificate proves that the only added critical values are the
lifts of the eighteen mixed values, and that every collision is a
transverse A/B node; simultaneous nodes have disjoint local disks.

Let D be a compact disk in the universal base whose boundary avoids all
critical points. The images of all twenty-one finite punctures are bounded
on D, including on its critical fibers. A real constant R larger than that
bound gives an actual regular section v=R over D. If necessary, transport
its basepoint to the prescribed generic-fiber basepoint by a fiber path.
This changes the recorded based whiskers, not the group comparison.

The finite puncture configuration is locally trivial off the finitely many
critical points in D. Ordinary van Kampen, using the section, gives its
fundamental group as the generic F21 modulo the transported local nodal
variation relations. A local transverse two-point full twist gives the
single commutator of the two local meridians. Several disjoint nodes give
the corresponding separate commutators. Conjugating each local relation
back along its actual whisker gives precisely

    [u*a_C*u^-1, v*b_D*v^-1].

These whiskers cannot be discarded. In particular this calculation does
not identify a right-angled Artin group.

## 2. The old-fiber cover supplies every lifted relation

The filling map on the generic finite fiber is the actual retraction
F21->F5 killing all sixteen added meridians. Every transported nodal
relator maps to1 in F5. Pulling the old universal-fiber cover back over the
whole finite nodal model therefore gives the group

    ker(F21->F5) / normal_closure(all F5-conjugates of all node relators).

This is the usual Reidemeister-Schreier calculation: the free kernel has
basis the old-F5 translates of the sixteen added meridians, and a choice
of coset representatives supplies every conjugate of every relation.
Conjugation within the free kernel is included in the normal closure.
Thus there is no missing family of lifted-node relations.

Exhaust the universal base by such disks, nested after small boundary
perturbations. The preimages form an increasing open exhaustion after
slightly thickening the disks. Any loop or nullhomotopy has compact image,
hence lies in one member. Fundamental groups and these presentations pass
to their direct limit. This supplies the locally finite presentation of
K_s claimed in the proposal. It uses the actual finite nodal configuration
and its actual covering; it does not invoke a general nonproper-fibration
principle or assert properness at infinity.

## 3. Free factors and simultaneous involution marking

The old universal fiber is a disk with a locally finite set of added
punctures. Its fundamental group is the free product of the free groups
on the A and B punctures, after choosing a simultaneous planar meridian
system. Filling either family gives the respective one-sided free group
R_A or R_B. The one-sided covers are genuine bundles over the contractible
universal base, so this is the actual group comparison, not an abstract
choice of sections of a quotient.

The based lift of F is a holomorphic involution of the old universal disk
fixing the chosen source basepoint. It has a single fixed point there.
At a generic fiber no added puncture is fixed. Its quotient is a punctured
disk with one order-two cone point. Nested finite meridian systems in that
quotient give the orbifold free product C2*Free({u_i}); the unbranched
covering kernel has paired free basis u_i and tau*u_i*tau. Thus F exchanges
the A/B bases literally in this chosen marking. This is a discrete basis
statement; no claim about a completed infinite free basis is made.

## 4. Exact Alexander module

Put F=R_A*R_B, N=ker(F->E), E=R_A x R_B. The E-cover of the wedge of the
two roses is the one-skeleton of the product of the two Cayley trees.
Since that product is contractible, its boundary map identifies N_ab with
its free module of oriented squares:

    N_ab = direct_sum_(C,D) Z[E] e_(C,D).

With left-edge conventions the square boundary is

    d2 e_(a,b) = (1-b)e_a + (a-1)e_b.

The map d2 is injective. The Fox derivative cycle of every actual transported
node word consequently determines one unique finite square chain. If L
is the normal subgroup generated by those actual words, M=N/L and

    M_ab = N_ab / image(L).

Normal conjugation gives exactly the Z[E]-submodule generated by the node
chains. Thus the proposal retains all coefficient information lost by the
previous E-coinvariant calculation. Negative swap is the correct F action
on oriented squares, including the simultaneous swap of E coordinates.

## 5. Scope

The presentation and module formula are now independently audited. No
explicit full node-column matrix or relation-module membership calculation
has been performed in this audit. No statement that M is free, that Z is
aspherical, that fixed targets lift, or that the projected fixed subgroup
is the source follows from the formula alone.

## 6. Final formal-source audits

B90_proposed.tex was read completely and passed independently, including
the discrete F21/F22/B78 transfer, selected-source incidence, right-defect
correction and compact-density argument. No change was requested.

B91_proposed.tex was read completely and passed independently. The exact
Tate isomorphism H^1(C2,J tensor J)=J/2J is intrinsic and diagonal-equivariant;
H^2 is zero. For the stated right-defect convention the translated negative
rectangle gives r^-1-1, with the inverse retained correctly. The source
left-ideal quotient is the permutation module on left cosets rI. Relations
among node columns, through H^2 of their kernel, remain an explicit gap.

## 7. Fixed-node-column geometry (communicated for the next refinement)

Off nodal values, normalize the two global fixed sections over the simply
connected base so the involution is z->-z. Average the finite-family
isotopy vector field under this involution while fixing the chosen source
point0, then lift that actual finite isotopy to the old universal fiber.
This gives equivariant transports. For fixed lifted nodes, choose the
whiskers in a peripheral tree of the selected punctured source lift.

The local based distinction is essential: the source section does not
extend through the removed node. In {z^2-t^2 !=0}, its base lasso z=0
becomes the product ab of the two positive local meridians. Eliminating
that lasso yields [a,b]. Consequently the fixed node column has Tate image
i_p-1, up to the stated inverse convention, for the ACTUAL source
peripheral i_p. These peripherals generate the source-kernel image I;
their diagonal translates therefore generate its left augmentation ideal.
Nonfixed pairs of node cells are free C2-orbits and contribute no H^1.
This audits the proposed node-cell image refinement, not the vanishing of
the remaining relation-kernel H^2 contribution.

## 8. Final B92 formal-source audit

B92_proposed.tex was read completely and passed independently. Actual
equivariant transports, the nearby source point, the positive local
source lasso ab and the distinction between node indices and cell lifts
are retained. The mixed-whisker correction is the stated (1-F) boundary,
so the node-cell H^1 image is exactly the source left ideal. The further
H^2 of the relation kernel supplies the canonical additional image;
its vanishing is not inferred. Subsequent exact source-lasso and rank47
cover computations provide actual finite inputs without changing this
infinite-module limitation.
