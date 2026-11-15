"""Research notes only. This script never reads or writes transcription text for correction."""

ITEMS = []

def add(id, section, title, kind, scans, anchor, queries, sentences, results="No directly corresponding entry", confidence=None):
    assert 1 <= len(sentences) <= 4, id
    assert kind in {"conjecture", "unproved claim", "unpursued implication", "own idea", "reading question", "self-flagged", "withdrawn in same text"}
    assert kind != "own idea" or confidence in {"high", "medium", "low"}
    ITEMS.append(dict(id=id, section=section, title=title, kind=kind, scans=scans, anchor=anchor,
                      queries=queries, sentences=sentences, results=results, confidence=confidence))

add("R067", "Endomorphisms and universal operations", "A constant coefficient of one justifies cancellation in the graded case", "own idea", "200, 233", "a_11=1+… and later completion", [r"complet", r"graded", r"136-automorphism"], (
    r"For an element $a=1+h$ with $h$ in positive weight in the direct-sum PD algebra $k\{T\}$, a nonzero $b$ has a least nonzero weight component $b_d$, and the weight-$d$ part of $ab$ is exactly $b_d$, proving that multiplication by $a$ is injective over any base ring.",
    r"The same least-weight argument applies in the separated product completion for this weight filtration, where the geometric series also makes $1+h$ a unit; it does not automatically cover every other topology or quotient ideal mentioned later.",
    r"Confidence is **high** because the proof is a direct graded-component calculation, so it supplies the cancellation needed to pass from $2a_{11}b_{ik}=0$ to $2b_{ik}=0$ in the standard case while leaving the uncertain words “un div. de zéro|n. div. de zéro” on scan 200 untouched.",
    r"Context comparison: this **adds** a verified local step to **136-automorphism-group-scheme** and the completion discussion in `ps6.tex`, §111, manuscript pp. 450–451; the more general completion/base-change caveat of §124, manuscript pp. 521–522, remains separate."
), results="Hua: 136-automorphism-group-scheme", confidence="high")

add("R001", "Answers to the package questions", "The integral comparison is explicitly weightwise", "unproved claim", "231, 233", "Corollary 1.5 and the first two displays on scan 233", [r"De.?Rham", r"136-pd-de-rham-shadows", r"linearization"], (
    r"The assertion beginning “pour tt $X$ semi-simplicial” identifies $C^{p,*}_{\mathrm{DRpd}}(X,k)$ with $\tau^{\le p}R\Gamma(X,k)$ and states $H^{p,i}_{\mathrm{DRpd}}(X,k)\simeq H^i(X,k)$ for $i\le p$, with zero above that bound; $k=\mathbb Z$ is allowed by the stated generality.",
    r"The weight is $p$ and the differential degree is $i$, since scan 231 explicitly writes $\mathcal A_*^{p,i}=\Gamma_k^{p-i}\Phi_*\otimes_k\Lambda^i\Psi_*$, so this is a family of truncated additive models rather than an assertion that one fixed weight computes all degrees.",
    r"The proof supplied is a resolution argument whose use of flasqueness and truncation still needs the categorical checks in R039–R041; no full multiplicative comparison is written in these two pages.",
    r"Context comparison: these pages **add** a precise calculation to the question in `README.md`, lines 17–21, and **differ** from the later schematization program in `ps6.tex`, §124, manuscript pp. 521–522; they directly bear on **WG2 §2.4 #5** and refine **136-pd-de-rham-shadows**, rather than establishing **WG H6**."
), results="WG2 §2.4 #5; Hua: 136-pd-de-rham-shadows; WG H6 (scope limitation)")

add("R002", "Answers to the package questions", "Functoriality has two distinct variances", "unpursued implication", "204, 221, 233", "triple functor, opening paragraph, and Hom definition", [r"ground ring", r"ring extension", r"functor", r"2\.4 #5"], (
    r"The words “devient un foncteur covariant” on scan 204 concern triples $(S,S^+,t)$ and morphisms $(u,\lambda)$ satisfying $u(t)=\lambda t'$, whereas “Les … algèbres différentielles sont fonctorielles en $(A,M)$” on scan 221 concerns the four algebraic complexes.",
    r"The definition $C^{p,*}_{\mathrm{DRpd}}(X,k)=\operatorname{Hom}(X,\Phi_*^{p,*})$ on scan 233 supplies contravariance in $X$ by precomposition, so the manuscript gives concrete support to the functorial part of S11(i).",
    r"Context comparison: this **adds** explicit algebraic formulas to `README.md`, lines 17–23, but `ps6.tex`, §124, manuscript pp. 521–522, **differs** by discussing derived adjunctions and ground-ring extension for schematic types; covariance in triples alone supplies none of that later equivalence or adjunction data."
), results="WG2 §2.4 #5; WG2 §Week #3")

add("R003", "Answers to the package questions", "The point already detects the product qualification", "own idea", "204, 217, 231, 233", "A_0=S and divided-power multiplication", [r"divided powers", r"multiplicat", r"136-pd-de-rham-shadows"], (
    r"For $X=\Delta^0$ the presentation gives $\mathcal A_0=k\{T\}$ in differential degree zero, and its weight-$p$ generator satisfies $T^{(p)}T^{(q)}=\binom{p+q}{p}T^{(p+q)}$; thus identifying each copy with $H^0(\Delta^0,k)=k$ does not identify their products with ordinary multiplication without that coefficient.",
    r"There is no unital ring specialization $\mathbb Z\{T\}\to\mathbb Z$ sending $T$ to $1$, since $T^2=2T^{(2)}$ would imply $1=2a$ in $\mathbb Z$, so the rational maneuver of setting a simplex parameter equal to one cannot silently be used integrally.",
    r"Confidence is **high** because both conclusions follow from the displayed presentation and the elementary divided-power identity, without assuming an unidentified comparison theorem.",
    r"Context comparison: this **adds** a product test to **WG2 §2.4 #5** and **136-pd-de-rham-shadows**, while `ps6.tex`, §119, manuscript pp. 501–503, likewise **differs** between divided-power and binomial algebraic structures rather than identifying them."
), results="WG2 §2.4 #5; Hua: 136-pd-de-rham-shadows", confidence="high")

add("R004", "Answers to the package questions", "A stronger unweighted PD claim has a concrete obstruction", "own idea", "215, 217, 233", "PD ideal and integral comparison", [r"divided powers", r"suitable ideal", r"2\.4 #5"], (
    r"Suppose the proposed interpretation were an ordinary integral cochain algebra with the usual cup ring and differential-compatible divided powers on every even positive-degree cocycle: then a cocycle $x$ would give $[x]^2=2[\gamma_2(x)]$, because $d\gamma_2(x)=x\,dx=0$.",
    r"For the degree-two generator $u$ of $H^*(\mathbb{CP}^2;\mathbb Z)=\mathbb Z[u]/(u^3)$, $u^2$ is not twice another integral class, giving a counterexample to that stronger interpretation (Hatcher, 2002, Theorem 3.19).",
    r"Confidence is **high** because this only uses the PD identity and the explicit cohomology ring; it does not require divided powers of boundaries to be boundaries, and it does not refute the weighted assertion actually written on scan 233.",
    r"Context comparison: this **adds** an obstruction relevant to **WG2 §2.4 #5**; `ps6.tex`, §120, manuscript pp. 506–507, already discusses divided powers on a suitable ideal, a restriction that the stronger claim would have discarded."
), results="WG2 §2.4 #5", confidence="high")

add("R005", "Answers to the package questions", "No definition of a topos de De Rham occurs in this packet", "reading question", "189–234, especially 233", "packet-wide search; RΓ display", [r"topos de De", r"faisceaut", r"Illusie", r"topos"], (
    r"The handwritten text reaches “$\mathbb R\Gamma(X,k)$” on scan 233, but these retained pages provide no site, topology, category of sheaves, or definition bearing the name “topos de De Rham”, and they do not define its “faisceautisation”.",
    r"Those two expressions occur in the supplied `README.md`, lines 17–21, as the researchers’ questions, while `PURSUING_STACKS_CONTENTS.md`, §94, points to a retrospective on the PD de Rham complex whose chapter-V text is not included.",
    r"Context comparison: `ps6.tex`, §127, manuscript pp. 536–538, **adds** a later discussion of simplicial fpqc sheaves and Illusie’s derived category of a topos, including a warning that ordinary sections need not preserve weak equivalences; it does not identify that construction with a named de Rham topos in this packet.",
    r"The answer is therefore undetermined from the supplied pages, not a license to equate the missing term with a crystalline site, an infinitesimal site, or a modern de Rham stack."
), results="WG2 §Week #3; WG H6 (unresolved)")

add("R006", "Answers to the package questions", "Universal constructions that are actually present", "unpursued implication", "204, 215, 217, 225–226", "triple functor; theorem b; representability formulas", [r"universal", r"polynomial map", r"analyz", r"represent"], (
    r"The universal property on scan 215 calls $\Gamma(M^0)\otimes\Lambda(M^1)$ the alternating graded PD algebra “engendrée par le $S$-module gradué $M^*$”, with its homomorphisms represented by graded maps $M^*\to K^*$; scans 204 and 225–226 supply, respectively, a parameterized simplex algebra and representability formulas for normalization.",
    r"These are concrete universal constructions in the packet, but the phrase “constructions universelles” is not itself an announced lecture section here, and the proof on scan 215 stops at “Dém :”.",
    r"Context comparison: `ps6.tex`, §111, manuscript pp. 449–451, **restates a related** universal-polynomial role for $\Gamma$ and its completion, while §120, manuscript pp. 506–507, **adds** Lazare’s analyzers and composition laws for general operations; neither text proves that all those later notions were the intended scope of the 1976 heading sought in `README.md`."
), results="WG2 §2.4 #5; WG2 §Week #3")

add("R007", "Answers to the package questions", "A local working sequence, not a recoverable full lecture plan", "reading question", "190–212, 215–223, 225–233", "successive headings and proof fragments", [r"lecture", r"1976", r"94\.", r"four functors"], (
    r"The visible sequence runs from endomorphism calculations to “p.d. dans les anneaux alternés”, then “Quelques complexes d’algèbres différentielles”, normalization material, and “Quelques calculs d’homotopie”, ending with the truncated cohomology comparison and a new completion paragraph.",
    r"That sequence reconstructs the organization of these working leaves, but the packet contains no lecture syllabus, dated IHÉS title leaf, stated duration, or explicit total page count, and the cancelled and loose leaves preclude treating scan order as a proved chronology of composition.",
    r"Context comparison: this **adds** an observed local organization to `README.md`, lines 9 and 15–27, whereas its association with a 1976 lecture and the later retrospective listed in `PURSUING_STACKS_CONTENTS.md`, §94, remain contextual provenance rather than words on these scanned faces."
), results="WG2 §Week #3")

add("R008", "Answers to the package questions", "Abelian varieties occur on reused typescript, not as PD lecture examples", "reading question", "189, 191, 193, 195, 197, 199, 201, 203, 205, 207, 209, 228, 230, 232, 234", "reused pages headed IX, especially 5.4 and 14.1.12", [r"abelian variet", r"vari.t.s ab.l", r"Fourier", r"Chern", r"bonne r.duction"], (
    r"Abelian schemes and their generic fibres are explicitly named, for example “schéma abélien” in the reduction arguments and “Dualité des schémas abéliens” in the heading on scan 209, but these occur on reused typescript about Néron models, Tate modules, biextensions, and monodromy.",
    r"The retained handwritten PD pages do not present abelian varieties as worked examples of the cochain construction, and no Chern class of a Fourier transform is named anywhere in this packet.",
    r"Context comparison: searches for Fourier, Chern, and abelian-variety phrases in `ps6.tex` and `ps7.tex` supplied no matching example; these pages therefore **differ** from the examples conjectured in `README.md`, line 21, without ruling out examples on unprovided leaves of cote 136."
), results="WG2 §Week #3")

