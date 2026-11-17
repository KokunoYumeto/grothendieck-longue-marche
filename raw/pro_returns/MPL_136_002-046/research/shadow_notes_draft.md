# Research notes draft: shadows and binomial rigidity, scans 020–034

## Scope and status

These notes use the frozen page files only; this ancillary reader did not inspect images or change transcription. Locations called “TeX lines” refer to the individual frozen page file, not physical manuscript lines. The supplied context README, `notes/RESULTS_STATE.md`, Hua README, the relevant sections of Hua's modernised cote136, and the cited same-cote research entries were read before drafting.

The supplied results register groups **g1031, g1034, g1035, g1041, and g1080** under **gap g1048**; these are earlier runs' claims, not referee certifications. Its summary does not separately identify which of g1034/g1035 names which negligible-class obstruction, so this draft cites the pair where appropriate rather than inventing that allocation. The underlying supporting memo `research/derived_functor_checks.md` cited by the previous package is not supplied here. Hua's modernised reading and Lean verification statements are credited to Michel Hua's project; no Lean source or certificate was inspected in this task.

### Merge priorities

- **SH12:** scan026 explicitly calls the literal elementwise-negligible class thick; this is an earlier, direct locus for the obstruction already recorded under g1034–g1035.
- **SH14:** scan027 restricts the unit isomorphism to nonnegative degrees; Hua's full modernised reading retains that qualification, whereas the supplied findings-register summary drops it.
- **SH18:** Hua's footnote equating two differently indexed coefficients is itself mathematically incorrect under the definition on scan020; it must not justify changing the frozen manuscript.
- **SH11:** the finite-truncation Hom display on scan026 has an adjunction-variance problem; the later adjunction ladder distinguishes the inclusion from the right-adjoint section functor.
- **SH15:** the Ext corollary is announced before its proof; the later context claims a repair using g1041, and the finite proof here alone does not establish it.

## Per-item notes

### SH01 — The no-carry argument is written out, with local reading questions

**Source:** cote136, scans020–021, manuscript pp19–20; scan020 TeX lines6–69 and scan021 lines3–5. **Kind:** unpursued implication. **Exact cue:** “en étudiant le développement, dans $\mathbb F_p[X,Y]$, de $(X+Y)^{i+j}$”.

The pages write out the digitwise congruence for $c_{ij}=(i+j)!/(i!j!)$ and its no-carry criterion by treating both the low-digit no-carry and carry cases, rather than merely citing them. The intended arithmetic route underlies the later prime-local argument, but local notation anomalies and disagreements with Hua's commentary remain recorded in SH25; this is not a verification of every formula literally as written. The additional historical evidence is Grothendieck's manuscript argument, rather than a new proof of the coefficient-uniform rigidity already claimed in the context.

**Context and relation:** `hua_project/136.modern.tex`, “Coefficients binomiaux modulo $p$ (pages19 à22),” lines580–629, corresponding to scans020–023: restates this argument, credits Lucas/Kummer in its editorial discussion, and says its Lean check does **not** verify this particular lemma or digit-induction proof. `same_cote_136/MPL_136_235-281_notes.md`, N21, scans275/277/279: this package supplies the earlier manuscript arithmetic behind that note's prime-local method. **Results-state:** g1031, as summarized by gapg1048; Hua finding **136-shadow-full-faithfulness**. **Search:** SH01.

### SH02 — The sparse local lemma does not make all its entries equal

**Source:** cote136, scan021, manuscript p20, TeX lines65–69; conclusion on scan022 line3. **Kind:** unpursued implication. **Exact cue:** “mais \uline{pas} néc. $=x_4$”.

The margin gives the explicit limitation $p=2$, $N=2$, $e=2$: the sparse relations imply $x_2=x_3=x_6$, but do not force equality with $x_4$. Thus Lemme2 concludes only $x_N=x_{N+1}$; it must not be strengthened to constancy on its whole finite indexing set. The global theorem on scan023 adds the full family of pairwise binomial relations and then applies the sparse lemma successively.

**Context and relation:** `hua_project/136.modern.tex`, “Coefficients binomiaux modulo $p$,” lines607–629, scans021–023: acknowledges the same limitation but does not retain this numerical example; these pages add the explicit counterexample parameters. `same_cote_136/MPL_136_235-281_notes.md`, N21, scans275/277/279: concerns the stronger all-pairs hypothesis and is not contradicted. **Results-state:** g1031 / gapg1048; Hua **136-shadow-full-faithfulness**. **Search:** SH02.

