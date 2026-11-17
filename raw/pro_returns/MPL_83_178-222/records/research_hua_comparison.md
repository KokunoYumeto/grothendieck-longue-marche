# Comparison with Michel Hua's modernised reading of cote 83

Research contribution prepared after the primary reader's freeze at 2026-11-17 17:10:31 UTC and after context access. No scan images were read by this contributor, and no frozen transcription file was changed. The comparisons below use the primary reader's frozen LaTeX, the full 1,964-line supplied `context/hua_project/83.modern.tex`, its README, the package README, and `context/notes/RESULTS_STATE.md`.

## Source status and concordance

**Hua** below always means **Michel Hua's project's AI-produced modernised reading of cote 83**, supplied as `hua_project/83.modern.tex`, downloaded for this context on 14 November 2026. Its header labels it an interpretation, reports an unchecked first pass dated 17 October 2026, says that its bibliography was initially cited from memory, and explicitly lists departures from the source; its references to Lean files are claims about files not supplied here and have not been audited in this comparison. Statements credited to Hua must not be attributed to this transcription project or treated as a diplomatic reading.

For the matched tail of this dossier, **Hua's page number is the current scan number minus one**: Hua p.177 corresponds to scan178, p.182 to scan183, p.188 to scan189, p.210 to scan211, p.218 to scan219, and p.221 to scan222. This follows the matching passages and the frozen marginal numbers; it is not a claim that every page number in the whole archive follows the same offset. For earlier material outside the packet, the references below retain Hua's own page coordinates and do not pretend to be a fresh inspection of those scans.

| Current scans | Hua locator in `hua_project/83.modern.tex` | Relation |
|---|---|---|
| 178–181 | XI, “Extensions $\lambda$-scindées (pages 171 à 180)”, lines 1719–1756 | Summarises the same extension product; preserves flatness and unresolved coherence. |
| 183–192 | XII, “Trois variables (pages 182 à 191)”, lines 1763–1836 | Modernises notation, repairs coefficient/product errors, and retains the invariant-ring question. |
| 193–201 | XII, “Quatre variables, et le cube (pages 191 à 200)”, lines 1838–1875 | Summarises dimension, integrality, and cube arrangement; gives no proof of freeness. |
| 203,205,207 | XIII, “Variables et relations (pages 202 à 206)”, lines 1883–1907 | Identifies the 28 variables and 32 written relations; explicitly propagates the missing product term. |
| 203,209,211,213,215,217,219,221 | XIII, “Les relations linéaires entre les $\Sigma_a$ (pages 202, 208 à 220)”, lines 1909–1944 | Adds an octahedral adjacency interpretation and computes the two determinants. |
| 222 | XIV, “Le feuillet « L 19 » (page 221)”, lines 1947–1962 | Interprets this reused typescript, while most other typescripts are explicitly excluded from Hua's transcription. |

The relevant results-register entries are **LM4 F.7**, **LM4_SUCCESSOR B.38–B.41**, **PUSH_ORDER5_FRAME Itemsfromt 2**, **LM7_PUSH E.65**, and **EXIT_TOWER E.49** only for proposed bridges or their limits. The register has no separate settled entry for the concrete extension, trace-polynomial, or cube-determinant calculations below; attaching an unrelated GT result to them would be misleading.

## Candidate notes: local mathematics and source comparison

### H01 — The packet's actual subject is narrower than the planning title

**File/scans:** 83/178–181,183–221. **Kind:** reading question. **Manuscript anchor:** “opération interne”; “alg. d'Az. de rang 4”; “28 variables”. **Context:** Hua XI–XIII; `README.md`, “This package in our plan”; `RESULTS_STATE.md`, “Orientation for this package”. **Register:** LM4 F.7; LM4_SUCCESSOR B.38–B.41; PUSH_ORDER5_FRAME Itemsfromt 2.

These leaves support Hua's account of the dossier's late shift from polyhedra to affine extension products and matrix invariants, but contain no definition of a level-n polyhedron, no modular-curve map, and no five-point mapping-class relation. Their cube is an indexing device for four matrix variables and their traces, not an asserted icosahedron or a model of $M_{0,5}$. Consequently the open register items remain open on this packet's evidence.

### H02 — The date is attached to a suite, not to each mathematical leaf

**File/scan:** 83/183. **Kind:** reading question. **Manuscript anchor:** “I bis”; “Mai 1986”; “Juillet 1986”. **Context:** Hua XII heading and “Le fil du dossier, et les conventions”. **Register:** orientation question “Which leaves are of 1986”; no mathematical result ID.

