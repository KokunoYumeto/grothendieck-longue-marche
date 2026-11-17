# Proposed semisimple closure of the odd relation-module gate

Saved before checkpoint13 freeze. This is a newly derived proof proposal,
sent to root and CE for independent audit. It is not in the formal paper.

## Statement under review

Let q:Pi=C2 amalg C3→Q be a finite quotient, injective on the two factors.
Let b_Q be an involution with b_Q(tau_Q)=tau_Q^-1. Suppose its prescribed
s/r normalizer frames have norm1, giving subgroups V4 and S3 in
E=Q semidirect <b_Q> over the source factors. Let p not divide 2|Q|.
For L=ker q and M=L/Phi_p(L), the proposed conclusion is that the
actual G=Pi/Phi_p(L) admits an involutory negative automorphism above
b_Q, with literal cusp inversion and with lifts of both prescribed
normalizer frames. No claim of a full involution or of simultaneous
compatibility across arbitrary primes/levels is made.

## 1. Exact virtual relation module

The finite Bass--Serre cover gives the exact Q-module sequence

  0 → M → Fp[Q] → Fp[Q/<s>] + Fp[Q/<r>] → Fp → 0.

Thus [M]=[1]+[Fp[Q]]-[Fp[Q/<s>]]-[Fp[Q/<r>]] in K0(Fp[Q]).
Every term on the right is the restriction of an actual E-module.
Use the trivial module for1, Ind_<b_Q>^E(1) for the regular Q-module,
and induction from the given V4 and S3 subgroups for the two vertex
permutation modules. Hence [M] lies in the image of restriction K0(E).

## 2. Positivity in an index-two restriction image

The needed elementary semisimple lemma is: if Q has index2 in E,
p does not divide |E|, and an actual Fp[Q]-module X has its class in
the image K0(E)→K0(Q), then X extends to an actual E-module.

Here is a proposed direct verification, avoiding an unsupported
positivity inference for arbitrary subgroup restrictions. Decompose
Fp[Q] into matrix algebras over finite fields. The outside involution
permutes the simple blocks in orbits of length1 or2.

For an orbit of length2, the crossed-product block is a matrix algebra
whose simple module restricts to the two Q-simples, each once. Thus
the image lattice on that orbit is exactly the nonnegative diagonal
ray after intersection with the positive cone.

For a fixed matrix block M_n(k), its automorphism induces an automorphism
sigma of k of order at most2. If sigma is nontrivial, finite-field norm
surjectivity removes the crossed-product scalar; the simple crossed
block restricts to one Q-simple. If sigma is trivial, Skolem--Noether
reduces the crossed block to M_n(k[z]/(z^2-d)) for some d in k^×.
If d is a square there are two simple E-modules, each restricting once
to the Q-simple. If d is nonsquare there is one simple E-module,
restricting twice to it. Thus on each fixed orbit the restriction
image is either the full integer lattice or twice that lattice, with
the corresponding nonnegative generator supplied by an actual simple
E-module. No difference of inaccessible positive generators is needed.

These block calculations prove the semisimple lemma if all stated
crossed-product identifications are retained. In particular, applying
the lemma merely to an arbitrary subgroup would be unjustified;
the index-two calculation is essential.

### Shorter exact positivity proof supplied by root

The crossed-product classification can be replaced entirely by the
following semisimple induction argument. Let S be a simple Fp[Q]-module.
If S and its outside conjugate S^b are nonisomorphic, then

  End_E(Ind_Q^E S)=Hom_Q(S,S+S^b)=End_Q(S)

is a division ring. Semisimplicity therefore makes Ind S simple, and
its restriction is S+S^b. Frobenius reciprocity shows that every
E-simple whose restriction contains S is this one.

If S^b is isomorphic to S, write

  Ind_Q^E S = direct_sum_i T_i^{n_i}.

Every restriction Res(T_i) is S^{e_i}, and restriction of Ind S is
S^2. Consequently sum_i n_i e_i=2. Every E-simple supported on S
occurs among these T_i, by Frobenius reciprocity. The possible
restriction multiplicities are therefore either all1, or just2.
In either case every nonnegative multiplicity in their integer
lattice is realized by an actual nonnegative sum of these E-simples.
Applying this on all orbits proves the needed saturation lemma.

This short argument uses only semisimplicity, restriction-induction,
and Frobenius reciprocity. It is the preferred proof of Section2;
the preceding block calculation records the independent motivation.

## 3. Preserve the actual boundary vector

Let t=tau_Q, m=ord(t), and r=[Q:<t>]. The span of the positive boundary
classes in M is the Q-module

  P = Fp[Q/<t>] / Fp·(sum of all cusp basis vectors).

This includes r=1, when P=0. The only relation is the total boundary
sum, from the actual oriented finite surface cover. The vector of
tau^m is the class of the identity cusp, up to its fixed nonzero
normalization. Let b_Q act on this permutation module by minus the
natural cusp permutation. Since b_Q(t)=t^-1, this is a well-defined
involutory E-extension of P and sends the actual identity boundary
vector to its negative.

Because p does not divide |Q|, P is a direct Q-summand of M. The
actual quotient M/P has virtual class in the restriction image:
[M] does by Section1 and [P] does by the signed extension. Apply the
index-two semisimple lemma to M/P. Combining the resulting extension
with the signed P extension gives a b_Q-semilinear B on the actual
M with B^2=1 and B a_bar=-a_bar, where a_bar=(1/m)tau^m is the
averaged cusp translation in a splitting G=M semidirect Q.

## 4. Return to the actual group and frames

The exact criterion in odd_relation_module_coprime_gate_13h.md now
constructs the actual automorphism: solve the cusp linear equation
for k, then remove its square by the inner correction -v/2,
v=k+Bk. This retains literal cusp inversion.

The two retained lower norm-one frames lift by normalizer surjectivity
and odd-by-C2 splitting, exactly as proved in that note. This keeps
their lower Q-values and their separate equations. It does not assert
a preselected common transporter, an entire prescribed higher action,
or compatibility of all frame choices across further refinements.

## Audit questions and scope

The key new assertion requiring independent review is the precise
finite-field crossed-product argument in Section2, together with the
actual boundary-module identification in Section3. The relation-module
and boundary exact sequences are genuine source statements, not a
virtual target substituted for the actual quotient. If the argument
passes, it proves a one-step odd relation lift; it still does not give
an order-two lift to the full source or solve either main question.