### SH03 — The tail-rigidity theorem has a complete stated prime-local route

**Source:** cote136, scans022–023, manuscript pp21–22; scan022 lines27–61 and scan023 lines3–16. **Kind:** unpursued implication. **Exact cues:** “cqfd. Ouf !”; “Quitte à localiser en tous les nbs premiers $p$”.

The induction replaces $N$ by $(N+1)/p-1$, retains the required bound on $e$, and proves the adjacent equality needed for Théorème1. The theorem is stated for an arbitrary abelian group, with no finite-generation, flatness, or torsion-freeness hypothesis. These pages therefore locate Grothendieck's own proof of the result credited to the shadow programme; “Ouf !” marks the end of the proof, not an unresolved verification flag.

**Context and relation:** `same_cote_136/MPL_136_235-281_notes.md`, N21, scans275/277/279: already supplies a different prime-local proof, using a common index $p^r-1$; the present pages add manuscript provenance and a distinct digit-induction route. `hua_project/136.modern.tex`, “Coefficients binomiaux modulo $p$,” lines607–629, scans021–023: distinguishes its claimed Lean proof of `binomial_constant` from this manuscript proof. **Results-state:** g1031 / gapg1048; Hua **136-shadow-full-faithfulness**. **Search:** SH03.

### SH04 — Full faithfulness uses rigidity in the group of maps

**Source:** cote136, scans024–025, manuscript pp23–24; scan024 lines4–42 and scan025 lines2–14. **Kind:** unpursued implication. **Exact cue:** “le th. nous permet de conclure que tous les $u_i$ sont égaux”.

The proof of full faithfulness encodes a graded $S$-linear map between shadows by a family of $k$-linear maps $u_i$ and applies the preceding abelian-group theorem to their differences. Consequently the result reconstructs morphisms functorially, rather than merely recovering isomorphism classes or copying the same underlying module in each degree. This is direct manuscript support for Hua's credited finding and for the already recorded finite-tail result g1031; no new independent proof is claimed here.

**Context and relation:** `hua_project/136.modern.tex`, “Les foncteurs « ombres » $\omega_N$ (pages22 à25),” lines630–648, scans023–025: same argument, with a carefully limited claim that `hom_family_constant`, rather than the entire graded-category statement, was checked in Lean. `same_cote_136/MPL_136_235-281_notes.md`, N19–N22, scans252/265/275/277/279: these pages supply the earlier explicit proof where the later pages formulate conditions or assume them. **Results-state:** g1031 / gapg1048; Hua **136-shadow-full-faithfulness**. **Search:** SH04.

### SH05 — “Bijectivité?” is answered on the same page

**Source:** cote136, scan024, manuscript p23, TeX lines23–35. **Kind:** self-flagged: a step he himself marks as unverified, resolved locally. **Exact cue:** “L'injectivité de $\varphi$ est claire. Bijectivité?”

The question concerns reconstruction of an element from a compatible family in the product of the shadow's components. The page immediately writes the binomial relations for its coefficients and concludes that they are all equal by Théorème1, ending “cqfd.” The research register should retain the question mark but mark it as answered here, rather than counting it as a remaining gap.

**Context and relation:** `hua_project/136.modern.tex`, “Les foncteurs « ombres » $\omega_N$,” lines636–653, scans024–025: states the resulting identification without preserving the local question-and-answer sequence; the present pages add that sequence. `same_cote_136/MPL_136_235-281_notes.md`, N21–N22, scans252/275/277/279: compatible with the already claimed finite recovery. **Results-state:** g1031 / gapg1048; Hua **136-shadow-full-faithfulness**. **Search:** SH05.

### SH06 — The tensor base on scan023 is a reading/typing question

**Source:** cote136, scan023, manuscript p22, TeX lines18–24. **Kind:** reading question. **Exact cue:** `$\omega_N(M)=M\otimes_S S^{+(N)}$`.

The frozen page declares $M$ only a $k$-module but writes the tensor product over $S$, while its displayed direct-sum description and the later $omega_0(M)=M\otimes_kS$ on scan025 point to a tensor product over $k$. Hua's modernised reading explicitly records this discrepancy and replaces the base in its interpretation. The diplomatic text must remain unchanged; the context supports an editorial typing question, not an unmarked correction.

