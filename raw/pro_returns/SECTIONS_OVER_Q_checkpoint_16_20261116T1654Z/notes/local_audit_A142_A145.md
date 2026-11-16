# Independent audit: A142–A145

Auditor: /root/local_preprint. Workspace:
/workspace/scratch/0e9bfd5def12. Audit date: 16 November 2026.

## A142 — restricted-product reciprocity obstruction

Source: work/sections/tripod_reciprocity_obstruction.tex.
Certificate: work/code/tripod_reciprocity_obstruction_certificate.py,
with retained _output.txt and tripod_reciprocity_obstruction_data.json.
The parent and /root/legendre_main independently read the complete proof;
Legendre reran the complete certificate successfully.

The construction retains the A134 local centres at all 611 recorded
primes and changes the centre at the additional prime 4679 to
T=(1-c)+4679, where c=-338/191. The three literal residue roots
2304, 2961, 4466, their nonzero derivatives, the nonsquare class of the
quadratic character, and the valuation-one zero of f(T)-f(c) were
checked. At the retained centres, the identity
f(T)-f(c)=-4(T-c)(T-(1-c)) gives invariant zero, including the
cancellations at 2, 7 and 139. The modified induction excludes both
fibres T=c and T=1-c; its boundary count is at most 6D, and the
same explicit Weil bound remains positive.

The actual refinement maps are X_i=uY_i^m, with coefficient
a_i'=a_i u^{n_i} and new exponent mn_i. They retain every controlled
T_p exactly. At new coefficient primes both omitted differences are
units; outside the controlled set the chosen good points also make
them units. Thus the final tuple x_p-f(c) is in every finite
restricted product and its quadratic invariant sum is exactly 1/2.
This is an ordinary completed tripod pair with no completed new
coordinate at these same local centres. The executed certificate
checks the displayed finite arithmetic and 216 genus/boundary bounds;
the proof supplies the infinite recursion.

The reported display typos in A142.2, A142.15 and A142.16 have been
corrected. No remaining mathematical correction was found.

## A143 — rank-two elliptic quotient and finite-primary exclusion

Source: work/sections/harmonic_elliptic_positive_rank.tex.
Certificate: work/code/harmonic_elliptic_rank_certificate.py,
retained _output.txt and harmonic_elliptic_rank_data.json.
The certificate was independently rerun successfully.

The exact maps D -> E -> F, their degrees, the order-four deck
automorphism, both dual two-isogenies and both duplication composites
were checked. The four boundary points exhaust the two displayed
elliptic boundary fibres, each with ramification index two.
Both descent kernels were checked, including the points with zero
x-coordinate. The sixteen E-squareclasses and the three excluded
F-quartics prove that phi:E(Q)->F(Q) is onto and the rank is exactly
two. The classes of the two explicit points are independent modulo
the complete torsion contribution.

For the analytic claim, the original primary scan was independently
downloaded to work/sources/tunnell1983_independent_audit.pdf.
Printed pages 326, 328 and 329 were rendered and visually read.
The signed theta formula and
L(E,1)=b(573)^2 beta/(2 sqrt(1146)) agree exactly with Tunnell's
Theorems 1 and 3. The integer enumeration gives sixteen positive and
sixteen negative terms; the two ternary counts and the independent
eta-product coefficient agree.

For the lifting exclusion, the actual surjection on Mordell–Weil
completions, the finite-primary idempotent and localization maps were
checked. At the specified good primes, the two-primary part of
E(Q_p) is exactly E[2], and every supported odd-primary component
vanishes. The proper elliptic image is therefore one of the two
boundary images. The actual finite etale cover D° -> U transfers a
Selmer lift to a positive-density cuspidal set. AP-D25 was reread in
its Selmer range. Its density-one ordinary-integrality conclusion
then forces a global cusp, whose actual inverse-cover decomposition
group gives one of the rational boundary points of D. The elliptic
image is torsion, contradicting the stipulated non-torsion completed
class. The argument includes coefficient prime 2.

Execution totals include 36,480 primitive residue pairs for the
191-adic quartic exclusion and 1,988 elliptic points at fifteen
good primes for the full two-primary comparison. Full audit: PASS.

