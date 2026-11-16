# For the next Fable round

Queue kept by the main session (Claude Opus 5.5 at effort max). Each item: what to look at, why, and the notes entry it
comes from. Nothing here has been sent. The user decides the round.

- **F1. The general A.3 (base K).**
  - Check the principle "virtually G_{K^ab}-fixed = algebraic Hecke characters of K" against LM8 A.1, A.3, A.4 and A.6.
  - Check the predictions: over Q and over K without a CM subfield, the boundary only; over Q(i), the E-isotypic part.
  - Does it bear on the open tripod-section items (LM7/LM8)?
  - Source: NOTES_20261115 §1.
  - Who: the Longue Marche field, or aec1e030 for the modular side.
- **F2. Kronecker limit formula at the three cusps of the tripod.**
  - Y_0(4) = P^1 minus {0, 1, inf}; lambda and 1 - lambda are eta quotients; Goldstein's cusp-attached eta functions.
  - Question: is the limit formula at a cusp the archimedean counterpart of A.1, with the Kummer classes kappa(a),
    kappa(1 - a) as the l-adic shadows?
  - Source: §5, and Williams Ch. 11.
- **F3. LM's Delta and the eta multiplier.**
  - SL_2(Z)^ab = Z/12, the Rademacher function, the frame {1, 5, 7, 11}, and GT-hat acting through lambda mod 12.
  - Question: is "Delta = 0 on GT-hat" a statement about the multiplier class?
  - Source: §7. Who: the Longue Marche expert's Delta notes.
- **F4. S6 B.4.33 at the cusp of the j-line.**
  - Engel's surface has J of degree 1, so w = 0 is the I_1 cusp.
  - Compare the proof's logarithmic characters and the "q-ghost" map with cusp inertia (Tate curve) and LM8 A.1.
  - Source: §6.
- **F5. A rho-isotypic cosmic Galois group for weight-one cusp forms.**
  - Connes-Marcolli's one generator per degree is the count for the odd rho = 1 + chi_-4.
  - Is there a renormalization-group reading for irreducible odd rho?
  - Source: §3.
- **F6. Stark units of weight-one forms as integral points of the tripod.**
  - D = -23 gives log alpha, with alpha an exceptional unit.
  - When is the Stark unit of a dihedral (or exceptional) weight-one form a solution of u + v = 1?
  - Source: §4.
- **F7. Class field theory as geometry, at level 2, and A.1 as malnormality.** (Notes §11.)
  - Connes-Consani's class field functor: abelian extensions of Q become covers of X_Q, with Frobenius as the monodromy
    of the orbit of length log p and inertia as the isotropy.
  - Is there a level-2 version on the K-lattice space of Connes-Marcolli-Ramachandran, and what in it matches LM8 A.3's
    E-isotypic term?
  - Is LM8 A.1 the arithmetic analogue of the malnormality of peripheral subgroups in hyperbolic (pseudo-Anosov)
    mapping tori?
- **Refinement of F1/F2.** Banerjee-Merel (arXiv 2204.06379) give an analytic criterion, through Eisenstein cycles and
  scattering constants, for cusp divisors on covers of the tripod (Gamma in Gamma(2)) to be torsion: the archimedean
  side of A.3's cusp-divisor term. (Notes §12.)
- **F4, answered by a1bd1599.** w = 0 is the cusp of Alb(S_2)'s j-line, not the base cusp; B.4.33 sits at the corner of
  two commuting inertias. See NOTES §15.
- **F8. S6's Euler number and LM's Delta.** (Notes §15.)
  - S6: p = 12 l_0 - 4 l_1 - 3 l_2 = ±1 is the Seifert Euler number over S^2(3,4) (orders 3 at IV*/j = 0, 4 at
    III/j = 1728, coefficient 12 at the cusp).
  - LM: Delta is the sign at the cusp in a reciprocity with signs at 3 and 4, frames in (Z/12)^x.
  - Questions: is p the Rademacher function (Meyer cocycle) of Engel's monodromies, and does p = ±1 match the frame
    classes {1, 11} (signs agree) under the right orientation? Is the S^6 condition a "Delta = 0" statement for the
    monodromy representation of the S6 family?
  - Who: aec1e030 (Lead 3) together with a1bd1599 (S6), or the LM expert's Delta notes.