**Context and relation:** `hua_project/136.modern.tex`, “Les foncteurs « ombres » $\omega_N$,” lines632–634, scan023: exact same discrepancy, explicitly footnoted. `notes/RESULTS_STATE.md`, entry **MPL_150_085-099+151_001-031 H05**, names scan023 among its reading questions, but the underlying H05 text is not supplied and cannot be assumed to ask this exact question. **Results-state:** H05; g1031 / gapg1048. **Search:** SH06.

### SH07 — The one-generator description of the tail ideal is withdrawn

**Source:** cote136, scan023, manuscript p22, TeX lines18–20. **Kind:** withdrawn in the same text. **Exact deleted cue:** “engendré par $\unsure{T^{(N)}}$”.

The retained definition is the entire graded tail $S^{+(N)}=\sum_{i\geq N}kT^{(i)}$, following deletion of the proposed one-generator description. That distinction matters: our check is that in $\Gamma_{\mathbb F_2}(T)$ the PD ideal generated by $T^{(3)}$ cannot contain $T^{(4)}$, since its only possible degree4 contribution is $T^{(1)}T^{(3)}=4T^{(4)}=0$, while higher divided powers have degree at least6. This example is an ancillary explanation of the deleted phrase, not a claimed new theorem or an alteration of its doubtful reading.

**Own-check confidence:** high for the stated homogeneous-degree calculation; the deleted generator's reading retains the frozen doubt. **Context and relation:** `hua_project/136.modern.tex`, “Les foncteurs « ombres » $\omega_N$,” lines632–634, scan023: keeps the direct-sum definition but does not discuss the deletion. `same_cote_136/MPL_136_235-281_notes.md`, N25, scan256 and uses on257–267: its augmentation-ideal example concerns a related failure of ordinary generation in characteristic $p$, not this exact PD-generator claim. **Results-state:** g1031 and the negligible-class issues g1034–g1035, as summarized by gapg1048. **Search:** SH07.

### SH08 — The recovery adjoint is an explicit product equalizer

**Source:** cote136, scan025, manuscript p24, TeX lines16–32. **Kind:** unpursued implication. **Exact cue:** “Le foncteur $\omega_N$ admet un adjoint à droite $\pi_N$”.

The page gives $\pi_N$ as compatible families in $\prod_{i\geq N}\mathcal M_i$, with relations $x_iT^{(j)}=c_{ij}x_{i+j}$, and identifies full faithfulness with invertibility of $M\to\pi_N\omega_N(M)$. This specifies a coefficient-module recovery functor, distinct from the graded right adjoint $\varphi_N$ to truncation that appears on scan027. It supplies a concrete categorical meaning for recovering a module from its shadow, while proving neither a derived recovery statement nor exactness of every such product-equalizer functor.

**Context and relation:** `hua_project/136.modern.tex`, “Les foncteurs « ombres » $\omega_N$,” lines650–653, scan025: restates the formula. `same_cote_136/MPL_136_235-281_notes.md`, N17/N19, scans244/248/250/252: later truncation-adjoint calculations elaborate the different graded recovery functor. **Results-state:** g1031 / gapg1048; no new solution of the broader bare-derivator entries is implied. **Search:** SH08.

### SH09 — Full faithfulness of shadows does not make truncation fully faithful

**Source:** cote136, scan026, manuscript p25, TeX line2, following scan025 lines34–36. **Kind:** unpursued implication. **Exact cue:** “les foncteurs $\tau_N$ ne sont pas pl. fidèles bien sûr”.

The text expressly distinguishes full faithfulness on induced coefficient objects from full faithfulness on the whole category of virtual shadows. For $N\geq1$, a module concentrated in degree $N-1$ is lost by $\tau_N$, which explains the distinction already asserted by the author. This prevents the finite-tail theorem from being silently generalized to arbitrary graded modules.

**Context and relation:** `hua_project/136.modern.tex`, “Les foncteurs « ombres » $\omega_N$,” lines655–658, scans025–026: same explicit distinction. `same_cote_136/MPL_136_235-281_notes.md`, N19/N22, scans252/265/275: later full-faithfulness statements concern the induced coefficient subcategory, not all graded modules. **Results-state:** g1031 / gapg1048. **Search:** SH09.

### SH10 — Nonnegative grading is initially an explicit question

**Source:** cote136, scan026, manuscript p25, TeX line4. **Kind:** self-flagged: a step he himself marks as unverified. **Exact cue:** `[à degrés $\geq0$?]`.

