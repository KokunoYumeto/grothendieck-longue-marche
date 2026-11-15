# Candidate documentary, doubt, and revision notes

Prepared from the frozen text of cote 154, scans 127–176, after the transcription freeze reported at 2026-11-15 01:44:43 UTC. No manuscript image was consulted by this agent, and no page or combined transcription was changed. These are candidate research notes, not corrections to the diplomatic transcription.

## Citation and status conventions

The source for each scan NNN is pages/MPL_154_127-176_154_scanNNN.tex in the working directory; references below give approximate source line numbers, including diagram-code lines where a label occurs. The context files are in /workspace/scratch/74fd90793254/context. All 33 candidate IDs have prior timestamped term/object searches in records/research_doubts_searches.md.

“Own idea” labels an editorial classification, proposed comparison, or interpretive caution supplied here; it does not attribute that judgment to the manuscript. Confidence concerns the stated observation, not the truth of an unproved mathematical claim or the certainty of every letter. The supplied Esquisse_cote119_copy1_API_transcription.tex explicitly says it has not been checked by eye; entries from RESULTS_STATE.md remain unreviewed claims or first-pass leads unless explicitly reviewed, and their named external source files have not been read here.

## Documentary material

### D01 — Fifty selected scans and a continuous offset in marginal pagination

**Source:** all 50 page files; first scan 127:116 and last scan 176:297; isolated marginal numerals at 134:2 and 172:387.  
**Kind:** documentary observation; confidence high for the mechanical count and mapping.

The 50 selected scans 127–176 carry exactly one recorded <code>\mspage</code> value each, continuously 126–175, so scan N corresponds to marginal number N−1 throughout this selection. This supplies the concrete check behind the context’s <code>154-generisation-cube</code> location “their pp. 153; our scans 154” (RESULTS_STATE.md:122), while README.md:9 independently specifies the selected scan range. The additional <code>\margin{\unsure{1}}</code> at 134:2 and <code>\margin{\unsure{4}}</code> at 172:387, and the printed “PAGE 1” on 137:3, should not be promoted to competing total-page counts. **Own idea, high confidence:** describe this as a 50-scan selection with marginal pagination 126–175; the selected text does not itself announce a 50-page work or establish the complete cote’s extent.

### D02 — A dated title occurs inside a canceled passage

**Source:** scan 160:2–5,75–76, marginal page 159.  
**Kind:** documentary observation; confidence high about the cancellation scope and date as transcribed; low on the marked X-form.

The exact date <code>\uline{1.1.84}</code> precedes “Compléments et rectifications sur les facettes exceptionnelles de” <code>$(\unsure{X|\mathcal X},K)$</code>, and both occur within the <code>\deleted{...}</code> spanning 160:2–75. It is therefore a locally dated, canceled heading, not an uncanceled title leaf for the whole selection. **Own idea, medium confidence:** the conventional French date reading is 1 January 1984, but this dates the annotated passage and does not date every selected page. The direct search found no matching title or date entry in the supplied context.

### D03 — Computer-printout dates belong to the reused paper

**Source:** scans 128:63–74; 137:3; 142:3–4; 146:359–370; 147:30–41; 150:2; 155:3–4; 156:189–190; 159:118–142; 161:301–310; 165:97–102; 167:39–44; 169:3; 173:35–40; related repeated and faint print identified in the inventory below.  
**Kind:** documentary observation and own dating caution; confidence high that these are transcribed printed job/news dates.

The printed layers contain “19 AUG 82 JOB EXECUTION DATE,” “25/ 8/ 82” with “10 HEURES 57 MINUTES,” job dates of 16 and 17 August 1982, and computing/news dates listed below. They also contain a compiler-version date “06/28/82,” a printed header date “08/19/82,” announcement and journal-update dates, and the numerical field “DATE = 82.231”; their distinct printed functions should remain explicit. **Own idea, high confidence:** these identify the reused printout layer and must not replace the local manuscript date in D02; a notice announcing a future system change does not itself date the handwritten mathematics. The sole context hit for the broad date query, Esquisse API text 119/28:1223–1224, concerns mathematical reflections from December 1981 to January 1982 and is unrelated, so no matching register entry for this printout evidence was found.

