# The Montpellier programme: planning and simulation pass (war game)

Claude Fable 5.2 (effort max), 12 Nov 2026 (written from 16:15 UTC). No sub-agents. Asked for by the user on
12 Nov 2026, about 15:50 UTC: take the plan made at effort medium, consider the shape of the mathematics in it,
simulate how the programme develops from what has already been found, say what has to change for it to be a coherent
whole, and say what mathematics follows from the totality.

**Marks used throughout.**
- **[C]** checked today: in a file or return I opened, or by one of the 15 web lookups listed at the end.
- **[B]** believed: from my knowledge of the literature, or my own derivation; not verified today.
- **[G]** guess: a prediction about pages nobody has read yet.
- Results of 2026 that our files call "claimed, unrefereed" (OpenAI families 008, 019, 031, 032; the 2026 arXiv
  papers) keep that status here.
- Places in the archive are given by cote and scan number of the archive PDF, as the returns give them; his own page
  numbers are in the transcriptions.

**Read for this pass** (about 215k tokens of sources): the plan (`PLAN_EVERYTHING.md`, `ORGANIZATION_RECOMMENDATION.md`,
`PLACEMENT_EVERYTHING.md`, `SECTIONS_STATE.md`, the report `ARCHIVE_PLAN_20261112.html`); for *Les Dérivateurs*
`NEW_RESULTS.md`, the expert's and the CATHOT expert's FINDINGS, HUNCHES and results, the six draft prompts' Parts and
their change record; for *La Longue Marche* the expert's FINDINGS, HUNCHES and handoff, the development candidates, the
reports of LM2, LM3 and LM3b, the Parts of LM4–LM8 and the cross-links in LM5; of the archive returns: Grothendieck's
contents page of cote 147, the opening overview of all ten notes files, the 118 items they class as conjectures, and
about 28 scan pages of cotes 142, 147 and 149 read in the transcription; `RECENT_RESULTS.md` and `BRIEF_FOR_PROMPTS.md`.
Not read: the transcriptions in full, the returns STRATA, PATHS, BISITE, RESIDUE themselves (only what LM5 quotes),
any scan image.

---

## Summary

1. **The six books stand; the programme is one problem.** Grothendieck returns throughout to one task: take a
   geometric object apart along a stratification and rebuild it (its fundamental groupoid, topos, homotopy type,
   Galois action) from elementary pieces and gluing data. It is the boundary of the moduli spaces (147), the
   stratified spaces (150–151), the gluing question of *Les Dérivateurs* XII, the hole-filling of the Longue Marche,
   a map on a surface. The new mathematics sits on these bridges between books. The medium plan has no reader, no
   register field and no budget for them.
2. **Two of the first four cotes back are not what the archive's titles say, and a third holds more** [C]. Cote 149
   ("untitled") is the anabelian notes of 1983 (it opens "1. Résultats de fidélité"; it has the *Conjecture
   fondamentale* and Conjectures A, B, B′), not a sequel to 147. Cote 142 opens with a 19-page text "Catégories de
   Galois-Teichmüller d'un corps alg. clos". Cote 147 contains, in its §§11–13, the theory of stratifications that
   the plan files in Book V, and Grothendieck's own counterexample to his reconstruction claim (the sphere, scan
   180). Most other placements rest on titles alone. A reconnaissance pass over the scans and eight probe packages
   come before the bulk.
3. **Our results already meet the returns at the level of statements.** His question at 147 scan 180 (the homotopy
   type of a topos glued from an open part and its closed complement) is the one he asks again in *Les Dérivateurs*
   XII app. ms. 17–18, answered yes in our returns (FINDINGS F-G6; STRATA C.3). Today's theorem (filtered ⇔
   colimits of sets and of groupoids are homotopy colimits; unchecked) says why gluing along a span needs the
   Grothendieck construction. LM2's computation of GT₀ on SL₂(Z/n) is a statement about the polyhedra of cote 79 [G].
4. **The pipeline puts the research prompts last.** Pro transcribes, Opus checks, Fable reads the checked chapter and
   only then writes prompts for Pro. Pro mode is the resource that may end first. For the keystone chapters Fable
   must read the first pass now; the second pass then reports the reading changes that touch mathematics.
5. **Order.** Keep the adopted order with three changes: probes first (156-1/2, 136, 93, 79, 83, 154, 138, 159);
   the dossier around *Pursuing Stacks* with cote 158 and cotes 137, 133 before the motives; cotes 79, 83 and 64
   with the maps. Cost: the motives finish about 13 Pro runs later than planned.
6. **Budget.** A protected core of about 5,700 pages (about 63 Pro runs at 90 scans, 81 at 70; about 157 Opus points
   for a full second pass, the returned pages included) fits the four Opus weeks and can be through before the end
   of November. The whole (10,150 pages still to send) does not fit four Opus weeks. Section 5 gives the cut order.
7. **What to pursue first** (section 3): the boundary of the Teichmüller tower as a profinite exit-path category with
   GT as its automorphism group; the gluing theorem common to Books III, V and VI; a criterion for when his
   reconstruction by fundamental groupoids is exact (his "π₂ obstruction"); GT-shadows on his regular polyhedra;
   after their return, the 1976 de Rham notes against integral schematization (Toën 2020, Horel 2024).
8. **One result found in this pass, unchecked** (S6): for a hyperbolic curve over a number field and any section s,
   the centralizer in the geometric fundamental group of s restricted to the kernel of the cyclotomic character is
   trivial if s is not cuspidal and is the inertia group if it is. This is Grothendieck's "précision" in the margin
   of 149 scan 56; the proof uses Ribet's theorem of 1981. It repairs the Longue Marche §34 (FINDINGS F17).

## Guide map

**Where we are** [C, from the report of 12 Nov, 15:40 UTC]: 611 of 10,761 Pro pages returned (cotes 147, 149, 146, 142
and 45 pages of cote 1); 438 scans built and waiting (16, 47, 54, 44; 4–9, 100); no second pass on any archive
package; no Fable reading of any archive return; eleven research prompts drafted and unsent (LM4–LM8; six on *Les
Dérivateurs*).

| Book | What it is, in one line | State | Next | Bridges it carries (section 1) | Results in hand that meet it |
|---|---|---|---|---|---|
| Front door | The Esquisse, annotated; two popular texts | not started | 161-3, 161-4 in one run with the maps | all | — |
| I | EGA after chapter IV | not started | plans (21–23, 26, 35, 48, 102); map against print **and the Stacks project** | B11 | EGA and SGA editions |
| II | Cohomology, motives, the 1976 de Rham notes | 438 scans built | 16/47/54/44 and crystals now; 137, 133, 136 before the motives | B3, B4, B7, B8, B9 | 008 with Brown (claimed); LM (the same Galois group) |
| III | The Long March and the notes around it | LM done; 142, 146, 147, 149 returned | 144, 148, 143, 145, 141; revise LM5 and LM6 against the returns | B1–B6, B12 | LM FINDINGS F1–F27; LM2, LM3, LM3b; STRATA; 019, 031 (claimed) |
| IV | Maps, regular polyhedra over rings | not started | 138 and the maps; probes of 79 and 83, then both in full | B5, B6, B12 | LM2 (congruence images); LM §§36–37 |
| V | Tame topology, stratified spaces, forms | 147 §§11–13 returned (filed in III) | 150–152, 120, 121; probe 156-1/2 | B1, B10 | STRATA C, F; F-G6; today's theorem F4-6 |
| VI | Stacks, derivators | *Dérivateurs* companion 28 of 32 chunks | six prompts now; 158 and the dossier 103–118 | B1, B2, B7, B8, B10 | NEW_RESULTS 1–12; FINDINGS; HUNCHES H1–H10 |
| Workshop | Early notes, documents, concordance, register | 45 pp. of cote 1 | the register and the notation table start now, for the whole archive | — | — |

**What comes next, in order** (reasons in sections 2 and 4):
1. Repair before sending: one-stream sentence, the 31 dropped scans, and a check that no context zip is empty (the
   one for MPL_147_048-137 was: its 222 notes carry no comparison [C]).
2. Reconnaissance pass over the scans of every cote above 40 pages (Claude Opus 5.5; no Pro): his own headings,
   pagination, dates, hand, typed share. Output: a content map; corrected placements; real context summaries.
