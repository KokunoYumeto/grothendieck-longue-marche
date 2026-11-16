# Independent audit of the uniform coefficient-three obstruction

Date:2026-11-16. Inspected proof: `work/a_main_uniform_cubic_three.md`. Verdict: **passes**, including rational twists with dyadic ramification and baseline zero in the stated pure coefficient-three case. No A-owned manuscript was edited.

## Statement and global-to-local scope

The assertion concerns a rational-origin cubic `X^3+Y^3=dZ^3`, an infinite-order rational point R, and an exponent equal to an integer n at every coefficient prime other than three. It excludes every nonzero alteration at three in the actual joint compact/j-line quotient. The combination with A.68 addresses all finite alterations of a nonzero integer. It does not assert the unrestricted full section conjecture or the finite-support baseline-zero statement at every other coefficient prime on every twist.

The quadratic flex-ratio character is defined over the full three-torsion field and factors through the stated quotient by A.67. Over that field, both the proper three-torsion tower and the R-division tower are pro-three. Thus a nontrivial quadratic difference character cannot be hidden in either tower. The prescribed-primary Chebotarev step of A.68 applies to a preimage T of any prescribed S under a nonzero three-adic scalar. The necessary squareclass condition therefore holds at every three-primary translate, in a sufficiently deep finite torsion field. The proof never substitutes a compact Kummer label for a full punctured-curve section.

## Exact dyadic field bridge

The scaling `(X,Y,Z) -> (tX,tY,Z)`, where `t^3=9/d`, preserves O and `J=X^3/(dZ^3)`. It therefore takes the prescribed cusp block and its normalized flex-ratio function to the one used in A.69. Every dyadic unit has a unique cube root by Hensel's lemma. Consequently the scaling is defined over Q2 or a totally ramified cubic extension; adjoining ζ first gives the cyclic extension F/K2 of degree one or three, with K2=Q2(ζ) unramified quadratic.

There is an explicit independent verification that this is exactly the local three-torsion field. For

\[
E_0:y^2+y=x^3-1
\]

the three-division polynomial is `3x(x^3−3)`. At x=0 the y-coordinates are ζ,ζ², and at x=bζ^i, b³=3, they are 1,−2. The odd dyadic root b belongs to Q2. All nine points are consequently defined over K2. The CM automorphism `(x,y)->(ζx,y)` acts faithfully on this set. If the cubic untwist is nontrivial, its descent action cannot disappear on E[3], so F is precisely the local field of all three-torsion. Good reduction then puts every higher odd-torsion extension inside F times an unramified extension of K2.

This is the necessary bridge from the global squareclass condition to the actual dyadic fields used in the norm argument. It does not incorrectly assume that a ramified twist itself has good reduction over K2.

## Reduction subtraction and the formal parameter

In the unramified case the point is Q2-rational and reduces to one of the three points of E0(F2). Its unique prime-to-two torsion lift is rational. In the ramified cubic case inertia acts trivially on the residue field, while the descended point satisfies `τB'=[ζ]^kB'`. Its reduction therefore lies in the order-three fixed subgroup of CM, and its unique three-torsion lift B0 is fixed both by τ and by CM.

Subtracting B0 is legitimate in the global necessary condition: under the fixed algebraic embedding every such local B0 is the image of an actual global three-torsion point, and division of the conditions at `S−B0` and `−B0` gives the required ratio based at Bf. For a nonzero integer multiple of an infinite-order R, Bf cannot be the origin. Nor can it be nonzero odd torsion, since it belongs to the dyadic formal group.

The parameter `z=−x/y` satisfies `z([ζ]Q)=ζz(Q)` exactly. In the cubic ramified case, `z(Bf)^3` is fixed by τ and lies in K2. With normalized integer valuation h=vF(z(Bf)), one has

\[
v_2(z(B_f)^3)=h,
\]

because vF(2)=3. Thus an even positive height gives divisibility by four after taking the cube. This accounts correctly for the ramification index.

## Odd-height obstruction

The pole d0 of g0 is `(b,1)`. Modulo two its denominator is x+y, and substitution into the reduced curve gives `(x+1)^3`. Its numerator at d0 is `3(ζ²−1)`, a dyadic unit. The translated formal expansion therefore has a threefold pole with unit leading coefficient. At odd height h the quotient has valuation −3h, which is odd and remains odd in every unramified extension of F. It is not a square.

## Even-height obstruction and norm

In the unramified case Bf is the origin modulo four, so every ordinary translated ratio is congruent to g0(T) modulo four. For a square unit u² in an unramified dyadic field, `σ4(u²)≡u^8 mod4`. Frobenius four acts on odd torsion by [−2], since E0(F2) has order three. This yields the A.69 congruence `g0([−2]T)≡g0(T)^4 mod4`.

In the ramified case, for T of order dividing nine but not three, the translated function `g0(T+Q(z))` is an integral power series and a unit. Multiplication over z,ζz,ζ²z is invariant, hence is an integral power series in z³ with constant term g0(T)³. The preceding exact valuation gives its congruence modulo four. The denominator norm is literally one, because the three CM transforms of the flex-line ratio telescope. The norm of the square ratio is therefore a square unit in an unramified field, congruent to g0(T)³ modulo four.

Applying Frobenius yields a difference of cubes. Its cofactor is a unit: the two inputs agree modulo two, are nonzero there, and three is a unit. Thus the same A.69 congruence follows without dividing by three or by a ramified uniformizer.

## Exact finite contradiction

The independent replay `work/c_A70_A69_replay.out` executes the existing exact SymPy certificate. The reduced half-numerator of `g0([−2]Q)−g0(Q)^4` is nonzero and has unique highest-pole monomial `ζ x^10 y`, of pole order23. Its denominator is `(x+y)^8` modulo two and vanishes only at an order-three cusp. None of the72 points of E[9]−E[3] lies there, and neither does its [−2] image. Odd-torsion reduction is injective. Consequently those72 distinct points cannot all be zeros of this polynomial function of pole degree23.

This verifies the exact obstruction needed in both even-height cases, including Bf=O. No new analytic rank calculation, unproved torsion-field comparison, or numerical approximation enters the uniform argument.
