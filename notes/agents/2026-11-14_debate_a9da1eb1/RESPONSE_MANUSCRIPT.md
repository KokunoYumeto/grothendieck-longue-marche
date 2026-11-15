# Response, round 2: MANUSCRIPT

By Claude Fable 5.2 at effort max, 14 November 2026, 17:24–17:33 UTC (clock read at 17:24 and at the end). Read for this round: the
user's words (P5041, P5042), the brief, `POSITION_INTAKE.md`, `POSITION_CROSSRUN.md`, `POSITION_FERMAT.md`,
`UNSTUCK_LM_EXPERT.md`, `UNSTUCK_POINCARE_FERMAT.md`, `ASSEMBLY_NOTES_SUCCESSORS.md`, and sections 4.4 and 4.6 of the
moonshine dictionary (the rest of it not read). No literature, no scan, no return. **(mine)** marks my own
statements; hunches are called hunches; "from memory" means not opened. I edited no prompt: the texts of section 3
are for their owners.

## 1. Corrections to my own paper

1. **Stix 2015 (my headline 2 and section 4.2) was overstated.** I wrote that over Q a birationally liftable
   non-cuspidal section comes from a rational point. As I now recall the paper, it proves two things: (i) a
   birationally liftable section has an adelic point that is integral outside a set of places of density 0, or is
   cuspidal; (ii) over totally real and imaginary quadratic fields, *birationally adelic* non-cuspidal sections come
   from rational points, where "adelic" asks integrality at almost all places on every open subcurve. The second
   hypothesis assumes away exactly what is open: the places of density 0. So **D.U4 does not give D.U1**, and B.27 and
   F.15 are not one item. What b) does give is in 2.2 below and in text T2. Astra must open the paper and state
   which hypothesis the theorem has.
2. **Criterion (R) is not mine alone.** The intake found the same statement in the same round (its 4.1), by the
   same two steps (rationality of T over the field of the cover; A.C2.7). Two derivations made without sight of
   each other agree. Neither has been checked by a third reader.
3. Section 2.3 of my paper, "no row states the surjectivity half over cyclotomic bases": stands. Section 7 stands.

## 2. Where I agree and where I do not

### 2.1 A1: the four levers are one principle with three uses (mine)

A collision at P gives, on every prime-to-p Galois cover D with a lift of P rational over k′, a non-zero p-primary
class T in J_D(k′) with a free orbit under the deck group (odd order). Therefore **T dies under every homomorphism
J_D → B over k′ with B(k′)[p] = 0.** The levers are choices of B:

| Lever | B | What it needs | Remark |
|---|---|---|---|
| Intake 4.1 = manuscript (R) | the new part (Prym) of J_D | p ∤ h(D)/h(C) over k′ | then T is invariant under the deck group, against the free orbit: no collision at P |
| Poincaré expert | the Jacobian of a curve X_0 of p-rank zero, through a correspondence | a correspondence that separates P from Q | p-rank zero is "B(k″)[p] = 0 for every k″"; only k″ = k′ is needed, so **ordinary targets with no rational p-torsion over k′ serve as well** |
| A.C2.20 (the run) | a primitive block of p-rank zero | no unit root at all | the special case valid over every field |
| Longue Marche expert, Path 1 | none | — | see below |

