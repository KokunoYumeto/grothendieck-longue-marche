# Research notes: scans 032–039 — support K-theory, covariant Chern characters, and reused étale sheets

Research performed after the parent's transcription freeze, using only the frozen TEX pages and the two supplied context files; no source images were read and no TEX file was edited. The notes below are independent mathematical/literature assessments, not transcription amendments. Search IDs S01–S21 refer to the actual per-note searches in **records/context_search_supports.md**; irrelevant substring hits were checked and rejected.

The supplied **context/notes/RESULTS_STATE.md** reports zero matching own open, settled, intake, returned-package, and planning entries. Its three Hua findings are AI-produced, unchecked leads with intake status “new to us: our package for this cote is waiting”; only the indirect comparison specified in S09 bears on this block. The prose below does not claim novelty or treat that status as mathematical validation.

## Compact notes

### S01 — 033 — Definition distinction; relative versus intrinsic perfection

**Anchor:** “parfaits rel. à f”; $D^\bullet_{\mathrm{parf}}(i_n)$.

Relative perfection for a closed immersion into a Noetherian ambient scheme is tested by the pushed-forward complex, and is not the condition of being perfect intrinsically on the infinitesimal neighbourhood (Alonso Tarrío et al., 2023, Corollary 4.2). Our diagnostic $A=k[t]$, $B_n=A/(t^n)$, $n\ge2$, shows that $k$ is perfect over $A$ but has an infinite periodic free resolution over $B_n$, so substituting $\operatorname{Perf}(Z_n)$ changes the written category. Context check S01 found no relevant object, scan, or entry ID in either context file; confidence in this distinction is high because the two projective dimensions are explicitly calculable (Appendix A).

### S02 — 033 — Unproved assertion; finite-stage Ext test

**Anchor:** “le foncteur est pl. fidèle.”

The assertion concerns the filtered limit, not each $Ri_{n*}$: already $\operatorname{Ext}^1_k(k,k)=0$ whereas $\operatorname{Ext}^1_{k[t]}(k,k)=k$, represented by the nonsplit extension with middle term $k[t]/(t^2)$. At a thicker stage $B_n$, $n\ge2$, the nonzero higher Ext groups also show that the individual derived pushforward need not be faithful, even though their extra classes can die under transition. This is our high-confidence diagnostic of the work the limit must do, not a counterexample to the written limit claim; context search S02 found no relevant result or ID in **context/README.md** or **context/notes/RESULTS_STATE.md**.

### S03 — 033 — Conditional reconstruction of the full-faithfulness claim

**Anchor:** $\operatorname{Lim}_nD^\bullet_{\mathrm{parf}}(i_n)\to D_Z(X)$.

For $X=\operatorname{Spec}A$ with $A$ Noetherian and $Z=V(I)$, our reconstruction gives $\varinjlim_n\operatorname{Ext}^q_{A/I^n}(M,N)\simeq\operatorname{Ext}^q_A(M,N)$ for finite modules killed by powers of $I$, and consequently the expected filtered categorical comparison after restricting to complexes perfect over $A$. The proof uses the equivalence between derived $I$-power torsion modules and complexes with torsion cohomology (Stacks Project, Tags 0955 and 06UP), together with finiteness of the data in bounded complexes and roofs; Appendix B records the actual argument. Confidence is high for this stated affine Noetherian version, but the page's unrestricted “préschéma” formulation, the precise meaning of its categorical limit, and the target notation $D_Z(X)$ require additional conventions before this argument supplies a proof. Context search S03 found no corresponding own entry; the torsion hit **Hua, findings register, 2-chern-ring-not-injective-pn** concerns scan022 and a different Chern-ring problem, so does not settle this statement.

### S04 — 033,035 — Construction condition; families of supports

**Anchor:** “une famille $\Phi$” and the limit over $Z\in\Phi$.

A customary family of supports consists of closed subsets closed under taking closed subsets and finite unions; the latter condition makes the displayed inclusion-indexed limit filtered and permits adding classes carried by different supports. This is a condition to make the proposed construction precise, not a claim that the author intended an arbitrary undirected collection. Context search S04 found no supported-K construction or matching own ID; its “family” and $\varphi$ hits are the unrelated ordinary Chern-ring entries **2-chern-ring-gamma-comparison** (scans021,022,029,030) and **2-chern-ring-not-injective-pn** (scan022), both unchecked Hua leads; confidence in the condition is high by the definition of a filtered support system.