3. Send the built packages; build and send ranks 4 and 5; send the eight probes.
4. Fable readers on 147, 149, 146, 142 from the first pass, each with the carry-questions of section 4.3.
5. Send the six *Dérivateurs* prompts (they need nothing from the archive; one of them checks today's theorem).
   Revise LM6 against cote 149 and LM5 against 147 §§11–13 and 149 scans 3–23, then send.
6. Start the archive-wide question register and notation table from what exists.
7. Then order W of section 2.5.

**What develops where.** Edition and translation: every chapter. Companion in the *Dérivateurs* style: Books V, VI,
II (motives, crystals). Book in the Longue Marche style: Book III; Book IV. Concordance with a short residue: Book I.
New mathematics: the bridges B1–B12, through the prompts of section 4.4.

---

## 1. The shape of the mathematics

### 1.1 The books

**Book I. Elements, continued** (51 cotes, 3,158 pp.).
- *Objects.* Schemes and their morphisms; representable functors (Hilbert, Hom, Picard); descent; group schemes and
  torsors; residues and duality; intersections; étale cohomology and the fundamental group.
- *Central questions.* The chapters of the EGA after IV: which constructions exist and in what generality.
- *What he had, where he stopped.* EGA I–IV in print (1960–67). The plan changed at least twice: thirteen chapters in
  the printed introduction of EGA I (1960) [B, from memory of that introduction], twelve in the plan transcribed as
  CSG U90d [C, `SECTIONS_STATE.md` §4]; cotes 26 and 48 are a third witness, unread. The prenotes of chapter V are
  typed (cote 25). The drafts for VI are short (102, 126–128, 131, 98, 91).
- *Later.* Artin's algebraic spaces and representability criteria answered most of what an "EGA VI" had to settle
  [B]. The Stacks project is the continuation in fact: it has a chapter for nearly every chapter he planned [B].
  So the map of his drafts has three columns (print by number, Stacks tags, the draft), and the residue to develop
  is expected to be small [G]: chapter V itself, non-flat descent (127, 128), Hom functors by non-projective
  methods (91), and what 26 lists as open.

**Book II. Cohomology and motives** (29 cotes, 2,397 pp.).
- *Objects.* De Rham cohomology as a crystal; Barsotti–Tate groups; cycles, correspondences, Poincaré–Hodge algebras
  (16); motives over a field and over a base (12); motivic Galois groups (13, 15); ⊗-categories with fibre functors
  (10, 155); the divided-power de Rham complex (136, 137).
- *Central questions.* One cohomology behind the ℓ-adic, de Rham and crystalline ones; which classes are algebraic;
  the Galois group seen through linear objects; in 1975–76, which multiplicative structure on cochains carries a
  homotopy type over Z.
- *What he had, where he stopped.* Crystals were handed on in 1966–70 (letter to Tate; Pisa 1969). Motives were never
  written up ("Motifs", 24 typed pages from cote 12, is the only text [C, `SECTIONS_STATE.md` §3]). The standard
  conjectures are open in general. The 1976 lecture is lost; 460 pages of notes remain.
- *Later.* Berthelot, Messing, Illusie; de Jong; Fontaine. At a prime p the common source he asked for is prismatic
  cohomology (Bhatt–Scholze), and crystals are quasi-coherent sheaves on a stack attached to the scheme (the de Rham
  stack; prismatization: Drinfeld, Bhatt–Lurie) [B]. Motives: Jannsen 1992; motivic Galois groups without the
  standard conjectures (Nori; Ayoub 2014) and motives over a base with the six operations (Ayoub 2007, built on
  derivators; Cisinski–Déglise) [B]. Standard conjectures: abelian varieties (Lieberman; Ancona for fourfolds in
  characteristic p [B]; all of them by 032 with Milne's theorems, claimed [C, `RECENT_RESULTS.md` L6]). Integral
  homotopy types by cochains with extra structure: Toën 2020 (the group scheme of integer-valued polynomials) and
  Horel 2024 (cosimplicial binomial rings) [C, lookups 2 and 5]. The plan's account of 136–137 names none of this
  line (section 2.3, stage 8).

**Book III. The Long March** (17 cotes, 2,922 pp.).
- *Objects.* Profinite groups with loops (π̂ with its inertia classes); extensions E → Γ; Teichmüller groups and their
  two completions; the modular multiplicities M(g,ν) and their Deligne–Mumford compactifications; MD-graphs and
  "maquettes"; Teichmüller groupoids with their structure at infinity; sections and "paquets" at the cusps; the
  category of Galois–Teichmüller (finite étale maps between curves up to isotopy; 142 scans 3–22 [C]).
- *Central questions.* Determine Γ_Q by its outer actions; say which outer homomorphisms are geometric; describe the
  whole by generators and relations.
- *What he had, where he stopped.* 1978–80: the isotopy category, its "enveloppe profinie" without a universal
  property, and the conjecture that compatibility with all coverings and all morphisms defined over K is
  "suffisamment draconienne" to single out Γ (142 scans 12, 17, 21, 95–96 [C]); he calls it "de nature trop
  platonique" and turns to M(0,4), M(0,5) (scan 100 [C]). 1981: in today's terms Γ′(0,3) = GT₀ and Γ′(0,ν) = GT for
  ν ≥ 4 (LM2 B.m2; LM3 E.7, E.10: the returns' claims); he stops at the filling map ("corollaire hâtif", 2:sc349)
  and at centre and normalizer statements he could not prove profinitely (FINDINGS F5). Cote 147: thirteen sections;
  §12 ends with his "Remords" and the text ends inside the digression of §13. Cote 149 (1983): the conjectures in
  their last form.
- *Later.* Belyi 1979; Drinfeld 1990, Ihara; Nakamura, Tamagawa, Mochizuki 1999 (the Hom-form); Harbater–Schneps
  2000; Hoshi–Mochizuki 2011; Pop 2019 (I/OM), which is the 1978 conjecture in its tripod form [B for the
  identification]; Boggi 2026; Carlson–Haine–Wolf 2024 for the étale-topos form of the letter to Faltings (finitely
  generated fields of characteristic 0, after inverting universal homeomorphisms) [C, lookup 3]. The section
  conjecture over number fields is open; 019 claims the p-adic case.

**Book IV. Maps and polyhedra** (20 cotes, 1,954 pp.).
- *Objects.* Maps as finite sets with an action of the cartographic group; cellular n-maps; regular polyhedra as the
  most symmetric maps, and their forms over rings and finite fields; polygons and cyclotomy; quadrics, quadratic
  forms, SO(3) ≃ GP(1), Azumaya algebras of rank 4.
- *Central questions.* The Galois action on maps; the classification of regular polyhedra over a ring and their
  specialization.
- *What he had, where he stopped.* Course texts of 1976–78; notes to 1986; in print only Esquisse §§3–4.
- *Later.* `SECTIONS_STATE.md` and the recommendation say the programme has almost no successor. That is wrong.
  Abstract regular polytopes (McMullen–Schulte) are his cellular n-maps with a regularity condition [B]; Monson and
  Schulte (2004–08) construct regular polytopes over finite fields by reducing crystallographic Coxeter groups
  modulo p [C, lookup 6]; Γ_Q acts faithfully on regular dessins (González-Diez and Jaikin-Zapirain) [C, lookup 8,
  secondary sources]; GT-shadows compute the action of finite levels of GT on dessins (Guillot; Dolgushev and
  coauthors 2024) [C, lookup 14]; Ji 2023.
- *Prediction* [G]: cote 79 ("2-polyèdres réguliers triangulés et modules de rang 2 sur Z/nZ et Z") is the
  combinatorial theory of the modular curves X(n); the Longue Marche §§36–37 has the cases n = 2, 3, 4, 5 (FINDINGS
  F14). Cote 83 (icosahedra, bi-icosahedra) is tied to M(0,5). The tie itself is in the returns [C]: 147 (near scan
  68) reads the ten divisors at infinity of M̂(0,I), I of five elements, as the ten pairs of I, "d'après l'étude
  combinatoire de l'icosaèdre, choisissant une orientation de I — ce qui détermine un icosaèdre orienté", and asks
  for the full S₅-action (notes N068-02); cote 146 names the icosahedron five times; the Esquisse says the same
  [C, lookup 13].

**Book V. Tame topology and the geometry of forms** (18 cotes, 1,319 pp.).
- *Objects.* Tame spaces; stratified spaces with conical neighbourhoods; unfolding ("déploiement"); stratified
  topoi; "stratifications locales"; in 1986 forms, networks, cuttings, workshops.
- *Central questions.* A topology in which a stratified object has tubular neighbourhoods and can be taken apart
  and rebuilt; comparison of the tame theories.
- *What he had, where he stopped.* 120–121 (1973–79), unread. 147 §§11–13 [C]: four elementary rank-one models
  (C*, the point, the germ of disc, the germ of punctured disc; scan 164), the expectation that products of these
  give all elementary topoi (scan 165) and express all canonical topoi of the stratification (scan 169), the
  reconstruction remark and the "Remords" (scans 179–180), axioms a)–d) of a stratification (scan 181). 150–151
  (Dec 1981–Jan 1982), unread. 156 (1986): four versions of one chapter in six weeks, unread.
- *Later.* O-minimal structures; the o-minimal Hauptvermutung of Shiota (2014): definably homeomorphic compact
  polyhedra are PL homeomorphic [C, lookup 10]. Exit paths and exodromy (MacPherson; Lurie; Barwick–Glasman–Haine;
  the unfolding is the "unzip" of Ayala–Francis–Tanaka [B]; the homotopy link, Douteau–Waas, in STRATA C.2).

**Book VI. Stacks and derivators** (34 cotes, 3,702 pp.).
- *Objects.* Small categories as models of homotopy types; fundamental localizers; test categories; n-stacks;
  schematization; derivators; total asphericity; fibrations and cofibrations of categories.
- *Central questions.* What a homotopy type is, algebraically; what a category of coefficients is; which axioms
  single out W∞.
- *What he had, where he stopped.* The Tapis de Quillen (1968); *Pursuing Stacks* (1983); *Les Dérivateurs*
  (1990–91). The points where he stopped are now located [C, FINDINGS]: XII Théorème 2 was not verified by him and
  is false for W∞ (F-G1); the questions of XVI are answered (F3-3); the conjecture of II ms. 36ter is false (Δ_inj),
  and its true form is today's theorem (F4-6, unchecked).
- *Later.* Cisinski 2006; Maltsiniotis; Heller, Franke, Groth; Ayoub; Lurie; Toën; Kaledin 2026; 312 and 317
  (claimed).

### 1.2 The bridges, as statements

| | Between | The statement | Where in the archive | Where in our files or the literature | Status |
|---|---|---|---|---|---|
| B1 | III.4, V.3, VI | A space or topos glued from an open part U and a closed part Y is the homotopy pushout of U ← T* → Y, T* the punctured tube (the link). In Cat: for a sieve A and its complement B with crossing arrows E, BX is the homotopy pushout of BA ← BE → BB. The 1-topos of sheaves locally constant on the pieces computes the right homotopy type only when the exit-path category is a 1-category. | 147 scans 164–169, 179–180; 150, 151 (unread); *Dérivateurs* XII ms. 62–63, XII app. ms. 17–18 | STRATA C.1–C.8; FINDINGS F-G6; POLES G.19; LM3 F.5–F.14; LM3b H.6–H.9; S2 below | proved in Cat (returns, reviewed in part); his 1981 formulation not yet written |
| B2 | III, VI | Level 1 is exactly what functors modulo natural transformations carry: π₀Fun(X, G) = [BX, BG] when G is a groupoid; no category represents X ↦ [BX, Y] when Y is not a 1-type; a W∞-invariant small ind-object of categories is an ind-groupoid. | LM §§1–4, 14, 16; 147 scan 180; V ms. 44–46, VII ms. 129–132 | CATHOT C.1–C.4, B.11; OWN_RESULTS 3.1–3.2; GALOIS B.10–B.12; LM3 F.3 | proved, two proofs by two systems |
| B3 | II.6, III.3 | The Lie algebra of the pro-unipotent automorphism group of the genus-0 tower (grt₁) is the motivic Lie algebra of mixed Tate motives over Z: free on one generator in each odd weight ≥ 3. The profinite statement Γ_Q = GT is separate and open. | 13, 15 (unread); LM §§26–32, 46 | Brown 2012 (injection); 008, Willwacher, Hirose (surjection, claimed); LM3 E.8, E.20; LM2 B.g | claimed 2026 |
| B4 | II.5–6, III | Full faithfulness, twice: the Tate conjecture for ℓ-adic realizations (linear), the Hom-conjecture for fundamental groups (non-linear). The second is proved (Mochizuki 1999, Theorem A) from linear statements about H¹ of all finite coverings. | 14, 15 (unread); 149 scan 48 (*Conjecture fondamentale*); LM §5 | FINDINGS F6, F25; LM3 D | theorem for dominant maps; sections open |
| B5 | III.3, III.6, IV.4 | Every element of GT₀ preserves every congruence kernel of SL₂(Ẑ) and acts on SL₂(Z/n) through (Z/n)*/squares; the images of Γ_Q, GT and GT₀ agree there (orders 1, 2, 2, 2, 2, 2, 4, 4, 8 for n = 2, 3, 4, 5, 6, 7, 8, 12, 24). | LM §§36–37, 53; 79, 64 (unread) | LM2 C.d1, C.r1–C.r3 | the return's claim; reading 79 as X(n) is [G] |
| B6 | III.1, III.7, IV.2 | A map is a finite set with an action of the cartographic group, hence a covering of P¹ minus three points, hence a curve over Q̄; GT acts on maps; Γ_Q acts faithfully already on regular ones. | 142 scans 108–114; 138, 76 (unread) | Belyi 1979; González-Diez–Jaikin-Zapirain; GT-shadows | theorems |
| B7 | II.9, VI.4 | Integral homotopy types of finite type are carried by cochains with a binomial structure (algebras over the plethory of integer-valued polynomials); the homotopy groups of the schematization over Z are modules over the group scheme H = Spec of that ring. | 136, 137, 133, 153 (unread; 153 opened by the placement file: "T(T−1)…(T−n+1)/n!") ; *Pursuing Stacks* VI | Toën 2020; Horel 2024; Borger–Wieland for the plethory [C, lookups 2, 5, 15] | theorems; their relation to his notes is [G] |
| B8 | II.1–2, VI | A crystal is a quasi-coherent sheaf on a stack made from the scheme; the unipotent homotopy type of a scheme is an affine stack. | 5–9 (unread); *Pursuing Stacks* VI | Simpson; Drinfeld; Bhatt–Lurie; Toën's affine stacks; Mondal–Reinecke [B] | theorems |
| B9 | II.6, VI, I | Motives over a base with f*, f_*, f_!, f^!: the formalism "Motifs" asks for, built on derivators. | 12 ("M(X) over a noetherian base") | Ayoub 2007; Cisinski–Déglise [B] | theorems; the t-structure is open |
| B10 | V.1, V.4, VI | Compact tame spaces up to tame homeomorphism are compact polyhedra up to PL homeomorphism; their homotopy types are those of finite categories (Hot₀). No localizer of Cat sees simple homotopy types. | 120, 121, 156 (unread); V ms. 51–52; XVI ms. 87–96 | Shiota 2014; CATHOT G; OWN_RESULTS §2; POLES D.4–D.6 | theorems; the reading of 156 is [G] |
| B11 | I, III | Injectivity of points → sections rests on the absence of divisible elements in the rational points of the generalized Jacobian, not on finite generation. | LM 2:sc64; 149 §1 ("Théorème 3") | FINDINGS F15 | corrected statement, checked on Stix and Esnault–Hai |
| B12 | IV.6, III, II.9 | Forms of P¹ are conics, are Azumaya algebras of rank 4, are quadratic forms of rank 3 up to scalars: SO(3) ≃ GP(1). | 82, 83, 84, 77 (unread); LM §20; 133 | development candidate 7 | classical; his use of it unread |

---

## 2. The war game

### 2.1 The model

Inputs, all from the report of 12 Nov [C]: Pro runs two or three packages at once; one stream takes about 80 minutes
for 45 scans, 130 for 70, 165 for 90; about 120 packages remain at 90 scans (about 150 at 70); Pro mode may end with
November. The second pass costs about 0.025 points per scan on the Opus half (50 points a week; four weeks given). A
Fable reader costs about 4.5 Fable points and takes 220k tokens of source: 150 archive pages with Pro's notes, 380
without; 314 Fable points remain with the three resets. Research prompts use the same Pro slots as transcription.
Assumed [G]: nine Pro runs a day when sending is steady.

### 2.2 Stage 0, already played: the returns against the plan

| Cote | The plan's description | What the return is [C] | Consequence |
|---|---|---|---|
| 147 | Structure at infinity of M(g,ν), ms. pp. 1–90, "paginated text with contents" | 13 sections. §§1–6: standard curves, MD-graphs and "maquettes", the Mumford–Deligne theorem, specialization and generization. §§7–8: the modular multiplicities of dimension ≤ 2 (scan 60: M̂(0,4), M̂(1,1) "cas élémentaires", then M̂(0,5), M̂(1,2) and products) and strata in ambient dimension ≤ 4. §§9–10: the "MDT-structure", extensions SΠ₁M_G of ∏Π₁M(g_α, Î_α) by Z^Ã(G), generization morphisms; the "Programme" of scan 104: all groupoids Π₁M(g,I) "par générateurs et relations". §§11–13: unfolding of a normal-crossings divisor, elementary types, general stratifications | Book V's subject begins here, a year or more before cotes 150–151. The two-level principle of the Esquisse is at scan 60 in a first form ("J'ai l'impression", notes N060-03) |
| 149 | "Untitled paginated text (ms. pp. 1–67)", filed as the sequel of 147 | The anabelian notes: "1. Résultats de fidélité" (scan 3); Kummer theory and rigidity (24–46); *Conjecture fondamentale* (48); Conjectures A (56), B (59), B′ (63); good reduction (100); sections of 𝓔_L over 𝓔_K and valuations, conjecture a), b) (126–127); a "maquette" at infinity for varieties of higher dimension and its π₂ question (133–134) | Misplaced. It is a text of its own, dated 1983 in the earlier transcription, and the subject of LM6. An outside witness exists: "Notes anabéliennes", deciphered by Carmona with Künzer (39 pp., Wayback copy; `SECTIONS_STATE.md` §18 could not name its cote) |
| 146 | Teichmüller groupoids (from 1978) | Finite-object models of the groupoids (S₀T_G as a contracted product, scan 100), three-, four- and five-point geometry with tangential data, sewing, torus presentations; a conjecture that the space of disc choices is contractible (scan 106); documentary evidence for dates (scans 126–134) | It supplies the explicit models that 147 §9 uses. The global pass of III.1 and III.4 must be one pass |
| 142 | Galois action on Teichmüller (from 1978) | (i) "Catégories de Galois-Teichmüller d'un corps alg. clos", 19 pp.: finite étale maps of surfaces up to isotopy; the "programme à l'horizon" (scan 17). (ii) Equations for endomorphisms with parameters β, λ, lifts under ρ and σ, and the wish to check complex conjugation "par un calcul dans Π(0,3)" (scans 25–42). (iii) Base points near a puncture (46–50). (iv) "Notre objet est d'essayer de déterminer … cette action" (69). (v) Necessary conditions a), b) for an automorphism to come from Γ, conjectured sufficient; Belyi named in the margin (95–96). (vi) "de nature trop platonique"; towards conditions from M(0,4), M(0,5) (100). (vii) Cartographic groups (108–114). (viii) Boundary groupoids, "pavage par des carrés ?" (115–122) | Several layers, at least one after 1979. Dating by layer is a task of the second pass. Layer (vii) belongs to Book IV as well |

