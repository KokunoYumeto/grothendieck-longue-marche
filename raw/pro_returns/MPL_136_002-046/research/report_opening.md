# MPL_136_002–046 — research notes

## Evidence, scope, and status

These notes concern **cote 136, archive scans 002–046, with blank scan 019 omitted: 44 supplied pages**. The diplomatic transcription was read and audited by one reader in sequence without OCR, reconciled for recurring notation, and frozen at **2026-11-17 15:04:33 UTC**; the context was opened at **15:04:34 UTC**, after SHA-256 verification of all 44 page files and their exact combined concatenation. Research analysis could then be divided among assistants, but no scan reading, transcription, or visual audit was delegated. The transcription has not been edited in response to the context or the mathematical observations below.

Manuscript citations use **archive scan numbers**, not a presumed author's pagination. A locator explicitly called a “TeX line” refers to the corresponding individual file in `pages/`; other locations are approximate positions on the manuscript. Brief quotations are from the frozen transcription, including retained anomalies and doubts. A transcription doubt is not automatically an authorial question: those are distinguished in the dedicated self-flagged-steps section.

The context consists of `README.md`, `notes/RESULTS_STATE.md`, the four files in `same_cote_136/`, and Michel Hua's project's `hua_project/136.modern.tex` with its README. The earlier package notes are **first-pass leads, not independently established results**. A status in `RESULTS_STATE.md` is the research run's claim unless a review is explicitly reported there; this report does not silently promote those statuses. **Hua, modernised reading of cote 136** is credited as his project's AI-produced interpretation, and his numbered page *n* corresponds to archive scan *n+1*; his findings-register entries are also claims to check, not proofs supplied by their labels.

The findings below distinguish the literal manuscript statement, a contextual continuation, and an editorial inference. No independent external literature survey was undertaken for this return: external authors or works mentioned by the supplied notes remain attributed comparison leads unless the reasoning is given here. In particular, an unavailable earlier report or bibliography entry has not been reconstructed from its title.

## Answers to the questions posed with the packet

| Question | Finding from these pages | Evidence and limit |
|---|---|---|
| Is this his own “Historique”? | **Yes.** | Scan 003 has “1 Historique” under “Complexe DR à p.d. et ombres des modules,” with “Plan conf. IHES en 1976” in the margin; the historical sequence continues into 004. The separate claim that Carmona printed two pages is not verified by these supplied sources. |
| Is the construction functorial on semi-simplicial sets? | **Yes, as a stated and explicitly constructed structured functor.** | Scans 006–009 form the simplex over a PD triple $(S,J,t)$ and its contravariant Hom construction, then specialize to $S=k\{T\}$; 009 explicitly says contravariant in $\mathcal X_*$ and covariant in $k$. The historical “$\frac12$ simplicial” terminology must not be replaced without checking the intended indexing category. |
| Does it compute integral cohomology with products? | **The supported statement is weighted reconstruction through shadows.** | Scan 007 expressly warns that the general $(S,J,t)$ construction does not simply have $H^*(X,S)$; 009–011 assert the weightwise truncated comparison and recovery of the cohomology algebra from its shadows. That is stronger than a merely rational construction but different from an ordinary unweighted integral PD cochain algebra with the usual cohomology. |
| What do divided powers contribute? | **They are part of the cochain structure and of the coefficient algebra $k\{T\}$.** | The differential compatibility is written on 007 and 013, and the multiplication in weight uses binomial coefficients. Descent of PD operations to ordinary integral cohomology and reconstruction of the full integral homotopy type are not proved by these pages; they belong under **follow-ups @305**. |
| What is the “topos de De Rham”? | **No separately named new topos is defined in this extract.** | Scan 016 starts with a commutative ring object in an already given topos and asks for structured derived direct images. The later “condition de De Rham” in `MPL_136_047-094_notes.md`, R039, scan 091, supplies a test-object existence condition; it does not identify a new topos here. |
| What is “faisceautisation”? | **Internalizing the PD construction and seeking functorial derived direct images that retain its structures.** | Scan 016 proposes quasi-isomorphic flasque replacements, asks whether they always exist, and names a cosimplicial-topos problem posed by Deligne. The later context, especially `MPL_136_047-094_notes.md`, R027–R041, scans 080–091, adds universal acyclicity, comparison and direct-image arguments. |
| Are abelian varieties or Fourier-transform Chern classes lecture examples? | **No such handwritten example was located in these 44 pages.** | Abeloid and Hodge material occurs on reused typed faces 036/038/046; “Chern” and “Fourier” do not occur in the frozen text. This narrows **WG2 §2.4 #5** / **MPL_133 B10** for the supplied range and makes no claim about all of cote 136. |

### The mathematical distinction behind the answer

For the universal coefficient ring $S=k\{T\}$, the displayed construction has complementary degree $p$, exterior degree $q$, differential of bidegree $(-1,+1)$, and total weight $w=p+q$. The intended comparison expressed by scans 009–010 is

