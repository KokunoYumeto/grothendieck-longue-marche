# Research memo: reused sheafification and filtered-module leaves

## Scope and evidentiary status

This memo examines only the frozen transcriptions of cote 33, scans 039, 041, 043, 045 and 047, and the three supplied context documents. No images were opened, and no transcription, inventory, doubts file, or progress log was changed. Source-line locators below refer to the individual frozen `.tex` files, not inferred manuscript line numbers.

The four English leaves are a reused typescript. Their authorship has not been established. Scan047 is enclosed in a page-level deletion in the frozen transcription; its mathematical content remains reportable, but cancellation of the sheet does not by itself establish retraction of every statement on it. All counterexamples below are conditional on the literal transcribed statement and its visible hypotheses; they do not establish what an unidentified source may have stipulated elsewhere.

The supplied `RESULTS_STATE.md` explicitly treats the returned-package notes as first-pass leads. None of the present items resolves or changes the status of **LM7 E.23**, **LM4 D.12**, **LM4 F.7**, or **LM7_PUSH C.6**. The relevant register connections are principally **MPL_33_098-146 §76** and **§78**, the comparison workflow and verified-locator lists, together with **§65** for the separate index of self-flagged steps. Where **MPL_33_098-146 N54** is mentioned, the connection is the method of testing a literal reused-source assertion, not its different theorem about étaleness.

## Draft research items

Each item contains one to four substantive sentences; confidence, context-search disposition, and source locators are recorded separately.

### RS01. The asserted product-Hom formula fails on a two-point space

**File / scans / lines:** 33; 041:17–26 and 043:10–23. **Kind:** own idea.

Even after replacing the free index set `x∈U` in the displayed global Hom formula by `x∈X`, the assertion followed by “It is easily checked that these maps are inverses” fails for abelian sheaves on the Sierpiński space \(X=\{s,\eta\}\), whose opens are \(\varnothing,\{\eta\},X\). A sheaf is an arrow \(A\to B\), and \(P_X\) sends it to \(A\oplus B\xrightarrow{\operatorname{pr}_B}B\), so its morphisms have the form 
\[
\left(\begin{pmatrix}a&b\\0&d\end{pmatrix},d\right),
\quad a:A\to A',\ b:B\to A',\ d:B\to B',
\]
rather than only the diagonal choices \(a,d\). For the constant sheaf \(\mathbb Z\), the maps \(\phi_X(m,n)=(m+n,n)\) and \(\phi_{\{\eta\}}(n)=n\) commute with restriction and supply the missing off-diagonal morphism.

**Confidence:** high; the commutative square and the extra Hom summand are explicit, and neither a choice principle nor a limiting argument is needed.

**Context:** The RS01 exact-term search found no corresponding object/formula in any supplied context file. `same_cote_33/MPL_33_098-146_notes.md`, N54, scan145, is a methodological parallel: it tests another literal reused-source assertion by an explicit example; this item adds a different counterexample and does not restate or contradict that lead. **Register:** bears on **MPL_33_098-146 N54** only methodologically and on **§76** as a new S19 comparison item; those statuses remain first-pass claims.