### D04 — Catalogue title versus local subject captions

**Source:** scans 136:20–35; 153:142; 155:18; 160:5; 166:244–248.  
**Kind:** documentary observation; confidence medium overall, low on the marked captions.

README.md:9 supplies the catalogue-style title “[Système de pseudo-droites] : notes manuscrites (1983-1984, s.d.),” but the selected frozen pages supply local captions such as <code>\unsure{types} de fuseaux</code>, “balayages élémentaires de positions relatives,” and <code>\unsure{Canali|Canaux}</code>. Scan 136 instead organizes a local dictionary under “faces,” “arêtes,” “arêtes biorientées,” and “Sommets,” while the substantial title at scan 160 belongs to the canceled passage recorded in D02. **Own idea, medium confidence:** the inventory records no cover in this selection, so retain the catalogue title as external metadata and these as local headings without reconstructing an unseen title page or section hierarchy. The context search found the README metadata and Hua’s scan-154 entry, but no entry for these particular captions.

## Explicit questions, deferred work, and incomplete constructions

### U01 — The inverse-circuit question is answered immediately

**Source:** scan 133:125,137–139, marginal page 132.  
**Kind:** own classification of a question as answered locally; confidence high.

“Comment trouverait-on le circuit inverse” is followed in the same line by “C'est en changeant à la fois la rive” and “l'orientation,” with the two choices denoted ρ and ω. The same passage records <code>D_9=D_1</code> and then describes the operation σ₂ on the relevant orientations. **Own idea, high confidence:** this question belongs in the research inventory as an answered explanatory question, not as evidence that the circuit construction is expressly left unverified. No matching context entry was found for the inverse-circuit question.

### U02 — The σ₁ and σ₀ tasks have later local progress

**Source:** scans 135:14,16,59; 138:213–217; 157:185–192.  
**Kind:** self-flagged task with later partial answer; own scope judgment; confidence high on the textual sequence, medium on the extent of resolution.

Scan 135 says “il resterait à interpréter” σ₁ and σ₀, and scan 138 still displays <code>\sigma_0=\ ?</code>; scan 135:16,59 gives a sector interpretation and local central symmetry for σ₁, while scan 157:190 later says σ₀ “change” α to −α while retaining σ_D, σ_D′, and β. **Own idea, medium confidence:** the task is visibly developed within this selection, so the early question mark must not be reported as an entirely unanswered σ₀ problem at the end of the packet, although the later formula alone is not a proof of every geometric identification. The direct context match is the API Esquisse, 119/12–13, lines 517–542, where the cartographic generators and <code>\rho_s=\sigma_2\sigma_1</code>, <code>\rho_f=\sigma_1\sigma_0</code>, <code>\sigma=\sigma_0\sigma_2=\sigma_2\sigma_0</code> are stated; it has no result-register ID and is not eye-checked. That supplies algebraic background, not a reviewed resolution of the specific fuseau interpretation.

### U03 — The joint quotient is expressly left to understand

**Source:** scan 135:59–82; compare scan 139:7–9.  
**Kind:** self-flagged/deferred step; confidence high.

“Il faudrait comprendre aussi les éléments de” <code>\widetilde X^{\swarrow\!\searrow}/(\sigma_1,\sigma)</code> expressly identifies a further interpretation task and associates it with the half-indexed figures <code>D_{1/2},D_{2/3},D_{5/6},D_{6/7}</code>. The later diagram at 139:7–9 includes the pair (σ₁,σ), but a diagram label by itself does not establish that the requested geometric interpretation has been supplied. **Own idea, medium confidence:** retain this as a deferred identification in the present selection. The only term/object matches in context are the cartographic-group formulas in the unverified API Esquisse 119/12–13:520,537; no matching context entry explaining this joint quotient was found.

### U04 — A closing equality is explicitly questioned

