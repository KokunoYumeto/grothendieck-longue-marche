# LM_P020 (scans 191–200): research notes, checked

The first pass's research notes R01–R39 are checked here against the corrected transcription `LM_P020_checked.tex`; its doubt table and abbreviation list are superseded by that file and by `LM_P020_changes.md`. Each note gives the scan, the kind and a verdict (keep, correct or drop) with the reason. Notes O1–O9 are mine (Claude, second pass), labelled "own". Mathematical statements are Grothendieck's unless a note is marked "own"; none of his claims here is proved in this extract.

## A. First-pass notes

**R01 — scan 191 — claim without proof — keep.** The construction of Eᵢ with 1 → Lᵢ → Eᵢ → Γ → 1 is said to work without a finiteness hypothesis on Γ ("s.s hyp. de finitude", most likely the abbreviation of "sans"; CSG/IUT "sans"), the universal case being the Teichmüller group of π′ fixing i, Autext_lac(π′;i) ≃ Aut_lac(π). No proof is given here.

**R02 — scans 191–195 — claim without proof — correct.** The theorem (finite Γ acting faithfully and fixing i is cyclic if Γ = Γ°, dihedral otherwise, with Eᵢ° ≃ ℤ and Γ° ≃ T/nT canonically) is reduced to the lemme fondamental, which is then admitted. The corrected margin (CSG/IUT footnote 60) says "il y a équivalence, si dans le th, on suppose le type (g,ν) anabélien — sinon le th. est un peu plus général", not "euclidien … donc": the restated theorem is equivalent to the preceding statement in the anabelian case and slightly more general otherwise.

**R03 — scans 191–192 — claim without proof — keep.** "(évidemment indépendant du choix de Lᵢ …)" is asserted. A proof must compare the identifications Γ° ≃ Eᵢ°/Lᵢ ≃ T/nT for Lᵢ and its π-conjugates.

**R04 — scan 192 — claim without proof — keep.** The extension of Γ° by T is identified, through the cohomology sequence of 0 → T → T⊗ℚ → T⊗ℚ/ℤ → 0, with the pull-back ("image inverse", which the witnesses drop) of 0 → T → T → Tₙ → 0 along a homomorphism Γ° → Tₙ. The argument uses the trivial action on T stated on the page; the connecting maps are not written out.

**R05 — scan 192 — implication not pursued — correct (resolved by the ink).** "sans torsion" is an insertion after "T" on the next line ("opère trivialemᵗ sur T sans torsion"), so it qualifies T, not the extension. Torsion-freeness of T ≃ ℤ is what makes T → T⊗ℚ injective in the coefficient sequence; nothing is asserted about torsion in the extension at this point.

**R06 — scan 193 — claim without proof — correct.** The step is "OPS" (on peut supposer), not "OBS": replacing Γ° by the kernel of the homomorphism to Tₙ, one may suppose it is zero. The needed implication (zero homomorphism ⇒ trivial action) is the content of the lemme fondamental.

**R07 — scan 193 — claim without proof — correct.** With the inserted word the lemma reads "Tout automorphisme direct extérieur u d'ordre fini n d'un groupe à lacets π, qui fixe une classe de lacets i et est tel que l'extension de ℤ/nℤ par Lᵢ ∈ i définie par u soit triviale, est trivial." The hypothesis "direct" (orientation-preserving) is part of the statement (CSG/IUT agree); the first pass had misread the inserted word as a margin "évident!". The lemma is admitted on scan 196, not proved.

**R08 — scans 193–194 — claim without proof — correct.** The reformulation is headed "Corollaire", not "Lemme": "Tout autom direct d'ordre fini u₀ d'un groupe à lacets π, qui soit direct et qui normalise un sous-groupe à lacets Lᵢ (i.e. qui centralise Lᵢ), est réduit à l'identité." "direct" is inserted twice (above "autom" and as "qui soit direct et"); one insertion may be meant to replace the other. See O1 for why the hypothesis is needed for the parenthesis.