- **F9. EXIT_TOWER E.71-E.74 as a ghost.** (Notes §16.)
  - Rose vertex groups are pro-p surface groups of genus g - 2 at every p, so they pass every nilpotent test.
  - What is the non-nilpotent, or profinite-rigidity, test that decides them? Is it the same mechanism as Item 2.4's
    braid ghost?
  - Who: the EXIT_TOWER intake or the LM expert's notes.
- **F10. S6: the AC26 family against CDP's hypotheses.** Does it satisfy them away from the corner (inf, 0), and is the corner exactly where they fail? That would make precise the user's reading that CDP-type methods, which build from a normalized lower-order object, cannot see the family. (Notes §18.)
- **F8, refined (Notes §19).** The S^6 condition p = ±1 is exactly chi_12(Seifert class) = +1 on (Z/12)^x, with the class in H^2(SL_2(Z), Z) via the monodromy. Is the vanishing-circle bundle the circle bundle of lambda^{±1} (the Hodge bundle) pulled back along J? That would make the link with eta geometric rather than a coincidence of (Z/12)^x/±1.
- **F11. Ramanujan's signatures 3, 4, 6 as the common structure.** (Notes §20; sent to aec1e030, 16 Nov ~02:0x UTC.)
  - S6's (3,4,inf) local data, LM's Delta (signs at j = 0 and j = 1728, chi_12), eta's chi_12, E_4^{1/4} =
    2F1(1/12, 5/12; 1; 1728/j), and the elliptic-expansion moonshine at j = 0 (arXiv 2108.01027).
  - Is the S6 period function beta (or tau, mu) a signature-3 or signature-4 hypergeometric period?
- **F8 answered (aec1e030, Ramanujan consult).** The S6 sphere condition is that the vanishing circles form the circle bundle of J*lambda^{+-1} on P(3,4). That is geometric, not a coincidence of the group. Delta stays separate (non-abelian). Items R1-R4: placement pending.

## F12 (16 Nov; NOTES §23) S6: is the w -> 0 obstruction exactly the cusp order of an eta-quotient?
For a1bd1599 (it has read S6_02_PUSH). B.4.19 gives the r-central divisor's component cover y^12 = K,
K = t^4/(t - 1)^3 = E4^12/(1728 E6^6 Delta), so y = 1728^{-1/12} E4/(eta^2 sqrt(E6)); B.4.33's contradiction is the
gamma-winding n of F per r-loop (B.4.33.14). Question: for a general admissible twist (l0, l1, l2) with l1 in
(Z/3)^x and l2 in (Z/4)^x, is the component cover y^12 = t^{4 l1}(t - 1)^{3 l2} (with the cusp term 12 l0), is the
gamma-winding of F equal to -ord_cusp K = p, and does B.4.33 then hold for every such twist (p is prime to 12, so
never 0)? If yes, non-fillability at (cusp, w = 0) is forced by the free actions at the two CM fibres, and the S^6
condition |p| = 1 is the minimal obstruction. Where to look: S6_02_PUSH sections/ab_push_global_partial.tex,
B_global_noncompletion.tex (B.4.31-B.4.33), report l. 49 (untwisted scope check).

## F13 (16 Nov; NOTES §24) The CM-type reading of S6's sphere condition, and the (1,6)-form.
For a1bd1599 (S6), with aec1e030 for the LM side. (a) Check that the local Seifert classes l1 mod 3, l2 mod 4 are the
characters by which Aut(E_rho) and Aut(E_i) act on the vanishing circle (i.e. powers of the CM types), so that
p = ±1 (mod 12) says the two CM types differ by an element of Gal(Q(zeta_12)/Q) fixing sqrt 3. (b) The monodromy
preserves Omega = 6 e1^e4 + e2^e3, a (1,1)-class on every fibre, indefinite exactly on the admissible range D < 0
(Omega^2 = -12): is this in the S6 returns, and does b2(X) = 0 kill it through the Leray d2? (c) How does LM8_PUSH
C.31 (three independent quadratic characters Delta, Delta_D, Delta_D^2 of GT0) sit against chi_-3, chi_-4, chi_12?