add("R009", "Answers to the package questions", "Semisimplicial terminology does not identify the indexing category with Delta_inj", "reading question", "194, 227, 229, 231", "all set maps; Dold–Puppe and normalization", [r"Delta_inj", r"Kan-Dold-Puppe", r"Simplex"], (
    r"Scan 194 explicitly considers applications simpliciales “(ensembl.!)” and then increasing maps, while scans 227–231 use the Dold–Puppe normalization and simplicial homotopy formalism, so the notation “$1/2$ simplicial” must be read with its own indexing conventions.",
    r"Context comparison: `ps7.tex`, §134, manuscript pp. 558–560, **restates** the special role of $\Delta$ and carefully distinguishes normalization from a general integrator, whereas **PRETOT A.12**, **TOTASPH C.10**, and **PATHS A.6** in `notes/RESULTS_STATE.md` concern the category $\Delta_{\mathrm{inj}}$ and its colimits.",
    r"The present flasqueness computations neither prove filteredness of $\Delta_{\mathrm{inj}}$ nor reopen those register entries; an identification of the actual index category is required before transferring any of their claimed results."
), results="PRETOT A.12; TOTASPH C.10; PATHS A.6")

add("R010", "Endomorphisms and universal operations", "The one-simplex extension statement is explicitly corrected", "withdrawn in same text", "194, 200", "proposition and marginal correction; final margin of scan 200", [r"136-automorphism", r"composition", r"analyz"], (
    r"The proposition on scan 194 originally extends every differential $S$-endomorphism of $\mathcal A_1$ compatible with both augmentations to all simplices, but its margin says “faux tel quel; vrai” subject to $2B_i=0$ for all $i\ge1$ (the reading of “si/ssi” remains marked in the frozen text).",
    r"Scan 200 identifies the obstruction when images of $dU_r$ must commute with images of even divided-power generators in a different variable, obtaining $2a_{1j}b_{ik}=0$ and then $2B_i=0$ under the stated cancellation step.",
    r"Context comparison: this **adds a necessary correction** to the broad classification lead **136-automorphism-group-scheme** in `notes/RESULTS_STATE.md`, line 127; `ps6.tex`, §120, manuscript pp. 506–507, discusses composition of universal operations but contains no corresponding proof of this extension theorem."
), results="Hua: 136-automorphism-group-scheme")

add("SF01", "Standing question: steps marked as unverified", "Vertex reversal", "self-flagged", "192", "NB", [r"136-automorphism", r"composition"], (
    r"“que deviennent les $B_i$ ?” is followed by the $C_i$ calculation on the same page: a locally answered check, with the double-reversal and sign verification still useful (R013).",
    r"Context comparison: this **adds** local data absent from `ps6.tex`, §120, manuscript pp. 506–507, and bears on **136-automorphism-group-scheme**."
), results="Hua: 136-automorphism-group-scheme")

add("SF02", "Standing question: steps marked as unverified", "A proposition retracted and its corollaries marked for correction", "withdrawn in same text", "194, 200", "correction margin and mixed commutator calculation", [r"136-automorphism", r"composition"], (
    r"“faux tel quel; vrai” with $2B_i=0$, and the uncertain margin asking for corrections to the corollaries, explicitly retract the unrestricted proposition; scan 200 supplies its mixed-commutator obstruction, subject to the cancellation issue in R011.",
    r"Context comparison: this **adds a scope correction** to **136-automorphism-group-scheme** in `notes/RESULTS_STATE.md`, line 127; no such proof is supplied by the general operations discussion in `ps6.tex`, §120, manuscript pp. 506–507."
), results="Hua: 136-automorphism-group-scheme")

add("SF03", "Standing question: steps marked as unverified", "Commutation of images from different variables", "self-flagged", "200", "mais commutent-ils aux…", [r"136-automorphism", r"divided powers"], (
    r"“mais commutent-ils aux” introduces the check that produces $2a_{1j}b_{ik}=0$ and the proposed conclusion $2B_i=0$, so the page contains an answer but also the unresolved zero-divisor reading noted in R011.",
    r"Context comparison: this **adds** a specific verification to **136-automorphism-group-scheme** (`notes/RESULTS_STATE.md`, line 127), with no matching coefficient argument in the supplied PS chapters."
), results="Hua: 136-automorphism-group-scheme")

add("SF04", "Standing question: steps marked as unverified", "The proposed semidirect decomposition", "self-flagged", "208", "first diagram", [r"136-automorphism", r"automorphism", r"composition"], (
    r"“(??)” is attached to the comparison arrow in the diagram preceding the proposed “produit $1/2$ direct”, leaving the map, monoid/group distinction, and decomposition to check (R016–R018).",
    r"Context comparison: it **qualifies** **136-automorphism-group-scheme** and **differs** from the mere composition algebra in `ps6.tex`, §120, manuscript pp. 506–507."
), results="Hua: 136-automorphism-group-scheme")

add("SF05", "Standing question: steps marked as unverified", "Cartier operations", "conjecture", "219–220", "unfinished characteristic-p lines", [r"Cartier", r"operations"], (
    r"“histoire des opérations, de Cartier ----” and “on doit avoir une histoire d’opérations de Cartier ----” state unfinished expectations for different members of the four-complex family, with no formula or proof supplied (R024).",
    r"Context comparison: no matching Cartier passage occurs in `ps6.tex` or `ps7.tex`; these leaves **add** a specific question to the operations theme of `ps6.tex`, §120, manuscript pp. 506–507, and **WG2 §2.4 #5**."
), results="WG2 §2.4 #5")

add("SF06", "Standing question: steps marked as unverified", "Flatness marked unnecessary", "withdrawn in same text", "219–220, 222–223", "inutile margins; Euler homotopy", [r"flat", r"R033"], (
    r"“inutile” and “(inutile)” mark the withdrawal of flatness in the rational cases, and “sans hyp. de platitude!” on scan 222 explains it through the total-weight contraction (R026).",
    r"Context comparison: this **adds a distinct method** to **MPL_134-8_043-087 R033** (`notes/RESULTS_STATE.md`, line 113), while the projective nonlinear argument in `ps6.tex`, §111, manuscript pp. 455–456, retains its own different hypotheses."
), results="MPL_134-8_043-087 R033; WG2 §2.4 #5")

add("SF07", "Standing question: steps marked as unverified", "The question mark beside PD de Rham", "self-flagged", "220–221", "left marginal question mark and proof sketch", [r"De.?Rham", r"Gamma", r"flat"], (
    r"The “?” and bracket beside the PD-de-Rham discussion on scan 220 are explicit, but their exact scope between identification and acyclicity is not fully determined by the placement; scan 221 supplies the Lazard–Künneth proof sketch for the acyclicity claim (R025).",
    r"Context comparison: this **adds** a local qualification to **WG2 §2.4 #5**, and the supplied chapters contain no matching marginal question; the closest related passage is `ps6.tex`, §111, manuscript pp. 455–456."
), results="WG2 §2.4 #5")

add("SF08", "Standing question: steps marked as unverified", "Degree-zero de Rham cohomology", "self-flagged", "223", "opening questions and donc inj, OK", [r"De.?Rham", r"homotop"], (
    r"“est-il vrai … aussi un isom ?”, “est injectif ?”, and the marginal “?” are answered on the same page by “donc inj, OK”, with invertibility of the homogeneous weight stated explicitly (R029).",
    r"Context comparison: this **adds** a locally resolved check to the PD-de-Rham topic listed in `PURSUING_STACKS_CONTENTS.md`, §94, whose full text is absent; it does not settle the integral issues of **WG2 §2.4 #5**."
), results="WG2 §2.4 #5")

add("SF09", "Standing question: steps marked as unverified", "Compatibility in the normalization formula", "self-flagged", "225", "end of Proposition 6 proof", [r"normalization", r"integrator"], (
    r"“il reste à faire de petites vérifications de compatibilité --” leaves the differential and functorial compatibilities of the representing formula unverified on this leaf (R032).",
    r"Context comparison: `ps7.tex`, §134, manuscript pp. 558–560, **adds** the relevant distinction between an integrator and the normalized equivalence, without filling these particular checks."
))

add("SF10", "Standing question: steps marked as unverified", "Derived exterior powers of projective complexes", "self-flagged", "229", "first paragraph and margin", [r"projective", r"Gamma", r"Dold"], (
    r"“sauf erreur” and “est-ce vrai ?” qualify the general $(L\Lambda^i)(L_\bullet)\simeq\Lambda^i(L_\bullet)$ assertion, whose answer depends on the convention for the right-hand side (R035).",
    r"Context comparison: `ps6.tex`, §111, manuscript pp. 455–456, and `ps7.tex`, §134, manuscript p. 560, **add** the projective simplicial-homotopy framework, but not an identification with naive termwise exterior powers."
), results="WG2 §2.4 #5")

add("SF11", "Standing question: steps marked as unverified", "The minimal normalized exterior model", "conjecture", "229, 231", "NB a and B_*^! in the tensor proof", [r"normalization", r"136-pd-de-rham-shadows"], (
    r"“Il est probable que … $k[i]$” is followed by “On n’en a pas besoin”, although the stronger model is invoked in the tensor calculation on scan 231; R036 gives a separate verification with its assumptions made explicit.",
    r"Context comparison: this **adds** a local conjectural-to-used step to **136-pd-de-rham-shadows**, beyond the general normalization discussion in `ps7.tex`, §134, manuscript pp. 559–560."
), results="Hua: 136-pd-de-rham-shadows")

add("SF12", "Standing question: steps marked as unverified", "A missing algebraic description", "self-flagged", "230", "Remark 14.1.12 a", [r"Raynaud", r"arithm", r"uniform"], (
    r"“Je n’en connais aucune description purement algébrico-géométrique” and the promised “caractérisation ‘arithmétique’” in §14.4 record an explicit limitation and a deferred route, not a claim that the problem remains open today (R061).",
    r"Context comparison: searches found no corresponding description in `ps6.tex`, `ps7.tex`, or the results register, so this **adds separate reused-source material**."
))

add("SF13", "Standing question: steps marked as unverified", "The possible opposite dual map", "self-flagged", "230, 234", "end of Remark 14.1.12 b", [r"biextension", r"sign", r"duality"], (
    r"“à moins que ce ne soit l’opposé ???” leaves the sign of the dual uniformization map unresolved, and scan 234 provides the adjacent biextension conventions needed for checking it (R062).",
    r"Context comparison: this **adds** a specific sign question absent from the context’s general duality discussion, for example `ps6.tex`, §124, manuscript pp. 528–529."
))

add("SF14", "Standing question: steps marked as unverified", "General duality proof deferred to section 7", "unproved claim", "195, 199", "references to n° 7 and 7.4.6", [r"Raynaud", r"Tate", r"duality"], (
    r"“va être donnée au n° 7” and “plus bas (7.4.6)” defer the general perfect-duality argument, distinguishing its Tate-theoretic mixed-characteristic route from the promised direct proof (R056).",
    r"Context comparison: neither the promised section nor a matching result is present in `ps6.tex`, `ps7.tex`, or `notes/RESULTS_STATE.md`, so this **adds** a documented proof dependency."
))

