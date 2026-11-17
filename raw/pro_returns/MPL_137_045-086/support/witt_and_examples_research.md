# Research support: Witt, Burnside, binomial operations, and named examples

Prepared after the root reader froze the transcription at **2026-11-17 21:38:33 UTC**. This research task used the frozen LaTeX text, supplied contextual texts, and primary literature; it did not inspect manuscript images, perform OCR, or modify any transcription file. The full `context/README.md` and all 505 lines of `context/notes/RESULTS_STATE.md` were read before these notes were written.

## Evidence and status

The supplied archive does **not** contain the cote 133 scans, its complete transcription, or `MPL_133_notes.md`. The latter is named in `RESULTS_STATE.md`, but that path identifies an unavailable earlier source and does not authorize retrieving it elsewhere. Consequently the present work can reconcile the supplied summaries, and can test a mathematical interpretation against the literature, but cannot independently establish what cote 133 says.

| Supplied item | Actual available content and status | Relevance here |
|---|---|---|
| `MPL_133 B01` | `RESULTS_STATE.md`, line 289: title “The binomial adjective belongs to the rank target”; first-pass lead, no supporting passage supplied | A warning against transferring binomial structure from a numerical target to the entire source ring |
| `MPL_133 B05` | `RESULTS_STATE.md`, line 290: title “The strongest supplied bridge is a correction and a new question in 1983”; first-pass lead | The full supplied *Pursuing Stacks* §119 permits a direct contextual comparison without pretending to read the missing 133 notes |
| `MPL_133 B06` | `RESULTS_STATE.md`, line 291: title distinguishing strict cosimplicial and strict DGA commutativity; first-pass lead | Scan 137/072 expressly places the induced cochain product laws at homotopy level |
| `MPL_133 §2` | `RESULTS_STATE.md`, line 447: truncated excerpt saying “Explicitly quadratic Witt theory” on 133 scans 006–009 | This is a reported earlier reading, not a newly verified identification |
| `MPL_133 §88` | `RESULTS_STATE.md`, line 454: truncated reconciliation mentioning quadratic-Witt and finite-set-operation material | Supports investigating two subjects rather than collapsing them into a single Witt-vector claim |
| `WG2 §Week #3` | Unchecked planning item, `RESULTS_STATE.md`, line 465 | Its proposed R-SCHEM synthesis remains a research program |
| `WG2 §2.4 #5` | Unchecked planning question, `RESULTS_STATE.md`, line 463 | The named geometric examples sought by the question are absent from the present frozen excerpt |
| *Pursuing Stacks* VI §119 | Supplied primary typed text, original pp. 500–503, `ps6.tex`, approximately lines 2880–3038 | Direct evidence for a withdrawn schematic comparison and a proposed binomial replacement |
| *Pursuing Stacks* VI §120 | Supplied primary typed text, original pp. 506–507, `ps6.tex`, approximately lines 3132–3199 | Separately lists divided-power, lambda, and binomial structures and proposes an analyzer framework |

Line numbers above refer to the supplied text files, not manuscript line numbers. None of the cote 133 leads above is marked as refereed in the supplied status register.

## Candidate research items for the main notes

### W01 — The cote 133 guess needs two qualifications

**Locator:** cote 137/045–086, whole supplied excerpt; contextual locator cote 133/006–009 only through the register. **Kind:** reading question / scope of a contextual claim. **Bears on:** `MPL_133 §2`, `MPL_133 §88`, `MPL_133 B01`, `WG2 §Week #3`.

No occurrence of “Witt,” “Burnside,” or “binomial” was found in the frozen 137/045–086 text, while the supplied register reports quadratic Witt theory on 133/006–009 and separately mentions finite-set operations. This **differs from and qualifies** the initial planning guess that “Witt” simply names the finite-G-set/Witt-vector construction; it does not refute the possibility of such a connection elsewhere in 133. The strongest justified answer is that the earlier return reports both quadratic-Witt and finite-set material, and the identification with Witt vectors still requires the unavailable 133 passages to be checked.

### W02 — The literature makes the finite-set/Witt bridge precise, but does not attribute it to this manuscript

**Locator:** cote 137/075–086, polynomial-category discussion as a possible comparison; no Witt construction is transcribed there. **Kind:** unpursued implication / literature comparison. **Bears on:** `WG2 §Week #3`, `MPL_133 §2`.

The mathematical comparison is consolidated in **R10** of `MPL_137_045-086_notes.md`, with the completion and group hypotheses and the distinction from Witt groups of forms. Checked source locators are **DS89**, §1 (author PDF pp. 2–3) and theorem (5–4–2), p. 33; **M14**, introduction, pp. 1291–1292; and **BAL05**, Definition 1.1.27 (the symmetric-space formulation). These are external comparisons: they neither establish a Witt construction on 137/045–086 nor identify the relationship between the subjects reported in the unavailable cote 133 passages. Full source URLs and access limits remain in the bibliography below.

