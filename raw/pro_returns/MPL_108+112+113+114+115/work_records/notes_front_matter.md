# Research notes — MPL 108, 112, 113, 114 and 115

## Scope, evidence and how to read the notes

These notes accompany the frozen diplomatic transcription of all **40 supplied scans**, in the prescribed order: 108/002–006, 112/002–005, 113/002–013, 114/002–006 and 115/002–015. A reference such as **115/010** always means cote 115, archive PDF scan 10, not the author's handwritten page number. The source text remains in the page fragments and combined LaTeX; the notes use modern notation only in explicitly interpretive discussion.

The sole transcriber read the whole images, the supplied halves, and the second audit in one stream, then reconciled notation before freezing the 40 fragments and combined transcription at **2026-11-17 19:31:09 UTC**. Context contents were first opened at **19:31:17 UTC**; the preliminary accidental listing of ZIP directory metadata, before the task instructions were fully read, is disclosed in the progress record, and no context member content was read at that stage. After freezing, three research workers assisted only with context comparisons and read the frozen text, not the scans; none transcribed or revised manuscript readings.

Every note separates manuscript evidence from interpretation. A **conjecture** entry includes an explicit question or programme; **unproved claim** also covers assertions supported only by a sketch; **self-flagged** records an author's question mark, verification warning or deliberate restriction. **Withdrawn in the same text** includes visibly cancelled attempts, without presuming that a replacement proves their negation. An **own idea** is an argument or proposed connection offered here, with confidence and reason; where it verifies a lead from Michel Hua's project, that credit is retained. A **reading question** reports what context suggests while leaving the frozen reading untouched.

The supplied `notes/RESULTS_STATE.md` was read before these notes were drafted. Its run statuses are claims of the indicated returns unless an explicit intake or referee verdict is supplied; the scope of any such verdict is not extended to neighbouring rows. Each of the **12 numbered NEW_RESULTS items**, **10 STRATA**, **76 PATHS**, **113 BISITE** and **56 RESIDUE** statements has an individual comparison below, as do all **7 supplied Hua findings** and the **3 known-after-all notices**. Each comparison-register row has the kind **reading question**: it asks how the supplied claim matches the frozen evidence, with the relation and original status given separately. Missing dossier section letters are not missing work: only the rows actually supplied are counted.

“Absent” means that the specific statement was not found in the entire frozen 40-scan selection; it makes no claim about other archive material. “Precursor” means a related question or ordinary construction, not a proof of the later theorem. “Different” identifies a material mismatch of definition, hypotheses, variance or scope. For absent statements no fictitious scan or quotation is assigned. Exact supplied statements, statuses, locators and per-item search records are preserved in the research JSON files under `work_records/`; long source paths identify the user's registers and were not separately accessed.

The strongest conclusions of the comparison are these:

- Neither the **strong W(7)** nor **total asphericity ⇒ filteredness** is stated in the supplied scans. The chronology section identifies the earliest related question here and the explicit later locators actually present in the supplied companion.
- The totality in 114/004 is the **Pursuing Stacks product/diagonal notion**. The companion explicitly distinguishes the later condition quantified over all outgoing functors, so the draft cannot close TOTASPH D.7 or RESIDUE F.5 by a change of terminology.
- Cote115 contains substantial **ordinary kernel, dual-adjunction, contraction and Kan-pairing machinery**. It does not state the derived, exceptional, spectral or higher-coherence conclusions of BISITE E–G and RESIDUE I, whose comparisons are given individually.
- The draft totality proposition on 114/004 differs from the retained *Pursuing Stacks* Proposition 4 at manuscript page 350. Its explicit Loc4 hypothesis defeats the all-functors-localizer objection, but the separate ordinary-cube obstruction remains relevant.
- Several literal assertions require correction in commentary: the unqualified external-product full-faithfulness assertion in 115/004, the arbitrary-coefficient tensor full-faithfulness assertion in 113/010–012, recognition from ordinary projectives alone in 113/004, and ordinary faithful/conservative restriction from asphericity in 114/005. None has been silently repaired in the transcription.

## Standing question 1 — Steps the manuscript itself marks as unverified

This register is an index of authorial reservations, not of the transcriber's `\unsure` readings. The full one-item research discussions follow; ordinary unproved assertions without an explicit reservation are recorded there separately. The quotations are short cues; LaTeX commands preserve cancellations or mathematical marks where relevant.