**R09 — scan 194 — claim without proof — correct.** The text says "on est ramené aussitôt au cas où u₀ est tel que u₀ᵖ = id, où p est un nb premier"; the first pass's inserted "(cas ν≥1)" is a misreading of "aussitôt". The reduction is sound (own check): if u₀ ≠ id has finite order m and p | m, then u₀^{m/p} has order p, is still direct and still centralises Lᵢ, so excluding non-trivial elements with uᵖ = id excludes u₀.

**R10 — scan 194, upper-left margin — conjecture — correct.** The NB reads: g = 0 with ν+1 = 1 or 2 is trivial; ν+1 = 3 ((g,ν) = (0,2) abélien!) "n'est pas trivial par contre", nor g = 1, ν+1 = 1 ((g,ν) = (1,0) abélien); "Pourtant le résultat doit être valable aussi dans ce cas". The first pass's "(0,2) doit l'être!" is not in the ink. The conjecture is that the lemma or its corollary also holds in the two abelian cases.

**R11 — scan 194, cancelled block — claim without proof (cancelled) — keep.** The cancelled lines describe the lifts of the outer action to a true action through the fixed points of Γ in U and choose a fixed point a with π = π₁(U,a). They are replaced by the margin "… sᵢ de S correspondant à un pt fixe de Γ op. sur U" and by scan 195.

**R12 — scan 195 — claim without proof — keep.** "on sait par ailleurs dans le cas géom. et op. fidèle qu'elle n'est pas triviale !": for a faithful geometric action fixing the puncture sᵢ, the extension of Γ by Lᵢ ≃ T is non-trivial. It is cited as known, and it must be the same extension as the one assumed trivial in the lemma.

**R13 — scan 195 — claim without proof — correct.** The ink has no "Nielsen": it says "Or sauf erreur ce résultat est (bien) connu (m̄ pour les groupes résolubles …)", with the margin "comme th. d'exist. de pts fixes d'un groupe … de Teichmüller". So the realizability of finite cyclic outer actions, even of solvable ones, is cited as known without a name; the reduction to prime order ("il suffit m̄ de le savoir pour un groupe cyclique d'ordre premier") is stated, not argued. For the literature behind it, see O3.

**R14 — scan 195 — question (doubt) — correct.** "J'ai seulement un doute s'il est démontré dans le cas général d'un (g,ν), ou seulement pour g ≥ 2, ν = 0": the interlinear "g ≥ 2" after "(g,ν)" is struck, so the alternatives are the general case and closed surfaces of genus at least 2. The first pass's reading kept "g ≥ 2" in both alternatives.

**R15 — scan 196 — conjecture — keep.** "(pour g ≥ 2 tout au moins) on s'en tire par dévissage pour le cas ν quelconque" announces a reduction from ν = 0 to arbitrary ν that is not carried out here.

**R16 — scan 196 — implication not pursued — keep, word corrected.** "le cas g = 0, 1 demanderait aussi un traitement à part" ("aussi", not "encore"). Scan 197 says only that the abelian cases (0,2) and (1,0) have essentially been treated directly; the other low-genus cases remain open in this extract.

**R17 — scan 196 — dependency marker — keep.** "préfère pour l'instant admettre le “lemme fondamental”": a), b) and everything after them on these pages depend on the admitted lemma.

**R18 — scan 196 — claim without proof (conditional) — correct.** b) reads "pour tte classe de [π-conjugaison] de tels scindages partiels sur Γ′ ⊂ Γ°, on a un iso. can. correspondant Γ′ ≃ Tₙ (= T/nT), où n = card Γ′" ("tte classe", singular, and "correspondant", both missed by the first pass). The margin (CSG/IUT footnote 62) restates it: "on a établi l'existence d'une applic. can. … des éléments d'ordre fini de Aut_lac(π) dans T⊗ℚ/T, satisfaisant les conditions examinées précédemment"; the first pass's "identification … tangentielles" is not in the ink.