### W03 — A minimal obstruction to calling a Burnside ring binomial

**Locator:** cote 137/076–077, scalar-degree discussion; contextual `MPL_133 B01`. **Kind:** own idea / elementary comparison test. **Confidence:** high, because the calculation uses the two orbit classes of a two-element group. **Relation:** adds a concrete test; does not claim novelty or identify the unseen rank map in 133.

Let $G=C_2$ and let $t=[G/\{1\}]$ in its Burnside ring: the orbit decomposition gives $A(G)=\mathbb Z[t]/(t^2-2t)$, with integral basis $1,t$ (Lück, Definition 1.1 and Example 1.4). Then $\binom t2=(t^2-t)/2=t/2\notin A(G)$, so the usual torsion-free binomial-ring condition fails, even though cardinality sends $t$ to $2$ in the binomial ring $\mathbb Z$. Thus a binomial numerical/rank target and operations on finite $G$-sets do not by themselves make the Burnside ring binomial; this sharpens the caution signaled by the **title** of *MPL_133 B01*. [L05]

### W04 — Divided powers do not automatically produce a binomial ring

**Locator:** cote 137/085, example paragraph, and 086, first line. **Kind:** own idea / elementary comparison test. **Confidence:** high, because grading detects the displayed obstruction. **Bears on:** `MPL_133 B01`, `MPL_133 B05`, `WG2 §Week #3`.

The example “La catégorie des $k$-modules est une $\otimes$-pd-catégorie” concerns divided-power operations, not an assertion that its underlying coefficient rings are binomial. For the usual free divided-power algebra $\Gamma_{\mathbb Z}(\mathbb Zx)$, one has $x^2=2\gamma_2(x)$, while $(x^2-x)/2=\gamma_2(x)-x/2$ fails to lie in the integral algebra because its degree-one coefficient is not integral. This **adds a test of the proposed bridge**: a comparison construction would be needed to reach binomial cochains; replacing one name by the other cannot suffice. The distinction agrees with the separate PD-on-an-ideal, lambda, and binomial structures enumerated in supplied *Pursuing Stacks* §120, pp. 506–507.

### W05 — The 1983 correction is directly present in the supplied primary context

**Locator:** cote 137/073–074, De Rham discussion; contextual *Pursuing Stacks* VI §119, pp. 500–503. **Kind:** unpursued implication / contextual comparison. **Bears on:** `MPL_133 B05`, `WG2 §Week #3`.

