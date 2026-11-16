# Birational-agent continuation after checkpoint 09

This is a continuation record, not an additional numbered theorem. Parent owns
the active paper, register, metadata, builds and durable packaging.

## Completed and audited results

* A.137: independently audited the nonsplit central-extension descent, the
  quartic detector, and the finite local point/cusp pullbacks. The actual finite
  quotient has order `2^136`. Its exact nilpotency class is 17, as proved by the
  covering-graph chain model and the retained certificate. Independently rerun
  output: `code/harmonic_quotient_class_birational_audit_output.txt`.
* A.136: independently audited the harmonic-to-tripod escaping-support map and
  its finite initialization scope.
* A.138: `sections/constant_tower_unit_lift_agent.tex` gives a coherent nonzero
  unit cofactor through the constant pure-three tower. All half-powers are
  explicitly in pro-three completions, not in the full exponent completion.
  Root and local audits and certificate reruns passed.
* A.140: `sections/wild_pure_tower_norm_agent.tex` proves onto actual field and
  unit norms, and compatible local norm fibres, in the specified pure-three
  tower over a three-adic field with no cube roots of unity and a radicand of
  valuation prime to three. It includes the exact old-field embedding after a
  rational radicand update. Root and local audits passed.
* A.144: `sections/successful_radicand_update_agent.tex` gives the exact update
  `q=511177`, `gamma=-68+64*alpha+alpha^2`, `alpha^3=3`,
  `z=alpha*q^8`, and
  `beta=(1-alpha)*(alpha^2-2)*q/gamma^3`.
  The norm of gamma is q, and the norm of beta to Q is -2. The same beta is an
  actual global norm at every finite depth of the changed tower, and has
  compatible local norm families everywhere. Its global inverse-limit fibre
  remains unresolved. Local independent full audit and certificate rerun pass;
  parent is independently auditing/integrating.

The A.144 local q-plan is genuinely two-dimensional: its norm-one cofactor has
`t=(1,1,1)`, `c=(0,2,1)`, while the root-unit characters are `a=(0,1,2)`.
The stable equations are `8*c_i-t_i*a_i=0 mod 3`. The literal identity
`beta*z=(1-alpha)*(3-2*alpha)*(q^3/gamma)^3` supplies the successful cubic norm
test, and the exact stable norm theorem supplies every later depth. At two the
local algebra has a compatible degree-one factor; it is not asserted that all
factors split. Put the target in that factor and one in the remaining factors.

## Further proved constant-tower input (not yet numbered)

Let `K_n=Q(3^(1/3^n))`, `L_n=K_n(mu_(3^n))`. A.138 proves that every L_n and
the intermediate cyclic-step fields have trivial three-primary class group.
The same is true for every subfield F of L_n: the three-primary Hilbert class
field of F base-changes to an unramified abelian three-extension of L_n, hence
lies in L_n; every nontrivial intermediate extension is ramified at three, so
the Hilbert extension is trivial.

Every actual unit norm `K_(n+1) -> K_n` is onto. Set
`F'=K_n(mu_3)` and `E'=K_(n+1)(mu_3)`. This is an actual cyclic cubic
extension, ramified only at its unique three-prime, and its class-group input
is as above. A.138's cyclic unit correction gives a unit eta with norm epsilon.
Its quadratic transfer gamma to K_(n+1) has norm epsilon squared. Thus
`gamma^2/epsilon` has norm epsilon exactly. This also gives onto completed unit
norms. Local_preprint independently checked this proof.

For A.144's q, the prime `P_0` with `alpha mod q=13382` has an infinite
degree-one branch in this CONSTANT tower. Here `v_3(q-1)=1` and alpha on that
branch is a cube. At each step choose the unique root whose residue-unit
three-primary component is trivial. All transition ideal norms have degree
one. Since every prime class has order prime to three, the branch primes have
generators in completed multiplicative groups. Onto unit norms correct their
ratios recursively, preserving the prescribed first generator gamma.

The resulting family begins at gamma in K_1, and its norm to Q is q. It does
not begin at the scalar q in K_1. That scalar has valuation one on the other
two q-primes, whose residue degrees grow without bound; it cannot be a
constant-tower universal norm. Consequently this family alone does not
transport the A.138 family to the changed radicand.

## Finite-S phantom investigation: exact warning

For a finite-support radicand and target, the finite-weight defect is defined
over a fixed finite ramification set S. Its H2 over that finite S is finite.
This does NOT justify declaring its image in full continuous cohomology
separated by finite coefficients. A possible finite torsion contribution must
be checked.