## A144 — successful radicand update

Source: work/sections/successful_radicand_update_agent.tex.
Certificate: work/code/successful_radicand_update_certificate.py
and retained _output.txt. The complete source was read and the
certificate independently rerun successfully.

The norm identities for gamma=-68+64 alpha+alpha^2, q=511177,
z=alpha q^8, and beta=(1-alpha)(alpha^2-2)q/gamma^3
were checked literally. The three q-branches, the unique zero of
gamma, all unit cube characters and the stable tame norm equations
were checked. In particular
beta*z=(1-alpha)(3-2alpha)*(q^3/gamma)^3
gives the exact local norm comparison.

At 2 the degree-one factor carries the nonunit target; all remaining
unit factors use unramified unit norms. At 3 the A140 actual pure
tower norm maps apply. The relative Galois closure has the full
holomorph as its decomposition group at 3. The character-lattice
localization square and the inflation argument therefore establish
the Hasse norm principle at every finite depth. The source claims
global norms at every finite level and explicitly retains the
remaining global inverse-compatibility question. Full audit: PASS.

## A145 — full source, construction, and uniform local detector

Source: work/sections/uniform_harmonic_detector_family.tex.
The complete saved source was read and passed the independent audit.
The strengthened work/code/uniform_harmonic_family_certificate.py
was independently rerun successfully. It checks all five literal
Hensel lifts modulo q squared, both extra-unit conditions, the exact
valuation gap, and the initial coefficient product. The two missing
backslashes before quad in A145.17 were reported to the parent.

The first binary node is retained in
work/notes/uniform_detector_branch_witness.json.
An independent certificate was executed successfully:
work/code/uniform_detector_branch_independent_audit.py and
work/code/uniform_detector_branch_independent_audit_output.txt.
It checks primality of 1065217, the strict initial bound, both
literal root tuples, and splitting of all five quadratic boundary
characters.

For the valuation-one branch, the controlled centre is
T=a_0 q^{n_0} with old root X_0=q.
The ordinary valuation factor in the refinement multiplier contains
q^1; all auxiliary stabilizer primes avoid the controlled set.
Thus v_q(u)=1 exactly. Approximating u/X_0 sufficiently closely
to 1 gives the actual new root in X_0=uY_0^h and retains T.
The final old coefficient has q-valuation n_0. The other two
coefficients and all later controlled multipliers are q-units.
The unit branch instead has q-valuation zero. Hence the first
differing binary node distinguishes the final pushed pair.
Retaining the original fresh-support steps ensures infinite support
also along the all-zero path.

The uniform detector's cuspidal comparison is literal. Let
barK_D be the proper mod-two homology kernel of A141.
It is contained in the actual degree-eight cover subgroup H_D.
A local full cusp representative whose finite image lies in
E_D/barK_D therefore has its full image in E_D, after lifting
the finite conjugator. Its fixed sheet gives a Galois-stable inertia
orbit, hence a rational boundary point of proper D. The intersection
with the base cusp decomposition group is the actual decomposition
group of that point. Compactification kills its inertia, so the
proper mu-two class evaluates as the proper Brauer value there.

Outside S={2,3,7,13,17,23,139,191,1119169},
the three finite boundary values have first entries
338/191, 529/191, 867/382, all units. The character d is
unramified there. At infinity take w=W/T; the function
(T-c)w^4 has residue a^{-1}, also a unit. Hence every boundary
value is zero outside S. The A139 ordinary-point calculation gives
zero at every ordinary D-point outside S as well. At the real place
d is positive, so its character is trivial. Thus the uniform
outside-S ordinary-or-cuspidal condition has no unresolved sheet,
orbit, or descent step.

The full saved proof also checks the common prime at each pair of
children, all cofinal scheduling, the signed first refinement and
the later principal-root maps, both omitted fibres, and the
preservation of the entire A142 invariant table. Full audit: PASS.
The binary map is continuous: for every fixed finite exponent, a
sufficiently long common prefix gives identical coefficient classes,
because the common exponents 4m! are cofinal. Thus the injection also
identifies a compact Cantor subset of the Hausdorff completed-pair
space. This strengthening was sent to the parent separately.