- **I disagree with the Longue Marche expert's Path 1 as a proof of A1.** Its last step ("in the abelianized
  fundamental group its class is the class of the point in the Picard group") is class field theory for the *full*
  étale π_1. That statement is true and is the one Grothendieck says survives in characteristic p (scan 35, the
  pro-étale part). A1 is about the prime-to-p quotient, where the abelian level loses exactly the p-primary part of
  the class group. The expert says he had not read the statement of A1. His instruction ("use the points as
  sections at closed points, where class field theory gives a hard invariant") is what (R) does: class field theory
  on a cover in which P splits. His Path 2 (not ordinary in the eigenspace of x − y) is weaker than (R) needs and
  is superseded.
- **With the intake's 4.1 I agree, and add (mine):** (a) the group may be any group of odd order prime to p, not
  only cyclic of prime degree; (b) only the least field over which the cover and the lift of P are defined
  matters, since larger fields only add rational torsion; (c) the group-ring form and the singleton lemma of text
  T1; (d) the closure principle (collisions go up along prime-to-p étale covers and forward along morphisms of
  proper curves), which the Poincaré expert also states in his step 1. The intake's count ("N_b ≡ N_0 + 1") is
  the case "p a primitive root modulo ℓ" of the group-ring form; I did not check its bound p > (2g − 2)².
- **With the Poincaré expert's path 3** (Bogomolov–Tschinkel) I agree; it was my second handle too, from the same
  memory. With (E) of T1 the target need not be supersingular, which makes the existence step easier: any elliptic
  curve over k′ with p ∤ #E(k′).
- The dictionary (4.6) offers no item for A1; nothing to add.

### 2.2 The tripod over Q

- **Ghosts.** The intake's "completed unit equation", the Fermat participant's "a_p → 0 in Ẑ against finite
  support" and the Poincaré expert's "ghost" are one object. I agree with all three descriptions, and with the
  Poincaré expert's [P] that finite ramification of one ρ̄_{s,ℓ} is automatic and the content is boundedness in ℓ.
- **What conjecture b) buys, corrected (mine).** (i) A birational lift makes the local points unconditional: the
  birational p-adic section theorem (Koenigsmann; from memory) replaces the theorem of 6 October for this step.
  (ii) Lifting over a puncture c gives a new class u_c = s^*κ(t − c) in the completion of Q^×, with local components
  x_v − c. Each puncture has its own possible ghost: the primes where x_v is very close to c. If for one rational
  c the class u_c has finite support, then u_c is a rational number r and x_v = c + r for all v, and LM6 E.6
  finishes. So a ghost section that lifts birationally must have a ghost at every rational c. This is statement (G)
  of T2: Stix's theorem without the adelic hypothesis. **Hunch:** (G) is true and is the right arithmetic core of
  D1; the tripod's own two punctures (the completed unit equation) are too few, and I expect, with the intake,
  that infinitely supported solutions exist there.
- **Dictionary M4 (a)** is b) at finite level for five punctures (the harmonic and equianharmonic points). I agree
  with it and note that each added point brings its own ghost test: "avoids those points at almost all places" is
  "no ghost at those c". It belongs with T2's finite-level item.
- **The Longue Marche expert's (iv)** (descent along the cyclotomic tower; "over Q(μ_{ℓ^∞}) nothing is obstructed")
  goes against what the manuscript conjectures: scans 61–63 ask for exactly one fixed point already for Γ°, the
  kernel of the cyclotomic character. On the injective side this is provable from π^{Γ°} = 1 (my 2.3 of round 1).
  So the tower loses nothing for points; whether new sections appear over Q(μ_∞) is an item (T2, B-C).
- The Fermat participant's 1.16 (rank-zero twists) and the Poincaré expert's stacky heights and level-by-level
  ghost classification: no comment from the manuscript; they are the intake's to place.

### 2.3 F.9

- The three hunches differ: the intake (the centralizer condition F.39–F.40 is the criterion), the Longue Marche
  expert (false as an intrinsic statement; true with "the sections of the points are preserved" added), the
  Poincaré expert (no closed answer; an equivalence with the Isom form for genus-0 curves over finite extensions).