$$
H^{w,q}_{\mathrm{reindexed}}(X,k)
\simeq
\begin{cases}
H^q(X,k)\,T^{(w)},&w\geq q,\\
0,&w<q,
\end{cases}
\qquad
H^{\bullet,q}_{\mathrm{reindexed}}
\simeq \tau_{\geq q}\bigl(H^q(X,k)\otimes_k S\bigr).
$$

This is an **interpretation of the intended comparison in the notes**, not a replacement of the frozen formulas: scan 009 retains an anomalous `$p=0$` in one acyclicity sentence, and the first two occurrences on scan 010 read `$H^0$` before the later `$H^q$` formula. The local reading questions below record those differences. The multiplication retains the weight coefficient

$$T^{(a)}T^{(b)}=\binom{a+b}{a}T^{(a+b)},$$

and scan 011 asserts that the original cup pairing can be recovered from sufficiently high shadows. The arithmetic of scans 020–025 supplies a direct finite-tail reconstruction argument; it does not alone prove derived multiplicative reconstruction or that PD operations descend to the ordinary cohomology ring. The supplied **follow-ups @305** and **gap g1048** already distinguish those stronger tasks, so they are cited rather than re-presented as newly discovered questions.

### What the later context makes concrete about faisceautisation

The opening question on 016 becomes more explicit in the supplied account of scans 080–091: choose an embedding $u:k\hookrightarrow\Phi$ in a given topos, put $\Psi=\operatorname{Coker}u$, and form the sheaf algebra

$$K_u^{p,q}=\Gamma_k^p(\Phi)\otimes_k\Lambda_k^q(\Psi),$$

with differential induced by $\Phi\to\Psi$. The reported assumptions include a flat cokernel and positive divided/exterior powers of $\Phi$ whose flasqueness survives the specified tensor operations; the intended result is a resolution of $k\{T\}$ with the same weightwise truncated cohomology comparison after sections or direct image. These are the concrete hypotheses and claims reported in `same_cote_136/MPL_136_047-094_notes.md`, R027–R031 (080–082), and **Hua, modernised reading of cote 136**, “Le bicomplexe d'une immersion,” within “Faisceaux tests sur un topos ; la condition de De Rham” (his 79–90 = scans 080–091); they have not been independently verified against those later images in this return.

The “condition de De Rham” is then the existence of such data for a ring object, and comparison through common enlargements is intended to make the resulting object independent of the chosen embedding in a suitable derived category. The later notes distinguish this intended independence from strict equality of maps or all higher coherences, and leave the direct-image acyclicity and universal quasi-isomorphism requirements as proof obligations (`MPL_136_047-094_notes.md`, R031–R041, scans 081–091). Thus “faisceautisation” has concrete algebraic and functorial content here: constructing and comparing structured resolutions internally and seeking their derived direct images; it is not evidence for identifying an otherwise unspecified new topos with a modern construction. This develops **WG2 §2.4 #5**, **follow-ups @305**, and the related **gap g1004** without declaring the existence or uniqueness problems solved.

### The lecture plan and the continuation in this packet

The actual heading is a lecture plan, not a polished table of contents. Its opening historical list is: differential forms and Stokes; De Rham and E. Cartan; Hodge; Cartan–Serre and Stein spaces; arithmetic/crystalline predecessors including Dwork, Washnitzer–Monsky, Berthelot and Illusie; algebraic de Rham comparison; and Sullivan's singular differential forms (003–004). The table below describes the order visible in the bundle, without asserting that every later arithmetic sheet was delivered in the lecture.

| Archive scans | Role in the visible sequence |
|---|---|
| 002–004 | Cover, dated plan annotation, “Historique,” and the rational Sullivan benchmark, with a torsion-loss objection. |
| 004–007 | Singular/simplex realization, the denominator problem, failure of the naive integral affine PD quotient, and the repair using $(S,J,t)$. |
| 008–009 | Universal choice $k\{T\}$, the two gradings, simplicial algebra, and the weightwise cohomology claim. |
| 010–011 | Reindexing by total weight, shadows, and reconstruction of ordinary cohomology and cup products. |
| 012–018 | “Remarques et Pbs”: rational specialization; integral homotopy-type question; cohomology operations; minimal models and Künneth; dual chains; faisceautisation; and stronger linear structures. The letters around the last two topics are revised or doubtful. |
| 020–025 | Binomial arithmetic, a finite-index lemma, tail rigidity, the shadow functor and compatible-family adjoint. |
| 026–035 | Virtual shadows and negligible objects; a stronger nonnegative extension/unit theorem; arithmetic proofs, revisions, and factorial valuations. |
| 037, 039, 041, 043, 045 | Homogeneous maps between tails, the negative-degree case, p-typical coefficients and divisibility; 037 also carries a cancelled rotated Cayley-graph fragment. |
| 036, 038, 040, 042, 044, 046 | Interleaved reused typed faces, with their own subject matter and page numbers. |

## Itemized research register

Each item below has a local identifier, an evidence locator, a kind, and a short assessment with context and register links. “Own idea” means an editorial deduction or proposed test in this return, with confidence and reason; it is not a claim of historical priority or novelty. Statements already identified as settled in the supplied project state are used as context, with their supplied status, and the added contribution is the earlier manuscript evidence or the difference in formulation.
