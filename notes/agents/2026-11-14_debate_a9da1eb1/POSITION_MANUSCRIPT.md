# Position paper, round 1: MANUSCRIPT

By Claude Fable 5.2 at effort max (the agent that sample-checked the archive packages of cotes 147 and 149 on
13 November), 14 November 2026, 16:46–17:13 UTC (clock read at the start and at the end). The returns are by GPT-6 Astra (ChatGPT Pro mode); what they state
is that model's claim. **(mine)** marks my own remarks; a hunch is called a hunch. Literature named "from memory" was
not opened in this round.

**Headline.**
1. For A1, the manuscript's own reduction ("se ramenant au cas d'un corps fini parfait", scan 35) gives a sharper
   criterion than A.C2.20 **(mine, six-line proof below, to be checked)**: a collision at P is excluded by one
   P-split cover of odd degree prime to p whose relative class number is prime to p. Only the p-torsion *rational
   over the field of the lifts* matters; the run asked for p-rank zero of the whole block.
2. Over Q, his conjecture b) (birational lifting, scans 57–58 and 127) implies Conjecture A by Stix's theorem of
   2015 (from memory). LM6 B.27 and F.15, ANABELIAN D.U1 and D.U4, are then one item, and his route to it is b).
3. F.9 is our question, not his. Scan 52 read literally is refuted by F.1, and the counterexamples are the valuation
   sections of his own §4. For fields that are not finitely generated his text gives a different answer (scans 6–8).
4. Four attributions and five readings need correcting (section 7).

## 1. What I read