- **From the manuscript:** the Longue Marche expert's added condition is the closed-point condition, which his own
  text lacks and his §4 explains (F.1's counterexamples are the valuation sections). The Poincaré expert's
  equivalence is the statement closest to how he works (he reduces everything to P¹ with holes, scans 42, 66–68).
  I take it as the lead item, with the pro-form beside it. The intake's criterion is a statement to prove or
  refute under them. Text T3.

### 2.4 B′

Nobody else addressed it. My finding stands: D.12 and D.14 refute B′ for abstract actions, which he did not
conjecture. Text T4.

### 2.5 Questions put to me

- **Cross-run, cote 143, scan 30 ("structure « locale » éventuelle"):** I have not read cote 143. My readings are
  cote 149 (all), four pages of cote 147, and the sample pages of package 33. The archive reader of cote 143 or the
  Longue Marche expert must answer.
- **Cross-run, fixed loci of finite groups in completed groups:** cote 149 has no such statement. The nearest are
  about torsion and centralizers, and I give them as text T5. Conjectures B and B′ are about fixed points of the
  Galois group, not of finite groups.
- **Fermat, §51.16 (scans 172–178 of La Longue Marche):** not in what I read. For the Longue Marche expert.
- **Intake, the second-pass readings of scans 35–36 and 52:** agreed; they are the ones I used. Two more for the
  companion: scan 36 has "Y′ de X" in the ink (his slip for Y); scan 126 has I_V.

## 3. Texts for the owners

### T1. To the intake: ANABELIAN successor, Part A (the A1 cluster), to stand before its present leads

> **The principle (debate of 14 November; found by the intake and by the manuscript participant independently;
> checked by neither beyond its own derivation).** Let C be smooth, proper, geometrically connected of genus ≥ 2
> over a finite field k of characteristic p, and P ≠ Q in C(k) with conjugate sections for the geometrically
> prime-to-p group. Let k′/k be finite and D → C_{k′} a connected étale Galois cover with group G of order prime to
> p, defined over k′, with a k′-point P′ over P. Then: (a) there are a k′-point Q′ over Q and g ∈ G such that
> T = [Q′ − gP′] is a non-zero p-primary class in J_D(k′) (A.1, A.3); (b) if |G| is odd, δT ≠ T for every δ ≠ 1 in
> G (A.C2.7); (c) h(T) = 0 for every homomorphism h : J_D → B of abelian varieties over k′ with B(k′)[p] = 0.
> Three uses. **(R)** B the new part of J_D: if p does not divide h(D)/h(C_{k′}), then T is G-invariant, against
> (b), and P collides with no point. **(S)** B the Jacobian of a curve X_0 of p-rank zero and h given by a
> correspondence C ← D → X_0: φ_*π^*(P) = φ_*π^*(Q). **(E)** B an elliptic curve over k′ with p ∤ #B(k′), ordinary
> allowed: φ(Q′) = φ(gP′) for every k′-morphism φ : D → B. A.C2.20 is the case where B has no p-torsion over any
> field. In Grothendieck's text this is the reduction of scan 35 (margin: "se ramenant au cas d'un corps fini
> parfait") applied to the covering statement of scan 36.
>
> **Item A-R1.** Prove or refute (a), (b), (c) and (R), for every G of odd order prime to p.
>
> **Item A-R2 (the group-ring form).** For a quotient A of J(k′) of odd order prime to p put
> θ = [0] + Σ_{R ∈ C(k′)} [R − P] in F_p[A]. Prove: in genus two, (R) holds for the cover with group A exactly when
> ψ(θ) ≠ 0 for every non-trivial character ψ of A with values in F̄_p; when A is cyclic of prime order ℓ and p is a
> primitive root modulo ℓ, this fails exactly when the numbers of points in the cosets, with one added for the
> coset of P, are all congruent modulo p. Give the form for every genus (effective divisors of degree ≤ 2g − 2).
>
> **Item A-R3 (existence).** Prove or refute: for every C of genus ≥ 2 over a finite field and every rational
> point P there are k′ and a cover as in (R). Routes, as routes: the count in cosets (the intake's Lead on
> p > (2g − 2)²); the singleton lemma: in genus two, if ℓ is an odd prime with p a primitive root modulo ℓ and
> χ : J(k′) → Z/ℓ is onto with kernel H, then at most 2(|H| − 1) points share a coset with another point (A.C2.21's
> count), so (R) holds for χ as soon as #C(k′) ≥ 2|H| and ℓ > #C(k′); non-cyclic and non-abelian G; (E) with the
> existence of maps to elliptic curves without rational p-torsion.
>
> **Item A-R4 (closure).** Prove: a collision on C gives a collision on every prime-to-p étale cover of C (after a
> finite extension), and its image under any non-constant morphism of proper curves is a collision or a point. So
> the class of curves satisfying A1 over all finite fields contains C when it contains a prime-to-p étale cover of
> C, and contains D when D has a point-separating family of morphisms to curves in the class. List what this
> reaches from A.19, A.29l, A.C2.26. Then prove or refute: every curve of genus ≥ 2 over F̄_p has a prime-to-p
> étale cover with a point-separating family of maps to curves in the class (open Bogomolov–Tschinkel, *Unramified
> correspondences*, and decide the degrees and the cases p = 2, 3).
>
> **Not a route to A1:** class field theory for the full étale π_1 separates points over finite fields at the
> abelian level (C(k) → Pic¹ is injective); that is the statement of scan 35 for the pro-étale part, and A1 is
> what remains when the p-part is removed.
>
> **Checks, never the item:** re-derive A.C2.26 (all 64 classes over F_4) from (R) with the least (k′, ℓ, χ) for each
> rational point; the classes 203/302 first.

### T2. To the intake: SECTIONS_OVER_Q, Part B (birational lifting), to stand at its head

> **His route (cote 149, scans 56–58, 124–127).** "C'est la structure E_L → E_K qui est la plus riche a priori, et
> de loin plus commode pour le genre 0 et 1"; the model form "revient à la forme birationnelle, quand on y précise
> cette dernière en disant que tt scindage de E_U − E_K se remonte en un scindage de E_L − E_K (ou aussi, en un
> scindage de E_V − E_K, si V est un modèle ⊂ U)"; in the function field every section normalizes an inertia group
> I_V of a valuation (conjecture a), scan 126) and lifts exist (conjecture b), scan 127).
>
> **Item B-0.** Open Stix, *On the birational section conjecture with local conditions* (2015), and state exactly
> what it proves for a section of the tripod over Q that lifts to G_{Q(t)}: integrality of the adelic point outside
> density 0, and rationality under which adelic hypothesis. Open the birational p-adic section theorem (Koenigsmann;
> Pop) and state it. Then record, for every row of this prompt that uses local points, whether it needs the theorem
> of 6 October or only these.
>
> **Item B-G (the ghost at every puncture; prove or refute).** Let (x_v) be a point of ∏_v P¹(Q_v) and suppose that
> for every c ∈ Q there is u_c in the profinite completion of Q^× whose image in the completion of Q_v^× is x_v − c
> for every v with x_v ≠ c, ∞. Then (x_v) is one rational number. Decide the finite forms as well: c in a finite
> set S ⊃ {0, 1}; S = {0, 1} is the completed unit equation of Lead L… (decide whether infinitely supported
> solutions exist); find the least S for which only rational solutions remain, or prove there is none. One step
> is immediate and to be written out: if u_c is a rational number for one c, then x_v = c + u_c for all v.
>
> **Item B-L.** Prove for the tripod over Q: [every section lifts to G_{Q(t)}] and (G) imply that every non-cuspidal
> section is the section of a rational point, using the birational local theorem, (G) and LM6 E.6, and not the
> theorem of 6 October.
>
> **Item B-F (finite level; his "forage de trous", scans 58, 66–67).** For a section s of the tripod let Π_s be the
> fibre over s(G_Q) of π_1(M_{0,5}) → π_1(M_{0,4}): an extension of G_Q by a free profinite group of rank 3, "the
> line punctured at 0, 1, ∞ and at the point of s". Prove: s lifts over the puncture c ∈ Q exactly when the point
> section of c on the tripod lifts to Π_s; compatible lifts over all finite sets of punctures give the birational
> lift; the first obstruction is the class of scans 80–82 (the conormal class in Pic) and vanishes by ANABELIAN
> D.23. Then prove or refute that every section lifts over one rational puncture, and over the five points of the
> dictionary's M4 (a), with the ghost test of B-G at each added point.
>
> **Item B-C (cyclotomic base; scans 61–62: "dès que K est ext. de type fini d'un corps cyclotomique").** (i) Prove:
> if two K-points of an anabelian curve have sections that are π-conjugate on G_{K(μ_∞)}, the points are equal
> (from π^{s(Γ°)} = 1 and Th. 3 over K). (ii) Over Q(μ_∞) the points ζ_6 and ζ_6^{-1} of the tripod have x and 1 − x
> roots of unity, so their abelianized sections coincide; verify, and find the first quotient that separates them.
> (iii) Prove or refute Conjecture A for the tripod over Q(μ_∞).

