# Odd relation-module cusp detection and the normalization boundary

Research record; not integrated into the formal thirteenth-hour paper.
The finite cusp-detector argument was independently checked by CE in
the checkpoint12 conversation. The normalization consequence below is
spelled out separately to retain its precise scope.

Write `Pi=C2 amalg C3`, `tau=sr`. Let `q:Pi→Q` be an actual finite
quotient, injective on both named finite factors, with Q noncyclic.
Put `L=ker(q)`, `m=ord(q(tau))`, and for an odd prime p put

`G_p=Pi / closure([L,L] L^p)`.

Then the image in Q of `C_{G_p}(tau)` is exactly `<q(tau)>`.
The group is finite, of order

`|G_p|=|Q| p^(1+|Q|/6)`.

## Proof

The discrete finite-index subgroup underlying L is torsion-free and
is the fundamental group of an oriented surface with punctures. Its
profinite completion is L, by the full induced topology on an open
subgroup. Its cusps are indexed by `Q/<q(tau)>`, their common width
is m, and their number is `r=|Q|/m`. The noncyclic assumption implies
r≥2. The rank of L is `1+|Q|/6`, either by open Kurosh or by the Euler
characteristic of the cover.

The positively oriented boundary classes in `H_1(L,F_p)` have exactly
one linear relation, their total sum. Thus they are distinct: for r≥3
the difference of two standard coordinate vectors is not a multiple
of the all-ones relation, and for r=2 the two classes are opposite
nonzero vectors, distinct because p is odd.

If g centralizes tau in G_p, then it fixes the homology class of
`tau^m`. The deck action permutes the positive boundary classes,
without changing orientation. Their distinctness forces q(g) to
stabilize the cusp coset `<q(tau)>`, hence to belong to that cyclic
subgroup. Conversely powers of tau give every element of that
cyclic subgroup. The order formula follows from the rank calculation.

This also proves the full centralizer identity

`C_Pi(tau)=closure(<tau>)`.

Indeed arbitrary finite quotients may first be refined by the usual
S3 quotient, so that factor-faithfulness and noncyclicity hold. Apply
the finite detector at each such quotient. Compactness of the closed
procyclic subgroup then gives the full assertion. The cusp subgroup
itself is isomorphic to Zhat: its powers have unbounded order at
every prime, as is also immediate from a torsion-free finite cover.

## Exact involution-preserving normalization

Suppose b is a full negative peripheral involution and

`b(tau)=a tau^(-1) a^(-1)`.

The equation `b^2(tau)=tau` gives `z=b(a)a` in the full centralizer
of tau. Write `z=tau^t`. On the one hand

`b(z)=a b(a)=a z a^(-1)`;

on the other hand inversion of the cusp gives

`b(z)=a z^(-1) a^(-1)`.

Thus `z^2=1`, and torsion-freeness of the cusp forces z=1. Consequently

`b'=Inn(a^(-1)) b`

is still an involution and sends tau to its literal inverse.
Replacing a by `a tau^(-u)` changes neither the cusp equation nor
this norm-one property.

If additionally `q(a)` belongs to `<q(tau)>`, choose u with
`q(a)=q(tau)^u`. The replacement then has trivial Q-image, so the
normalization preserves the literal induced Q-action. This is the
exact finite-data condition needed to remove the normalization
hypothesis from an application; it is not automatic in Q itself.

## Consequence for the stored A79 action

Let Q and its fixed positive action be those of A79. If a full
negative involution inducing that Q-action exists without requiring
literal cusp inversion, every cusp conjugator a must have image
outside `<q(tau)>`. Otherwise the preceding normalization preserves
the Q-action and contradicts A79.

At the odd detector G_p, a specified induced negative action which
already inverts tau literally would force q(a) into `<q(tau)>`, and
therefore cannot be the image of such a full involution.

**Unresolved gate:** this argument does not construct an involutory
negative action on G_p above the stored Q-action, with the required
literal cusp value. The actual odd relation-module action must still
be built and checked. Its existence cannot be inferred from separate
normalizer norms, a scalar central refinement, or coprime lifting of
individual finite subgroups. We therefore retain A79's literal-tau
scope in the formal paper and make no new order-preserving-lifting
counterexample from this observation alone.
