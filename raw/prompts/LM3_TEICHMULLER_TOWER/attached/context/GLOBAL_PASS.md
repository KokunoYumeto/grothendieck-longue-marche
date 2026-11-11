# La Longue Marche: the global pass over the research notes (Claude, coordinator)

User, 8 Nov 2026: "The idea was you do the second pass during the second pass. Because you have broad knowledge, of all
the nodes, you find which things are worth trying to crack." / "How do the agents know how to develop something when
you do it in bounded prompts? The point was to look at the full structure." The per-package agents only check the
transcription; the choice of what becomes a Pro development prompt is made here, across the whole manuscript.

Sources read: second_pass/NOTES_A_conjectures.md (Grothendieck's conjectures, questions, expectations and programme,
624 notes; checked notes where the package has had its second pass, else Pro's notes), built by notes_by_kind.py
from ALL_RESEARCH_NOTES.md (collect_research_notes.py). Still to read: NOTES_B (unpursued implications), NOTES_C
(unproved claims, model ideas), and the checked notes of P011-P027, which the classifier missed.
Literature status below is from my knowledge, to be checked before any prompt cites it.

## Topics, cote 140-2 (scans 1-575, manuscript pp. 1-292), as read so far

T1. Groups with loops (groupes à lacets): rigidity of the peripheral structure.
- Centralizer and centre triviality, uniqueness of conjugators (scans 53-54, 62; 496: "je cale sur a)", centre of a
  free profinite group; "Consulter Deligne"; centre of Gal and of its open subgroups).
- Normaliser and transporter of the loop subgroups: N_E(L_i) = E_i (84), Trans_E(L_i^d, L_i) = E_i (69).
- Discreteness of the Hom-categories (53).
- "Toute extension sans torsion d'un groupe fini par un groupe à lacets est (canoniquement) un groupe à lacets"
  (353).
- Literature: the centre-freeness of profinite surface groups and of free profinite groups is known; the normalisers
  of inertia are Nakamura's; for the torsion-free extension statement, cf. the profinite Nielsen realisation
  literature (Boggi, Zalesskii and others). To check.

T2. Γ-actions on surfaces and their group data: the 2-functor and the 2-equivalence conjecture (scans 270-306).
- The 2-functor from topological Γ-actions to topos or groupoid data is conjectured to be a 2-equivalence, "i.e. 3
  fidèle" (270-271). Fidelity means Π1^Γ = 1 (288); H^1(Γ, B^0) = 1 (285).
- The realisability criterion (294): a faithful outer action is realisable iff it lifts by drilling holes
  ("forage de trous") to an admissible action whose extension is a group with loops.
- The bijection (∗) Φ(Π,Γ) ← Φ(Π',Γ) ⨿ I'^! (289-290), not proved outside realisable cases.
- The theorem on 304: π_0(SA_{g,ν}) ≅ SΓ^{!+}, (SA_{g,ν})^0 ∞-connected.
- "Le plus agréable serait que ce soit un homotopisme" (281).
- Programme 292-293: cyclic groups acting directly, then by dévissage.
- Literature: discrete Nielsen realisation (Kerckhoff 1983); Earle-Eells; profinite analogues open or partial. This
  is a strong candidate: Grothendieck's 1981 formulation, discrete and profinite.

T3. Teichmüller groups, discretisations and the "conjecture fondamentale" (scans 315-380, 472-479).
- Is T̂ normal in T̂̂ = Outext? The question of 322-323 (one conjecture retracted as "ultra-faux"); T̂⁺ invariant;
  N_Σ = T̂̂ (324, 326).
- Prédiscrét⁺(π) → Prédiscrét⁺(π') bijective (347, 355); Discret(π) → Discret(π') injective (352).
- The "conjecture fondamentale": 𝕀Γ_{g,ν} ≅ Gal(Q̄/Q), Γ_Q → Γ_{g,ν} bijective, the Γ_{g,ν} canonically
  isomorphic (341, 356, 371, 376).
- 479: "l'impression que je peux montrer" that Γ_Q → Γ_{0,3} is an isomorphism, via a Russian's result passed on by
  Deligne. That is Belyi (1979), which gives injectivity; surjectivity is the GT question. 479: the "question
  essentielle" is an algebraic description of Γ_{0,3} and of the admissible splittings.
- Literature: Drinfeld, Ihara (GT, 1990-91), Lochak-Schneps, Harbater-Schneps; GT = Gal(Q̄/Q) is open. Pop (2002):
  Out of the Teichmüller tower in genus 0 is Gal (I/OM). Hoshi-Minamide-Mochizuki on GT. To check.

T4. Faithfulness of Galois actions (scans 496-505).
- Γ → Out(π̂_1(U)) is faithful for an anabelian U (497, 502); also after the quotient by the script T (502).
- Γ → 𝚪_g (g ≥ 2) and Γ → 𝚪_{1,1}: "peut-être est-ce tout à fait faux ?" (504-505).
- Literature: Belyi for (0,3), Matsumoto (1996) for affine curves, Hoshi-Mochizuki for proper curves; the action
  on the profinite mapping class groups (modulo T̂) to check.

T5. Admissible splittings and rational points: the section conjecture in its 1981 form (scans 65, 413, 480-488).
- "Ceci suggère une approche de la conjecture de Mordell" (65): finiteness of conjugacy classes of splittings, g ≥ 2.
  "Idem pour une approche du th. de Fermat" (65).
- Pathological lifts (413); conditions "faisant intervenir les Frobenius" (480); intrinsic description of admissible
  outer actions (480).
- Admissible germs of splittings correspond to the algebraic points of a moduli object (488); distinctness criteria
  for g > 0 and for g = 0 (487); a unique invariant loop structure, "Ce n'est pas la peine" (483).
- Literature: the section conjecture (letter to Faltings, 1983), Stix's book, Koenigsmann, Pop (birational), the
  real case (Mochizuki, Wickelgren), Pop-Stix (p-adic). The 1981 form in LM is earlier and different in detail.

T6. Real structures: anti-involutions, X^σ, and maximal free abelian subgroups (scans 436-470).
- Recover algebraically the position of the points at infinity on the components of X^σ (437, margin).
- Classes distinct in 𝒯_g, and every σ satisfying (4) in one of them (440: "Nous montrerons (on l'espère !)").
- Classification of anti-involutions of a cylinder (457); a group "voisin d'un groupe de tresses" (460).
- "Ce sont peut-être les sous-groupes abéliens-libres maximaux" (470); their normalisers; the strips ("lanières") as
  rank-one groups of a reductive group.
- Literature: Weichold-Harnack classification; Birman-Lubotzky-McCarthy (1983) on maximal free abelian subgroups;
  real section conjecture. Profinite analogues to check.

T7. Type (1,1) and SL(2,Z)^ (scans 505, 511-524).
- Is the arithmetic action on 𝒯̂⁺_{1,1} ≅ SL(2,Z)^ faithful "mod" (505)?
- Lifting through ±1, compatible with Γ (515-516, 522-523).
- Anabelian converse: a Γ-compatible group-theoretic lift comes from a geometric one (523).
- "Je doute qu'il en existe une" (524): the rigidification.
- Literature: GT action on SL2-hat, the two-level relations (Ihara, Lochak-Schneps), congruence subgroup property
  questions. To check.

(140-3, 140-4 and 140-1 follow.)

## Cote 140-3 (scans 1-696, manuscript pp. 293-650): the arithmetic image and the group schemes M_{ρ,σ}

T8. Necessary conditions for an outer automorphism to come from Γ_Q (§41 on; scans 28-130 of 140-3, and the C3
packages).
- Congruence relations on (0,3) and (1,1): are they "de nature arithmétique" or consequences of a purely algebraic
  profinite formalism (54)? "Toute une kyrielle" of conditions (57).
- The triple of involutions and reflections σ_∞, ρ (9-10, 85).
- Only two explicit solutions, u = 1 and u = τ∞: "pas ... d'en construire explicitement une seule" (120).
- Signs ε = ±1 and class field theory: ε' = +1 iff p ≡ 1 (4) (C3 155).
- "je n'ai pas de caractérisation bien plausible à proposer" for Γ_Q in Γ̃ (C3 170, 178, 185).
- The "groupe adélique" of triples satisfying the loop relation (C3 204-205).
- Literature: Drinfeld's GT relations (2-cycle, hexagon, pentagon), Ihara, Lochak-Schneps, Nakamura. Which of
  Grothendieck's conditions follow from them, and which are new?

T9. The group schemes M_{ρ,σ} over Z (C3 207-696).
- Pairs of matrices satisfying the loop relation; the scheme of solutions and its relative dimension (C3 151).
- Group sheaves over Spec Z presented by finite cyclic maps and G_a: "Il est plausible ... vaudrait bien la peine de
  tirer cette question au clair" (C3 336; for SL2 and GL2, orders 4 and 6). Compare Serre's amalgam
  SL2(Z) = Z/4 *_{Z/2} Z/6.
- Uniqueness of the lifts (358), surjectivity of parametrisations (370).
- A systematic construction of "représentations motiviques" from geometric or discrete representations (C3 489).
- Adelic points of a group scheme over Z (C3 546).
- Central extensions by μ_2, their nontriviality, normality of complements (C3 596-605).
- The Brauer class c as a cup product (C3 610-611), "ne peut guère être que Z/4Z" (631), lifts with full image as
  "un exercice plaisant et délectable" of class field theory (634).

## Cote 140-4 (scans 1-280, manuscript pp. 650bis-787)

T10. Unipotent sections and G_a over arithmetic bases (C4 1-41).
- Is a fibrewise unipotent section given by a homomorphism G_a → G (6)?
- The "lemme dubitatif": does integrality of signed combinations of divided powers or exponentials force integrality
  in residue characteristics 2, 3, 5? "un contreexemple ... ou un théorème !" (C4 10-16).
- Smoothness of the parameter scheme, away from residue characteristics 2 and 3 (C4 41).

T11. The level-12 congruence subgroup and the Fermat tower (C4 58-171).
- Level 12 (64), the order 32 (64).
- Relation to "la tour des courbes de Fermat" (95-97, 135-145); "Je n'aurais certes pas suspecté" a splitting (136).
- Γ_Q → an extension of Ẑ* by Ẑ (157). The Kummer-type maps: surjective, or with open image, linearly independent
  for distinct primes (167-170).
- Literature: Ihara (1986, Fermat tower, Jacobi sums), Anderson (hyperadelic gamma), Coleman.

T12. The anabelian yoga for rational points, and Fermat via sections (C4 172-178).
- "Si nous arrivions à prouver l'inexistence de scindages ... autres que ceux à l'infini" (173): Fermat's equation
  via M_{0,3} and N_{1,1}; "Il n'est nullement exclu qu'une analyse assez poussée ... pour tout n ≥ 3" (173).
- Successive Lie (nilpotent) approximations of π_1 and of the extension, each refinement prompting a new study of
  splittings (173, 178).
- Literature: Kim's nonabelian Chabauty (unipotent π_1), Ellenberg's 2-nilpotent obstructions, Wickelgren's
  nilpotent obstructions for P^1 - {0,1,∞}, Deligne 1989. A very strong candidate.

T13. L-groups and Galois-Teichmüller structures (C4 183-247).
- "Il semble que ∀ L-groupe soit isomorphe à un groupe obtenu ainsi" (a finite group acting on a surface, 183).
- Centraliser conditions; characterisation up to non-unique isomorphism (185-186).
- Teichmüller groups defined in this context (187-188).
- Modular multiplicities over Q and Z (193-197): is every such multiplicity a quotient of a smooth quasi-projective
  curve by a finite group? Cf. Behrend-Noohi, uniformisation of DM curves.
- Galois-Teichmüller structures and their axioms (204-208); quasi-unipotent homomorphisms and integral
  one-parameter subgroups (210-221); presentations by generators and relations (231); limiting topos (242-243).

## Cote 140-1 (the draft, 37 scans)

Computations with SL2, Π_{0,3}, central extensions, PM_{11} versus PU_{0,3} (20, 27), and 1 → Z → ? → SL(2,Z) → 1
(29). Mostly local questions feeding T7 and T9.

## Candidate development prompts (first selection, to be revised with NOTES_B/C and the checked notes P011-P027)

Each is one topic of the manuscript, as one long rigorous Pro run, with all of his passages on it collected:
- D1. Γ-actions on surfaces: the 2-equivalence conjecture, the realisability criterion and the torsion-free
  extension statement (T1, T2), discrete and profinite.
- D2. Grothendieck's necessary conditions for the arithmetic image, against the GT relations (T3, T8).
- D3. Fermat and Mordell via sections, in the 1981 form; nilpotent obstructions for Fermat curves (T5, T12).
- D4. The group schemes M_{ρ,σ}: presentations over Z, the "lemme dubitatif", smoothness, level 12 (T9, T10).
- D5. Faithfulness of the Galois actions on profinite mapping class groups (T4).
- D6. Real structures: anti-involutions, X^σ, maximal abelian subgroups (T6).
- D7. L-groups and Galois-Teichmüller structures (T13).
- D8. The Fermat tower and the Kummer-type maps (T11).
- D9. Type (1,1): lifts through ±1, the μ_2 central extensions and the Brauer class (T7, T9).

## Additions from the checked notes of P011-P027 (140-2 scans 101-270, the start of the theory)

- T2, earlier passages: essential surjectivity is "un problème ouvert sur lequel les gens sèchent" (101-102).
  Second pass S08 (270) identifies it as Nielsen realisation, solved by Kerckhoff in 1983; the 2-categorical
  fidelity on top of it is not covered.
- T2: questions c), d) and e) of 197-198. c) π^Γ = 1 for finite Γ ⊂ Aut_lac(π)? d) A unique maximal section
  subgroup, with a proof on 201-203. e) Finitely many classes of lifts? c) and e) are reduced to the realisability of
  cyclic outer actions.