The bracketed question occurs in the definition of virtual shadows, so the ambient grading category is not fully settled at this point. Scan027 then states its recovery isomorphism only in nonnegative degrees, a qualification that resolves the scope of that theorem without proving that every earlier categorical assertion was intended in the same ambient category. This is a substantive hypothesis question, not a decorative question mark.

**Context and relation:** `same_cote_136/MPL_136_235-281_notes.md`, N22, scan252 and275; N32, scans265/275–277; N71, scans256–273: all restrict their positive reconstruction or repair to nonnegative modules. `hua_project/136.modern.tex`, “Le théorème sur $M\otimes_kS$,” lines674–681, scan027: preserves the nonnegative qualification. **Results-state:** g1031, g1041, g1080, as summarized by gapg1048. **Search:** SH10.

### SH11 — The displayed adjunction on scan026 has a variance problem

**Source:** cote136, scan026, manuscript p25, TeX lines7–14. **Kind:** reading question. **Exact cue:** “le foncteur … pass. au quotient admet un adjoint à droite”.

The issue is not whether finite truncation has a right adjoint, but whether the displayed Hom identification and the inclusion $\tau_N\mathcal M\hookrightarrow\mathcal M$ identify the correct member of the adjunction chain. With $k=\mathbb Q$, $S\simeq\mathbb Q[t]$, $N=1$, and both named modules equal to $S$, the written comparison has left side $\operatorname{Hom}_{\mathrm{gr}}(S,tS)=0$ and right side $\operatorname{Hom}_{\mathrm{gr}}(tS,tS)=\mathbb Q$, independently of the frozen first-argument letter doubt. Later context distinguishes the inclusion $i_N$ from the section functor $\varphi_N$ through $i_N\dashv\tau_N\dashv\varphi_N$, so the earlier display needs a source-level variance question rather than silent use as an adjunction formula.

**Own-check confidence:** high for the elementary graded Hom calculation; the source-level diagnosis remains a reading question because the manuscript formula is frozen. **Context and relation:** `same_cote_136/MPL_136_235-281_notes.md`, N17, scans244/246/248/250: the later adjunction ladder differs from the apparent earlier identification. `hua_project/136.modern.tex`, “Les catégories $\mathcal M_N$ et les modules négligeables,” subsection “Adjoints de l'inclusion,” lines1782–1809, scans244–252; and “Modules gradués : la mise au propre,” lines1961–1978, scans287–299: distinguish the functors explicitly. **Results-state:** gapg1048, with g1031 not refuted by this display problem. **Search:** SH11.

### SH12 — Scan026 already asserts the literal negligible class is thick

**Source:** cote136, scan026, manuscript p25, TeX line16. **Kind:** unproved claim, contradicted by a counterexample already recorded in the supplied research context. **Exact cues:** “$\varinjlim$ \inserted{filtr.} d'ombres $N$-négligeables”; “C'est encore une sous-catégorie épaisse”.

The page explicitly combines the elementwise condition that a sufficiently high tail annihilate each homogeneous element with the claim that this class is thick. The supplied N25 counterexample over $\Gamma_{\mathbb F_p}(T)$, using $0\to I/I^2\to S/I^2\to\mathbb F_p\to0$, already refutes extension-closure of that literal class; these pages add an earlier direct assertion, not a new counterexample. Fixed-$N$ bounded modules, uniformly bounded modules, and the elementwise class must therefore remain distinct in the notes, and the class cannot simply be replaced in the transcription by the later repaired localizing Serre closure.

**Context and relation:** `same_cote_136/MPL_136_235-281_notes.md`, N23–N26, scans254/256 and uses257–267: identifies the same distinctions and the two different obstructions. `hua_project/136.modern.tex`, “Les foncteurs « ombres » $\omega_N$,” lines660–669, scan026, and “Modules négligeables,” lines1836–1860, scans254–259: repeats the thick-class/localization interpretation without supplying this counterexample. **Results-state:** g1034–g1035 and gapg1048; statuses are the supplied runs' claims. **Search:** SH12.

### SH13 — “Ou encore” at infinity needs a specified localization

**Source:** cote136, scan026 final words and scan027, manuscript pp25–26, TeX lines11–17. **Kind:** unproved claim. **Exact cue:** “ou encore” before `$M\otimes_kS\in\operatorname{Im\,ess}\varphi_{0,\infty}$`.