**Source:** scan 137:259–263, especially line 261, marginal page 136.  
**Kind:** self-flagged equality plus reading question; confidence high on the question mark and low on the target index.

The long circuit ends with the exact transcription <code>D_{20}\overset{?}{=}D_{\unsure{6|0}}</code>, so both the equality’s status and the right-hand subscript need to remain visible. **Own idea, medium confidence:** record a questioned closure/identification rather than silently turning the sequence into a verified period or selecting 6 instead of 0 on mathematical grounds. The source line also begins with an uncertain <code>D_{\unsure{9|1}}</code>, which limits a reconstructed cyclic indexing scheme. No matching context entry for this specific circuit or equality was found.

### U05 — Even the two endpoints receive a local doubt marker

**Source:** scan 151:76–79, especially line 77, marginal page 150.  
**Kind:** self-flagged local reconstruction issue; confidence high.

After saying that the incident faces and their edge circuits are not the difficulty, the text singles out “les deux” <code>\inserted{(?)}</code> “sommets incidents” to a_L. **Own idea, medium confidence:** the insertion attaches a doubt to this endpoint description; it should not be generalized into a claim that every edge in every surface has an unknown number of ends. Context matches EXIT_ONE_TYPE P4e (RESULTS_STATE.md:42; source named EXIT_ONE_TYPE_results.csv, cote 149 scan 133) and MPL_121_049-073+153+155 R121-08 (:82; source named MPL_121_049-073+153+155_notes.md, cote 121 scans 050–052) concern broader loss of link/attachment information and are respectively an unreviewed return claim and a first-pass lead, not this particular endpoint question. No exact matching entry was found.

### U06 — The endpoint construction lacks a secured choice

**Source:** scan 151:79–82.  
**Kind:** self-flagged/unverified construction; confidence high on the hesitation, medium on its interpretation.

The proposed task is “de reconstruire le sommet extrémité” from (L,ω_s), “si possible” using a critical relative position obtained by “blocage” around s. The concluding sentence says “il y a plusieurs choix naturels” and “il n'est pas sûr qu'aucun de ces choix ne marche!”, whose exact double-negative wording should remain intact. **Own idea, medium confidence:** this is positive evidence that a canonical working choice has not been secured at this point, but it does not justify silently rewriting the sentence as either “all choices work” or “none works.” Context MPL_150_044-084 N18 and Q2 (RESULTS_STATE.md:87,107; source named MPL_150_044-084_notes.md, scans 150/077,081–084 and 150/073–084 respectively) are first-pass attachment/choice-of-retractions leads only; no matching entry proves or refutes this blocking construction.

### U07 — The universal specialization question is not answered by its conditional continuation

**Source:** scan 154:31–37, marginal page 153.  
**Kind:** explicit mathematical question; confidence high.

For a non-principal D with <code>\operatorname{card}S_D\geq2</code>, the text asks whether every “position relative principale” through S_D “est-elle une spécialisation de D ?”. The next sentence begins “Pour celles … qui sont des spécialisations de D,” so its orientation-arrow description applies to an already restricted subclass and does not, by its wording, answer the universal question. **Own idea, high confidence:** keep the question separate from the cube assertion that follows. The same-page context entry Hua <code>154-generisation-cube</code> (RESULTS_STATE.md:122; cote 154, marginal p153/scan154) addresses stable generizations, is marked “conjecture (unsearched)” with no verdict, and supplies no answer to this principal-specialization question.

### U08 — The map from repères to stable positions stops mid-description

**Source:** scan 136:24–40, especially lines 37–40, marginal page 135.  
**Kind:** incomplete written construction; own classification, confidence high about incompleteness.

The displayed map ends with “la position relative stable obtenue en” followed only by canceled <code>\unsure{mouvant}</code>, leaving its final instruction absent in this text. Its domain is written (D,s,ω) at line 40 even though the preceding frame data at line 25 insert an additional orientation <code>\bar\omega</code>, a distinction worth preserving without supplying a repair. **Own idea, medium confidence:** this is an incomplete formulation rather than an explicit statement that the intended map does not exist. The context API Esquisse discusses repères at 119/12–13:517–542 and the relative-position surface at 119/50:2211–2223, but no matching entry completes this particular map.

