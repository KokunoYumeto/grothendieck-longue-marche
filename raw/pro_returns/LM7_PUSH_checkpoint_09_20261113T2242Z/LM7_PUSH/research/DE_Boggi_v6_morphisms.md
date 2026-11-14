# Boggi v6: exact tower comparisons and two local proof issues

This is a primary-source proof audit, not a conclusion that the main theorem
fails. It records the maps that must be retained in any application to E.3.
The finite 3.A6 computation continues independently.

## Primary texts actually read

* Marco Boggi, *Automorphisms of profinite mapping class groups*,
  [arXiv:2011.15075v6](https://arxiv.org/html/2011.15075v6), revised
  22 April 2026, 53 pages. Theorem 6.7 and Corollary 6.24 assert the full
  profinite GT action and the outer-tower action. The exact definitions
  used below are in Sections 2.1, 2.8, 5.2 and Remark 6.2.
* Marco Boggi and Louis Funar, *Automorphisms of procongruence curve and
  pants complexes*, [author PDF](https://www-fourier.univ-grenoble-alpes.fr/~funar/bf_final.pdf),
  Theorem 4.14, printed pages 22--23. This is reference [7] in Boggi v6.

The downloaded v6 PDF/HTML/text are retained in `research/Boggi_v6_source/`.
The current proof audit does not replace either theorem by its older
procongruence version. The hypotheses and arrows of the current version
are being checked directly.

## Admissibility of the annular-complement sewing map

The surface category in Section 2.1 permits the embedding of a pair of
pants into a one-boundary torus obtained by attaching an annulus to two
of its boundary circles. The one-punctured-disc restriction in that
definition does not remove this annular complement. Section 2.8 assigns
the induced homomorphism of relative mapping class groups; it does not
require that homomorphism to be injective.

For the actual sewing map, let the two glued boundary twists be
`tau_1,tau_2` and let the resulting nonseparating core twist be `tau`.
Then both twists map to `tau`, and `tau_1 tau_2^{-1}` lies in the kernel.
This is the explicit noninjective arrow that must be used. Its target
centralizer contains the core twist and the remaining boundary twist.

## Exact inner ambiguity in outer naturality

For an arrow `eta:G -> H`, chosen representatives of two outer
automorphisms obey

    phi_H eta = Inn(c_eta) eta phi_G.

Replacing representatives by `Inn(b_G) phi_G` and `Inn(b_H) phi_H`
replaces the comparison by

    c_eta' = b_H c_eta eta(b_G)^{-1}.

Right multiplication by an element of `C_H(eta(G))` does not change the
same comparison equation. For composable `eta:G -> H`, `theta:H -> K`,
the comparison equations give the exact constraint

    c_(theta eta)^{-1} c_theta theta(c_eta) in C_K(theta eta(G)).

These equations identify the required based coherence data. No claim is
made here that the entire outer tower fails to determine the NTY/BBR
comparison: that question requires all the relevant arrows and their
centralizer equations together.

## Proposition 6.9: the capping image must retain a Weierstrass point

In the proof of Proposition 6.9, v6 identifies the full closed
hyperelliptic group with `B_(2g+1)/<z^2>`. The capping map used in that
paragraph fills a boundary circle centred at a selected Weierstrass
point. Its image fixes that point. Under the Birman--Hilden sphere
quotient, it is the stabilizer of one of the `2g+2` branch points, hence
has index `2g+2` in the full hyperelliptic group. Thus the particular
capping arrow in the printed proof does not have the full group as
its image.

The actual arrows to preserve are

    B_(2g+1)/<z^2> -> Upsilon(S)_[selected Weierstrass point]
                         -> Upsilon(S)
                         -> Gamma_(0,[2g+2]),

where the middle inclusion is the branch-point stabilizer inclusion
and the last arrow has the deck involution as its kernel. This local
typing issue is not a disproof of Proposition 6.9 or Theorem 6.7.

A repair through the full `B_(2g+2)` hyperelliptic presentation is under
separate primary-source audit by the geometry agent. No unverified
presentation or descent assertion is used in the current E.3 results.

## Lemma 6.16: based uniqueness has a visible twist ambiguity

Let `H=P Gamma(S)_(vec sigma)` and let `G_i` be the group obtained by
forgetting the oriented curve `gamma_i` from that multicurve, as in
Lemma 6.16. The twist `tau_(gamma_i)` is central in `H`. Both the identity
and `Inn(tau_(gamma_i))` therefore restrict to the identity on `H`.
They are distinct automorphisms of `G_i`: the twist about the displayed
curve `beta_i`, which meets `gamma_i` once, detects the difference.
Both automorphisms preserve inertia. Consequently the printed
uniqueness assertion for an actual automorphism has this explicit
family of alternatives.

The use of [7, Theorem 4.14] in the uniqueness argument does not remove
this family. That theorem assumes an open subgroup of the whole
procongruence mapping class group. The oriented-curve stabilizer here
is not such an open subgroup. Cutting also retains the boundary
inertia represented by the same twist.

For these explicit alternatives there is an exact global correction:
`tau_(gamma_i)` centralizes every `G_j` with `j != i`, so the local
changes `Inn(tau_(gamma_i)^(a_i))` glue to

    Inn(product_i tau_(gamma_i)^(a_i)).

Thus this exhibited ambiguity is compatible with uniqueness in the
appropriate outer quotient. A full repaired proof would also have to
identify every possible ambiguity, rather than only this family.
That additional classification has not been asserted in this note.

## Scope retained for E.3

Theorem 6.7 is an action on the full profinite groups and Corollary 6.24
is an outer-tower statement. Their use for the based CM comparison
still requires the actual genus-zero, cutting and sewing arrows and
the exact conjugator equations above. The present note supplies no
replacement for the missing full-GT-to-IV comparison. It preserves the
two local proof issues and the exact possible repair maps for further
audit, without changing any accepted finite or profinite certificate.
