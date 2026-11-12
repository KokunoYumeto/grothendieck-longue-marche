# The Montpellier programme: war game, round 2

Claude Fable 5.2 (effort max), round 2, 12 Nov 2026 (written 16:55–17:25 UTC, clock checked). No sub-agents. Round 1 is
`PROGRAM_WARGAME_20261112.md` (Claude Fable 5.2, effort max, the same day); it stopped at its compute bound and is left
as it is. This file is to be read first: its summary and guide map replace round 1's. Sections 1.1, 1.2, 2.3–2.6, 3 and
4 of round 1 stay valid except where section 1 below changes them.

**Marks.**
- **[C]** checked today: in a file, return or transcription I opened, or by a web lookup listed at the end.
- **[B]** believed: from my knowledge of the literature or my own derivation; not verified today.
- **[G]** guess: a prediction about pages nobody has read yet.
- Results our files call "claimed, unrefereed" (OpenAI families 008, 019, 031, 032; arXiv papers of 2026) keep that
  status. Statements of the Pro returns are "the return's claim" until one of our reviews has passed them.
- Places in the archive: cote and scan number of the archive PDF, as the returns give them.
- "Astra" is GPT-6 Astra (ChatGPT Pro mode); a "Pro run" is one run slot of it. "Opus" is Claude Opus 5.5 at max.
  "Fable" is Claude Fable 5.2.

**Read for round 2** (about 250k tokens of sources): round 1 in full; `EXISTING_EDITIONS_CHECK_20261112.md` in full;
the return MPL_16+47+54+44 (the transcription of all 82 scans; of the notes the 23 items classed as conjectures and the
three post-freeze sections on the standard conjectures, the Fourier transform and duality); of the *Dérivateurs*
returns STRATA, PATHS, BISITE and RESIDUE the summary sections of the reports and every row of the results registers
(statements cut at 200 to 300 characters), with the expert's handoff file in full; cote 149 in full (both returns);
the opening 19-page text of cote 142; `MANIFEST.csv` for titles and page counts. Not read: any scan image; the
doubts registers; the page-specific notes of the Book II return other than those named; the audit appendices of the
four reports and the proofs inside the four returns.

---

## Summary (replaces round 1's)

1. **The shape stands, and his own text now carries its main bridge twice.** The six books are one problem: take a
   geometric object apart along a stratification and rebuild it. Cote 149 (the anabelian notes of 1983), read in
   full, ends on that problem: the strata D_J of a boundary with normal crossings, tori T^J, a "maquette
   simpliciale", the map π₂(D_J) → T^J (scans 128–136). It is 147 §§11–13 again, in the arithmetic setting [C].
2. **Book II on real content.** The first package (16, 47, 54, 44) holds: the ring of correspondences as an algebra
   over a universal Lefschetz ring, with the induction on hyperplane sections and the two letters to Coates (16);
   the Fourier transform on derived categories of abelian schemes with its inversion theorem, written after 1968
   (47; Mukai 1981, Laumon 1996); de Rham H¹ through the universal vector extension (54; it belongs with the
   crystals); a programme of seven theorems on intermediate Jacobians with a height formula (44). The literature
   meets it at every point, our results at none. A third of the 82 scans are reused sheets and covers [C].
3. ***Les Dérivateurs*, returns 5–8.** 368 statements, none reviewed at effort max. They hold the gluing theorem in
   Cat, his own counterexample (S² with a point), the exit categories of the genus-zero moduli, forgetting a point
   as a proper and non-smooth functor in all genera, the six operations on Cat, and open tests on spaces. They meet
   147 §§7–13, 150, 151, 115 and the dossier around *Pursuing Stacks*. RESIDUE is the residue of open questions,
   not a text on residues [C]. Sixty of their rows are reviewed first; until then they are claims.
4. **The second pass at 0.04 points a scan.** A full pass of the core costs 259 points (248 with a light rate for
   reused sheets), not 157. The four Opus weeks, about 162 points, cover Book III with rank 4, Book V with 156,
   the dossier, II.9 and Book II through the motives, about 4,100 scans. Book IV, the periphery of III and the
   rest of II need a fifth and sixth week, or a light pass (section 4).
5. **Pro.** The core is 5,791 pages to send: 65 to 72 runs of 90 scans, 83 to 92 of 70. With research runs one to
   three it can be through by 22 to 26 November [G for the rate]. The send order is the protection order (4.4).
6. **The division of labour** is the plan's frame: GPT-6 Astra transcribes and answers the research prompts;
   Claude Opus 5.5 does the whole second pass and the global pass; Claude Fable 5.2 reads, does the mathematics
   and writes the prompts. Section 5 gives four weeks in those four columns.
7. **Outside editions.** *Pursuing Stacks*, the Esquisse and EGA V are collated over the API from the outside
   texts; cote 25 ("Nouveau EGA V") is transcribed from the scans; the handwritten leaves of the *Pursuing Stacks*
   folders join the Pro queue with the dossier.
8. **Order.** Round 1's order W, with: the crystals now; two more probes (cote 43; the short notes 49–52); cote
   115 as a keystone of the dossier.
9. **Found in this pass, unchecked** (section 7). R2: for any section of a hyperbolic curve over a number field,
   the centralizer of the image of the cyclotomic kernel is trivial or an inertia group; this is S6 of round 1
   argued in full, and it settles several statements of 149. R3: his "à vérifier" of 149 scan 45. R4: the limit
   Galois action at a place of bad reduction is not that of a curve, by weights and by Torelli, with one case
   left. R1: the threshold he asks for in 16 scan 29 is 6.
10. **Prompts.** The six packaged ones go now. To write first: CYCLOTOMIC_KERNEL, FLAGGED_149 (every step that 149
    and 142 mark "à vérifier"), EXIT_ONE_TYPE, FOURIER_1970; then LM6, LM5, EXIT_TOWER and GT_CATEGORY revised
    by the readers of 149, of the gluing chapters, and of 142 (section 6).

## Guide map

**Where we are** [C]. 693 of 10,761 Pro pages are back: cotes 147, 149, 146, 142, 45 pages of cote 1, and 16, 47,
54, 44. The crystals (356 scans) are built and waiting. No archive package has had its second pass. In the two
war-game passes Fable has read 149, the opening of 142, the first Book II return and samples of 147; no reader
with a brief has run. Research prompts: six packaged and
unsent; LM4–LM8 drafted, LM4–LM6 to be revised; four specified here.

| Book | State | Next | Bridges | Results that meet it |
|---|---|---|---|---|
| Front door | not started | the Esquisse by collation from cote 119 (API); 161-3, 161-4 with the maps | all | — |
| I. Elements, continued | not started | cote 25 from the scans (API); the plans (rank 3); the map against print and the Stacks project | B11 | EGA and SGA editions |
| II. Cohomology and motives | 16, 47, 54, 44 back; crystals built | crystals now, with 54; motives after the dossier | B3, B4, B7, B8, B9, B13, B16 | the literature (2.3); 008 (claimed) |
| III. The Long March | LM done; 142, 146, 147, 149 back | rank 4; the readers R-149 and R-GLUE; LM4–LM6 revised | B1–B6, B12, B13, B14 | LM findings; LM2, LM3, LM3b; STRATA F, RESIDUE H (claims); R2–R4 |
| IV. Maps and polyhedra | not started | probes 79, 83, 138; then the maps with 64 | B5, B6, B12 | LM2 |
| V. Tame topology, forms | 147 §§11–13 and 149 scans 128–136 back | rank 5; probes 156-1/2 and 154 | B1, B10, B13, B15 | STRATA A–C, BISITE D, RESIDUE G (claims) |
| VI. Stacks and derivators | companion at 28 of 32 chunks; returns 5–8 unreviewed | the six prompts; the dossier with 115, 158, the leaves of 134; *Pursuing Stacks* by collation | B1, B2, B7, B8, B10, B14, B15 | NEW_RESULTS 1–12; returns 5–8 (claims) |
| Workshop | 45 pp. of cote 1 | the register and the notation table, for the whole archive | — | — |

**Next, in order.**
1. Before sending: the repairs of round 1 (one stream; the 31 dropped scans; the check that no context zip is
   empty) and a "sheet kind" column in the inventory.
2. Send: the crystals; rank 4; rank 5 with 153 and 155; the ten probes; the leaves of 134 with 158.
3. Send the six packaged prompts; write and send CYCLOTOMIC_KERNEL, FLAGGED_149, EXIT_ONE_TYPE, FOURIER_1970.
4. Opus, with this week's 12 points: 149, 147 §§9–13, the opening and the last 29 scans of 142.
5. Fable: R-149 and R-GLUE (section 5, week 1).
6. Outside the meters: the reconnaissance pass (title sheets, reused sheets, dates); cote 25 and the collations
   over the API.
7. Week 2: the review of the 60 rows of returns 5–8 that the archive needs; then section 5.

**Where to look.** What changed in round 1: section 1. Book II: section 2. Returns 5–8: section 3. Budget and cut
order: section 4. The four weeks: section 5. Prompts: section 6. Results: section 7. Round 1 remains the reference
for the stages (its 2.3–2.4), the fields of the register (4.2) and the risks (5.6).

---

## 1. What the new reading changes in round 1

### 1.1 Shape: the books (round 1, section 1.1)

| Book | Change | Reason and evidence |
|---|---|---|
| II | Objects of its first group: rings of correspondences with a Lefschetz element (the general "Poincaré–Hodge algebra" appears only in order 2); the Fourier functor on derived categories of abelian schemes; the universal vector extension; the abelian varieties P^i(X) with a height pairing. To "what he had" add: the inversion theorem for the Fourier functor, written after 1968 | 16 scans 3–18, 25–29; 47 scans 3–8; 54 scan 3; 44 scans 2–4 [C]; section 2 |
| II and the archive's folders 06–09 | The first "Book II" package came from three archive folders: 16 from *Théorie des motifs*, 44 from *Jacobiennes*, 47 and 54 from *Variétés abéliennes*. That folder holds more short undated notes of the same kind, which round 1 left on the periphery: 49 (Picard of abelian schemes, 9 pp.), 50 (10), 51 ("Bonne réduction", 22), 52 (Torelli, 13). Cote 43 (generalized Jacobians, 207 pp.) is the tool of 149 Théorème 3 and of 142 Proposition 2 | `MANIFEST.csv` [C]; cote 47 is 10 pages and holds a theorem |
| III | Cote 149 is a text in four numbered sections, with proofs: §1 "Résultats de fidélité" (Théorèmes 1–3; scans 3–40), §2 "La question de pleine fidélité" (41–52), §3 "Étude des sections de E_U sur Γ" (53–104), §4 "Sections d'extensions, et anneaux de valuation généraux" (105–136). Two labels of round 1 were wrong: scans 24–40 are the corollaries of Théorème 2 and Théorème 3, not "Kummer theory and rigidity"; the good-reduction theorem for sections is at scans 70–78 and the bad-reduction conjecture at 99–103 | read in full [C] |
| III | Cote 142 is at least two texts with their own title sheets: "Catégories de Galois-Teichmüller d'un corps alg. clos", marked "19 pages" (scans 2–21), and "Opérations de Γ_(Q̄/Q) sur Π₁U₀₃", marked "40 pages" (from scan 22). The first is of 1980 or later if the margin of scan 8 ("th. profond et récent": every finite subgroup of the Teichmüller group is a stabilizer) means Kerckhoff's theorem [B for the identification] | scans 2, 8, 22 [C] |
| III ↔ V | 149 §4 ends (scans 128–136) on the strata D_J of a normal-crossings boundary, the tori T^J → π_(U/K), "tubulures étales", a "maquette simpliciale" on the index set and the map π₂(D_J) → T^J. This is 147 §§11–13 again, in the arithmetic setting. The text stops at ms. p. 67 inside this development. Its bridge to 147 is stated by him: "Sans m'y attendre, me voici à tâter un peu la structure à l'∞ des variétés modulaires de Teichmüller !" (scan 101) | scans 101, 128–136 [C] |
| I | Cote 25 is the one text of Book I that exists nowhere in French: IV 16, 17.15–16, 20, 21, "Remords" pages and a letter to Dieudonné. IV 20 ("Sections hyperplanes et projections coniques") is the geometry behind the hyperplane induction of 16 and behind Th. 5–6 of 44; 17.16 (smooth quadratic forms) touches Book IV | `EXISTING_EDITIONS_CHECK_20261112.md` §3 [C]; the two links are [G] |
| VI | Handwritten leaves in the *Pursuing Stacks* folders are in no edition: a 4-page letter "Cher Deligne" (134-1), the provisional contents and the dedication (134-2 sites 3–13), French copies of letters (134-2 sites 145–183), about 40 pages of notes on listing paper (134-8 sites 42–86) | same file §1 [C] |