| Cote / scan | Author's words or mark | What remains unverified or qualified |
|---|---|---|
|108/003, item 1|“implied by L 5)?”|Čech-asphericity implication; R10801.|
|108/003, item 3|“(Cat) a model category?”|Model structure on Cat; R10804.|
|108/003, item 4|“When is” / “(closed) model category?”|Presheaf model structure; R10805.|
|108/003, item 6c|“a test category, or wtc? no”|Bare negative answer, without its proof; R10807–08.|
|108/003, item 7|“Dold Puppe axiomatized?”|Axiomatization and the O-shaped example; R10810.|
|108/003, item 10|“strict?” / “is Gr(M)” / “Dold-Puppe ??”|Group-object modelling and strictness; R10813.|
|108/004, item 11|“Est-il suffisant”|Reduction to all Δ₀→Δₙ→X tests; R10815.|
|108/004, item 13|“Is a … 0-connected topos also totally ∞-connected?”|The forward implication; R10817.|
|108/004, item 13 insertion|“and conversely”|The converse is separately requested; R10829.|
|108/004, item 13|“Is it enough that product of two …”|The binary-product test for connected objects; R10830.|
|108/004, item 13 parenthesis|“W-aspheric objects”|The alternative binary-product test for the selected weak class; R10831.|
|108/005, second item 15|“pour un type d'homotopie relatif … ?”|Relative homotopy spectral sequence; R10820.|
|108/005, item 16|“induisent-ils des équivalences quasi-inverses”|Localization by homotopisms; R10821.|
|108/005, item 16|“Est-il vrai que X … ssi A_/X l'est”|First contractibility comparison; R10822.|
|108/005, item 16|“Que ∀ C … si (et seulement si)”|Right-adjoint contractibility comparison; R10823.|
|108/005, item 16|“un homotopisme ?”|Product comparison; R10824.|
|108/005, item 16|“Variantes”|Further variants named but not formulated; R10824.|
|108/006|cancelled “Prendre” example|The ring-category candidate is withdrawn; R10827.|
|108/006|“sauf si A≃Δ₀”|An explicit exception to the contractor claim, not a doubt; R10828.|
|112/003, question 1|“est-ce une équivalence de catégories ?”|Localization/derived equivalence; R11203.|
|112/003, margin|“OK pour A=Δ, mais est-ce OK pour A=Δ_/X”|The slice extension; R11204.|
|112/003, question 2|“a-t-on”|Positive Ext comparison; R11208.|
|112/003, bracket|“même sans supposer L,M lisses ?”|Removing smoothness; R11209.|
|112/003, insertion|“et peut-on y remplacer … ?”|Complexes instead of objects; R11210.|
|112/003, question 3|“On cherche L′” / “tronqué … homotopiq.”|Truncation realization; the earlier vanishing assumption is deleted; R11211, R11215.|
|113/003|cancelled “il suffit que”|MU-fibration integration criterion remains a cancelled attempt; R11301.|
|113/010, diagram|“pl. fid ?”|The key full-faithfulness arrow is questioned; R11313.|
|113/010, margin|“Attention, il faut passer à un univers plus gros”|Size warning; R11315.|
|113/012, margin|“à vérifier”|Contraction formula; R11317.|
|113/012, margin|“il suffit de le vérifier pour”|Proposed reduction to representables, not an additional completed proof; R11317.|
|113/012, bottom|“Question” / “TSVP”|Enough projectives and Tor-acyclicity; conditional continuation on scan013; R11320.|
|114/002, item 1|“Morphisms of asph. structures? Inverse images?”|Two tasks left open; R11401, R11424.|
|114/002, item 5|“When does … give rise to a can. modelizer?”|Existence criterion; R11405.|
|114/002, item 6 margin|“V ? Also VII”|Unsettled placement of the test-functor topic; R11406.|
|114/002, item 7|“Finiteness conditions … ?”|Finiteness programme; R11407.|
|114/002, item 8|“Computation of cohomology by boundary operator?”|Boundary-operator programme; R11408.|
|114/002, bottom|“(7) and 8) may not be treated at all”|Express postponement/possible omission.|
|114/002, bottom|“1, 4, 5, 6 can be looked at later”|Express postponement, not “at Caen”.|
|114/003|“weak test category?”|The P_f(I) candidate; R11410.|
|114/003|“total 0-connectedness” with “?” over implication|The totality question; R11412.|
|114/004|“I'll have to clarify the points a) and b)”|The preceding contractor discussion needs clarification; R11425; the retained-text comparison is R11415.|
|114/004|“look whether it really depends on W”|Dependence on the localizer, followed by the draft proposition; R11412–15.|
|114/005, opening|“?” over ⇒ “i* conservatif et fidèle”|Nerve conservativity/faithfulness; R11416–19.|
|114/005, margin|“Mais il faut … hypothèse sur W!”|Unspecified missing localizer condition; R11418.|
|114/005|“Peut-on avoir M_as=∅”|Empty example, then “OK”; R11420.|
|114/005|“Contr'exemple! Peut-on avoir M_as={a}”|Singleton example continued on scan006; R11421.|
|114/006, cancelled|“à vérifier des conditions qui l'assurent”|Adjoint existence and admissibility; R11422.|
|114/006, cancelled|“Mais va-t-on supposer que f_! applique”|Preservation of the aspherical part; R11423.|
|114/006, cancelled display|“f_!(Â_as)⊂ B̂_as ?”|The specialized preservation question; R11423.|
|115/003, first two displays|“?” over ≃|Two preliminary Hom/adjunction comparisons.|
|115/003, opposite orientation|large cancellation strokes|The draft wheel is cancelled; compare the live wheel on scan006.|
|115/006, bottom|“Je suppose I,J finis pour ``play safe''.”|Deliberate finiteness safeguard, not an infinite-family theorem.|
|115/008, lower section|“Iso (si et) seulement si … représentable ?”|Reflexive objects versus representables.|
|115/008, next line|“une équivalence faible (sans doute pas)”|A separate weak-equivalence question; the doubt belongs here.|
|115/008, next line|“transforment-ils équiv. faibles en isom ?”|Whether the two transforms invert weak equivalences.|
|115/009, cancelled|“F(X^∨) ?”|A cancelled higher-functorial/topos draft, not a settled comparison.|
|115/012, margin|“Cas où … est pl. fidèle ?”|Full faithfulness of the envelope functor.|
|115/012, insertion|“?” over equality|Identification of the induced functor with φ_* bearing the uncertain sharp/natural superscript.|
|115/012, margin|“comm. comm ?”|One of the compatibility/commutation checks is questioned.|
|115/012, display|“v=v′∘φ_* ?”|The proposed morphism compatibility.|
|115/014, final paragraph|“Mais” / “ne sont pas …” / “n'est pas tjrs une équivalence”|A warning limiting the preceding gluing claim.|
|115/015, bottom|unfinished Hom_!(Â_ab expression|No explicit verification phrase, but the final example is visibly incomplete.|

## Standing question 2 — Titles, author numbering and page counts

No supplied title sheet states a total such as “19 pages” or a range such as “Pages 1–67”. The scan counts below are counts of the supplied selection, not numbers written by Grothendieck. Archive foliation, printer dates and the page numbers of reused texts have not been put into `\mspage`.

| Cote / scan | Title or written count/number | Interpretation and limits |
|---|---|---|
|108/002|“Divers” / “Liste questions”|Cover; no author page count. Five scans supplied for cote 108.|
|108/003–005|question numbers 1–17, with 15 repeated|Question numbering, not pagination; no missing page inferred from the repetition.|
|108/004|“--18--”; “4 janvier 1973”|Printed pagination/date of the reused Stavroulakis text, not author pagination or the date of the homotopy notes.|
|112/002|“Linéarisation”|Cover; no author page count. Four scans supplied. The separate column of digits is not a written count of this dossier.|
|112/003|“Linéarisation” in a drawn bracket|An internal heading; no author page number.|
|112/004|“4.11.”|Date-like inscription with no year, not a page range.|
|113/002|“Abelianization”; uncertain marginal “9.”|Cover; no explicit page count. The uncertain 9 is not interpreted as “9 pages”; 377 and 1 are archival. Twelve scans supplied.|
|113/004,006,008,010,012|circled 1,2,3,4,5|Author numbering of the additive sequence; scan013 continues the last discussion without a fresh handwritten number.|
|113/003|cancelled MU-fibration draft|A separate reused draft before the numbered sequence; no independent title/count is visible.|
|113/005,007,009,011,013|computer printouts, including “16 SEP 82” and “29 06 82”|Reuse evidence, not dates assigned to the mathematical writing.|
|114/002|“Asphéricité” in the margin|Subject heading/cover-like agenda; no count. Five scans supplied. IV, V, VI, VII are work-plan references.|
|114/004|“350”|Printed page of a PS draft, with manuscript corrections; not a handwritten page number for the two-leaf French sequence.|
|114/005–006|1,2|Author numbering of the French asphericity draft.|
|115/002|“``Correspondances'' fonctorielles” / “Dualité des topos”|Cover; no page count. Fourteen scans supplied.|
|115/004,006,008,010,011,012|circled 1,2,3,4,5,6|Author numbering of the correspondence sequence.|
|115/014|7, uncircled|Author numbering continues, with no circle supplied by the transcription.|
|115/015|no new author number|Final coefficient continuation, with an unfinished expression; no inferred 8.|
|115/003,005,007,008,013|reused computer material, including “02 JUN 82”|Physical reuse evidence only; no inference of an exact writing date.|

Title and count comparisons used the frozen pages, inventory and `hua_project/README.md` plus the five modernized files. Hua's page n corresponds to scan n+1; its editorial page ranges and archive dating brackets are not author-written counts or dates.