### S05 — 034 — Reused theorem fragment; an essential prior hypothesis

**Anchor:** “surjectif”; “radiciel”; equivalence of étale categories.

The typed argument and its examples match SGA 4, Exposé VIII, §1, whose topological-invariance theorem concerns universal homeomorphisms; a standard precise hypothesis package is integral, universally injective, and surjective (Stacks Project, Tag 04DZ). Our explicit test $D(t)\amalg V(t)\to\mathbb A^1_k$ is radicial and surjective but has disconnected source and connected target, so its small étale topoi cannot be equivalent: integrality cannot simply be dropped. The complete theorem explicitly includes integrality on the preceding source page, SGA 4 VIII, p. 367, so the isolated fragment must not be used to attribute its omission to the full theorem. Context search S05 found no corresponding entry in either context file; confidence is high in the hypothesis distinction and source identification, independently confirmed by the primary reader against original SGA 4 pp. 367–369.

### S06 — 034,036,039 — Source identification and qualified chronology

**Anchor:** “EGA IV 1.9.9”; “Corollaire 5.11”, “5.12”, “5.13”.

The reused typed passages match SGA 4 VIII §1 (034) and VII §§5.11–5.13 (036,039), including the étale-invariance examples and the successive direct-image continuity corollaries, rather than forming additional handwritten Riemann–Roch arguments. **context/README.md** associates the assembled cote with “[1957]” and “antérieur[es à] 1958,” while the typed stratum's explicit EGA IV reference is to material published in 1964 and its SGA 4 counterparts appeared in the 1972 volume (Grothendieck, 1964; Artin et al., 1972). This is strong evidence against applying a single unqualified 1957 date to all the assembled textual layers, but publication dates are not strict dates for manuscripts or circulated drafts, and these comparisons alone date neither the handwriting nor the physical reuse. Search S06 has that README catalogue entry as its only substantive hit, with no research-result ID in **context/notes/RESULTS_STATE.md**; confidence is high in the bibliographic distinction and deliberately limited on physical chronology.

### S07 — 035 — Pseudo-ring; the unit issue is substantive