## F14 (16 Nov; NOTES §25 (c)) Do GT0's frames act on S6's local twists?
For aec1e030 with a1bd1599. S6's local twists are classes in H^1 of the local inertia (Z/3 at j = 0, Z/4 at j = 1728)
with coefficients in H_1(E) (for Z/3: Z[omega]/(1 - omega), the fixed points of the CM automorphism). Lift the action
of GT0 from the completed modular group to the completed base group Z/3 * Z/4 of S6 (the cover by E6^{1/2}), let it
act on the affine monodromy through its frames, and decide whether an element with central frame class a multiplies
the classes (l1 mod 3, l2 mod 4) by (a mod 3, a mod 4) up to lambda. If so, Delta(Phi) = 1 exactly when Phi carries
the sphere's local data (p = ±1 mod 12) to a lens class (p = ±5): a precise form of F8.
- **F14 answered in the negative (main session, NOTES §25 (e)).** S6's Seifert data are invariants of single cyclic
  local groups and of a circle direction fixed by all the monodromy, so GT0 moves them only through lambda; frames, hence
  Delta, cannot act on them. Left: whether Delta is the level-12 class of the difference between the descended action and
  the tripod action of the j-line (not queued).
- **Wording corrected (NOTES §30 (a)).** "Central frame class" rests on a reading that DELTA_ON_GT cp01 A.2-L1 refutes:
  the frames lie in the centralizers C(R0) and C(S) in SL2(F3), not in the centre. Only the parity pair (a, b) and its
  CRT compression u are defined.

## F16 (16 Nov; NOTES §30 (b), (i), (j); rewritten ~05:1x UTC) S6's corner and the bit 3^{1/4}.
For aec1e030 or a1bd1599. Settled already: the field side is DELTA_ON_GT A.12 (K4^ab ∩ K3^ab = Q^ab(3^{1/4})); and
numerically (49 digits, check_siegel_bit.py) the Siegel value at the order-3 fixed point of E_rho is
g_a(rho) = ± e^{-pi i/12} 3^{1/4} (g^12 = -27) and at E_i[1 - i] it is g_b(i) = -1 + i, so S6's nomes are exactly
q1 = (w/1728)^2 g_a(rho)^12 = -w^2/48^3 and q2 = (w/1728) g_b(i)^6 = i w/216. Questions: (a) prove g_a(rho)^12 = -27
and the value of g_a(rho) exactly (distribution relation, Kronecker limit formula at rho); (b) does S6's level-12 corner
(monodromy I - 12E, component cover y^12 = K) realize the 12th root g_a(rho)/g_b(i) of q1/q2^2, so that a Galois element
acts on the corner's twelve sheets through the Kummer character of 3^{1/4}, the frame parity of DELTA_ON_GT on
G_{Q^ab}? If yes, state the precise sense in which S6's corner carries Delta's bit; if no, say what the corner's 12th
root is instead.
- **(a) and (b) answered ~09:0x UTC by the main session (Claude Opus 5.5 at effort max), NOTES §33.** (a) Proved:
  g_a(tau)^12 = Delta/P'(z_a)^4 for every tau (Klein forms; root of unity checked), so g_a(rho)^12 = -27 exactly;
  g_b(i) = -e^{-pi i/4} f(i)^2 = -1 + i. (b) No in the literal form: B.4.19's y^12 = t^4/(t-1)^3 is the ratio of the
  orbifold root coordinates, branched at the CM points. The bit sits in the corner parameter r: q1 = -2^-12 3^-3 r^12,
  q2 = (i/216) r^6, so q1^(1/12) needs 3^(1/4) over Q^ab and q2^(1/6) does not.