Scan183 independently supports Hua's dating of the “I bis” suite to May–July 1986. It does not date each later cube calculation individually or establish a chronology between the separately reused typed drafts. The late algebra should therefore not be silently assigned to the dossier's earlier 1982–83 icosahedral work.

### H03 — Flatness belongs in the extension construction

**File/scans:** 83/178,180. **Kind:** unproved claim. **Manuscript anchor:** “l'injectivité si les $F_i$ sont plats”; “à quotients $F_i$ plats, au besoin”. **Context:** Hua XI, “Extensions $\lambda$-scindées”, pp.175–180. **Register:** no matching settled entry.

Hua correctly keeps the flatness hypothesis in its description of the universal product, and these leaves make its purpose explicit: it is used for injectivity of the left-hand term of the extension. The marginal alternative on scan178 suggests changing the input category or replacing a tensor product by its image, so an arbitrary-base formulation needs to specify which construction is intended. This is a local module-theoretic question, not an application of the tower results in the register.

### H04 — The unit candidate is identified, while coherence remains unverified

**File/scans:** 83/180–181. **Kind:** self-flagged. **Manuscript anchor:** “à vérifier leurs compatibilités !”; “a-t-on une unité ?”; “si $\beta=1$, on retrouve ${}^1E=E$”. **Context:** Hua XI, “Extensions $\lambda$-scindées”, and introductory “Ce que le dossier annonce sans l'établir”. **Register:** no matching settled entry.

Hua lists the unit among unfinished points, but the present text goes far enough to identify $E_1$ as a unit candidate through the displayed functor comparison. What is visibly left unchecked includes the associativity/commutativity compatibility data and their relation to this candidate. A precise follow-up should distinguish constructing unit isomorphisms from proving the coherence of the resulting monoidal category.

### H05 — A category question hidden by the scalar criterion

**File/scans:** 83/180–181. **Kind:** own idea / reading question. **Manuscript anchor:** “ssi $\beta$ est inversible”; “l'idéal somme … et $\lambda k$ est $k$”. **Context:** Hua XI, “Extensions $\lambda$-scindées”, including its formula for $u^\pi$. **Register:** no matching settled entry. **Confidence:** medium; the elementary calculation is clear but the exact morphism category must be recovered from the earlier leaves.

If the two assertions concern the same category with no chosen splitting as part of an object, invertibility of the scalar $\beta$ is not intrinsic, whereas the ideal condition $(\beta,\lambda)=k$ is. In a split model $u_\beta(a,x)=\lambda a+\beta x$, the shear $(a,x)\mapsto(a+cx,x)$ changes the parameter by $\lambda c$, so for $\lambda=1$ the objects with $\beta=0$ and $\beta=1$ are isomorphic although only one scalar is a unit. Hua repeats the two assertions without resolving this distinction; the frozen wording should stand while the category, and any fixed splitting in the functor assertion, is checked.

### H06 — Two bilinear forms must not acquire one definition

**File/scans:** 83/183,188. **Kind:** reading question. **Manuscript anchor:** “$\operatorname{Tr}xy$” underbraced as $\varphi$; later “$\varphi(u,v)=\operatorname{Tr}u\operatorname{Tr}v-\operatorname{Tr}(uv)$”. **Context:** Hua “Conventions, valables pour tout le dossier”; XII, “Trois variables”. **Register:** no matching settled entry.

Hua consistently calls the trace pairing $\varphi$ and the determinant's polar form $\psi$, whereas the current leaves reuse $\varphi$ for different forms on scans183 and188. Its clean notation is useful for analysis but cannot be imported into the diplomatic text. Any subsequent proof must declare which pairing is used before taking its Gram determinant or orthogonal complement.

### H07 — A misleading “and e” in the modernised account

**File/scan:** 83/183, opening argument. **Kind:** reading question. **Manuscript anchor:** “$\det,1$ sans $e$ ne suffisent”. **Context:** Hua XII, “Trois variables”, opening paragraph, lines1768–1777. **Register:** no matching settled entry.

Hua's paragraph says that $\det,1,e$ leave multiplication ambiguous up to the opposite algebra, but the frozen source explicitly says “$\det,1$ sans $e$”. This is a substantive difference in the prose, not merely a notation change: the manuscript proposes using orientation as the missing datum. The exact reconstruction over bases where 2 is not invertible remains a mathematical question, but it must not erase the source's distinction.