### 1.2 Shape: the bridges (round 1, section 1.2)

Four new rows.

| | Between | The statement | Where in the archive | Where in our files or the literature | Status |
|---|---|---|---|---|---|
| B13 | III, V, II | The boundary of a normal-crossings compactification X ⊃ U: strata D_J, tori T^J, the extension 1 → T^J → E_(U_J) → E_(D_J) → 1, and the simplicial complex on the index set of the components. The simple homotopy type of that complex does not depend on X, and its reduced homology is the top weight piece of the cohomology of U. The exit-path category of (X, D) maps to the poset of strata, whose nerve is the complex; what the complex forgets is the strata and the tori | 149 scans 128–136; 147 scans 164–181; 150, 151 (unread) | Thuillier 2007 and Payne 2013 [C, lookup 5]; STRATA B.1–B.3, C.5; S2 | theorems; they answer in part his "quelle est sa signification topologique ?" (scan 133) |
| B14 | III, VI | Filling a hole is a functor between Teichmüller groupoids (142 scan 20) but not a morphism of his Galois–Teichmüller category (scans 18–21). On the entrance categories of the compactified moduli it is W∞-proper and not smooth, its lifting categories are contractible or BZ, and its right Kan extension is the direct image along the universal curve. Drilling a hole is a construction on sections, not on groups ("forage de trous", 149 scan 67): today's cuspidalization | 142 scans 18–21; 149 scans 66–68; 147 §§9–10; LM 2:sc349 | STRATA F.9–F.15; BISITE F.15–F.17; RESIDUE H.3–H.6 (the returns' claims, unreviewed); Mochizuki 2007 and Hoshi–Mochizuki for cuspidalization [B] | proved in Cat; the anabelian side open |
| B15 | V, VI | For a finite poset P with the topology of down-sets, spaces over P localized at the maps that are equivalences over every open set are the functors P → spaces. Over the real line the same statement is open in our returns. Tame topology is the setting in which it should hold for compact spaces, by triangulation | 120, 121 (unread); 150, 151 | BISITE D.2, D.4, D.5, D.12; RESIDUE G.1–G.5; Shiota 2014; Haine–Porta–Teyssier 2024 (compact subanalytic stratified spaces have finite exit-path ∞-categories [C, lookup 11]) | theorem for finite posets; [G] beyond |
| B16 | II.4–II.6, folders 06–09 | For an abelian scheme the ring of correspondences modulo rational equivalence, tensored with Q, is lefschetzien in the sense of 16 no 8; the Fourier functor of 47 is the tool | 16 scans 15–18; 47 scans 3–11 | Künnemann 1993 [C for the paper, lookup 12; B for the match]; Lieberman; Kleiman 2A; Deninger–Murre | theorem |

Amendments to round 1's rows.
- **B1.** Add 149 scans 128–136. STRATA F.3 refutes "aspherical strata give an ordinary exit category" by S² with one point: this is his own example of 147 scan 180 [C]. STRATA C.4: unrestricted paths cannot replace the crossing category in the gluing formula [C].
- **B2.** PATHS D.K5 is a second derivation, from *Les Dérivateurs* V ms. 44–46 [C].
- **B4.** The exact form of the non-linear statement (149 scan 48): for U an anabelian elementary variety over a finite extension of Q and V regular of finite type over Q, an outer homomorphism E_V → E_U over Γ_Q comes from a morphism V → U if and only if its restriction to E_V°, the kernel of the cyclotomic character, is anabelian. It covers all morphisms, points included, with no condition of dominance. The first version, with "open image" (scan 44), he withdraws on the next page [C].
- **B11.** His text has the wrong reason and the right one: scan 34 invokes Mordell–Weil ("G(K) est Z-module de type fini") for an extension of an abelian variety by a torus, which is false for the toric part; scan 85 uses that G_m(S) has no infinitely divisible element [C].

### 1.3 Stage 0 again: cotes 149 and 142 read in full

**Cote 149, statement by statement** [C for the text; the last column is B unless marked].

| Scans | His statement | His own status | Today |
|---|---|---|---|
| 13–15 | Théorème 1: every open subgroup of E_K, and of π_K, has trivial centralizer (K of finite type over Q) | proved modulo three facts marked "à vérifier" (the centre of an open normal subgroup of Γ_Q; the centre and the torsion of a free profinite group) | all three are standard |
| 22 | Théorème 2: K ↦ Π_K over Π_Q is faithful | proved (Corollaires 1–3, Théorème 3, and a geometric complement, scans 37–40) | superseded by full faithfulness (Pop; Mochizuki) |
| 32–34 | Théorème 3: points → classes of sections is injective, already for the abelianized extension | proved; the reason given fails for a toric part | true (B11) |
| 44–45 | Question-conjecture for fields; its consequence π_K^(Γ′°) ≠ 1 for sections of E_K | corrected while writing ("Or je m'aperçois que ceci est sans doute faux") | the birational Hom-form: Pop, Mochizuki |
| 45 | The centralizer of Γ′° in Γ_Q is trivial | "à vérifier !" | true: section 7, R3 (unchecked) |
| 48 | Conjecture fondamentale (B4 above) | conjecture | for dominant maps of curves Mochizuki 1999; for points the section conjecture, open over number fields |
| 54–56 | Proposition (sections at distinct cusps are distinct); π^(Γ°) = L_i; Conjecture A with its "précisions" | proved "sauf pour le type (0,3)"; "hautement plausible" | the précisions and the case (0,3): S6, now R2 (unchecked) |
| 57–58, 127 | Every section of E_U lifts to a section of E_L; with it the model form equals the birational form | conjecture b) | the cuspidalization conjecture for sections (Esnault–Hai 2008); its equivalence with the section conjecture is in Bresciani [C, lookup 7] |
| 59–63 | Conjectures B and B′; "tous nos beaux énoncés" should hold over fields of finite type over a cyclotomic field | conjecture | the birational form over cyclotomic extensions: Tsujimura 2023 [C for the paper, lookup 2; B for the match] |
| 66–69 | Rebuild every E_K from Γ_Q acting on π̂₀,₃ by "forage de trous"; the "sphère arithmétique"; "il me faudra développer un langage géométrique … où les points rigides jouent un rôle prépondérant" | programme | cuspidalization (B14) |
| 74–78 | "Théorème (?)": a rational point extends over a trait if and only if its section kills inertia; inertia goes into L_i by μ·κ_i, μ the intersection multiplicity | one step admitted ("Il faudrait que je demande à Carlos") | standard (specialization of sections) |
| 79–85 | The extension 1 → T → N(L_i) → E_S → 1 has as class the conormal bundle of the cusp section; the geometric splittings are a torsor under G_m(S)^ inside all splittings; he asks for a profinite characterization of them | "une histoire d'ombres" to prove; open question | tangential sections (Stix; Esnault–Hai's "packets" [C, lookup 7]); the characterization is open (S24) |
| 99–103 | "Conjecture-à-tout-hasard": good reduction ⟺ inertia acts trivially on π ⟺ on H₁ ⟺ the limit action is "admissible" | conjecture; "mais je l'ai démontré, dans le contexte des VA, il y a belle lurette !" | a ⟺ b is Oda (proper) and Tamagawa (affine) [C, lookup 4]; c, d ⟹ a is false for curves [C, same: H¹ does not suffice]; e ⟹ a: R4 |
| 120–127 | The Riemann–Zariski space 𝔛_(L/K); Conjecture a): sections of 𝓔_L over 𝓔_K correspond to valuations with residue field algebraic over K | conjecture | the birational section conjecture in valuative form (p-adic: Koenigsmann, Pop) |
| 129–134 | 1°) T^(I(x)) → π_(U/K) is injective; margin: "visiblement faux « en général »" after blowing up a point of D, "y a-t-il un modèle « minimal » … ???"; the composite π₂(D_J) → T^J → π_(U/K) is zero | presumption, withdrawn in the margin; question | S2 |

Two readings to hand to the second pass: formulas (32)–(33) of scan 127 are written for 𝓔_L where the argument (dévissage along an elementary fibration) and the margin of the same page need 𝓔_U; in 47 scan 9 the exponents of χ (2.3 above).

**Cote 142, the opening text** [C]. The category has surfaces of finite type as objects and isotopy classes of finite étale maps as morphisms; Proposition 2 and Corollaire 3 make each class a torsor under the homeomorphisms isotopic to the identity (anabelian case). The "enveloppe profinie" is built under hypothesis (*) (the image in Aut(Y) of the automorphisms of an arrow X → Y has finite index), with composition extended by continuity (scans 10–14); (*) holds here, because the liftable mapping classes have finite index, and so does the injectivity hypothesis of scan 14, because Teichmüller groups are residually finite [B]. The "programme à l'horizon" (scan 17) is to determine this category with the action of Aut k "par voie « algébrique » (ni transcendante ni de géométrie algébrique !)". Scans 18–21: hole-filling cannot be made a morphism that composes with the étale maps, "à moins d'y aller comme une brute et de définir une catégorie plus grosse … par générateurs et relations". That brute course is what 147 scan 104 and the Esquisse then take.

### 1.4 The stages (round 1, section 2.3): changes only

| Stage | Change | Reason |
|---|---|---|
| 1 (built packages) | Played for 16, 47, 54, 44: section 2. For the crystals: 54 joins them; their context zip gets Oda 1969 and the letter to Tate | 54 scan 7 asks what Oda's theorem answers |
| 2 (rank 4) | Two more checks: does 148 or 144 continue 149 §4 after ms. p. 67 (look for D_J, "tubulure", "maquette")? Is the inertia computation of 149 scan 78 written out anywhere | 149 stops in mid-argument on scan 136 |
| 3 (rank 5) | The context zip gets 149 scans 128–136 and STRATA C, F with BISITE D and RESIDUE G, H as statements with status. The reader looks for the words "tubulure" and "ombre": 149, written after 150–151, uses them as known | 149 scans 133–134 [C]; dates from `MANIFEST.csv` |
| 4 (probes) | Two more: cote 43, first 45 scans; the short notes 49, 50, 51, 52 whole (54 pp., one run) | 1.1 above |
| 5 (EGA plans) | Before it, outside the Pro queue: cote 25 from the scans over the API, with the Circle's scan as second witness and the English translations for alignment only | editions check §3 |
| 6 (dossier, 158, 137, 133) | Cote 115 (14 pp., "Correspondances fonctorielles. Dualité des topos") becomes a keystone: BISITE Parts F–G and RESIDUE Part I are its subject [G for the match]. The handwritten leaves of 134 travel with this stage | section 3 |
| 7 (motives) | Carry the lettering table and the three questions of 2.4 | section 2 |
| 9 (maps, 79, 83, 64) | 64 (moduli of elliptic curves, 156 pp., from 1980) is announced by 149 scans 99–101 (the place at infinity of the modular curve of type (1,1)) | [C] for the text, [G] for 64 |

### 1.5 The order (round 1, sections 2.5 and 4.5)

Order W stands. Its additions: the crystals now; the two extra probes; the leaves of 134 with the dossier; cote 25, the Esquisse and *Pursuing Stacks* by collation over the API beside the Pro queue. What changes more is the order of the second pass, which at 0.04 points a scan no longer covers the core in four weeks (section 4): Opus follows the order of mathematical dependence (Book III returned, then ranks 4 and 5, probes, the dossier, II.9, crystals, motives, 156), and Book IV loses its full pass first.

### 1.6 The breaks (round 1, section 2.6): additions

| # | Break | Bites at | Do now |
|---|---|---|---|
| 16 | A third of the first 1960s package is reused sheets and covers (20 and 8 of 82 scans); the page counts of the Paris-years folders overstate their mathematics, and the second pass pays full rate for typed pages of printed texts | every package of Books I and II | a "sheet kind" column in the inventory (text; reused typed; cancelled draft; cover); light rate for reused typed pages; readers skip them |
| 17 | His letters A–D for the standard conjectures are not the printed ones | the first note or register entry that quotes one | the lettering table of 2.3 |
| 18 | Returns 5–8 of *Les Dérivateurs* (368 statements) have no review at effort max, and the expert's handoff has no section on them; yet round 1 and the LM prompts quote STRATA as proved | the first companion page that states one as a theorem | review first the 60 rows the archive needs (section 3.3) |
| 19 | The second pass costs 0.04 points a scan, not 0.025 | week 4 | tiers and order of section 4 |
| 20 | Outside editions of *Pursuing Stacks*, the Esquisse and EGA V are not faithful; cote 25 was never transcribed | the front door and Books I, VI | collation over the API; cote 25 from the scans |
| 21 | 149 and 142 mark many of their own steps "à vérifier", "sauf erreur", "je présume", "admis" (149 scans 14, 15, 21, 45, 78, 79, 119, 130); the notes file them among "unproved claims" | the register | a kind "self-flagged" in notes and register; one cheap prompt per text that proves or refutes them all |
| 22 | Texts inside one cote have their own title sheets and page counts ("19 pages", "40 pages", "Pages 1–67") | chaptering of Book III | the reconnaissance pass records title sheets as unit boundaries |