**What our results met there.**
- 147 scans 179–180 and bridge B1. His *Remarque*: when all strata D* are K(π,1) ("ce qui est le cas dans la situation
  de Teichmüller !"), the system of the fundamental groupoids of the elementary pieces with the canonical morphisms
  must rebuild the groupoid of X, the "topos quasi-galoisien" and "par là aussi les types d'homotopie … y compris X";
  margin: this must hold "indépendamment de toute autre hypothèse (genre K(π,1)) de façon essentiellement triviale".
  His *Remords*: for X = P¹(C) with the point ∞ the system is {1} ← Z → {1}, the topos of sheaves locally constant on
  the pieces is the presheaf topos of • → •, whose cohomology vanishes, and S² is not recovered. Both are right
  [B, my reading]: the homotopy colimit of the classifying spaces of {1} ← Z → {1} is S², so the system does
  determine X when it is glued by the Grothendieck construction; the 1-topos is the presheaf topos on the homotopy
  category of the exit-path category, which here has lost the circle Map(∞, c) ≃ S¹. In Cat this is STRATA C.3 and
  C.4, and it is the question he poses in XII app. ms. 17–18 ten years later. Today's theorem F4-6 gives the reason
  in one line: an ordinary colimit of groupoids over a shape computes the homotopy colimit for all diagrams only
  when the shape is filtered, and a span is not.
- 147 scan 104 and LM3 Part F. The "Programme" asks for what LM3 F.5–F.16 builds for genus 0 and for the types (1,1),
  (1,2): the transporter category of stable graphs with multitwist groups, completed, with GT as automorphism group
  of the decorated genus-0 tower (the return's claims; their item-by-item review is with another agent).
- 149 scan 56 and FINDINGS F7, F17, hunch H5. The margin "π^Γ° = (1) (premier cas), π^Γ° = L_i (deux. cas)" is the
  criterion the Longue Marche lacked. It is provable (S6).
- 149 scans 126–127 and 019. Conjecture b) ("toute section de 𝓔_U sur 𝓔_K se relève en une section de 𝓔_L") is the
  step from a section on the curve to a section on its function field. In 019 that step rests on its Theorem 1.2,
  for p-adic fields, and a) is the valuative form used there through Koenigsmann and Pop–Stix [B, my reading of the
  audit of 019 in the LM3 report, Part D]. Over number fields both are open.
- 149 scan 52 (the étale topos is expected "1-fidèle", "peut-être pleinement fidèle" after inverting universal
  homeomorphisms; margin "S de car. 0 ?") is a theorem for finitely generated fields of characteristic 0
  (Carlson–Haine–Wolf 2024 [C, lookup 3]); LM3 C.11 proves the curve case from Mochizuki's theorem.
- 142 scans 95–96 and Pop. The conjecture that conditions a), b) suffice is, in substance, I/OM (Pop 2019), which LM2
  C.a12 and LM3 E use with its hypotheses [B for the identification; to be written by the reader of 142].
- 142 scans 25–42 and LM2 B.m2. LM2 proves that the loop equation of §46 (1981) is Drinfeld's (I), (II). If these
  scans carry the same system and date from 1978–79, he had the two relations of GT₀ before Belyi's theorem reached
  him. This needs the dating of the sheets (the notes file has a block on "physical-sheet dating").

**Questions this stage settles.** 149 is not part of III.4. The reconstruction claim of 147 has an exact modern form.
**Questions it opens.** S1, S2, S5, S6, S7, S8 of section 3. **Prompts it triggers.** EXIT_TOWER, EXIT_ONE_TYPE,
CYCLOTOMIC_KERNEL, GT_CATEGORY (section 4.4), and the revision of LM5 and LM6.

**Where the plan broke at stage 0, and what to do now.**
1. *149 misplaced.* Give it its own chapter in Book III ("The anabelian notes, 1983"), before the dated notes of
   1981–83 or with 148 once that returns. Collate the Carmona–Künzer transcription as a witness and credit it.
2. *Titles do not describe contents.* Two of four cotes were wrongly or thinly described. Run the reconnaissance
   pass of the guide map before any further placement is used for a context zip or a reader's brief.
3. *The context zip of MPL_147_048-137 was empty* (22 bytes; all 222 notes are marked "C0"). Add a build check
   (non-empty zip, README present, files listed exist). Redo the comparison for those notes by script (grep of
   their search terms) and a short Opus read; no Pro run is needed.
4. *Notation.* The symbol Γ(g,ν) has three meanings in the Longue Marche (F13); the returns add 𝔖/𝒮, M̂!, SΠ₁M_G,
   S₀T_G, Γ° (kernel of the cyclotomic character in 149), E_K, 𝓔_L. Start one notation table for the whole archive
   now (stable id, first occurrence, variants, meaning, modern name), and fix the English renderings of
   "multiplicité", "lacet", "maquette", "déploiement", "paquet", "anabélien" (in 149 a property of a homomorphism:
   every open subgroup has an image with trivial centralizer) before any chapter of Book III is translated; Books V
   and VI use the same words.
5. *Order inside a unit.* The paginated texts went first, so the notes on 147 could not use 146 and 142. Nothing to
   redo; the second pass repairs it if the global pass of III.1 and III.4 is done jointly.

### 2.3 The first tranche, stage by stage

The stages are in the order recommended in 2.5. "Likely" is [G] unless marked.

**Stage 1. The built packages: 16, 47, 54, 44; crystals 5, 6, 7, 8, 9, 4, 100** (440 pp.).
- *Likely.* 16: axioms of a Poincaré–Hodge algebra (a graded algebra with duality, a class with the hard Lefschetz
  property, a rational subalgebra of algebraic classes, a positivity condition) and formal deductions among the
  conjectures; the two letters to Coates [C]. 47: a Fourier transform between the derived categories of A and its
  dual by the Poincaré bundle, perhaps with inversion, undated, before Mukai (1981). 44: the abelian varieties
  J^i(X) of the letter to Serre. Crystals: the letter to Tate; the talks of 1967; Barsotti–Tate groups and good
  reduction; in 8, calculations of 1970, perhaps around the "mysterious functor" of the Nice talk.