## Rejected suggestions, cancellations, and substantive local revisions

### W01 — The inverse guess for σ₀ is explicitly rejected

**Source:** scan 135:3–5.  
**Kind:** withdrawn in the same text; confidence high.

“Pour” σ₀, “serait-ce l'inverse ?” receives the immediate underlined answer “Non”; the next clause attributes the envisaged symmetry to σ and describes the repère’s symmetry about its origin vertex. **Own idea, high confidence:** this is a rejected local identification, not an unresolved conjecture or evidence that σ₀ is absent from the eventual structure. The context match in the API Esquisse 119/12–13:520,537 is only the general operator presentation; no result entry records this particular rejected suggestion.

### W02 — “Principales” is removed from a frame description

**Source:** scan 138:217.  
**Kind:** substantive local revision plus uncertain terminology; confidence high on the deletion, low on the replacement word.

The description of the relative positions corresponding to surface repères deletes <code>\unsure{sont}\ \unsure{principales}</code> and continues with “sont de” <code>\unsure{tricalité|criticalité}</code> <code>\geq2</code>, together with a chosen vertex and a local orientation. **Own idea, medium confidence:** record the replacement as a change in the stated description, without turning the deleted principal condition into a standing hypothesis or resolving the uncertain technical word. The context query produced unrelated ordinary uses of “principale(s)” in the API Esquisse; no matching entry for this condition was found.

### W03 — A corrected exchange is distinct from a canceled formula

**Source:** scan 140:8–23, especially lines 10–19.  
**Kind:** local revision; own caution about the meaning of cancellation; confidence medium.

The σ₁ description deletes <code>\unsure{a^+\text{ et }a^-}</code> and instead exchanges a⁺ with b⁺ and a⁻ with b⁻, while the passage retains <code>\sigma_1=\sigma\sigma'</code> and cancels <code>\unsure{\sigma=\sigma_1\sigma'}</code>. **Own idea, medium confidence:** cancellation of the latter line alone is not a manuscript refutation of that algebraic identity, since the immediate involutive interpretation may make the two formulas equivalent. The context API Esquisse 119/12–13:520–537 supplies the general cartographic relations; the other hits, including BISITE G.10 and RESIDUE H.1, concern barycentric/finite-poset constructions and do not resolve this example. No matching context entry for the particular four-repère example was found.

### W04 — The orientation conventions include explicit repairs

**Source:** scans 133:125,139,173; 151:4–9.  
**Kind:** local revision affecting later sign conventions; confidence medium.

At 133:139 the canceled wording <code>\unsure{change fixe}</code> is followed by underlined “fixe” for the local orientation <code>\bar\omega</code>, whereas ω changes; at 151:9 a second <code>\unsure{gauche}</code> is deleted and replaced by underlined “droite.” **Own idea, medium confidence:** these are affirmative local repairs to orientation descriptions, so the deleted words should not be used to manufacture a contradiction with the retained direction or sign. Scan 151:8 also cancels an uncertain fragment attempting to connect the arc germ to a stable relative position, which belongs with the incomplete-construction evidence rather than a proved identification. No matching context entry for these specific conventions or repairs was found.

### W05 — Fuseau terminology is revised without retracting the whole classification

**Source:** scan 153:142–168.  
**Kind:** abandoned terminology and qualified assertion; confidence medium, low for marked names.

The classification lists couloirs, semi-couloirs, and ordinary fuseaux while canceling <code>\unsure{biparalléliques}</code>, <code>\unsure{paralléliques}</code>, and a separate “ordinaire”; the alternatives <code>\unsure{unilatéraux}</code> and <code>\unsure{triviaux}</code> appear as insertions. **Own idea, medium confidence:** these are changes in nomenclature or local placement, not sufficient evidence that the three-way geometric discussion has been withdrawn. The final qualification “Sauf dans cas triviaux” limits the assertion that a fuseau is determined by its banks’ isotopy classes; it is an exception clause, not a doubt marker. The context search found no matching fuseau/couloir entry.

