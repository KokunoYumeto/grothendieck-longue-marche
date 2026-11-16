# A.71: uniform completion for every finite alteration on every rational-origin cubic twist

The exact theorem is the statement of A.69 with E9 replaced by any E_d:X³+Y³=dZ³ having its rational infinity origin and a stipulated nontorsion R∈E_d(Q). For every integer n and every exponent a equal to n outside a finite coefficient-prime set, Γ3 Selmer lifting is possible exactly when a=n. A.70 handles all nonzero baselines, so only finite support around0 remains.

Use the short Weierstrass model

 E_d:Y²=X³−432d²,     a0³=d,     K=Q(ζ),     L=K(a0)=Q(E_d[3]).

The J1 flexes are (12a0²ζ^i,36d), and their tangent-line ratio normalized atO is

 g_d=(6a0ζ²X−Y−36d)/(6a0X−Y−36d).

The tangent-line identity proves its divisor3(d1)−3(d0), and it is the retained Γ3 character of A.67. All of A.69's common joint-tower argument applies to E_d,R and this character: choose a finite abelian base F0/K, place L in the proper joint torsion/R-division tower, and exhibit a torsion value h∈F0 whose quadratic radical is not Galois overK. Odd translation kernels automatically kill quadratic characters; if2 occurs, a surviving residualC3 kills the2-translation kernel by Cayley–Hamilton. Zero-primary Chebotarev places the global character's radical in the tower, and a prescribed-primary target contradicts the noncontainment of sqrt(h). This argument requires no special equation beyond CM and the explicit retained character.

## Support containing2

Let c³=2 and F0=K(c). The point S2=(6ca0²,0) is nonzero2-torsion and

               g_d(S2)=(ζ²c−1)/(c−1)=h.

This is exactly the A.69 nonsquare at31, with cubic conjugate product1 and non-Galois radical overK. Also F0(E_d[2])=F0(a0)=F0L, because adjoining the2-torsion x-coordinate gives a0² and hence a0.

The residual2-torsion image overF0 isC3 unless a0∈F0. This exception says that the rational cube class ofd is one of1,2,4. Indeed Kummer theory overK identifies the cyclic cubic subfields, and a rational number that becomes a cube in the quadratic extensionK/Q was already a rational cube. The three exceptional twists have rank0, by the executed and rigorously certified A.38 rows:

 d=1: conductor27, central interval [0.588879583428483319104563 +/-2.77e-25];
 d=2: conductor36, central interval [0.701091052662727130587510 +/-5.35e-25];
 d=4: conductor108, central interval [1.1129126745223053845620 +/-3.84e-23].

These nonzero values and the CM theorem cited in A.37 give Mordell–Weil rank0, so they cannot occur under the hypothesis thatR is nontorsion. Thus the residualC3 always survives in the case at hand, and the common tower argument excludes every finite support containing2.

## Odd support containing p≥5

Use the fixed E9 witness from A.69. Let b³=3,

 M0=K(b)(E9[p]),     h=g0(S_p),     S_p∈E9[p].

A.69 proves that h is nonsquare inM0 and that its three conjugates under the automorphismτ fixing E9[p] and cyclingb have product1. Now let

                      F0=M0K(a0).

The fieldF0 is abelian overK, and [F0:M0] is1 or3. Therefore h remains nonsquare inF0. Any liftσ ofτ toGal(F0/K) satisfies hσhσ²h=1, because h∈M0. The lift need NOT have order3; only its restriction does. IfF0(sqrt(h))/K were Galois, the squareclass ofh would beσ-invariant and the product identity would imply thath is square, contradiction. Thus the non-Galois-radical property persists without any disjointness assumption onK(a0) andM0.

The elementt=b²/a0 lies inF0 and has t³=9/d. The Weierstrass scaling (X,Y)↦(t²X,t³Y) identifiesE_d withE9's short model and takesg_d to the normalizedg0 (after the known integral minimal-model change forE9). Therefore S_d=t^(-1)S_p is a p-torsion point onE_d defined overF0 and satisfiesg_d(S_d)=h. Its orderp>=5 makes it interior. The baseF0 already containsL. Since2 is absent, every translation kernel is pro-odd, so no residual2 condition is needed. The common tower argument now excludes every such finite support.

## Remaining support and conclusion

If the nonempty support contains neither2 nor a prime>=5, it equals{3}, which is excluded uniformly by A.70. Zero is realized by the O-cusp, and each nonzero ordinary integer by its actual rational point. Hence all finite alterations of all integers are classified uniformly on every rational-origin cubic twist with a nontorsion rational point.

The symbolic transport, two-torsion evaluation and tangent-line identities are independently checked in a_main_twist_transport.py. The rank-zero rows are selections from the existing certified census, not new heuristic rank evaluations. Infinite alterations, the finite quotient's fibres, and cubic torsors without a rational origin remain outside this theorem.
