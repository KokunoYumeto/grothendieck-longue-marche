# Root complete proof, source and executable audit of D.91

**PASS; approved for canonical integration.** Root read the entire 530-line
candidate, `notes/de_sha_all_cusp_parameters_draft.tex`, SHA-256
`2c82e369cc244d1b841710530a763d4bcaba4063afae84707ac4cb4272931ddd`,
and rederived its actual comparison maps, the finite boundary extension,
the finite-exponent splitting and the integral infinite-depth splitting.
Root also read both complete certificate sources and executed both. The
precise executed hashes and comparisons are in
`notes/root_D91_certificate_verification.json`. The independent FGH and
PBC full audits are retained separately. PBC's earlier candidate differs
from this one only by the subsequently removed literal `+in` typo; FGH
audited the final candidate hash above.

## Scope and exhaustive case distinction

The statement concerns the compact second-cohomology kernels for every
completed cusp parameter, with its actual tangential marking. It does
not classify arbitrary abelian pairs, unrestricted first-cohomology
ranks, or higher-derived obstructions. The away-five zero case is
handled directly by equality of the actual global and local graphs,
including the zero parameter; it is not inferred from arithmetic on
infinite valuations. For a nonzero away-five class the depth r is finite,
the local depth N is at least r, and the coefficient depth m may be
infinite. The equal-image case N=r is zero. The cases m at most r,
m infinite, and r at most N at most m reduce to the previously proved
D.88--D.90 with the actual graph action checked, leaving precisely
r<m<N, with N finite or infinite. Thus no ordering of the three depths
is omitted.

For finite e=N-r the formula has a countable product of cyclic groups
of order 5^e, the two copies of each smaller boundary factor of order
5^(H+j), and the separate free factor of rank 2H in K. At infinite N
and finite m, the smaller finite factors remain, with orders 5^(h+j).
Absorbing a finite free factor into a countable product of Z_5 is only
an abstract compact-module identification and does not identify the
natural subgroup S inside K. The text makes this distinction explicitly.

## Actual operators and the retained scalar generator

Put h=m-r>0 and, at finite depth, b=N-m>0. The actual operator ideal
from D.87 is (P,q_m), where P=uvw and q_j=t^(5^j)-1. The kernel is
the actual map from the coinvariants of J/(PJ+q_m J) to those of
R/(PR+q_m R), with J=q_r R. Retaining q_r as the source scalar
generator matters: the source action is chi^(-1) S_chi(t^(5^r)) rho_0,
and the actual map to the target is multiplication by q_r. The graph
multiplier becomes one modulo q_m, by an integral unit quotient,
not merely after tensoring with Q_5.

With F=q_m/q_r, the finite scalar ring is
B=Lambda/(q_m,5^b F); at infinity it is Z_5[C_(5^m)][[v]]. In
both cases T=B/P. Reduction modulo u gives C[[v]], with C=Z/5^e
or Z_5. Both v and w are regular: the second assertion uses the
continuous invertible change of variable v to u+(1+u)v. The element u
is topologically nilpotent, t is a unit, and the change preserves
q_m. No cancellation by u in the cyclic group ring is assumed.

## The shell injection survives coefficient reduction

The exact sequence 0 -> E -> T -> Q -> 0 has
E=vwB/uvwB and Q=B/vw. The retained generator q_r v w gives the
precise shell action chi S_chi(1+v)^3, whose coinvariants are the
countable product C. The quotient Q/uQ consists of the two jets with
nontrivial tame weights chi^2 and chi^3. Also (u) intersect (vw)
equals (uvw): modulo u, multiplication by v^2 is injective even
over finite C. Consequently uT -> uQ is an equivariant isomorphism;
every invariant in Q lifts invariantly. This proves the zero connecting
map and the actual injection E_Gamma -> M. The argument works after
every reduction modulo a power of five, which will be essential at
the infinite endpoint.

The annihilator of u in B is exactly C_b[[v]] N_m, where
N_m=q_m/u and C_b=Z/5^b, or Z_5 at infinity. To check this, lift
uf=F(q_r g+5^b k) to the original domain, evaluate at u=0 to see
k(0)=0, and cancel u there. The exact order of the remaining norm
class follows by cancelling F and then reducing modulo q_r; the
norm coefficients are units. Thus the two-axis map has precisely
the kernel C_b v N_m, of tame weight chi^3, and an augmentation
cokernel of weight chi^2. Both vanish under tame averaging. The
argument does not mistakenly declare the two-axis map injective.

## Boundary transport and the actual stabilizer homomorphism

Multiplication by u q_r transports the first-axis action to the
ordinary permutation action on uJ_(r,N)/q_m uJ_(r,N). The full
cyclic norm cannot lie in J, so u is injective on J. The kernel
and cokernel of the ensuing inclusion into J/q_m J have the
nontrivial tame weights chi^2 and chi. The diagonal axis is the
same after the explicit half-gauge, which commutes with q_r.
Hence Q_Gamma consists of two copies of (J/q_m J)_Gamma.

At finite depth the relevant affine group is D semidirect Gamma,
where D is cyclic of order 5^b and translates by 5^m. Dualizing
the compact permutation modules gives discrete Q_5/Z_5-valued
functions. Pullback of these functions restricts point-stabilizer
characters. Dualizing back therefore gives the inclusion of
stabilizers on pro-five abelianizations. It is not a transfer map.

