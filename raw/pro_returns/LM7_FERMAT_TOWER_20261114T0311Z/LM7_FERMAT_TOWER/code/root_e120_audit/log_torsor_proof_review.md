# Root review of the integral elliptic logarithm torsor

Verdict: PASS for the frozen note's coefficient, cup-primitive and evaluated
local-class assertions. The intrinsic arithmetic extension comparison
specified in its final section remains active and unassigned.

Reviewed note SHA-256:
`d5a59b170710b68f481a81e02895f3ae977c28b6f60d8e7669a0fb01b257704e`.
Frozen manifest SHA-256:
`c288aafb2017b0fcc0da339ddc63e7c3404736e0b1a9bdd27d3241e7ab789d90`.
Root replay audit SHA-256:
`35ff6ffe6d4d9ed4b5f3b09407513fd985998115ffc32bb3c27f1fff31d4624f`.

The entire note and both final mathematical programs were read. The earlier
frozen Tor-symbol and theta-distribution constructions retain their separate
root reviews, complete replays and independent checkers.

## Exact logarithm coefficients and maps

For the actual division torsor [3^n]Q=A0, the map delta_Q -> (1,[3]Q)
has image h mod 3=a A0. Translation by a coherent division point gives
the actual inverse coordinates h=a h0+3z, with a modulo 3^n and z modulo
3^(n-1). The finite group consequently has factors
C_(3^n), C_(3^(n-1)), C_(3^(n-1)). Its inverse limit is the indicated
rank-three lattice. The completed augmentation-ideal calculation identifies
the quotient by I squared through those same coordinates. Both finite
kernels are retained: C3 squared for L/3^n L -> L_n, and C3 for
L_(n+1) -> L/3^n L. The latter kernel's transition is zero.

The arithmetic action on (a,z) contains the actual integral torsor cocycle
(A-I)h0/3. Substitution gives dz=-kappa_t cup a with the stated
inhomogeneous-cochain sign. Compatible theta Kummer classes give the class
in this lattice by the actual transfer maps and Norm_[3](theta)=theta.
The inverse-limit H1 comparison uses finite H0 groups, so its lim^1 term
vanishes. At a good prime away three, scalar inertia vanishes and the
remaining inertia equation is killed by q(F_E-I), an injective lattice
map. Wild inertia has residue characteristic different from three.
This verifies the stated unramified factorization through the retained
arithmetic source.

The map Phi(a,z)=a t0-p*(omega S z) has inverse given by the scalar
coordinate and z=-(omega S)^(-1)x. Its determinant is the unit omega squared.
The raw expression (a l-p*omega S h)/3 is integral in the actual lattice
because l=3t0+p*u and omega S h0=u. The intertwining square follows by
substituting S A=chi A^(-T) S, including its cross term. Complex conjugation
has its separate literal square and transports theta_pi to theta_bar(pi).
The note does not identify those two arithmetic classes.

The finite quotient is exactly
M/(3^n Z3 t0+3^(n-1)p*H*(2)); its use retains the previously lost digit.
The executed exhaustive check includes all 61,320 finite elements for
n=1,2,3,4, their inverses and the actual Frobenius action.

## Division chart and basis transport

The finite-field certificate uses the retained polynomial model and
literal points P,Q. The Miller line products and twelve bilinearity checks
give Weil exponents 1,4,13 at levels 3,9,27. Thus omega=13 modulo 27
belongs to this specified division chart. The generic transport with
B congruent to I modulo three is retained, including C_B, the dual row
map, the determinant change of omega, and the integral carry in z.
The full free-pro-three basis automorphism is specified on generators
and has invertible Frattini matrix. Its role is transport of the complete
arithmetic action by conjugation. No numerical B or extra preservation of
an omitted boundary word is assigned by this basis-change construction.

## Evaluated full local class

For F=[-2] on the proper Tate module and chi=4, the displayed target
matrix has F-I with columns (3,0,4),(0,-9,0),(0,0,-9).
The map to C9 plus C27 is (a,x1,x2) -> (x1,a+6x2), with the specified
moduli; every column maps to zero. The inverse sends (r,s) to (s,r,0).
For an arbitrary vector, its difference from this inverse is
(-6x2,0,x2)=(F-I)(-2x2,0,-x2). The period 9 in the first factor has
preimage (0,-1,0), and 27t0=(F-I)(9,0,4). These are the actual
integral boundary identities. They also show that the finite target at
n=3 detects the entire local group.

The finite transfer uses one wrap-around term (k,kR) for an orbit,
with no added orbit-length multiplier. Every representative change is
checked as an actual (F-I)-boundary. The resulting raw pairs at
levels 3,9,27 are (2;2,0),(8;8,3),(8;8,3). The last pair gives
(8,4,4) in the target. The chosen roots of theta(A0)=-lambda have
scalar Kummer value two; the simultaneous change s=-2 has raw boundary
(3s,-9s omega^(-1)e1). It gives (2;26,3) and target (2,4,5).
Both target representatives give the same local class (4 mod 9,5 mod 27),
whose order is 27 and whose augmentation is two modulo three.

## Literature scope and remaining comparison

The original Kings 2007 PDF, arXiv0711.2443, Section 1.1 and Definitions
1.1.2--1.1.3 were reopened and read: finite covers, trace transitions,
the logarithm sheaf and its abelian quotient. The original Kings 2000 PDF,
arXivmath/0003113, was reopened for the statement of Theorem 4.1.3,
Lemma 3.5.1 with its proof, and the rational moment/splitting passages in
Section 3.5. The complete proof of Theorem 4.1.3 was read by the author
agent, not independently in this root review. No unreviewed step of that
theorem is needed for the direct lattice and local calculations above.
The prime-to-three torsion restriction in Lemma 3.5.1 is retained;
the actual three-torsion lattice here is supplied by the direct map L1.

The required next map starts with the intrinsic class-two arithmetic
extension and its retained peripheral commutators. The coefficient
isomorphism Phi, the evaluated theta class and the already verified Tor
regulator give explicit targets and comparison data. Their coefficient
in that intrinsic extension has not been assigned. No result in this
review promotes the auxiliary calculation to a completed E.23 answer.

## Independent execution

`log_torsor_replay.py` checked all nine owned files and four immutable
inputs before and after copying the two complete programs to a fresh
directory. Both actual executions exited zero with empty stderr. Every
byte of each complete stdout, stderr and JSON agreed with the frozen
author files; there were no field exclusions. The author files remained
unchanged. All fresh outputs, the replay driver and its actual transcript
are retained with the audit.
