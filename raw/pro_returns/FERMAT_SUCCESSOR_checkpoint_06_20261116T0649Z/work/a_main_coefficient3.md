# New A.68 work proof: finite alterations at the actual X3 quotient

This note strengthens A.67. It has two independent mechanisms. The norm/ramification proof settles any finite alteration of a nonzero integer that changes a coefficient prime other than3. The local3 translation identity plus prescribed-primary Chebotarev settles pure coefficient3 alterations, including baseline0 using an explicit9-torsion witness. It does not claim a result for arbitrary finite support around0 at other primes.

## Proposed exact theorem and scope

Let E/Q be an elliptic cubic twist as in A.67 (rational infinity flex O, full3-torsion boundary) and R in E(Q) nontorsion. Let Gamma3 be the actual joint compact plus finite j-line X3 quotient of A.67.

1. If a equals a nonzero integer n outside a finite set of coefficient primes, and some changed component has coefficient p!=3, then a has no Gamma3 Selmer lift.
2. On E9:y²+y=x³-1, P=(1,0), if a equals ANY integer n outside coefficient3, then a has a Gamma3 Selmer lift if and only if a=n.
3. Consequently on the least curve the complete Gamma3 lifting exponent set among all finite alterations of nonzero integers is exactly the nonzero integers. Every actual integer is realized by its point section; baseline0,a0 is realized by the O-cusp packet image. No complete fibre classification at the finite quotient is claimed.

The first assertion uses only CM Kummer openness A.61, not finite-Sha or analytic rank; all cubic Jacobian twists are CM over a finite extension. The rational-origin condition remains as in A.67.

## A prescribed-primary Frobenius lemma

Let F contain the CM field, let P be a finite set of coefficient primes, and choose a finite extension making all required torsion targets T_p rational. A.61 says the joint Kummer image H of R is open in the product over p in P of TpE semidirect Gp. Thus it contains a product neighbourhood of the identity consisting of translation lattices p^{m_p}TpE times open torsion-image subgroups Gp,1.

For a chosen p-primary torsion point T_p, lift it to tau_p in VpE. Choose A_p in Gp,1 sufficiently close toI, with A_p-I invertible, so c_p=(A_p-I)tau_p belongs to p^{m_p}TpE. Such A_p exist arbitrarily closeI: take sufficiently high p-powers of a good Frobenius after its prime-to-p finite part has been killed. Its eigenvalues have nonzero Weil weight, hence no positive power has eigenvalue1. If the target is zero take tau_p=0. The tuple(A_p,c_p) lies in H.

The condition c_p-(A_p-I)tau_p in (A_p-I)TpE is open near this tuple. Indeed after fixing the denominator valuation of (A_p-I)^(-1), the image lattice is constant on a sufficiently small neighbourhood. It is exactly equality of the unramified local Kummer classes of R and T_p. At good places of residue characteristic outside P, local Kummer injectivity says the actual p-primary component of R is T_p. Since the targets are rational over F, the condition is conjugacy invariant; translation conjugation alters c_p only by (A_p-I)TpE. This gives one nonempty open Frobenius condition prescribing all the primary targets simultaneously. Reapply the lemma after each finite field extension used below; do not reuse a condition over an incompatible base field.

## The finite alteration at a prime p!=3: containment, ramification, norms

Let a_q=n outside a finite set P and put delta_p=a_p-n. Choose p in P, p!=3, with delta_p!=0. Choose one of the X3 flex-ratio units g over L=Q(E[3]), with divisor3(d1-d0), where d0,d1 lie in the J1 block. By A.67's direct kernel argument kappa2(g) factors through Gamma3 over L. A hypothetical Selmer section therefore supplies a global class beta in H1(L,mu2) whose local value is g(Q_v) at every interior forced centre Q_v=aR.

Fix ONCE a finite extension F/L containing the CM endomorphisms, all E[l] for l in P, and a square root of a representative of beta. Over F this global class is zero. Let K_infty/F be the full joint torsion and R-division tower for l in P. It is Galois. There is a single finite S of primes of F, containing2,P,bad reduction and the fixed field's ramification, outside which the entire tower is unramified. The reason is structural: at a good place of residue characteristic not in P, E extends to an abelian scheme and every multiplication-by-l^r map is finite etale; the fibres above the integral section R are finite etale as well. Properness ensures that R is an integral section at every such place.