### 1.7 What follows from the totality (round 1, section 3): changes and additions

**Changed.**
- **S1 (exit-path tower).** The uncompleted half is now in the returns for all genera, as claims: an ordinary EI exit model for the stable genus-zero moduli (STRATA F.7, by Jansen), the skeletons for 4 and 5 points with their coset hom-sets (F.2, F.4–F.6), forgetting as a W∞-proper functor for every stable (g, n), smooth only for (0,3) (RESIDUE H.5), geometric direct image along the universal curve equal to right Kan extension (H.6), clutching as a replete full cosieve (STRATA F.12), the Teichmüller groupoid as the open subgroupoid with its Lego presentation (F.17). STRATA says itself that it supplies "no profinite completion of the moduli category, arithmetic Galois action, or comparison with the Grothendieck–Teichmüller group". EXIT_TOWER shrinks to: identify his MDT-structure (147 §§9–10) and the finite models of 146 with these categories; complete them; the open rows of LM3 and LM3b.
- **S2 (one-category criterion).** Corroborated in the cases (STRATA F.1–F.3, F.6). New from 149 scan 130: the criterion depends on the compactification (after blowing up a point of D two meridians coincide), and he asks for a minimal model. The prompt gains two Parts (section 6).
- **S3 (gluing is exodromy).** Its reader can start now: 147 §§11–13, 149 scans 128–136, STRATA A–C, F, BISITE D, RESIDUE G, H are all in hand; 150–151 are then read against a written dictionary. Add Haine–Porta–Teyssier 2024: exodromy without conicality, for subanalytic stratifications [C, lookup 11].
- **S4 (shapes).** The exact class of shapes over which Cat-valued colimits are homotopy colimits is left open in PATHS A.8 and RESIDUE F.7, with the weakly-terminal and finite-object cases proved (RESIDUE F.4). Today's theorem claims the answer (filtered) in general [C for the statements; the theorem is unchecked].
- **S5 (three categories).** A concrete form for C_all with its boundary [G, mine]: the system of exit-path categories of the Hurwitz stacks of admissible covers, with their two projections to moduli of curves. Reason: his obstacle at 142 scans 18–21 is that hole-filling composed with étale maps gives ramified maps between the completed curves with free ramification points (his diagram (24)), which are points of Hurwitz spaces and their boundaries. GT_CATEGORY asks for this.
- **S6.** Now R2 of section 7, with the affine case argued in full and its consequences inside 149 listed. Literature after the lookups: the lemma it needs is in Stix, "On cuspidal sections" (Theorem 20, attributed to Nakamura) [C, lookup 6]; Ribet's theorem is as quoted [C, lookup 10]; work on anabelian geometry over cyclotomic extensions (Tsujimura 2023, 2025) uses the same theorem of Ribet [C for the titles], so the statement may be known there.
- **S7 (B, B′).** After R2: for Γ° there is at most one fixed point at infinity, and it exists exactly for cuspidal sections. Uniqueness at finite distance for Γ° is injectivity of points → sections over K(μ_∞), where the toric part does have divisible elements (roots of unity): this is the hard part, and the subject of the recent work just named.
- **S8.** Conjecture b) is the cuspidalization conjecture (1.3). Conjecture a) is stated by him for any K ⊂ L of finite type over Q through the points of dimension 0 of 𝔛_(L/K).
- **S11 (schematization).** The localizer of all k-linear local systems is computed in the returns: W_D(k)^lc is bijection on components, isomorphism on π₁ and k-homology equivalence of universal covers (RESIDUE D.5); the rational ones fail axiom (7 F) (D.11); the second stage for F_p is computed (I.9). My class W_sch(k), with finite-dimensional local systems only, is coarser and is the one to study.
- **S12 (level 1).** Second support in PATHS D.K5.

**Added.**

| | Statement | Rests on | Plausibility; what would decide it | V | T |
|---|---|---|---|---|---|
| S21 | The standard conjectures for singular varieties: his proposal of January 1967 to reduce the Lefschetz conjecture to hypersurfaces, which must then be singular | 16 scan 47 | Taken up thirty years later as "the standard conjectures should extend to singular varieties" by Corti–Hanamura, who derive a motivic decomposition theorem from the standard conjectures [C, lookup 8]. The reduction to hypersurfaces is, as far as I know, not in print [B]. In reach: B for all smooth varieties from B for one smooth model in each birational class (blow-up formula, weak factorization), stated precisely | 4 | 2 |
| S22 | Cote 47 as a dated witness: the derived Fourier transform on abelian schemes, with inversion, after 1968 | 47 scans 3–11 | Two searches found no mention in the literature (lookups 1, 15). Decided by the second pass (date, hand) and by a search of the correspondence. In reach: the proof closed as he set it up; his integrality question (FOURIER_1970) | 4 | 5 |
| S23 | The "Conjecture-à-tout-hasard" of 149: status table of a)–f) | 149 scans 99–103 | a ⟺ b known; c, d ⟹ a false; e ⟹ a by weights and by Torelli except when the components of a compact-type reduction are isogenous (R4, unchecked) | 3 | 4 |
| S24 | Characterize profinitely the geometric tangential sections (the torsor under K* inside the torsor under K̂*) | 149 scan 85 | Open, to my knowledge; it is the integrality question for Kummer classes. Record | 4 | 1 |
| S25 | The "maquette simpliciale" at infinity (B13): what the exit-path category adds to the boundary complex | 149 scan 133; 147 §§11–13 | A dictionary to write, with the theorems of Thuillier and Payne; one Part of EXIT_ONE_TYPE | 3 | 5 |
| S26 | Tame realization (B15): over a compact tame space, cosheaves of spaces are the localization of tame spaces over it at the open-test equivalences | BISITE D.2, D.12; RESIDUE G.3, G.5; 120, 121 unread | [G]. Decided by a proof by triangulation or by a counterexample; after rank 5 | 4 | 3 |
| S27 | The strict bifibration over the five-element monoid of type S² | STRATA E.11 = PATHS E.11 = BISITE B.21 = RESIDUE A.8 | The same row is open in four returns; RESIDUE A.5 shows this monoid is the only one of order ≤ 5 that is not a 1-type. One dedicated prompt, or a decision to stop | 2 | 2 |
| S28 | Integral Lefschetz and Fourier: which order the integral correspondences of an abelian variety generate in ∏ Mat_(n−i+1)(Q), and which multiples of δ^k are classes of integral cycles | 16 scan 14 (false over Z as written); 47 scan 9 | The literature on integral Fourier transforms (Moonen–Polishchuk; Beckmann–de Gaay Fortman) answers parts; a comparison is in reach, new theorems probably not | 3 | 3 |

**Ranking, revised.** Pursue now: R2/S6 (check), S4 (drafted), S2 with S25, S22 (FOURIER_1970), S10 (as round 1), the self-flagged statements of 149 (break 21). Pursue after the Fable readings named in section 5: S1, S3, S5, S23. After returns: S26, S11, S9 tables, S13. Record: S7, S8, S21, S24, S27, S28, S18.

### 1.8 The questions we ask (round 1, section 4): changes

