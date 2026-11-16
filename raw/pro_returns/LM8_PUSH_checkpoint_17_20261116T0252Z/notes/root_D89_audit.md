# Root full proof audit of D.89

**PASS.** Root read the complete candidate
`notes/de_sha_primitive_valuation_cusp_draft.tex`, SHA-256
`3106671f92ebf80143b1b6695a4c8663626d27ebcc419029cd87dd0e6f883d3e`.
Root also freshly reread D.82's actual Kummer-five descent, saturation and
tame-projector proof, and D.77's full local primitive cubic construction.
This is a structural proof with the exact D.82/D.88 computations already
executed. It makes no new finite computational assertion requiring a
separate illustrative test.

The hypothesis is a completed cusp parameter (a,0) whose coefficient
A=a_5 is a five-adic unit. The away-five lattice may have arbitrary
finite depth r and infinite support, or be zero. Its local unit depth
N is at least r, with infinity allowed. The proposed answer is the
exact full compact kernel, not merely a bound or a section criterion.

## The actual graph and two operator elements

D.83/D.87 identify the global and local operator images with the
away-five lattice and its local unit sublattice, both retaining the
same graph g to (A*kappa(5)(g),g). D.82 proves that kappa(5) really
descends to the actual untwisted operator image. Its proof uses the
raw odd Soulé weights 1+4*5^(j-1) and exact finite Kummer product
Phi_(5^j)(1)=5. It is not the weight-five Soulé character.

D.82's local valuation argument makes the image of kappa(5) on the
cyclotomic kernel all of Z_5. Thus an actual element tau with value
one exists. The actual compact image of (kappa(5),kappa_3) is stable
under the integral tame projector separating weights one and three.
D.77's explicit local Kummer calculation makes the cubic coordinate
primitive. Hence there is an actual delta with zero kappa(5) and
beta_delta-1=P times a unit. Root checked these exact image arguments,
including why an integral projector preserves the compact image.

## Exact ideal and zero map

On the cyclotomic kernel, each graph operator is multiplication by
t_1^(A*kappa(5)(g))*beta_g. The delta difference supplies P to the
operator-difference ideal, and tau then supplies t_1^A-1. Conversely
every difference belongs to (P,t_1^A-1), by the integral binomial
factorization and beta_g-1 divisible by P. Since A is a unit,
(t_1^A-1)/u has unit constant term, making this ideal exactly (u).
The two actual differences suffice; no dense subgroup is silently
substituted for an equality of closed operator images.

For R=Lambda/(q_N), or Lambda at infinity, and the actual submodule
J=q_r R, dual invariance under that cyclotomic kernel is precisely
annihilation of uR and uJ. This follows even though the functionals
are not Lambda-linear: every scalar multiple of a difference still
acts on an element of the same module. The inclusion J into R has
image inside uR because q_r is divisible by u. Thus the actual map
from R-invariants to J-invariants is zero. This identifies the whole
kernel in D.87 with (J/uJ)(-1)_Gamma, rather than comparing its rank
with a larger invariant quotient.

## Retained generator and both endpoints

At finite relative depth e=N-r, the scalar relation q_N/q_r has
constant term 5^e, so J/uJ is (Z/5^e)[[v]]. At infinite depth,
J=q_r Lambda and J/uJ is Z_5[[v]]. The actual generator q_r contributes
a factor chi under substitution; the untwisted Alexander factor at
u=0 contributes chi*S_chi(1+v); the graph multiplier becomes one.
Removing the single Cartier twist leaves precisely
chi*S_chi(1+v) times cyclotomic substitution. There is no division by
the nonunit 5^r.

Multiplication by v identifies this module with the augmentation
ideal under the chi-weighted multiplier action. The missing constant
quotient has a nontrivial tame character, so it contributes neither
an invariant correction nor coinvariants. The invariant discrete
dual consists of inverse-unit-weighted functions on each nonzero
valuation shell, zero at the origin. Continuity forces finite shell
support. There is one arbitrary value per shell in Z/5^e at finite
depth, and in Q_5/Z_5 at infinite depth. Their compact duals give
product Z/5^e and product Z_5 respectively, with the actual topology
and exact exponent. The infinite case is computed directly.

## Full K-group and examples

The nonzero boundary classes a and a-b both have global and local
depth zero because A is a unit. The zero boundary b supplies the
same countable product on both sides. D.77's natural local/global
boundary map is therefore an isomorphism, so D.63 gives K=S with
no additional free kernel. This also covers the equal-image case
e=0 and the pure valuation parameter with no away-five class.

The rational tangent 5*(1+5^(e+1))^(5^r) has coefficient one at five,
away-five depth r because its valuation at two is 5^r, and local
unit depth r+e. The infinite example adds kappa(5) to D.88's exact
zero-log completed parameter. These are actual cusp parameters and
therefore supply full sections; their finite valuation support lets
D.74 compute the first-cohomology translation group. Infinite torsion
in the compact second-cohomology kernel does not assert torsion in
that translation group.

The proof explicitly excludes a nonzero nonunit A, whose operator
ideal imposes a different cyclotomic relation. It makes no assertion
about arbitrary pair existence or higher derived obstructions. Root
approved canonical integration after this complete proof and
dependency check; PBC and FGH have separate full PASS ledgers.