- *What meets it.* Little of ours. From the literature [B]: the Kähler package (Poincaré duality, hard Lefschetz,
  Hodge–Riemann) is now proved in settings with no variety (Adiprasito–Huh–Katz; Elias–Williamson), by inductions
  that 16 can be compared with; Lieberman's proof of conjecture B for abelian varieties runs through the Pontryagin
  product, the calculus of 47 and 54; the J^i(X) have distinguished models over the base field
  (Achter–Casalaina-Martin–Vial); homomorphisms of Barsotti–Tate groups (de Jong 1998); prismatic Dieudonné theory.
- *Settles.* The error rate and package size for the 1960s hand; whether 47 states involutivity; whether 16 holds an
  inductive strategy for B and the index theorem and where it stops.
- *Prompts.* None before the reading.
- *Break.* The plan gives ranks 2 and 7 no context zip. Give each one made of outside witnesses (the printed
  "Standard conjectures"; the letters L10d, L11d, L23d; the transcription of the letter to Tate), opened after the
  freeze like any context, so that the notes say what the folder adds to print.

**Stage 2. Rank 4: 144, 148, 143, 145, 141** (339 pp.).
- *Likely.* 144 continues the Longue Marche after June 1981. 148 is of 1983, the year of the letter to Faltings: the
  most likely place for the two-level principle in the form of the Esquisse and for the relation of order 5 from
  M(0,5) written as an equation. 143 and 145 are earlier drafts. 141: Kummer theory at a cusp.
- *What meets it.* All of the LM files. Three checks decide most of it: (i) hunch H1: is the M(0,5) condition an
  equation here, and of what date; (ii) F13: which Γ(g,ν) each page means; (iii) whether he returns to the filling
  map (LM3b B.4–B.6: onto, with a kernel larger than point-pushing, already for (0,4) → (0,3)) and to (f) of §32
  (settled, F21).
- *Settles.* The chronology from GT₀ to GT inside the archive.
- *Break.* LM4–LM6 were drafted on the Longue Marche alone. Cote 149 treats the subject of LM6 two years later; 147
  §§11–13 and 149 scans 3–23 restate the topoi of LM5; 142 scans 25–42 bear on LM4 Part E. Revise the three prompts
  against the returned notes before they are sent. Otherwise Pro is asked to prove what he later corrected.

**Stage 3. Rank 5: 150, 151, 152, 120, 121; with them 153 and 155** (300 pp.).
- *Likely.* 150: conical neighbourhoods; the unfolding of a stratified space into manifolds with corners, with
  fibrations between faces; the dévissage of Esquisse §5. 151: the same for topoi, with the tube as a datum. Then the
  sequence is 147 §12 (the groupoids of the pieces do not suffice for the 1-topos) → 150–151 (the tube) → XII app.
  (gluing in Cat). 120–121: axioms for tame spaces, written before o-minimal structures were defined. 152 (plane
  trees) has three candidate readings: the stable trees of the strata of M̄(0,n); the "types" of the path categories
  of *Les Dérivateurs* VII ms. 99–102; dessins that are trees.
- *What meets it.* STRATA C.1–C.8 and F.1–F.13; F-G6; F4-6; LM3 F; LM3b H; 147 §§11–13.
- *Settles.* Whether he resolved the Remords himself in December 1981; whether his axioms are those of an o-minimal
  structure; whether his comparison of tame theories is Shiota's theorem.
- *Prompts.* DEVISSAGE and TAME_AXIOMS after the return. EXIT_ONE_TYPE needs only 147 and goes now.
- *Breaks.* 153 ("Analyseurs") and 155 (a ⊗-category with a fibre functor over k′/k) return here and belong to II.9
  and II.7: route their notes to the readers of 136–137 and of cote 10. The context zip of this rank must hold 147
  scans 138–190 and the statements STRATA C.1–C.8; "returns of cote 147; Esquisse §§5–6" is too coarse.

**Stage 4. Eight probes** (about 350 pp.; each is the first package of its cote).
- 156-1 with 156-2 (44 pp.). Nobody has read a page; the plan fixes two chapters of Book V blind. A guess to test:
  a form is a tame space known through its finite cuttings, a pro-object of finite posets or categories under
  refinement. If so, 156 joins Book V to Hot₀ (V ms. 51–52) and to simple homotopy in Cat (XVI ms. 87–96), and the
  CATHOT results on finite categories become its tools. If not, nothing is lost.
- 136 scans 2–46: his own "Historique" (Carmona printed two pages of it [C]).
- 93 scans 2–46, after its typed sheets are listed: 235 pages whose content the plan does not know.
- 79 and 83, 45 scans each: test B5 and the reading of the bi-icosahedron through M(0,5).
- 154 (pseudolines, 1983–84, on listing paper): tame topology, forms, or neither.
- 138: the earliest folder on the arithmetic of maps, before Belyi.
- 159 whole (33 pp.): projective connections; with 93 and 64 a possible cluster on the differential equations of
  uniformization.

**Stage 5. Rank 3: 21, 22, 23, 26, 35, 48, 102** (188 pp.).
- *Likely.* Plans, lists of open problems, complements.
- *Break.* The plan files 51 cotes under chapter numbers taken from one of his plans. Use subject keys now
  (projective methods; construction; groups; Picard; duality; intersections; étale), with a concordance to each of
  his numberings, so that no chapter is renamed when 26 and 48 return. Put the Stacks project in the map from the
  first row.

