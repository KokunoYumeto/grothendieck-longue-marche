# Literal based reflection on the actual annular first-neck subgroup

DE, checkpoint23. Complete actual marking calculation; no full-group centralizer consequence is inferred.

## 1. Selected gauge and the short parameter region

Use the selected UPPER collar connector from the actual far section to y=-1. The principal square-root lift ends at z=+i, t=-i. The original ordinary cut meridians

  O=(O1,O2,O3,O4,O5)=(x1,x3,x4,x5,x6)

are transported together with their one upper-half-plane entry and this connector. The positive neck cone is x1 x2 x1^{-1}=a C a^{-1}. The lower connector, whose lift ends t=+i, is a different gauge and is not substituted.

The original neck q*=exp(i pi/5) can be compared to the rational first-arc point q_e=(4+3i)/5. Use the vertical segment q_b=4/5+i/2 to q_e, and then the short unit arc back to q*. In Q=(1+q)/(1-q) coordinates, both this path and the original radial/short-arc path lie in Re Q>=0, Im Q>=3, within a common regular neighborhood. They are homotopic relative endpoints there.

This short region is regular for the actual marked system. For u_j=exp(2pi i j/5), A_j=(1-cos(theta_j))Q-i sin(theta_j) has Im A_j>1. The least lower bound is 3(1-cos(2pi/5))-sin(2pi/5)>1; squaring its positive sides reduces the inequality to39>17sqrt5. Since Re A_j>=0, h_j=(A_j-1)/(A_j+1) is in the first quadrant. The selected branch square root is also in that quadrant. Consequently all five y-punctures remain in the upper half-plane. The same-sign coincidences and branch contacts on the unit circle occur only at the old fifth-root values, outside this short arc. Opposite-sign coincidences cannot occur while the h_j lie in the first quadrant.

This upper-y assertion is NOT made over the whole first unit-circle arc. In particular q=(3+4i)/5 would cross the fixed y=-1 gap and is not used for this calibration.

## 2. Exact bridge from the original marking

The independent producer check_annular_neck_bridge23.py uses exact-unit rational approximations to the four fifth roots and the literal vertical segment q=4/5+i(1/2+s/10), 0<=s<=1. It checks all fifteen pair separations by exact rational-polynomial positivity, uniformly greater than1/1000, and both endpoint projection gaps greater than1/1000. Projection-root isolation finds exactly one crossing: the cone and h4² pair, with h4² passing above the cone. The chronological braid is therefore positive sigma2.

The initial full physical order is (h1²,cone0,h4²,h2²,h3²,q); the endpoint order is (h1²,h4²,cone0,h2²,h3²,q). Under the calibrated geometric push,

  x2 -> x2 x3 x2^{-1},     x3 -> x2,

and the other four generators are fixed. All twelve inverse compositions are checked. Thus the ENTIRE original ordinary basis O maps literally to endpoint cuts(1,2,4,5,6), with no remaining conjugator. This is stronger than a matching peripheral-label list.

## 3. An actual Cayley basis, read in those endpoint cuts

At q_e every selected y-puncture lies on the upper unit circle. Set

  xi=i(y+1)/(y-1),       y=(xi+i)/(xi-i).

The selected gap y=-1 maps to xi=0, and J(y)=1/conj(y) becomes xi->conj(xi). The upper y half-plane maps to the right xi half-plane. The five punctures have positive real xi coordinates in physical order(h1²,h4²,h2²,h3²,q).

Choose the standard positive upper-comb meridians at xi=0, entering the open right half-plane before rising above the real interval. The entry avoids the inverse Cayley pole xi=i. Read their exact Möbius images against the endpoint downward cuts, using the selected upper connector from the original far base to y=-1. Every quadratic real-cut root, height sign, endpoint, tangency and denominator minimum is checked. The result is literally

  (xi-meridian1,...,xi-meridian5) = endpoint cuts(1,2,4,5,6).

