# Candidate: all intermediate covers of the exponent-p Heisenberg cover

Unregistered; no claim is promoted before full written proof and independent audits. This is separate from A64's torsion enlargement.

## Exact proposed scope

For every odd p, let C_p be the actual A61/A62 cover, G=H_p, Z=centre, q:C_p→E and f=[p]q. Every intermediate affine cover of f should have both all-prime assertions of TaskA5. The only new subgroup case is S≤H_p noncentral of order p. Its compactification D=C_p/S has genus 1+p(p−1)/2, p cusps and degree p² over U. Normalizers already follow from A59; the new claim is fixed inertia.

Every finite two-generated group of exponent p and nilpotency class at most two is a quotient of H_p. If it is nonabelian it is H_p itself. Its characteristic geometric cover is unique: the quotient of the free rank-two profinite group by pth powers and third commutators has order p³ and is H_p. Thus, if the proposed intermediate statement passes, it settles the original fixed-group question on every finite cover whose geometric Galois closure has exponent p and class at most two, after the usual finite arithmetic descent. No cofinality follows.

## Subgroup classification and actual square

If S contains Z, the quotient proper curve is an isogeny quotient of E and A40 applies. If S∩Z=1, its image in G/Z=F_p² is isotropic for the nondegenerate commutator form. Thus S is trivial or has order p. Noncentral S acts freely on the entire generic proper C_p because every generic stabilizer for G is trivial or Z. Therefore C_p→D is unramified degree p, giving the genus formula. The p² original cusps split into free S-orbits of size p, leaving p cusps.

Let T=S̄≤E[p], φ:E→A=E/T, and φ̂:A→E. The equivariance of q under actual deck translations gives q_D:D→A with q_D f_S=φq and degree p. The map to U is φ̂q_D, because φ̂φ=[p]. Its cusp set is the entire inverse image of ker φ̂, and q_D is totally ramified over each of the p points in ker φ̂. All objects become actual over a finite number field.

## Ordinary p: a place where T is étale

For p=1 mod4, write (p)=π·barπ in Z[i]. The two geometric CM lines E[π] and E[barπ] are the respective connected kernels at the two split residue places. T cannot equal both, so choose a place where T meets the connected kernel trivially. Its nonzero points then specialize injectively to the étale subgroup of E[p].

On the actual A62 model, every nonidentity s∈S changes the target point by a nonzero reduced translation. Consequently it fixes no special point or component point; the generic action is also free. The finite constant-group quotient is an étale S-torsor, so it preserves semistability. The p rational marked clusters of A62 lie above the p distinct reduced E[p] points, each contains p marks, and S permutes them freely. A rational companion path inside one cluster maps isomorphically to its quotient copy, and its two marks are not S-equivalent. A42 gives all-prime fixed inertia for every selected cusp.

## Inert p: domination of positive components

At p=3 mod4, both E and A have good supersingular reduction after finite extension. The special φ has degree p and is purely inseparable. Every cusp of D maps to ker φ̂ and specializes to O in A.

J_D is an isogeny factor of J_C: f_{S,*}f_S^*=[p]. Since J_C has potential good reduction by A61, so does J_D (an auxiliary-prime Tate representation is an unramified direct summand). Thus the semistable dual graph of D is a tree.

Use regular semistable models and extend q_D to the good A. A direct extension proof suffices: Liu9.2.7 resolves the rational map by finitely many point blowups; each exceptional P1 maps constantly to the elliptic special fibre. Descend one blowup at a time. The image of the graph is proper and quasi-finite over the normal original surface, hence finite birational and an isomorphism. This proves descent without assuming a Néron mapping property for a nonsmooth source.

Likewise resolve the actual morphism C_p→D by point blowups of the regular source. **Fresh primary:** Liu, Algebraic Geometry and Arithmetic Curves, Theorem9.2.7, printed396–397, PDF412–413, https://rexresearch1.com/GeometryLibrary/AlgebraicGeometryArithmeticCurvesLiu.pdf , opened in `turn1007view0/1`. The added components are rational. The resulting proper map is surjective because its image is closed and contains the entire generic fibre. Every positive-genus component of D is therefore dominated by one of the original positive-genus components of C_p; a rational component cannot dominate a positive-genus smooth projective normalization (Lüroth).

A61 has one elliptic main component, radicial of degree p over E, and all other positive-genus components map constantly to finite critical centres different from O. After φ, those centres remain distinct from O because φ is radicial on the supersingular special fibre. The composite on the source main is radicial, hence its nonconstant factor through D is also radicial. Only that one source component can dominate a component with nonconstant map to A. Thus D has exactly one such main component, with exactly one point above O, and every other positive-genus component maps constantly away from O.

All marked points of D lie over O after specialization. A rational component carrying one has constant map O. Its path to the main cannot pass through a positive-genus component with a different constant image. All such rational branches attach at the unique main point over O; nodalness gives at most one attaching branch, so the O-fibre has one connected rational subtree. If it is absent before marking, separation of the p≥3 cusps inserts a rational tree at that smooth main point. If present, marked sections cannot stay on its main attaching node. Every cusp therefore has a distinct rational companion, giving A42 at every coefficient prime.

## Remaining audit gates

- Explicit source for good reduction of an abelian isogeny factor (existing Serre–Tate/NOS dependency), and compact type from potential good Jacobian.
- Check the model-resolution and graph-image descent proof carefully, especially that exceptional components are only P1 and that proper surjectivity covers every special component.
- Verify ordinary connected-line orientation at the two Gaussian places and the free constant-group quotient even though its order equals the residue characteristic.
- Execute an exact finite Heisenberg subgroup/cusp-orbit certificate before drafting a registered statement.

The separate prime-to-p isogeny pullback C_p×_{E,[n]}E is also promising. Its actual deck group is H_p×E[n], its proper genus is 1+n²p²(p−1)/2, and the étale base change of A61/A62 has one main and n² copies of each attached branch. Rational marked paths lift through the disjoint copies. This has not yet been merged into the candidate scope.