**Stage 6. Rank 9 with 137 and 133: 158, 108, 112–118, 103–107, 109, 111, 135; 137; 133** (575 pp.).
- *Likely.* 113–118: the 1983 forms of *Les Dérivateurs* XI–XII and XVI [C, the plan]. 115 ("correspondances
  fonctorielles, dualité des topos"): perhaps the bimodule of crossing arrows of STRATA C.1. 137: cosimplicial
  algebras with strict multiplication. 133: operations on the ring of finite G-sets and a Witt construction.
- *What meets it.* All of NEW_RESULTS and FINDINGS. The reader's task is definite: for each of the twelve results
  and each question of XVI answered in F3-3, find its 1983 form in 108, 114, 117, 118; say where the strong form of
  W(7) and "totalement asphérique ⟹ filtrant" first appear.
- *Settles.* The companion can close.
- *Prompts.* The six drafted prompts do not wait for this stage. After it: SCHEMATIZATION_LOCALIZER.
- *Break.* 133 is at rank 22 in the plan; it must travel with 137 and 136.

**Stage 7. Rank 6: 14, 13, 12, 15, 18** (637 pp.).
- *Likely.* 14: deductions among the conjectures of Hodge, Tate, Lefschetz and Weil. 13, 15: motivic Galois groups
  over a field, the extension by Γ_Q, L-functions of motives. 12: motives over a base, weights, "cohomologie
  absolue" [C, the contents of "Motifs"]. 18: Hodge realizations. His period conjecture is known through others'
  reports [B]; if he wrote it down, it is here.
- *What meets it.* B3 and B4. The reader builds the table "linear statement, non-linear statement": Tate and the
  anabelian Hom; semisimplicity and trivial centres; polarizations and real structures; weights and cyclotomic
  normalizers.
- *Break.* The typed sheets of 12 and 15 go to the API after an inventory. The context zip needs "Motifs" as a
  witness.

**Stage 8. The rest of 136** (330 pp.).
- *Likely.* The divided-power de Rham complex of a semi-simplicial set or topos as an integral cochain model;
  "constructions universelles"; a "topos de De Rham".
- *What meets it.* B7. The plan's literature for this cote stops at Illusie and Bhatt–Lurie–Mathew. The line it
  needs: Cartan, "Théories cohomologiques" (Invent. Math. 35, 1976), which I believe treats forms with divided
  powers at Grothendieck's suggestion [B; the lookups confirmed the reference only]; Miller 1978; Dwyer's tame
  homotopy theory; Mandell; Ekedahl; Toën 2020; Horel 2024.
- *Settles.* What the lost lecture said.

**Stage 9. Rank 10 with 79, 83, 64 and the two popular texts** (about 1,020 pp.).
- *What meets it.* B5, B6, LM2. The context zip: LM §§36–37 and 53, LM2 sections C.d and C.r, and a corrected sheet
  of the literature of Book IV (section 1.1).
- *Prompts.* POLYHEDRA_SHADOWS.

**Stage 10. Rank 11: the final state of 156** (353 pp. after the probe). Its brief is written from the probe.

### 2.4 The second and third tranches

- *The rest of Book IV* (72, 86, 85, 69, 74; then 73, 78, 77, 82, 84, 87, 89; about 1,140 pp.). Calculations and
  tables. Returns: enumerations that a script can recompute. Do not give each 150 pages a Fable reader; one reader
  per chapter on the transcription alone, after the scripts have run.
- *The rest of Book II* (10, 11, 56, 60, the rest of 93, 161-5, 130; about 630 pp.). 10 is largely typed. With it
  belongs 155 (1984), back with rank 5: it asks to "exprimer la rigidité" for a fibre functor over an extension
  k′/k, the question Deligne's "Catégories tannakiennes" (1990) settles [B].
- *The periphery of Book III* (67; 159 if not probed). The letter to Bers (1984) is in print.
- *The three earlier versions of Analysis situs* (294 pp.). Variants of 156-8. Last among the handwritten texts of
  Book V; first candidate to cut.
- *Book I and the workshop* (about 3,000 pp.). Drafts of printed texts. The second pass is a map against print and
  the Stacks project; a Fable reader only for what the map finds in neither.

### 2.5 Three orders compared

Pages are those still to send (10,150). "Runs" are Pro runs of 70 scans.

| After | A. The adopted order (built packages, then ranks 3, 4, 5, 6, 8, 9, 10, 11, 12, …) | W. Recommended (built; 4; 5; probes; 3; 9 with 137, 133; 6; rest of 136; 10 with 79, 83, 64; 11; …) | B. Book order (front door, I, II, …) |
|---|---|---|---|
| 30 runs (2,100 pp.) | everything through the motives; 200 pp. of 137, 136 | everything through the EGA plans; all eight probes; the dossier and 158; no motives yet | part of Book I |
| 45 runs (3,150 pp.) | adds 137, 136, the dossier, most of the maps | adds 137, 133, the motives, all of 136 | Book I |
| 60 runs (4,200 pp.) | adds the maps, 156 (final), 64, 67, 159, most of 10, 11, 56, 60; nothing of 79, 83, 93, 154 | adds the maps, 79, 83, 64, the popular texts; 156 final not yet (probe only) | Book I and half of Book II; nothing from Montpellier |
| 75 runs (5,250 pp.) | adds 79, 83 and the other polyhedra | adds 156 (final), 67, rank 13, 72, 86, 85: the protected core of section 5 but for the rest of 93, the pseudolines, 127 and 128 | — |

- *A against W.* They nearly agree by run 80. They differ if Pro ends between runs 25 and 70. W gives, at every cut, some
  pages of every book and a decision on every unknown; it closes the *Dérivateurs* companion earlier; it reads the
  two cotes of Book IV that touch the Longue Marche before the bulk of that book. Its price: the motives finish at
  about run 40 where A finishes them at run 27, and the final state of 156 comes after run 60.
- *B, and a chronological order.* Both put the Paris years first (about 4,800 Pro pages [G for the count]), most
  of them drafts of, or notes behind, texts in print. Nothing our results meet would return in the first 60 runs. A
  chronological order has one merit, that a hand and a notation are learned once; our second pass can have it
  anyway by keeping a sign table per period (section 4.1).
- **Recommended: W.** It is the adopted order with three moves, each for a stated reason: probes first (placements
  rest on titles); rank 9 and 137, 133 before rank 6 (they meet the results in hand, close a companion, and the
  1960s hand must be tested on the built packages before 637 more pages of it are sent); 79, 83, 64 with rank 10
  (bridge B5).

### 2.6 The breaks, in one list

| # | Break | Stage at which it bites | Do now |
|---|---|---|---|
| 1 | Placements rest on archive titles; two of the first four were wrong or thin | every later context zip and brief | reconnaissance pass; probes |
| 2 | 149 filed as the sequel of 147 | the edition of III.4; LM6 | own chapter; collate "Notes anabéliennes" |
| 3 | Empty context zip (MPL_147_048-137) | the reading of 147 | build check; redo the comparison by script |
| 4 | No archive-wide notation table; Γ(g,ν) has three meanings | first translation of a Book III chapter; Books V, VI reuse the words | start the table and the glossary now |
| 5 | LM4–LM6 drafted before the returns of 142, 147, 149 | when they are sent | revise against the returned notes first |
| 6 | The Fable reader waits for the second pass; prompts come last | from December, when Pro may be gone | keystone chapters are read on the first pass (section 5.3) |
| 7 | No reader, register field or budget for the bridges | the first chapter whose result changes another book (it has happened: 147 and XII app.) | bridge tags; bridge readers; 15–20 % of Fable held back |
| 8 | Notes are 850 tokens a page, more than the text | every Fable reading | compact note format; compact the existing notes by script |
| 9 | Book I's chapter numbers follow one of several plans; the map ignores the Stacks project | rank 3; every Book I folder | subject keys; three-column map |
| 10 | Book IV's literature is misdescribed ("no successor") | the briefs of ranks 10, 14, 18 | corrected literature sheet (section 1.1) |
| 11 | Book V chapters 4–5 are planned unread | rank 11 | probe 156-1/2 |
| 12 | The plan's literature for 136–137 misses integral homotopy theory; 133 is nine ranks away | rank 8 | corrected sheet; 133 with 137 |
| 13 | 153, 155 arrive with the stratified spaces | rank 5 | route by bridge tag |
| 14 | The register is planned per chapter | the first cross-chapter answer (147 scan 180 is answered in XII app.) | one register, with links between entries (section 4.2) |
| 15 | One Fable reading of every page leaves the calculation folders over-read and the bridges unread | resets 2 and 3 | allocation of section 5.2 |

---

## 3. What follows from the totality

Each item: the statement; what it rests on; how plausible, and why; what would decide it; which chapters and returns
bear on it. V is value to the field, T tractability with our means (Pro prompts, Fable reading, Opus checking), both
from 1 to 5. The table at the end ranks them.

### S1. The tower with its structure at infinity is a system of profinite exit-path categories, and GT is its automorphism group

- **Statement.** For 2g − 2 + n > 0 let E(g,n) be the exit-path category of the Deligne–Mumford compactification of
  M(g,n) stratified by topological type: objects are stable graphs, arrows are transporters modulo the multitwists of
  the source. (a) E(g,n) is an ordinary category and its classifying space is the compactification. (b) Its
  completion Ê(g,n) by finite congruences has as finite representations the finite sheaves constructible along the
  boundary. (c) Forgetting, clutching and relabelling are functors between the Ê(g,n); the automorphism group of the
  decorated genus-0 system is GT, and Γ_Q acts on it faithfully. (d) Conjecture: the automorphism group of the whole
  system is GT, and the system is generated in modular dimension ≤ 1 with relations in dimension 2.
- **Rests on.** 147 §§7–10 and scans 60, 104, 179 (his "MDT-structure" and "Programme"); for (a), Jansen 2023 as used
  in STRATA F.8 and LM3 F; for (b), (c), LM3 F.2–F.14 with Barwick–Glasman–Haine and Harbater–Schneps; for (d),
  Boggi's theorem for the procongruence tower (2026 preprint, read in the introduction only: FINDINGS F27),
  Hatcher–Lochak–Schneps and Nakamura–Schneps.
- **Plausibility.** (a)–(c): proved in the returns; STRATA has been reviewed, LM3 and LM3b not yet item by item.
  (d): true for the procongruence completions if
  the preprint holds; for the full completions it needs the congruence subgroup property in genus ≥ 3, which is open
  (F4).
- **What would decide it.** The open rows LM3 F.16, LM3b E.4, E.9 (genus 1), H.9 (five points).
- **Bears on.** III.1, III.4; V.3; IV.2. **V 5, T 3. Pursue** (EXIT_TOWER).

### S2. When his reconstruction by fundamental groupoids is exact

- **Statement.** Let D be a divisor with normal crossings in a complex manifold or Deligne–Mumford stack X, with
  strata D_J*. The exit-path ∞-category of (X, D) is equivalent to an ordinary category if and only if every stratum
  is aspherical and, for all J′ ⊂ J, the lattice Z^(J∖J′) of meridians around D_J* injects into π₁(D_J′*). Exactly
  then sheaves of sets locally constant on the strata determine the stratified homotopy type, and the remark of 147
  scan 179 holds as written. The second condition is the vanishing of his maps π₂ → Z^(J∖J′).
- **Rests on.** The mapping spaces of an exit-path category are the homotopy fibres of the local links (here tori)
  over the larger stratum [B, my derivation from the standard description]; 147 scans 80, 88, 130, 179–180; 149
  scans 133–134, where he meets the same obstruction for varieties of higher dimension.
- **Plausibility.** High. It may be known; I know no reference.
- **What would decide it.** A proof of two pages; the tests (P¹, ∞), M̄(0,n), a toric variety.
- **Bears on.** III.4; V.3; the "maquette" of 149. **V 3, T 5. Pursue** (EXIT_ONE_TYPE, short).

### S3. The gluing theorem: his dévissage is exodromy

- **Statement.** For a stratified topos in his sense (an open subtopos, its closed complement, the tube), the shape
  is the homotopy pushout of open ← punctured tube → closed. Constructible sheaves of sets are the functors on the
  homotopy category of the exit-path category, constructible sheaves of spaces the functors on the exit-path
  ∞-category. The unfolding of a tame stratified space is a diagram of manifolds with corners indexed by flags of
  strata, and the space is its homotopy colimit; conical local structure is equivalent to the existence of the
  unfolding.
- **Rests on.** B1; STRATA C.1–C.8; the literature named in 1.1 (Book V). His axioms are unread (150, 151).
- **Plausibility.** High; the work is to match his axioms to the theorems.
- **What would decide it.** The return of rank 5.
- **Bears on.** V.3; III.4; *Les Dérivateurs* XII. **V 4, T 4. Pursue after stage 3** (DEVISSAGE).

### S4. Shapes over which colimits are homotopy colimits

- **Statement.** A small category A is filtered if and only if homotopy colimits over A preserve 0-truncated and
  1-truncated spaces; it is totally W∞-aspherical if and only if they preserve 0-truncated spaces
  (`RESULT_FILTERED_BY_ONE_TYPES.md`; TOTASPH C.5). Open beside it: total asphericity equals exactness of abelian
  colimits (H1); sifted and total implies filtered (H7).
- **Plausibility.** The theorem was proved today and is unchecked; its proof is short.
- **What would decide it.** PRESHEAF_TOTALITY Part F.1 or TOTAL_EXACT Part D.1.
- **Bears on.** II ms. 36–36ter; VII §10; and, through B1, 147 scan 180: it is the reason a van Kampen statement
  for a pushout must use the 2-pushout (PATHS A.2–A.7). **V 3, T 5. Pursue** (drafted; send first).

### S5. Three categories, three groups

- **Statement.** Let C_tri be the tripod with its symmetric group S₃ and its loops; C_Teich the moduli tower with
  forgetting, clutching and relabelling; C_all the hyperbolic curves over Q̄ with all dominant maps. Then the
  loop-preserving outer automorphisms commuting with S₃ form GT₀; the automorphisms of the genus-0 part of C_Teich
  form GT; those of C_all form Γ_Q. Γ_Q = GT is the statement that compatibility with finite étale maps between
  different curves (his condition b) at 142 scan 95) follows from compatibility with the tower.
- **Rests on.** Harbater–Schneps and LM3 E.7 for GT₀; Hoshi–Minamide–Mochizuki and LM3 F.14 for GT; Pop 2019 and the
  criterion of Hoshi–Mochizuki–Tsujimura (LM3b D.6–D.7) for Γ_Q; 142 scans 17, 21, 95–100 for his own passage from
  C_all to C_Teich; 149 for his return to C_all.
- **Plausibility.** The frame is right [B]. The equality is unknown.
- **What would decide it.** Nothing in reach decides the equality. In reach: his category of 142 made precise and
  its automorphism group computed from Pop's theorem and the Hom-form, or the gap located; LM3b C.7 and C.9
  (coverings); finite levels (S10).
- **Bears on.** III.1; all of Book III. **V 5, T 2. Record the frame; pursue the bounded parts** (GT_CATEGORY).

### S6. The cyclotomic kernel sees the cusps (found in this pass; unchecked)

- **Statement.** Let U be a hyperbolic curve over a number field K, π its geometric fundamental group, s any section
  of π₁(U) → Γ_K, and Γ° the kernel of the cyclotomic character. Then the centralizer of s(Γ°) in π is trivial if s
  is not cuspidal, and is the inertia group L_i if s is cuspidal at the cusp i. Hence s is cuspidal if and only if
  that centralizer is non-trivial, and the inertia groups are exactly the non-trivial centralizers of this kind for
  germs of sections.
- **Argument** [B, mine]. Proper case. Let z ≠ 1 centralize s(Γ°); take a characteristic open N with z ∉ N and put
  H = N⟨z⟩. For a finite extension K′, s(Γ_K′) normalizes H, so H is the geometric group of a covering defined over
  K′, and the class of z in H^ab is fixed by Gal(K̄/K′(μ_∞)). H^ab is the Tate module of a Jacobian, and its
  invariants under that group vanish because the torsion of an abelian variety over K′(μ_∞) is finite (Ribet, 1981,
  appendix to Katz–Lang; cited, not opened today). But z generates H/N ≠ 1. Affine case. The invariants of H^ab are
  its part of weight −2, so z lies in an inertia group by Nakamura's characterization of inertia elements (1994,
  near (2.1.1)–(2.1.4); from memory); the centralizer lies in one L_i; the normalizer statements of FINDINGS F5
  then put s(Γ) in the decomposition group of i.