For a lower nonzero shell with k=r-j, its stabilizer has
pro-five abelianization C_(5^min(b,k)) plus Z_5. Its unique upper
orbit has graph stabilizer with chi in 1+5^(k+h) Z_5. On choosing
chi=(1+5^k)^(5^h), the translation coordinate is a unit by LTE,
and the actual inclusion sends a generator to (unit,5^h).
Its cokernel is the single cyclic group of order
5^(h+min(b,k)). It is generally not the product of two smaller
cyclic groups. The zero orbit gives no extra homology cokernel,
because the tame action kills D there and the upper zero
stabilizer maps onto Gamma. The orbit kernel is free of rank h.
This proves the boundary module
Z_5^h plus the factors C_(5^(h+min(b,k))) for 1<=k<=r.
In particular r=1,m=2,N=3 gives Z_5 plus Z/25.

The target boundary is the augmentation ideal in Z_5[C_(5^m)]
after tame averaging. The source and target transports commute
with multiplication by q_r, so the boundary comparison is the
literal inclusion into that permutation module. Its finite
homology cokernel maps to zero; its free part identifies with
the orbit kernel from depth m to depth r. The target's own
axis-intersection errors have nontrivial tame weights. Therefore
there is no additional free kernel hidden in the comparison.

## Finite-exponent splitting and the exact kernel

The actual target U is torsion-free, by its identification with
the local Cartier-invariant dual already proved in D.77. The
preimage in M of the two finite boundary parts is thus exactly
S: its remaining free boundary quotient maps injectively. This
gives an extension of the two finite boundary parts by the
countable product Z/5^e.

The entire extension has exponent dividing 5^e. This uses
restriction followed by corestriction for the actual finite-index
inclusion I_5 inside I_s; it does not assume that inclusion is
normal. Under D.87 the restriction kernel is annihilated by the
index 5^e. If x lifts a cyclic quotient generator of order
5^c, then 5^c x lies in the shell product and is annihilated by
5^(e-c). In this specific product that annihilator is exactly
5^c times the product. Correcting x by a shell element gives
an actual finite-order lift. Finitely many such lifts provide
a continuous splitting. The factors whose exponent equals e
are absorbed into the countable product; all smaller factors
are retained. This gives exactly the finite formula in D.91.4.

## Infinite-depth passage and integral splitting

For fixed m,r, the scalar modules at finite b are the quotients
of R_m by 5^b F R_m. Their inverse limit is R_m. Coinvariants
commute with this particular limit because the image of the
continuous operator rho(2)-1 is compact and closed, and the
intersection of that image plus 5^b F R_m is the image itself.
This is a proved compactness statement, not an unrestricted
interchange of cohomology and inverse limits. For b>=r, the
finite boundary factors have stabilized, their actual transition
maps are surjective, and the free orbit quotient maps are the
identity. Thus the limiting boundary factors are exactly
C_(5^(h+k)), together with Z_5^h.

Let M_0 be the preimage of the two finite boundary torsion
groups in M. The shell is now the countable product Z_5. The
coefficient-reduction version of the zero-snake injection proves
E_Gamma intersect 5^H M = 5^H E_Gamma. For H at least m,
the finite boundary quotient is killed by 5^H, so
5^H M_0=5^H E_Gamma. The resulting finite-exponent quotient
splits by the preceding order-correction argument. Lifting its
finite-order representatives to M_0 and correcting inside
5^H E_Gamma, which lies in 5^c E_Gamma for each required c,
produces actual integral finite-order representatives. This
proves a continuous splitting of M_0 itself.

Finally the actual source-to-target map kills the shell because
q_r v w=P(q_r/u) is zero in the target. It kills the finite
torsion because U is torsion-free, and is injective on the
remaining free boundary quotient. Therefore S=M_0 exactly.
No equal-corank argument or rational splitting is substituted
for this integral proof. D.77 then contributes the stated
separate free factor to K.

## Markings, examples, sources and execution

The actual coordinate transformations t -> 1-t and t -> 1/t
transport the abelian pairs to (0,a) and (-a,-a), respectively;
kappa(-1)=0 in the pro-five setting. Carrying the tangent
frame and inner gauge transports the complete global/local
diagrams, so all three cusp packets, including zero parameters,
are covered without identifying distinct marked sections.
The rational tangent in D.91.6 has exact away-five depth r:
1+5^(e+1) is 2 modulo 4, hence its valuation at 2 is one.
Its five-adic logarithm has the asserted depth e+1. The
independent five factor has depth m. The displayed example
therefore has (r,m,N,e)=(1,2,4,3), as claimed. The completed
infinite-depth examples use the explicitly checked unit
logarithms and actual cusp-section construction.

Root freshly opened Milne, *Class Field Theory*, version 4.03,
<https://www.jmilne.org/math/CourseNotes/CFT.pdf>: II Proposition
1.11, printed p.62; II Example 1.27(a,b), printed pp.68--69;
and II Example 1.29 and Proposition 1.30, printed p.70. The
retrieved passages `turn1221view0` and `turn1222view0` were read.
They supply Shapiro's evaluation-at-identity convention and
the finite-index restriction/corestriction identity. The
continuous open-stabilizer version here follows by the same
finite-coset cochain formula; the manuscript also explains
the duality and map orientation. The earlier overlarge tool
response was truncated and was not counted as read.

The owner certificate passed all 12 middle-range rows and
two target rows; every mathematical output field agreed,
excluding only elapsed-time and source-path metadata. Its
source SHA-256 is
`8ef061fba5ed6db2484eb4091401ff7fb97fc9ac78ce64c6d3b940b641097660`.
The independent PBC certificate passed all 180 stabilizer
Smith/LTE cases and reproduced its entire JSON byte for byte,
SHA-256
`67e7f0a576e19f14688dcf2132b246c96d8d90f19eca7246a24e73ed851511bb`.
These calculations check the literal norm/gauge matrices,
natural-map ranks and nonsplit cyclic factors; they supplement
the complete proof rather than extrapolate it. Earlier slow
or failed attempts and all audit revisions remain retained.
