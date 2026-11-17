# Independent review of the shared five-generator neck

Status: PASS for the first-arc, one-neck result in
`work_CE/shared_five_generator_neck_21h.txt`, read completely. Neither
the other four necks nor a profinite amalgam theorem is inferred.

## Exact sheet selection

For `q=exp(i phi)` with `0<phi<2 pi/5`, and
`u=exp(i theta)` with `theta=2 pi j/5`, the independently checked
coordinate identity gives

    (T_u+1)/(T_u-1)
      = i (1-cos theta) (cot(phi/2)-cot(theta/2)).

The factor on the right has positive imaginary part, since cotangent
is strictly decreasing on `(0,pi)`. If `Z=i y` with `y>0`, then

    Im((Z+1)/(Z-1)) = -2y/(1+y^2) < 0.

Thus all four literal A punctures lie in the lower t semicircle.
The branch `exp(-i phi/2)` does also. Their F partners lie in the
upper semicircle. This proves the family labeling, not only a count.

In `y=t^2`, choose an annular-sector disk containing the five deleted
points other than the retained point 1 and avoiding the cones 0 and
infinity. The lower lift contains exactly the four A punctures and
the indicated branch puncture. A connector in the small gap near the
retained point fixes the common sheet and based free group K of rank 5.

## Common neck and endpoint representatives

Choose a small simply connected q neighborhood of `exp(i pi/5)`
avoiding the complete critical set and all old punctures. The literal
puncture motion gives a common isotopy of the disk and its arc system,
fixing the gap connector. At a selected inner endpoint, all five moving
points lie outside the unit circle; at the selected outer endpoint,
all lie inside it. The transported disk can be isotoped into the
corresponding bad side at each endpoint, inside the same lower
half-plane and avoiding the other punctures. Both representatives
are peripheral disks around all five points of that half-plane, so
this endpoint isotopy does not change the based subgroup.

This is an endpoint construction through a regular neck. It does not
require a disk to stay wholly in a bad side at the middle unit-circle
fiber. The common group is therefore literally K, with one system of
whiskers, rather than two independently chosen free factors.

The resulting ordinary orbifold fiber marking is

    C2_0 * C2_infinity * K.

Its two bad factors share K. Their full injections after critical
filling have not been asserted.

## Detector and topology

Filling only the B graphs gives the actual sphere-eight-puncture
bundle Q_A over the old q base. The remaining graph collisions occur
only at removed old base values. The chosen disk contains five of
these eight punctures and has three outside; its subgroup is a
literal free factor F5 in the fiber F7. The base has vanishing pi2,
so the fiber injects in the bundle group. Over the indicated regional
bases the base group is free. Characteristic finite quotients of F7,
together with the finite image of each monodromy action, give its
full induced profinite topology. The free-factor retraction gives
the same assertion for K.

The one-family filling is not F-equivariant. The proof correctly uses
it only on the ordinary index-two subgroup. A kernel word from K in
a bad orbifold vertex would be trivial in the regional orbifold group,
hence in its ordinary subgroup, and then in the ordinary detector.
For topology, take the finite-index core under the external involution
of the detector kernel. This extends the separating finite quotient
to the orbifold group. It proves full K topology in each bad vertex;
it does not prove efficiency of an amalgam of those vertices.

On the simply connected slit bases used below, the same detector
actually gives a retraction from the ordinary index-two subgroup of
each bad vertex onto K. The filled bundle group is its fiber F7;
compose the ordinary filling map with the explicit free-factor
retraction F7 to K. Its restriction to the literal K is the identity.
Thus K is a virtual retract of each bad vertex. No equivariant
one-family filling is asserted, and this strengthening alone does
not settle profinite efficiency of their amalgam.

## The discrete one-neck pushout

The slit inner and outer bases may be chosen simply connected, retain
all their actual critical values, and meet through one contractible
regular neck. Their orbifold groups are `C2_0*R_-` and
`R_+*C2_infinity`. In the pushout over
`C2_0*C2_infinity*K`, eliminate the two free cone generators against
their actual representatives in the opposite vertex. The remaining
pushout is `R_- *_K R_+`. Since K injects on both sides, this is an
actual discrete amalgam. It does not require the full neck fiber
to inject in either region.

An involution in a vertex fixes no edge because K is torsion-free,
so its centralizer in this amalgam lies in that same vertex. The
centralizer inside the bad vertex remains uncomputed. No global or
completed fixed-source equality follows.

## Limitation of a common supported point-push extension

An unrestricted annular point push can change the chosen square-root
sheet of an individual puncture. It cannot automatically be realized
on both bad sides with the same marking. For a closed puncture
trajectory supported in `|y|>1`, its winding numbers about 0 and 1
are equal: the segment from 0 to 1 is disjoint from the trajectory.
For a trajectory supported in `|y|<1`, its winding about 1 is zero.
A common regular-neck isotopy fixing `0,1,infinity` preserves these
integer winding invariants. Hence a pure trajectory represented in
both supported subgroups has winding zero about 0 and cannot flip
the square-root lift. The argument applies to each labeled track.

This refutes only that common-supported-push extension mechanism.
It does not rule out every possible abstract common K marking on
the other necks. Their actual comparison remains a separate gate.
