# Infinite nonunit coefficient support: exact exclusions

## Status and scope

This note continues A.65 without changing frozen deliverables. The main theorem below is a proved extension, independently checked in its formal-distance step by B. A.65 settles exponents that are units at almost all coefficient primes. The present argument handles many exponents whose nonunit support is infinite, and uses no CM or finite-Sha hypothesis.

**Proposed theorem (A.66 if assigned).** Let E/Q be an elliptic curve, N>=2, U=E-E[N], and R in E(Q) nontorsion. Let a=(a_p) in Zhat have only finitely many zero components. Suppose that for some prime lambda, the finite integers v_p(a_p) are divisible by lambda for all but finitely many p. If the proper Kummer section a*kappa(R) has a geometrically abelian Selmer lift, then a is a nonzero integer; its abelian Selmer fibre is the unique point section by A.64. The same exponent exclusion holds at every larger quotient, including the intrinsic metabelian one. No statement about the metabelian fibres is made.

Over an arbitrary number field the new contradiction is valid whenever infinitely many positive coefficient valuations occur. Only the reduction of the finitely many positive valuations to actual integers uses A.65 over Q.

In particular a_p=p^lambda at every coefficient prime has no such lift. More generally, every nonintegral componentwise lambda-th power b^lambda with only finitely many zero components is excluded. This includes infinite nonunit support and is not contained in A.65 or A.63.

## Simple boundary functions

Pass to one finite Galois extension L splitting E[N]. Choose independent P,Q in E[N](L), so O,P,Q,P+Q are four distinct points. The degree-zero divisor

  (P)+(Q)-(P+Q)-(O)

has zero Abel--Jacobi class and is principal. In a Weierstrass plane model one can take the line through P,Q divided by the vertical line through P+Q. Let g be a defining rational function, and for each d in E[N](L) let g_d be its translate with divisor

  (P+d)+(Q+d)-(P+Q+d)-(d).

Every g_d is a unit on U, with a simple pole at d. This family is finite and supplies a unit of order exactly one at every cusp. Thus no coprimality condition between lambda and N is necessary. The earlier f_d with divisor N(d-O) can alternatively be retained at coefficient level N*lambda, but this simple-pole family makes that detour unnecessary.

A putative global geometric-abelian Selmer section supplies global classes in H1(L,mu_lambda) for all g_d. Choose one representative of each and one fixed finite set S containing their supports, the primes of bad reduction, all primes over N*2, the ramified rational primes of L, the finitely many zero-component primes of a, the finitely many coefficient primes at which v_p(a_p) is not divisible by lambda, and all vertical components of all g_d. Outside S, the four horizontal divisors of every g_d are disjoint and each has multiplicity +/-1.

At any finite v outside S above q, the compact local centre Q_v=[a]R is nontorsion. Indeed the local elliptic logarithm has torsion kernel, R remains nontorsion locally, and its logarithm is multiplied by the nonzero a_q. Hence the local Selmer class is the actual point Q_v in U(L_v). The global mod-lambda characters give

  v(g_d(Q_v)) = 0 mod lambda

for every d and v outside S. If Q_v approaches any cusp c, apply g_c, whose simple pole forces that positive formal distance to be divisible by lambda.

## The rational orbit and the formal-distance transfer

If a has infinitely many positive finite valuations, the eventual divisibility assumption supplies infinitely many ordinary positive integers n_j which are lambda-th powers and divide a in Zhat. For example, enumerate distinct primes p_i outside S with v_{p_i}(a_{p_i})>=lambda and take n_j=(p_1...p_j)^lambda. Put R_j=[n_j]R. These are infinitely many distinct L-rational points, none torsion. The quotient b_j=a/n_j lies in Zhat.

If R_j reduces to a cusp d in E[N], then Q_v=[b_j]R_j reduces to the cusp [b_j modN]d. In the formal group,

  Q_v-[b_j]d = [b_j](R_j-d).

Since q is odd and unramified in L, the formal logarithm is an isometry on the formal kernel. Multiplication by b_j changes the formal distance by exactly

  v_q(b_{j,q}) = v_q(a_q)-v_q(n_j).

This is a finite nonnegative multiple of lambda: n_j divides a, all its prime valuations are lambda multiples, and the exceptional a-valuations were included in S. The distance of Q_v from its cusp is divisible by lambda by the unit characters, so the distance of R_j from d is divisible by lambda also. Whenever R_j does not approach a zero or pole of g, its valuation under g is zero. Therefore

  v(g(R_j)) = 0 mod lambda

for every j and every v outside the same fixed S.

The group L(S,lambda) of multiplicative classes unramified in valuation outside S is finite. Hence infinitely many R_j lift to a finite family of twists z^lambda=c^(-1)g. These covers are geometrically connected: g has simple zeros. Each degree-lambda cover of E is fully ramified at the four distinct points O,P,Q,P+Q and nowhere else. Riemann--Hurwitz gives 2g-2=4(lambda-1), hence g=2lambda-1>=3. Faltings makes each twist's L-rational points finite, contradiction.

If a has only finitely many positive finite valuations, together with the assumed finite zero set it is a unit at almost all coefficient primes. A.65 makes it a nonzero integer and supplies the exact abelian fibre. This completes the proposed theorem.

## A separate exact necessary local distance formula

Let a have no zero components, and at a good rational prime q>=5 not dividing N let r_q be the order of R modq. Put d_q=r_q/gcd(r_q,N) and h_q=v_q(t([r_q]R)), where t is a formal parameter at O. Then

  aR modq lies in E[N] iff d_q divides a in Zhat.

When that condition holds, the positive distance to its unique N-torsion cusp is

  H_q(a)=v_q(a_q)-v_q(r_q)+h_q.

Indeed [N]aR=[Na/r_q]([r_q]R), and multiplication by N is a formal isometry. For a putative abelian Selmer lift, the family of simple-pole unit characters at every finite coefficient level m forces H_q(a) to be divisible by m for all but finitely many such q. Thus along the boundary-prime set the H_q tend to zero profinitely. If the boundary-prime set is infinite, their positive ordinary values tend to infinity as well. If it is finite, the rational-unit finite-support argument of A.65 forces a to be an integer.

This criterion by itself does not settle arbitrary a. For example the elementary valuation profile v_p(a_p)=1 at every p is not eventually zero modulo any lambda, so the proved new theorem does not exclude it. One cannot replace the fixed finite S by an infinite exceptional set, or assume uniform control of elliptic logarithm valuations. No such shortcut is claimed.