### H08 — Perfect trace pairing survives characteristic two

**File/scan:** 83/183. **Kind:** own idea / correction of a context claim. **Manuscript anchor:** “celle-ci est non dég.” **Context:** Hua IX, “Le critère (pages 92 à 99)”, footnote at lines1285–1287; Hua XII opening. **Register:** no matching settled entry. **Confidence:** high; direct matrix-unit calculation.

Hua's earlier footnote says the trace form is degenerate in characteristic two, but for $M_2(k)$ the pairing $(X,Y)\mapsto\operatorname{Tr}(XY)$ has Gram determinant $-1$ on $E_{11},E_{12},E_{21},E_{22}$ over $\mathbb Z$. Thus that statement is false for the full matrix algebra in every characteristic, and scan183's use of nondegeneracy is compatible with the direct calculation. The possible degeneracy of restrictions to a trace-zero subspace must be kept separate from the pairing on the whole Azumaya algebra.

### H09 — Orientation normalization changes within the working notes

**File/scans:** 83/185–189. **Kind:** withdrawn in the same text / reading question. **Manuscript anchor:** “$2(\tau-\tau')=\varepsilon_0\Delta$” (185); “$\tau-\tau'=\varepsilon_0\Delta$” (189). **Context:** Hua XII, “Trois variables”, pp.184–188, coefficient footnote. **Register:** no matching settled entry.

Hua already identifies the factor-of-two problem and chooses the later normalization in its modernised formula. The diplomatic sequence adds the visible overwritten $1/2$ and $1/4$, the unanswered orientation convention, and scan186's reversal of $\tau$ and $\tau'$, so these must be studied as separate working states. This is not evidence for two distinct invariant theories, and the later identity does not authorize silently repairing the earlier leaf.

### H10 — The missing cubic norm term is already a Hua finding

**File/scans:** 83/189,205. **Kind:** unproved claim / own verification of a context finding. **Manuscript anchor:** “$\tau\tau'=\Pi$”. **Context:** Hua XII, “Trois variables”, pp.188–191; XIII, “Variables et relations”, footnote on $\pi_s$. **Register:** no matching settled entry. **Confidence:** high for the displayed specialization; the general corrected identity is credited to Hua pending the independent algebra check.

Hua explicitly records that the written product polynomial lacks $-4cc'c''$, and that the same omission reaches the vertex product formula. With $x=y=z=I_2$ over $\mathbb Z$, the frozen polynomial is 8 while $\operatorname{Tr}(xyz)\operatorname{Tr}(zyx)=4$, confirming a discrepancy without relying on a difficult reading. This packet supplies a full diplomatic record of all three displayed versions on189 and the later reuse on205; the correction belongs in research notes, not the frozen formulas.

### H11 — The three-matrix presentation is still explicitly a question

**File/scans:** 83/190–192. **Kind:** self-flagged / unproved claim. **Manuscript anchor:** “À vérifier”; “finie libre de rang 2”. **Context:** Hua XII, “Trois variables”, pp.189–191. **Register:** no matching settled entry.

Hua calls the characteristic-zero statement classical but explicitly says it has not checked the arbitrary-base assertion; its bibliography is not a substitute for that missing verification. The source asks simultaneously for generation, the sole quadratic relation, and freeness over the nine-variable subring, each of which requires a proof with the corrected product polynomial. Scan192's warning about using $\Delta$ instead of $\tau$ shows why a characteristic-zero proof cannot simply be divided by two and reused integrally.

### H12 — The four-matrix freeness presumption is stronger than the summary

**File/scans:** 83/193–194. **Kind:** conjecture. **Manuscript anchor:** “je présume que $B$ est fini libre de rang $2^4$ sur $A$”; “soumises aux seules relations”. **Context:** Hua XII, “Quatre variables, et le cube”, pp.192–193. **Register:** no matching settled entry.

Hua preserves the fact of a freeness presumption but its prose drops the explicit proposed rank $2^4$ and does not settle the assertion. The present packet therefore adds a sharply testable claim: four quadratic choices are being treated as independent despite the relation among fourteen shorter invariants. The rank, the generating set, and the “only relations” phrase should be tested separately, with no inference from a variable-minus-equation count.

### H13 — Integrality degree is an upper bound, not a rank calculation

**File/scans:** 83/197,199. **Kind:** unproved claim. **Manuscript anchor:** “de degré au plus huit sur $A$”; “divisant”; “de degré 8 (?)”. **Context:** Hua XII, “Quatre variables, et le cube”, pp.196–199. **Register:** no matching settled entry.

Hua correctly reports the degree-eight bound as an integrality argument obtained by grouping two matrices into one. The full transcription preserves the omitted or doubtful coefficient entries, a later question mark, and several intermediate rings, so it does not support promoting this to a proved free rank-eight extension. An explicit corrected monic equation would check integrality, but generic degree and integral module rank would still be separate questions.

### H14 — “Three values” is not the later twelve-variable system

**File/scans:** 83/201,203. **Kind:** withdrawn in the same text / reading question. **Manuscript anchor:** “il n'y a que trois valeurs de $\Sigma_a$” (201); twelve displayed relations (203). **Context:** Hua XII, “Quatre variables, et le cube”, final footnote; XIII, “Les relations linéaires”. **Register:** no matching settled entry.

Hua already notices that the later calculation uses twelve edge quantities rather than retaining scan201's assertion that only direction matters. The current text preserves both stages without an explicit verbal retraction, so “withdrawn” here means abandoned by the later parametrization, not crossed out on the earlier leaf. An analyst should not impose the earlier equality on the later linear system unless an additional specialization is stated.

### H15 — Thirty-two displayed relations are not a proved presentation

**File/scans:** 83/205,207. **Kind:** unproved claim. **Manuscript anchor:** “28 variables”; “32 relations !”; “$\pi_a=$ —”; “expression … un peu compliquée”. **Context:** Hua XIII, “Variables et relations (pages 202 à 206)”. **Register:** no matching settled entry.

Hua lists the vertex and edge sum/product relations but does not claim a complete elimination or a proved invariant-ring presentation. The source itself leaves the edge product polynomial unwritten and carries forward the earlier defective vertex product polynomial. A complete construction would need the actual equations, their dependencies, and a comparison with the invariant ring; the numerical excess of equations does not establish any of these.

### H16 — The octahedral interpretation needs a condition at two

**File/scans:** 83/201,203,215,217. **Kind:** own idea / correction of a context claim. **Manuscript anchor:** “$\tau_f+\tau_{f'}=\Sigma_a$”; the half-sum formulas on215,217. **Context:** Hua XIII, “Les relations linéaires entre les $\Sigma_a$”, injectivity footnote. **Register:** no matching settled entry. **Confidence:** high; the kernel calculation uses only the displayed edge-sum map.

Hua's octahedron interpretation gives the map from six face values to twelve adjacent-pair sums, but its unqualified assertion of injectivity fails over a ring with nonzero 2-torsion. On a connected graph containing an odd cycle, zero edge sums force alternating signs and then $2t=0$, so here the kernel consists of the constant face vector with value $t\in k[2]$. In particular the rank drops from six over $\mathbb Q$ to five over $\mathbb F_2$, explaining why the half-sum reconstruction needs a hypothesis or an integral saturation analysis.

### H17 — The unfinished determinant has a definite value

**File/scan:** 83/211. **Kind:** unpursued implication / verification of a context finding. **Manuscript anchor:** the displayed $6\times6$ matrix and its minors. **Context:** Hua XIII, “Les relations linéaires”, determinant footnote, Hua p.210. **Register:** no matching settled entry. **Confidence:** high; exact integer determinant computation.

Hua reports a determinant of $1024=2^{10}$ for this unfinished calculation. Direct exact computation from the six rows of the frozen matrix gives the same value, so the context finding is supported by this packet rather than newly discovered here. This confirms invertibility after inverting two, but it does not validate the preceding formulas or settle their integral image.

### H18 — The block determinant error has only a two-primary correction

**File/scan:** 83/219. **Kind:** own verification of a context finding. **Manuscript anchor:** “$27^2-1=728$”; “premier à3”; “OK”. **Context:** Hua XIII, “Les relations linéaires”, Hua p.218. **Register:** no matching settled entry. **Confidence:** high; exact block identity and Smith form.

Hua already corrects the number to $512=2^9$: for the written diagonal block $M$, $M^2=9I_3$, and therefore $\det\left(\begin{smallmatrix}M&I_3\\I_3&M\end{smallmatrix}\right)=\det(8I_3)=512$. Exact computation from the frozen matrix confirms this and gives Smith invariant factors $1,1,1,8,8,8$, which refine the statement that the map becomes invertible after inverting two. The source's conclusion “nonzero and prime to3” survives, while the apparent primes7 and13 are artifacts of its determinant calculation.

### H19 — The context's clean formulas cannot decide a doubtful symbol

**File/scans:** 83/190,205,217. **Kind:** reading question. **Manuscript anchor:** rank `\unsure{2}`; `$\det\unsure{y|z}$`; `$b^{\unsure{3|'}}$`. **Context:** Hua XII “Trois variables” and XIII “Les relations linéaires”. **Register:** no matching settled entry.

Hua uses rank4, $\det z$, and consistent primed cube variables in its mathematical exposition, which are plausible intended values but not new evidence about the strokes in this packet. These are context-induced questions to retain beside the frozen uncertainty marks. Since Hua explicitly repairs and renames the source, agreement with a clean modern formula cannot turn the first-pass visual candidate into a confident alternative.

### H20 — The reused typescripts add evidence excluded by Hua

**File/scans:** 83/196,198,200,202,204,208,210,212,214,216,218,220,222. **Kind:** unpursued implication. **Manuscript anchor:** “L17”, “L19”, “L22”; “maison pour tous”; “respect de soi”. **Context:** Hua header exclusions; “Le fil du dossier”; XIV, “Le feuillet « L19 »”. **Register:** no matching mathematical entry; only `MPL_142_001-093 §316` as a bibliography lead for SGA, not a verification of the personal testimony.

Hua expressly excludes most of these typed pages and discusses only the last L19, whereas the packet supplies their complete text and revision states. The duplicate L17 sheets198/204 and L19 sheets196/222, the L22 fragment under the mathematics on200, and the SGA correspondence on208–216 make this a useful textual-history dossier in its own right. The author's allegations and recollections remain testimony to be compared with documents, not independently established historical facts.

## Candidate notes: the planning questions and limits of Hua's evidence

### H21 — A modular-curve keyword is not an established identification

**File/scans:** 83/183,193–207. **Kind:** reading question. **Manuscript anchor:** “Cas de quatre variables”; “28 variables”. **Context:** Hua résumé/keywords, lines184–190; VI “Généralisation : le cône nilpotent”; VII “Classes de nilpotents et carte universelle”; `README.md`, bridge B5. **Register:** LM2 C.d1, C.r1–C.r3 (the return's claims); LM4_SUCCESSOR B.38.

Hua names $X(5)$ as a term to investigate, but nowhere in its supplied exposition writes a map $X(n)\to X(1)$ or proves that it is the polyhedron under discussion. Its earlier congruence-map construction is a relevant lead, while the present packet gives no additional modular identification. Any affirmative answer must therefore come from the explicit modular/cartographic construction and exact quotient conventions, not from Hua's keyword list or from the late cube.

### H22 — Hua supplies an earlier bi-icosahedron model, not a five-point moduli identification

**File/scans:** 83/193–205 (absence of a claimed link). **Kind:** reading question. **Manuscript anchor:** “quatre variables”; four diagonals and six faces in the cube. **Context:** Hua VI “Orientations (pages52 à55)” and “Les groupes (pages55 à59)”; introductory “Ce que seule une lecture d'ensemble peut dire”. **Register:** PUSH_ORDER5_FRAME Itemsfromt 2; LM4_SUCCESSOR B.39–B.41.

Hua defines the earlier bi-icosahedron as two complementary icosahedral structures on twelve vertices and describes its linear groups; these are credited contextual interpretations of leaves outside this packet. Neither its full supplied text nor the current leaves identify that finite combinatorial object with $M_{0,5}$ or construct the required five-point maps. Shared appearances of fivefold symmetry or of a symmetric group therefore supply a research lead, not the missing comparison.

### H23 — Ring-valued polyhedra require explicit geometric and descent data

**File/scans:** 83/178–181,183,192. **Kind:** own idea. **Manuscript anchor:** “sur $k$”; “si $2$ non inv.” **Context:** Hua VII “Les classes $C^*(e)$ (pages64 à68)” and “Triangles et orientation (pages69 à73)”; XI “Extensions $\lambda$-scindées”. **Register:** README question “regular polyhedron over a ring”; no settled formal-definition entry. **Confidence:** medium; a formulation task rather than a proved equivalence.

Hua's earlier nilpotent model depends on a rank-two module, a symplectic generator, square classes, and hypotheses involving $\mu_2(k)$ and 2-torsion in the Picard group. A proposed definition over general rings must state whether vertices are global points, a sheaf, or a scheme, how incidence descends, and what “regular” means for the group action. The late packet reinforces the need to keep bad-prime behavior explicit but supplies no axiom system resolving these choices.

### H24 — Matrix invariants do not compute profinite centralizers or the GT character

**File/scans:** 83/183–205. **Kind:** reading question. **Manuscript anchor:** “$G=\operatorname{Aut}(\mathcal A)$”; “$\mathfrak S_4$”. **Context:** Hua XII–XIII; `RESULTS_STATE.md`, orientation and open entries. **Register:** LM4 F.7; LM4_SUCCESSOR B.38–B.41; EXIT_TOWER E.49; LM7_PUSH E.65.

The algebraic automorphism group and finite permutation actions in these leaves are not, by themselves, the profinite mapping-class centralizers or the GT groups in those register entries. Moreover the manuscript's $\Delta$ is a triple-trace/orientation quantity, whereas the register's $\Delta$ is a character on a profinite group; equal notation is not a constructed map between them. No status in the results register should change on the basis of these leaves or of Hua's modernised matrix calculations.

## Exact computations performed in this comparison

The independent checks were limited to the matrices already transcribed; they are not manuscript-reading checks. SymPy exact arithmetic yielded:

- Scan211 determinant: 1024.
- Scan219 determinant: 512; its diagonal $3\times3$ block squares to $9I_3$.
- Scan219 Smith form, positive invariant factors: $(1,1,1,8,8,8)$.
- Full matrix-algebra trace pairing on $E_{11},E_{12},E_{21},E_{22}$: Gram determinant $-1$.
- For the written scan189 product polynomial at $x=y=z=I_2$, the polynomial evaluates to8 while the trace product is4.

The main research agent is independently checking the trace and cube algebra in a reproducible script. No claim about the unprovided Lean source, whole invariant-ring generation, the full GT pentagon, or a profinite centralizer has been verified here.

## Supplemental review requested by the primary reader

The following items add mathematical questions or scope qualifications not already made in H01–H24. Searches of the supplied LM texts and notes found direct comparisons in `LM_140-3_text.tex` §48 and `LM_140-4_text.tex` scans74–75 and147; the exact $\lambda$-split construction was found in Hua XI but not in the supplied LM texts or returned-package notes. No settled entry of `RESULTS_STATE.md` resolves these local calculations, and no unrelated register status is assigned to them.

### H25 — The universal object must remember the auxiliary multilinear map

**File/scans:** 83/178–179. **Kind:** unpursued implication. **Manuscript anchor:** “un $f$ … correspondant à un $f^\circ$ déjà donné”; “comme application associée”. **Context:** Hua XI, “Le produit $*$”, pp.151–152, and “Extensions $\lambda$-scindées”, pp.174–178. **Register:** no matching settled entry.

Scan179 treats $f^\circ$ as supplied data independent of the freely chosen $g$, which explains why a universal construction for $f$ alone would lose information. In the split formula with $\lambda=0$ and $b_1=b_2=0$, one has $f=g$ for every choice of $f^\circ$, so the extra tensor contribution cannot be recovered from the displayed function. This extends Hua's warning for involutions in characteristic two to the general $\lambda$ construction and should be preserved when formalizing scan178's proposed replacement by an image.

### H26 — Characteristic-two failure of the Delta coordinate need not mean inseparability

**File/scans:** 83/190–192. **Kind:** own idea. **Manuscript anchor:** “$\Delta=\tau+\tau'=\Sigma\in A$”; “$\Delta$ ne risque pas d'engendrer”. **Context:** Hua XII, “Trois variables”; compare `LM_140-3_text.tex`, scans259–260, quadratic subalgebras and characteristic-dependent torus degeneration. **Register:** no matching settled entry. **Confidence:** high, conditional on the proposed corrected quadratic presentation.

For $B=A[\tau]/(\tau^2-\Sigma\tau+\Pi)$ in characteristic two, the derivative is $\Sigma$, so $B/A$ is étale precisely where $\Sigma$ is invertible even though $\Delta$ belongs to $A$. On that open set, $u=\tau/\Sigma$ gives the Artin–Schreier equation $u^2+u=\Pi/\Sigma^2$; on $\Sigma=0$ the situation is instead inseparable or nonreduced according to the fibre. Thus the failure of this particular generator must be separated from ramification, as the earlier LM quadratic-algebra calculations already separate regularity from being a torus.

### H27 — An invariant ring does not classify all simultaneous conjugacy orbits

**File/scans:** 83/190–193. **Kind:** own idea / unpursued implication. **Manuscript anchor:** “fonctions … $G$-invariantes”; “espace quotient”. **Context:** `LM_140-3_text.tex`, §48, scans255–258, especially scan256 “pas un mono”; `LM_140-3_notes.md`, N26–N34. **Register:** no matching settled entry. **Confidence:** high; explicit matrix example.

Even over an algebraically closed field, the triples $(I,I,I)$ and $(I+E_{12},I,I)$ have the same listed traces, determinants, pair traces, and triple trace, but cannot be simultaneously conjugate because their first components are respectively scalar and nonscalar. This realizes for these leaves the distinction already explicit in LM scan256 between the invariant-theoretic quotient and the set or sheaf of all conjugacy orbits. Consequently even a proof of the proposed invariant-ring presentation would not by itself give a fine moduli space of all triples or classify their nonsemisimple orbits.

### H28 — The involution's fixed ring need not commute with specialization

**File/scans:** 83/191,195. **Kind:** own idea. **Manuscript anchor:** “$\tau\longrightarrow\tau'=\Sigma-\tau$”; the $\mathfrak S_2$-labelled ring diagram. **Context:** Hua XII, “Trois variables” and “Quatre variables, et le cube”; compare the arbitrary-base warning in `LM_140-3_text.tex`, scan255. **Register:** no matching settled entry. **Confidence:** high, conditional on the displayed free quadratic algebra.

Writing an element uniquely as $\alpha+\beta\tau$, invariance under $\tau\mapsto\Sigma-\tau$ is equivalent to $2\beta=0$ and $\Sigma\beta=0$. For the universal polynomial ring $A$, $\Sigma$ has unit leading coefficient and is a non-zero-divisor, so this calculation supports the fixed ring $A$ rather than refuting195. After a characteristic-two specialization with $\Sigma=0$, however, the involution becomes the identity and fixes all of $B$. The issue is therefore failure of invariants to commute with such specialization, not a blanket failure of the universal ring diagram.

### H29 — The sign graph gives an explicit lifting condition for invariant coefficients

**File/scans:** 83/195,199–200. **Kind:** unpursued implication. **Manuscript anchor:** “$(\mathrm{id},\mathrm{sg})$”; “$\beta'=-\beta$”; “$\alpha'-\alpha=\beta\sigma$”. **Context:** Hua XII, “Quatre variables, et le cube”; `LM_140-4_text.tex`, scan147, warning that a cyclic-ratio map commutes with $\mathfrak S_3^+$ but not all of $\mathfrak S_3$; `LM_140-4_notes.md`, second-pass S02. **Register:** no matching settled entry.

For a transposition $s$ acting on coefficients and sending $\tau$ to $\Sigma-\tau$, invariance of $\alpha+\beta\tau$ requires $s\beta=-\beta$ and $s\alpha-\alpha=\Sigma\beta$, exactly the two conditions suggested by these scratch calculations. An alternating coefficient $\beta$ therefore does not automatically produce an invariant element: the second equation is a further lifting problem, particularly when one cannot divide by two. The LM scan147 comparison is methodological rather than an identification of objects: both passages warn that an action agreeing on the alternating subgroup may differ by a sign on the full symmetric group.

### H30 — The written coefficient ring omits a displayed argument

**File/scan:** 83/197, the ring immediately after “donc ds”. **Kind:** reading question. **Manuscript anchor:** “$\operatorname{Tr}x_3x_4$” above the coefficient list; its absence from the next displayed ring. **Context:** Hua XII, “Quatre variables, et le cube”, grouping $x_3x_4$ into one variable; the nine-variable presentation on current190. **Register:** no matching settled entry.

The displayed list of inputs for $\Sigma_{1,2,(3,4)}$ and $\Pi_{1,2,(3,4)}$ includes $\operatorname{Tr}(x_3x_4)$, but the next coefficient-ring line omits that generator. Hua's compressed integrality argument uses the full set of invariants and does not preserve this omission as a separate issue. A proof of the degree bound must first specify the corrected coefficient ring in the research analysis, while the frozen ring on the page remains unchanged.

### H31 — The half-sum obstruction has an exact integral criterion

**File/scan:** 83/215. **Kind:** own idea. **Manuscript anchor:** “$\delta'+\delta''=a'-a$”; the three boxed half-sums. **Context:** Hua XIII, “Les relations linéaires”; `LM_140-4_text.tex`, scans74–75, recovery of $\nu_0$ from $2\nu_0$ only when 2 is a regular section. **Register:** no matching settled entry. **Confidence:** high; exact solution of the three displayed equations.

Put $\varepsilon_1=a'-a$, $\varepsilon_2=b'-b$, $\varepsilon_3=c'-c$: over a ring $k$, the three equations have a solution if and only if $\varepsilon_1+\varepsilon_2+\varepsilon_3\in2k$. If $2s=\varepsilon_1+\varepsilon_2+\varepsilon_3$, all solutions are $\delta=s-\varepsilon_1$, $\delta'=s-\varepsilon_2$, $\delta''=s-\varepsilon_3$, with the choice of $s$ a torsor under $k[2]$. Thus over $\mathbb Z$ there is one parity condition and a unique solution, whereas over a general base divisibility governs existence and absence of 2-torsion governs uniqueness, matching the distinction made explicitly in the earlier LM passage.

### H32 — The common delta value, rather than one solved equation, is the likely sign problem

**File/scans:** 83/213–215. **Kind:** reading question. **Manuscript anchor:** “$b-\gamma=\alpha-a'=\alpha'-b'=a-\beta'=\delta''$”. **Context:** Hua XIII, “Les relations linéaires”, its normalized delta system; current215's solved relations. **Register:** no matching settled entry.

The solved formulas across213–215 give $\gamma=b+\delta''$, $\alpha=a'-\delta''$, $\alpha'=b'-\delta''$, and $\beta'=a+\delta''$, so all four members of the displayed chain equal $-\delta''$. Therefore changing only $\gamma=b+\delta''$ to a minus would break agreement with the later system; a change in the chain's common-value sign explains all four discrepancies together. This identifies the scope of the mathematical inconsistency without choosing a different ink reading.

### H33 — The three final direction parameters are sums, not the earlier individual edge invariants

**File/scans:** 83/201,221. **Kind:** reading question / unpursued implication. **Manuscript anchor:** “$\lambda=a+a'$”, “$\mu=b+b'$”, “$\nu=c+c'$”; “correspondent aux trois directions d'arêtes”. **Context:** Hua XII final footnote on the abandoned three-value claim and XIII final paragraph. **Register:** no matching settled entry.

Scan221's three parameters are sums of paired edge coordinates, so their existence does not reinstate scan201's stronger claim that each $\Sigma_a$ depends only on direction. Even after these three sums are known, differences of opposite-edge coordinates remain as separate data, with the parity restrictions of scan215. The identity $\varphi_a+\varphi_{a'}=2(\mu+\nu)$ should therefore be read as a relation on a quotient of the six-parameter system, not a reduction of that whole system to three free variables.

### H34 — Compare the integral coordinate systems before comparing determinants

**File/scans:** 83/209,211,215,219. **Kind:** own idea / reading question. **Manuscript anchor:** “$a,b,c,d,\alpha,u$”; “$a,b,c,d,a';u$”; “$d-b=u-v$”. **Context:** Hua XIII, “Les relations linéaires”, which groups the parametrizations but does not write their integral change of basis. **Register:** no matching settled entry. **Confidence:** medium; explicit edge/face identification remains to be checked.

The six-parameter construction on209 uses no halves, while the chosen six-edge coordinates on215 have a parity condition, suggesting that an explicit integral change-of-coordinates matrix could explain the relation between the two lattice descriptions. The determinant ratio $1024/512=2$ is compatible with an index-two change but does not prove one, especially because211's $S_2$ uses $u+(d-b)$ where209 writes $v=u-(d-b)$. This is a useful calculation to carry out after matching every face and edge label; a determinant ratio alone must not be promoted to a geometric identification.

### H35 — The missing term is invisible in some bad-characteristic tests

**File/scans:** 83/185,189,205. **Kind:** own idea / scope correction to a context statement. **Manuscript anchor:** “$\tau\tau'=\Pi$”; the integrality target over $\mathbb Z$ on185. **Context:** Hua XII, “Trois variables”, footnote saying the formula is false when $cc'c''\ne0$; Hua I's earlier $\mathbb F_4$ model. **Register:** no matching settled entry. **Confidence:** high; the difference is the explicit polynomial term.

The exact discrepancy is $4cc'c''$, so failure occurs when that product is nonzero, not merely when $cc'c''$ is nonzero over an arbitrary ring. In particular the omitted term vanishes in characteristics two and four and on every specialization with one singular matrix, meaning those tests cannot detect the integral error. This qualifies Hua's wording and explains why a universal check over $\mathbb Z$ or a characteristic-zero specialization is needed, without asserting any historical explanation for the omission.