- **Rests on.** 149 scan 55 ("hautement plausible", to be put among the "conjectures-clefs") and the margin of scan
  56; LM 2:sc433; FINDINGS F17 (2:sc483 is false as written) and hunch H5, whose note calls the point case
  conjectural. It agrees with LM3b D.5: a line with complex multiplication has an open normalizer and is not
  centralized by Γ°.
- **Plausibility.** Proper case: I hold it proved, given Ribet's theorem. Affine case: it hangs on one lemma quoted
  from memory. Novelty: one search found nothing; none is claimed.
- **What would decide it.** A check by GPT-6 Astra; then finitely generated fields (Katz–Lang), M(g,n), real places.
- **Bears on.** III (149; LM §§32–34); LM6. **V 4, T 5. Pursue** (CYCLOTOMIC_KERNEL; then into LM6).

### S7. The fixed-point conjectures B and B′

- **Statement** (149 scans 59, 63). B: every action of Γ on the universal profinite covering Ũ that comes from a
  section has exactly one fixed point in its completion, and so has Γ°. B′: for a "courbe de Poincaré" 𝒰 over K̄
  with completion 𝒳 and any action of Γ compatible with its action on K̄, Γ° has exactly one fixed point on 𝒳; no
  group π is assumed normalized.
- **Rests on.** B for Γ is the section conjecture with cusps in its limit form [B]. B′ is stronger; I know no
  counterpart.
- **Plausibility.** B: that of the section conjecture; uniqueness for Γ° may follow as in S6. B′: unknown. An
  action that normalizes no π is a tower of K-forms cofinal in the universal tower; the test is whether such towers
  exist beyond those of sections.
- **Bears on.** 149; LM6. **V 3, T 2. Record; one Part in the revised LM6.**

### S8. Sections and valuations

- **Statement** (149 scans 126–127). For K ⊂ L finitely generated over Q: a) every section of 𝓔_L over 𝓔_K
  normalizes the inertia group of a unique valuation ring of L over K with residue field algebraic over K, and comes
  from its decomposition group; b) for an elementary anabelian model U of L, every section of 𝓔_U lifts to 𝓔_L.
- **Rests on.** a) is the birational section conjecture in valuative form; its p-adic analogue is a theorem
  (Koenigsmann) [C, lookup 12]. b) is the step that 019 claims for p-adic fields.
- **What would decide it.** Over number fields, out of reach. In reach: the equivalences between a), b) and
  Conjecture A, written in his terms.
- **Bears on.** 149; LM6. **V 4, T 2. Record; state in LM6.**

### S9. GT and the motivic Galois group, level by level

- **Statement.** (i) Claimed in 2026: grt₁ is the Lie algebra of the unipotent motivic Galois group of mixed Tate
  motives over Z (B3). (ii) In genus one: grt_ell is a semidirect product of grt with a Lie algebra r_ell
  (Enriquez); the fundamental Lie algebra of the universal mixed elliptic motives is a semidirect product of that of
  mixed Tate motives with a Lie algebra u in which Pollack's relations from cusp forms are motivic
  (Hain–Matsumoto); the elliptic double shuffle Lie algebra is conjectured isomorphic to both [C, lookup 11].
  Conjecture: grt_ell is the Lie algebra of π₁ of mixed elliptic motives.
- **Rests on.** LM3 E.10 (Γ′(1,1) = GT); LM3b A.12–A.16 (the elliptic computation to degree 14; the normalizer
  quotient lives in degrees 6 and 10) and E.1–E.9.
- **Plausibility.** It is a conjecture of the field; (i) supports it.
- **What would decide it.** A proof in all weights is out of reach. Tables by weight and depth are in reach, and
  the programs exist in the LM3b return.
- **Bears on.** II.6 (13, 15); III.3 (§§52–53); LM8. **V 5, T 2 for the theorem, 4 for the tables. Pursue the
  tables; record the conjecture.**

### S10. His regular polyhedra as a test bench for GT

- **Statement.** (i) [G] The regular triangulated polyhedron of level n in cote 79 is the map of X(n) over X(1).
  (ii) GT₀ acts on it through the determinant modulo squares, exactly as Γ_Q does (B5): congruence levels cannot
  separate Γ_Q, GT and GT₀. (iii) The first separating candidates are regular maps with non-congruence groups. LM2
  left the case PSL₂(F₇) open (a shadow of order 1,024 whose arithmetic part is not determined: B.f5) and found a
  non-arithmetic solution of (I), (II) only on a group of order 13^747 (B.g15).
- **Rests on.** LM2; GT-shadows (Dolgushev and coauthors: arithmetic for dihedral 2-groups, 2024 [C, lookup 14]);
  Esquisse §4.
- **What would decide it.** Finite computations: GT₀- and GT-shadows and arithmetic images on PSL₂(F_q) for q = 7,
  8, 9, 11, 13 and on the bi-icosahedron.
- **Bears on.** IV.4 (79, 83, 72); III.3. **V 4, T 4. Pursue** (POLYHEDRA_SHADOWS; it can start from LM2 before
  79 returns).

### S11. The 1976 notes and integral schematization

- **Statements to test on the return.** (i) The complex of 136 is a functorial cochain algebra on semi-simplicial
  sets that computes integral cohomology with its products. (ii) The "structures multiplicatives" of 137 are
  strictly commutative cosimplicial algebras. (iii) The "analyseur" of 153 is the composition structure on
  integer-valued polynomials, whose algebras are the binomial rings (Borger–Wieland call it a plethory
  [C, lookup 15]). If so, B7 is where his line leads.
- **A question that is ours.** Is schematization a fundamental localizer? Let W_sch(k) be the functors that induce
  equivalences on finite-dimensional k-linear local systems and on their cohomology. Which of the axioms Loc (6),
  (7 F) does it satisfy (GALOIS B.6–B.7: a localizer of locally constant coefficients never has the reverse
  cofibration axiom and is proper only when it is W∞), and is Toën's schematization its localization?
- **Plausibility.** (i)–(iii): moderate. The question is well posed and uses returns we have.
- **Bears on.** II.9; VI.4–5 (112, 113); XVI. **V 4, T 3. Record now; pursue after stages 6 and 8**
  (SCHEMATIZATION_LOCALIZER).

### S12 to S20, recorded

- **S12. The level-1 principle.** B2, S2 and S4 together: ordinary categories of coverings, 1-topoi and functors
  modulo natural transformations carry exactly the 1-types; to see more one either glues 1-truncated pieces by the
  Grothendieck construction along shapes that are not filtered, or raises the coefficients. His path from 1981 to
  1991 is the discovery of both. This is the thread for the companions of III.4, V.3 and VI. **V 3, T 5. Write it.**
- **S13. Tame axioms.** His axioms of 120–121 define o-minimal structures or a named variant; his comparison of
  tame theories is Shiota's theorem. Decided by the return. **V 3, T 4.**
- **S14. Forms** [G]. A form is a pro-object of finite posets under refinement. Decided by the probe.
- **S15. A table for 13 and 15.** Which of his statements on motivic Galois groups are theorems for the groups of
  Nori and Ayoub, and which need the standard conjectures. **V 3, T 3.**
- **S16. 155 and Deligne 1990.** A fibre functor over k′/k and "la rigidité". Historical; decided by ten pages.
- **S17. Poincaré–Hodge algebras and Kähler packages.** A comparison of inductions, for the commentary. One
  programme I considered does not exist: motives built from the combinatorial Kähler packages are sums of Tate
  objects, because every class there is algebraic, so their Galois group is G_m.
- **S18. The standard conjectures beyond abelian varieties.** No result in hand bears on them. Record only.
- **S19. The residue of Book I.** What his plans and drafts contain that is neither in print nor in the Stacks
  project. Expected small.
- **S20. 93, 159, 64** [G]. Gauss–Manin, the Cartier operation and projective connections in 1972–82: possibly one
  subject, the differential equations of uniformization and their p-curvature. Decided by the probes.

### Ranking

| Rank | Item | V | T | Decision | Needs |
|---|---|---|---|---|---|
| 1 | S6 cyclotomic kernel | 4 | 5 | pursue now | nothing; 149 is back |
| 2 | S1 exit-path tower | 5 | 3 | pursue now | LM3, LM3b, STRATA; 147 is back |
| 3 | S4 shapes | 3 | 5 | pursue now (drafted) | nothing |
| 4 | S2 one-category criterion | 3 | 5 | pursue now | nothing |
| 5 | S10 polyhedra and shadows | 4 | 4 | pursue now, extend after 79, 83 | LM2 |
| 6 | S3 gluing theorem | 4 | 4 | pursue after rank 5 | 150, 151 |
| 7 | S11 schematization | 4 | 3 | pursue after 137, 136, 153, 112, 113 | returns |
| 8 | S9 elliptic tables | 5 | 4 (tables) | pursue as a Part of LM8 | LM Part II reading |
| 9 | S5 three categories | 5 | 2 | frame recorded; GT_CATEGORY | reader of 142 |
| 10 | S12 level-1 principle | 3 | 5 | write into the companions | — |
| 11 | S8, S7 | 4, 3 | 2 | record; Parts of LM6 | — |
| 12 | S13, S15, S16, S17, S19 | 2–3 | 3–5 | commentary, on return | returns |
| 13 | S14, S20 | ? | ? | probes decide | probes |
| 14 | S18 | 5 | 1 | record only | — |

---

## 4. How this changes the questions we ask along the way

### 4.1 Transcription prompts and their context zips

| Change | Reason | From which stage |
|---|---|---|
| A build check: the context zip is not empty, has its README, and every listed file exists | The zip of MPL_147_048-137 held nothing; 222 notes have no comparison [C] | now |
| One stream always; 45–70 scans for keystone chapters (Book III, V, the dossier, II.9, probes), 90 for calculation folders and drafts of printed texts | With a full second pass the first-pass error rate matters less than coverage; Pro runs are the scarce unit. The 45-scan one-stream package had 0.73 errors per 100 words, the others 1.56–2.15 [C] | next send |
| A sign table per period of his hand in the main zip: his recurring signs and abbreviations, taken from pages the second pass has confirmed. No mathematics in it | Streams of one package read his curled G three ways; 16 of 17 errors carried no doubt mark [C] | 1980s hand now (from the Longue Marche second pass); 1960s hand after packages 11, 30–33 are checked |
| The context zip is built per bridge: neighbouring transcriptions as now, plus the chapter's carry-questions (4.3), the register entries of linked chapters, and our statements the chapter meets, each with its status. Opened after the freeze, as now | The notes on 147 could not know STRATA or the Longue Marche findings; a note is as good as its context | ranks 4 and 5 |
| A zip for the ranks that have none (2, 7, 15, 16, 18–20, 22, 25): outside witnesses (printed texts and letters) and the content map | The notes can then say what the folder adds to print | built packages |
| Notes in compact rows: id; scan; kind; his words (25 words at most); the point (40 words); bridge tag; context hit (file, scan, relation); confidence for own ideas. Long form for at most 15 items a package, those Pro judges most consequential | Notes are 850 tokens a page against 570 of text [C]. At about 300 a reader takes about 250 pages in place of 150. The existing notes are compacted by script | next send |
| Two more kinds of note: *retraction* ("faux", "Remords", "visiblement faux") and *self-answer* (he answers what the context shows he asked earlier) | Both occurred in the first returns and were filed as "conjecture" | next send |
| Two standing questions in every notes task: what on these pages dates them (dates, persons, results of others, paper, versos); which other manuscripts he cites or announces | Layers in 142; the chronology of the GT relations; an internal citation graph that finds misplaced and missing folders (cote 110) | next send |

