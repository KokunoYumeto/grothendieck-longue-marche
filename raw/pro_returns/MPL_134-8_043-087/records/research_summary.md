## Findings and guide to the registers

The principal addition of these leaves is a detailed working argument around the localized linearization question in *Pursuing Stacks* VII §134, pp.557–560. Scan 049 marks its proposed equivalence `W_{\mathcal M}^{-1}\mathcal M\to\mathrm D_\bullet(Ab_k)` “Thm(?)”; scans 048–059 supply tensor-acyclic interval assumptions, a resolving adjunction, counit tests, and the explicit bicomplex proof on scan 054. The source continues to mark projectivity, descent of adjunction, and preservation of acyclic complexes as questions or unfinished steps, so the contribution includes both substantial calculations and a visible record of what remained to be checked. [Current witnesses: R004–R035; supplied typescript: `ps7.tex`, §§134–135; RESULTS_STATE leads: GALOIS G.6, RESIDUE I.7.]

The later leaves develop coefficient change, duality, and augmentation adjoints through the actual functors `Hom(a,-)`, `\kappa_!`, `\kappa^*`, and `\kappa_*`. These formulas can be compared directly with the typescript's correction of the existence of `f_!` in §138, p.586 and its rejection of a constant-resolution shortcut in §139, pp.588–589. Scan 077 adds a finite-projective module example and explicit unit/counit rank tests; scans 081, 084 and 086 return to the interval construction and end with a questioned lift and an `Ext^1` condition. [Current witnesses: R044–R074; supplied typescript: `ps7.tex`, §§138–139; RESULTS_STATE leads: GALOIS G.6, RESIDUE I.7, IMPL I1/P1.]

Scan 074 also contains a particularly close comparison with *Pursuing Stacks* VI §119, pp.501–503: the handwritten leaf writes `P(a+b)=P(a)+P(b)+ab`, while the typescript writes `P(a+a')=P(a)+P(a')+aa'`. Identifying the handwritten variable `b` with the typescript variable `a'` gives the same displayed equation in their truncated-power-series calculations. The handwritten product line contains an uncertain `P_n(t)` and an inserted `P`; its full frozen form is retained in R059, while the clean product formula is cited as the typescript's formula. [Current witnesses: R059 and R082; supplied typescript: `ps6.tex`, §§119–120.]

### H1 — Strong W(7): earliest explicit supplied-context witness located; reading question

No statement of strong W(7) or W(7 bis) was located in the current 44-scan range; the explicit definition located in the supplied companion is **DER XII §V.2.1, manuscript pp.75–76, printed p.55**, where the two opposite cover-square inclusions satisfy the written biconditional `(U∩U′→U′)∈W ⇔ (U→X)∈W`. The cube formulation follows at **manuscript pp.76–77, printed p.56**, and Théorème 2 at **manuscript p.78, printed p.57** asserts it for `W_∞` with the admission “Je n'ai pas écrit la vérification en forme”. The context records a checked refutation of this strong assertion under NEW_RESULTS 8/TOTASPH A.13, while the fuller axiom and counterexample comparisons appear in PS37–PS39 below. [Source: `companion/chunks/DER_XIIb-a.tex`; state control: RESULTS_STATE TOTASPH A.9 and POLES B.2/G.5; A.13 review reported in NEW_RESULTS 8.]

### H2 — Total asphericity and filteredness: first question and renewed conjecture located; reading question

The first located explicit question in the supplied companion is **DER II §2, manuscript p.36, printed p.21**, “cela implique-t-il que X soit filtrante ?”, followed by the renewed displayed conjecture at **manuscript p.36ter, printed p.23**, after the retracted Proposition 2.19 and its inserted counterexample. Current scan 058 says “i.e. J est tot asph.” after tensor-acyclicity tests; its written objects and comparison maps are recorded separately in R032–R034 and PS15/PS42. RESULTS_STATE TOTASPH C.10 and NEW_RESULTS 11 record the checked counterexample claim to categorical filteredness, while TOTASPH D.7/RESIDUE F.5 keep the remaining exact-colimit direction open. [Source: `companion/chunks/DER_II-a.tex`, manuscript pp.36–36ter; current witness: scan 058.]

### H3 — Witness order and calendar chronology; reading question

These “first located” findings concern the searched supplied witnesses and their manuscript order, not a calendar priority claim: the inserted II material refers forward to XII and XVI. The catalogue dates the annotated *Pursuing Stacks* typescript but calls the handwritten leaves undated, and the 1982 printer dates and yearless August copying instruction do not identify a date for each handwritten calculation. The surviving source order, visible page numbers, and separate layers of correction are therefore recorded without assigning a date of anticipation or revision to an individual leaf. [Sources: context `README.md`; `DER_II-a.tex`, manuscript pp.36bis–36ter; current scans 043, 047, 056, 059, 062, 064, 072–074; PS01/PS43.]

### H4 — The planning question about relative Theorem A in 1983; reading question

The context README assigns that broader question to archive cotes **117 and 118**, which are outside the present supplied scan range. Within cote 134-8, scan 068 writes a slice-homology comparison and scan 075 gives an augmented-additive implication network, explicitly naming a resolution argument for objects of `N^{\unsure{\flat|b}}` by sums of objects of `N`; those are the concrete forms located here. They should be compared with the supplied typescript's functorial homology formulas in VII §135, pp.561–564, and with RESULTS_STATE GALOIS B.1/B.3/D.2, but this packet does not supply a full witness answering the question for cotes 117–118. [Current witnesses: R048, R055, R060–R064; source: context `README.md`, planning question.]

### Coverage guide

| Register | Coverage and purpose |
|---|---|
| Main notes R001–R082 | Individual manuscript questions, claims, proof fragments, comparisons, reading questions, and explicitly labelled research actions or calculations. |
| Standing sections | Every literal source question-mark row, additional explicit unfinished steps, material revisions, titles, page references, and both pagination systems. |
| PS01–PS45 | Leaf-cluster comparison with the supplied *Pursuing Stacks* text, including the historical witnesses and chronology limits. |
| NEW_RESULTS 1–12 and K1–K3 | Every numbered result and all three closing attributions, with reported review status and a bounded current-page mapping. |
| Open-state 1–26 | Every open RESULTS_STATE entry, including the two candidate-prompt items; no status is silently changed. |
| Dossier STRATA/PATHS/BISITE/RESIDUE | Every one of the 255 supplied statement IDs, individually mapped, with exact source statuses and comparison anchors. |

No full form of any of the twelve numbered NEW_RESULTS statements was located in the present pages. This conclusion is a textual coverage result; the maps and functors that provide useful comparisons are identified in the individual entries, and no claim of mathematical disconnection is made. The exact source rows and query evidence are preserved in the coverage JSON files, so a later reader can trace both positive connections and bounded absence findings.

