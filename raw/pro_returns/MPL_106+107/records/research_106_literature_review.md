# Cote 106: section independence and the standard fraction calculus

## Bounded conclusion

**Under the standard Brown cofibrant-object axioms, the modified category of roofs in 106/012–016 has the correct localized Hom-set after taking connected components; in particular, its section-independence criterion is automatic.** The same conclusion holds for cofibrant objects of a CF1–CF4 precofibration category, and the original roof convention of 106/006 also works under these hypotheses. This does **not** identify the manuscript’s incompletely specified “C1–C3” with a modern axiom list, complete its written proof, or establish novelty.

This review used only the frozen transcription and the primary works listed below; no manuscript scan was viewed and no transcription or completed dossier mapping was changed. The mathematical deductions in §§3–5 below are an explicit comparison argument, separate from the manuscript and from the quoted theorem statements.

### Own-idea verification note R106-V1

**Location:** 106/012–016, especially the section criterion at 106/016. **Context:** PATHS A.P1, exact supplied status `claim (return: Proved)`, locator `VII ms.65–74`, in `context/DOSSIER_STATEMENTS_WITH_STATUS.md`; that ID is not selected in RESULTS_STATE. **Selected state lead:** Hua, findings register, `106-section-criterion-span-faithfulness`, status `conjecture (candidate: their search found no reference) | L…`, reported at `context/notes/RESULTS_STATE.md`, line 120, for package scans 010–016; this lead is not a reviewed theorem.

Under explicit CF1–CF4 hypotheses, joint-map cofibrant refinements identify the connected components of the modified strict-roof category with localized Hom-sets. Section independence follows because both section roofs map to one unrestricted roof, and this strict zigzag lifts through those refinements. **Confidence is high for that conditional deduction**, because the finite constructions use only stated factorization, pushout, and two-out-of-three axioms, with the localization universal property checked below. Identification of these sufficient hypotheses with the folder’s literal, incompletely specified C1–C3 remains unestablished, so this verification adds neither an unconditional manuscript theorem nor a novelty claim.

The argument below is the verification appendix for R106-V1.

## 1. What is actually being compared

Fix cofibrant objects \(x,y\), and write a roof as \(x\xrightarrow{a}z\xleftarrow{s}y\); its localization value is \([s]^{-1}[a]\). Morphisms of roofs are **strictly commuting maps of the middle object**, fixing \(x,y\), and connected components mean equivalence under finite zigzags of such morphisms.

| Roof category | Conditions | Location or role |
|---|---|---|
| \(F_0(x,y)\) | \(a\) arbitrary; \(s\in W\cap\mathrm{Cof}\) | Original construction, 106/006; doubt and revision at 106/012 |
| \(F_1(x,y)\) | \(a\in\mathrm{Cof}\); \(s\in W\) | Modified construction, 106/012–016 |
| \(R(x,y)\) | \(a\) arbitrary; \(s\in W\); middle object cofibrant | Auxiliary comparison category only |
| \(J(x,y)\) | \((a,s):x\amalg y\to z\) a cofibration; \(s\in W\) | Auxiliary full subcategory of both \(F_0,F_1\) |

For a middle map \(u:z\to z'\), the equality \(us=s'\) and two-out-of-three force \(u\in W\). Thus imposing “middle maps weak equivalences” adds no restriction to these strictly commuting roof morphisms; this does not say that arbitrary vertical arrows in an unrestricted all-type path construction are automatically weak equivalences.

## 2. Exact literature scope

Rădulescu-Banu’s Theorem 6.4.4 describes localized maps by weak-equivalence denominators and equality by common refinements **up to homotopy**. Theorem 6.4.5 permits numerators and joint maps that are cofibrations, with acyclic-cofibration denominators; its equality criterion still retains a homotopy condition on the numerators (2009, §6.4, pp.77–78). Consequently, those theorem statements should not be paraphrased as already asserting a strictly commuting common refinement of arbitrary roofs.

