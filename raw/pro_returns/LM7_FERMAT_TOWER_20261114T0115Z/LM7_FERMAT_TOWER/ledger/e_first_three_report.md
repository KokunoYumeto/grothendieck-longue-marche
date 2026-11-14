# E.49: complete global H sections with first Kummer class three

The fixed raw first cocycle is A=3 kappa_3(3), using positive compatible real roots. The result evaluates its entire global section fiber in the actual arithmetic quotient H.

Let P be the rational primes p!=3 for which the residue of 27 has multiplicative order prime to three. The complete coordinates are

Z_3 × R(P) × Z_3 × Z_3[[Z]],

where R(P) is the module of Z_3 sequences tending to zero modulo every power of three. The scaled toric coordinate is

(kappa_3(3), b_3 kappa_3(3) + sum_p b_p kappa_3(p)).

Thus the toric image is explicitly determined, including all completed inputs. Every toric fiber has the compact coordinates Z_3 × Z_3[[Z]]. All these parameter groups are torsion-free.

## Actual arithmetic normal form

The proof changes the prolongations of the two actual Frobenii over seven by an explicit conjugation. If the initial Kummer value is t=1 mod3, conjugation by rho_0^((t^-1-1)/12) changes it to one. The conjugate generator has value minus one, and their Frattini classes remain the free basis.

With sigma=tau and rho=tau' tau^-1, the twisted coefficient action is exactly

sigma(u)=7T^3 u(T^7), rho(u)=T^-6 u, C(u)=-u(T^-1).

Every unramified section class has the unique representative

v(tau)=3b_3 + z eta + T^3 W f(W^2),

where W=(T-T^-1)/2 and eta=1-(T^-1+T^-2)/2. The proof gives the correcting coboundary by division by T^-6-1, proves that this correction is C-fixed, and extracts the remaining odd W-series. The division is integral because (T^-6-1) and (T^3-1) generate the same ideal. Every inverse map is continuous on its actual closed principal ideal.

## Finite coefficients and residue surjectivity

For the actual finite coefficient images, the action over K=Q(zeta_3) has three-power image. Degree-one cocycles factor through the maximal pro-three quotient by their graph homomorphisms. Higher full-group cohomology vanishes by the proved trivial-F_3 composition series and the arithmetic dimension bound. This supplies the precise finite-coefficient comparison with the free group.

At p!=3, removing the Tate twist gives the affine Frobenius x -> A_F+p x. Its unique possible fixed point is integral exactly when ord_p(27) is prime to three. In that case the invariant integral measure lattice is Z_3 delta_x; otherwise it is zero. Nonfixed affine orbits admit no nonzero invariant integral measure, as their successive orbit partitions force arbitrarily high three-divisibility. Intersecting with J gives 3 Z_3 delta_x, whose scaled toric residue is integral.

Finite localization yields a short exact degree-one sequence because the unramified degree-two group is zero. The left finite groups are Mittag-Leffler. Its inverse limit is therefore exactly onto the restricted residue families, without a closure or an omitted inverse-limit term. All primes p=2 mod3 are allowed, including two.

## Independent field and norm calculation

The actual finite etale algebras factor into

F_n=Q(3^(1/3^(n-1))) and L_n=Q(3^(1/3^(n-1)) zeta_(3^n)).

The degrees are 3^(n-1) and 2*3^(n-1). The lambda-valuations 2/3^(n-1) prove the full local degrees over K and total ramification at the unique prime above three. The L_n tower and the auxiliary KF_n tower are cyclic cubic at each step and ramify nowhere else.

The ambiguous class formula proves that their class numbers are prime to three. The strongly ambiguous formula then makes the ordinary-unit norm index divide a prime-to-three class number; since that index is a power of three, it is one. Thus actual ordinary-unit norms are onto in the cyclic towers. Averaging complex conjugation by (1+c)/2 gives surjective completed unit norms in the F_n tower.

The ordinary-unit norm limit is completely evaluated by the power series f. At level one, Shapiro and the exact Kummer relation lambda^2=-3 zeta_3 identify the two three-prime valuations of a+z eta+T^3Wf as (a+z,-z). Their vanishing leaves exactly T^3Wf. This proves the entire ordinary-unit limit, not only a rank bound.

For p!=3, finite Frobenius orbits are the prime ideals of the etale algebra; pushing their orbit sums multiplies by the relative residue degree, exactly the ideal norm. The unique integral affine fixed point gives a compatible degree-one prime chain. Every other valuation disappears. The full valuation limit is Z_3^2 × R(P).

For each allowed prime, completed principal divisors exist because the class groups are prime to three. Surjective unit norms then correct chosen generators recursively into a coherent system pi_p. The specified three-unit systems xi_F,xi_L and ordinary-unit system epsilon(f) give every section through

epsilon(f) xi_F^(3b_3+z) xi_L^(-z) product_p pi_p^(3b_p).

The cube condition at level zero is exactly the stated divisibility of the three-prime sum and the other valuation coefficients. This independently constructs every allowed global class by actual norm equations.

## Executed certificates

The saved files are code/e_first_three.py, code/e_first_three.out, and code/e_first_three.json.

- 64 exact Laurent-polynomial normal-form reductions, recovering the original correcting coboundary and power series.
- The exact C/sigma/rho action identities and all three-prime valuation maps.
- 22 exact arithmetic Frobenius conjugations with three-adically integral exponents.
- 957 ideal-norm positional transitions at 54 primes, including the saturated fixed-chain criterion.
- Four exact radical field factorizations, local-degree certificates, and generator norms.

All checks pass. The ineligible primes below 260 are 19, 37, 109, 127, 163, 181, and 199.

## Scope and exact comparisons

This is a full evaluation of the indicated global H-section fiber. The actual maps from the intrinsic metabelian and marked groups retain the kernels displayed in E.38 and E.47. No section lift through those kernels is inferred from these target coordinates.

## Primary passages

The existing bibliography entries are reused. Lemmermeyer's original author preprint, https://arxiv.org/pdf/1309.1071, was opened at Theorem 1, formulas (1) and (2), including the full ideal and unit Herbrand argument. Formula (2) is the precise ordinary-unit norm index used here.

The finite localization maps are Milne, Arithmetic Duality Theorems, II.0.1(f), II.1.7(b), and II.2.9. The continuous inverse-limit comparison is Jannsen, Continuous Etale Cohomology, Proposition 1.6 and Theorem 2.2. These exact primary passages were opened for the preceding localization results and are retained with their actual finite coefficient and Mittag-Leffler hypotheses.