### W06 — The “et non = L” correction is itself canceled

**Source:** scan 160:2–10,75.  
**Kind:** withdrawn correction; confidence high on the cancellation scope, low on the marked superscript.

Inside the whole canceled passage, the proposed correction reads <code>\varphi^{-1}(\unsure{X_1^a|X_1^0})=L\cup K_0</code> with “et non” <code>=L</code>. **Own idea, high confidence:** this documents a correction that was drafted and canceled, so neither the corrected formula nor the rejected formula should be promoted to an established result on this evidence alone. The context query’s φ/facette hits concern STRATA F.9/F.11 and unrelated API Esquisse facets; no matching entry for this preimage formula or exceptional-facet correction was found.

### W07 — The canceled draft also contains geometric prescriptions

**Source:** scan 160:12,68–75.  
**Kind:** withdrawn in the same text; confidence high on withdrawal, low to medium on the detailed readings.

The same cancellation encloses the “double paire de facettes,” a chosen “branche principale” δ, a common boundary point for the other branches, “la loi de symétrie,” privileged-bank rules, and a modification of a <code>\unsure{ruban généralisé}</code> by a parallel interior <code>\unsure{path}</code>. **Own idea, medium confidence:** these preserve the content of a proposed exceptional-facet construction but cannot be presented as the uncanceled final construction or as a proved symmetry law. Several decisive terms remain explicitly uncertain, including the description of the points whose multiplicities obey the symmetry. No matching context entry for these prescriptions was found.

### W08 — Canceled trials do not each amount to a withdrawn theorem

**Source:** scans 135:17–58,60–82; 140:35–46; 141:85,95,101,136; 145:17–18; 146:203–204,275,325; 161:293–294; 169:158–162; 172:188–189.  
**Kind:** revision inventory; own classification; confidence medium.

The frozen markup preserves canceled trial drawings and scope blocks, the strings “A B C D E F G” and “A B C E D” at 145:17–18, replaced diagram indices and operator labels, and the local numerical revisions <code>\deleted{\unsure{6}}\inserted{7}</code> and <code>\deleted{\unsure{7}}\inserted{6}</code> at 172:188–189. **Own idea, medium confidence:** list these as evidence of diagrammatic or notational revision, while withholding any claim that a particular theorem has been refuted unless surrounding prose states one. Context MPL_148_029-072 R39 (RESULTS_STATE.md:85; source named MPL_148_029-072_notes.md, 148/067:10,62–85,87–96) is a first-pass lead about a different canceled skeleton description, not an identification of these drawings. No matching entry for these particular trials was found.

### W09 — Two small wording revisions should not reverse retained assertions

**Source:** scans 155:37–38; 158:18–23.  
**Kind:** local revision; confidence high on the retained textual direction, low on marked deleted words.

At 155:38 the text retains “n'est” and underlined “pas” while canceling <code>\unsure{jamais}</code>, so its assertion remains that position 1 in that configuration is not critical. At 158:20, <code>\unsure{système de trois droites}</code> is replaced by “triangle” of X before the discussion of the dual triangle. **Own idea, medium confidence:** these revisions change wording or the chosen description and should not be turned into a negation of the final statement or a rejection of duality. No matching context entry was found for either local revision.

### W10 — The K,L conditions retain several local replacements

**Source:** scan 171:280–309, especially lines 284,288,290,295,301.  
**Kind:** canceled and revised formulation within a condition list; confidence medium.