- T2: the invariant μ on finite-order elements (155-160): "J'ignore si cette application μ peut se définir
  intrinsèquement", the central open question there; the torus case (157-158); "forage de trous ... à la fin des
  fins, attaquer !" (160).
- T1: "pas prouvé pour le moment dans aucun cas anabélien profini !" (118, margin), for centraliser triviality.
  Kummer structures and the "conjecture bordélique" (§7; 113-115).
- T6, earlier passages:
  - π^{Γ_s'} = 1 in the arithmetic case (136; second pass N4 gives a weight argument).
  - The bijection question "Cette application est-elle bijective ??" (139), and its component-level analogue for an
    anti-involution, π_0(U^Γ) → classes of sections (148). This is the real section conjecture.
  - Straightening of anti-involutions of a disc (148).
  - "Ça doit être le seul contre-exemple" (179).
- T14 (new). The "topos abracadabra" B_{X,U}: is its cohomology computed "galoisiennement", and is
  H^*(B_{X,U},F) → H^*(X_ét, f^*F) an isomorphism for torsion F (124)? Rejected for genus 0 with locally constant
  coefficients, "Non, à cause du genre 0 !!!" (129). 2-cartesian squares of topoi (166).
- T15 (new). Isotopy and homotopy, arithmetic (231-260):
  - 2-isotopic descriptions by Gr-categories (232-239).
  - Neutrality of a gerbe, "brr!" (240-241: consult Giraud or Breen).
  - Fidelity bounds in terms of dim S, flagged as conflicting (247-248).
  - What a homotopy means arithmetically for forms of P^1: "sans doute un relèvement de u en une section du
    revêtement simplement connexe" (249).
  - The 2-category of Azumaya algebras (250); "bien profond" for simple connectedness (259).
  - Compare A^1-homotopy (Morel-Voevodsky) and étale homotopy. A possible D10.