**R19 — scan 197 — claim without proof — keep, reading corrected.** The restriction to the anabelian case is dropped as soon as π ≠ 0, "ce qui inclut les cas abéliens g = 0, ν = 2 et g = 1, ν = 0" ("abéliens" is an insertion, not a margin note), which are said to have essentially been treated directly, extensions of Γ by π ≃ ℤ or ℤ² being always realizable. No construction is given here.

**R20 — scan 197 — claim (replacement hypothesis) — correct.** The inserted phrase is "une extension produit", not "une extension scindée": in the abelian cases faithfulness is replaced by "l'extension n'est une extension produit sur (or sous) aucun sous-groupe Γ′ ⊂ Γ° avec Γ′ ≠ 1". This is a different, weaker condition than non-splitting; see O5.

**R21 — scan 197 — question — correct.** c) reads "Si Γ est un sous-groupe fini de Aut_lac(π) i.e. un grpe fini opérant fidèlᵗ sur π, a-t-on π^Γ = {1} ?" with the label "c)" and without the "d'ordre n" of the first pass (those words belong to the margin's "d'ordre 2"). The margin reduces it: "OPS Γ = Γ° donc Γ engendré par un autom. direct u ou Γ engendré par un anti-autom. d'ordre 2" (see O6). Γ = 1 must be excluded (R33).

**R22 — scan 198 — question with warning — correct.** d) asks whether Γ′, Γ″ with Γ′ ∩ Γ″ ≠ (1) are "contenus dans le π-conjugué d'un ss-gpe fini Γ‴ de E", restated as "tt sous-groupe section ≠ 1 est contenu dans un unique sous-groupe section maximal, mod. π-conjugaison" ("section", not "fini"; a section is a subgroup meeting π trivially, i.e. a partial splitting). The margin NB is "Deviendrait faux en se plaçant dans le groupe Aut_lac(π) […]", not "Deuxièmement d) faux": the warning concerns the analogue in Aut_lac(π), not d) itself (see O7). The witnesses continue after scan 200 with "Démontrons d)", outside this package.

**R23 — scan 198 — question and conditional claims — correct.** e) asks whether the set of π-conjugacy classes of lifts of Γ′ to E is finite. The inserted paragraph says "Dans le cas c), OPS Γ cyclique d'ordre premier et c'est OK s'il est acquis qu'une op. extérieure d'un tel groupe sur un π_{g,ν} est réalisable" (conditional; the first pass read "c'est là où il est acquis", and the item letter, c) or e), is not fully settled). The margin adds "De m̄ e) est établi si on admet que les op. ext. de groupes cycliques sur un π ≃ π_{g,ν} sont réalisables": both c) and e) are reduced to the realizability of cyclic outer actions, not established.

**R24 — scan 198 — claim without proof — correct.** The Théorème (for finite Γ₀ ≠ 1 in A = Aut_lac(π)⁰ the normaliser equals the centraliser Z, whose finite-order elements form a cyclic group, the largest finite subgroup containing Γ₀, central in Z) is marked "Ultra fort!", and an oblique stroke crosses its first lines. With the cancelled proof on 199–200 and the warnings "pas vrai!" and "faux!", it reads as an abandoned attempt; neither witness contains it.

**R25 — scan 199 — claim without proof — keep, reading corrected.** The claim that the finite-order elements of Z form a cyclic group, maximal among finite subgroups containing Γ₀ and central in Z, is not proved; the inserted name of that group is read "F" (not Γ). The page is cancelled by an oblique stroke of uncertain scope.

**R26 — scan 199 — claim without proof — keep, with a reading doubt.** The NB has "et normalise|centralise Γ₀": the ink is closer to "centralise", the sense needs "normalise". With "normalise" it says an orientation-reversing g normalising Γ₀ induces σ ↦ σ⁻¹ on Γ₀ (via the canonical Γ₀ ≃ T_{n₀} and the action −1 on T); with "centralise" the same argument would force Γ₀ to have exponent at most 2.