add("SF15", "Standing question: steps marked as unverified", "Removing the prime restriction", "self-flagged", "201", "Il reste à prouver", [r"orthogonal", r"Barsotti"], (
    r"“Il reste à prouver … sans restriction sur $\ell$” introduces an all-primes step that the following paragraph reduces using ranks, strictness, and orthogonality, so its local status is a written reduction rather than an unqualified omission (R057).",
    r"Context comparison: this **adds** a dependency absent from the supplied PS chapters and register."
))

add("SF16", "Standing question: steps marked as unverified", "A proof called easy and left to the reader", "unproved claim", "203", "final paragraph", [r"Barsotti", r"isogen"], (
    r"“Nous laisserons au lecteur la démonstration (facile)” of 5.2.5 is accompanied by a promise of special cases in §7.4.7, which is absent here (R058).",
    r"Context comparison: this **adds** a deferred specialization lemma with no matching proof in `ps6.tex`, `ps7.tex`, or the results register."
))

add("SF17", "Standing question: steps marked as unverified", "A historical conjecture now announced as a corollary", "unproved claim", "205", "Corollary 5.10", [r"conject", r"bonne r.duction", r"Tate"], (
    r"“résultat conjecturé dans [8, 4.9]” identifies the earlier status of the good-reduction criterion, while “il reste à prouver la suffisance” begins the proof offered here, which continues beyond the retained face (R059).",
    r"Context comparison: this **adds** a historical proof-status distinction absent from the supplied PS chapters and register, and is unrelated to a conjecture about the PD lecture’s examples."
))

add("SF18", "Standing question: steps marked as unverified", "Completeness to be removed in section 6.1", "unproved claim", "209", "footnote (*)", [r"complet", r"toric"], (
    r"“Cette hypothèse n’est d’ailleurs pas essentielle, comme on montre dans 6.1 ci-dessous” explicitly defers removal of the completeness hypothesis in the formal-torus construction (R060).",
    r"Context comparison: it **differs** from the PD-completion issue on scan 233 and `ps6.tex`, §111, manuscript pp. 450–451; the promised argument is not in the supplied materials."
))

add("SF19", "Standing question: steps marked as unverified", "The extension of the PD axioms is only partly checked", "unproved claim", "217", "Voyons dans quelle mesure and axioms (0)–(4)", [r"divided powers", r"ideal", r"operations"], (
    r"“Voyons dans quelle mesure $(A)$ reste valable” is followed by checks labelled “OK” and restrictions to strict commutation, but the final iterated-power identity (4) is only written down without a completed verification on this leaf.",
    r"Context comparison: this **adds** a remaining local proof obligation to R021 and **WG2 §2.4 #5**, while `ps6.tex`, §120, manuscript pp. 506–507, **restates** the wider operations theme rather than this axiom check."
), results="WG2 §2.4 #5")

add("TC01", "Standing question: titles, foliation, and page counts", "Packet extent is not an authorial page count", "reading question", "189–234, excluding 214", "all retained faces", [r"189-234", r"45 scans", r"lecture"], (
    r"There are 45 retained scan pages in the requested inclusive range, with scan 214 omitted by the supplied scan package; the inventory classifies 24 as text, 20 as reused_typed, and one as cancelled_draft, including the pencil-only face at scan 224 among the reused sheets.",
    r"No retained cover or title sheet states a total such as “19 pages” or a range such as “Pages 1–67”; the visible foliation below must not be turned into an asserted length of the lecture.",
    r"Context comparison: `README.md`, line 9, **restates** the scan-range provenance, while its “first 45 scans” on lines 16 and 27 **differs** by referring to the earlier, unavailable probe package rather than an authorial count for the present leaves."
), results="WG2 §Week #3")

add("TC02", "Standing question: titles, foliation, and page counts", "The pencil foliation is distinct from the PDF scan numbers", "reading question", "189–234, excluding 214", "small face numbers, including scan 224", [r"page", r"189-234", r"136-pd"], (
    r"The visible small face numbers run from 188 on scan 189 to 233 on scan 234, following scan number minus one on the retained images; the absent scan 214 would occupy the gap at 213, but no content of that omitted face is inferred.",
    r"Scan 224 contributes the number 223 only on the presented face, and the frozen transcription does not reconstruct the reversed show-through as a second text.",
    r"Context comparison: these observations **add** a foliation distinction to `README.md`, line 9, and to the scan mapping in the Hua entries at `notes/RESULTS_STATE.md`, lines 126–127; the provenance of the pencil numbering is not independently established by those files."
), results="Hua: 136-pd-de-rham-shadows; Hua: 136-automorphism-group-scheme")

add("TC03", "Standing question: titles, foliation, and page counts", "The reused IX sheets have a separate, nonconsecutive pagination", "reading question", "189, 191, 193, 195, 197, 199, 201, 203, 205, 207, 209, 211, 213, 228, 230, 232, 234", "typed page headers and repeated larger foliation labels", [r"monodrom", r"189-234", r"page"], (
    r"""The typed page numbers and the separate larger numbers on the IX leaves are:

| PDF scan | Typed page | Larger number |
|---:|---:|---:|
| 189 | 64 | 382 |
| 191 | 62 | 380 |
| 193 | 61 | 379 |
| 195 | 60 | 378 |
| 197 | 59 | 377 |
| 199 | 58 | 376 |
| 201 | 57 | 375 |
| 203 | 56 | 374 |
| 205 | 67 | 385 |
| 207 | 52 | 370 |
| 209 | 51 | 369 |
| 211 | 50 | 368 |
| 213 | 49 | 367 |
| 228 | 192 | 510 |
| 230 | 191 | 509 |
| 232 | 190 | 508 |
| 234 | 189 | 507 |""",
    r"These are observed foliation values, including repeated larger labels in the transcription, not evidence that this packet contains a continuous 49–67 or 189–192 text in reading order.",
    r"Context comparison: this **adds** provenance information absent from the PS chapters and **qualifies** the contiguous scan spans used by the Hua entries in `notes/RESULTS_STATE.md`, lines 126–127."
), results="Hua: 136-pd-de-rham-shadows; Hua: 136-automorphism-group-scheme")

add("TC04", "Standing question: titles, foliation, and page counts", "Handwritten working headings", "reading question", "204, 215, 219–221, 223, 227", "titles, boxed headings, and marginal subheadings", [r"De.?Rham", r"analyz", r"94\.", r"1976"], (
    r"""The substantive working headings are:

| Scan | Heading as represented in the frozen transcription |
|---:|---|
| 204 | Endomorphismes de l’anneau différentiel $\frac12$ simplicial $\mathcal A_*$ |
| 215 | p.d. dans les anneaux alternés |
| 219 | Quelques complexes d’algèbres différentielles. |
| 219 | De Rham; Koszul (marginal subheadings) |
| 220 | De Rham P.D.; Koszul P.D. (marginal subheadings) |
| 221 | Relations\|Relation entre les 4 complexes, et fonctorialité. (uncertain ending retained) |
| 223 | Dualité |
| 227 | Quelques calculs d’homotopie |""",
    r"None of these headings is accompanied by a stated number of pages or a lecture date.",
    r"Context comparison: they **add** local organization to `README.md`, lines 15–23, and **differ** from the later retrospective listed in `PURSUING_STACKS_CONTENTS.md`, §94, whose body was not supplied."
), results="WG2 §Week #3")

add("TC05", "Standing question: titles, foliation, and page counts", "Two headings belong to the reused IX text", "reading question", "209, 228", "5 and 14.2", [r"orthogonal", r"monodrom", r"abelian"], (
    r"Scan 209 carries section 5, beginning “Le théorème d’orthogonalité dans le cas $\ell=p$ (cas semi-stable)” and continuing through duality of the abelian schemes, characterization of the fixed part, and criteria for good, essentially good, and semistable reduction; scan 228 carries “14.2. Relations de l’homomorphisme $i:\underline M_K\longrightarrow G_K$ avec la monodromie”.",
    r"Neither heading gives a total page count, and neither is a title of the handwritten PD-complex sequence.",
    r"Context comparison: these headings **differ** from the lecture topics and examples guessed in `README.md`, lines 17–21, and no matching section text is present in the supplied PS chapters."
))

add("TC06", "Standing question: titles, foliation, and page counts", "The Stoia title and page four", "reading question", "216, 218", "title and printed foliation", [r"Stoia", r"Gorenstein", r"page"], (
    r"Scan 216 bears the title “POINTS DE GORENSTEIN D’UN MORPHISME” followed by “par Manuela STOIA”, while scan 218 is numbered “4” and includes “Bibliographie” and the Bucharest institutional address.",
    r"The number four is a visible page number, not an explicit declaration that the entire article or all of its intermediate pages are included in this packet.",
    r"Context comparison: neither the title nor its author appears in the supplied context, so this **adds** independent reused-sheet provenance and has no direct RESULTS_STATE counterpart."
))

add("TC07", "Standing question: titles, foliation, and page counts", "Loose-leaf annotations are not page-count statements", "reading question", "215, 225", "marginal labels", [r"loose", r"feuille", r"1976"], (
    r"Scan 215 has “Feuille paumée|jaunie...” in an explicitly uncertain reading, and scan 225 has “Feuille volante paumée...” with the final adjective likewise marked doubtful; neither label includes a page total.",
    r"Context comparison: these annotations **add** documentary evidence about loose leaves absent from `README.md` and the supplied PS chapters, but do not establish the chronology or complete plan of the lecture."
))

add("TC08", "Standing question: titles, foliation, and page counts", "The cancelled leaf and missing lecture title", "reading question", "226; packet-wide", "cancelled Proposition 6 and absence of cover", [r"lecture", r"1976", r"94\.", r"page"], (
    r"Scan 226 is the cancelled draft with face number 225 and a struck Proposition 6, not a cover carrying a title or a stated length, and no retained page supplies the archival title’s bracketed IHÉS attribution or date.",
    r"Context comparison: this **differs** between direct leaf evidence and `README.md`, line 9, whose wording reproduces the archival description; `PURSUING_STACKS_CONTENTS.md`, §94, provides a later retrospective lead rather than the missing lecture title sheet."
), results="WG2 §Week #3")

add("R011", "Endomorphisms and universal operations", "The cancellation used to obtain 2B_i=0 needs its own hypothesis", "reading question", "200", "margin beginning a_11=1+…", [r"136-automorphism", r"complet", r"divided"], (
    r"After the coefficient conditions $2a_{1j}b_{ik}=0$, the margin calls $a_{11}=1+\sum\alpha_iT^{(i)}$ something read as “un div. de zéro|n. div. de zéro” and concludes $2b_{ik}=0$; the first, visually uncertain alternative cannot justify cancellation.",
    r"A possible mathematical repair is to prove injectivity of multiplication by a series with constant coefficient one in the intended graded or completed algebra, or to prove it is a unit under an appropriate completion; R067 verifies the standard graded case, but that does not authorize altering the frozen reading.",
    r"Context comparison: `ps6.tex`, §111, manuscript pp. 450–451, **adds** an explicit completed PD algebra, and scan 233 itself later imposes completeness; **136-automorphism-group-scheme** does not settle which hypothesis was in force at scan 200."
), results="Hua: 136-automorphism-group-scheme")