The finite essential-image conditions are presented as equivalent to an infinite one, although the previous page's sentence defining the localized category breaks off at “et le localisé est”. The weighted arithmetic proof on scans027–034 establishes finite-tail extension and does not by itself supply a valid quotient, its section functor, or the asserted infinite equivalence. The repaired derived reconstruction already claimed under g1080 gives a different, explicitly specified setting, so it should be cited conditionally rather than read backward into this unfinished definition.

**Context and relation:** `same_cote_136/MPL_136_235-281_notes.md`, N27/N28/N34, scans257/259/265/267, and N71, scans256–273: later attempts and a proposed repair of exactly this passage. `hua_project/136.modern.tex`, “Modules négligeables,” lines1836–1860, scans254–259: presents the later infinite construction; the present locus adds its early incomplete formulation. **Results-state:** g1034–g1035, g1080, gapg1048. **Search:** SH13.

### SH14 — The stronger unit is explicitly restricted to nonnegative degrees

**Source:** cote136, scan027, manuscript p26, TeX lines7–29. **Kind:** reading question / scope reconciliation. **Exact cue:** “L'hom précédent est un isom en degrés $\geq0$”.

This supports the nonnegative unit $M\otimes_kS\simeq\varphi_{0N}\tau_N(M\otimes_kS)$, not an unrestricted all-$\mathbb Z$-graded unit. The supplied findings-register summary of Hua's **136-shadow-full-faithfulness** suppresses that qualifier, but Hua's full modernised section retains it correctly. N22 of the later package already records the characteristic-zero Laurent-polynomial obstruction to the unrestricted interpretation, so the present contribution is the exact early manuscript qualification and correction of the summary's scope.

**Context and relation:** `notes/RESULTS_STATE.md`, **136-shadow-full-faithfulness**, line467, versus `hua_project/136.modern.tex`, “Le théorème sur $M\otimes_kS$ (pages26 à34),” lines674–681, scan027: summary overstates; full reading agrees. `same_cote_136/MPL_136_235-281_notes.md`, N22, scans252/275: already gives the nonnegative theorem and the negative-degree warning. **Results-state:** g1031 / gapg1048; Hua's finding is credited to his project. **Search:** SH14.

### SH15 — The Ext corollary is announced here, with no proof in this range

**Source:** cote136, scan027, manuscript p26, TeX lines31–35. **Kind:** unproved claim. **Exact cue:** `$\operatorname{Ext}^n(\tau_{N-i}(S)[-i],M\otimes_kS)=0\quad\text{si }n>0$`.

The corollary is stated for $i\geq0$, but the following proof handles the ordinary homogeneous-Hom extension theorem and does not supply the higher-Ext argument. Hua's later reconstruction section explicitly identifies a derived-composition gap in the attempted proof on scans263–265. The supplied later notes N32–N33 claim a repair for finite truncation in the nonnegative module category using the additional exact left adjoint summarized as g1041; this existing result should be cited, not re-derived or promoted to an unrestricted infinite statement.

**Context and relation:** `hua_project/136.modern.tex`, “Le théorème sur $M\otimes_kS$,” lines741–744, scan027, and “Reconstruire un complexe à partir de son ombre,” lines1870–1894, scans263–265: explicit deferral and qualification. `same_cote_136/MPL_136_235-281_notes.md`, N29–N34, scans261–267: separates the formal gap from the claimed concrete repair. **Results-state:** g1041 and gapg1048; g1080 is a further repaired-setting claim, not a proof of the literal infinite category. **Search:** SH15.

### SH16 — The weighted family theorem is stronger than degree-zero rigidity

**Source:** cote136, scans027–034, manuscript pp26–33; scan027 lines24–43 and scan028 lines2–6 state it. **Kind:** unpursued implication. **Exact cues:** “Ce théorème équivaut à l'énoncé suivant, où $k$ ne figure plus”; “il existe un unique $\xi\in M$”.

The families satisfy $c_{\ell,k}\xi_k=c_{\ell,k-i}\xi_{k+\ell}$, and the conclusion reconstructs them from one coefficient with the weight factors $\binom{k}{i}$. This is the arithmetic needed to recover lower nonnegative degrees of $M\otimes_kS$, beyond the degree-zero constancy theorem, and explains why the full-faithfulness statement is followed by a second proof. The original statement retains $0\leq i\leq N$; Hua's claim of a more general Lean theorem is his project's editorial result, not a broader claim made on these pages.