Opened primary source: Grzegorz Banaszak, *Wild kernels and divisibility in
K-groups of global fields*, arXiv:1208.2137v1, 10 August 2012, primary PDF
`https://arxiv.org/pdf/1208.2137`.
Theorem 4.3 identifies the inverse limit of finite-coefficient localization
kernels with the finite group of divisible elements. Theorem 4.5, equation
(74), injects that group into a coefficient lim-one group, with torsion-free
residue quotient by Proposition 4.4. Thus a blanket torsion-free-phantom
argument is unavailable. Its precise application to our mixed finite-weight
module has not been proved here. This source is a scope check, not a claimed
obstruction for A.144.

The tempting abstract coefficient argument is also invalid: if
`C=H^2(G,M)`, the transition on
`C[p^(r+1)]/C[p^r]` induced by multiplication by p is not generally zero.
For `C=Q_p/Z_p` it is an isomorphism. No torsion-freeness of the coefficient
lim-one follows from that shortcut.

## Current exact missing step

A.144 proves every finite global norm fibre is nonempty and every local
inverse fibre is nonempty. A global inverse fibre, actual or completed, has
not yet been produced. A common finite support bound on global completed
norm representatives would give compact fibres, but no such bound has been
established for the changed tower. Its extra q-ramification prevents reusing
the constant-tower class-number argument without an additional proof.

At an unramified unit-radicand prime, A.89's inverse norm-zero divisor kernel
vanishes: only the possible stable degree-one branch survives, and its norm
map is injective. This is the literal reason that unused primes with infinite
linear branches do not by themselves supply norm-zero corrections while the
lower target remains fixed.

Do not infer a completed ordinary ghost or a full metabelian section from
these finite-depth results. The same-pair global compatibility problem remains
the main task.

## A.149: successful compatibility in the inert-eleven changed tower

The later prime-eleven variant now has a complete proof, saved in
`sections/coherent_inert_radicand_update_agent.tex`. Its certificate and output
are `code/coherent_inert_radicand_update_certificate.*`. Root and local source
audits are in progress at the time of this note; the conceptual proof has
passed both stress tests.

Use `gamma=2+alpha`, `z=alpha*11^8`, `a'=3*11^24`, and
`beta=(1-alpha)*(alpha^2-2)*11/(2+alpha)^3`. The norm of beta is -2. At the
quadratic eleven-place, the three characters of alpha, 1-alpha and U are
`1,0,2`; the stable norm equation is `8*2-1=0 mod3`. The linear eleven-place
has no three-primary residue-unit factor. All local norm families therefore
exist compatibly, with the same two-adic branch used in A.144.

The genuinely new global input is the ray group of Q(mu_3) at eleven. Its
residue group has order120, and the global mu_3 kills its whole three-part;
higher ray conductors add only eleven-primary factors. Thus no abelian
three-extension is ramified only at eleven. For any finite Galois
three-extension ramified only at three and eleven, inertia at three normally
generates the group; the maximal-subgroup property of a finite three-group
makes inertia the full group. The Hilbert three-class fields of the radical
and cyclotomic layers are therefore trivial. Every layer has full
decomposition at three.

Here is the precise cohomological consequence used. For a finite module A
split by one of those class-zero layers, a cocycle locally coboundary at all
places of the fixed finite set S restricts to an everywhere-unramified
abelian three-character of that layer. It is zero by the class group. Full
decomposition at three then turns the same local coboundary witness into a
global witness. Finite Poitou--Tate duality gives H2-localization injectivity
for every finite coefficient quotient of the actual module D_z. Over finite
S the finite H1 groups are finite, so the cochain Milnor sequence gives
`H2(G_K,S,D_z)=lim H2(G_K,S,D_z/(3^r,T^r))`. The compatible local norms kill
the defect locally and hence globally in this exact group.

A lift in H1(G_K,S,V_z) then projects, through the actual root-permutation
quotients, to ONE compatible family of completed S-unit norm preimages with
first term exactly beta. Shapiro uses E_j=K'_(j+1), so its unit set is
S_(j+1); this index is explicit in the saved proof. Including Q at level zero
gives `o_pol(3*11^24,-2)=0` via the norm-tower map of A.77/A.81. This solves
the completed global compatibility for that changed example, not for A.144's
different prime511177 and not for an infinite-support ordinary ghost.

Freshly opened primary inputs: Milne CFT V Theorem1.7 (ray class exact
sequence), and Milne ADT I Theorem4.10(a), Corollary4.15 (finite duality and
finite-set finiteness). Their exact maps and the two limits are retained in
the proof. The certificate checks960 local residue conditions and465
derived-to-augmentation coefficient bounds, not the class-field or cohomology
arguments themselves.