add("R012", "Endomorphisms and universal operations", "Consequences depend sharply on the prime two", "unpursued implication", "194, 200, 217", "2B_i correction and strict commutation", [r"136-automorphism", r"divided powers", r"ideal"], (
    r"The correction on scan 194 itself distinguishes characteristic two, where $2B_i=0$ imposes no condition, from the case where $2$ is invertible, where it forces all $B_i$ to vanish and hence preserves the grading.",
    r"This is consistent with scan 217’s stronger requirement $x^1y^1=0$ for “commutent strictement”, rather than merely $2x^1y^1=0$, and warns against classifying ungraded endomorphisms by a rational calculation alone.",
    r"Context comparison: this **adds** an explicit prime-two mechanism to **136-automorphism-group-scheme**; `ps6.tex`, §119, manuscript pp. 500–503, **differs** by exposing another integral obstruction through binomial polynomials, with no assertion that the two obstructions are identical."
), results="Hua: 136-automorphism-group-scheme; WG2 §2.4 #5")

add("R013", "Endomorphisms and universal operations", "Reversing the vertices is worked out, rather than left unanswered", "self-flagged", "192", "NB and subsequent formula for C_i", [r"composition", r"136-automorphism", r"diagonal"], (
    r"The question “Si on échange le rôle de $X_0$ et $X_1$ … que deviennent les $B_i$ ?” is followed on the same page by the calculation of the transformed coefficients $C_i$, so it is a self-posed check with a written answer rather than an unresolved conjecture.",
    r"Checking that transformation twice gives the original coefficients would test the formulas and their signs, especially because the surrounding formulas distinguish ordinary from divided powers.",
    r"Context comparison: no vertex-reversal formula was found in the supplied context; this **adds** local data to **136-automorphism-group-scheme**, while `ps6.tex`, §120, manuscript pp. 506–507, supplies only the broader composition-of-operations setting."
), results="Hua: 136-automorphism-group-scheme")

add("R014", "Endomorphisms and universal operations", "Cumulative coordinates make the extension problem finite in each dimension", "unpursued implication", "196, 198, 200", "U_r generators and A_n presentation", [r"polynomial", r"universal", r"136-automorphism"], (
    r"The cumulative variables $U_r$ give $\mathcal A_n\simeq S\{U_0,\ldots,U_{n-1}\}[dU_0,\ldots,dU_{n-1}]$, and scan 198 says that the $X_r$ “se reconstituent” from them, reducing extension to generator relations.",
    r"The calculation separates the divided-power multiplication relations among the $U_r^{(i)}$, the differential relations, and the mixed commutation relations exposed on scan 200; these are the concrete checks a proof of the corrected proposition needs.",
    r"Context comparison: this **adds** a presentation-level method to **136-automorphism-group-scheme**; `ps6.tex`, §111, manuscript pp. 449–451, **restates a related** free-PD universal principle without these simplex coordinates."
), results="Hua: 136-automorphism-group-scheme")

add("R015", "Endomorphisms and universal operations", "The functor of triples includes a scale as part of a morphism", "unpursued implication", "204, 206", "u(t)=λt′; regularity paragraph", [r"ring extension", r"ground ring", r"universal"], (
    r"The condition “$u(t)=\lambda t'$” on scan 204 makes $X_i\mapsto\lambda X_i$ and $dX_i\mapsto\lambda dX_i$ compatible with the simplex relation, and the stated composition is $(u',\lambda')(u,\lambda)=(u'u,u'(\lambda)\lambda')$.",
    r"Scan 206 removes the need to record $\lambda$ separately only when $t'$ is regular, so a functor defined solely on the underlying ring maps loses information at torsion bases.",
    r"Context comparison: these pages **add** precise base-change data to **WG2 §2.4 #5**, while `ps6.tex`, §124, manuscript pp. 521–522, **differs** by asking for derived functors compatible with arbitrary ground-ring extension rather than this strict presentation alone."
), results="WG2 §2.4 #5; Hua: 136-automorphism-group-scheme")

add("R016", "Endomorphisms and universal operations", "Endomorphisms form a monoid before any automorphism restriction", "withdrawn in same text", "206, 208", "groupe deleted twice; semidirect diagram", [r"136-automorphism", r"composition", r"automorphism"], (
    r"On scan 206 “groupe” is twice deleted and replaced by “monoïde” in the definition of $G_k$, while scan 208 again uses group language around a diagram marked “(??)” and a proposed semidirect product.",
    r"The distinction is substantive: $\lambda=0$ is permitted in the displayed endomorphism monoid and cannot give an invertible simplex endomorphism, so no group claim follows until invertibility conditions are imposed.",
    r"Context comparison: this **adds a qualification** to the automorphism-group-scheme conclusion in **136-automorphism-group-scheme**; `ps6.tex`, §120, manuscript pp. 506–507, treats an algebra of operations closed under composition, not an assertion that every operation is invertible."
), results="Hua: 136-automorphism-group-scheme")

add("R017", "Endomorphisms and universal operations", "The intersection G_k ∩ H_k records torsion missed by rationalization", "own idea", "208", "boxed coefficient conditions", [r"torsion", r"136-automorphism", r"ground ring"], (
    r"From “$(i+1)\lambda_i=0$” and $\lambda_0=1$, taking $k=\mathbb F_p$ and $\lambda=1+aT^{(p-1)}$ with $a\ne0$ gives $(\lambda-1)T=0$ and hence an element of the displayed $G_k\cap H_k$.",
    r"It is nonidentity on $\mathcal A_1$ because it sends the independent generator $X_0$ to $X_0+aT^{(p-1)}X_0$, even though it fixes $T$, so the intersection is a real stabilizer phenomenon rather than a redundant parametrization of the base map.",
    r"Confidence is **high** because the PD monomials in the independent variables $T,X_0$ form the displayed free basis and the annihilation relation is immediate.",
    r"Context comparison: this **adds** a test example to **136-automorphism-group-scheme**; `ps6.tex`, §110, manuscript pp. 443–445, likewise warns that torsion obstructs naive base-change reasoning, but supplies no such stabilizer calculation."
), results="Hua: 136-automorphism-group-scheme", confidence="high")

add("R021", "The four complexes and divided powers", "The free alternating PD theorem has an unwritten proof", "unproved claim", "215, 217", "theorem a–b; final Dém; axioms on the following handwritten leaf", [r"universal.*polynomial", r"Gamma", r"divided powers"], (
    r"Scan 215 asserts existence, functorial uniqueness, and the representing property of the PD structure on $J=\varepsilon^{-1}(I)\subset\Gamma(M^0)\otimes\Lambda(M^1)$, then ends with the bare heading “Dém :”.",
    r"Scan 217 supplies axioms and an extension formula but does not write a proof covering arbitrary base modules, compatibility with the base ideal, and the full bijection of homomorphism sets, so those remain proof obligations within this packet.",
    r"Context comparison: `ps6.tex`, §111, manuscript pp. 449–451, **restates a related** universal property of divided-power algebras, while §120, manuscript pp. 506–507, **adds** a general operations framework; neither replaces the missing proof of this particular mod-two graded statement.",
    r"For comparison with a modern formulation, the Stacks Project’s definition of graded divided powers explicitly includes the vanishing of higher divided powers on products of odd elements (Stacks Project Authors, n.d.-a, Definition 23.6.1)."
), results="WG2 §2.4 #5")

add("R022", "The four complexes and divided powers", "Divided powers on cochains do not automatically descend as operations on cohomology", "unpursued implication", "217, 220, 233", "axiom (5), differential compatibility, and comparison", [r"divided powers", r"operations", r"2\.4 #5"], (
    r"The added axiom “$(\lambda_1x_1)^{(i)}=0$” for $i\ge2$ and the differential rule $d(x^{(i)})=x^{(i-1)}dx$ specify cochain-level structure, but the pages do not check that changing a cocycle by a boundary leaves the proposed higher operation unchanged in cohomology.",
    r"This distinction is real: differential compatibility alone need not make the divided power of a boundary another boundary (Stacks Project Authors, n.d.-a, warning after Definition 23.6.5), so an operation on the identified $H^i(X,k)$ requires a separate descent argument and an account of its weight.",
    r"Context comparison: this **adds** a precise test for **WG2 §2.4 #5**, whose integrality thread asks about divided powers as structure on cochains, and **differs** from assuming that the discussion of algebraic operations in `ps6.tex`, §120, manuscript pp. 506–507, already settles the cohomological descent."
), results="WG2 §2.4 #5; Hua: 136-pd-de-rham-shadows")

add("R023", "The four complexes and divided powers", "A rank-one calculation separates the four acyclicity claims", "own idea", "219–222", "complexes (1)–(4) and total-degree formula", [r"divided powers", r"tensor", r"MPL_134-8_043-087 R033"], (
    r"""For $M=Ax$ and fixed total weight $N>0$, the four complexes reduce to the two-term maps below, directly from $d(x^N)=Nx^{N-1}dx$, $d(x^{(N)})=x^{(N-1)}dx$, and $x\,x^{(N-1)}=Nx^{(N)}$:

| Complex | Direction in exterior degree | Coefficient of the map |
|---|---|---|
| Ordinary de Rham, $\operatorname{Sym}\otimes\Lambda$ | $0\to1$ | $N$ |
| Ordinary Koszul, $\operatorname{Sym}\otimes\Lambda$ | $1\to0$ | $1$ |
| PD de Rham, $\Gamma\otimes\Lambda$ | $0\to1$ | $1$ |
| PD Koszul, $\Gamma\otimes\Lambda$ | $1\to0$ | $N$ |""",
    r"Thus ordinary Koszul and PD de Rham are already exact in positive weight in this example over every ring, whereas the other two see $\ker(N:A\to A)$ and $A/NA$ and require invertibility of $N$ for the same conclusion.",
    r"Confidence is **high** because this is a direct basis computation, and it explains why the four statements cannot be merged into a characteristic-independent Poincaré lemma.",
    r"Context comparison: this **adds** a local calculation to **WG2 §2.4 #5** and a useful test for the flat/projective method recorded as **MPL_134-8_043-087 R033**; the supplied context has no matching four-complex calculation, while `ps6.tex`, §111, manuscript pp. 455–456, separately emphasizes projectivity in nonlinear homological arguments."
), results="WG2 §2.4 #5; MPL_134-8_043-087 R033 (method only)", confidence="high")

add("R024", "The four complexes and divided powers", "The Cartier-operation expectations are genuinely unfinished", "conjecture", "219, 220", "last lines of complexes (1) and (4)", [r"Cartier", r"operations", r"divided powers"], (
    r"Scan 219 trails off at “histoire des opérations, de Cartier ----”, and scan 220 says “on doit avoir une histoire d’opérations de Cartier ----” for the PD Koszul complex in characteristic $p$.",
    r"A proof would have to specify the target, grading, Frobenius twist, and flatness or smoothness assumptions, then distinguish the familiar ordinary-de-Rham direction from its degreewise dual PD-Koszul direction rather than supplying an unnamed isomorphism.",
    r"Context comparison: the searches found no Cartier calculation in `ps6.tex` or `ps7.tex`; the pages **add** this expectation to **WG2 §2.4 #5**, while `ps6.tex`, §120, manuscript pp. 506–507, only **restates** the broader interest in additional operations."
), results="WG2 §2.4 #5")