**Context and relation:** `same_cote_136/MPL_136_235-281_notes.md`, N22, scans252/275: already states the weighted calculation; this package adds the manuscript theorem and its extended proof. `hua_project/136.modern.tex`, “Le théorème sur $M\otimes_kS$,” lines688–739, scans027–034: reproduces the statement and distinguishes its claimed `binomial_shadow_existsUnique` proof from the manuscript's proof. **Results-state:** g1031 / gapg1048; Hua **136-shadow-full-faithfulness**. **Search:** SH16.

### SH17 — Bézout reconstruction makes the local-to-global passage constructive

**Source:** cote136, scans028–029, manuscript pp27–28; scan028 lines8–21 and scan029 lines4–16. **Kind:** unpursued implication. **Exact cue:** “premiers dans leur ensemble”.

Subject to the coefficient-index reading question SH18, the argument chooses finitely many high-index coefficients with an integral Bézout combination equal to1, uses that combination to define the global $\xi$, and checks the defining relations in every prime localization. Scan029 provides arbitrarily large unit coefficients by taking $k=i+p^\varepsilon$ with $p^\varepsilon>i$. The new contribution to the earlier notes is that this finite reconstruction mechanism is explicitly present in the manuscript, rather than an added finiteness hypothesis on $M$.

**Context and relation:** `same_cote_136/MPL_136_235-281_notes.md`, N22, scans252/275: already uses the same Bézout method; the pages supply the historical argument. `hua_project/136.modern.tex`, “Le théorème sur $M\otimes_kS$,” lines706–715, scans028–029: same mechanism, with its own claimed `span_choose_eq_top` verification. **Results-state:** g1031 / gapg1048; Hua **136-shadow-full-faithfulness**. **Search:** SH17.

### SH18 — The coefficient alternation is real, and Hua's explanatory equality is false

**Source:** cote136, scan028, manuscript p27, TeX lines4/9/11/19, and scan032, manuscript p31, line20; coefficient definition at scan020 line14 and scan028 line6. **Kind:** reading question. **Exact cues:** `$c_{i,k-i}$` and `$c_{k,k-i}$`.

The frozen text alternates these index patterns, while explicitly defining $c_{a,b}=(a+b)!/(a!b!)$. Hua's footnote says that both are equal to $\binom{k}{i}$, but under that definition $c_{k,k-i}=\binom{2k-i}{k}$ whereas $c_{i,k-i}=\binom{k}{i}$; for $i=1,k=2$ they are3 and2. The context therefore raises a manuscript indexing or reading question and also needs an editorial correction of its own; it cannot authorize replacing either frozen coefficient.

**Own-check confidence:** high for the displayed elementary calculation; no new image reading is claimed. **Context and relation:** `hua_project/136.modern.tex`, “Le théorème sur $M\otimes_kS$,” lines691–693, scans028–032: its footnote notices the alternation but gives an incorrect equality. `same_cote_136/MPL_136_235-281_notes.md`, N22, scans252/275: uses the ordinary binomial formulation consistently and does not resolve the earlier ink. **Results-state:** g1031 / gapg1048; Hua **136-shadow-full-faithfulness** remains a separately qualified theorem claim. **Search:** SH18.

### SH19 — Here $\mathbf Z_p$ explicitly means localization, not completion

**Source:** cote136, scan028, manuscript p27, TeX line8; compare scan021 line66 and scan023 line16. **Kind:** unpursued implication. **Exact cue:** `$\mathbf Z_p\overset{\mathrm{def}}=\mathbf Z_{(p\mathbf Z)}$`.

The manuscript explicitly identifies the notation with the localization of the integers at $p$, characterized by invertibility of integers prime to $p$. Its reconstruction arguments therefore impose no $p$-adic completeness or separatedness on the arbitrary coefficient group. Reading this symbol as the completed $p$-adic integers would introduce a hypothesis not present in the text.

**Context and relation:** `hua_project/136.modern.tex`, “Coefficients binomiaux modulo $p$,” lines607–629, scans021–023, and “Le théorème sur $M\otimes_kS$,” lines710–718, scans028–029: modernises the same ring as $\mathbb Z_{(p)}$. `same_cote_136/MPL_136_235-281_notes.md`, N21–N22, scans252/275/277/279: uses prime localization, so agrees with the explicit definition. **Results-state:** g1031 / gapg1048. **Search:** SH19.

### SH20 — The ratio calculation is revised; the lemma survives