**Primary comparison:** Stacks, Lemmas 6.27.2–3, Tags [009B](https://stacks.math.columbia.edu/tag/009B) and [009C](https://stacks.math.columbia.edu/tag/009C); the example and matrix computation are ours.

### RS02. The adjunction identifies the omitted stalk object

**File / scans / lines:** 33; 041:17–26 and 043:10–23. **Kind:** own idea.

For abelian sheaves, writing \(P_XF=\prod_{x\in X}i_{x*}F_x\) and applying the stalk–skyscraper adjunction gives the comparison formula
\[
\operatorname{Hom}(P_XF,P_XF')
\cong\prod_{x\in X}\operatorname{Hom}((P_XF)_x,F'_x),
\]
whose first argument is generally larger than \(F_x\). On the two-point test of RS01, \((P_XF)_s=A\oplus B\), whereas \(F_s=A\); the evaluation retraction does not make these objects equal. This separates the invalid fullness assertion from the visible faithfulness argument in scan043:25–34, which only requires the monomorphism \(\rho_{F'}\).

**Confidence:** high; the formula follows from the universal property of a product and the cited adjunction, and the distinction is computed directly in RS01.

**Context:** RS02 found no exact match for skyscrapers or a stalk-adjunction comparison in the three supplied documents. `same_cote_33/MPL_33_098-146_notes.md`, “Comparison map for S19,” concerns other scans, chiefly 100–146; this item adds a separate categorical strand rather than a result about those scans. **Register:** **MPL_33_098-146 §76**, **§78** are relevant as the comparison method, with no substantive prior result to rederive.

**Primary comparison:** The Stacks Project Authors (n.d.), Lemma 6.27.3, Tag [009C](https://stacks.math.columbia.edu/tag/009C).

### RS03. Three source/target and indexing questions remain after freezing

**File / scans / lines:** 33; 041:15, 20–21; 043:12–22. **Kind:** reading question.

The naturality line in scan041 uses \(r_{x'U}\varphi_U\), although the objects subsequently named involve \(x\), and the restriction identity invokes \(\tilde p_{xV}\) while quantifying \(x\in U\) rather than \(x\in V\). Scan043 uses a global sheaf Hom on the left but the unbound open \(U\) on the right, and its proposed inverse includes \((\rho_{F'})_x\), whose source is \(F'_x\), in a composite declared to start at \(F_x\). These are type/index questions for collation with the source, separate from RS01: correcting those letters would not eliminate the off-diagonal counterexample, and the frozen text must remain unchanged.

**Context:** RS03 found no exact parallel formula. `same_cote_33/MPL_33_098-146_notes.md`, N39, scan146:30–32, similarly flags a mismatched factor, while N46 lists distinct reused-source anomalies on scans105, 109, 111, 131, 135, 139 and 143; this item adds new loci and restates their conservative collation method only. **Register:** **MPL_33_098-146 §76**; no same-point settled entry.

**Evidence:** The literal frozen formulas themselves; the proposed type checks are our analysis, not alternate transcriptions.

### RS04. Exact sheafification requires the preceding categorical hypotheses

**File / scans / lines:** 33; 043:36–41; 045:3–20. **Kind:** unproved claim.

The sentence “If \(\underline A\) is right perfect then \(R_X\) is exact” follows a reflection assertion explicitly requiring completeness and enough small objects, so it should not be detached from those preceding assumptions or the unavailable definitions I,4.1 and I,5.2. The visible use of right perfection is to pass exactness through the directed colimit defining a stalk, after which products supply only the left-exact sequence actually printed; this identifies an AB5-like role without proving that the source's terminology coincides with a modern definition. Kleisli and Wu (1964, p. 422) independently retain a small-object condition in their related category-valued injective-sheaf result, while the modern abelian-group/module case provides a verified baseline, not a proof of every generality asserted here.

**Context:** RS04 found no occurrence of the specific hypotheses or of sheafification in the supplied context. The notes' S19 comparison map has no corresponding sheafification scan; this adds a hypothesis-recovery task. **Register:** **MPL_33_098-146 §76**, **§78**; none of the LM4/LM7 entries supplies the missing categorical definitions.

**Primary comparisons:** Kleisli and Wu (1964), p. 422, final paragraph; Stacks, §18.3, especially Lemmas 18.3.1–2, Tags [03CM](https://stacks.math.columbia.edu/tag/03CM) and [03CO](https://stacks.math.columbia.edu/tag/03CO). These sources verify the stated comparisons, not the historical author's exact definition of right perfection.

### RS05. The intersection construction has a proof independent of the false Hom formula

**File / scan / lines:** 33; 039:22–30. **Kind:** own idea.

Assume the collection of relevant subsheaves of \(P_XF\) is a set, sheaves are closed under the required limits, and every sheaf unit \(G\to P_XG\) is monic. For a map \(\varphi:F\to G\) to a sheaf, the pullback \(H=P_XF\times_{P_XG}G\) is then a subsheaf of \(P_XF\) through which \(\rho_F\) factors, so minimality of \(R(F)=\bigcap G_i\) supplies the desired \(R(F)\to G\). The equalizer of two such factorizations is a subsheaf containing the image of \(F\), so the same minimality proves uniqueness. This conditional argument salvages the reflection construction without assuming that arbitrary morphisms \(P_XF\to P_XF'\) are coordinatewise, and exposes the separate size and monicity dependencies.

**Confidence:** high for the conditional proof; the unseen Chapter I hypotheses must still be checked to establish all of its premises in the source's general category.

**Context:** RS05 found no exact match for the construction in any supplied document. No same-point context scan is supplied; this adds a proof route to the S19 comparison work. **Register:** **MPL_33_098-146 §76** only at the programme level; no registered theorem is re-proved.

**Primary comparison:** Stacks, Lemma 19.11.1, within Tag [05AB](https://stacks.math.columbia.edu/tag/05AB), verifies set-sized subobjects when the category is abelian with a generator; that is one sufficient setting, not an inference that completeness alone implies the needed size bound.

### RS06. Enough injectives is a conclusion with two distinct dependencies

**File / scan / lines:** 33; 039:7–12. **Kind:** unproved claim.

The conclusion “has enough injectives” can be compared with the modern theorem for a Grothendieck abelian category, but first the proof must establish the stated abelian/filtered-colimit/generator properties for \(\underline S(X,\underline A)\). A pointwise construction using products of skyscrapers containing injective stalk objects also requires that the stalk tests detect monomorphisms; Kleisli and Wu (1964, pp. 420–422) isolate this issue in extending their argument to general coefficient categories. Thus the failed fullness statement of RS01 should not be used to reject this independent conclusion, and the latter should not be accepted merely from the word “generator.”

**Context:** RS06 found no exact same-point claim in the supplied context or any matching scan. This adds an independent dependency check to the comparison programme. **Register:** **MPL_33_098-146 §76**, **§78**; no LM4/LM7 status changes.

**Primary comparisons:** Stacks, Theorem 19.11.7, Tag [079H](https://stacks.math.columbia.edu/tag/079H); Kleisli and Wu (1964), pp. 420–422.

### RS07. Gray's Columbia mimeograph is a retrieval lead, not an attribution

**File / scans / lines:** 33; 039, 041, 043, 045, English typescript throughout. **Kind:** own idea.

Kleisli and Wu's bibliography (1964, p. 423, reference 5) names a mimeographed Columbia text by J. W. Gray on category-valued sheaves, and their preceding discussion uses the same unusual combination of perfection and small-object assumptions. That makes the mimeograph a specific source to retrieve and collate against the four leaves' numbering and wording. Neither the accessible reference nor similarity of terminology identifies these pages as Gray's text, and no authorship or date has been inserted into the transcription.

**Confidence:** low for source identity; the bibliographic lead is verified, but no exact textual match has been obtained.

**Context:** RS07 found no Gray/Kleisli/Wu/mimeograph match. `same_cote_33/MPL_33_098-146_notes.md`, N42 (scan099) and N56 (scans101–121 and 125–143), likewise distinguish reused-source evidence from unverified bibliographic candidates; this adds a new candidate, not an established identification. **Register:** **MPL_33_098-146 §1**, **§76** as scope and comparison records.

**Primary comparison:** Kleisli and Wu (1964), p. 423, reference 5. Gray's 1962 and 1965 publications were searched, but accessible full text sufficient for collation was not obtained.

### RS08. A separation question survives on the cancelled filtered-module source

**File / scan / lines:** 33; 047:3–5. **Kind:** self-flagged: a step the source itself marks as unverified.

The opening continuation says “Nous ignorons s'il en est encore ainsi (sans hypothèse de séparation) pour \(n\) quelconque,” concerning an implication labeled b)\(\Rightarrow\)c), and separately denies the converse without separation, even for \(n=1\). The definitions of b) and c) are absent from this leaf, so neither implication can be reconstructed safely from the topic or assigned an exact modern regularity criterion. This is an explicit question in a cancelled/reused source, not proof that the handwritten author's current programme contained the same open problem or that cancellation mathematically retracted it.

**Context:** RS08 found no exact matching question, section 19.6, or reference 0,15.1.12 in the context. `same_cote_33/MPL_33_098-146_notes.md`, N55 and its self-flagged index S14 (scan145), concern a different incomplete reused source; this adds another source-dependent item. **Register:** bears directly on **MPL_33_098-146 §65** as an extension of the self-flagged-step inventory, without upgrading any previous lead.

**Evidence:** Frozen scan047; recovery of its preceding source page is the necessary next step.

### RS09. The two filtrations differ even in the simplest Noetherian example

**File / scan / lines:** 33; 047:10–31. **Kind:** own idea.

The warning that \(R''_k\subset R'_k\) but the filtrations are generally distinct has the elementary test \(A=k[t]\), \(N=A\), \(R=tA\), \(J=(t)\), \(N_0=A\), and \(N_k=0\) for \(k\geq1\). Then \(N'_k=t^kA\), while \(R'_k=t^kA\) and \(R''_k=t^{k+1}A\) for every \(k\geq1\). The inclusion \(R\hookrightarrow N\) induces the zero map in every graded degree if \(R\) is given \(R''\), whereas the induced filtration \(R'\) gives the exact graded row printed on the leaf; hence replacing the two filtrations by one would lose substantive information.

**Confidence:** high; all submodules and graded maps are computed explicitly, with no Noetherian approximation or separation argument required.

**Context:** RS09 found no exact filtration/Artin–Rees match in the supplied material. The local-algebra notes N50–N51 in `same_cote_33/MPL_33_098-146_notes.md` (scan135) concern different regular-local and completeness assertions, not this filtration comparison; the new example adds a separate local-algebra issue. **Register:** **MPL_33_098-146 §76** as an additional comparison strand; no substantive register row settles it.

**Primary comparison:** Stacks, Lemma 12.19.12, Tag [05SP](https://stacks.math.columbia.edu/tag/05SP), validates the exact graded sequence with induced and quotient filtrations; the polynomial-ring test is ours.

### RS10. The filtration defect has a Tor interpretation, while Artin–Rees gives cofinality

**File / scan / lines:** 33; 047:18–35. **Kind:** own idea.

For the original filtration concentrated in degree zero and an exact sequence \(0\to R\to N\to M\to0\) with \(N\) flat, the tensor long exact sequence identifies
\[
(R\cap J^kN)/J^kR\cong\operatorname{Tor}_1^A(A/J^k,M),
\]
so the difference between \(R'_k\) and \(R''_k\) measures an explicit failure of left exactness. If one additionally assumes \(A\) Noetherian and \(N\) finite, Artin–Rees makes the induced and \(J\)-adic filtrations cofinal, but does not make them equal in each degree, as RS09 already shows. These are useful separate tests for the later regularity criteria: a Tor-vanishing condition can force equality, whereas completion arguments generally require only cofinality.

**Confidence:** high under the displayed extra assumptions; the first statement is the boundary map for tensoring the given short exact sequence, and the second uses exactly the hypotheses of the cited Artin–Rees theorem.

**Context:** RS10 found no exact strictness/Artin–Rees or induced-filtration match. `same_cote_33/MPL_33_098-146_notes.md`, N44 (scans109,111 and 126–136), proposes a different finite-resolution/Tor comparison; this adds a kernel-level obstruction and does not establish that proposed trace/multiplicity link. **Register:** **MPL_33_098-146 §76**; the finite-complex entries **N25** and **N40** do not settle this filtration problem.

**Primary comparisons:** Stacks, §10.75, Lemmas 10.75.2 and 10.75.8, Tag [00LY](https://stacks.math.columbia.edu/tag/00LY); Lemma 10.51.2, Tag [00IN](https://stacks.math.columbia.edu/tag/00IN). The quotient identification is our application of the former.

### RS11. An invisible divisible summand illustrates the separation issue

**File / scan / lines:** 33; 047:5, in relation to the filtration discussion. **Kind:** own idea.

As a test mechanism rather than an identification of the missing b)/c) conditions, let \(A=k[t]\), \(D=k[t,t^{-1}]/k[t]\), and \(M=A\oplus D\). Since \(tD=D\), the \(t\)-adic associated graded module of \(M\) is \(k[T]\), and the natural polynomial map from \((M/tM)[T]\) is an isomorphism, yet multiplication by \(t\) on \(M\) kills the nonzero class of \(t^{-1}\) in \(D\). The obstruction lies in the nonseparated part \(\bigcap_{n\geq0}t^nM=D\); the example explains why graded information can miss torsion without resolving the source's unidentified implication.

**Confidence:** high for the calculation; unresolved correspondence with the labels b) and c), which have not been recovered.

**Context:** RS11 found no exact nonseparation/quasi-regularity match. N50–N51 in `same_cote_33/MPL_33_098-146_notes.md`, scan135, test other missing scope conditions and provide only a methodological parallel; this adds a distinct separation example. **Register:** **MPL_33_098-146 N54** and **§76** only as the literal-scope testing/comparison method, not as substantive prior solutions.

**Evidence:** Direct module calculation supplied here; no novelty or historical priority is claimed.

### RS12. Source pagination and a precise EGA comparison target

**File / scans / lines:** 33; 039:2,31; 041:2,29; 043:2,42; 045:2,25; 047:2,4,8,20,33. **Kind:** reading question.

The English leaves carry printed numbers 40, 34, 38, 39 in scan order 039, 041, 043, 045, while their separate handwritten numbers are 38, 40, 42, 44; scan047 carries handwritten 46 and the source header `-- IV--1007 --`. The numbered section 19.6 and formulas 19.6.1–19.6.2 give a precise target for comparison with EGA IV's fourth part, but exact collation with the published section was not completed because the retrieved primary PDF exceeded the reading service's size limit. None of these isolated source page numbers is a stated page total, and the title alteration `quotient` deleted / `filtré` inserted must remain a fact of this leaf rather than being normalized from a later edition.

**Context:** RS12 found no exact matching printed-number sequence or section in the supplied context. `same_cote_33/MPL_33_098-146_notes.md`, T07 (scans101–121) and T08 (scans099,123,125–143,145), already distinguish source pagination from totals; this adds a further independent numbering stream. **Register:** **MPL_33_098-146 §1**, **§76**; no chronology or source identity is upgraded.

**Primary locator:** Grothendieck (1967), EGA IV, fourth part, bibliographic record at [Numdam](https://www.numdam.org/item/PMIHES_1967__32__5_0/), DOI 10.1007/BF02732123. The section locator is a research target; this metadata alone does not verify a word-for-word match.

## Verification details for the main counterexample

The Sierpiński computation is completely internal to elementary category theory. Let \(s\) be the closed point and \(\eta\) the open point. Every cover of \(X\) contains \(X\), so an abelian sheaf is specified by its single nontrivial restriction \(r:A=F(X)\to B=F(\{\eta\})\), with zero value on the empty open; its stalks are \(F_s=A\) and \(F_\eta=B\). Consequently
\[
P_XF(X)=A\oplus B,\qquad
P_XF(\{\eta\})=B,\qquad
\operatorname{res}=\operatorname{pr}_B.
\]

For \(F'=(A'\to B')\), a natural transformation is a pair \(u:A\oplus B\to A'\oplus B'\), \(v:B\to B'\) satisfying
\[
\operatorname{pr}_{B'}u=v\operatorname{pr}_B.
\]
Writing \(u\) as a matrix yields \(u=\left(\begin{smallmatrix}a&b\\0&d\end{smallmatrix}\right)\), \(v=d\), with no further condition on \(b\). Thus the claimed coordinatewise map is injective but not surjective whenever \(\operatorname{Hom}(B,A')\ne0\).

For \(F=F'=(\mathbb Z\xrightarrow{1}\mathbb Z)\), the unit on global sections is \(m\mapsto(m,m)\). Applying the typescript's proposed reverse construction, with its source index repaired only for this mathematical test, to \(u(m,n)=(m+n,n)\) produces multiplication by 2 at \(s\) and the identity at \(\eta\). Returning by the coordinatewise construction gives \((m,n)\mapsto(2m,n)\), which differs from \(u\), for example at \((0,1)\). Taking \(F=F'\) also shows that the substantive failure persists even if the \(\rho_{F'}\) index in the frozen text is left as written.

The counterexample does not affect the elementary monomorphism argument for faithfulness in scan043:25–34. Nor does it refute the existence or exactness of ordinary sheafification. Those assertions have separate hypotheses and proofs, as recorded in RS04–RS06.

## Per-item context searches

The exact and thematic queries, files searched, and every returned matching line are saved in `research_reused_sheaves_context_search.json`. Each item was searched against all of:

- `context/README.md`;
- `context/notes/RESULTS_STATE.md`;
- `context/same_cote_33/MPL_33_098-146_notes.md`.

The final exact-term queries returned no same-point matches for RS01–RS12. The context links above therefore explicitly identify thematic parallels and their scan loci rather than pretending that another package proved the new item. The README's earlier statement that no prior material was included is superseded by its dated additions listing the results register and same-cote notes; both additions were read.

## Verified primary sources and locators

| Key | Exact URL | Verified locator | Claim supported / limit |
|---|---|---|---|
| S1 | https://stacks.math.columbia.edu/tag/009C | Lemma 6.27.3 | The stalk–skyscraper adjunction, including its abelian-group and module versions. |
| S2 | https://stacks.math.columbia.edu/tag/009B | Lemma 6.27.2 | A skyscraper's stalk at another point depends on specialization; it need not vanish away from its named point. |
| S3 | https://stacks.math.columbia.edu/tag/03CM | §18.3; Lemmas 18.3.1–2 and their proofs | Abelian sheaves, the associated-sheaf adjunction, kernels/cokernels, and the ordinary abelian-valued baseline. |
| S4 | https://stacks.math.columbia.edu/tag/03CO | Lemma 18.3.2 | Limits, colimits via sheafification, and exact filtered colimits for abelian sheaves. |
| S5 | https://stacks.math.columbia.edu/tag/05AB | Lemma 19.11.1 | In an abelian category with a generator, subobjects of a fixed object form a set. |
| S6 | https://stacks.math.columbia.edu/tag/079H | Theorem 19.11.7 | A Grothendieck abelian category has functorial injective embeddings. |
| S7 | https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6AE93F5371402CA9DBFA53470AD0BED1/S0008439500052309a.pdf/on-injective-sheaves.pdf | Printed pp. 420–422; p. 423, reference 5 | Pointwise injective-sheaf argument; the historical additional hypothesis; a verified Gray mimeograph citation, not identification of the archive leaves. |
| S8 | https://stacks.math.columbia.edu/tag/05SP | Lemma 12.19.12 | Exactness of associated graded for induced and quotient filtrations. |
| S9 | https://stacks.math.columbia.edu/tag/00LY | Lemmas 10.75.2, 10.75.8 | The Tor long exact sequence and vanishing of positive Tor for a flat argument. |
| S10 | https://stacks.math.columbia.edu/tag/00IN | Lemma 10.51.2 | Artin–Rees with a Noetherian ring and finite modules; it controls a shifted induced filtration. |
| S11 | https://www.numdam.org/item/PMIHES_1967__32__5_0/ | Bibliographic record | EGA IV, fourth part, 1967, volume 32, pp. 5–361, DOI 10.1007/BF02732123; no full-text collation achieved. |

### APA-style bibliography

Grothendieck, A. (1967). *Éléments de géométrie algébrique IV, quatrième partie*. Publications Mathématiques de l'IHÉS, 32, 5–361. https://doi.org/10.1007/BF02732123

Kleisli, H., & Wu, Y.-C. (1964). On injective sheaves. *Canadian Mathematical Bulletin, 7*(3), 415–423. https://doi.org/10.4153/CMB-1964-040-4

The Stacks Project Authors. (n.d.). *The Stacks Project*. Specific sections and tags are listed above; retrieved November 15, 2026.

### Retrieval limits

The AMS and Project Euclid copies of Gray's 1962 announcement could not be read through the available service, and the publisher endpoint for Gray's 1965 paper returned an access error. EGA IV's fourth-part facsimile was found at Numdam and at the Grothendieck Circle, but exceeded the service's PDF size limit; its primary bibliographic record was verified. No inaccessible theorem statement or exact historical source identification has been treated as established on the strength of a search snippet or a secondary account.