The rule that no later mathematics enters the transcription stays. Everything above is in the notes phase or is
palaeographic.

### 4.2 The second pass: the global pass and the register

**What the global pass looks for, beyond headers and concordance.**
1. Date layers, with the evidence (stage 0, cote 142).
2. Notation: every symbol gets its id in the archive-wide table; each occurrence of an ambiguous one (Γ(g,ν)) is
   tagged with its meaning.
3. Internal references ("cf. pp. 74′ ff.", "mes notes sur …"): rows of the citation graph.
4. Retractions and self-answers, linked to the entries they touch.
5. Every "Programme".
6. Outside witnesses collated and credited (for 149 the "Notes anabéliennes"; for 147 and 151 Carmona's fragments).
7. For calculation folders: every table and enumeration, for recomputation by script.
8. For each explicit question or conjecture: a search of the register so far before a status is written. The answer
   may be in another book.
9. The joint pass: III.1 with III.4; V.3 with 147 §§11–13; II.9 with VI.5.

**The register: one for the archive, in two tiers.** The ten notes files hold 1,484 items for 611 pages, 118 of them
classed as conjectures [C, counted today]. At that rate the archive yields about 26,000 items and about 2,000
conjectures and questions. Tier A (his explicit questions, conjectures, expectations, programmes, retractions) gets
a researched status. Tier B (claims without proof) is rows only, generated from the notes.

Fields of a tier-A entry:

| Field | Content |
|---|---|
| id | stable: cote, scan, running number |
| place | cote, scan, manuscript page; book and chapter |
| date | with the evidence and its strength |
| his words | the French, short |
| kind | question, conjecture, expectation, programme, claim, retraction, self-answer |
| statement | typed: objects, hypotheses, conclusion; notation ids |
| bridge tags | B1–B12, more as they appear |
| links | same-as, refines, answers, retracts, uses: to other entries, in any book |
| status today | proved (by whom, where); refuted; open; claimed 2026, unrefereed; ours (the number in NEW_RESULTS or the return and its review status); not known to have been studied; superseded by his own later text |
| how the status was verified | on the primary text; from a return, unverified; from memory |
| what would decide it | one line |
| prompt | the research prompt that carries it, if any |
| depends on a doubtful reading | scan and line, or no |

Entries to seed today, from what this pass read: 147 scan 60 (two levels); 147 scan 104 (Programme); 147 scan 179
(Remarque) and scan 180 (Remords; its closing question is *answered by* XII app. ms. 17–18 with STRATA C.3); 149
scans 48, 52, 55–56, 59, 61–63, 100, 126–127, 133–134; 142 scans 17, 21, 96, 100; 146 scan 106; the entries behind
FINDINGS F1–F27 of the Longue Marche; the audit rows of *Les Dérivateurs* already used in the reviews (II-C-004,
II-C-010 and the questions of XVI listed in F3-3).

### 4.3 The Fable readers

**Changes to every brief.**
- The reader of a keystone chapter reads the first pass (section 5.3).
- It receives the bridge rows of 1.2 that touch its chapter, the register entries linked to it, and the carry-questions
  below.
- Besides FINDINGS, HUNCHES and prompts it writes two short files: PREDICTIONS (what the chapters still to come
  should contain if its reading is right) and BREAKS (what in an earlier companion, prompt or placement must
  change). The first makes each stage a test of this war game; the second is how a retcon is caught early.
- It lists every reading its mathematics depends on, with scan and line, for the second pass.

**Carry-questions by chapter.**

| Reader | Carries |
|---|---|
| 147 | Write the MDT-structure of §§9–10 as a category and compare it with the transporter category of LM3 F.5–F.7. State the remark of scan 179 and the Remords in exit-path terms; is S2 what he needs? Which of his constructions are left unfinished, and which does 146 complete? Is "J'ai l'impression" (scan 60) the two-level principle, and what does he say would prove it? What are the four elementary types for, and does scan 165 survive scan 180? |
| 149 | It is the anabelian notes: collate with "Notes anabéliennes". For each of the *Conjecture fondamentale*, A, B, B′, a), b): the exact statement, its relation to FINDINGS F5–F8, F15–F18, F24–F25, and its status. Check S6 against his own argument around scans 55–56 and 61. What is the "maquette" at infinity of scans 133–134 and is its π₂ question S2? Which statements go beyond the letter to Faltings? |
| 146 | The finite-object groupoids S₀T_G: are they skeleta of the transporter categories of LM3 F? The conjecture of scan 106 (contractible space of disc choices) and its use in the sewing. What the dated sheets (scans 126–134) fix |
| 142 | Define his category of Galois–Teichmüller (scans 3–22) with its arrows and the "enveloppe profinie"; compare with LM3 F.2–F.4. Write the equations of scans 25–42 against (I), (II) of LM2 B.m2 and carry out the check under complex conjugation he asks for. State conditions a), b) of scan 95 and compare with Pop's theorem; what fails for G_m (his margin). Date each layer. Scans 108–114 against Book IV |
| 144, 148, 143, 145, 141 | The three checks of stage 2. Every return to a question of the Longue Marche: which, and with what result |
| 150, 151, 152, 120, 121 | His axioms for a stratified space and for a stratified topos, typed. Is the tube a datum? Does he resolve the Remords? His axioms for tame spaces against o-minimal structures; his comparison statement against Shiota. Which of the three readings of 152 holds |
| 16, 47, 54, 44 | The axioms of a Poincaré–Hodge algebra; every formal deduction; any inductive strategy for B and the index theorem, and where it stops. In 47: is involutivity stated, proved, for abelian schemes? Dates |
| Crystals | The "yoga in three cases" of 1967; every statement on Barsotti–Tate groups that is now a theorem (de Jong; Berthelot–Breen–Messing) or still open; what 8 computes |
| The dossier, 158, 137, 133 | For each of NEW_RESULTS 1–12 and each answer of F3-3, its 1983 form if any. Is 115 the bimodule of STRATA C.1? What 137 means by "structures multiplicatives" and 133 by "Witt" |
| Motives | The table of stage 7. His exact sequence for motivic Galois groups over Q. Any statement of the period conjecture. What "Motifs" leaves out of cote 12 |
| 136 | (i)–(iii) of S11. What the "topos de De Rham" is and what its "faisceautisation" does. The plan of the lecture |
| Maps, 79, 83, 64 | Is the polyhedron of level n the map of X(n)? What "regular polyhedron over a ring" is, as a definition. The bi-icosahedron against M(0,5). What 138 knew before Belyi |
| 156 | His definition of a form, a network, a cutting, a workshop, typed. Whether S14 holds. What "Analysis situs" changes from the first version to the fourth |

**Bridge readers** (new; about ten, 45 Fable points). Each reads two or three checked chapters from different books
with the returns that join them: gluing (147 §§11–13, 150, 151, XII and its appendix, STRATA); schematization (133,
137, 136 in extract, 153, 112, 113, *Pursuing Stacks* VI–VII); the Galois group twice (13, 15, 149, LM §§5, 32–36,
LM3 D–E); maps and modular polyhedra (138, 76, 79, 83, 64, LM §§36–37 and 53, LM2 C); finite models (120, 121, 156,
V and XVI §6, CATHOT). A last reader takes only the FINDINGS, PREDICTIONS and BREAKS files of all the others and
rewrites sections 1.2 and 3 of this document.

### 4.4 The research prompts: directions and order

Three transcription runs to one research run while the protected core is being sent. Each prompt keeps the form
fixed on 12 Nov: the results it builds on with their status, what counts as done, proofs asked for, never a status
report.

| Order | Prompt | Asks for | Builds on | Can go |
|---|---|---|---|---|
| 1 | PRESHEAF_TOTALITY, TOTAL_EXACT | Part F.1 and D.1 first: the check of today's theorem (S4); then their pushes | drafted | now |
| 2 | REVERSIBLE_LOCALIZERS, INDLOCAL, FINMON, S2COUNT | as drafted | drafted | now |
| 3 | CYCLOTOMIC_KERNEL | check the proper case of S6 step by step; prove the affine case with the lemma on inertia elements cited from the source; extend to finitely generated fields, to M(g,n), to real places; derive the corrected §34 | 149 scans 55–63; F5, F17; LM3b D | now |
| 4 | EXIT_ONE_TYPE | prove or correct S2; compute the cases named there | 147 scans 80, 88, 130, 179–180 | now |
| 5 | LM6, revised | his conjectures of 149 beside those of 1981; S7, S8 as Parts | LM6 draft; 149; F7, F15–F18, F24–F26 | after the revision |
| 6 | LM5, revised | add 147 §§11–13 and 149 scans 3–23 | LM5 draft; LM3 C.10–C.11; LM3b H.6–H.8 | after the revision |
| 7 | EXIT_TOWER | S1: identify his MDT-structure with the completed transporter category; prove scan 179 in his formulation; attack LM3 F.16, LM3b E.4, E.9, H.9; the equations of 142 scans 25–42 against (I), (II) | LM3 F; LM3b E, H; STRATA F | after the reading of 147 |
| 8 | LM4, revised; GT_CATEGORY | S5: his category of 142, its completion, its automorphisms | 142; Pop; LM3 F.2–F.4 | after the reading of 142 |
| 9 | POLYHEDRA_SHADOWS | S10 | LM2 B.f, B.s, C.r | now for PSL₂(F₇); extended after 79, 83 |
| 10 | LM7, LM8 with the elliptic tables (S9) | as drafted, plus tables by weight and depth | Parts II–IV read by Fable | after those readers |
| 11 | DEVISSAGE, TAME_AXIOMS | S3, S13 | 150, 151, 120, 121 | after rank 5 |
| 12 | SCHEMATIZATION_LOCALIZER; the 1976 lecture reconstructed; the 1983 origins of our results | S11; stage 6 | 137, 136, 133, 153, 112–118, 108 | after stages 6 and 8 |
| 13 | A table for 13 and 15; 47 if it has statements without proof | S15 | motives | after stage 7 |

About 25 research runs in all with the eleven drafted ones.

### 4.5 The transcription order

Section 2.5, order W: the built packages; rank 4; rank 5; the eight probes; rank 3; rank 9 with 137 and 133; rank
6; the rest of 136; rank 10 with 79, 83, 64 and the two popular texts; rank 11; then 67, rank 13, the rest of rank
14, the rest of 93 with 161-5, 154 and 80 if the probe says so, 127 and 128; then the rest in the cut order of
section 5.4 read backwards.

---

## 5. Scope and expectations

### 5.1 The protected core

What must be through Pro before it can end, whatever else is cut: the pages our results meet, the pages nobody has
read on which the shape depends, and the texts with no counterpart in print.

| Part | Cotes | Pages |
|---|---|---|
| III | 144, 148, 143, 145, 141; 64, 67, 159; 138 | 760 |
| V | 150, 151, 152, 120, 121; 156-1, -2, -3, -5, -8, -9; 154 and 80 if the probe says so | 924 |
| VI | 158, 103–109, 111–118, 135 | 437 |
| II.9 | 137, 136, 133, 153 | 523 |
| II.1–8, handwritten | 16, 47, 54, 44; 4–9, 100; 14, 13, 12, 15, 18; 10, 11, 56, 60; 155 | 1,448 |
| II.3 | 93, if the probe says so | 235 |
| IV | 76, 88, 70, 75, 161-6; 79, 83, 72, 86, 85 | 1,025 |
| I | 21, 22, 23, 26, 35, 48, 102; 127, 128 | 242 |
| Front door | 161-3, 161-4 | 85 |
| **Core** | | **about 5,700** |
| Outside the core | section 5.4 | about 4,450 |