### T3. To the intake: ANABELIAN successor, Part F, to replace the opening of the F.9 item

> **What he wrote, and what is ours.** Scan 52: X ↦ X_ét on reduced schemes locally of finite presentation over a
> locally noetherian S is 1-faithful, and "peut-être pleinement fidèle" once universal homeomorphisms are inverted,
> for morphisms of topoi over S_ét, with no condition on closed points; margin "S de car. 0 ?" (in characteristic p
> the absolute Frobenius and the identity give isomorphic morphisms of topoi). F.1 refutes the full-faithfulness
> half as written, over every field of characteristic 0; the extra morphisms are sections of G_{k(t)} → G_k, which
> his §4 (scans 124–127) describes by valuations. For fields that are not finitely generated he replaces B_K by the
> system (B_{K_i}) over the finitely generated subfields (scans 6–8). Which fields reconstruct (F.9) is our question.
>
> **Item F-a (the equivalence).** Prove or refute: finite-type schemes over k are reconstructed from their étale
> topoi with the closed-point condition exactly when the Isom form of the Grothendieck conjecture holds for
> hyperbolic curves of genus 0 over every finite extension of k; then whether P¹ minus four points suffices.
> **Item F-b (the pro-form).** Prove: for every field k of characteristic 0, morphisms of finite-type k-schemes
> (absolutely weakly normal) are the closed-point-preserving morphisms of the pro-systems of étale topoi over
> finitely generated subfields; so k reconstructs exactly when every closed-point-preserving morphism of étale
> topoi over k descends to a finitely generated subfield. Restate F.37, F.43–F.49 and F.39–F.41, F.47–F.48 in this
> form, and prove or refute that the centralizer condition of F.39–F.40 is equivalent to it.
> **Item F-c (the unpinned morphisms).** For a curve X over k finitely generated over Q, prove or refute: the
> morphisms Spec(k)_ét → X_ét over k_ét are the k-points together with the sections of G_{k(x)} → G_k at non-closed
> points x; under conjecture a) these are splittings of decomposition groups of valuations with residue field
> finite over k.
> **Item F-d (over a base).** Decide reconstruction over S of finite type over Z, with universal homeomorphisms
> inverted and the closed-point condition; say what happens at S = Spec Z.
> **Item F-e (his experiment).** Every outer automorphism of E_K (K the function field of a proper curve X over a
> number field) that respects the "structure à lacets" and commutes with Γ comes from an automorphism of X: name
> the theorems that settle it and whether the hypothesis on the loop structure is needed.
> F.9 stays as the row to which F-a and F-b report.