**Source:** cote136, scans030–031, manuscript pp29–30; scan030 lines19–44 and scan031 lines2–6. **Kind:** withdrawn in the same text: calculation, not the lemma. **Exact deleted cue:** “le quotient de (a) et (b)”; **retained cue:** “Donc les deux quantités (a) et (b)”.

A substantial intermediate factorial/divisibility calculation is struck out, after which the retained proof identifies the two rational ratios and uses that one is a quotient of $p$-local units. Scan031 then applies the defining recurrence to transfer vanishing between the two indices. The deletion records a change of proof, not a withdrawal of Lemme1.1 or permission to omit the cancelled calculation from the transcription.

**Context and relation:** `hua_project/136.modern.tex`, “Le théorème sur $M\otimes_kS$,” Lemme1.1, lines720–725, scans030–031: keeps the final ratio argument without its revision history; these pages add the latter. `same_cote_136/MPL_136_235-281_notes.md`, N22, scans252/275: establishes the same weighted recovery by a different presentation and does not require this discarded calculation. **Results-state:** g1031 / gapg1048. **Search:** SH20.

### SH21 — The margin supplies the common high-index shortcut

**Source:** cote136, scans031–032, manuscript pp30–31; scan031 lines47–60 and scan032 lines2–20. **Kind:** unpursued implication. **Exact cue:** “Présentation plus simple”.

The margin replaces the digit-by-digit construction by completing $i+j$ to $p^r-1$, and the next page compares two indices through a common high index of that form. Thus the efficient high-index method used in the supplied later research is already explicitly present in this manuscript's weighted proof. This supports that method's historical attribution without identifying it with the earlier sparse-index proof of Théorème1 or claiming the supplied Lean implementation has been checked here.

**Context and relation:** `same_cote_136/MPL_136_235-281_notes.md`, N21–N22, scans252/275/277/279: same common-index strategy, previously presented as an independent check. `hua_project/136.modern.tex`, “Le théorème sur $M\otimes_kS$,” lines697–707 and726–731, scans031–032: separately describes its claimed formal proof and the manuscript's simplification. **Results-state:** g1031 / gapg1048; Hua **136-shadow-full-faithfulness**. **Search:** SH21.

### SH22 — The zero sign on scan032 conflicts with the unit hypothesis

**Source:** cote136, scan032, manuscript p31, TeX line11; compare scan031 lines16–18 and scan032 line20. **Kind:** reading question. **Exact cue:** `$c_{i,\unsure{k'|\widetilde k}-i}=0$`.

The frozen line says that a second index satisfies the same conditions as the first and then writes equality to zero, whereas the surrounding argument requires the relevant binomial coefficient to be nonzero modulo $p$. Hua's modernisation states the unit condition and thereby suggests a different intended sign, but it cannot settle whether the discrepancy is a manuscript slip or a reading issue. The transcription remains untouched, including its existing index doubt.

**Context and relation:** `hua_project/136.modern.tex`, “Le théorème sur $M\otimes_kS$,” Lemme1, lines726–731, scans031–032: states the unit hypothesis instead of the frozen zero sign. `same_cote_136/MPL_136_235-281_notes.md`, N22, scans252/275: relies on the same unit mechanism but supplies no reading of this earlier line. **Results-state:** g1031 / gapg1048. **Search:** SH22.

### SH23 — The long carry algorithm is abandoned for a completed-sum proof

**Source:** cote136, scans033–034, manuscript pp32–33; scan033 lines7–50 and scan034 lines2–25. **Kind:** withdrawn in the same text: proof attempt, replaced locally. **Exact retained cue:** “par le critère habituel”.

The extended recurrence for carries on scan033 continues in deleted text at the top of scan034. The retained proof then takes $\ell=p^r-1-(i+j)$ and applies the no-carry criterion to both $(i+j)+\ell$ and $i+(j+\ell)$, before isolating the common lemma $\mu+\nu=p^r-1\Rightarrow c_{\mu,\nu}\not\equiv0\pmod p$. This closes the second propagation step of the weighted theorem, so the cancelled carry bookkeeping is not an unresolved proof gap in the retained argument.

**Context and relation:** `hua_project/136.modern.tex`, “Le théorème sur $M\otimes_kS$,” Lemme2 and following paragraph, lines733–739, scans033–034: explicitly notes the cancelled carry proof and the retained replacement. `same_cote_136/MPL_136_235-281_notes.md`, N22, scans252/275: its high-index proof matches the retained mechanism rather than the cancelled recurrence. **Results-state:** g1031 / gapg1048. **Search:** SH23.