For ANY p-primary torsion point T, choose a p-primary T' satisfying delta_p*T'=T. This is possible because delta_p is a nonzero element of Zp: divide by its p-power valuation and invert its unit part. Take a finite torsion field F_r contained in K_infty that defines T,T'. Consider h_T=g(nR+T), an ordinary nonzero algebraic value because nR is nontorsion and the divisor of g is torsion.

CLAIM: sqrt(h_T) belongs to K_infty. If the quadratic extension F_r(sqrt(h_T)) is not contained in K_infty, its intersection with the Galois tower is exactly F_r. Chebotarev can then impose both a nonsquare Frobenius in this quadratic extension and the open condition in the preceding lemma with R_p=T' and every other altered R_l=0. At such a good place the actual compact centre is

 aR=nR+sum_{l inP}delta_l R_l=nR+T.

It is interior, so beta=0 makes g(nR+T) a local square. This contradicts the nontrivial quadratic Frobenius. The claim follows. It also covers the case where h_T was already a square in F_r.

Thus the quadratic extension defined by h_T is unramified outside the same S, for every T. At places outside S (in particular outside2), the valuation of h_T is even. This holds in any finite torsion field defining T: the larger fields used to define T' are themselves unramified outside S, so their ramification indices there are1. Evenness descends. Residue degrees can be even when p2 and cause no problem.

Set m=p². Then m=1 mod3, so [m] fixes d0,d1. The norm of g along [m] has divisor equal to that of g, hence

 Norm_[m](g)=C*g, C in F^times.

Iteration gives C_j=C^(1+m²+...+m^(2j-2)), and the exact fibre norm identity is

 product_{T in E[m^j]} g(nR+T) = C_j*g([m^j]nR).

Enlarge S by the support of C. In a finite torsion field containing E[m^j], every factor on the left has even valuation outside S. Thus g([m^j]nR) does also. This value lies in F, and the torsion field is unramified outside S, so the same parity holds in F. Hence the infinitely many distinct rational points [m^j]nR lift to the finitely many twists z²=c^(-1)g with c in F(S,2). Their compactifications have genus2. Faltings is a contradiction.

This proof includes p2. It never assumes that a quadratic extension is disjoint from a pro2 tower when it is contained; containment is precisely the case where uniform ramification supplies the needed information. It also handles simultaneous finite coefficient changes because the prescribed-primary condition set all other altered primary components to zero.

## Pure coefficient3 changes: forcing, then a target torsion translation

Let a_q=n for q!=3 and a3=alpha. Over L=Q(E[3]) the complete proper3-torsion and R-Kummer tower is pro3. The zero-primary condition and quadratic disjointness force the global g-class to be kappa2(g(nR)) whenever n!=0. If n0, the same reasoning gives the zero class: at zero-primary places the compact centre is O, and g is regular there with g(O)=1, independent of cusp tangent.

Suppose first n!=0 and alpha!=n. Put k=v3(alpha-n), and choose T in E[3^(k+1)] with (alpha-n)T=d1. Over L'=L(E[3^(k+1)]) this target is rational. The extension L'/L has odd3-power degree. The A.67 identity proves that

 h=g(nR+d1)/g(nR)

is nonsquare in L, by its odd valuation at the unique place above3; it stays nonsquare over L'. Its quadratic extension is disjoint from the pro3 torsion/Kummer tower over L'. Apply the prescribed-primary lemma with R3=T and choose the nonsquare quadratic Frobenius simultaneously. The actual compact centre at that place is nR+(alpha-n)T=nR+d1. This contradicts the forced global g-class. Thus alpha=n.

For n0, suppose alpha!=0. There is a fixed order9 point S for which g(S) is nonsquare in L9=L(E[9]). To prove this exactly, at q73 use b=25,zeta=8 modulo73. The point P=(1,0) has order9 and g(P)=56 is a nonsquare. The order9 residue point has a unique prime-to73 torsion lift S in E[9](Q73). It belongs to L9; the residue degree of L9/L at that place is odd because this is a pro3 extension, so the nonsquare persists. Thus g(S) is globally nonsquare in L9, and S is interior since its order is exactly9.

Choose T with alpha*T=S over L_r=L(E[3^(v3alpha+2)]). The odd extension preserves the nonsquare class of g(S). The quadratic extension it defines is disjoint from the pro3 tower. Prescribed-primary Chebotarev with R3=T then forces the local centre to be S and its g-value nonsquare. This contradicts the zero global g-class. Hence alpha0, as asserted.

No analogous baseline0 result at arbitrary other coefficient primes is inferred: the norm orbit of nR would be constant when n0, and its Faltings contradiction would disappear.