Both directions of all five free-basis substitutions are independently checked. Thus this is the actual transported O basis, not an unspecified basis in the same free group. The upper connector's endpoint cut word is(1), and is retained in every full path; the literal equality above includes its cancellation with the Möbius path words.

The auxiliary unbounded connector is interpreted through the existing radial plane-to-disk homeomorphism. It fixes the finite punctures and compresses the exterior inside retained y=1. Its image is the selected upper collar. Hence this cut comparison agrees with the whole-neck marking rather than inadvertently circling the retained boundary point.

## 4. Literal reflection words

Let P0=1 and Pj=O1...Oj. In the xi comb, reflection changes the upper whisker to the lower one. Reading that reflected path against downward cuts crosses exactly the preceding j-1 rays positively, followed by the negative local meridian, and then the reverse prefix. Therefore the actual based involution is

  eta(Oj)=P_(j-1) Oj^{-1} P_(j-1)^{-1},       1<=j<=5.       (1)

The independent polygon calibration verifies all five formulas. Both eta²=1 and eta(O1...O5)=(O1...O5)^{-1} are literal free-word identities. Since the complete bridge and Cayley basis have already been identified, (1) has no unaccounted common conjugator.

For the q0-adapted common basis (a,bar b,d,e,f), use the exact Nielsen table

  O1=a bar b a^{-1}, O2=a, O3=f d e d^{-1} f^{-1},
  O4=d, O5=d^{-1} f d.

Both inverse substitutions and all five eta² identities are checked again after this change. In particular the requested outer cone conjugator is

  eta^{-1}(a)=eta(a)=a bar b a^{-1} bar b^{-1} a^{-1}.        (2)

All five expanded adapted words are in annular_neck_reflection23.json. Equation(2) is a literal word; it is not replaced by its abelianization, and no claim is made that it belongs to a subgroup centralized by the inner annular section.

## 5. Transfer from the rational coefficients to the true roots

The coefficients are rational points ON the unit circle, obtained by the rational half-angle parametrization from the already certified30-digit fifth-root coordinates. Independent exact radical intervals show Euclidean error<1e-29. On the entire coefficient homotopy and q segment, |q|<=1, the h denominator exceeds4/5, and its numerator and both u-derivatives are bounded by5. The derivative of h² is consequently<600, so every configuration point moves by<1e-26.

The exact bridge separations and endpoint gaps exceed1/1000. They therefore persist, and the actual braid/cut marking is unchanged. At the endpoint use the short unit-circle coefficient homotopy, so the fixed-circle/Cayley structure is retained. The Cayley puncture order, positive comb and inverse images vary without a puncture crossing; this transfers the exact basis words to the true fifth roots. The short actual unit arc q_e to exp(i pi/5) lies in the same upper-half-plane marking region, so it introduces no additional based change.

## 6. Exact records and scope

* check_annular_neck_reflection23.py/.out/.err and annular_neck_reflection23.json: all Möbius cut paths, exact root/height records, endpoint basis identities, reflection words and adapted substitutions.
* check_annular_neck_bridge23.py/.out/.err and annular_neck_bridge23.json: all15 separation polynomials, the single chronological crossing, full push/back dictionaries and the original physical marking.
* check_annular_neck_deformation23.py/.out/.err and annular_neck_reflection_deformation23.json: exact true-root radical intervals, error bounds and input hashes.
* check_annular_gap_and_reflection23.py/.out/.err: separate cut replay and generic disk-reflection calibration. Its original right-base calibration is not substituted for the actual left-base Cayley calculation; both are separately marked.

The independent CE compiler compile_annular_neck_presentation23.py also replays all five ACTUAL left-base xi polygons under reflection and obtains the same five words, then checks the complete adapted substitutions. This supplements the separate generic reflection calibration.

The result completes the finite actual eta input for the one-neck presentation. It does not prove a centralizer formula after the two cross commutators, source injectivity in that quotient, or any global fixed-source equality.