**Anchor:** “pseudoanneau (pas néc d'élément 1).”

Derived tensor product preserves supported perfect complexes, and the ambient perfect-complex ring acts on their Grothendieck group, while the ambient unit $[\mathcal O_X]$ is unavailable when the allowed supports do not contain $X$. Thus the qualified nonunital language fits the construction and should not be silently replaced by “ring with 1”; the modern localized Chern character also has an explicitly multiplicative supported formulation (Stacks Project, Tag 0FET). Context search S07 found no relevant supported-ring entry in either context file; confidence in this structural explanation is high, without excluding accidental units for special supports such as an open-and-closed component.

### S08 — 035 — Construction ambiguity; rational equivalence with supports

**Anchor:** “en prenant tjrs des cycles sur $X$ à support … $\Phi$.”

The phrase leaves a consequential choice between rational-equivalence data that stay inside the allowed supports and the image of supported cycles in the ordinary Chow group. In our test $X=\mathbb A^1_k$, $Z=\{0\}$, the former gives $CH_0(Z)=\mathbb Z$, whereas the class of $0$ maps to zero in $CH_0(X)$ because it is the divisor of $t$ on $X$. This high-confidence calculation shows that forgetting supports can lose information and that the proposed $A^\bullet_\Phi(X)$ is not determined merely as a subobject of $A^\bullet(X)$; context search S08 found no matching result or ID in the two supplied files.

### S09 — 035 — Explicit open construction; the supported filtration

**Anchor:** “on essaiera de définir … via une filtration sur le $\lambda$-pseudo-anneau $K^\bullet_\Phi(X)$ ??”.

This is expressly a proposed construction: a rigorous version must specify supported exterior operations, a unitization or equivalent convention for $\gamma$-operations, the filtration, and the comparison with cycles, rather than importing the ordinary unital-ring argument unchanged. **context/notes/RESULTS_STATE.md**, search S09, supplies the indirect lead **Hua, findings register, 2-chern-ring-gamma-comparison**, scans021,022,029,030, with unchecked status “new to us … waiting”; that entry concerns geometric elements in an ordinary $\lambda$-ring and proves no supported version here. The rational localized-character homomorphism of Stacks Project Tag 0FET is a concrete later comparison target, but does not by itself establish the integral filtration the page proposes. Confidence is high that the question remains open within these sheets, and medium that the earlier comparison is the most useful route because support and nonunital conventions remain to be fixed.

### S10 — 035 — Explicit self-flagged extension

**Anchor:** “Classes de Chern [cohomologiques|homologiques] ??” (word reading uncertain in the frozen text).

The double question mark marks an additional proposed extension, and the unresolved cohomological/homological reading must not be settled from the expectation of a later theory. Covariant homological characteristic classes and contravariant/operational characteristic classes require distinct targets and functorialities; the eventual bivariant framework connects them without making them interchangeable (Fulton & MacPherson, 1981). Context search S10 found no same-object entry in either context file; confidence is high in the self-flagged status and only moderate in the proposed literature connection.

### S11 — 037 — Explicit doubt; which inverse images have no conditions?

**Anchor:** “images inverses sans conditions (?)”.

Absolute perfect complexes admit arbitrary derived pullback, but that fact does not prove unrestricted base change for the proposed relative perfect categories: the modern bivariant construction uses Tor-independent squares (Alonso Tarrío et al., 2023, Proposition 3.11 and Theorem 6.1). Our test base-changes $\operatorname{Spec}k\to\operatorname{Spec}k[t]$ by $\operatorname{Spec}k[t]/(t^2)\to\operatorname{Spec}k[t]$; $\mathcal O_{\operatorname{Spec}k}$ is perfect relative to the first map and is not perfect relative to the resulting classical fibre map, whose target is the dual numbers. This high-confidence obstruction concerns relative classical base change, not ordinary derived pullback of an absolute perfect complex. Context search S11 found no relevant own entry; incidental “Tor” substring hits in Hua's Chern-ring discussion concern different objects and do not resolve the page's question.

### S12 — 037 — Proposed covariance; why “sans plus” is plausible

**Anchor:** “propreté sur supports (sans plus)” and the displayed equality commuting with $g_*$.

Relative perfection can make proper covariance stronger than covariance of absolute $K^0$: for a proper $g:X\to Y$ between Noetherian schemes over a Noetherian base $S$, $Rg_*$ preserves complexes perfect relative to $S$, without requiring $g$ itself to have finite Tor-dimension (Alonso Tarrío et al., 2023, Proposition 3.5). A later realized analogue is the proper-covariant rational transformation $G_0(X)\to CH_*(X)_{\mathbb Q}$ for quasi-projective schemes, with its module property and smooth Todd normalization (Baum et al., 1975, §0 and Chapter II). This comparison explains the force of the proposal but does not prove every relative, support-indexed assertion in the unfinished sheet; the uncertain word “bivification|homification” remains a reading uncertainty. Search S12 matches only the general Riemann–Roch subject in **context/README.md**, no same-object result ID; confidence is high in the cited mathematics and moderate in identifying the exact intended formalism.

### S13 — 037 — Unfinished canonical-element proposal

**Anchor:** “un élément canonique explicitable”.

One rigorous candidate for the formal map $K^0(X)\to K^0(X\to S)$, when $X\to S$ is locally of finite type between Noetherian schemes and has finite Tor-dimension, is multiplication by the relative orientation $[\mathcal O_X]$ (Alonso Tarrío et al., 2023, §6.9). The Riemann–Roch image of the structure sheaf is a Todd homology class, and in singular situations that class need not come from an ordinary cohomology class capped with the fundamental class (Baum et al., 1975, §0.2 and IV §6). This supplies a candidate interpretation rather than an identification of the unfinished “canonical element,” and does not establish an integral $K^0$-preimage of any desired Todd factor; confidence is high for the formal distinction and low-to-medium for its identification with this fragment. Context search S13 found no relevant entry in either supplied context file.

### S14 — 038 — Hypothesis-sensitive comparison; regular ambient scheme

**Anchor:** the four vertical labels “iso si $X'$ rég.”.

For a Noetherian regular ambient scheme $X'$, bounded coherent complexes on $X'$ are perfect, giving the expected perfect/coherent comparison, also after imposing cohomological support (Stacks Project, Tag 08E0). The thickenings $X_n$ themselves can be singular, so the left-hand relative-perfect categories should still not be replaced by intrinsically perfect complexes on $X_n$; the example in S01 tests exactly this distinction. Confidence is high for this Noetherian interpretation, while the diagram by itself does not prove the comparison under every prescheme convention. Context search S14 found no related result or ID in either context file.

### S15 — 038 — Coherent dévissage; stronger than the written surjectivity label

**Anchor:** $K_\bullet(X_0)\to\varinjlim K_\bullet(X_n)$, “surj. si $X'$ rég.”.

If the lower groups are coherent Grothendieck groups and $X'$ is Noetherian, nilpotent dévissage makes each thickening pushforward $G_0(X_0)\to G_0(X_n)$ an isomorphism, and also identifies $G_0(X_0)$ with the coherent group supported on $X$ inside $X'$; ambient regularity is unnecessary for this lower-row statement (Quillen, 1973, §5, Theorem 4, and §7.3, Propositions 3.1–3.2). The finite ideal-adic filtration supplies the dévissage, while regularity is needed for the passage to the upper perfect groups, not for the filtration itself. Search S15 found only the unrelated “surjectivity” in **Hua, findings register, 2-chern-ring-gamma-comparison** (scans021,022,029,030; unchecked), not a matching own result. Confidence is high under the explicit Noetherian/coherent interpretation; this is a conditional strengthening, not a transcription correction.

### S16 — 038 — Withdrawn arrows and distinct forget-support map

**Anchor:** cancelled $v'$-arrows; live $w'v'=\mathrm{id}$, $v'w'=\mathrm{id}$.

The frozen diagram cancels the diagonal $v'$ and the lower return $v'$, while leaving the two inverse identities written below; this is drafting evidence, not a completed construction of the cancelled arrows. The lower isomorphism from the limit of thickening groups to the supported coherent group must also be distinguished from the other $w'$, the rightmost map forgetting supports. Our high-confidence test $Z=\{0\}\subset\mathbb A^1_k$ sends the nonzero generator of $G_0(Z)$ to zero in $G_0(\mathbb A^1_k)$ by $0\to\mathcal O\xrightarrow{t}\mathcal O\to k\to0$, so no inverse assertion should be transferred to that rightmost map. Context search S16 found no relevant entry in either supplied context file.

### S17 — 038 — Supported Riemann–Roch expression

**Anchor:** $\operatorname{ch}(i_!x)\operatorname{Todd}(X'/S)$.

For an embedding into a smooth ambient variety, the later singular Riemann–Roch construction combines the localized Chern character of an ambient resolution with the ambient Todd class to obtain a class on the support, and proves independence and proper covariance (Baum et al., 1975, I §6 and II §3). This makes the displayed expression a precise research lead, but the ordinary ambient Chern character alone can lose the supported class, as S08 and S16 demonstrate; a localized character supplies the missing supported target (Stacks Project, Tags 0FB0 and 0FET). Confidence is high in this comparison under its smooth-ambient, field, and rational-coefficient hypotheses, but it does not establish the sheet's unrestricted relative formulation. Context search S17 found no same-object result or ID in either context file.

### S18 — 036,039 — Reused continuity statements; scope of hypotheses

**Anchor:** “morphismes de transition affines”; “quasi-compacts et quasi-séparés”.

These are étale direct-image continuity statements: in the abelian-sheaf case, filtered limits with affine transitions and quasi-compact, quasi-separated structural morphisms admit the indicated comparison of higher direct images, including the variant formed from an arbitrary sheaf on the limit (Stacks Project, Tag 03Q4, Lemmas 59.51.8–59.51.10). The visible revisions replace a single base-change system by two compatible inverse systems, which is a substantive generalization already encompassed by that modern statement. The frozen text marks these reused bodies as cancelled, so they should be identified as a separate source layer rather than adopted as live Riemann–Roch claims. Context search S18 found no matching result or ID; confidence is high in the mathematical comparison and source identification, independently confirmed by the primary reader against original SGA 4 VII, pp. 363–364.

### S19 — 036,039 — Type mismatch; retain the written projection letters

**Anchor:** scan036 $u_i^*(R^nf_{i*}F_i)$, with $u_i:X\to X_i$; scan039 $v_i^*(R^nf_{i*}(u_{i*}F))$, with $v_i:Y\to Y_i$.

The sheaf $R^nf_{i*}F_i$ lives on $Y_i$, so its pullback to $Y$ requires the $Y$-projection, called $v_i$ in039; the $u_i$ explicitly defined in036 has the wrong source and target for that operation. Likewise,036's proof says the question is local on $X_{i_0}$ immediately before making $Y_{i_0}$ affine, which warrants a separate locality-label check. Direct visual collation shows that SGA 4 VII, p. 364, retains the same $u_i$ display mismatch but reads $Y_{i_0}$ in the proof; these are high-confidence type diagnostics, also supported by the well-typed modern formulation in Stacks Project Tag 03Q4, and do not authorize changing the frozen readings. Context search S19 found no related entry in either file.

### S20 — 036 — Nontrivial warning; group schemes versus inverse-image sheaves

**Anchor:** “n'est pas un cas particulier”; “au sens du changement de base pour les préschémas”.

The warning is mathematically substantive because base change of a group scheme and inverse image of its associated sheaf on the small étale site need not coincide. Our example takes algebraically closed $k$, $K=k(t)$, and $\mathbb G_m$: the small étale sheaf over $k$ is the constant sheaf $k^\times$, whose inverse image to connected $\operatorname{Spec}K$ still has global sections $k^\times$, whereas the base-changed group scheme has sections $K^\times$. Confidence is high in this explicit distinction, so the printed warning should be retained even where theorem numbers are in revision. Context search S20 found no corresponding result or ID in the supplied files.

### S21 — 032 — Cover/title record

**Anchor:** “Caractères de Chern covariants” and “à supports”.

The cover announces the support/covariance block, while the exact $K$- and $A$-superscript readings remain uncertain in the frozen text. Its marginal “31” is a written number, not a stated count of the ensuing pages, and no page count should be manufactured. Context search S21 found only the cote-level title/date in **context/README.md**, not a specific result or ID in **context/notes/RESULTS_STATE.md**; confidence is high in this bounded title-sheet assessment.

## Appendix A — Explicit diagnostic calculations (our analysis, not manuscript claims)

### Relative versus intrinsic perfection and finite-stage Ext

Let $A=k[t]$, $B_n=A/(t^n)$, $n\ge2$, and $M=k$. The resolution
\[
0\longrightarrow A\xrightarrow{t}A\longrightarrow k\longrightarrow0
\]
shows that $k$ is $A$-perfect. Over $B_n$, the resolution
\[
\cdots\xrightarrow{t}B_n\xrightarrow{t^{n-1}}B_n
\xrightarrow{t}B_n\longrightarrow k\longrightarrow0
\]
is exact because the annihilators of $t$ and $t^{n-1}$ are respectively $(t^{n-1})$ and $(t)$. Applying $\operatorname{Hom}_{B_n}(-,k)$ gives zero differentials, hence $\operatorname{Ext}^q_{B_n}(k,k)=k$ for every $q\ge0$, whereas $\operatorname{Ext}^q_A(k,k)=0$ for $q\ge2$. This proves both the relative/intrinsic distinction and the failure of faithfulness at a thickened finite stage.

For $m>n$, a comparison from the $B_m$-resolution to the $B_n$-resolution has component $t^{m-n}$ in degree two, so the induced transition on $\operatorname{Ext}^2(k,k)$ is zero. In degree one the comparison is reduction, so the nontrivial extension class persists. This small example illustrates how the filtered limit can remove false higher extensions while recovering the ambient degree-one extension.

### Surjective radicial does not suffice

The morphism
\[
\operatorname{Spec}k[t,t^{-1}]\amalg\operatorname{Spec}k
\longrightarrow\operatorname{Spec}k[t]
\]
is surjective and remains injective on points after every base change, because its two pieces become the complementary open $D(t)$ and closed $V(t)$. Its source has two connected components and its target one; the constant finite étale sheaf $\mathbb Z/2$ therefore has four global sections on the source and two on the target. The map is not a universal homeomorphism and is not integral. This is a diagnostic of an omitted hypothesis if one reads the fragment in isolation, not a refutation of the complete SGA theorem.

### Classical base change of relative perfection

Base-changing $k[t]\to k$ along $k[t]\to k[t]/(t^2)$ gives $k[t]/(t^2)\to k$. The object $k$ has finite Tor-dimension over $k[t]$, but the periodic resolution above shows infinite Tor-dimension over $k[t]/(t^2)$. This is the obstruction in S11.

## Appendix B — Affine Noetherian repair of the categorical-limit claim (our analysis)

Assume $A$ Noetherian, $I\subset A$, and let $\mathcal T$ be the abelian category of all $I$-power-torsion $A$-modules, with $\mathcal C\subset\mathcal T$ its finite modules. The Noetherian torsion comparison identifies $D(\mathcal T)$ with the full subcategory of $D(A)$ whose cohomology is $I$-power torsion (Stacks Project, Tag 0955).

The subcategory $\mathcal C$ is Serre in $\mathcal T$. Given a surjection $T\to M$ with $M$ finite, choose lifts of finitely many generators; their $A$-span is a finite torsion submodule still surjecting onto $M$. Thus the criterion of Stacks Project Lemma 13.17.4 (Tag 06UP) gives the fully faithful bounded derived comparison, indeed an equivalence onto bounded complexes with finite torsion cohomology.

Each bounded complex in $\mathcal C$ has every term killed by one common power $I^n$. A roof representing a morphism in its bounded derived category, and the finite data witnessing equality of two roofs, also involve finitely many finite torsion modules, hence lie over some $A/I^m$. Therefore the filtered categorical colimit of $D^b(\operatorname{mod}_{fg}(A/I^n))$, using restriction of scalars, identifies with $D^b(\mathcal C)$. For finite torsion $M,N$, this gives
\[
\varinjlim_{n\gg0}\operatorname{Ext}^q_{A/I^n}(M,N)
 \;\cong\; \operatorname{Ext}^q_A(M,N).
\]

Restrict to objects whose image in $D(A)$ is perfect. For the Noetherian closed immersions $i_n:\operatorname{Spec}(A/I^n)\to\operatorname{Spec}A$, these are exactly the relatively perfect objects under the usual definition. The same finite-roof argument restricts because quasi-isomorphic roofs retain perfection over $A$, yielding an equivalence with $\operatorname{Perf}_{V(I)}(A)$, provided this is the intended target. The proof establishes an explicitly hypothesized affine version; it neither defines every notation in scan033 nor supplies a global non-Noetherian proof.

## Appendix C — Coherent dévissage in scan038 (our analysis)

For a Noetherian $X'$ and a coherent sheaf $F$ set-theoretically supported on the closed subscheme cut out by $\mathcal I$, some power $\mathcal I^N$ annihilates $F$. The finite filtration $F\supset\mathcal IF\supset\cdots\supset\mathcal I^NF=0$ has quotients killed by $\mathcal I$, so they come from coherent sheaves on the closed subscheme. Quillen's dévissage theorem applies to the full subcategory of objects killed by $\mathcal I$, which is closed under subobjects, quotients, and finite sums, and proves the isomorphism of coherent Grothendieck groups; the formula $[F]=\sum_j[\mathcal I^jF/\mathcal I^{j+1}F]$ alone would show generation but not all relations. This separates genuine dévissage from the unsupported inference “every object has a filtration, therefore every derived morphism is already represented on the reduced subscheme.”

## Primary-source references (APA; evidence history)

- Alonso Tarrío, L., Jeremías López, A., & Sancho de Salas, F. (2023). Relative perfect complexes. *Mathematische Zeitschrift, 304*, Article 42. https://doi.org/10.1007/s00209-023-03294-7 . Author preprint: https://arxiv.org/pdf/2112.09680 . Consulted Definition 3.1, Corollary 4.2, Propositions 3.5 and 3.11, Theorem 6.1, and §6.9.
- Artin, M., Grothendieck, A., & Verdier, J.-L. (Eds.). (1972). *Théorie des topos et cohomologie étale des schémas, Tome 2 (SGA 4)* (Lecture Notes in Mathematics, Vol. 270). Springer. https://doi.org/10.1007/BFb0061319 . Original Exposé VII: https://fabrice.orgogozo.perso.math.cnrs.fr/SGA4/originaux/SGA4-VIIo.pdf ; original Exposé VIII: https://fabrice.orgogozo.perso.math.cnrs.fr/SGA4/originaux/SGA4-VIIIo.pdf ; primary archive index: https://fabrice.orgogozo.perso.math.cnrs.fr/SGA4/ . Indexed searches provided indexed original text matching the frozen sheets; **direct PDF opening failed**, and no original page images were inspected by this agent. The complete SLMath original is https://library.slmath.org/nonmsri/sga/sga/pdf/sga4-2.pdf , but the web tool rejected its approximately 30 MB size; no local copy was successfully obtained. The primary reader subsequently downloaded and visually inspected the original SLMath pages 363–365 and 367–369, confirming the source identification and the distinctions in S05, S18 and S19; original page URLs follow the pattern https://library.slmath.org/nonmsri/sga/sga/4-2/4-2t_364.jpeg .
- Baum, P., Fulton, W., & MacPherson, R. (1975). Riemann–Roch for singular varieties. *Publications Mathématiques de l'IHÉS, 45*, 101–145. https://doi.org/10.1007/BF02684299 . Original: https://www.numdam.org/article/PMIHES_1975__45__101_0.pdf . Consulted §0, I §6, II §3, and the stated IV §6 obstruction.
- Fulton, W., & MacPherson, R. (1981). *Categorical framework for the study of singular spaces*. *Memoirs of the American Mathematical Society, 31*(243). https://doi.org/10.1090/memo/0243 . Publisher metadata and contents consulted, not the full proof text; used only to identify the bivariant framework.
- Grothendieck, A. (1964). Éléments de géométrie algébrique: IV. Étude locale des schémas et des morphismes de schémas, Première partie. *Publications Mathématiques de l'IHÉS, 20*, 5–259. https://doi.org/10.1007/BF02684747 . Official record: https://archive.numdam.org/articles/10.1007/BF02684747/ . Consulted bibliographic chronology, not an argument that publication date strictly dates a draft.
- Quillen, D. (1973). Higher algebraic K-theory: I. In H. Bass (Ed.), *Algebraic K-theory I: Higher K-theories* (Lecture Notes in Mathematics, Vol. 341, pp. 85–147). Springer. https://doi.org/10.1007/BFb0067053 . Original article copy: https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Quillen-Higher-I.pdf . Consulted §5, Theorem 4, and §7.3, Propositions 3.1–3.2.
- The Stacks Project Authors. (n.d.). *The Stacks Project*. Retrieved November 16, 2026, from the tags below; each tag is a primary maintained statement, not a claim about historical priority.

| Tag / section | Use | Exact URL  |
|---|---|---|
| 06UP, §13.17, Lemma 13.17.4 | Derived comparison for a Serre subcategory | https://stacks.math.columbia.edu/tag/06UP  |
| 08E0, §36.11 | Coherent derived category and regularity/perfection | https://stacks.math.columbia.edu/tag/08E0  |
| 0G7F, §36.6 | Cohomological support convention | https://stacks.math.columbia.edu/tag/0G7F  |
| 0BJA, §47.8 | Derived torsion; warning outside Noetherian setting | https://stacks.math.columbia.edu/tag/0BJA  |
| 0955, Lemma 47.10.1 | Noetherian derived torsion equivalence | https://stacks.math.columbia.edu/tag/0955  |
| 04DZ, Theorem 59.45.2 | Étale invariance under integral, radicial, surjective maps | https://stacks.math.columbia.edu/tag/04DZ  |
| 03Q4, §59.51 | Continuity and higher direct images | https://stacks.math.columbia.edu/tag/03Q4  |
| 0B75, §42.33 | Bivariant Chow targets and variance | https://stacks.math.columbia.edu/tag/0B75  |
| 0FB0, §42.50 | Localized Chern classes | https://stacks.math.columbia.edu/tag/0FB0  |
| 0FET, Remark 42.56.11 | Rational localized character on supported perfect K-theory | https://stacks.math.columbia.edu/tag/0FET  |

## Completion checks

- Frozen pages read: 032–039 only for this task; TEX unchanged.
- Context read and searched: only context/README.md and context/notes/RESULTS_STATE.md, after freeze.
- Images: none opened, neither manuscript scans nor SGA screenshots.
- Own calculations explicitly labelled and hypothesis-bounded; no novelty claim.
- Source-identification history: this reviewer initially used indexed original-PDF extracts; the primary reader subsequently performed the independent visual collation recorded above.