### T4. To the intake: wherever Conjecture B′ is an item (ANABELIAN successor, D5, or SECTIONS_OVER_Q)

> Conjecture B (scan 59) is for actions "continue[s] dans un sens convenable (sans doute la conv. simple-discrète
> sur les Ū_i finis sur Ū entre Ũ et Ū)". B′ (scan 63) differs from B, in his words, only in that the action is not
> assumed to normalize a group π. **Item.** Define the topology on the semilinear automorphisms of a Poincaré curve
> for which the groups π are open; prove that a continuous action has an open subgroup that normalizes some π, and
> that B′ follows from B over finite extensions (uniqueness of the fixed point of the smaller group makes it fixed
> by the whole group). ANABELIAN D.11–D.14 and LM6 F.41, F.47 are results on abstract actions; record them as such.

### T5. To the cross-run participant: EXIT_TOWER, the caution on the two published proofs, if his words are wanted

> Cote 149 has no statement on fixed loci of finite groups in completed groups. Its statements on torsion: scan
> 14, "les seuls éléments ≠ 1 de Γ_Q d'ordre fini sont les conjugués de τ, conjugaison complexe", with the
> centralizer of τ equal to (1, τ); scan 15, "on admet que dans un groupe profini libre, il n'y a pas d'élément
> d'ordre fini ≠ 1" (margin: "à vérifier"); the margin of scan 28, for a complete curve of genus ≥ 2: "vérifier
> que son π_1 est à centre trivial et qu'il n'a pas d'éléments d'ordre fini".

Nothing for PUSH_ITEMS Part 1, Part 2, LM8_PUSH or PUSH_ITEMS_LM7_CONTINUED: the manuscript calls for no change there.

## 4. Hunches and requests of his that fit no present prompt

For the intake to place in the consolidation; my proposal for each.
1. **Scan 8:** "une description purement algébrique … du pro-pro-groupe fini associé … à (C, C)": the system of the
   Galois groups of all finitely generated subfields of C. Proposal: a row in the list of later prompts; it is the
   pro-form of F-b made absolute.
2. **Scan 50:** the Conjecture fondamentale for spectra of regular local rings essentially of finite type over Q
   (dominant morphisms ↔ open homomorphisms). Proposal: one item in SECTIONS_OVER_Q, Part C (fields), as "prove or
   refute".
3. **Scans 120, 128, 130:** the converse on centres ("A-t-on une réciproque ?"), which valuations give the same
   group Δ_V, and whether a minimal model makes T^{I(x)} → π_{U/K} injective. Proposal: three rows beside LM6
   F.34 and F.6 (higher-dimensional targets), same part.
4. **Scans 99–103**, the good-reduction conjecture: which arrows hold (Oda–Tamagawa, from memory; H_1 alone fails in
   genus 0 with colliding punctures). Proposal: no prompt; a note in the companion and one line in the consolidated
   register stating what Parts B and C of the ANABELIAN return settled.
5. **Scan 36, margin:** Theorem 2 in characteristic p for the prime-to-p groups. Proposal: one row in the
   ANABELIAN successor, Part A, after A-R4 (it follows if A1 holds for products of curves of genus 0, which he
   says is clear).

Context at the end of this round: about 890k tokens (the guard read 876,811 just before this file was written); the step used about 75k of its 80k.