The list cancels <code>c) \unsure{on a} L\subset X, \unsure{1-compl.}</code>, supplies the retained condition that vertices of L have <code>\unsure{pair}</code> order, and introduces an incident multiplicity <code>\unsure{\nu_a|\ell_a}</code> after a canceled fragment. It also cancels <code>\unsure{\nu'_s|\nu_s}</code> before the 0/1 indicator <code>\unsure{\varepsilon_s}</code>. **Own idea, medium confidence:** preserve these as changes to the proposed data and notation rather than inferring that L ceased to be a cellular subobject, since L is already included in the heading at line 280. The context has generic 1-complex passages in the unverified API Esquisse, but no matching entry for this K,L condition list.

## Important reading and claim-status questions

### Q01 — The cube assertion is declarative; the prior register supplies a different status label

**Source:** scan 154:31–44.  
**Kind:** unproved declarative assertion and context comparison; confidence high on the distinction of wording.

“Les générisations stbles de D correspondent aux sommets d'un cube” is followed by its dimension ν, semi-stable generizations as edges, and incidence as specialization, with “canon.” and “arêtes” marked uncertain. Unlike the principal-specialization sentence at 154:34, this sentence has no question mark or explicit conjectural qualifier. Context Hua <code>154-generisation-cube</code> (RESULTS_STATE.md:122; cote154, p153/scan154) calls it “conjecture (unsearched)” and “Lean card: statement, no verdict…,” which is an unreviewed register status, not wording to insert into the manuscript. **Own idea, medium confidence:** describe it as a manuscript assertion whose proof is not supplied in this local paragraph, and use the API Esquisse 119/50:2211–2223 only as related evidence for the broader relative-position “surface modulaire” project.

### Q02 — The exponent and the straight-line comparison require separate reading caution

**Source:** scan 154:75–79.  
**Kind:** important reading question and context comparison; confidence low on the uncertain exponent/caption.

The count is frozen as <code>2^{\nu\unsure{+}}</code> “sommets” and <code>\nu2^{\nu-1}</code> “arêtes”; the adjacent caption reads <code>\unsure{Produit}</code> “des diagonales d'un polygone” with uncertain inserted “convexe,” uncertain “régulier,” and canceled “degré” before <code>2\nu</code>. Hua’s unreviewed <code>154-generisation-cube</code> entry instead gives an unqualified 2^ν vertex count and a straight-line comparison with only 2ν stable positions. **Own idea, high confidence:** preserve that difference between the frozen reading and the register paraphrase, rather than using the paraphrase to remove the exponent uncertainty or to extract a fully articulated straight-line theorem from the fragmentary caption. The other context hit, API Esquisse 119/23:1020, concerns a different regular polygon and supplies no resolution.

### Q03 — The disconnectedness marginal note is too uncertain for a firm counterexample

**Source:** scan 153:140.  
**Kind:** important reading question; confidence low.

The marginal NB has <code>\unsure{demeure}</code>, an intervening <code>\illegible{1}</code>, and <code>\unsure{disconnexe}</code> after a “couple” of uncertain “flèches,” even after adding uncertain adjacent “fuseaux.” Its explanation also has uncertain “libre” and “bord du fuseau.” **Own idea, high confidence:** record this as a potentially consequential disconnectedness remark whose subject and qualification remain insecure, not as a verified connectedness obstruction or a proved counterexample. No matching entry for the remark was found in context.

### Q04 — The hypotheses of the fuseau bijection remain partly insecure

**Source:** scan 153:153–168.  
**Kind:** important reading question concerning a declared correspondence; confidence low on the definition details.

The text states a “corresp. 1-1” between isotopy classes of fuseaux and semi-stable relative positions and adds “canon.”, but the defining conditions include uncertain <code>\{s,\bar s\}</code>, an uncertain implication sign, and the entirely uncertain subscript in <code>\Sigma'_{\sigma\ne1}</code>. **Own idea, medium confidence:** an eventual formal statement needs the precise ambient arrangement, intersection, and corridor condition fixed before this can be used as a theorem; the local declaration should nevertheless remain distinguished from explicit self-doubt. The subsequent “Sauf dans cas triviaux” also prevents dropping the exceptional cases from the bank-determination claim. No matching context entry was found for this fuseau definition or bijection.

### Q05 — Duality and orientation formulas should not be normalized from expectation

**Source:** scans 157:185–192; 158:18–23,119–120.  
**Kind:** reading/interpretation question; confidence medium for the retained sign pattern, low for the marked technical word.

The frozen text has <code>\omega^*=-\alpha^*\wedge\beta^*</code> but <code>\omega=\alpha\wedge\beta</code>, accompanied by “non croisés”; the next scan says the unprimed α,β,ω are “associés” while the primed triple is “non associés.” The preceding dual-triangle paragraph contains the unresolved reading <code>\unsure{d'épure|d'équerre}</code>. **Own idea, medium confidence:** these are distinctions to interpret using the stated choices and duality conventions, not sufficient evidence of a contradiction or permission to change a sign to match an expected convention. No matching context entry on these dual projective-plane orientation signs was found.

### Q06 — Several conditions are essential to the constant face sum

**Source:** scan 171:280–309.  
**Kind:** important reading question and bounded own interpretation; confidence low to medium.

The condition list culminates in a face sum equal to <code>2n</code>, “n indép. de F,” using <code>2\unsure{\nu_s|\ell_s}+\varepsilon_s</code> at vertices and <code>\unsure{\nu_a|\ell_a}</code> at edges with an uncertain <code>\subset|\in</code> and uncertain <code>\overline F</code>. The earlier clauses leave readings such as “dépliement|déploiement,” the doubled-curve notation, “section,” and the extra qualifier in condition d uncertain, and condition f actually says “le sommet de K sur l'arête.” **Own idea, high confidence:** a reconstruction or counterexample based on a silently corrected condition f, a guessed boundary-incidence convention, or an assumed meaning of the barred face would exceed this frozen text. The broad context search found only generic cellular/valence/multiplicity discussions and separate register claims, with no matching entry for this constant-face-sum system.

### Q07 — The inequality’s final punctuation is not a secure self-doubt marker

**Source:** scan 131:47–55.  
**Kind:** important reading question; confidence low on punctuation and the interrupted calculation.

The inequality at line 51 ends with <code>\unsure{\ast}\unsure{?|!}</code>, so the frozen reading does not decide whether the punctuation expresses a question or an exclamation. Canceled work at line 53 and the following <code>(\alpha\unsure{+|-}\beta)/2</code> description with an unfinished parenthesis at line 55 further limit a reconstructed calculation. **Own idea, high confidence:** retain this as uncertain arithmetic/punctuation rather than counting it among securely author-flagged unverified assertions. The context hits for an unrelated genus inequality and α,β variables in the API Esquisse do not match this calculation; no matching entry was found.

### Q08 — A counting expression has an uncertain factor and a canceled completion

**Source:** scan 142:236–241.  
**Kind:** important reading question and local cancellation; confidence low on the lower-order factor.

After <code>n(n-1)(n-2)/2</code>, the next expression subtracts <code>n(n-1)(\unsure{n-1|n-2})/2</code> from a half-product and then writes an equals sign, canceled <code>\unsure{n+2}</code>, and <code>\sim\frac18n^4</code>. **Own idea, high confidence:** the leading asymptotic shown in the text should not be used to choose the uncertain factor or to fill the canceled exact value; different lower-order terms can share the displayed leading term. No matching counting/asymptotic entry was found in context.

### Q09 — The final cycle and the Δ label do not by themselves settle an order or vanishing claim

**Source:** scan 176:3–9,225.  
**Kind:** important reading/interpretation question; confidence low on the marked labels.

The top diagram runs 1→2→3→4→5=1 with “spéc,” uncertain “gén,” “gén,” and <code>\unsure{épéc|spéc}</code>, while a lower label is <code>\unsure{\Delta=0|\Delta\simeq0}</code>. **Own idea, medium confidence:** a cycle combining generization and specialization does not by itself assert a directed specialization cycle, and the marked Δ relation is not a secure vanishing theorem. The relevant same-subject context hit is the unreviewed Hua cube entry, which does not identify this final diagram. The search also found the explicitly refereed LM7_PUSH E.65 chain involving a character Δ (RESULTS_STATE.md:8), but no object-identifying evidence connects that different Δ to this diagram; no matching context entry for the final label was found.

### Q10 — Elementary-sweep claims retain their local hypotheses

**Source:** scan 155:18,37–38,66–67,103–106; compare scan 156:183,185.  
**Kind:** bounded declarative claims and own scope caution; confidence medium.

The three configurations explicitly restrict the other vertices and line traces present, and their captions distinguish a case in which position 1 is not critical from cases where “1 est critique ssi 2 l'est,” including an asymmetric case. **Own idea, medium confidence:** these are local stated comparisons under the diagram’s hypotheses, not an express assertion that all elementary sweeps preserve criticality or an author-marked unresolved question. The context API Esquisse 119/48–49:2139–2168 discusses “balayage” and bigon creation/erasure and explicitly links the first operation to a dynamic theory of pseudolines, but it is unverified API text and supplies no proof of these three criticality captions. No matching result-register entry was found.

### Q11 — The cyclic sequences have distinct recorded terminal exponents

**Source:** scan 132:320–329.  
**Kind:** important indexing question; confidence low on the recurring letter, medium on the recorded exponents.

The repeated symbol is consistently marked <code>\unsure{\zeta|\xi}</code>, while one row ends with <code>u^{2(n-1)-1}</code> and a later row with <code>u^{2n-2}</code>; other lines identify a primed zero-indexed term. **Own idea, medium confidence:** these rows require a precise account of their starting points and ranges before combining them into one orbit formula, and the apparent one-step exponent difference should not be removed by editorial normalization. The only context search hit was the unrelated finite-poset enumeration entry RESIDUE H.7 (STATEMENTS_WITH_STATUS.md:68, “no review”), so no matching entry for these cyclic sequences was found.

## Documentary appendix: date expressions in their printed roles

This appendix belongs to D03; its context search preceded the note. The date strings below are documentary readings, not a new calendar conversion of machine identifiers or a chronology assigned to the handwriting.

| Expression as transcribed | Printed role and source |
|---|---|
| 19 AUG 82 | Job execution on 128:70; faint counterpart 129:63; repeated banners on 143:33–38, 144:99–104, 146:359–364, 147:30–35, 151:99–104, 152:17–22, 158:206–211. |
| 08/19/82-15:20:31 | Program/compiler header on 137:3; uncertain faint counterpart 138:3. |
| 06/28/82 | Parenthesized CFT version date in the same headers, 137:3 and 138:3. |
| 25/ 8/ 82; 10 HEURES 57 MINUTES | Plotter/processing heading, 142:3–4. |
| 11-08-82 | “DERNIERE MISE A JOUR DE JOURNAL,” 146:366 and 147:37. |
| 20 AOUT … 23 AOUT | Announced interruption from Friday 20 August to Monday 23 August, 146:368–370 and 147:39–41; those two lines do not print a year. |
| DATE = 82.231 | Numerical job field, 150:2 and 169:3; retained as a code rather than silently expanded. |
| 21 AOUT 1982 | Announced system installation, 155:3–4 and 156:189–190. |
| 06/08/82 | JESNEWS FR1 heading, 159:118. |
| 12 JUILLET 82 | Earlier job-class change described in the news text, 159:122. |
| 9 AOUT 1982 | Date for an announced Xerox printing capability, 159:127. |
| 09/08/1982 | JESNEWS Cadarache heading, 159:134. |
| 1/7/82 | Date of command-alias removal described in the news text, 159:136. |
| 30/7/82; 8H00 | Announced/retrospective GAF service change, 159:142. |
| 16 AUG 82 | Job execution at 161:306 and repeated banners at 165:97–102 and 167:39–44. |
| 17 AUG 82 | Repeated job banner, 173:35–40. |
| 1.1.84 | Manuscript date within the canceled passage, 160:3; included here only to distinguish D02 from the printed layer. |

Numerical strings inside TikZ geometry, including coordinate fragments that happen to resemble a date, have been excluded. No title/page-count/date conclusion rests on a machine filename, a drawing coordinate, or an expansion of a Julian-style job code.