- **Transcription prompts (4.1).** The inventory gets the column "sheet kind". The notes keep their post-freeze research sections as they are: in the Book II return these 81 items are a third of the notes file and carry most of its value, with references opened (2.3 used them throughout); the compaction of round 1 applies to the 347 page notes. Two more standing questions: which steps the manuscript itself marks as unverified; which title sheets and page counts it carries.
- **Context zips.** For Paris-years folders: the free printed witnesses (Kleiman's text in *Dix exposés*, "Standard conjectures", Oda 1969, Mukai 1981, the CSG transcriptions of the letters). For ranks 5 and 9: the statements of section 3.2 with status.
- **The register (4.2).** New kinds: "self-flagged" and "withdrawn in the same text" (149 scans 44–45 and 130; 16 scan 44; 47 scan 5, where "l'identité" is corrected to (−1)ⁿ s_A*). Seed entries: the table of 1.3; the 23 conjecture-class notes of the Book II return; 16 scans 14, 17, 18, 22, 29, 47, 49; 47 scans 8, 9; 54 scan 7; 44 scans 2, 4, 6, 8, 9; 142 scans 8, 17, 21.
- **Fable readers (4.3).** Carry-questions answered here are struck; the new ones are in sections 2.4, 3.3 and 5.
- **Notation and glossary.** Add from 149: E_K against 𝓔_K (he changes notation at scan 105, "révision de notations"), Γ°, T = T_∞(K̄*), L_i, N_x, I_x, 𝔛_(L/K), D_J; the words "trait", "jauge", "ombre", "tubulure étale", "groupe bout", "paquet", "forage" and "bouchage de trous", "modèle élémentaire anabélien", "sphère arithmétique", "courbe de Poincaré", "points rigides", "filtration modélique", "admissible". From 16: "anneau de correspondances lefschetzien", "élément de Lefschetz", "élément co-lefschetzien". From 142: "catégorie isotopique", "enveloppe profinie", "catégorie de Teichmüller-Galois" and "de Galois-Teichmüller" (he writes both).

### 1.9 Scope (round 1, section 5)

Replaced by sections 4 and 5 below.

---

## 2. Book II, simulated on real content

The first Book II package is back: cotes 16, 47, 54 and 44, 82 scans, run from 14:45 to 16:17 UTC on 12 Nov, frozen at
15:58, with 428 notes [C, `RETURN_NOTES.md`, `progress.log`]. No second pass has been made; every reading below is a
first-pass reading.

### 2.1 What came back

Of the 82 scans, 54 carry his text on the subject of the folder, 20 are reused sheets (typed pages of other texts whose
backs he wrote on, and cancelled drafts of his own), and 8 are covers and title sheets [C, counted from the
transcription]. A third of the first 1960s package is not the folder's mathematics; a quarter is reused sheets.

| Cote | Scans | On the subject | Content [C] |
|---|---|---|---|
| 16 | 54 | 37 | (a) "Sur certains anneaux gradués", ms. pp. 1–16, nos 1–8 (scans 3–18): graded rings of endomorphisms with their grading projectors π_i; uniqueness and existence of the π_i; the "conditions de Lefschetz"; the universal ring Φ₀ = Z[L₀, Λ₀] acting on the exterior algebra of a symplectic lattice; the theorem and proposition of nos 6–7; "anneau de correspondances lefschetzien" (no 8). (b) Loose calculations and a counterexample (20, 22). (c) "Algèbres de Hodge d'ordre 2" (25, 27, 29). (d) "Formulaire de L, Λ" for a hyperplane section Y ⊂ X (33, 34, 36, 38, 40, 42). (e) Two typed letters to Coates, dated 4.1.67 (44–47) and "6.1.1966" (48–50). (f) A lemma and corollary with proof: Λ is algebraic if and only if each L^(n−i) has an algebraic inverse (51, 53, 55). Reused sheets: typescript pages of "Le groupe de Brauer III" with his corrections (19, 21, 23), corrections to SGAD XV–XVII (26), an English typescript on the cohomology of group schemes (28, 30), a note of Karoubi (35), pages of an English typescript on injective sheaves and derived Hom, by its content Hartshorne's *Residues and Duality* [B] (37, 39, 41), a page of EGA IV 18.11 with the margin "Virer (ii) sauf raison sérieuse !" (43), Bourbaki's "Algèbres étales et la différente", Tribu no 65 (52, 54, 56) |
| 47 | 11 | 9 | "Produit de convolution sur les VA et transformation de Fourier sur les VA" (scans 3–11): the functor Φ_L(F) = R pr₂*(L pr₁*(F) ⊗ L) for an abelian scheme A over any base S; Proposition: Φ_L turns the Pontryagin product into the tensor product (3–4); "Théorème": for A and its dual B the composite Φ_(ˢL) Φ_L is s_A* followed by τ_A[−n], τ_A = Λⁿ t_A (4–6); Lemma 1 (the direct image of the Weil sheaf is e*(τ)[−n]) from Lemma 2 "(Mumford)" (6–8); remarks on Pic, on Chern characters and Riemann–Roch, on duality (8–11) |
| 54 | 8 | 3 | "Dualité en cohomologie des V. A." (scans 3, 5, 7): the extension S_A: 0 → t_A^∨ → H¹(A) → t_B → 0 of de Rham cohomology; the universal extension E of A by a vector group, with t_E = H¹(B); H¹(A) and H¹(B) dual; comparison with Cartier duality of the kernels of p, the kernels of Frobenius being orthogonal; the question whether S_A "peut se déduire de la connaissance de ₚA ??". Reused: an EGA IV draft on flatness (4, 6), a Bourbaki draft on chambers (8) |
| 44 | 9 | 5 | "Programme de travail" (scans 2, 4, 6): seven theorems to prove on the abelian varieties P^i(X) made from cycles algebraically equivalent to zero, with margin labels "Hodge", "Néron", "Lefschetz", "Matsusaka"; the typed letter to Serre of 12.8.1964 with handwritten margins (8, 9). Cancelled drafts of his own on completions of graded rings (3) and on root data (5); a Bourbaki sheet (7) |

**Dates** [C for the evidence, B for the inference]. Cote 16: the letters are dated; the reused sheets are of 1965–67
(EGA IV §18, Tribu no 65, Karoubi's note). The second letter's "6.1.1966" continues the first of 4.1.67 ("Here a few
more comments to my talk") and is almost surely 6.1.1967; the notes keep both dates as written (S18), which is right
for the transcription, and the global pass has to decide. Cote 47 cites "Kleiman dans '10 Exposés…'" (scan 11) and
"(Mumford)" for the vanishing lemma (scan 7): it was written after 1968. Cote 54 carries the archive's "[à partir de
1971]"; its closing question was answered in print by Oda in 1969 (2.3), so either the date is late or he did not
know the paper: the reused sheets (a draft on flatness in the style of EGA IV, a Bourbaki draft no 391) point to
the 1960s [B]. Cote 44: 1964.

**Outside witnesses** [C, `SECTIONS_STATE.md` §3]. The two letters to Coates are transcribed at the CSG (L11d, L10d).
The letter to Serre is in the printed correspondence. Nothing else in the package is in print.

### 2.2 Round 1's predictions against the return

| Round 1 (stage 1) | The return [C] | Verdict |
|---|---|---|
| 16 holds "axioms of a Poincaré–Hodge algebra" with a positivity condition | The axioms appear only for "ordre 2", the cohomology ring of a surface, with a Lefschetz and a Poincaré condition and no positivity condition (scans 25, 27). The main text is the abstract algebra of rings of correspondences | half right |
| Formal deductions among the conjectures | Scans 33–42, 44–50, 51–55 | right |
| "Whether 16 holds an inductive strategy for B and the index theorem and where it stops" | It holds the induction on hyperplane sections for the Lefschetz conjecture: his C(X) ⟺ C(Y) and A⁰(X×Y), hence C(X) ⟺ A⁰(X×Y), A⁰(Y×Z), … along a flag (scan 42; letter, scans 45–46). It stops at 1-cycles on threefolds (scans 46–47). On the index theorem there is only the statement that C(X) with I(X×X) makes the ring of correspondence classes semisimple (scan 49) | settled |
| 47: a Fourier transform by the Poincaré bundle, "perhaps with inversion", undated, before Mukai | Inversion is the "Théorème", over any base, with the determinant twist; written after 1968 | right; dated from below |
| 44: the J^i(X) of the letter to Serre | Yes, and a programme of seven theorems that the printed letter does not contain | right, and more |
| "Little of ours" meets it | Confirmed. The literature meets it at every point (2.3) | right |
| Error rate and package size for the 1960s hand | 82 scans in 73 minutes to the freeze; 624 doubts on 74 scans, 336 of low confidence. The error rate waits for the second pass | open |

### 2.3 The mathematics, and what the literature says to it

His letters A, B, C, D are not the printed ones. From the letters (scans 44–50) [C; the notes' S1 gives the same
dictionary in part]: his A is the printed A (Lefschetz on algebraic classes); his C is the printed B (Λ algebraic); his
D, used to make characteristic polynomials of algebraic endomorphisms rational (scan 48), is the printed C (Künneth
projectors) [B]; his B, equal to A once the index theorem holds (scan 45), is the printed D (homological equals
numerical) [B]. The global pass fixes this table before any note quotes a letter.

**16 (a). The ring of correspondences as an algebra over a universal ring.**
- *What he does.* A graded ring 𝓔 with projectors π_i and an element L of degree 2 is called a "anneau de
  correspondances lefschetzien" when there is a homomorphism of graded rings Φ → 𝓔 from the universal ring Φ (generated
  by L₀, Λ₀ and the π_i acting on Λ*(M₀), M₀ a symplectic lattice of rank 2n) carrying L₀ to L and the π_i to the π_i.
  Theorem of no 6 and proposition of no 7 (scans 10–16): this is equivalent to hard Lefschetz for L together with
  Λ ∈ 𝓔; the homomorphism is unique, and the π_i, the Λ and the projectors π_(i,α) on the pieces L^α P^(i−2α) are then
  determined by the graded ring and L, by the eight formulas (6.14). He asks whether L alone determines the
  homomorphism and answers "Non", already for n = 1 (scan 17). No 8 asks for a characterization of the Lefschetz
  elements; scan 22 gives a ring with L⁴ = 0, L′² = LL′, L²L′ = L³ in which L is a Lefschetz element and L′ is not
  "bien que L′³ = L³" [C: I checked the example; L′ kills L − L′ in degree 2].
- *In today's terms* [B]. Φ ⊗ Q is the image of the enveloping algebra of sl₂ with its weight projectors in
  End(Λ*Q^(2n)), the product of the matrix algebras Mat_(n−i+1)(Q) for 0 ≤ i ≤ n (the notes compute this model: S3).
  The theorem says that the Lefschetz conjecture B(X) is the statement that the whole sl₂-action on H*(X), with its
  primitive projectors, is by algebraic correspondences. This is Kleiman's Proposition 1.4.4 and Theorem 2.9 (1968)
  in the form of a universal property, which is not in print. Two later theories are instances of his definition:
  André's motivated cycles (1996) are the smallest ring of correspondences containing the algebraic ones that is
  lefschetzien in his sense; Künnemann's theorem (1993) is that for an abelian scheme the ring of correspondences
  modulo rational equivalence, tensored with Q, is lefschetzien.
- *An error to record* [C]. No 7 takes the model "sur Z !" (scan 14) and says that Λ₀, the contraction with the dual
  form, is the operator Λ of (6.5). Both fail over Z. For n = 2, L₀² sends 1 to ξ² = 2·vol, so (6.1)₀ fails; for
  n = 3 already L₀: Λ² → Λ⁴ has determinant ±2 on the span of the three e_i∧f_i (my check); and the contraction
  satisfies Λ₀L₀ = n on Λ⁰, not 1: it is the sl₂-lowering operator, Kleiman's ᶜΛ, not the Λ of (6.5). The notes saw
  the first and third points (R1, R2, S2). Over Q the text stands with Λ₀ replaced by the operator of (6.5). The
  integral question it raises (which order in ∏ Mat_(n−i+1)(Q) the integral correspondences of an abelian variety
  generate, with divided powers) is the question of integral Fourier transforms in 47 below.

**16 (c). Hodge algebras of order 2.** For H⁰ = k, H¹ = V, H² = kξ ⊕ W, H³ = V^∨, H⁴ = kξ² he writes the product in
terms of an alternating form φ on V, an alternating map ψ: Λ²V → W and a symmetric form Q on W, finds the
associativity condition (boxed, scan 25), and reads off: Lefschetz ⟺ φ non-degenerate, Poincaré ⟺ Q non-degenerate.
Scan 27 rewrites the data as a 4-form χ on V, an "extension" (W̃, Q̃) of the form χ′ it induces on Λ²V, and ξ ∈ W̃ with
Q̃(ξ, ξ) = 1. Scan 29 asserts that the orbits of ξ and of the inverse bivector φ̌ under an endomorphism u of Λ²V built
from them "pourront être infinies, si dim V ≥ 4 (ou 6 ?)". The notes build examples for dim V = 6 and 4m (D19, D20).
The threshold is 6: section 7, R1.

**16 (d), (e), (f). The hyperplane induction and the letters.**
- Λ_Y = φ*Λ_X²φ_* (boxed, scan 40), so C(X) implies C(Y); conversely C(X) ⟺ C(Y) and A⁰(X×Y) (scan 42). These are in
  Kleiman 1968, 2.12–2.14 [C, the notes' S9].
- Letter of 4.1.67: the conjecture "A(k) = C(k)" is equivalent to A(T)⁰, the condition in the critical degree only,
  for all T of even (or all of odd) dimension (scan 46). Known then: C(X) for dim X ≤ 2; A(X) in characteristic 0 for
  dim X ≤ 4; "the main problems arise already for 1-cycles on threefolds" (scan 47). He withdraws a claim: in
  characteristic p it is "not clear to me" that A and C are independent of the polarization (scan 44).
- Letter of "6.1.1966": C(X) ⟺ there are algebraic isomorphisms H^(2n−i) → H^i and characteristic polynomials of
  algebraic endomorphisms are rational, by Cayley–Hamilton (scans 48–49); so C is independent of the polarization.
  This is Kleiman 2.9–2.10 [C, S12]. "The complete yoga then being that we have the category of motives which is
  semi-simple !" (scan 49).
- *Later* [B unless marked]. Semisimplicity of numerical motives is unconditional (Jannsen 1992 [C, S15]); the
  kernel from homological to numerical correspondences is nilpotent when the Künneth projectors are algebraic
  [C, S16]. The Lefschetz conjecture is known for abelian varieties (Lieberman, Kleiman), in general for H¹ and
  for dimension ≤ 2, and in scattered cases since (some hyperkähler families: Charles–Markman); it is open for
  threefolds in general, as in 1967. The Hodge-type conjecture is known for surfaces and for abelian fourfolds
  (Ancona 2021); 032 claims the standard conjectures for all abelian varieties.
- *A programme he states* [C for the text]. "If one wants to reduce somehow to the case of hypersurfaces, one will
  have to work also with singular ones, and see how to reformulate for singular varieties the standard conjectures"
  (scan 47; Serre had killed the smooth version: such an X would be simply connected). The reformulation for
  singular varieties was taken up by Corti–Hanamura [C, lookup 8]; the reduction to hypersurfaces is S21 of 1.7.

**47. The Fourier transform.**
- *What is there* [C]. Multiplicativity with full proof, for A an abelian scheme over any S and any S-scheme X with a
  sheaf L on A ×_S X; the margin extends it to flat group schemes and to pairings of torsors (scan 3). The inversion
  theorem Φ_(ˢL) Φ_L ≅ s_A*( ) ⊗ τ_A[−n], with the remark that bounded quasi-coherent complexes do as well as perfect
  ones (scan 5). Its proof is complete except for one step: that the map R p*(W) → e*(τ)[−n] he constructs is an
  isomorphism at the points of the unit section, "à faire une vérification de compatibilité....." (scan 8). The
  notes give the plan that closes it (F7, F8).
- *Later* [C from the notes' F3, F4, F18; B for my reading]. Over a field this is Mukai's theorem (1981, Theorem
  2.2). Over a base with the twist it is Laumon (1996, Theorem 1.2.4). The product formulas on Chow groups with the
  sign (−1)ⁿ are Beauville (1983, Proposition 3). So the folder holds, some years after 1968, the statement and most
  of the proof of the theorem that carries Mukai's name, in Laumon's generality. Two searches found no mention of
  this in the literature (lookups 1, 15); that is not proof that there is none.
- *The heuristic of scan 9.* For a line bundle L of Euler characteristic χ ≠ 0, "φ_L(cl L) = χ L′^(−1/χ)", that is
  ch = χ exp(−D′/χ). In the ample case this is Mukai's Proposition 3.11 read on Chern characters [C, F11]. His
  expansion of the total Chern class has one factor χ too many; the right coefficient is
  c_k = (−1)^k (χ−1)…(χ−k+1) D′^k / (k! χ^(k−1)) [C, F12; I derived the same independently], and his closing
  integrality statement, with χ^(k−2), is true and weaker than what the Chern classes give [C, F14]. He asks: "ces
  formules sont-elles bien vraies mod torsion ?" This is today's subject of integral Fourier transforms and the
  integral Hodge conjecture for abelian varieties (Moonen–Polishchuk 2010; Beckmann–de Gaay Fortman 2023 [C, F15]).

**54. De Rham H¹ and the universal vector extension.** The identification of the Lie algebra of the universal
extension of A with H¹_dR of the dual is the theorem of Mazur–Messing (1974), who credit him [B]; the duality of
H¹_dR(A) and H¹_dR(B) with its three descriptions is Coleman 1998 [C, D02]; the orthogonality of the Frobenius
kernels under Cartier duality and the answer "yes" to his closing question are Oda 1969 (H¹_dR(A) is the Dieudonné
module of ₚA, the Hodge sequence included) [C, D03, D05]. This folder belongs with the crystals (2.4).

**44. The programme of 1964.**
- *What is there* [C]. Th. 3: Z^i_alg(X)/Z^i_alb(X) = P^i(X) is an abelian variety and P^i(X), P^(n+1−i)(X) are dual.
  Th. 2: dim ≤ ½ b_(2i−1). Th. 4 ("Hodge"): for n = 2m − 1 the self-duality of P^m(X) is a polarization. Th. 5
  ("Néron"): for cycles Z, Z′ of complementary codimension on X whose restrictions ζ, ζ′ to the generic member Y of a
  pencil are algebraically equivalent to zero, the Néron–Tate pairing is ⟨ζ, ζ′⟩ = (−1)^m Z·Z′; margin: "Doit résulter
  d'un énoncé plus général sur des fibrations, et admet une variante locale". Th. 6 ("Lefschetz"): P^i(X) → P^i(Y) is
  an isomorphism for 2i ≤ n − 1. Th. 7 ("Matsusaka"): numerical equivalence equals τ-equivalence. The letter adds, in
  margins not in print: "conjecturalement t_(J^i) ⊂ H^i(X, Ω^(i−1))", and, on the positivity, "il faut tenir compte de
  la décomposition primitive".
- *Later* [B unless marked]. The universal object is the algebraic representative: it exists in codimension 1, 2 and
  dim X (Murre 1985; Kahn 2021 for the bound 2 dim ≤ b₃ [C, D09]); Achter–Casalaina-Martin–Vial make it functorial and
  descend it [C, D08, D10]. Th. 5 is the function-field case of the height pairing of Beilinson (1987) and Bloch
  (1984), defined exactly as an intersection number on a model, with local terms: his "variante locale". Th. 7 is
  false in codimension ≥ 2: Griffiths 1969 (1-cycles on the quintic threefold; Clemens 1983 for infinite generation
  [C, D14]); the letter of 1967 still lists it as unknown for 1-cycles on threefolds (16 scan 46). Th. 4 is true in
  characteristic 0 by Hodge theory. In characteristic p, Achter–Casalaina-Martin–Vial (Astérisque 455, 2025) build
  a canonical auto-duality on the intermediate Jacobian of a threefold that agrees with the Hodge-theoretic
  polarization in characteristic 0 [C, lookup 3]; whether it is a polarization, his question to Serre, I could not
  confirm. The identification of his J^i with the image of the Abel–Jacobi map fails in general (Ottem–Suzuki 2020
  [C, D11]).

### 2.4 How it meets the stages that follow

| Stage that follows | What this return hands to it | Carry-question for the reader |
|---|---|---|
| Crystals (4–9, 100), built and waiting | Cote 54 is its first page: de Rham H¹ of an abelian scheme through the universal vector extension, and the comparison with the kernel of p | Where does the universal extension first appear, and is the crystal of the letter to Tate (May 1966) built from it? Does 6 or 9 answer the "??" of 54 scan 7, and does he cite Oda? Date 54 |
| Motives (14, 13, 12, 15, 18) | The definition of a lefschetzien ring of correspondences; the yoga of semisimplicity in its first written form (16 scan 49); his own lettering of the conjectures | Is the category of motives in 12–13 built on lefschetzien rings? Is the sl₂ of 16 inside his motivic Galois group, and the grading its weight cocharacter? Does 14 take up the programme for singular hypersurfaces (16 scan 47)? Which lettering does 14 use? |
| Abelian varieties and Picard (the folders 06–09 of the archive) | 47 and 44 are their research end: Fourier transform, intermediate Jacobians | Is there a second witness of 47 with the compatibility check done? Earlier forms of Th. 1–7 |
| The 1976 de Rham notes (136, 137) | A thread, not a statement [G]: the two integrality questions of this return (the integral Lefschetz ring of 16 scan 14; the divisibility of δ′^k in 47 scan 9) are questions about divided powers, which 136–137 treat as a structure on cochains | Does 136 or 137 name abelian varieties or Chern classes of the Fourier transform among its examples? |
| Books III and IV | Nothing direct. One formal echo: positivity as the source of semisimplicity (16 scan 49) against trivial centres in the anabelian notes (round 1, stage 7 table) | — |

### 2.5 What it changes in the plan

1. **Cote 54 moves to the crystals unit** for the second pass and the reader (it stays in its folder in the edition).
2. **Reused sheets are a quarter of this package.** The reconnaissance pass marks them per scan (typed page of a known
   text; cancelled draft; cover). The second pass gives typed reused pages the light rate, and the reader skips them.
   Applied to the Paris-years folders this lowers the Opus cost of Books I and II by about a fifth [G for the share
   elsewhere; C for this package]. They are also the dating evidence: a table "reused sheet, source, date" per cote
   goes into the global pass.
3. **A lettering table for the conjectures** (his A–D against the printed A–D, I) before the motives are read.
4. **Outside witnesses to collate:** CSG L10d and L11d for 16 scans 44–50; the printed letter to Serre for 44 scans
   8–9, with the margins as our addition.
5. **One reader for this package and the crystals together** (54 pages of text here; 126k tokens with all notes, about
   75k with the notes compacted): the reader of "II.1–II.4, the Paris years".
6. **Research prompts from this return** (specified in section 6): FOURIER_1970 (close the proof of 47 as he set it
   up, over a base; settle his question modulo torsion against the integral-transform literature); LEFSCHETZ_RINGS
   (the universal property of 16 written out and proved over Q; the integral order; André's cycles as the free
   lefschetzien ring); JACOBIANS_1964 (Th. 1–7 one by one: proved, false, open, with the height formula of Th. 5
   proved over a function field). None is urgent against Books III, V and VI; all three are cheap, because the
   statements are definite and the literature is close.
7. **For the commentary, not for prompts:** the dictionary of 2.3; the error over Z; the date of 47.

---

## 3. The *Les Dérivateurs* returns 5–8 in the war game

### 3.1 What they are, and their status

| Return | Statements | Proved / Known / Refuted / Open | Subject [C, reports and registers] |
|---|---|---|---|
| 5 STRATA | 81 | 54 / 14 / 9 / 4 | Diagrams on a poset as sheaves on its Alexandrov space; EI categories as exit categories; gluing along a sieve and its cosieve; proper and smooth functors and base change; strict bifibration representatives; the exit categories of the genus-zero moduli; other localizers |
| 6 PATHS | 76 | 40 / 11 / 19 / 6 | The path categories of chapter VII against the hammock localization; Cat-valued colimits against the Grothendieck construction; the tests (a), (b), (c) of chapter IX, rectification, Kaledin's enhancements; endpoint functors |
| 7 BISITE | 126 | 72 / 18 / 32 / 4 | The fine relative localizations of Cat/S and their two variances; complementarity of smooth and proper; open tests on spaces; base change, projection and exchange formulas; correspondences; dualizing weights; the genus-zero forgetting functor |
| 8 RESIDUE | 85 | 54 / 7 / 11 / 13 | What returns 1–7 left over ("residue" in that sense; nothing on residues and duality): transports over the monoid of type S²; absolute against relative Theorem A in chapter XVI; intrinsic fibrations; totality; open tests over the line; forgetting a marked point in all genera; correspondences and ambidexterity; second stages; strict 2-categories |

Status [C]: none of the four has a review at effort max. The folders `pro_reviews_max_20261112\5_STRATA` … `8_RESIDUE`
are empty; the expert stopped inside return 4. The section "What a successor should look for first in returns 5–8"
that my brief names is not in `KNOWLEDGE_HANDOFF.md`: the expert was told to put it in a final message, and the file
holds only the list of chapters each prompt names (its lines 164–168). The reviews of 10 November were made at effort
medium and do not count. So every row below is "the return's claim". The returns check one another in places
(RESIDUE D.10 recomputes all 48 entries of BISITE B.15; PATHS D.K1–K5 rechecks GALOIS B.9–B.12), which is evidence,
not a review.

### 3.2 Which results meet which archive chapters

| Results | The statement, in short | Meets | What it gives there |
|---|---|---|---|
| STRATA C.1–C.3, C.5 | A category X cut into a sieve A and its cosieve B is rebuilt from the crossing bimodule; BX is the homotopy pushout of BA ← BE → BB, E the category of crossing arrows; finite filtrations glue by their flag categories | 147 scans 164–169, 179–180; 150, 151; XII ms. 59–63 and app. ms. 17–18 | Bridge B1 in Cat. The flag categories are the candidate for his "déploiement" [G] |
| STRATA C.4, F.3 | Paths cannot replace crossing arrows; S² with a point has contractible strata and a circle of exit paths | 147 scan 180 ("Remords") | His counterexample and its reason, as numbered statements |
| STRATA C.6–C.8 | Coefficients on X are the lax pullback of those on A and B over E; taking homotopy categories first loses morphisms; locally constant coefficients form an honest pullback | 151 ("Topos stratifié"); 147 scan 179 (the system of groupoids of the pieces); 149 scans 133–135 (extensions (37), (38)) | The typed form of "a stratified topos is its pieces with gluing data", and the level at which it is true |
| STRATA A.1–A.6, A.12, B.1–B.3 | Diagrams on a poset are hypersheaves on its Alexandrov space, ordinary sheaves when down-sets are finite; an ordinary category is an exit category exactly when it is EI; finite acyclic categories are realized | 147 scans 164–165 (the four elementary types and their products); 151 | A prediction to test: his "topos élémentaires" are the presheaf topoi of the local exit categories, products of the four rank-one models [G] |
| STRATA F.1–F.17; BISITE F.15–F.17; RESIDUE H.1–H.7 | Exit categories of the stable genus-zero moduli, explicit for 4 and 5 points (4 and 26 strata; 236 for 6 points); forgetting a point is W∞-proper for every stable (g, n) and smooth only for (0,3); its bad lifting categories are BZ; the direct image along the universal curve is right Kan extension; clutching is a replete full cosieve | 147 §§7–10 and scans 60, 104; 146 scan 100 (S₀T_G); 142 scans 18–21; 149 scans 99–101; LM 2:sc349 | Bridges B1 and B14; the first half of S1. The BZ is the vanishing cycle at a node: whether it is what makes the filling map's kernel larger than point-pushing (LM3b B.4–B.6) is a question for EXIT_TOWER [G] |
| STRATA D.1–D.9; BISITE E, F.1–F.14; RESIDUE I.1–I.6, I.8 | Proper and smooth for functors of posets and of categories; the two base-change theorems and their converses; projection and exchange formulas with their exact restrictions; a correspondence formalism on the smooth class; the universally ambidextrous maps are the finite discrete bifibrations | 115 ("Correspondances fonctorielles. Dualité des topos", 14 pp., from 1982); 113–118 (the 1983 forms of XI–XII, XVI); cote 12 (motives over a base: the formalism asked for, bridge B9) | What the six operations are on Cat, with every hypothesis. The reader of 115 compares statement by statement [G that 115 is this] |
| BISITE G.1–G.14 | The dualizing weight of a homotopy-finite category; Verdier duality on a finite poset under an upper-interval criterion; ordinary Verdier duality need not preserve the least-vertex stratification | 115 ("dualité des topos"); 151 | The same reader |
| BISITE D.1–D.13; RESIDUE G.1–G.5 | Open tests: over a finite poset the localization of spaces over it is the diagram category; proper maps do not preserve open-test equivalences, local product maps do; over the line the comparison is open | 120, 121; 150 | Bridge B15 and S26: the place where tame hypotheses should enter |
| PATHS A.1–A.8; STRATA G.2; RESIDUE F.1–F.7 | For filtered shapes the colimit in Cat is the homotopy colimit; total asphericity does not suffice (Δ_inj); the exact class is open in the returns | II ms. 36–36ter; VII ms. 99–110; 147 scan 180 | S4. Today's theorem (unchecked) claims the exact class is the filtered one |
| PATHS B, C, E | Weak-vertical paths are the hammock localization; whether all-vertical paths give the same is open (B.8); loop and composition structures; every functor factors as a weak equivalence followed by a smooth and proper functor whose strict fibres are homotopy fibres (E.5) | The dossier around *Pursuing Stacks* (108, 114 and neighbours; unread); LM §§1–4 | For the dossier's reader: which of these his 1983 notes state. E.5 is a tool for tubes and unfoldings in Book V [G] |
| PATHS D.1–D.23, D.K1–K5 | The three tests of IX; what rectification needs; a relative poset can present BZ and fail rectification; all-small-shape invariance forces 1-types | IX; V ms. 44–46; the dossier | B2 and S12; the companion of VI |
| BISITE A, B, C; RESIDUE B, C, D | The localizer axioms as written against the adopted ones; XIIc B062 false (six, then five objects); the absolute package of XVI does not give relative Theorem A even with retracts or strong saturation; intrinsic fibrations of W_n, of homology localizers, of W_D(k)^lc | XVI; 117, 118 (its 1983 forms) | Edition notes for XVI; a question for the dossier's reader: did he have relative Theorem A in 1983? Input for S11 |
| STRATA E; PATHS E.6, E.11; BISITE B.21; RESIDUE A | Strict bifibration representatives exist over every poset, every base with 1-type classifying space, every base whose arrows are all monic or all epic; open over the five-element monoid of type S² | VI ms. 186–195 | Internal to Book VI (S27) |
| BISITE C.5–C.10, F.18; RESIDUE J | Strict higher categories: two fine theories, recognition over ordinary bases; open over genuine 2-cells | *Pursuing Stacks* (n-stacks); the dossier | Wait for the dossier |

### 3.3 What this means for the order and the prompts

1. **A review of 60 rows before anything else uses them.** The archive needs, in this order: STRATA C.1–C.8 and
   F.1–F.17; RESIDUE H.1–H.7 and G.1–G.5; BISITE D.1–D.13, F.15–F.17, G.9–G.12. One Fable reader at max in week 2
   (section 5), with the sections' proofs and the sources they cite. The full reviews of the four returns (368 rows)
   follow in weeks 3 and 4. Until then companions and prompts quote these rows as claims.
2. **The gluing reader starts in week 1.** Everything it needs is in hand (1.7, S3). Its first product is the
   dictionary: his words of 147 §§11–13 and 149 scans 128–136 against the statements above.
3. **Rank 5 and the dossier keep their early places in order W**, now for a second reason: they are the chapters these
   returns meet. Cote 115 is read as a keystone. Their context zips carry the rows of 3.2 with status.
4. **The six packaged prompts go now, unchanged.** PRESHEAF_TOTALITY and TOTAL_EXACT first: they carry the check of
   today's theorem, which would close PATHS A.8 and RESIDUE F.7 at once. REVERSIBLE_LOCALIZERS covers RESIDUE I.7.
5. **New prompts that returns 5–8 call for** (specified in section 6): TAME_REALIZATION (BISITE D.12, RESIDUE G.3,
   after 120–121); HAMMOCK_FULL (PATHS B.8); a decision on S27. The open rows on strict higher categories wait for
   the dossier. STRATA A.6 and B.5 (geometric sheaf exodromy beyond the finite case) are left: Haine–Porta–Teyssier
   cover the tame cases we need.
6. **EXIT_TOWER and LM5 are rewritten against these rows**, not against LM3 alone: the uncompleted categories exist;
   the prompts ask for completion, for the comparison with his MDT-structure and with the models of 146, and for
   the Galois action.

---

## 4. The protected core and the cut order, at 0.04 points a scan

### 4.1 Inputs

- In the Pro queue 10,761 pages; returned 693 (611 and the 82 of the first Book II package); to send 10,068
  [C, round 1's figures and `RETURN_NOTES.md`].
- Opus: 0.04 points a scan for the full second pass (the corrected figure). I take it to include the global pass; if
  the global pass is measured separately, add it. Available for the archive: about 12 points in what is left of
  this week and 50 a week after it [C, round 1's reading of the report; the brief's budget], so about 162 points in
  the four weeks to 9 December.
- Pro: one stream of 45 scans takes about 80 minutes, 70 take 130, 90 take 165 (round 1, for the hand of the 1980s).
  Measured today on the hand of the 1960s: 82 scans in 92 minutes, notes included [C, `progress.log`]. Nine runs a
  day when sending is steady [G]. Pro mode may end with November.
- Light rate for reused typed sheets and for pages checked against print: 0.01 points a scan [G, a quarter of the
  full rate as in round 1]. Share of reused sheets in Paris-years folders: a quarter [C for one package, G beyond].

### 4.2 The core, part by part

Pages are those still to send. "Runs" are Pro runs of at most 70 and at most 90 scans, cotes of one unit packed
together. Opus points are for a full pass at 0.04.

| | Part of the core | Pages | Runs ≤ 70 | Runs ≤ 90 | Opus, full |
|---|---|---|---|---|---|
| a | III returned: 147, 149, 146, 142 | (566 returned) | — | — | 22.6 |
| b | II first return: 16, 47, 54, 44 | (82 returned) | — | — | 3.3 (2.4 tiered) |
| c | III rank 4: 144, 148, 143, 145, 141 | 339 | 5 | 4 | 13.6 |
| d | V rank 5: 150, 151, 152, 120, 121 | 280 | 4 | 4 | 11.2 |
| e | V: 156-1, -2, -3, -5, -8, -9 | 397 | 6 | 5 | 15.9 |
| f | VI: 158 and the dossier 103–109, 111–118, 135 | 437 | 7 | 5 | 17.5 |
| g | VI: the handwritten leaves of 134 (new; confirm they are not already queued) | about 95 | 2 | 2 | 3.8 |
| h | II.9: 137, 136, 133, 153 | 523 | 8 | 6 | 20.9 |
| i | II: crystals 4–9, 100 (built) | 356 | 6 | 4 | 14.2 (11.6 tiered) |
| j | II: motives 14, 13, 12, 15, 18 | 637 | 10 | 8 | 25.5 (20.7 tiered) |
| k | I: 21, 22, 23, 26, 35, 48, 102; 127, 128 | 242 | 4 | 3 | 9.7 |
| l | III periphery: 64, 67, 159, 138 | 421 | 7 | 5 | 16.8 |
| m | IV: 76, 88, 70, 75, 161-6; 79, 83, 72, 86, 85 | 1,025 | 15 | 12 | 41.0 |
| n | II rest: 10, 11, 56, 60, 155; and 93 | 608 | 10 | 8 | 24.3 (19.4 tiered) |
| o | V: 154, and 80 if the probe says so | 247 | 4 | 3 | 9.9 |
| p | Front door 161-3, 161-4; cote 1 (45 returned) | 85 | 2 | 1 | 5.2 |
| q | New probes: 43 (first 45 scans); 49, 50, 51, 52 | 99 | 2 | 2 | 4.0 |
| | **Core** | **5,791** | **83 to 92** | **65 to 72** | **259 (248 tiered)** |

- The lower figure of each range is the page count divided by the run size, the higher is the sum of the rows.
  With the keystone parts at 70 (c, d, e, f, g, h, q and all probes) and the rest at 90: about 78 runs.
- With one research run to three transcription runs: 87 to 123 runs; at nine a day, 10 to 14 days. The core can be
  through Pro by 22 to 26 November [G for the rate].
- Everything in the queue: 10,163 pages with row g, 113 runs at 90 or 146 at 70; with 30 research runs, 143 to 176
  runs, 16 to 20 days: the last days of November. As in round 1, the whole fits only if nothing slips.

### 4.3 What the Opus weeks cover

In the order of mathematical dependence, with the tiers of 4.1 (reused typed sheets light; the ten probes taken out
of their rows and checked as they return, 446 scans, 17.8 points):

| Step | Second pass of | Points | Running total |
|---|---|---|---|
| 1 | a: Book III returned (149; 147 §§9–13; 142 scans 1–22 and 94–122 first) | 22.6 | 22.6 |
| 2 | b: first Book II return | 2.4 | 25.0 |
| 3 | c: rank 4 | 13.6 | 38.6 |
| 4 | d with 153, 155: rank 5 | 12.0 | 50.6 |
| 5 | the ten probes | 17.8 | 68.4 |
| 6 | f, g: the dossier, 158, the leaves of 134 | 21.3 | 89.7 |
| 7 | h without the probe and 153: 137, 133, the rest of 136 | 18.7 | 108.4 |
| 8 | i: crystals | 11.6 | 120.0 |
| 9 | j: motives | 20.7 | 140.7 |
| 10 | e without the probe: 156-3, -5, -8, -9 | 14.1 | 154.8 |
| 11 | k: the EGA plans, 127, 128 | 9.7 | 164.5 |
| | **the four weeks end here (about 162 points)** | | |
| 12 | l without its probes: 64, 67, the rest of 138 | 13.7 | 178.2 |
| 13 | m without its probes: Book IV | 37.4 | 215.6 |
| 14 | n: the rest of Book II, the rest of 93 | 19.4 | 235.0 |
| 15 | o, p: 154 and 80; the front door; cote 1 | 13.3 | 248.3 |

At 0.025 the core fitted the four weeks (round 1). At 0.04 it does not: steps 12 to 15, 84 points, need a fifth
and most of a sixth week at 50 points. The four weeks cover Book III with rank 4, Book V with 156, the dossier,
II.9, and Book II through the motives: about 4,100 scans, the chapters our results meet and the chapters nobody has
read. They do not cover Book IV beyond its probes.

**If no fifth week is given**, in this order: Book IV's calculation folders (72, 86, 85) get recomputation by
script and the light rate; then all of step 13 at the light rate (9.4 points for 37.4); then step 14 at the light
rate; steps 12 and 15 stay full. That brings steps 12 to 15 to about 45 points, one week.

### 4.4 The cut order if Pro mode ends early

The send order is the protection order. Cumulative pages and runs:

| Send | Pages | Cumulative | Runs ≤ 70 | Runs ≤ 90 |
|---|---|---|---|---|
| 1. crystals (built) | 356 | 356 | 5 | 4 |
| 2. rank 4 | 339 | 695 | 10 | 8 |
| 3. rank 5 with 153, 155 | 300 | 995 | 14 | 11 |
| 4. the ten probes | 446 | 1,441 | 21 | 16 |
| 5. the leaves of 134, 158, the dossier, 137, 133 | 670 | 2,111 | 30 | 24 |
| 6. the rest of 136 | 330 | 2,441 | 35 | 27 |
| 7. motives | 637 | 3,078 | 44 | 34 |
| 8. 156-3, -5, -8, -9 | 353 | 3,431 | 49 | 38 |
| 9. the EGA plans, 127, 128 | 242 | 3,673 | 53 | 41 |
| 10. maps (rank 10), the rest of 79 and 83, 64, the two popular texts | 930 | 4,603 | 66 | 51 |
| 11. 67, the rest of 138, 72, 86, 85 | 433 | 5,036 | 72 | 56 |
| 12. the rest of Book II, the rest of 93, 154 and 80 | 755 | 5,791 | 83 | 65 |

Read with research runs interleaved one to three, the count of slots is a third higher. After 40 transcription
runs, rows 1–6 are through at 70 scans a run and rows 1–8 at 90; the maps are not. After 60, rows 1–9 and a third
of the maps at 70, rows 1–11 at 90.

Outside the core (about 4,300 pages), round 1's cut order stands, first cut first: ranks 21 and 24; rank 23; ranks
19, 20 and the rest of 22; rank 25 without cote 66; the three earlier versions of Analysis situs; 161-1, 161-2, 19;
the calculation folders; 71, 81, 132, 161-5. Two amendments: cote 43 and the notes 49–52 are probed before their
ranks are cut; *Pursuing Stacks*, the Esquisse and cotes 24–25 leave the Pro queue for the API (their handwritten
leaves stay in it, row g).

---

## 5. The next four weeks

Weeks are counted from 12 November; shift them to the meter's own reset day. Budgets: Opus about 12 points in week
1 and 50 in each later week; Fable what is left of the current allotment in week 1 (I assume about 10 points after
this pass [G]) and 100 points at each of the three resets, which I place at the start of weeks 2, 3 and 4. A Fable
reader holds 220k tokens of sources and costs about 4.5 points; "fill" is the share of the 220k I expect it to use.
"Compact notes" means the page notes of a return cut to rows by script, its post-freeze sections kept whole.

### Week 1 (12–18 November)

| | |
|---|---|
| **Pro packages** (about 27 runs) | The crystals, built: cotes 4–9 and 100 (356 scans, 4 runs of ≤ 90). Rank 4: 144, 148, 143, 145, 141 (5 runs of ≤ 70). Rank 5 with 153 and 155 (5 runs of ≤ 70). The ten probes, one run each or paired by hand and decade: 156-1 with 156-2; 136 scans 2–46; 93 scans 2–46; 79; 83; 154; 138; 159 whole; 43; 49–52 whole. The leaves of 134 with 158 (3 runs of ≤ 70). Before sending: the repairs of round 1 (one stream, the 31 dropped scans, the zip check) and the "sheet kind" column |
| **Opus** (12 points, 300 scans) | Cote 149 whole (136 scans, 5.4). 147 scans 90–190, §§9–13 (4.0). 142 scans 1–22 and 94–122 (2.0). Within these, first the readings listed in 1.3 and the dependency lists of the two readers below. Outside the meter: the reconnaissance pass over title sheets, reused sheets and dates, starting with the Paris-years folders |
| **Fable readers** (2; 9 points) | **R-149**: cote 149 (55k), its two notes files compacted (about 40k), the opening text of 142 (15k), the LM6 draft with FINDINGS F5–F8, F15–F18, F24–F26 (25k); fill 60 %. Product: LM6 revised; the check of R2 and R3 against his text; the status table of 1.3 made exact; what goes beyond the letter to Faltings. **R-GLUE**: 147 scans 90–190 with compact notes (90k), 149 scans 128–136 (5k), STRATA sections C and F (55k), RESIDUE Part H and BISITE F.15–F.17 (25k), the notes on XII and its appendix (10k); fill 85 %. Product: the dictionary of 3.3; LM5 revised; EXIT_ONE_TYPE and EXIT_TOWER in final form |
| **Research prompts** (10 runs) | The six packaged ones, PRESHEAF_TOTALITY and TOTAL_EXACT first. CYCLOTOMIC_KERNEL. FLAGGED_149. EXIT_ONE_TYPE. FOURIER_1970 |

### Week 2 (19–25 November)

| | |
|---|---|
| **Pro packages** (about 29 runs) | The dossier 103–109, 111–118, 135 (6 runs of ≤ 70). 137 and 133 (2). The rest of 136 (5 of ≤ 70). The motives 14, 13, 12, 15, 18 (8 of ≤ 90; the typed sheets of 12 and 15 to the API after an inventory). 156-3, -5, -8, -9 (5 of ≤ 70), briefed from the probe. The EGA plans with 127, 128 (3 of ≤ 90) |
| **Opus** (50 points, 1,250 scans) | The rest of 147 (3.5), 146 (5.4), the rest of 142 (2.8). The first Book II return, tiered (2.4). Rank 4 (13.6). Rank 5 with 153, 155 (12.0). The first five probes back (8.9). Global pass of III.1 with III.4 as one unit |
| **Fable readers** (15; 68 points, and 10 for the three experts) | **R-147**: 147 scans 3–89 with 146, compact notes; fill 80 %; carries the questions of round 1 on the MDT-structure and S₀T_G. **R-142**: 142 scans 22–122, compact notes, LM2 B.m2 and C, the LM4 draft; fill 60 %; dates the layers, writes his equations against (I), (II), drafts GT_CATEGORY. **R-II-1**: 16, 47, 54, 44 with their post-freeze notes, Kleiman's text of 1968, "Standard conjectures"; fill 60 %; writes LEFSCHETZ_RINGS and JACOBIANS_1964, the lettering table, the date of 47. **R-II-2, R-II-3**: the crystals in two halves with 54; fill 80 % each; the questions of 2.4. **R-4a, R-4b**: rank 4 (144 with 148; 143, 145, 141) with the LM findings; fill 85 %; the three checks of round 1 and the two of 1.4. **R-GLUE-2**: 150, 151, 152 against the dictionary; fill 80 %; writes DEVISSAGE. **R-TAME**: 120, 121, 153, 155 with the o-minimal axioms, BISITE Part D, RESIDUE Part G; fill 65 %; writes TAME_AXIOMS and TAME_REALIZATION. **R-P1, R-P2, R-P3**: the ten probes in three groups (156-1/2, 136, 154; 93, 159, 43, 49–52; 79, 83, 138); fill 65–75 %; each ends in a decision on placement and package size. **R-REV60**: the 60 rows of 3.3 with their proofs; fill 80 %. **R-LM-II, R-LM-III**: the Longue Marche Parts II and III (round 1) |
| **Research prompts** (9 runs) | LM6 revised. LM5 revised. EXIT_TOWER. LM4 revised with GT_CATEGORY. POLYHEDRA_SHADOWS. LEFSCHETZ_RINGS. JACOBIANS_1964. DEVISSAGE if rank 5 is read. HAMMOCK_FULL |

### Week 3 (26 November – 2 December)

| | |
|---|---|
| **Pro packages** (about 27 runs; Pro may end on the 30th) | The maps (rank 10) with the rest of 79 and 83, 64 and the two popular texts (11 runs of ≤ 90). 67, the rest of 138, 72, 86, 85 (5). The rest of Book II: 10, 11, 56, 60 (5). The rest of 93 (3). 154 and 80 if the probes say so (3). This completes the core |
| **Opus** (50 points) | The other five probes (8.9). The dossier, 158 and the leaves of 134 (21.3). 137, 133 and the rest of 136 (18.7). The start of the crystals (1.1). Global pass of V.3 with 147 §§11–13, and of II.9 with VI.5 |
| **Fable readers** (17; 77 points, and 8 for the experts) | **R-VI-1, -2, -3**: the dossier, 158 and the leaves of 134 in three parts, each with the rows of NEW_RESULTS and of 3.2 it must locate in 1983; fill 80 %; 115 goes to the first. **R-SCHEM**: 137, 133, 153, extracts of *Pursuing Stacks* VI–VII, RESIDUE D and I.9; fill 75 %; writes SCHEMATIZATION_LOCALIZER. **R-136a, R-136b**: cote 136; fill 85 %; the plan of the lost lecture. **R-M1, R-M2, R-M3**: the motives (14 with 18; 13 with 15; 12 with "Motifs"), compact notes; fill 85 %; the table of round 1, stage 7. **R-156a, R-156b**: 156 final; fill 85 %. **R-REV-S, R-REV-R**: the full reviews of STRATA and RESIDUE. **R-LM-IV, R-LM-draft**: as round 1. **R-RET-1, R-RET-2**: the returns of weeks 1–2 (CYCLOTOMIC_KERNEL, EXIT_ONE_TYPE, the totality prompts, FOURIER_1970), proofs read line by line |
| **Research prompts** (8 runs) | TAME_AXIOMS with TAME_REALIZATION. SCHEMATIZATION_LOCALIZER. LECTURE_1976. ORIGINS_1983. LM7. LM8 with the elliptic tables. MOTIVES_TABLE. One follow-up chosen from the week-1 returns |

### Week 4 (3–9 December)

| | |
|---|---|
| **Pro packages** (if Pro lasts) | Outside the core, round 1's cut order read backwards: 71, 81, 132, 161-5; the calculation folders; 161-1, 161-2, 19; the three earlier versions of Analysis situs; then as far as the runs go. Follow-up research runs |
| **Opus** (50 points) | The crystals (10.5). The motives (20.7). 156-3, -5, -8, -9 (14.1). The start of the EGA plans (4.7). After this week about 88 points of the core remain (4.3) |
| **Fable readers** (17; 77 points) | **R-I**: the EGA plans and cote 25, the three-column map; fill 70 %. **R-IV-1 … -4**: the maps, 79, 83, 64, compact notes; fill 85 %. **R-IV-5**: 67, 72, 86, 85 on the transcription alone, after the scripts; fill 60 %. **R-II-4, R-II-5**: 10, 11, 56, 60 and 93 on the transcription alone; fill 80 %. Four bridge readers: the Galois group twice (13, 15, 149, LM §§5 and 32–36, LM3 D–E); maps and modular polyhedra; finite models (120, 121, 156, *Les Dérivateurs* V and XVI §6, CATHOT); gluing, the final write-up for the companions of III.4, V.3 and VI. **R-REV-B, R-REV-P**: the full reviews of BISITE and PATHS. **R-RET-3, R-RET-4**: the returns of weeks 2–3. **R-ALL**: reads only the FINDINGS, PREDICTIONS and BREAKS files and rewrites sections 1.2 and 1.7 with round 1's 1.2 and 3 |
| **Research prompts** | Follow-ups only: what the readers of weeks 2–3 ask for; FORMS if 156 calls for it; the decision on S27 |

**Totals.** Pro: about 83 transcription runs for the core in three weeks and 27 research runs, 110 of about 160
slots to 30 November [G for the slots]; the remaining slots go to the periphery. Opus: about 160 points. Fable: 51
readers, 230 points, and 28 for the experts and re-reads, of about 310; the rest is reserve for a keystone chapter
that has to be read twice.

---

## 6. The research prompts to write first

Every prompt keeps the form fixed on 12 November: the results it builds on with their status; per item what counts
as done; what is unacceptable; when it is finished. "Draft" means a text exists; "spec" means only the paragraph
here or in round 1.

**Exist as packaged drafts** [C, `derivateurs_companion_20261109\pro_prompts_max_20261112\`]: PRESHEAF_TOTALITY,
TOTAL_EXACT, REVERSIBLE_LOCALIZERS, FINMON, INDLOCAL, S2COUNT. Send as they are.
**Exist as drafts to revise** [C, round 1]: LM4, LM5, LM6 (drafted on the Longue Marche alone); LM7, LM8.
**Spec only, to write first**, in this order:

1. **CYCLOTOMIC_KERNEL** (spec in round 1; extended here). Asks: for a hyperbolic curve U over a number field K
   and any section s, prove or refute that the centralizer in the geometric fundamental group of s(Γ°) is trivial
   when s is not cuspidal and is the inertia group when it is (R2), following the four steps of section 7 and
   citing the weight criterion for inertia from its source with its exact hypotheses; then, each with proof: the
   case (0,3) of his Proposition (149 scan 54); the "conséquence conjecturale" of scan 49; the statement of scan 45
   (R3); what remains of Conjecture B for Γ° (S7), with the toric obstruction made explicit; the same over fields of
   finite type over Q (Katz–Lang) and over K(μ_∞); the corrected §34 of the Longue Marche. Done: a verdict and a
   full proof or counterexample per item. Unacceptable: assuming the section conjecture; "known" without the
   source opened. Builds on 149 scans 45–63, FINDINGS F5, F17, LM3b D (claims).
2. **FLAGGED_149**. Asks: every step that cotes 149 and 142 mark as unverified, listed with scan and his words
   (149 scans 14, 15, 21, 45, 78, 79, 119, 130; 142 scans 5–7, 10, 11, 14), is proved with a citation opened or
   refuted with a counterexample; among them the centre and torsion of free profinite groups, the injectivity of
   Γ → Autext(π) (scan 21), N_V = Norm(I_V) (scan 119), the inertia computation μ·κ_i (scans 76–79) with its case
   ν = 1, hypothesis (*) and the injectivity hypothesis of 142. Done: one row per flagged step. This is the
   cheapest prompt in the list and clears the ground for LM6.
3. **EXIT_ONE_TYPE** (spec in round 1; revised). Starts from STRATA F.1–F.3 and F.6 (claims). Part 1: prove or
   correct S2 for a normal-crossings pair. Part 2: the dependence on the compactification that he notes at 149
   scan 130: what a blow-up of a stratum does to the exit-path ∞-category and to the criterion. Part 3: his
   question of a minimal model, in dimension 2 and for Artin's elementary neighbourhoods. Part 4: the boundary
   complex (S25): the functor from the exit-path category at infinity to the poset of strata, and what Thuillier's
   and Payne's theorems say in these terms. Tests: (P¹, ∞), M̄(0,n), a toric surface, a product of curves, a fibre
   of finite monodromy. Done: Part 1 with full proof; a theorem or a counterexample for each of Parts 2 and 3.
4. **FOURIER_1970**. Asks: (i) complete the proof of the inversion theorem of 47 as he set it up, over an
   arbitrary base, including the compatibility at the unit section that he leaves (scan 8), and state which
   boundedness is needed for his remark on quasi-coherent complexes; (ii) prove the generalizations of the margin
   of scan 3 (flat group schemes; pairings of torsors) or give counterexamples; (iii) the heuristic of scan 9 with
   the right coefficients, on which categories of cycles it holds, and his question "modulo torsion" against
   Moonen–Polishchuk and Beckmann–de Gaay Fortman; (iv) the sign he charges to Kleiman (scan 11), settled by a
   convention-exact comparison. Done: each of (i)–(iv) with proof. Builds on the notes' F1–F20 (first-pass claims).
5. **LM6, revised**. To the 1981 conjectures of the Longue Marche it adds 149: the Conjecture fondamentale in its
   form with E°; Conjectures A, B, B′; a) and b) of scan 126–127 and their equivalences; S23 (the
   "conjecture-à-tout-hasard", with R4 to check and the compact-type case with isogenous components to attack);
   S24 stated. Each item: his statement typed, its status with source, a proof where one is in reach. Written by
   R-149.
6. **LM5, revised**. The topoi: 149 scans 3–20 (the six points of view), scan 52, 147 §§11–13, against STRATA A–C.
   Written by R-GLUE.
7. **EXIT_TOWER** (spec in round 1; reduced as in 1.7). Asks: his MDT-structure and the models S₀T_G identified
   with the entrance categories of the returns; the completed tower with its functors; whether the lifting
   categories BZ of RESIDUE H.3 account for LM3b B.4–B.6; the open rows LM3 F.16, LM3b E.4, E.9, H.9.
8. **GT_CATEGORY with LM4, revised**. Asks: his category of 142 defined with all hypotheses proved; its profinite
   envelope and automorphism group; the extension by hole-filling through admissible covers (S5), or the precise
   reason it fails; the equations of scans 25–42 against (I), (II) with the dating evidence. Written by R-142.
9. **LEFSCHETZ_RINGS**. Asks: nos 1–8 of 16 proved over Q, with the universal property of Φ and the eight
   formulas (6.14); the two failures over Z (2.3) and the order that the integral operators generate, for n ≤ 4
   by computation; his question on characterizing Lefschetz elements, with the example of scan 22 generalized;
   the motivated cycles of André as the free lefschetzien ring on the algebraic correspondences, and Künnemann's
   theorem as an instance; the Hodge algebras of order 2 classified, with R1. Done: each with proof or program.
10. **JACOBIANS_1964**. Asks: Th. 1–7 of 44 one by one: proved (with the modern source), false (with the
    counterexample), or open (with the exact gap); Th. 5 proved over a function field as a statement on the
    height pairing of Beilinson and Bloch, with its local variant; Th. 4 in characteristic p stated against the
    auto-duality of Achter–Casalaina-Martin–Vial.
11. **POLYHEDRA_SHADOWS**: as round 1.

**After the returns and readings named** (one line each): DEVISSAGE and TAME_AXIOMS (rank 5; round 1);
TAME_REALIZATION (S26: prove the open-test comparison over compact tame bases by triangulation from BISITE D.2,
or find where it fails); HAMMOCK_FULL (PATHS B.8, the six variants one by one); SCHEMATIZATION_LOCALIZER (S11, on
W_sch(k) with finite-dimensional local systems, starting from RESIDUE D.5, D.11, I.9); LECTURE_1976 and
ORIGINS_1983 (round 1, stages 6 and 8); LM7; LM8 with the elliptic tables (S9); MOTIVES_TABLE (S15).

---

## 7. Results found in this pass (all unchecked)

**R1. The threshold in 16 scan 29 is 6.** *Statement.* Let V have dimension 4, χ ≠ 0 a 4-form, Q(a, b) = χ(a∧b) on
Λ²V, ξ ∈ Λ²V with Q(ξ, ξ) = 1 and φ(x, y) = Q(x∧y, ξ) non-degenerate, φ̌ ∈ Λ²V the inverse bivector, and
u = Λ²(φ^♯) ∘ Q^♭ (the convention of the notes' D19). Then u(ξ) = 2ξ, u = −2 on the Q-orthogonal complement of ξ,
and φ̌ is a multiple of ξ. So the orbits of ξ and φ̌ under u span a line: nothing happens in dimension 4, and the notes' example
(D19) shows that spans of dimension 3 occur in dimension 6. *Sketch.* All such (χ, ξ) are equivalent over an
algebraic closure; in the normal form ξ = a e₁∧f₁ + b e₂∧f₂, χ = c e₁*∧f₁*∧e₂*∧f₂* with 2abc = 1 one finds
u(e₁∧f₁) = e₂∧f₂/(a²c), u(e₂∧f₂) = e₁∧f₁/(b²c) and u = −2 on the four mixed basis vectors. *Meaning.* For an
abelian surface u is twice the Hodge star on H²: the Fourier transform followed by pull-back along the
polarization. *What would check it.* A six-by-six computation by script; the reading of "4 (ou 6 ?)" and of the
definition of u on the scan.

**R2. The cyclotomic kernel sees the cusps (S6 of round 1, argued in full).** *Statement.* K a number field, U a
hyperbolic curve over K, π its geometric fundamental group, s a section, Γ° the kernel of the cyclotomic character,
C the centralizer of s(Γ°) in π. If U is proper, C = 1. If U is affine, C = 1 unless s normalizes an inertia group
I_x, and then C = I_x and x is unique. *Sketch.* (1) Let z ≠ 1 be in C, N an open characteristic subgroup of π not
containing z, H = N⟨z⟩. An open subgroup of Γ normalizes H through s, so H belongs to a covering defined over a
finite extension K′, and the class of z in H^ab is fixed by Gal(K̄/K′(μ_∞)). (2) Proper case: H^ab is the Tate
module of a Jacobian; it has no invariants under that group, because the torsion of an abelian variety over K′(μ_∞)
is finite (Ribet [C, lookup 10]); but z generates H/N ≠ 1. (3) Affine case: by the same theorem the class of z lies
in the image W of the inertia groups in H′^ab, for every open H′ containing z; by the weight criterion for inertia
(Nakamura; Stix, Theorem 20 [C for its existence, lookup 6; its exact form to be checked]) z lies in an inertia
group. (4) C lies in one inertia group: if z ∈ I_x and z′ ∈ I_y were non-trivial elements of C with x ≠ y, then
zz′ ∈ C lies in some I_w; in an open H containing C with at least four cusps in which x and y are distinct, W is
the free module on the cusps modulo the diagonal, and the relation [z] + [z′] = [zz′] forces [z] = 0 or [z′] = 0,
while an inertia group of H injects into H^ab. (5) Γ° is normal, so s(Γ) normalizes C and hence I_x; conversely a
section normalizing I_x acts on it through the cyclotomic character, so I_x ⊂ C. *What it gives in 149.* His
"précisions" to Conjecture A (scan 56 margin); (3) of scan 55; the missing case (0,3) of the Proposition of scan
54; the "conséquence conjecturale" of scan 49 for curves; for Γ°, at most one fixed point at infinity in
Conjecture B; and the reading that his Conjecture fondamentale for V a point is the section conjecture. It
repairs the Longue Marche §34 (FINDINGS F17). *What would check it.* CYCLOTOMIC_KERNEL. *Novelty.* None claimed;
recent work over cyclotomic extensions uses the same theorem of Ribet (1.7).

**R3. The centralizer in Γ_Q of the absolute Galois group of k(μ_∞) is trivial** (149 scan 45, "à vérifier !").
*Sketch.* Enlarge k to be Galois over Q; put F = k(μ_∞). Let σ commute with every element of G_F. Then for every
x the stabilizers of x and σx in G_F agree, so F(σx) = F(x); in particular σ(F) ⊂ F, and for a ∈ F* and a prime ℓ,
Kummer theory gives σ(a) = a^j c^ℓ with j prime to ℓ. If σ moved a number field k′ ⊂ F, Galois over Q, take p
split completely and unramified in k′, a prime 𝔭 above it (so σ𝔭 ≠ 𝔭), a ∈ k′ of valuation 1 at 𝔭 and 0 at the
other primes above p, and ℓ not dividing p(p − 1). At a place of F above 𝔭 the value group is (1/(p − 1))·Z[1/p], in
which 1 is not divisible by ℓ; the valuations of σ(a) = a^j c^ℓ give 0 ≡ j modulo ℓ, a contradiction. So σ fixes
F. The same argument over every finite extension of F, each again of the form k″(μ_∞), shows σ = 1. *What would
check it.* One Part of FLAGGED_149; it is probably in the literature on Hilbertian fields.

**R4. The limit action at a place of bad reduction is not that of a curve** (149 scans 101–103, e ⟹ a).
*Statement.* Let U_η be a proper hyperbolic curve over the fraction field of a henselian trait with residue field
k of finite type over Q, with stable bad reduction. For any splitting of 1 → T → 𝓔_η → 𝓔_k → 1, the resulting
outer action of 𝓔_k on π is not the outer action attached to a smooth proper curve over a finite extension of k,
(i) if the Jacobian has toric rank t > 0, (ii) if t = 0 and the components of the special fibre have pairwise
non-isogenous Jacobians with endomorphism ring Z. *Sketch.* (i) On π^ab ⊗ Q_ℓ the Frobenius weights of the limit
action are 0 and −2 with multiplicity t and −1 elsewhere (the monodromy filtration; the graded pieces do not depend
on the splitting), while H₁ of a smooth proper curve is pure of weight −1. (ii) π determines H₁ with its symplectic
form; here it is that of the product of the Jacobians of the components with the product polarization; an
isomorphism with H₁ of a smooth curve C, for all ℓ and compatible with the forms, makes Jac C isomorphic to that
product as a polarized variety (Faltings; the hypothesis leaves no other principal polarization), and the theta
divisor of a Jacobian is irreducible. *Left open.* Compact type with isogenous components, where H₁ with its form
does not decide. *What would check it.* A Part of LM6 revised.

**A reading, not a result.** Th. 5 of 44 ("Néron") is the height pairing of Beilinson and Bloch over a function
field, twenty years before it was defined [B]: to be confirmed by JACOBIANS_1964.

---

## Lookups made (15), and what each settled

1. Search for a mention of a Fourier transform on abelian varieties by Grothendieck before Mukai: nothing found.
2. Tsujimura, "Birational anabelian Grothendieck conjecture for curves over arbitrary cyclotomic extension fields
   of number fields", Adv. Math. 435 (2023), 109380: publication confirmed, statement not shown. A 2025 preprint
   (arXiv:2501.11277) on Kummer extensions over maximal cyclotomic fields names "a finiteness theorem of Ribet".
3. Achter–Casalaina-Martin–Vial, "Decomposition of the diagonal, intermediate Jacobians, and universal
   codimension-2 cycles in positive characteristic" (Astérisque 455, 2025; arXiv:2007.07470): a canonical
   auto-duality on the intermediate Jacobian of a threefold, agreeing with the Hodge-theoretic principal
   polarization in characteristic 0. Whether it is a polarization in characteristic p: not shown.
4. Good reduction of hyperbolic curves: Oda's criterion (proper), extended by Tamagawa (affine); H¹ alone does not
   suffice (from surveys and papers that state it, among them arXiv:1801.08728).
5. Payne, "Boundary complexes and weight filtrations" (arXiv:1109.4286), Theorem 1.1: the simple homotopy type of
   the boundary complex is independent of the compactification (with Thuillier 2007); its reduced homology is the
   top graded piece of the weight filtration.
6. Stix, "On cuspidal sections of algebraic fundamental groups" (arXiv:0809.0017), Theorem 20, attributed to
   Nakamura: a non-trivial closed subgroup of the geometric fundamental group lies in an inertia group if and only
   if it is pro-cyclic and (essentially) cyclotomically normalized; Nakamura 1994 announces a "weight
   characterization of inertia subgroups" in its §2.1. The form used in R2 was not shown.
7. Esnault–Hai, "Packets in Grothendieck's section conjecture" (Adv. Math. 218, 2008; arXiv:math/0703877); Stix
   on tangential sections; Bresciani (arXiv:2108.13397): the section conjecture is equivalent to the cuspidalization
   conjecture of Esnault and Hai.
8. Corti–Hanamura, "Motivic decomposition and intersection Chow groups I" (arXiv:math/9804123): the standard
   conjectures should extend to singular varieties; a motivic decomposition theorem from the standard conjectures.
9. Search for the text of the letter to Faltings on the kernel of the cyclotomic character: only the locations of
   the letter and its translation were found.
10. Ribet's theorem (appendix to Katz–Lang, 1981): for an abelian variety over a number field k, the torsion over
    k(μ_∞) is finite; restated in several recent papers.
11. Haine–Porta–Teyssier, "Exodromy beyond conicality" (arXiv:2401.12825): exodromic stratified spaces; compact
    subanalytic stratified spaces have finite exit-path ∞-categories.
12. Künnemann: a Lefschetz decomposition for Chow motives of abelian schemes, confirmed through papers that cite
    it; the reference Invent. Math. 113 (1993) is from memory.
13. Fetch of the English letter to Faltings at williamstein.org: failed (HTTP 522).
14. Fetch of the same at the Circle's site under a guessed address: failed (HTTP 404). What 149 adds to the letter
    stays a task of the reader R-149.
15. A second search for the history of the Fourier transform before Mukai (Lieberman, Kleiman, Grothendieck):
    nothing found on Grothendieck.

Sources of the lookups: arxiv.org (1109.4286, 0809.0017, math/0703877, 2108.13397, math/9804123, 2401.12825,
2007.07470, 2501.11277, 1801.08728), en.wikipedia.org (Fourier–Mukai transform), kurims.kyoto-u.ac.jp (reference
lists), webusers.imj-prg.fr and williamstein.org (the Circle's list of letters).