### SH24 — A concrete product comparison to test under the repaired quotient

**Source:** cote136, scans025–027, manuscript pp24–26; tail definitions and truncation statements. **Kind:** own idea. **Exact cue:** “Néanmoins ils sont tous pleinement fidèles” (scan026).

To address the still-open multiplicative part of gapg1048, test the natural pairing $\omega_N(M)\otimes_S\omega_{N'}(M')\to\omega_{N+N'}(M\otimes_kM')$ and its derived, coherent replacement in the explicitly repaired quotient. Already for $M=M'=\mathbb Z$ and $N=N'=1$, its degree2 map multiplies by2, so ordinary finite-tail full faithfulness does not make this comparison a degreewise isomorphism. The previously supplied augmentation-ideal obstruction explains why arbitrarily high characteristic-$p$ degrees also matter; whether the derived kernel and cokernel become negligible in the repaired category, compatibly with associativity and divided powers, remains the proposed test rather than a conclusion.

**Confidence:** high for the elementary degree2 obstruction; medium for the proposed research route, because a monoidal structure and its coherences must still be constructed. **Context and relation:** `same_cote_136/MPL_136_235-281_notes.md`, N25 (scan256 and uses257–267), N40 (scan273), N71–N73 (scans237–239/256–273): connects the existing obstruction, repaired linear recovery, and weighted-product discussion without re-deriving them. `hua_project/136.modern.tex`, “Reconstruire un complexe à partir de son ombre,” lines1909–1918, scans271–273: records the additional multiplication claim. **Results-state:** open gapg1048; its settled-note claims g1031/g1034–g1035/g1041/g1080 do not already settle this compatibility. **Search:** SH24.

### SH25 — Local notation anomalies in the opening binomial proof remain unresolved

**Source:** cote136, scan020, manuscript p19, TeX lines38/54/60–69. **Kind:** reading question. **Exact frozen cue:** `\text{Soit }\unsure{w'|w}=p+w'`; **related retained readings:** `$\mathbb F_p[X,Y]$` and `$c_{r,s}$`.

The frozen carry-case line reads `\unsure{w'|w}=p+w'`, whereas the preceding deleted expression is `$w=p+w'$` and the subsequent argument uses `$w'=u+v-p$`; these local readings must be retained as questions, not silently normalized into a blanket verification of the literal proof. Hua's opening footnote additionally reports `$\mathbb F_p[V,Y]$` and `$c_{v,s}$`, but those variants are not independently confirmed by this frozen transcription, which reads `$\mathbb F_p[X,Y]$` and `$c_{r,s}$`. His modernised explanation and the later N21 arithmetic argument support the intended mechanism, but neither resolves these differences in the ink, which require a future independent image review rather than changes to the frozen text.

**Context and relation:** `hua_project/136.modern.tex`, “Coefficients binomiaux modulo $p$ (pages19 à22),” lines580–598, corresponding to scans020–023: same intended argument, with editorial letter readings that differ from this transcription. `same_cote_136/MPL_136_235-281_notes.md`, N21, scans275/277/279: supplies an independent coefficient-uniform argument, not an adjudication of the scan020 letter/prime readings. **Results-state:** g1031 / gapg1048; Hua **136-shadow-full-faithfulness**. **Search:** SH25.

## Boundaries for merging

No source in this range establishes an unrestricted all-graded unit, validates the literal infinite negligible quotient, proves the Ext corollary from ordinary full faithfulness alone, or supplies a monoidal/PD reconstruction merely by declaring the shadow functors fully faithful. Conversely, the written digit argument, sparse local lemma, arbitrary-abelian-group tail rigidity, coefficient equalizer, morphism recovery, and retained weighted arithmetic argument should not be labelled open merely because later notes reprove or reformulate them; this historical assessment does not certify every literal formula, and the local reading questions remain as recorded. The source's transient “Bijectivité?” is resolved; its `[à degrés $\geq0$?]` is an actual scope question; the extensive cancelled calculations are proof revisions rather than retractions of the weighted theorem.

Per-note supplied-context queries and selected hits are recorded in `shadow_searches.md` and `shadow_searches.json`; `shadow_searches.py` reproduces that search ledger. The ledger searched all four supplied same-cote notes, Hua's modernised cote136, and `RESULTS_STATE.md`; no unsupplied earlier note or supporting proof was accessed.
