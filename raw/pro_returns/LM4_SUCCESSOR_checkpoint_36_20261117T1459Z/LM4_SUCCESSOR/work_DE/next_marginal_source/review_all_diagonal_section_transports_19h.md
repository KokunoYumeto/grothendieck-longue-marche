# Independent all-eight diagonal-kernel transport review

The research extension of B99 passes in its stated zero-kernel scope.
The independent checker `verify_all_diagonal_section_transports.py`
imports no CE producer. It uses the owned rational quadratic crossing
routine, resolves simultaneous crossings from the right, and reconstructs
the three polynomial four-strand bridges from their exact endpoints.
It checks both directions of every Nielsen transport, both transported
old-zero/old-one operators, the literal node words, all four static
fillings, and the eight actual augmented-row involution conditions.
Its genuine output and complete certificate are retained alongside it.

## Literal static filling and bridge direction

The audited old six-cut physical ordering is
(zeta²,zeta³,zeta,0,zeta⁴,1), and the named old meridians map to
(x4,x6,x3,x3^-1 x1 x3,x3^-1 x2 x3,x5).
For u=zeta^i retain only q=u,0,u²,1, writing their physical
meridians as a,b,c,d respectively. The four literal old maps are

 i=1: (b,d,a,a^-1 c a,1,1),
 i=2: (b,d,1,a,1,c),
 i=3: (b,d,c,1,c^-1 a c,1),
 i=4: (b,d,1,1,c,a).

These are actual free-factor fillings of the common six-cut marking,
not an arbitrary relabeling of an abstract F4. The geometric forward
bridge carries reference meridians to the endpoint; therefore endpoint
physical meridians return to the B99 reference via the inverse push.
The independent checker verifies this direction and all substitutions.

The three nonconstant v paths are the straight chords from zeta² to
zeta, zeta³, zeta⁴ using the certified rational approximations. Their
distances from the complete critical set {0,1,-1} exceed1/100.
True cyclotomic endpoint displacement is smaller than10^-28, as
certified by the earlier exact radical bounds, so the same based
transport applies to the true configurations. The far q point remains
outside all moving punctures because the chords lie in |v|<=1 up to
the negligible endpoint deformation.

## The constant-v and constant-w kernels

The actual involution sigma(v,w)=(w,v), or sigma(v,q)=(q/v,q),
preserves both X and X0 and covers the identity on the q base.
It carries the entire constant-v=u section to the constant-w=u
section, with the identical based q loops. Thus their section
homomorphisms are intertwined by the induced pointed isomorphism
between the corresponding surface basepoints. Changing those
surface basepoints to the recorded common peripheral whiskers
introduces only an inner isomorphism. A zero kernel is unaffected
by that conjugation. Consequently the two complete section kernels
are equal as subsets of the same named old B6, and the B99
tubular-centralizer comparison identifies them with the two actual
zero-head kernels on K.

This does not assert literal equality of the two nonzero head words.
For each of the eight audited diagonal rows, beta(z)z=1. The existing
free-orbifold centralizer argument therefore identifies its K-row
stabilizer with precisely that zero-head kernel. Pulling back the
same complete B99 normal-closure kernel along the four displayed
based maps supplies all eight row-stabilizer descriptions.

## Limits

The conclusion concerns entire discrete row stabilizers, including
the full signed two-operator orbit in B99. It gives no full-column
monomial action, no block-intersection computation, no vanishing of
kappa, and no equality I=R. The exact retained row data do not
replace the nonabelian coefficient and transported-node calculations.

The small B99 true-root supplement was also inspected in full:
`work_CE/code/check_B99_deformation_margin.py` and genuine output.
Its exact radical enclosure, all17 segments/51 critical-distance
checks, and initial cut gaps greater than1/3 pass independently on
inspection. The genuine earlier coarse-bound failure is preserved.

## Auxiliary substitution presentation

The subsequent complete research Section6 and the small producer
`work_CE/code/diagonal_kernel_substitution_presentations.py` also pass.
An additional independent replay is saved as
`verify_diagonal_substitutions_independent.py/.out/.err` with
`diagonal_substitutions_independent_review.json`. It reconstructs all
six-generator forward/inverse arrays from the literal active/inactive
cuts, checks both inverse compositions, fixes the inactive meridians,
preserves old q-retained filling, and verifies every factor diagram.

The exact normal-closure formula follows without an extra topological
assumption. In the six-cut marking B6=V_i * F(inactive two cuts).
Extend each of the two transported V_i automorphisms by the identity
on those inactive cuts. The resulting auxiliary automorphisms Phi
intertwine Pi_i with the reference operators. The normal closure of
the inactive meridians and the full signed Phi-orbit of the displayed
relator therefore maps onto N and contains exactly its full preimage.
This gives both containments for the claimed stabilizer formula.

These are auxiliary automorphisms of the based free group B6, not
asserted geometric monodromies of the full deleted surface. Their
words have genuine full-column actions through the already certified
six old operators, but this normal-closure presentation supplies no
uniform description or monomiality of those actions.

## Formal B101 source review

The complete `work_CE/B101_all_diagonal_head_kernels_proposed.tex`
was read after these checks. Both literal filling tables, all four
bridge maps and inverses, physical/old basis distinction, all eight
row labels, both cone classes, all four relator preimages, and the
full auxiliary-substitution normal-closure argument agree with the
independent certificates. The formal proof passes without a required
mathematical correction. Its no-completion and no-full-column scope
is explicit and retained.