**R27 — scan 199 — claim without proof — keep.** Putting u and Γ₀ in a finite commutative, hence cyclic, subgroup Γ′ uses "un ss-groupe fini de A est cyclique" (from the admitted lemma), and the next step needs a realization of Γ′ extending the chosen realization of Γ₀; that is exactly where scan 200 fails.

**R28 — scan 200 — claim without proof — keep.** "le relèvement de l'action extérieure de Γ₀ en une action est décrit par un unique pt a ∈ U" is asserted; the correspondence between lifts, fixed points and their conjugacy classes is not proved here.

**R29 — scan 200 — claim explicitly rejected — keep.** "de façon unique" (double underline) carries the margin "pas vrai!" (double underline); the rejected step is the uniqueness of the realization of Γ′ extending that of Γ₀ and fixing a.

**R30 — scan 200 — lemma explicitly rejected — correct.** The hypotheses read: u₀ of finite order n₀ ≠ 1 of an orientable surface (the struck "supposée X^{u₀} ≠ ∅", i.e. u₀ has a fixed point, replaced by "U = X−S, X (compacte, …, et) laissant fixe un pt a ∈ U"), d ∈ ℕ*; if u of (X,S) satisfies u^d = u₀ and u(a) = a, then u is determined by its action on π₁(U,a), and ⟨u⟩ is determined "(il est d'ordre nd)". The margin says "faux!".

**R31 — scans 192–193 — own idea (first pass) — keep.** The model E_χ = {(q,γ) : q mod T = χ(γ)} is the pull-back extension, and for γ ∈ ker χ the element (0,γ) is a non-trivial torsion element. This correctly isolates what must be excluded (torsion in Eᵢ° over ker χ) to make χ injective.

**R32 — scans 193–194 — own idea (first pass) — keep.** A strategy, not a proof; it should now start from the corrected statement (a "Corollaire" with the hypothesis "direct").

**R33 — scans 197–198 — own idea (first pass) — keep.** For Γ = 1, π^Γ = π, so c) needs Γ ≠ 1, which the margin's reduction to a cyclic Γ generated by a non-trivial element implicitly assumes.

**R34 — scans 198–199 — own idea (first pass) — keep.** ℚ/ℤ shows that "every finite subgroup is cyclic" does not give a largest finite subgroup; this tests the inference in R25, not the specific claim.

**R35 — scans 198–200 — own idea (first pass) — keep.** Separating points, orbits and conjugacy classes of lifts is the right bookkeeping for e) and for R28.

**R36 — scan 199 — own idea (first pass) — keep.** The naturality square for Γ₀ ≃ T_{n₀} is also the way to settle the normalise/centralise reading of R26: it gives inversion exactly for orientation-reversing normalising elements.

**R37 — scan 200 — own idea (first pass) — keep, with a restriction.** The algebra is right: if h commutes with u₀ and is isotopic to the identity relative to a, then v = huh⁻¹ satisfies v^d = u₀ and induces the same automorphism of π₁(U,a). Such an h exists only among homeomorphisms; see O9 for the conformal case.

**R38 — scans 195–200 — own idea (first pass) — keep.** Existence of a realization, extension of a given realization to a larger group, and uniqueness of that extension are separate obligations; the "pas vrai!" and "faux!" both sit at the uniqueness step.

**R39 — scan 200 — own idea (first pass) — keep, reading settled.** The insertion reads "(il est d'ordre nd)", with no subscript, and n is not defined in the lemma (only n₀). With n = n₀ the claim fails in general: if u has order m and u^d = u₀ has order n₀, then m = n₀·gcd(m,d), which equals n₀d only when d | m (m = 3, d = 2 gives order 3, not 6).

## B. Own notes (Claude, second pass)