- **Remainder closed ~12:1x UTC by the main session (Claude Opus 5.5 at effort max), NOTES §34.** Yes at the
  order-3 end. By S6_02_PUSH B.1.2 with S6_02 A.1.2, the twelve-cycle there is the I_12 of E_1 = C/(Z + kappa_1 Z),
  and S6_02 A.4.1 says Alb(S_1) = E_1; the Albanese map from the cover is [3], labels i -> 3i, image = R11's four
  components. At the order-4 end it is the I_12 of E_2 = C/(Z + kappa_2 Z), a double cover of Alb(S_2) (I_6). The two
  ends are Tate curves over Q(i)((r)) with parameters c1 r^12 and c2^2 r^12, ratio 27/64; S6_02's d_* is
  -1 + (3i/2 pi) log(3/4) exactly. Galois moves no component; G_{Q^ab} acts on the 12-torsion section q1^(1/12) of
  the order-3 end by the sign of Q^ab(3^(1/4)), and trivially at the order-4 end. Nothing is left for an agent here
  unless someone wants B.4.19's global overlaps tested for an arithmetic identification of the two ends (§34 (c)).

## F17 (16 Nov; NOTES §30 (g)) Two refuted steps in other people's papers: check before anyone is told.
EXIT_TOWER cp16 D.72 (Minahan 2025, the adjacent-descending-link bound used on p. 29; the acyclicity theorem itself is not
refuted) and E.82 (a bounded-injective-path reading of Wilkes, Lemma 4.2). Open both papers, check the construction
against the exact statements, and say whether each is a gap in the paper or a misreading by the run. Only then a draft
to the user ([[informing-authors]]).
- **Added ~05:5x UTC.** EXIT_TOWER cp18 E.83 (Refuted) strengthens E.82: an explicit profinite tree X with edge space Zhat x {0,1}^N, a free, faithful, irreducible Zhat action, exact augmentation sequence, every abstract path component of one or two edges, path quotient (Zhat x [0,1])/((q,1) ~ (q+1,0)); it refutes 'the bounded-injective-path reading' of Wilkes 2018, Proposition 4.3 (E.82 was about Lemma 4.2). Check both against Wilkes's exact statements and proofs: is the bounded-path step used there, or only in the run's reading?

## F15 (16 Nov; NOTES §26) S6's corner obstruction as a gerbe class.
For a1bd1599. B.4.33.14 gives F(s, v + n) - F(s, v) = n gamma - 6n(n - 1) delta per r-loop (w = r^6, monodromy
I - 12E): a Heisenberg cocycle of level 12 in the delta direction, plus the mixed term log w . log s. Is the obstruction
the Dixmier-Douady class of a gerbe on the boundary 3-torus of a corner neighbourhood (q-angle, r-angle, delta circle),
cup product of the r-meridian with a flux class, with level 12 or p? Compare the user's note
Papors/Chatnotes/comprehensive_coupled_gerbe_theta_hesse_landau_paper_final.tex, Prop. meridional-nonextension.
- **F12, F13 (b), F15 answered by a1bd1599** (Claude Fable 5.2 at effort high, 16 Nov ~02:2x UTC, ~25k tokens;
  consults/CONSULT_A1BD1599_S6_CORNER_20261116.md). F12: the integer is p; the general-twist B.4.33 is not checked.
  F13 (b): the form, D_part = (6/pi) log N - (1/pi) log 1728 and the maximum are already proved in S6_02 (D.1.4, C.2.1,
  C.2.3); b2(X) = 0 kills Omega in the Leray sequence by the usual argument once a multiple extends over the special
  fibres (Engel 7.3-7.4). F15: the mixed class is an Euler class of a Heisenberg nilmanifold over the angle torus,
  T-dual to the user's T^3 gerbe; B.4.33 is analytic and global, not a topological non-extension.

## F18 (16 Nov; NOTES §39) ANABELIAN A1 and A.87: check before anyone calls it new or wrong.
For the Longue Marche expert (with the user's OK). ANABELIAN_SUCCESSOR final A.3 claims injectivity of the geometrically
prime-to-p point-section map for every proper curve of genus >= 2 over every finite field. That is the emptiness of
Saidi-Tamagawa's exceptional set E_C (2009, finite; 2017, behaviour under covers) for Sigma = {l != p}, and it answers
the question of cote 149, scans 35-36 ("Il se pourrait qu'on puisse en deduire P = Q"). A.87 refutes full prime-to-p
configuration exactness, even for complex curves; the run says the "cuspidalization literature" disputes or uses it.
Check: (1) literature on E_C after 2017; (2) AG.40-AG.42 (sections in agent_geometric/); (3) which paper asserts full
prime-to-p exactness and whether a published proof rests on it (as with F17, nobody is told before this is checked).