add("R025", "The four complexes and divided powers", "The Lazard–Künneth reduction is a proof method with explicit scope", "unproved claim", "221", "bracketed proof of the calculation in (3)", [r"flat", r"projective", r"R033", r"filtered"], (
    r"The proof sketch says “par Lazard, puis par Künneth” to reduce a flat module to finite free modules and then to rank one, using the preceding assertion that the complexes commute with filtered colimits and carry sums to tensor products.",
    r"To complete that proof one must check these compatibilities for $\Gamma$, $\Lambda$, and the differentials, and use exactness of filtered colimits and the relevant tensor acyclicity; the rank-one maps in R023 show why the stated characteristic conditions matter.",
    r"Context comparison: this **adds a related method**, not a proof of the earlier claim, to **MPL_134-8_043-087 R033** (`notes/RESULTS_STATE.md`, line 113, referring to cote 134-8 scan 058), and `ps6.tex`, §111, manuscript pp. 455–456, **differs** by using projective resolutions and strict homotopies for a nonlinear functor."
), results="MPL_134-8_043-087 R033; WG2 §2.4 #5")

add("R026", "The four complexes and divided powers", "The flatness annotations are explained by the later Euler homotopy", "withdrawn in same text", "219, 220, 222–223", "inutile margins and θ=dδ+δd", [r"flat", r"homotop", r"R033"], (
    r"The word “inutile” beside flatness in the characteristic-zero ordinary-de-Rham statement on scan 219, and “(inutile)” in the PD-Koszul statement on scan 220, are justified later by “sans hyp. de platitude!” on scan 222.",
    r"On the summand of positive total weight $N$, the identity $d\delta+\delta d=N$ gives a contracting homotopy after dividing by $N$, so a $\mathbb Q$-algebra base removes the flatness requirement for those conclusions.",
    r"Context comparison: this **adds** a different route from the flatness method in **MPL_134-8_043-087 R033**, without retracting the projectivity requirement for the different nonlinear argument in `ps6.tex`, §111, manuscript pp. 455–456."
), results="MPL_134-8_043-087 R033 (distinction); WG2 §2.4 #5")

add("R027", "The four complexes and divided powers", "The final vanishing sentence confuses weight with cohomological degree if read literally", "own idea", "222", "last sentence after the boxed θ identity", [r"degree", r"divided powers", r"2\.4 #5"], (
    r"The sentence “$H^n_{DR}$ et $H_n^{\mathrm{Kos}}$ sont nuls pour tout $n$ tel que $n.1_A$ inv.” follows a formula whose $n$ is explicitly “degré total”, so it is valid as a contraction statement for that weight, not as unrestricted vanishing in cohomological degree $n$.",
    r"For $A=\mathbb F_p$ and the ordinary de Rham complex of $A[x]$, the closed form $x^{p-1}dx$ is not exact because differentiating a polynomial gives zero coefficient at that monomial, yet its cohomological degree is one and $1$ is invertible.",
    r"Confidence is **high** because this counterexample is a one-variable calculation; its total weight is $p$, precisely the noninvertible number appearing in the Euler formula, so it also identifies the needed qualification without changing the text.",
    r"Context comparison: this **adds** a grading warning to **WG2 §2.4 #5** and **136-pd-de-rham-shadows**; the context’s `ps6.tex`, §124, manuscript pp. 521–522, does not supply a replacement grading convention for this sentence."
), results="WG2 §2.4 #5; Hua: 136-pd-de-rham-shadows", confidence="high")

add("R028", "The four complexes and divided powers", "Characteristic zero is being used in the stronger Q-algebra sense", "reading question", "208, 219, 221–223", "car. 0 and explicit Q-algebra glosses", [r"characteristic", r"rational", r"ground ring"], (
    r"Scan 219 explicitly glosses “$A$ de car. $0$” as “$A$ une $\mathbf Q$-algèbre”, and scan 208 makes a similar gloss, which must govern the later shorthand in scans 221–223 if all positive weights are to be contracted.",
    r"Merely having characteristic zero is insufficient: in the ordinary de Rham complex of $\mathbb Z[x]$, the class of $x\,dx$ is nonzero and killed by two, since $d(x^2)=2x\,dx$.",
    r"Context comparison: this **adds** a base-ring qualification to **WG2 §2.4 #5**; `ps6.tex`, §110, manuscript pp. 443–445, and §119, manuscript pp. 500–503, **differ** explicitly between integral and rational constructions rather than allowing this shorthand to identify them."
), results="WG2 §2.4 #5")

add("R029", "The four complexes and divided powers", "The H0 question is answered on its own page", "self-flagged", "223", "first paragraph through donc inj, OK", [r"homotop", r"degree", r"De.?Rham"], (
    r"The questions “est-il vrai … aussi un isom ?” and “est injectif ?” concern whether closed homogeneous functions of positive degree are zero, and the page answers them by composing $d$ with $\delta$ to obtain multiplication by the weight $h$, ending “donc inj, OK”.",
    r"This resolves the local doubt when $h$ is invertible, as the parenthesis expressly says, and hence resolves $H^0\simeq A$ under the intended $\mathbb Q$-algebra hypothesis without a flatness assumption.",
    r"Context comparison: this **adds** a completed local check to the PD-de-Rham topic listed in `PURSUING_STACKS_CONTENTS.md`, §94; no identical $H^0$ calculation was found in the provided chapters VI–VII, and **WG2 §2.4 #5** is not thereby settled integrally."
), results="WG2 §2.4 #5")

add("R030", "The four complexes and divided powers", "The Koszul regularity criterion retains its hypotheses", "unproved claim", "221–222", "general Koszul construction and transverse condition", [r"Koszul", r"regular", r"flat"], (
    r"The phrase “est ‘transverse’” is followed by a sufficient regular-sequence condition and a necessity claim when $S$ is noetherian and $\varphi(\mathcal M)\subset\operatorname{rad}S$, with $\mathcal M$ finite free.",
    r"A proof must identify the intended radical and preserve the finiteness and local/Jacobson-radical hypotheses; the corresponding modern statement distinguishes regular, Koszul-regular, and $H_1$-regular sequences in general, making them equivalent under the appropriate noetherian local conditions (Stacks Project Authors, n.d.-b, Lemma 15.31.7).",
    r"Context comparison: no Koszul criterion occurs in the supplied `ps6.tex` or `ps7.tex`, so this **adds** algebraic groundwork rather than resolving a register theorem about exact colimits or total asphericity."
))

add("R031", "The four complexes and divided powers", "Duality is degreewise and needs sign and finiteness checks", "unproved claim", "223", "Dualité paragraph", [r"duality", r"perfect", r"complet"], (
    r"The words “on vérifie” assert that $d_M$ and $\delta_{M'}$, and multiplication and comultiplication, are transposes under the pairings $\operatorname{Sym}^*M\times\Gamma^*M'\to A$ and $\Lambda^*M\times\Lambda^*M'\to A$.",
    r"The page states perfection only for finite projective $M$ paired with its dual, so a complete verification should record exterior signs and distinguish the degreewise graded dual from the unrestricted dual of an infinite direct sum, which naturally introduces products.",
    r"Context comparison: `ps6.tex`, §111, manuscript pp. 450–451, **adds** the completion $\prod_i\Gamma^i$, and §124, manuscript pp. 528–529, **differs** by considering derived perfect duality and the failure of a broader autoduality; neither automatically proves these explicit transposition formulas."
), results="WG2 §2.4 #5")

add("R032", "Normalization and the homotopy argument", "The normalization representability formula leaves compatibility checks", "self-flagged", "225", "Proposition 6 and final line of its proof", [r"normalization", r"Kan-Dold-Puppe", r"integrator"], (
    r"After deriving $ND_i(L_*)\simeq\operatorname{Hom}_{k,*}(\Lambda^i\Phi_*,L_*)$, the proof expressly says “il reste à faire de petites vérifications de compatibilité”, so objectwise representability has not yet been promoted on the page to the full asserted identification of complexes.",
    r"The missing checks include naturality, the transpose differential, and the special degree-zero object, particularly because the argument invokes propositions 3–5 that are not supplied as a continuous preceding proof here.",
    r"Context comparison: `ps7.tex`, §134, manuscript pp. 558–559, **adds** a warning that the standard integrator functor must still be normalized to obtain the Dold–Puppe equivalence, making this distinction directly relevant without establishing the omitted compatibilities."
), results="PRETOT A.12; TOTASPH C.10; PATHS A.6 (index-category distinction only)")

add("R033", "Normalization and the homotopy argument", "The cancelled normalization draft carries a different exterior index", "withdrawn in same text", "225–226", "live Proposition 6 and cancelled Proposition 6", [r"normalization", r"Dold", r"integrator"], (
    r"The cancelled proposition on scan 226 uses $C_*^i=\Lambda^{i+1}\Phi_*$ in its representing formula, whereas the live Proposition 6 on scan 225 uses $\Lambda^i\Phi_*$ and singles out degree zero.",
    r"The cancellation is documentary evidence that the first displayed form was withdrawn, but scan order alone does not establish which leaf was composed first or whether an intervening reindexing explains every difference.",
    r"Context comparison: these leaves **add** a local indexing issue to the normalization discussion in `ps7.tex`, §134, manuscript pp. 558–560; the supplied context contains neither the earlier propositions nor a matching correction, so neither formula should be silently made identical to the other."
))

add("R034", "Normalization and the homotopy argument", "Applying an arbitrary functor preserves the explicit simplicial homotopy", "unpursued implication", "227", "Proposition 1 and Corollary 1.1", [r"homotopism", r"projective", r"Gamma"], (
    r"The conclusion “Pour tt. foncteur $F$ … $F(\Phi_*)$ est homotopique à $F(0)$” uses an actual simplicial homotopy transferred from the two-term normalization $k\xrightarrow{1}k$, whose component identities can be preserved by any functor.",
    r"It should not be enlarged into the assertion that an arbitrary nonlinear functor preserves arbitrary quasi-isomorphisms, since the stronger explicit homotopy is the point of the argument.",
    r"Context comparison: `ps6.tex`, §111, manuscript pp. 455–456, **restates** exactly this distinction in its projective-resolution argument for $\Gamma$, and `ps7.tex`, §134, manuscript p. 560, **adds** the projectivity conditions under which weak equivalences are strict abelian homotopisms."
), results="WG2 §2.4 #5")

add("R035", "Normalization and the homotopy argument", "The derived exterior-power question depends on the meaning of the right-hand side", "self-flagged", "229", "sauf erreur and est-ce vrai margin", [r"projective", r"Gamma", r"Kan-Dold-Puppe"], (
    r"The proposed general identification $(L\Lambda^i)(L_\bullet)\simeq\Lambda^i(L_\bullet)$ for degreewise projective chain complexes is explicitly qualified by “sauf erreur” and “est-ce vrai ?”.",
    r"If the right-hand side means normalize the degreewise exterior power after Dold–Puppe denormalization, projective models provide the appropriate construction, but if it means apply $\Lambda^i$ separately to each chain term, even $L_\bullet=k[1]$ and $i=2$ gives zero on that naive right-hand side instead of the asserted $k[2]$.",
    r"Context comparison: `ps6.tex`, §111, manuscript pp. 455–456, **adds** the relevant projective simplicial-resolution argument, and `ps7.tex`, §134, manuscript p. 560, **restates** its strict-homotopy input; those passages support a convention-sensitive answer rather than an unqualified yes."
), results="WG2 §2.4 #5")