### 5.2 What the budget allows

**Pro.** The core is about 63 runs at 90 scans or 81 at 70; with one research run to three, 85 to 108 runs; at nine
a day, 10 to 12 days: the core can be through by 25 November [G for the rate]. Everything is 113 runs at 90 or 145
at 70, with 25 research runs 138 to 170: 15 to 19 days, the edge of November.

**Opus** (0.025 points a scan [C]). The returned pages and the core: 6,290 scans, about 157 points. The four weeks
give about 162 points for the archive (12 this week by the report, then 50 a week if nothing else uses the Opus
half). So the core gets its full second pass and nothing else fits. Outside the core: a full pass would be about 111 points more; at the report's
light rates (a quarter against print) about 45, a fifth week.

**Fable** (314 points; 4.5 a reader).

| Use | Readers | Points |
|---|---|---|
| 147, 149, 146, 142 | 4 | 18 |
| The Longue Marche, Parts II–IV and the draft | 4 | 18 |
| The *Dérivateurs* returns 5–8 | 4 | 18 |
| The rest of the core, at about 250 pages a reader with compact notes | 23 | 104 |
| Bridge readers and the reader of the totality | 10 | 45 |
| Outside the core, on the transcription alone (380 pages a reader) | 12 | 54 |
| Consultations of the three experts, debate, re-reads after reading changes | — | 30 |
| Reserve | — | 27 |
| **All** | **57** | **314** |

With the notes at their present 850 tokens a page the core alone needs 38 readers (171 points), and the bridge
readers and the reserve disappear. The compact notes of 4.1 are what pays for the bridges.

### 5.3 The pipeline change

For the keystone chapters (the core of Books III, V, VI and II.9, and the probes) the Fable reader starts when the
first pass returns. It reads the transcription with Pro's notes, opens a scan where a formula is in doubt, and lists
every reading its mathematics depends on. The second pass takes that list first and sends back each change that
alters a statement; the reader answers as a consultant (about 0.05 Fable points a question [C]). The edition still
waits for the full second pass. Reason: a first-pass error rate of 0.7 to 2.2 per 100 words does not prevent
mathematical reading, and the alternative is that the prompts for Pro are written in December.

### 5.4 What to cut first if Pro mode ends early

In this order; the first is cut first. Each can go later by another route, or be read against print.
1. Ranks 21 and 24: drafts and remnants of the printed seminars (1,069 pp.).
2. Rank 23: the old elliptic-curve notes and the Picard typescript (510 pp.; its typed sheets go to the API in any
   case).
3. Ranks 19 and 20 and the rest of 22: the notes behind FGA and SGA 7, and the 1960s folders (about 1,080 pp.). Cote
   91 (Hom functors by non-projective methods) last among them.
4. Rank 25 without cote 66 (213 pp.).
5. Rank 17: the three earlier versions of Analysis situs (294 pp.).
6. 161-1, 161-2 and 19 (225 pp.).
7. The calculation folders: 77, 78, 84, 82, 73, 87, 89; 69, 74 (about 900 pp.).
8. 71, 81, 132, 161-5 (about 160 pp.).

Inside the core, if it comes to that: 10 (largely typed) and 60 first; then 86, 85; then the rest of 93.

### 5.5 What exists when (if Pro lasts through November)

| By | Transcribed | Checked and published | Read by Fable | Results |
|---|---|---|---|---|
| 19 Nov | built packages, ranks 4 and 5, the probes | III.4 and III.1 checked (the report's plan) | 147, 149, 146, 142 | returns of the six *Dérivateurs* prompts, of CYCLOTOMIC_KERNEL and EXIT_ONE_TYPE; content map; register and notation table in a first state |
| 30 Nov | the core | the anabelian notes; III.2, III.5; V.1, V.3; the *Dérivateurs* companion closed with 158 | the dossier, 137, 133; the stratified spaces; the dated notes | about 25 research returns; LM5, LM6 answered; EXIT_TOWER |
| mid-December | what remains outside the core, as far as Pro allows | the core checked: Books III, V, VI (new text), II.9, II.4–6, IV.1, 2, 4 | the core; the bridge readers | sections 1.2 and 3 of this document rewritten from the readings; companions of III.4, V.3 and VI with the level-1 thread |
| January | — | Book I as a map with its residue; the rest of Book IV; translations, after the glossary | outside the core | the Longue Marche book with its new chapters |

### 5.6 Risks

1. *Pro ends or disconnects.* The core first; one stream; checkpoints every ten pages; a second account doubles the
   slots.
2. *The second pass overruns.* The core first; variants and drafts of printed texts last or light.
3. *A status is wrong.* 008, 019, 031, 032 are claims. S6, S2 and today's theorem are ours and unchecked. No
   companion states any of them as a theorem before a check; a proof that uses one says so.
4. *A reading error carries a conclusion.* The dependency lists of 5.3.
5. *The experts' contexts end* (630k to 855k of 1M [C]). Their handoff files are current. Two consultations are
   worth making now: the Longue Marche expert on the lemma S6 needs in the affine case; the *Dérivateurs* expert on
   the reading of 147 scans 179–180 given in 2.2.
6. *The register outgrows its makers* (about 26,000 items). Two tiers.
7. *Sending is by hand.* A queue of the next twenty runs, transcription and research interleaved, kept ready.
8. *This document steers by guesses.* Every [G] is marked. The probes, the PREDICTIONS files and the last bridge
   reader test them; sections 1.2 and 3 are rewritten when they have.

---

## 6. What I would change in the medium-effort plan

Kept: the front door, the six books, the three layers of a page, the cote order as second index, the API route for
clean typescripts, "unread mathematics first". Changed:

1. **A reconnaissance stage before any placement is used.** The plan placed most of the 178 cotes from the archive's
   titles and notes; it opened pages of 17. Two of the first four returned differ from their titles.
2. **Cote 149 is its own chapter** (the anabelian notes), not the sequel of 147.
3. **147 §§11–13 are also the first position of V.3.** The edition stays in III.4; Book V starts from them.
4. **The order**: probes; rank 9 with 137, 133 before rank 6; 79, 83, 64 with rank 10; 133 out of rank 22.
5. **Bridges are objects of the plan**: twelve named statements (1.2), a tag in every note and register entry,
   ten readers, a share of the Fable budget. On the site: beside the story in six steps of the recommendation §3, a
   page "one problem, six forms" that links the bridge pages.
6. **One register for the archive**, in two tiers, with links between entries (answers, retracts). The plan writes
   it chapter by chapter.
7. **One notation table and one glossary for the archive**, before the first translation.
8. **Book I**: subject keys in place of chapter numbers from one plan; the Stacks project as a column of the map;
   the development is chapter V from cote 25 and a short residue. "The unwritten chapters written out with proofs"
   would mostly rewrite what exists.
9. **Book IV**: the literature corrected (it has successors: abstract regular polytopes, polytopes over finite
   fields, regular dessins, GT-shadows); its core (79, 83, 72, 86, 85) in the first tranche; to be described, once
   the probes confirm it, as the combinatorial theory of the modular curves and of the forms of P¹.
10. **II.9 with VI.4–5 as one unit of reading**; its literature corrected (integral homotopy theory: Toën 2020,
    Horel 2024 and what leads to them).
11. **The pipeline**: for the keystone chapters Fable reads the first pass; prompts go out while Pro exists.
12. **Fable by yield, not one reading of every page**: none for drafts of printed texts until the map finds
    something; one a chapter for the calculation folders; the bridges read twice.
13. **Notes in compact rows**; two new kinds (retraction, self-answer); two standing questions (dating; citations).
14. **A context zip for every rank**, built per bridge, with a build check.
15. **Three corrections to `SECTIONS_STATE.md`**: §18 (the source of "Notes anabéliennes" is cote 149; cote 142
    begins with the categories of Galois–Teichmüller); §11 ("no identified successor" for the regular polyhedra);
    §16 (the later development of 136–137).

---

## Lookups made (15), and what each settled

1. Cartan, "Théories cohomologiques": Invent. Math. 35 (1976), 261–272, confirmed; its content not shown. The link
   to Grothendieck's lecture stays [B].
2. Toën, "Le problème de la schématisation de Grothendieck revisité" (Épijournal Géom. Algébrique 4, 2020;
   arXiv:1911.05509): schematization over Z; the group scheme H whose functions are the integer-valued polynomials;
   homotopy groups of the affinization are H-modules, not O-modules.
3. Carlson–Haine–Wolf, "Reconstruction of schemes from their étale topoi" (arXiv:2407.19920): the conjecture of the
   letter to Faltings for finitely generated fields of characteristic 0 (seminormal schemes) and, after perfection,
   in positive characteristic; follow-ups by Carlson–Stix (sub-p-adic fields) and Berens.
4. zbMATH record of Cartan's paper: not reachable.
5. Horel, "Binomial rings and homotopy theory" (J. reine angew. Math., 2024; arXiv:2211.02349): a fully faithful
   functor from nilpotent spaces of finite type to cosimplicial binomial rings; an integral version of GT. Antieau,
   arXiv:2308.07288, confirmed as a reference only.
6. Monson–Schulte, "Reflection groups and polytopes over finite fields" I–III (Adv. Appl. Math. 2004, 2007, 2008).
7. The record of Cartan's paper at mathdoc: reference only.
8. González-Diez–Jaikin-Zapirain: Γ_Q acts faithfully on regular dessins (from surveys that cite it).
9. Pop, "Finite tripod variants of I/OM" (Invent. Math. 216, 2019): publication confirmed; its statement was not
   shown, so the identification with 142 scan 96 stays [B].
10. Shiota, "O-minimal Hauptvermutung for polyhedra I" (Invent. Math. 196, 2014): definably homeomorphic compact
    polyhedra are PL homeomorphic; every compact definable set is definably a polyhedron.
11. Enriquez, "Elliptic associators" (arXiv:1003.1012); Hain–Matsumoto, "Universal mixed elliptic motives"
    (arXiv:1512.03975): the semidirect products; Pollack's relations are motivic; the three Lie algebras are
    conjecturally isomorphic (Lochak–Matthes–Schneps).
12. A search for the statement S6: nothing found; Koenigsmann's theorem on birational sections over p-adic fields
    confirmed.
13. The icosahedron and M(0,5): the Esquisse ties them (through D. Roberts's slides); the real locus of the
    compactification has twelve pentagons. The word "bi-icosaèdre" was not found outside our files.
14. Bortnovskyi–Dolgushev–Holikov–Pashkovskyi (arXiv:2405.11725): GT-shadows for dihedral groups of 2-power order
    are arithmetic.
15. Borger–Wieland, "Plethystic algebra" (Adv. Math. 194, 2005): binomial rings are the algebras over the plethory
    of integer-valued polynomials. Lazard's "analyseurs" (1955) was not found by the search and stays [B].