Horel describes precisely \(F_0\) in his introduction and reports the stronger assertion that its nerve models a localization mapping space; he also discusses composition by pushout (2016, pp.1–2). His introduction points to Cisinski for the version without functorial factorization, whereas Horel’s own partial-Brown-category definition imposes a functorial factorization condition (Definition 2.2 and Remark 2.3). The elementary \(\pi_0\) argument below needs no functorial choices and makes no corresponding nerve-equivalence assertion for \(F_1\).

## 3. Explicit sufficient hypotheses

Work in the cofibrant objects of a CF1–CF4 precofibration category: weak equivalences contain isomorphisms and satisfy two-out-of-three; cofibrations contain isomorphisms and are composition-stable; pushouts along cofibrations exist and preserve cofibrations, including acyclic ones; maps with cofibrant source factor as a cofibration followed by a weak equivalence. Finite coproducts of cofibrant objects are available. This is the standard finite hypothesis set related to Brown’s cofibrant-object axioms by Rădulescu-Banu (2009, Definition 1.1.1 and Proposition 2.1.2); CF5–CF6 and saturation are not used here.

## 4. A strict refinement argument comparing the three roof conventions

Set \(K=x\amalg y\). For an object \(r:K\to z\) of \(R\), factor it as

\[
K\xrightarrow[\mathrm{cof}]{j}Q
 \xrightarrow[\sim]{q}z.
\]

The \(y\)-leg of \(Q\) is a cofibration and is weak by two-out-of-three, so \(Q\in J\), and \(q\) is a strict roof morphism. This replacement stays inside \(F_0\) or \(F_1\) when its target roof belongs to that category.

For a strict roof morphism \(u:z\to z'\), choose such replacements \(Q\to z\) and \(Q'\to z'\). Form \(P=Q\amalg_KQ'\), map \(P\to z'\) using \(uq\) and \(q'\), and factor this map as \(P\hookrightarrow T\xrightarrow{\sim}z'\). Then \(T\in J\), and the induced strict roof morphisms \(Q\to T\leftarrow Q'\) are weak equivalences by two-out-of-three.

Every object is therefore reached from \(J\), and every arrow in a finite connecting zigzag can be replaced by a zigzag in \(J\). It follows directly, without assuming functorial replacements, that all the inclusions induce bijections

\[
\pi_0J\ \cong\ \pi_0F_0\ \cong\ \pi_0R
\qquad\text{and}\qquad
\pi_0J\ \cong\ \pi_0F_1\ \cong\ \pi_0R.
\]

### Why the common component set is the localized Hom-set

For completeness, the ordinary localization conclusion can also be checked without promoting Horel’s stronger mapping-space statement to unlisted hypotheses. Form a category \(H\) with the objects of \(C\) and Hom-sets \(\pi_0F_0(x,y)\); compose roofs by pushout along the backward acyclic cofibration, as in 106/006–008. This is well-defined on components, associative there, and receives \(C\to H\) by \(a\mapsto(a,1)\).

For \(w:x\to y\) in \(W\), factor \((1_y,w):y\amalg x\to y\) as a cofibration \((a,b):y\amalg x\to Q\), followed by \(q:Q\overset{\sim}{\to}y\). Both \(a,b\) are acyclic cofibrations, with \(qa=1_y\) and \(qb=w\), and the roof \((a,b):y\to x\) represents an inverse to \(w\). Indeed, one composite is the roof \((aw,b)\), connected in \(R(x,x)\) to \((w,w)\) by \(q\), while \((1_x,1_x)\to(w,w)\) is induced by \(w\); the other composite has middle object \(Q\amalg_x y\) and collapses to the identity roof using \(q\) and \(1_y\).

The comparison in the preceding paragraph transfers the first connection from \(R\) to \(F_0\). Every functor \(C\to D\) inverting \(W\) then factors uniquely through \(H\), with a roof sent to the inverse of the image of its denominator composed with the image of its numerator. Thus \(H\cong C[W^{-1}]\), and the canonical map