- The user's words and the brief; `INTAKE_ANABELIAN_149_FINAL_20261114.md` and `INTAKE_LM6_FINAL_20261114.md`, in full.
- **Cote 149, all 136 scans, in the second-pass text** (`second_pass\out\MPL_149_001-090\` and `…_091-136\`, the
  per-scan files), read once from first to last in a rendering made by script that shortens the markup and keeps
  doubts, deletions, insertions and margins. Scans 036 (lower half) and 126 (lower third) looked at in the ink.
- The two registers, by rows: ANABELIAN A.1–A.3, A.8, A.28, A.30, D.3, D.11, D.12, D.14, D.19, D.23, D.25, D.26,
  D.U1, D.U4, F.1, F.9; LM6 B.27, D.8, F.6, F.15, F.24: statements (cut at 300–1,000 characters), the
  manuscript-passage columns, and text searches over statements and notes for a few themes (named where used).
- **Not read:** any proof of the returns; the reports; the handoff; the second pass's change lists and
  `notes_checked` files; cote 147 (no row I saw cites it); the prompts. Where I say "no row has it", that is a text
  search of statements and notes, not a reading of the proofs.

## 2. What he says, and what the runs make of it

### 2.1 Scans 32–36: Theorem 3 and characteristic p (A1, A2)

What the text says, in order:
- Th. 3 (scan 32): for X of finite type over K (finitely generated over Q), embeddable in an extension of an
  abelian variety by a torus, the maps (*) X(K) → π-conjugacy classes of splittings and (**) X(K) → splittings of
  the abelianized extension are injective. The proof is Kummer plus Mordell–Weil: G(K) has no infinitely divisible
  element.
- Scan 34: all ℓ are needed; "si on omet p, alors la translation par un point d'ordre p donne un contre-exemple".
- Scan 35: with the pro-étale part of H_1 (he inverts finite radicial surjective morphisms, "quasi-variétés") the
  statement survives in characteristic p; margin: "O.K. en se remplaçant d'abord K par un [anneau] de type fini sur
  F_p, puis en se ramenant au cas d'un corps fini parfait." Then: for the groups "premiers à p", (**) is false
  already for an elliptic curve with a point removed, and "il est cependant possible que l'injectivité de (*) reste
  valable sans hyp. de caractéristique".
- Scan 36: for two morphisms f, g with the same prime-to-p π_1, P = f(x), Q = g(x): Q − P is p-torsion in the
  generalized Jacobian, and for every finite étale Galois cover Y′ of degree prime to p, pointed by P′ over P, some
  Q′ over Q has Q′ − P′ p-torsion in G_{Y′}. "Il se pourrait qu'on puisse en déduire P = Q." A struck line just below
  had tried the abelian covers by isogenies _nG first. Margin: Th. 2 stays true in characteristic p for the
  prime-to-p groups, because Y can be taken a product of curves of genus zero.

Against the runs:

| Point | The runs | Verdict (mine) |
|---|---|---|
| A1 = injectivity of (*) for the geometrically prime-to-p group | A.30, with A.8: reduced to smooth proper curves of genus ≥ 2 over finite fields; genus zero and affine genus one decided | Read rightly. The reduction to finite fields is his margin on scan 35. His own test case (the punctured elliptic curve) is among the decided ones. |
| A2 = the covering condition of scan 36 | A.3: equivalent to equality of the sections | Read rightly. The ink has "Y′ de X", a slip for "de Y" (P′ lies over P ∈ Y); the run's reading is the only one that makes sense. |
| "p-torsion" | "p-primary torsion" (A.1) | Same thing: he writes "d'ordre une puissance de p" three lines earlier. |
| The struck line on abelian covers | A.C2.20, A.C2.23: cyclic covers suffice when a primitive block has p-rank zero; abelian towers add nothing | The run's criterion lives one level above what he struck: an abelian cover D, then the Jacobian of D. Nothing is read into him. |
| Margin: Th. 2 in characteristic p | no row found by a search of the A rows for his Theorem 2 | Not taken up as a statement. It is a claim of his with a two-line reason; worth one row. |
| The pro-étale part ("relèvements radiciels") | no row | Over a finite field, with the full étale π_1, the abelian level already separates points: this is class field theory (C(k) → Pic¹ is injective). The prime-to-p question is exactly what class field theory leaves. **(mine)** |

### 2.2 Scans 41–52: full faithfulness (F)

- Scans 43–45, fields: a morphism B_{K′} → B_K over B_Q comes from K ⊂ K′ iff E_{K′} → E_K has open image. His
  condition c) (anabelian) is "pas assez fort"; he corrects it to c′) with E° (kernel of the cyclotomic character) and
  draws the consequence that every section of E_K over an open Γ′ has π_K^{Γ′°} ≠ 1 when K is transcendental.
- Scan 48, models ("Conjecture fondamentale"): for V regular of finite type over Q and U elementary anabelian, an
  outer homomorphism f: E_V → E_U over Γ_Q comes from a morphism V → U iff f|E_V° is anabelian, that is, the image
  of *every open subgroup* of E_V° has trivial centralizer. For V a point this is: the sections whose Γ°-part has
  trivial centralizer are the rational points (his "sections admissibles", scan 66). LM6 B.27 ("zero cyclotomic
  centralizer") is this statement. Read rightly; the register should keep "every open subgroup".
- Scan 49: the two consequences are "d'apparence opposée" (π^{Γ°} ≠ 1 for fields, = 1 for points of models), and he
  announces a study of their relation. The relation is conjecture b) of scan 127: a point section lifts to the
  function field, where its fixed group is an inertia group I_V, which dies on the model. No run says this in so
  many words.
- Scan 52: X ↦ X_ét on reduced schemes locally of finite presentation over a locally noetherian S is 1-faithful, and
  "peut-être pleinement fidèle" after inverting universal homeomorphisms; margin "S de car. 0 ?"; an experiment
  proposed: every outer automorphism of E_K (K the function field of a proper curve X over a number field) that
  respects the "structure à lacets" and commutes with Γ comes from an automorphism of X.

Against the runs **(mine)**:
- **The margin "S de car. 0 ?" is about Frobenius.** In characteristic p the absolute Frobenius and the identity of X
  induce isomorphic morphisms of étale topoi, so 1-faithfulness on reduced schemes fails over every S of
  characteristic p unless universal homeomorphisms are inverted first. The intake reads the margin as a general
  doubt.
- **His statement is the "relative-only" one**: morphisms of topoi over S_ét, with no condition on closed points.
  F.1 refutes exactly that over every field of characteristic 0, by a tangential splitting G_k → G_{k(t)}. So F.1 is
  a refutation of scan 52 as written, and the companion should say so. The counterexamples are not foreign to him:
  they are the sections of E_L over E_K attached to valuations, the subject of his §4 (scans 124–127), written after
  scan 52. His conjecture a) there says they are *all* the extra morphisms. The closed-point condition of
  Carlson–Haine–Wolf is, in his language, "V has its centre at a closed point with trivial valuation".
- **Inverting universal homeomorphisms** is the category in which Carlson–Haine–Wolf work (absolute weak
  normalization, F.1's wording). Read rightly.
- **F.9 reads more into him than is there.** He never asks which fields reconstruct. His base is Q or finitely
  generated over Q ("il est essentiel ici que le corps de base ne soit pas quelconque", scan 42), and for other
  fields he says at once that B_K is the wrong object: "le 2-foncteur K ↦ B_K … est cependant loin d'être fidèle",
  and one must take "le système projectif des B_{K_i}" over the finitely generated subfields, which "va avoir toutes
  les propriétés de fidélité" of the finitely generated case (scans 6–8). The failures found by the run (Q̄, real
  closed fields, the henselian fields of F.47–F.48) are fields where the limit forgets the system.
- **Not taken up by any row I found:** the statement over a base S (the intake says so too); the experiment with
  the "structure à lacets" (no hit for "lacets" or "loop structure" in the ANABELIAN register); the pro-system.

### 2.3 Scans 53–63: Conjectures A, B, B′

- Proposition of scan 54 and its gap: cuspidal packets at two different cusps are distinct "sauf pour le type (0,3),
  qui mérite un examen approfondi" (filling two holes of the tripod leaves type (0,1)). He gets out by admitting
  π^{Γ°} = L_i, "à énoncer parmi les conjectures-clefs". So the tripod is the one case his elementary argument does
  not reach, and the fixed-group statement is what closes it. If our CYCLOTOMIC_KERNEL statement holds (LM6 F.1,
  F.7; not read by me), this gap of the manuscript is closed.
- Conjecture A (scan 56) with the two precisions in the margin: π^{Γ°} = 1 for points, π^{Γ°} = L_i for cusps. D.U1
  is Conjecture A for the tripod over Q. Read rightly.
- Scans 56–58: for the function field L the sections "se grouperaient par paquets" by the conjugacy class of the
  centralizer of Γ°; "c'est la structure E_L → E_K qui est la plus riche a priori, et de loin plus commode pour le
  genre 0 et 1"; "la forme modélique … revient à la forme birationnelle, quand on y précise cette dernière en disant
  que tt scindage de E_U − E_K se remonte en un scindage de E_L − E_K (ou aussi, en un scindage de E_V − E_K, si V
  est un modèle ⊂ U)". This is F.15 = D.U4, already here for curves, with its finite-level form.
- Conjecture B (scan 59) asks for an action "continue dans un sens convenable". B′ (scan 63) is introduced with:
  "La différence avec la conjecture B, que celle-ci renforce, c'est qu'ici on ne suppose *pas* que l'action de Γ sur
  U normalise l'action d'un groupe profini π". Continuity is not dropped.
  - D.12 and D.14 use "exactly abstract semilinear actions, without a hidden continuity assumption" and refute B′
    for them. **That refutes a statement he did not make.** D.12's action comes from a discontinuous section.
  - **(mine)** With any topology on the automorphisms of the Poincaré curve in which the groups π are open, a
    continuous action has an open subgroup Γ′ that normalizes some π, so B′ follows from B over finite extensions
    (uniqueness of the Γ′°-fixed point makes it Γ-fixed). B′ then says: the choice of π is irrelevant. To be written
    as a row and proved; it replaces "B′ refuted" in the companion.
- Scans 61–62: "je me demande … si ces énoncés ne devraient pas être valables … dès que K est ext. de type fini
  d'un corps cyclotomique". **(mine)** The injectivity half reduces to number fields: if two points x, y over K have
  sections that are π-conjugate on Γ°, the conjugating element is unique because π^{s(Γ°)} = 1, hence Γ-equivariant,
  hence the sections are conjugate over Γ and x = y by Th. 3. The abelian level alone fails there, for the same
  reason as in characteristic p: over Q(μ_∞) the points ζ_6 and ζ_6^{-1} of the tripod have x and 1 − x roots of
  unity, which are divisible, so their abelianized sections coincide. The surjectivity half (Conjecture A over
  cyclotomic bases) is asked by him and, as far as I found, stated by no row.

### 2.4 Scans 64–104: families, specialization, bad reduction

- Scans 70–78 (a rational section extends iff its group section kills inertia), 79–85 (the class of
  1 → T → N(L_i) → E_S → 1 is the class of the conormal bundle in Pic(S); the geometric splittings form a
  G_m(S)-subtorsor that the profinite description should characterize), 85–99 (a section over K gives sections over
  every residue field; of the second kind where the rational section meets the boundary). LM6 F.24 is his question
  of scan 85. Read rightly.
- Scans 99–103, "Conjecture-à-tout-hasard": a) good reduction ⇔ b) inertia acts trivially on π ⇔ c), d) trivially
  on H_1. **(mine, from memory)** a) ⇔ b) is the criterion of Oda and Tamagawa. c), d) ⇒ a) is false: trivial
  action on H_1 with bad reduction occurs for stable reduction of compact type, and in genus 0 whenever two
  punctures collide. His own margin on scan 103 points at the second case ("la multisection … n'est pas étale. Le
  cas du genre 0 devrait être particulièrement aisé à regarder"). Parts B and C had their intake earlier; the
  consolidated register should say which of a)–f) the run settled and how.
- Scans 103–104: he tried to build non-geometric *effective* actions out of geometric outer ones by bad reduction
  and "n'arrive pas par cette voie". That is his evidence for Conjecture A.

### 2.5 Scans 105–136: valuations (§4)

- Conjecture a) (scan 126): every section of E_L over E_K normalizes an **I_V** for a valuation ring V with residue
  field algebraic over K, V unique, and comes from a section of N_V. The ink has I written over N; the margin of
  scan 127 ("À nouveau se pose la question si N_V = Norm(I_V)") and the formula E_L^{(E_K°)} ≃ I_V settle it. LM6
  F.15 notes that "finite residue field" is needed; he inserted "fini" himself on scan 124.
- Conjecture b) (scan 127): every section of E_U over E_K lifts to E_L. The V ∩ L_1 argument of scans 125–126 is
  used rightly by LM6 F.15.
- Questions of §4 with no row that I found: the converse of scan 120 ("A-t-on une réciproque ?": if I_{x′} → E_U
  is trivial, V has a centre on U); scan 128, "dans quelle mesure des V distinctes définissent-elles des Δ_V
  distinctes"; scan 130, whether a "modèle minimal" X ⊃ U makes T^{I(x)} → π_{U/K} injective (his counterexample by
  blowing up a point of D is right: the loop around the exceptional divisor equals the loop around D).

## 3. What it means

**(mine)** The manuscript has one mechanism and three places where it is under strain.

- The mechanism of §1 is abelian: Kummer theory plus the absence of divisible elements. It breaks in the same way in
  the two variants he raises: for the prime-to-p groups in characteristic p (the p-primary torsion is invisible) and
  over cyclotomic fields (the roots of unity are divisible). In both he expects the non-abelian statement to hold.
- What rescues the cyclotomic case is a fixed-group statement (π^{Γ°} = 1, 2.3). What the run found for
  characteristic p is of the same kind: the torsion class T = Q′ − P′ has a *free* orbit under the deck group
  (A.C2.7). The run then asked the deck group to act trivially on all p-torsion of the cover. The manuscript's
  margin says to go down to a finite field first, and there only the *rational* p-torsion can carry T (section 4.1).
- For sections over Q the manuscript does not attack models directly. It passes to the function field, where
  sections are valuations, and it names the passage: conjecture b). Over Q that passage is the whole problem
  (section 4.2).
- For full faithfulness his statement is false as written and his own §4 says by how much. The honest form of scan
  52 has valuations on the scheme side, or a closed-point condition on the topos side.

## 4. Where we are stuck and how to get unstuck

### 4.1 A1

**What is going on (mine).** Over a finite field k a section is a lift of Frobenius, and a collision says that P
and Q lie in the same Nielsen class of Frobenius in the prime-to-p homotopy type. In every finite cover to which
the common lift descends, the lifts P′, Q′ are both rational and differ by a p-primary class. The question is whether
that class can survive in all covers.

**Criterion (R) (mine; to be checked line by line).** Let C be smooth, proper, geometrically connected of genus
≥ 2 over a finite field k of characteristic p, and P ∈ C(k). Let k′/k be finite and D → C_{k′} a connected étale
Galois cover whose group G has odd order prime to p and is defined over k′, in which P splits completely. If
p does not divide h(D)/h(C_{k′}) (class numbers over k′), then no Q ≠ P in C(k) has a section conjugate to that of P.

Proof. (1) E_D for the geometrically prime-to-p groups is the open subgroup of E_C (the kernels agree because
[π_C : π_D] is prime to p). (2) If s_Q = γ s_P γ^{-1}, restrict to G_{k′}: s_P lands in E_D at a rational lift P′, so
s_Q lands in γE_Dγ^{-1} = E_D at a rational lift Q′, and s_{Q′} is π_D-conjugate to s_{gP′} for the image g of γ in
G. Put P″ = gP′. (3) By A.1 on D over k′, T = Q′ − P″ is a non-zero p-primary class in J_D(k′). (4) |G| is prime to
p, so T = T_0 + T_1 with T_0 = e_triv T invariant under G and T_1 in the new part, both rational over k′ because G
is. The hypothesis says the new part has no k′-rational p-torsion, so T_1 = 0 and δT = T for every δ ∈ G. (5) For
δ ≠ 1 this gives δQ′ + P″ ∼ Q′ + δP″, two distinct effective divisors of degree 2, so D is hyperelliptic, and a free
automorphism of odd order is impossible: this is A.C2.7. ∎

Remarks **(mine)**.
- For a cyclic cover of prime degree ℓ given by a character χ of J(k′) (class field theory: the P-split unramified
  abelian covers over k′ are the quotients of J(k′)), h(D)/h(C) = N_{Q(ζ_ℓ)/Q} L(χ, 1). In genus two
  L(χ, 1) ≡ 1 + Σ_{R ∈ C(k′)} χ([R − P]) modulo p. So in genus two: **P collides with nobody as soon as some
  character χ of odd prime order ℓ ≠ p of some J(F_{q^r}) has N(1 + Σ_R χ([R − P])) prime to p.**
- A.C2.20 asks that the block have no unit root at all, which is rare (conductor 2454499369 for the classes
  203/302). (R) asks that no unit root be ≡ 1 modulo a prime above p, over one field; for a block with p of order
  o modulo ℓ this fails with probability about p^{-o}. The existence statement becomes a generic event.
- No row of Parts A and D mentions class numbers, rational p-torsion over the field of the lifts, or complete
  splitting (text search). So I take (R) to be absent from the return.
- **Hunch about the truth:** A1 holds. A collision at P would force p to divide the relative class number of every
  P-split odd cover over every finite extension, a divisibility with no source.
- **Second handle (mine):** collisions go up along prime-to-p étale covers and forward along morphisms of proper
  curves. So the class of curves satisfying A1 over all finite fields contains C whenever it contains a prime-to-p
  étale cover of C, and contains D whenever D has a point-separating family of morphisms to curves in the class.
  Seeds: A.19 (hyperelliptic, p odd), A.29l, A.C2.26. A.C2.20 and (R) may be applied anywhere in the prime-to-p
  tower, not only to cyclic covers of C itself. For the universal statement this route needs a theorem on
  unramified correspondences over F̄_p of the kind Bogomolov and Tschinkel proved for hyperelliptic curves (from
  memory).

### 4.2 The sections over Q (B.27 = D.U1, F.15 = D.U4)

**What is going on (mine).** The runs treat "every non-cuspidal section is a point" and "every section lifts
birationally" as two open rows. Stix (Invent. Math. 2015, "On the birational section conjecture with local
conditions"; from memory) proves that over Q, and over totally real and imaginary quadratic fields, every
birationally liftable non-cuspidal section of a hyperbolic curve comes from a rational point. No row of Parts A
and D of the ANABELIAN register contains "totally real" or "imaginary quadratic", although D.19, D.25, D.26 cite
Stix. If the theorem is as I recall, then over Q **D.U4 ⇒ D.U1**, and since points and cusps lift, the two rows are
equivalent. The manuscript says the same: the model form "revient à la forme birationnelle" once b) is added.

**Route.** Prove b) at finite level: lift a section s over one more puncture, compatibly; compactness gives the
birational lift. D.23 (cuspidally central lifts for every puncture divisor) is the first step. His scans 79–82
compute the first obstruction as a class in Pic.

**Hunch (mine).** Use the fibration M_{0,5} → M_{0,4}. For any section s of the tripod, the fibre Π_s of
E_{0,5} → E_{0,4} over s(Γ) is canonical: an extension of Γ by a free group of rank 3, "the line with four
punctures 0, 1, ∞, x_s" for a point x_s that may not exist. s lifts over the puncture x exactly when the point
section of x on the tripod lifts to a section of Π_s. So b) for s says: the virtual curve U_s carries the sections
of all rational x. D.30's Legendre representation is the H^1 of the double cover of U_s. The item is then: an
extension Π_s that is locally everywhere the group of a four-punctured line (D.6, D.25) and carries all rational
point sections is the group of a four-punctured line.

### 4.3 F.9

**What is going on (mine).** F.42 says no criterion exists in the Galois group with its cyclotomic character; the
run stopped between sufficient and necessary classes. The manuscript's framing explains the shape: for a field k
that is not finitely generated the object carrying the information is the pro-system (B_{k_i}), and
reconstruction over k in that sense follows from the finitely generated case. F.9 is then the question for which k
every closed-point-preserving morphism of étale topoi over k descends to a finitely generated subfield. The
failures are limits that forget their system (Q̄ = ⋃ number fields, F.44; the henselian fields, limits of finitely
generated fields with a compatible valuation). **Hunch:** there is no clean arithmetic classification, and the
statement worth proving is the pro-form plus the relative form over a base, which is what he asked.

## 5. What Astra should grind next

Each item is the whole task. Background: the ANABELIAN return's `sections\` for Part A, D, F with its register;
the LM6 paper for B, D, E, F; the second-pass text of cote 149 (scans 32–36, 41–66, 79–85, 99–104, 119–131).

1. **(R).** Prove or refute criterion (R) as stated in 4.1, for every finite group G of odd order prime to p. Then
   prove or refute: for every C of genus ≥ 2 over a finite field and every P ∈ C(k) there are k′ and D as in (R).
   Record, for each of the 64 genus-two classes over F_4 and each rational point, the least (r, ℓ, χ) that satisfies
   the genus-two form, with the L-polynomials; these are checks of (R), not the item.
2. **The closure principle** of 4.1 (up along prime-to-p étale covers, forward along morphisms), proved, and the
   list of curves it reaches from A.19, A.29l, A.C2.26; then prove or refute that every curve of genus ≥ 2 over
   F̄_p has a prime-to-p étale cover with a point-separating family of morphisms to curves in the class.
3. **Stix's theorem against D.U4 and D.U1.** Open the paper; state exactly what it gives for the tripod over Q;
   prove or refute "D.U4 ⇒ D.U1 over Q". Then prove D.U4 at finite level from D.23, in the form with Π_s of 4.2.
4. **The cyclotomic base** (scans 61–62): the injectivity statement of 2.3 with its proof; then prove or refute
   Conjecture A for the tripod over Q(μ_∞).
5. **Scan 52 as he wrote it:** (i) the pro-form of reconstruction over an arbitrary field of characteristic 0;
   (ii) reconstruction over S of finite type over Z with universal homeomorphisms inverted and the closed-point
   condition; (iii) the experiment with the "structure à lacets", with the literature that settles it named;
   (iv) that the non-pinned morphisms Spec k → X are exactly the sections of his conjecture a), for X a curve.
6. **B′ with continuity:** define the topology, prove B′ ⇐ B over finite extensions.
7. **The scan-36 margin:** Theorem 2 in characteristic p for the prime-to-p groups.

## 6. Prompt changes

I changed no file. Proposals for the owner of the two successor drafts (intake and register):

- **ANABELIAN successor, A1:** put (R) first among the routes, with its proof to be checked, the genus-two form,
  and the existence statement; add the closure principle; keep A.C2.20 as the special case "no unit root". Say that
  the census over F_4 is to be re-derived from (R) as a check.
- **ANABELIAN successor, F:** replace the item F.9 by item 5 above; keep F.9's classification as a row to which
  results are reported; state that scan 52 as written is refuted by F.1 and that §4 describes the counterexamples.
- **ANABELIAN successor, D5 / B′:** restate with his continuity (item 6); D.11–D.14 and LM6 F.41, F.47 stay as
  results on abstract actions.
- **SECTIONS_OVER_Q:** one main item, "D.U4, hence D.U1 by Stix", with the finite-level form and Π_s as routes
  beside the intake's routes (i)–(iii); add item 4 (cyclotomic base); cite cote 149 scans 57–58 for b), not only
  scan 127.
- **Both:** the attribution fixes of section 7.
- **Companion to cote 149** (not a prompt): notes on scans 35–36 (the margin and (R)), 45, 52 (Frobenius; F.1),
  54–55 (the (0,3) gap), 59 and 63 (continuity), 99–103 (which arrows hold), 126 (I_V).

## 7. Attributions and readings to correct

Attributions:
- LM6 D.8, "approche de la conjecture de Mordell, scan 65": the register says cote 140-2 (§8, folio 30v). Scan 65
  of cote 149 is the passage on sections of E_{U_S}; "Mordell" occurs in cote 149 only as Mordell–Weil (scans 34, 81).
- LM6 B.27 cites cote 140-2 (§§8–9, 32, 34); the cote 149 form is scan 48 with V a point and scan 66.
- "B′ refuted" (intake 3.1): refuted for abstract actions only; his B′ is continuous.
- F.9 "his question of scan 52": his question is the statement over S and the experiment; the classification of
  fields is ours.

Readings (second-pass text against the ink):
- Scan 36: "Y′ de X" is what the ink has; it is his slip for "de Y".
- Scan 126: "normalise un I_V" (I over N).
- Scan 52: "au dessus de X_ét" in the first sentence is a slip for S_ét, which he writes two lines later.
- Scan 45, the composite E_{K′} → Γ → Ẑ*: on 13 November I found the circle on this E blotted out in the ink; the
  second pass marks it doubtful. With the circle the definition of E°_{K′} is circular; without it, it is right.
- Scan 45, "la conjecture initiale … corrigée": I read "revue et corrigée" (the same phrase stands on scan 50);
  the second pass keeps "ainsi corrigée". No mathematics depends on it.

Context at the end of this round: about 800k tokens (the guard's reading when the paper was written: 798,908). The reading stopped at about 713k; the rest went into working out sections 2–4.
