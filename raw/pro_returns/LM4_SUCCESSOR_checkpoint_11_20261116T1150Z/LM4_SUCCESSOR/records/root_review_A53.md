# Root review: A.53, bounded scalar refinement for every finite abelian layer

Reviewed 16 November 2026, approximately 06:17–06:22 UTC. Accepted
after reading the complete final all-abelian working proof and the
independent CE audit. This is a structural theorem, not an inference
from the preceding finite examples.

The conditional hypotheses are explicit: Pi=C2 free-product C3 is
full profinite; R is closed normal and R=[R,Pi]; W is closed normal
inside R with V=R/W finite abelian; and H1(C,V-dual)=0 for the
actual retained C=Pi/R. The dual is the finite Pontryagin dual,
not just a vector-space dual at one prime. These distinctions are
essential to the arbitrary-exponent statement.

At each stage, the abelianization sequence has as its kernel only
the image of the NEW globally central scalar kernel. The preceding
abelianization is already V. Relative perfectness kills invariant
characters, and the stated H1 vanishing kills the new kernel through
the dual exact sequence. The cofinal finite-quotient argument is
valid: the scalar kernel is contained in the residual group and in
the kernel of its map to V, so the preceding induced quotient still
retains V. Finiteness of an unknown scalar kernel is not assumed.

For the class-two induction, the old derived center paired with V
maps into the new globally central kernel. Mixed-primary tensor
products vanish. On the p-primary component the old center has
p-group action through the maximal p-quotient of the finite action
head. Relative perfectness and finite p-group Nakayama imply that
the corresponding coinvariants of V_p are zero. Thus every pairing
vanishes. The new derived group is a finite quotient of the actual
integral exterior square of V, and its action factors through the
finite action head by functoriality of the commutator pairing.

The action on the new center is again a p-group: its kernel fixing
both subquotients embeds in Hom(old-center,new-central-kernel), a
finite p-group, and the old image is a p-group. Since the head is
a quotient of Pi, its maximal p-quotient is C2, C3, or trivial.
The actual relative commutator subgroups are therefore the powers
of the corresponding augmentation operator on the center.

The exact operator identities are I²=-2I in the dyadic case and
I³=-3I(1+I) in the triadic case. For primary exponents 2^e2 and
3^e3 they give I^(e2+1)=0 and I^(2e3+1)=0, respectively.
All other prime components have trivial action. Hence, for
m=max(1,e2+1,2e3+1), the actual scalar subgroups satisfy
W_(m+1)=W_m. Elementary layers give depths two, three, and one
at primes two, three, and at least five. Equality then persists.

The strongest unconditional application is the initial relative
pronilpotent base. For R=R_nil(K0), the ACTUAL closed normal group
N=K0/R is pronilpotent, and R=[R,K0]. Its pro-p-prime component
has zero invariants on V_p-dual: first take its coinvariants, then
use the finite p-group action of N_p and Nakayama. Restriction of
any continuous cocycle to the actual pro-p-prime subgroup is a
coboundary by averaging. After subtracting it, normality forces
all remaining values into those zero invariants. This proves the
needed H1 vanishing for every finite abelian residual quotient.
There is no substitution of a finite quotient's cohomology for
cohomology of the retained infinite group.

This theorem controls the actual scalar depth for all such finite
abelian residual layers. It does not produce the desired positive
peripheral action on the stabilized quotient, retain arbitrary
prescribed frames, solve the negative norm equation, or ensure
the cohomology hypothesis after arbitrary nonabelian enlargements.
Those remain separate obstructions to the full involution decision.
