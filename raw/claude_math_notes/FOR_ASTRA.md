# Candidate items for GPT-6 Astra (ChatGPT Pro mode)

Queue kept by the main session (Claude Opus 5.5 at effort max). These are statements of work, not yet prompts: a prompt
built from them goes through the push-rule lint (claude_tools/push_rule_pro_prompts.py --lint-math) and the user's yes.

- **A1. General A.3.** For a hyperbolic curve X over a number field K and every finite cover Y, determine the part of
  H_1(Y, Q_l) fixed by an open subgroup of G_{K^ab} acting through a cusp-packet section. Prove that it is the boundary
  module plus the parts of V_l Jac(Ybar) on which an open subgroup of G_K acts through algebraic Hecke characters of K
  of weight -1, cut by Weil-orthogonality to the Kummer classes of the cuspidal divisor classes. Corollaries: over Q, and
  over K without a CM subfield, the boundary only; over Q(i), recover LM8 A.3. (NOTES_20261115 §1.)
- **A2. Archimedean regulators of the tripod's Kummer classes.** At CM points tau, compute log|lambda(tau)| and
  log|1 - lambda(tau)| through the eta quotients and the Kronecker limit formula at the three cusps of Gamma_0(4).
  Compare them with elliptic units and with the Stark units of the weight-one forms of the CM field. (§4, §5.)
- **A3 (from aec1e030's Ramanujan consult, R2; for the next S6 prompt).** From the AC26 construction and Engel's
  surface: prove or refute that the base orbifold is P(3,4) with coordinates (E6^{1/2}, E4), that J*lambda = O(1), that
  the vanishing-circle bundle is the circle bundle of J*lambda^k with p = ±k, and that the circle over the cusp fibre lies
  over the torus knot T(3,4); state the sphere condition as k = ±1 and classify the total spaces for the unit classes 5
  and 7. (research_maps_20261114/DEDEKIND_LM8_CONSULT/CONSULT_AEC1E030_RAMANUJAN_20261116.md, R2.)
- **A4 (R1 and the open half of R3; companion).** For each Ramanujan signature 2, 3, 4, 6 (Berndt-Bhargava-Garvan): the
  group, Hauptmodul, weight-one period, the identity x + (1 - x) = 1, the lattice whose theta series is a power of the
  period, every transformation between signatures as a map of curves; and the elliptic-expansion identities at the CM
  points for signatures 4 and 6, which Hong-Mertens-Ono-Zhang say to expect (2F1(1/4, 3/4; 1; z), 2F1(1/6, 5/6; 1; z)),
  with each flat coordinate written through E4, E6 and the Chowla-Selberg period. The signature-2 and 3 identities are
  HMOZ Theorem 1 (published; part (1) also Shen-Zhou 2018), so R3's first half needs no prompt. (NOTES §31.)
- **A5 (NOTES §30 (j), F16).** Prove that the Siegel value at the order-3 fixed point of E_rho is ± e^{-pi i/12} 3^{1/4}
  (g^12 = -27) and at E_i[1 - i] is -1 + i, so that S6's nomes are q1 = (w/1728)^2 g_a(rho)^12 and q2 = (w/1728) g_b(i)^6
  exactly; then decide whether S6's level-12 corner realizes the 12th root g_a(rho)/g_b(i) and so carries the Kummer
  character of 3^{1/4} (Delta's bit on G_{Q^ab}). Waits for F16.