\[
\pi_0F_1(x,y)\longrightarrow
\operatorname{Hom}_{C[W^{-1}]}(x,y)
\]

is bijective, in particular injective. This is a \(\pi_0\)-level verification; it does not establish a weak equivalence between the **nerves** of \(F_0,F_1,R\).

## 5. The manuscript’s section criterion

Let \(w:x\to y\) lie in \(W\), with sections \(i,i':y\to x\). Two-out-of-three makes both sections weak equivalences, so \((1_x,i)\) and \((1_x,i')\) are objects of \(F_1(x,y)\), and their localization values are both \([w]\). The bijection above proves that their connected components agree.

There is also a direct strict-roof witness before using the localization theorem: both roofs map in \(R\) to \((w,1_y)\), by the middle map \(w\). Replacing this short zigzag through the construction of §4 gives a zigzag entirely in \(F_1\), proving exactly the section independence isolated at 106/016. The unmodified roof convention therefore was not invalid under the standard axioms merely because the proposed elementary inverse argument had stalled at 106/010–012.

## 6. Manuscript, Hua, and the Pursuing Stacks context

The frozen 106/002 text names **Brown**, while 106/006 reduces to the case where every object is cofibrant; the axioms labelled C1–C3 are not fully reproduced in this folder. Hua’s findings-register description names **Baues** and compresses the outcome into faithfulness, whereas 106/012–016 records a revision and a final criterion whose verification the author proposes. The safe report is therefore a **standard-theory conditional resolution of the manuscript’s residual question**, not an unconditional theorem under an independently verified literal C1–C3 list and not a novelty claim.

The supplied *Pursuing Stacks* text, `context/ps_chapters_VI_VII/ps6.tex`, §125, pp.530–532 (section headed 13.10), explicitly discusses Baues’s cofibration/fibration categories and then a programme starting from weak equivalences alone. This makes Baues a relevant contextual reading lead but does not override the word Brown at 106/002 or identify the two sets of hypotheses. Root’s separate verification of Brown’s original Proposition 2 (p.424) concerns the fibrant-object, right-fraction calculus in \(\pi C\); dualization supplies a comparison, not evidence that this folder states the same axiom list verbatim.

## References and verification record

Horel, G. (2016). *Brown categories and bicategories* (arXiv:1506.02851v2). arXiv. [Version record](https://arxiv.org/abs/1506.02851v2) — Introduction, pp.1–2; Definition 2.1; Definition 2.2 and Remark 2.3. [Primary PDF consulted](https://arxiv.org/pdf/1506.02851).

Rădulescu-Banu, A. (2009). *Cofibrations in homotopy theory* (arXiv:math/0610009v4). arXiv. [Version record](https://arxiv.org/abs/math/0610009v4) — Definition 1.1.1; Proposition 2.1.2; Theorems 6.4.4–6.4.5, printed pp.77–78 (PDF pages 85–86 counting from 1). [Primary PDF consulted](https://arxiv.org/pdf/math/0610009).

Brown’s original article was checked separately by root, not independently reopened in this review: Brown, K. S. (1973). Abstract homotopy theory and generalized sheaf cohomology. *Transactions of the American Mathematical Society, 186*, 419–458. [Author-hosted primary PDF](https://pi.math.cornell.edu/~kbrown/scan/1973.0186.pdf). Root records a December 1973 volume/title page and a 1974 copyright; Rădulescu-Banu’s bibliography key is `[Bro74]`, while Horel uses `[Bro73]`, so the dating convention must not be silently treated as a second paper.

Web retrievals available to root for reopening: `turn25view0` (Rădulescu-Banu PDF), `turn26view0`/`turn26view1` (Theorems 6.4.4–6.4.5), `turn28view5` (Brown/precofibration comparison), and `turn25view1` (Horel PDF, including introduction and axioms). The proof in §§3–5 is this review’s explicit deduction under stated axioms, and does not depend on the unreviewed companion runs.