The later context says Illusie rejected Grothendieck's proposed divided-power-derived-functor description of Eilenberg–MacLane homology, and Grothendieck supplies a degree-two obstruction using the extension denoted $W_2$, represented by $1+at+bt^2$. The splitting equation $P(a+a')-P(a)-P(a')=aa'$ has an integer-valued solution $\binom a2$ but no solution polynomial with integer coefficients, motivating the subsequent binomial comparison question. This **supports and makes explicit** the direction of the B05 lead, while showing why the cohomological comparisons on 137/073–074 cannot be promoted without further proof to a general integral reconstruction theorem. It is a correction of a particular later comparison hypothesis, not a retraction of every divided-power construction in the 1975–76 pages.

### W06 — The arithmetic warning in 137 is already an obstacle to purely pointwise recognition

**Locator:** cote 137/076, remark and left margin;077, first two paragraphs. **Kind:** withdrawn in the same text / unpursued implication. **Bears on:** `MPL_133 B01`, `WG2 §Week #3`, Hua finding `137-polynomial-categories-pd-tensor-categories` as an unverified contextual lead.

The frozen reading records the cancelled uniqueness argument and the “canulars ‘arithmétiques’” warning, with the example that $\lambda$ and $\lambda^p$ act identically on a group killed by $p$. Scan 077 then discusses all base algebras and makes the decomposition additional structure. This **adds a precise limitation** to any inference from scalar homogeneity to a binomial or polynomial-law structure: the degrees cannot in general be recovered from integer-point functions alone. The faint prose remains subject to the frozen doubt marks; this research comparison does not amend it.

### W07 — The specified geometric examples are not named in this excerpt

**Locator:** cote 137/072–074 and 085–086; search over all 045–086. **Kind:** unpursued implication / bounded negative finding. **Bears on:** `WG2 §2.4 #5`.

The named examples in the frozen text include a cup-product construction, a divided-power De Rham complex, “De Rham-Sullivan” in characteristic 0, and $k$-modules or $K$-modules on a topos, including graded modules. No explicit abelian variety, Fourier transform, or Chern class is named in 137/045–086, so these pages **do not confirm** the specific example proposed by the planning question. The generic ringed-topos example can of course be specialized to many geometric situations, but the specializations are not manuscript examples here. This bounded absence says nothing about omitted pages of 137 or the unsupplied portions of 136.

### W08 — The cup product supports the B06 distinction

**Locator:** cote 137/072, final two lines of prose. **Kind:** unpursued implication / scope of a claim. **Bears on:** `MPL_133 B06`.

The manuscript says of the induced product's associativity, commutativity and unit that “le tout à homotopie près,” and separately obtains the graded-algebra structure on cohomology. This **supports** the distinction anticipated in the B06 title: strict structure in a cosimplicial or universal-model presentation does not make the displayed cochain product a strict commutative DGA product. No claim about the homotopy information carried by all higher coherences follows just from this paragraph.

### W09 — The existing composition maps and the open PD question point in opposite directions

**Locator:** cote 137/081–083, $\alpha_{p,q}$ displays;085, final paragraph;086, opening. **Kind:** unpursued implication / own comparison. **Confidence:** high for the displayed direction distinction, medium for its eventual categorical formulation. **Bears on:** `137-polynomial-categories-pd-tensor-categories`, `WG2 §Week #3`.

The polynomial-category reconstruction uses maps $\Gamma^{pq}(X)\to\Gamma^p(\Gamma^q(X))$, whereas the later question about a structure “à p.d.” asks for maps in the reverse direction, from $\Gamma^p(\Gamma^q(M))$ to $\Gamma^{pq}(M)$. These are different pieces of structure, so the former coherence package should not silently be treated as already supplying the latter. The module example is said to have the latter canonically on 086, but the abstract case remains a question on 085. This **adds a distinction** useful for testing any proposed comparison with a monad or plethory, rather than claiming such a comparison has been established.

## Primary bibliography and checked locations

- **DS88.** Andreas W. M. Dress and Christian Siebeneicher, “The Burnside ring of profinite groups and the Witt vector construction,” *Advances in Mathematics* **70** (1988),87–132. DOI: [10.1016/0001-8708(88)90052-7](https://doi.org/10.1016/0001-8708(88)90052-7). Publisher abstract and metadata retrieved; the full publisher page returned 403, so no claim of inspecting the original full 1988 proof is made.
- **DS89.** Andreas W. M. Dress and Christian Siebeneicher, “The Burnside ring of the infinite cyclic group and its relations to the necklace algebra, lambda-rings, and the universal ring of Witt vectors,” *Advances in Mathematics* **78** (1989),1–41. DOI: [10.1016/0001-8708(89)90027-3](https://doi.org/10.1016/0001-8708(89)90027-3). [Author-hosted text](https://www.math.uni-bielefeld.de/~sieben/lothar/burnside_ring_of_cyclic_group.pdf), introduction and theorem (5–4–2), also §5–5 for Frobenius/restriction and Verschiebung/induction. The viewed author copy uses later MSC metadata; the journal publication date is separately confirmed by publisher metadata.
- **M14.** Lance Edward Miller, “On the Structure of Witt-Burnside Rings Attached to Pro-p Groups,” *Documenta Mathematica* **19** (2014),1291–1316. [Journal PDF](https://emis.de/ft/9833), introduction, pp. 1291–1292. Used for the precise profinite and pro-p specializations, not as a claim that the present manuscript constructs them.
- **BAL05.** Paul Balmer, “Witt Groups,” in *Handbook of K-Theory* (2005),539–576. [Author PDF](https://www.math.ucla.edu/~balmer/Pubfile/W-handbook.pdf), Definition 1.1.27 and §1.2.1. Used solely for the symmetric-space definition of a Witt group, to distinguish the forms-based subject from Witt vectors; it is not cited as a characteristic-independent identification of symmetric and quadratic Witt groups.
- **L05.** Wolfgang Lück, “The Burnside Ring and Equivariant Stable Cohomotopy for Infinite Groups,” *Pure and Applied Mathematics Quarterly* **1** (2005),479–541. [arXiv:math/0504051v2](https://arxiv.org/abs/math/0504051), Definition 1.1 and Example 1.4, source PDF pp. 4–5. The displayed typesetting date of the retrieved PDF is later than its 2005 arXiv version metadata; the cited definitions and example were checked directly.

These are literature comparisons and elementary tests, not novelty claims. No outside source is used to change the frozen transcription.

## Search record

Before composing each candidate item, the relevant terms were searched across the supplied context with `rg`; targeted passages were then read. Searches included `MPL_133`, `B01`, `B05`, `B06`, `Witt`, `Burnside`, `binom`, `rang`, `rank`, `Fourier`, `Chern`, `variété(s) abélienne(s)`, `abelian variet`, and the degree/composition vocabulary.

The complete frozen transcription has no match for `Witt`, `Burnside`, `binom`, `Fourier`, `Chern`, `variété`, `Jacobian`, or the explicit cote numbers 133/136. Matches for `abélienne` are about **abelian categories**, not abelian varieties. In the entire supplied context, the specific Fourier/Chern/abelian-variety query only matches the planning README; broad `abelian` searches also find many unrelated abelianization, group and category passages, which were not counted as geometric examples.

The local cross-reference searches do not establish absence in an entire cote or in the broader archive. The per-item distinctions above are retained precisely because only summaries of the neighboring returns were supplied.