add("R036", "Normalization and the homotopy argument", "The probable minimal exterior model has a direct verification", "own idea", "227, 229", "Il est probable que (Λ^iΨ_*)^!=k[i]", [r"normalization", r"projective", r"Dold"], (
    r"For the standard simplicial $K(\mathbb Z,1)$ identified with $\Psi_*$, degree $n$ has rank $n$, hence $\Lambda^i\Psi_n$ has rank $\binom ni$, and the Dold–Kan splitting implies that the ranks of its normalized terms are the binomial inverse of this sequence, namely one in degree $i$ and zero elsewhere.",
    r"Those normalized terms are direct summands of finite free abelian groups, so the vanishing of their ranks is actual vanishing, and the normalization projector commutes with base change to any $k$, yielding $N\Lambda^i\Psi_*\simeq k[i]$ after fixing the standard orientation.",
    r"Confidence is **high** because the argument uses a split integral normalization before base change, avoiding a false inference from ranks over a general ring; it verifies the manuscript’s “Il est probable” claim and is not proposed as a new theorem.",
    r"Context comparison: this **adds** a concrete verification to the projective normalization discussion in `ps7.tex`, §134, manuscript pp. 559–560, and supplies the flat model needed by **136-pd-de-rham-shadows**."
), results="Hua: 136-pd-de-rham-shadows", confidence="high")

add("R037", "Normalization and the homotopy argument", "The symmetric and divided-power variants need a separate reading and test", "own idea", "229", "NB b, Ψ^* and inserted tensor expression", [r"Gamma", r"symmetric", r"projective", r"divided powers"], (
    r"The claim that “Les mêmes arguments” make $\Gamma^i(\Psi^*)$ and $\operatorname{Sym}^i(\Psi^*)$ into $K(k,i)$ has a superscript star and an inserted tensor expression in the frozen reading, so the variance and the exact list of functors must first be established.",
    r"Conditionally interpreting these as the ordinary degreewise functors on the simplicial $K(\mathbb Z,1)$ from scan 227, normalized $\Gamma^2$ is $\mathbb Z\xrightarrow{\pm2}\mathbb Z$ in degrees two and one, while normalized $\operatorname{Sym}^2$ has the corresponding differential $\pm1$, so neither is $K(\mathbb Z,2)$.",
    r"Confidence is **high for this conditional test**, because with bar coordinates $x,y$ the normalized degree-two generators are $xy-2y^{(2)}$ and $xy-y^2$, whose first faces give respectively $-2x^{(2)}$ and $-x^2$; it does not settle the intended meaning of $\Psi^*$ or the insertion.",
    r"Context comparison: this **adds** a check beyond the projectivity discussion in `ps6.tex`, §111, manuscript pp. 455–456, which does not claim that all three nonlinear functors have the same derived values, and it prevents extending **136-pd-de-rham-shadows** using NB b without further evidence."
), results="Hua: 136-pd-de-rham-shadows", confidence="high")

add("R038", "Normalization and the homotopy argument", "The tensor shift uses a free normalized model", "unproved claim", "229, 231", "Corollary 1.4 and Eilenberg–Zilber argument", [r"tensor", r"projective", r"Kan-Dold-Puppe"], (
    r"Corollary 1.4 states $\pi_\ell(A_*\otimes\Lambda^i\Psi_*)\simeq\pi_{\ell-i}(A_*)$ for an arbitrary simplicial $k$-module, and scan 231 appeals to Eilenberg–Zilber, Dold–Puppe, and Künneth.",
    r"The explicit free model $N\Lambda^i\Psi_*\simeq k[i]$ from R036 explains why no extra flatness of $A_*$ is needed here: tensoring with this model is an ordinary shift, whereas replacing it only by an unspecified quasi-isomorphic complex would require a tensor-flatness argument.",
    r"Context comparison: `ps6.tex`, §111, manuscript pp. 455–456, and `ps7.tex`, §134, manuscript p. 560, **restate** the importance of the projective homotopy model; the page **adds** the particular exterior-power shift used in **136-pd-de-rham-shadows**."
), results="Hua: 136-pd-de-rham-shadows; MPL_134-8_043-087 R033 (tensor method)")

add("R039", "Normalization and the homotopy argument", "The chain boundary and final homotopy label have unresolved literal issues", "reading question", "231", "opening boundary formula and displayed Künneth conclusion", [r"boundary", r"normalization", r"Kan-Dold-Puppe"], (
    r"The frozen text writes $\partial_n=\sum_0^n\partial^*_{i,n}$ without alternating signs, and later places $\pi_{\ell-i}(A_*\otimes B_*)$ beneath $H_{\ell-i}(A_*^!)$, although Corollary 1.4 on scan 229 has $\pi_{\ell-i}(A_*)$.",
    r"Unless the face notation already incorporates signs, the unsigned boundary cannot define the usual chain complex over $\mathbb Z$—on a constant simplicial module its consecutive degree-two and degree-one maps compose to multiplication by six—so both spots deserve a convention check, not a silent correction.",
    r"Context comparison: `ps7.tex`, §134, manuscript pp. 558–560, **adds** the distinction between standard chains and normalization but does not supply a signed-face convention for this leaf; the affected argument is a step of **136-pd-de-rham-shadows**."
), results="Hua: 136-pd-de-rham-shadows")

add("R040", "Normalization and the homotopy argument", "From contractible components to a flasque resolution", "unproved claim", "231–233", "sont flasques and resolution truncation", [r"flasque", r"sections", r"topos", r"integrator"], (
    r"The passage from the homotopy calculation of $\mathcal A_*^{p,i}$ to “sont flasques” and then to a resolution computing $R\Gamma(X,k)$ is the main categorical step left compressed in scans 231–233.",
    r"A complete proof should specify the presheaf category and the meaning of flasque, verify the requisite extension or section-acyclicity property for the contractible simplicial modules, and explain the augmentation identifying the vertical complex as a resolution of $k_*$.",
    r"Context comparison: `ps7.tex`, §134, manuscript pp. 558–560, **adds** an integrator framework, while `ps6.tex`, §127, manuscript pp. 536–538, **differs** by warning about derived sections in a general topos; neither permits this explicit simplex argument to be transferred to every topos without proof."
), results="Hua: 136-pd-de-rham-shadows; WG H6 (not settled)")

add("R041", "Normalization and the homotopy argument", "The truncation step itself is compatible with a left-exact section functor", "own idea", "233", "definition of Φ^{p,i} and τ≤pΓ comparison", [r"sections", r"derived category", r"truncat"], (
    r"The displayed truncation uses $Z^p$ in its last degree, so once the claimed flasque resolution is available, the identity $\Gamma(X,\tau^{\le p}K)=\tau^{\le p}\Gamma(X,K)$ follows at the level of complexes because sections preserve kernels.",
    r"The resulting formula computes $H^i$ only for $i\le p$ and zero for $i>p$, exactly as the page states, while multiplication sends weights $p,q$ to $p+q$ rather than closing on a single truncated complex.",
    r"Confidence is **high** for the truncation calculation because it uses left exactness alone, but it is conditional on the resolution and acyclicity checks in R040.",
    r"Context comparison: this **adds** a precise verified step to **136-pd-de-rham-shadows** and **differs** from the broader unresolved section-functor questions in `ps6.tex`, §127, manuscript pp. 536–538."
), results="Hua: 136-pd-de-rham-shadows", confidence="high")

add("R042", "Normalization and the homotopy argument", "Completion begins a further problem at the end of the packet", "unproved claim", "233", "last paragraph defining S^[i]", [r"complet", r"pro-module", r"ground ring"], (
    r"After the cohomology formula, the text begins “Quitte à remplacer $S$ par son séparé complété” and assumes a topology controlled by ideals generated, or contained in closures of ideals generated, by the higher $t^{(j)}$.",
    r"No completed comparison theorem is concluded on this leaf, so extending earlier formulas to infinite sums requires specifying the topology, continuity of the endomorphisms, completed tensor products where needed, and the relevant compatibility with base change.",
    r"Context comparison: `ps6.tex`, §111, manuscript pp. 450–451, **restates** the need for completed divided powers, and §124, manuscript pp. 521–522, **adds** a pro-module warning for ring extension; these are relevant checks for **136-automorphism-group-scheme**, not a proof of its representability conclusion."
), results="Hua: 136-automorphism-group-scheme; WG2 §2.4 #5")

add("R043", "Earlier findings and the literature", "Assessment of 136-pd-de-rham-shadows", "reading question", "227, 229, 231, 233", "homotopy calculations and H_DRpd display", [r"136-pd-de-rham-shadows", r"2\.4 #5", r"De.?Rham"], (
    r"The Hua entry in `notes/RESULTS_STATE.md`, line 126, calls the “shadows” statement a conjecture candidate, but scans 231–233 explicitly state the weightwise additive comparison, with a proof outline rather than a question mark on that conclusion.",
    r"Its complementary index $a$ in $\Gamma^a\Phi\otimes\Lambda^i\Psi$ must be related to the manuscript’s total weight by $p=a+i$; fixing $a$ does not define a cochain subcomplex because $d$ lowers that exponent while raising the exterior degree.",
    r"Context comparison: the manuscript **restates** the register’s additive pattern after this reindexing but **qualifies** any multiplicative or novelty claim, and the cited scan range also includes reused typescript at scans 228, 230, and 232 that does not prove the PD statement.",
    r"The weight/product distinction in R003 and the Cartan–Miller literature comparison in R046 should be entered under this ID, while the register’s earlier “search found no reference” remains an unreviewed search report."
), results="Hua: 136-pd-de-rham-shadows; WG2 §2.4 #5")

add("R044", "Earlier findings and the literature", "Assessment of 136-automorphism-group-scheme", "reading question", "190–212, 233", "corrected extension, semilinearity, and completion", [r"136-automorphism-group-scheme", r"automorphism", r"complet"], (
    r"The Hua entry in `notes/RESULTS_STATE.md`, line 127, reports a classification by $(\varphi_0,A'_1,(B'_i))$ with a third condition $(2B'_i)J'=0$ and infers an affine group scheme, whereas these pages directly show the narrower correction “faux tel quel” with $2B_i=0$ in the universal base case.",
    r"Scans 204–212 **add** semilinear and torsion-sensitive information, but the general target ideal $J'$, the full earlier argument on the unprovided pages, and a proof that the completed automorphism functor is represented by a single affine group scheme are not available here.",
    r"Representability still requires a precise category of bases, continuity and completion conventions, polynomial or inverse-limit equations, and invertibility conditions; the endomorphism monoid and the diagram marked “(??)” do not establish those points by themselves.",
    r"Context comparison: this is **partial confirmation with explicit limits** of the register lead, and the completion warning in `ps6.tex`, §124, manuscript pp. 521–522, **adds** another issue to check rather than an automatic proof of the reported conclusion."
), results="Hua: 136-automorphism-group-scheme")

add("R045", "Earlier findings and the literature", "The later failure of a Γ-based schematization is a different assertion", "unpursued implication", "227–233", "ΓΦ⊗ΛΨ and the comparison conclusion", [r"Illusie", r"Breen", r"binomial", r"W_2"], (
    r"Context comparison: `ps6.tex`, §119, manuscript pp. 500–503, **contradicts** a later proposal that schematic linearization via derived $\Gamma$ computes ordinary $K(\pi,n)$ homology, citing Illusie/Breen and exhibiting the nonsplit integral extension represented by $1+at+bt^2$.",
    r"Its splitting equation $P(a+a')=P(a)+P(a')+aa'$ leads to $P(t)=t(t-1)/2+ct$, hence to integer-valued binomial polynomials instead of polynomials with integral coefficients, while the text explicitly distinguishes PD de Rham linearization from the unipotent-bundle approach.",
    r"This later retraction therefore **differs** from, and does not itself refute, the weighted cohomology assertion of scan 233; it supplies a warning against converting that assertion into the full schematization claim of **WG H6** or the larger ambitions of **WG2 §Week #3**."
), results="WG H6; WG2 §Week #3; Hua: 136-pd-de-rham-shadows")

