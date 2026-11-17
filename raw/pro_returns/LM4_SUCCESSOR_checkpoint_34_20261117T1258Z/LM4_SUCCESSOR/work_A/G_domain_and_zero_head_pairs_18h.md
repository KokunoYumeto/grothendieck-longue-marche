# The actual coefficient group embeds in F13 times F13

Research proof, checkpoint18. This supplies a domain argument for all sixteen
actual zero-head column pairs. It does not prove independence of the two
entire64-column modules or their whole-overlap cohomology.

## 1. An explicit finite-rank embedding

Retain B94's T=F5 and R, free on x_(g,i), g in T and i in the eight deleted
slots. Let alpha_t shift the retained label g to tg. The semidirect product

                         R semidirect_alpha T

is the free group on the five retained generators and eight generators a_i.
An explicit isomorphism sends x_(g,i) to g a_i g^-1 and fixes T. Conversely
send a_i to x_(1,i) and each retained generator to itself in the semidirect
product. The two homomorphisms are inverse on all displayed generators.
The forward map respects the action relation because
t(g a_i g^-1)t^-1=(tg)a_i(tg)^-1. Thus this identification does not require
an assertion about an arbitrary infinitely generated semidirect product.

The actual coefficient group is

G=(R_A times R_B) semidirect T,
(u,v,t)(x,y,s)=(u alpha_t(x),v alpha_beta(t)(y),ts).

There is an explicit injective homomorphism

  j:G -> (R semidirect_alpha T) times (R semidirect_alpha T),
  j(u,v,t)=((u,t),(v,beta(t))).                           (1)

Multiplication on the second coordinate is exactly its ordinary retained
shift by beta(t), and beta(ts)=beta(t)beta(s). Thus(1) is a homomorphism.
Its coordinates recover u,v,t, proving injectivity. Each target factor is
the free group F13 just identified. The common beta convention is therefore
retained; it is not silently replaced by an untwisted diagonal action.

## 2. A self-contained bi-order of the finite-rank free factors

In the ring of noncommutative formal series over Z on thirteen variables,
map the free generator a_i to1+X_i and its inverse to the formal geometric
series. This group homomorphism is injective. Indeed, write a nontrivial
reduced word in maximal blocks

                  a_i1^n1 ... a_ir^nr,

where every n_j is nonzero and adjacent i_j differ. The coefficient of
X_i1 ... X_ir is n1...nr, which is nonzero. This monomial has r successive
runs of variable names. Omitting a positive-degree term from any block
would leave fewer than r runs, so cannot produce it; taking positive terms
from all r blocks produces it only with degree1 from each block. The same
argument handles negative exponents, whose degree1 coefficient is n_j.

Order the finitely many variables, and order monomials first by total degree
and then lexicographically. For a nontrivial series f with constant term1,
declare f positive if the coefficient of the first nonzero monomial of
f-1 is positive. There is a first such monomial, since every degree has
only finitely many monomials. This gives a bi-invariant group order on the
image of the free group:

* inversion reverses the first nonzero coefficient;
* the product of two positive series is positive, since its first term is
  the earlier of the two first terms or their positive sum, while the
  product of the positive-degree parts has strictly larger degree;
* conjugation by a series of constant term1 preserves the entire lowest
  nonzero homogeneous part and hence its first monomial and coefficient.

These facts define a positive cone closed under multiplication and invariant
under conjugation, with exactly one of f,f^-1 positive for f not1. Thus the
free group is bi-orderable. This is the integral Magnus construction; the
argument needed here has been given explicitly. No order on an infinite
alphabet or finite-support convention for an infinite homogeneous piece is
required, because both factors in(1) have rank13.

The lexicographic product of two bi-orders is a bi-order, and restricting
it along(1) bi-orders the actual G.

## 3. The integral coefficient ring is a domain

Let A,B be nonzero elements of Z[G]. Their supports are finite. Let g0,h0
be the maximum elements of their respective supports in the bi-order.
The maximum element of the product support before collecting coefficients
is uniquely g0 h0. If g<g0 and h<=h0, then gh<g0 h<=g0 h0; if g=g0 and
h<h0, the product is again strictly smaller. Hence the coefficient of
g0 h0 in AB is the product of two nonzero integer coefficients. It is
nonzero. This proves that Omega=Z[G] has no zero divisors on either side.

In particular every nonzero coefficient in a private row of a left-module
column is regular. This conclusion uses the exact embedding(1), not a
general zero-divisor conjecture for torsion-free groups.

## 4. Consequence for the sixteen actual stabilizing actions

The complete actual certificate

* work_A/zero_head_diagonal_node_actions.json;
* work_A/code/check_zero_head_diagonal_node_actions.py/.out/.err

checks the sixteen zero-head root-generator/fixed-node pairs. For each pair,
let c be the actual original column and d its actual transported column.
Their augmented row and signed retained unit agree, but d has a nonzero
full G row absent from c. The certificate retains a specific nonzero term
at such a row; distinct G coefficients are collected exactly in its producer.

Suppose a c+b d=0 with a,b in Omega. The private row gives b d_row=0.
The coefficient d_row is nonzero, so the domain result forces b=0.
Since c is nonzero, any one of its nonzero rows then forces a=0. Thus

                         Omega c + Omega d

is a direct sum of two free rank-one Omega modules in every one of these
sixteen cases. The absence of a group-unit relation is therefore strengthened
to full two-column independence over all integral coefficients.

Each of these physical nodes is F-fixed. Its original one-column submodule
is F-stable by B94's actual mate relation; its transported one-column
submodule is F-stable by the actual discrepancy formula of B96. The root
generators are in the even source-cover subgroup. The two modules therefore
have their actual source-conjugate rank-one C2 types. For the selected-cone
nodes, each has H1=F2[R] and H2=0; for the other-cone nodes all positive
cohomology vanishes. Directness proves that these two-column sums have only
the two individual source contributions and no new positive-degree overlap
class. In particular this diagnostic supplies no new kappa value.

This result does NOT determine
L_ret intersect alpha_root(L_ret). Other columns of either64-column block
can enter a relation even though the displayed matching pair is independent.
It also does not determine overlaps with a whole preceding orbit sum.
No iteration, full old-base freeness, source equality, nonlinear fixed lift
or compact coefficient result is asserted.