**O1 — scans 193–194 — own idea.** The inserted "direct" is what makes the Corollaire's "(i.e. qui centralise Lᵢ)" right. An automorphism normalising Lᵢ ≃ ℤ acts on it by ±1. An orientation-preserving one that fixes the class i preserves the orientation of the loop and so centralises Lᵢ, while a reflection fixing the puncture normalises Lᵢ and inverts its generator. Without "direct" the equivalence "normalise ⇔ centralise" fails.

**O2 — scan 195 — claim checked (own, against the corrected text).** The removal of "Nielsen" matters for attribution: the ink cites no author. The text claims only that the result is known "sauf erreur", even for solvable groups, as a fixed-point theorem on Teichmüller space.

**O3 — scan 195 — own note (literature lead, from memory, to be checked against the corpus).** The claim matches the state of the Nielsen realization problem around 1981: Nielsen (Acta Math. 75, 1943) for finite cyclic groups, Fenchel (1948 and 1950) for finite solvable groups ("même pour les groupes résolubles"). The general finite case was proved by Kerckhoff (Ann. of Math. 117, 1983) through fixed points of the action on Teichmüller space, which is the margin's formulation. Whether these statements cover punctured surfaces and peripheral data, as needed for type (g,ν+1), is exactly Grothendieck's doubt in R14.

**O4 — scan 196 — implication not pursued (Grothendieck's, made explicit).** Combined with the margin, b) amounts to a map from the finite-order elements of Aut_lac(π) to T⊗ℚ/T. It is defined conditionally on the lemma, and its "conditions examinées précédemment" refer to pages before this package.

**O5 — scan 197 — own idea.** "Produit" is the right replacement for faithfulness in the abelian cases. Over Γ′ the extension is a product exactly when Γ′ acts trivially on π (here inner automorphisms are trivial) and the extension splits. So "never a product over Γ′ ≠ 1" still allows a Γ′ acting trivially with a non-split extension, which is the rotation about a puncture in the geometric case. With "scindée" the condition would instead exclude split extensions, which faithful semidirect products are, and the replacement would be wrong.

**O6 — scans 197–198 — own idea (check).** The reductions for c) are valid: π^Γ ⊂ π^{Γ′} for Γ′ ⊂ Γ, so one may pass to any non-trivial subgroup, first a cyclic subgroup of Γ° if Γ° ≠ 1 (otherwise Γ has order 2, generated by an orientation-reversing element, as the margin says), then one of prime order ("OPS Γ cyclique d'ordre premier"). This needs Γ ≠ 1 (R33).

**O7 — scan 198 — own idea (a test of the NB, to be written out).** In genus 2 the hyperelliptic involution ι is central in the mapping class group, so for a finite subgroup G ∋ ι and any mapping class h, the subgroups G and hGh⁻¹ meet in at least ⟨ι⟩. By Kerckhoff's fixed-point theorem a finite subgroup containing both would fix a point of Fix(G) ∩ h·Fix(G) in Teichmüller space. For G with an isolated fixed point p (e.g. the cyclic group of order 10 generated by ι and an element of order 5 of y² = x⁵ − 1) and h with h·p ≠ p, these sets are disjoint, so the analogue of d) fails in Aut_lac(π_{2,0}), consistent with the NB. The details (choice of G and h) still have to be checked.

**O8 — scans 198–200 — own note (status).** The Théorème on 198, its cancelled proof on 199–200, the "pas vrai!" and the "faux!" form one abandoned unit. A downstream edition should not cite the Théorème's statement as Grothendieck's result without that status; the witnesses omit the whole unit.

**O9 — scan 200 — own idea.** For conformal automorphisms of a hyperbolic Riemann surface of finite type, an automorphism fixing a and acting trivially on π₁(U,a) is isotopic to the identity, hence the identity (Hurwitz). So the first assertion of the lemma (u determined by its action on π₁(U,a)) holds there, and the construction of R37 needs homeomorphisms. The "faux!" therefore fits the topological reading and, independently, the order claim "nd" (R39).