add("R046", "Earlier findings and the literature", "Cartan–Miller is the closest verified comparison for the weighted shape", "unpursued implication", "204, 231, 233", "simplex PD algebra and weightwise cohomology", [r"Cartan", r"Miller", r"136-pd-de-rham-shadows"], (
    r"The construction $\Gamma(\Phi)\otimes\Lambda(\Psi)$ and “$i\le p$” comparison have the same weighted architecture as the Cartan–Miller polynomial-form theory, which Cenkl and Porter (1982, p. 9) describe as a bigraded algebra of compatible forms on simplices with divided-power coefficients.",
    r"Their integration map induces cohomology comparison but is not itself an algebra map, so a chain-level identification of presentations, grading conventions, and comparison maps would be needed before declaring the two constructions identical.",
    r"Context comparison: this **adds** a concrete literature route to the Cartan (1976) and Miller (1978) leads in `README.md`, lines 22–23, and **qualifies** the absence-of-reference implication in **136-pd-de-rham-shadows**; this review verified Cartan’s publisher metadata and Miller’s bibliographical entry but did not obtain and read their complete original papers."
), results="WG2 §2.4 #5; Hua: 136-pd-de-rham-shadows")

add("R047", "Earlier findings and the literature", "Higher operations explain why strict integral products need care", "unpursued implication", "217, 220, 233", "cochain PD structure and comparison", [r"operations", r"Cartan", r"Miller"], (
    r"Cenkl (1989, pp. 21–25) explains that the Cartan–Miller product corresponds to integral cup products with additional factors and constructs higher operations from the form complex, while Theorem 2 on pp. 32–33 rules out the commutative cochain problem over $\mathbb Z$ under the functorial acyclic-model and comparison hypotheses specified there.",
    r"This result is stronger in a different direction than the elementary PD obstruction in R004, and its precise hypotheses should be retained rather than turning it into a claim that no algebraic integral model of any kind can exist.",
    r"Context comparison: this **adds** a necessary product-and-higher-homotopy qualification to **WG2 §2.4 #5** and the S11(i) wording in `README.md`, lines 17–21; `ps6.tex`, §120, manuscript pp. 506–507, **restates** the interest in extra operations without supplying these later comparison homotopies."
), results="WG2 §2.4 #5; Hua: 136-pd-de-rham-shadows")

add("R048", "Earlier findings and the literature", "Dwyer’s tame theory is a comparison lead, not an equivalence proved here", "unpursued implication", "222, 231, 233", "invertible-weight homotopies and truncation", [r"Dwyer", r"tame", r"Cartan"], (
    r"The manuscript’s “degré total” and “tronquant” calculations suggest comparing denominator control with Dwyer’s tame homotopy theory, a lead already named in `README.md`, line 23.",
    r"Dwyer’s original publication was bibliographically verified, and the primary research account of Scheerer and Tanré (1991, pp. 375–376) describes an equivalence for suitably reduced simplicial sets and differential graded Lie algebras in a tame setting, with coefficient restrictions and a tame range.",
    r"Context comparison: this **adds** a precise question—how the manuscript’s weight filtration matches those bounds—but the retained pages give no comparison functor or equivalence, so the analogy neither proves S11(i) in its strongest form nor settles **WG H6**."
), results="WG2 §2.4 #5; WG H6 (not settled)")

add("R049", "Earlier findings and the literature", "Mandell concerns E∞ structure and homotopy type", "unpursued implication", "217, 231, 233", "PD algebra versus cohomological comparison", [r"Mandell", r"schemat", r"WG H6"], (
    r"Mandell (2006) proves that finite-type nilpotent spaces are classified up to weak equivalence by their integral cochains as $E_\infty$ algebras, while the induced cochain functor is faithful but not full.",
    r"The “$\mathbb R\Gamma(X,k)$” formula on scan 233 only identifies additive cohomology in a weight range, and scans 215–217 prescribe PD identities rather than an explicit $E_\infty$ enhancement and comparison, so Mandell’s conclusion cannot be read back into those pages.",
    r"Context comparison: this **adds** the relevant modern distinction to the Mandell lead in `README.md`, line 23, and **differs** from **WG H6**, which asks about finite-dimensional local systems and a localizer rather than the fully specified integral cochain object."
), results="WG H6; WG2 §2.4 #5")

add("R055", "Research points on reused typescript", "Fixed parts and the extension of the Néron property", "unproved claim", "189, 191", "Theorem 5.8, Corollary 5.9, and Proposition 5.6", [r"Barsotti", r"N.ron", r"Raynaud", r"Tate"], (
    r"The reused text attributes Theorem 5.8 to Raynaud and says the “propriété ‘néronienne’” extends to maps from ind–Barsotti–Tate groups without a smoothness hypothesis, under the stated semistable, henselian, and characteristic assumptions.",
    r"The local justification invokes Tate’s theorem and the fixed-part factorization rather than providing its full proof; Proposition 5.6 on scan 191 supplies the toric and pro-étale descriptions needed to interpret that factorization.",
    r"Context comparison: no matching Barsotti–Tate or Néron proposition was found in `ps6.tex`, `ps7.tex`, or `notes/RESULTS_STATE.md`, so these pages **add separate reused-source material**, not evidence that the handwritten PD complex was being applied to abelian varieties."
))

add("R056", "Research points on reused typescript", "The perfect duality theorem explicitly postpones its general proof", "unproved claim", "195, 197, 199", "Theorem 5.4 and references to 7.4.6", [r"Raynaud", r"duality", r"Tate", r"abelian"], (
    r"Theorem 5.4 on scan 197 asserts perfect duality of the abelian parts of the two special fibres, while scan 195 says “La démonstration … va être donnée au n° 7” and scan 199 promises a direct argument “plus bas (7.4.6)”.",
    r"Scan 199 distinguishes the easier $\ell\ne p$ case from the use of Tate’s theorem in mixed characteristic at $\ell=p$, so those qualifications cannot be removed when assessing what this fragment proves.",
    r"Context comparison: no corresponding theorem or its §7 proof is present in the supplied context; it **differs** from the abstract derived duality discussed in `ps6.tex`, §124, manuscript pp. 528–529, and has no direct RESULTS_STATE entry."
))

add("R057", "Research points on reused typescript", "The all-primes orthogonality step is identified and partly reduced on the page", "self-flagged", "201", "5.2.6 through 5.3", [r"orthogonal", r"Barsotti", r"duality"], (
    r"The sentence “Il reste à prouver … sans restriction sur $\ell$” isolates the extension of the toric/fixed-part inclusion to $\ell=p$, after which the page gives a rank-and-strictness argument and invokes the orthogonality theorem.",
    r"It should therefore be recorded as a self-identified step with a written reduction, rather than automatically classified as an entirely abandoned proof; checking the reduction requires the earlier theorem and the precise meaning of strict sub–pro-groups.",
    r"Context comparison: no matching orthogonality proof occurs in `ps6.tex`, `ps7.tex`, or `notes/RESULTS_STATE.md`, so this **adds** a dependency within the reused text and does not advance the PD-cochain comparison."
))

add("R058", "Research points on reused typescript", "Specialization rigidity of Barsotti–Tate morphisms is left to the reader", "unproved claim", "203", "Lemma 5.2.5 and final paragraph", [r"Barsotti", r"isogen", r"biextension"], (
    r"For the specialization test for a null morphism, isogeny, or isomorphism, the text says “Nous laisserons au lecteur la démonstration (facile)” and then promises the needed special cases in §7.4.7.",
    r"A proof must retain the connected noetherian base and the pro–Barsotti–Tate setting and justify how the finite-level or height conditions pass from the special fibre; those details are not present on this face.",
    r"Context comparison: the context contains neither that proof nor a matching RESULTS_STATE entry, so this **adds** a separate deferred lemma of the reused source rather than a corollary of the simplicial PD calculations."
))

add("R059", "Research points on reused typescript", "A formerly conjectured good-reduction criterion is presented as a corollary", "unproved claim", "205", "Corollary 5.10 and its unfinished proof", [r"bonne r.duction", r"Raynaud", r"Tate", r"conject"], (
    r"The parenthesis “C’est le résultat conjecturé dans [8, 4.9]” refers to the criterion equating good reduction of $A_K$ with good reduction of its pro-$\ell$ Barsotti–Tate group, with $\operatorname{char}K=0$ stipulated when $\ell=p$.",
    r"It is announced here as Corollary 5.10 with a proof begun, first in the semistable case and then after finite Galois extension, so it is not a newly posed conjecture in this packet; the retained page stops before that general argument finishes.",
    r"Context comparison: no corresponding reduction criterion was found in the supplied PS chapters or register, and the occurrence of an abelian scheme **differs** from the proposed PD-lecture examples in `README.md`, line 21."
))

add("R060", "Research points on reused typescript", "The completeness hypothesis is declared dispensable elsewhere", "unproved claim", "209", "footnote to the definition of the formal toric part", [r"complet", r"toric", r"Raynaud"], (
    r"The footnote says “Cette hypothèse n’est d’ailleurs pas essentielle, comme on montre dans 6.1 ci-dessous”, referring to completeness of the trait used to construct the compatible formal tori.",
    r"The promised §6.1 is absent from these retained pages, so the extension beyond completeness is a deferred claim in this excerpt, not supplied by the separate completion paragraph about PD rings on scan 233.",
    r"Context comparison: `ps6.tex`, §111, manuscript pp. 450–451, and §124, manuscript pp. 521–522, **differ** by treating completion in schematization, and no matching removal of this formal-geometric hypothesis occurs in the context or register."
))

add("R061", "Research points on reused typescript", "The algebraic description of the uniformization map is explicitly unavailable to the writer", "self-flagged", "230", "Remark 14.1.12 a", [r"Raynaud", r"arithm", r"alg.bric", r"uniform"], (
    r"After referring existence of $e$ to Raynaud, the text says “Je n’en connais aucune description purement algébrico-géométrique” for the homomorphism $i$, and promises an “arithmétique” characterization in §14.4.",
    r"This records the author’s stated limitation at the time of this typescript, alongside a proposed route through finite type over $\mathbb Z$; the missing §14.4 and subsequent literature would have to be checked before calling it an open problem today.",
    r"Context comparison: neither `ps6.tex` nor `ps7.tex` supplies that uniformization description, so the passage **adds** a separate self-flagged question and does not identify the “constructions universelles” sought by `README.md`."
))

add("R062", "Research points on reused typescript", "The dual uniformization map carries an unresolved sign", "self-flagged", "230, 234", "Remark 14.1.12 b and biextension trivializations", [r"biextension", r"duality", r"sign"], (
    r"The proposed identification with the homomorphism for the dual abelian scheme ends “à moins que ce ne soit l’opposé ???”, an explicit unresolved sign qualification.",
    r"A resolution would have to trace the biextension duality and trivialization conventions of scan 234 through the two analytic exact sequences; replacing the map by its negative without that check would erase a real question in the source.",
    r"Context comparison: no corresponding biextension sign convention was found in the supplied context, while `ps6.tex`, §124, manuscript pp. 528–529, **differs** by discussing abstract duality rather than this uniformization map."
))

add("R063", "Research points on reused typescript", "Trivializations and lifts are asserted to correspond canonically", "unproved claim", "234", "on vérifie immédiatement before (14.1.5)–(14.1.6)", [r"biextension", r"trivial", r"universal"], (
    r"The phrase “on vérifie immédiatement” introduces a canonical bijection between trivializations of $E_K$ and lifts $i:\underline M_K\to G_K$, or symmetrically lifts on the dual side.",
    r"Checking the correspondence requires the earlier extension data and the convention for the canonical biextension $W_K^{\natural}$, whose natural signs were inserted on the sheet; it is also the local input for the sign question in R062.",
    r"Context comparison: this **adds** a universal-property calculation from the reused source, but searches found no matching biextension construction in `ps6.tex`, `ps7.tex`, or `notes/RESULTS_STATE.md`, and it should not be renamed a universal construction of the PD lecture."
))

add("R064", "Research points on reused typescript", "The algebraic and analytic Tate-module maps are claimed to agree", "unproved claim", "228, 232, 234", "14.2, especially (14.2.2)–(14.2.3)", [r"monodrom", r"Tate", r"rigid", r"comparison"], (
    r"Scan 228 asserts that the maps “provenant de la théorie algébrique” are the same as those “provenant de la théorie transcendante”, after deriving torsion and Tate-module exact sequences from analytic uniformization.",
    r"The page begins a reduction to the semistable situation but breaks off, while scans 232 and 234 provide adjacent comparison and uniformization data rather than the missing end of that proof.",
    r"Context comparison: no matching analytic/algebraic Tate-module comparison occurs in the supplied context, so these pages **add separate material** and are not intermediate pages of the proof of **136-pd-de-rham-shadows**, despite lying inside its quoted scan range."
), results="Hua: 136-pd-de-rham-shadows (provenance correction)")

add("R065", "Research points on reused typescript", "Stoia’s Gorenstein note is a separate attributed text", "unproved claim", "216, 218", "title, theorem, and proper-flat corollary", [r"Gorenstein", r"Stoia", r"flat", r"Ext"], (
    r"The title “POINTS DE GORENSTEIN D’UN MORPHISME / par Manuela STOIA” introduces openness of the fibrewise Gorenstein locus for a flat morphism, and the retained final page gives the proper-flat corollary on the base and a Tor-based flatness argument.",
    r"Only these separated portions of the article are present, so its complete proof cannot be reconstructed from this packet alone, and its assertions must be attributed to the named reused text rather than to Grothendieck’s PD notes.",
    r"Context comparison: no Gorenstein or Stoia discussion was found in the supplied PS chapters or results register; this **differs** from the cochain project even though flatness and duality vocabulary overlap."
))

add("R066", "Endomorphisms and universal operations", "The image of dX0 has a literal discrepancy with later formulas", "reading question", "192, 210, 212", "first system on scan 192; φ1(dX0)=dξ1 later", [r"differential", r"136-automorphism", r"De.?Rham"], (
    r"The frozen transcription of scan 192 reads $\varphi(dX_0)=1+df$, whereas scans 210 and 212 write $\varphi_1(dX_0)=d\xi_1$, and the formula $\varphi(X_0)=X_0+f+B_1dX_0$ would normally produce $dX_0+df$ in this one-variable relative complex.",
    r"This may reflect an implicit identification of the differential basis with one or a local omission, but the discrepancy must remain a reading question because the frozen page cannot be regularized from the later mathematics.",
    r"Context comparison: no matching coefficient convention appears in `ps6.tex` or `ps7.tex`; the page **adds** a literal qualification to the endomorphism data summarized by **136-automorphism-group-scheme**."
), results="Hua: 136-automorphism-group-scheme")

add("R050", "Earlier findings and the literature", "Ekedahl connects the binomial thread to integral models", "unpursued implication", "227–233", "K(k,i) calculations and integral comparison", [r"Ekedahl", r"binomial", r"Symbin"], (
    r"Ekedahl (2002) constructs numerical models for nilpotent homotopy types with finitely generated homology, using polynomial maps with rational coefficients that take integral values, and relates these models to localization and completion.",
    r"Context comparison: this **develops** the integer-valued-polynomial direction formulated in `ps6.tex`, §119, manuscript pp. 502–503, rather than automatically identifying it with the PD form algebra of scan 233.",
    r"For **WG2 §Week #3** and **WG H6**, the useful comparison question is how the numerical model, its cochains, and the weighted PD complex are related by explicit functors under their finiteness and nilpotence assumptions, not whether similar integral terminology alone proves equivalence."
), results="WG2 §Week #3; WG H6")

add("R051", "Earlier findings and the literature", "Toën’s integral affinization has a different structural coefficient sheaf", "unpursued implication", "204, 233", "base rings and the cohomology comparison", [r"To.n", r"binomial", r"module structure", r"topos"], (
    r"For simply connected finite-type spaces, Toën (2020, Theorem 0.1) identifies the homotopy sheaves of integral affinization as $\pi_i(X)\otimes\mathbb H$, where $\mathbb H$ is the Hilbert additive group whose functions are integer-valued polynomials, and establishes faithfulness and detection of equivalence classes.",
    r"Context comparison: this **adds** a later answer to the structural-sheaf questions in `ps6.tex`, §127, manuscript pp. 537–538, and follows the binomial direction of §119, manuscript pp. 502–503; it **differs** from simply tensoring the manuscript’s constant coefficient ring $k$ into ordinary homotopy groups.",
    r"The theorem supplies neither a definition of the absent “topos de De Rham” on these leaves nor the local-systems classification in **WG H6**, and it should not be cited as a direct proof of the specific weighted-product assertions left to check here."
), results="WG H6; WG2 §Week #3")

add("R052", "Earlier findings and the literature", "Horel makes the binomial comparison sharper, with explicit restrictions", "unpursued implication", "215, 217, 233", "PD structure and cochain comparison", [r"Horel", r"binomial", r"B7", r"WG H6"], (
    r"Horel (2024, introduction, Theorem 5.4, and §8) constructs a homotopy theory of cosimplicial binomial rings whose cochain functor is fully faithful on nilpotent finite-type spaces; its adjunction unit is integral completion for connected finite-type spaces.",
    r"His Remark 8.5 also distinguishes the resulting binomial affine homotopy type from Toën’s ordinary affinization, so even these two later constructions should not be conflated, still less identified with $\Gamma$ merely because both involve factorial expressions.",
    r"Context comparison: this **adds** a precise realization of the binomial expectation in `ps6.tex`, §119, manuscript pp. 502–503, and supports the literature bridge B7 named in `README.md`, line 23, while leaving the manuscript-to-binomial comparison and **WG H6** unresolved."
), results="WG H6; WG2 §Week #3; README bridge B7")

add("R053", "Earlier findings and the literature", "Concrete enhanced cochains do not settle the bare-derivator construction", "unpursued implication", "204, 215, 221, 233", "explicit algebraic input data and functors", [r"GALOIS G\.6", r"GALOIS E\.11", r"RESIDUE I\.7", r"monoidal"], (
    r"The formulas “$\Gamma^*(M^0)\otimes\Lambda^*M^1$” and $\mathcal A_*(S,S^+,t)$ use a specified base ring, tensor product, grading, differential, and PD ideal, so they demonstrate a construction with substantial enhancement data.",
    r"Context comparison: they therefore **differ** from the open requests **GALOIS G.6**, **GALOIS E.11**, and **RESIDUE I.7** in `notes/RESULTS_STATE.md`, lines 13, 24, and 32, which ask for a functorial higher-coefficient assignment from an arbitrary bare derivator without such chosen enhancement.",
    r"The pages offer a concrete model to test after suitable extra structure is supplied, but neither a proof nor a counterexample for those general assignments, and their recorded open status should remain unchanged."
), results="GALOIS G.6; GALOIS E.11; RESIDUE I.7")

add("R054", "Earlier findings and the literature", "Constant-coefficient cohomology is not the finite-local-systems criterion", "unpursued implication", "227–233", "k_* and RΓ(X,k)", [r"WG H6", r"local systems", r"unipotent", r"pseudo-abelian"], (
    r"The objects “$k_*$” and “$R\Gamma(X,k)$” in the homotopy calculation use constant coefficients, and no reconstruction of categories of finite-dimensional local systems, their monodromy, or a localizer generated by them appears on these leaves.",
    r"Context comparison: this **differs** from **WG H6** (`notes/RESULTS_STATE.md`, line 119), while `ps6.tex`, §127, manuscript pp. 537–538, **adds** hypotheses about fundamental-group actions and pseudo-abelian types that show why such a passage would need more input.",
    r"The strongest supported update is that the packet supplies an integral algebraic cohomology method relevant to the war game, not that it verifies the proposed local-systems characterization of schematization."
), results="WG H6; WG2 §2.4 #5")

add("R018", "Endomorphisms and universal operations", "The multiplication sign in the endomorphism parametrization needs care", "reading question", "206", "substitution law and following parenthesis", [r"composition", r"136-automorphism", r"Omega"], (
    r"The displayed law is substitution, $(\lambda'*\lambda)(T)=\lambda'(T)\lambda(T\lambda'(T))$, but the following parenthesis writes $u_\lambda u_{\lambda'}=u_{\lambda\lambda'}$ without an explicit star in the frozen transcription.",
    r"If the latter juxtaposition meant ordinary multiplication in $S$, it would generally disagree with substitution, so the operation convention must be specified before checking a semidirect-product or representability assertion; the page has not been normalized to the expected notation.",
    r"Context comparison: `ps6.tex`, §120, manuscript pp. 506–507, **adds** the distinction between multiplication and composition of unary operations, and this is a reading question bearing directly on **136-automorphism-group-scheme**."
), results="Hua: 136-automorphism-group-scheme")

add("R019", "Endomorphisms and universal operations", "Semilinear factorization does not by itself finish the simplex classification", "unproved claim", "210, 212", "ξ_i relations and unique factorization remarque", [r"136-automorphism", r"universal", r"divided power"], (
    r"Scan 212 asserts that every $\varphi_1$ factors “de façon unique” as $\psi_1\circ\overline\varphi_0$, then imposes the second augmentation and obtains $\varphi_0(T^{(i)})=\varphi_0(T)^{(i)}$.",
    r"This provides a mechanism forcing preservation of the base divided powers even when it was not initially requested, but extending it to every simplex still depends on the corrected mixed-commutation conditions of scans 194 and 200.",
    r"Context comparison: it **adds** a local semilinear step to **136-automorphism-group-scheme**; no complete arbitrary-base classification or proof of representability is supplied in `ps6.tex` or `ps7.tex`, whose nearest related discussion is §120 of `ps6.tex`, manuscript pp. 506–507."
), results="Hua: 136-automorphism-group-scheme")

add("R020", "Endomorphisms and universal operations", "The last formula on scan 212 appears to specialize the base map silently", "own idea", "210, 212", "β compatibility followed by A_1=X_0+f", [r"136-automorphism", r"ground ring", r"ring extension"], (
    r"Scan 212 first requires $\beta(A_1)=\varphi_0(T)$ but then writes “$A_1=X_0+f$” with $f$ a sum of monomials divisible by both $X_0$ and $X_1$, which vanish under $\beta$ and would instead force $\beta(A_1)=T$.",
    r"Thus those last formulas require an unannounced restriction $\varphi_0(T)=T$, or a different choice of particular lift of $\varphi_0(T)$; the displayed sum also has no coefficient symbols, unlike the surrounding coefficient calculations.",
    r"Confidence is **high** for this compatibility test, because it is obtained by applying the augmentation explicitly defined on the page, while the author’s intended continuation is unknown.",
    r"Context comparison: this **adds** a limitation to **136-automorphism-group-scheme** and **differs** from the unrestricted base-change discussion in `ps6.tex`, §124, manuscript pp. 521–522; it is a research diagnosis, not a correction to the transcription."
), results="Hua: 136-automorphism-group-scheme", confidence="high")
