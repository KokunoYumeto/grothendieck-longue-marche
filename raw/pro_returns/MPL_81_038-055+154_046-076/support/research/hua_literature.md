# Post-freeze comparison with Michel Hua’s project and primary literature

## Scope, provenance, and conclusion

This report concerns cote 154, scans 046–076. It was prepared after root froze the 31 page transcriptions and their concatenation at 14:06:11 UTC on 17 November 2026 and opened context at 14:06:15 UTC. The research agent read no original scan image and changed no transcription. All source-reading questions below compare the frozen text with another edition; they are not independent paleographic verdicts.

The required context README, the entire 532-line RESULTS_STATE, the Michel Hua project README, and the entire 2,555-line Michel Hua modernization of cote 154 were read before completing the comparison. Michel Hua’s project is credited throughout. Its modernization explicitly distinguishes interpretation from transcription, supplies assumptions, repairs some statements, and reports other uncertainties. The header describes an AI-produced first pass, with only specified human checks. Neither that modernization nor the earlier result-register entries are treated as independently verified mathematics.

**The closest documented historical identification is the pseudoline “surface modulaire” of Esquisse §8.** Scans 046–076 investigate a combinatorial surface of relative positions, its polygonal transports, characters, and competing gluing conventions. The same subject supplies a concrete link to the broader moderate-topology agenda of Esquisse §§5–6. These pages do not by themselves establish its axiomatic foundations. A specific derivation of the 1986 geometry of forms from this construction remains unestablished: the manuscript exhibits a relevant practice of geometric assembly, but the necessary comparison of definitions and axioms is missing.

The useful modern comparison is the extension space of a rank-three oriented matroid. It is a comparison to construct, not an identification already proved here. In particular, a surface carrying the asserted nontrivial dihedral local system cannot simply be identified with an unmodified simply connected extension-space order complex. The exact treatment of exceptional positions and of orientation must be specified first.

## Locator conventions

The frozen source for scan N is:

    deliver/pages/MPL_81_038-055+154_046-076_154_scanNNN.tex

“T” means a line in that frozen page file. “H” means a line in:

    context/hua_project/154.modern.tex

Michel Hua’s numbered manuscript page p corresponds to this package’s scan p + 1. Thus Hua pp. 45–75 correspond to scans 046–076. An H range may synthesize several manuscript pages. The source element kind and position below reproduce or shorten the preceding % E marker. A statement that Hua “repairs” something describes the Michel Hua project’s editorial action; it never authorizes changing the diplomatic transcription.

## Detailed comparison

### H01 — The structural map and an exceptional preimage

**Source:** scan 046, T27–31, display / left lower, definition L, followed by margin text. The displayed formula gives \(L=\varphi^{-1}(\bigcup D_i)\); the margin qualifies the discussion by referring uncertainly to neighborhoods around components of \(K_0\).

**Michel Hua’s project:** “L’application structurale,” H1238–1257, Hua p. 45. It replaces the unrestricted preimage statement by
\[
\varphi^{-1}(X_1)=L\cup K_0,
\]
and cites Hua p. 159, corresponding to scan 160, for the later formula.

**Assessment:** This is an explicitly reasoned mathematical repair, supported by an outside-range comparator, not a competing decipherment of the same formula. The frozen margin already records a qualification. The relationship between the restriction away from exceptional neighborhoods and the global equality should be explained in research notes, without silently installing the global equality into scan 046.

### H02 — Exceptional-edge indices differ by one

**Source:** scan 047, T41, margin attached to lower-left item n, has uncertain equality/inequality followed by \(n-(\nu_s-1)-(\nu_t-1)\) for a stable exceptional side and \(n-\nu\) for an unstable side. Scan 056, T35–38, display / left middle, instead uses \((n-1)-(\nu_s-1)-(\nu_t-1)\). Scan 073, T12, inverted display beneath the two-vertex drawing, repeats the latter expression.

**Michel Hua’s project:** H1271–1280, Hua p. 46, explicitly retains this unresolved one-unit discrepancy, comparing Hua pp. 55, 93, and 110.

**Assessment:** Ask whether “index” and the later length count are the same quantity under the same subdivision convention. The evidence does not warrant a silent off-by-one correction. This matters to the alternating sum used in the half-turn calculation.

### H03 — The date is a post-freeze reading question

**Source:** scan 048, T2–3, text / upper-left date: uncertain “7.2.1984.”

**Michel Hua’s project:** H1414–1417, Hua p. 47: “2.2.84,” reported as checked on the facsimile by Michel Hua; its previous reading was “7.1.1984.”

**Assessment:** The editions disagree. The specific human check reported by Michel Hua’s project is relevant evidence for later review, not permission to replace the independently frozen reading. This research agent has not inspected the image.

### H04 — Distinguish polygon conventions and resolve the parity word

**Source:** scan 048, T16, text / left middle item a, gives two dual subdivisions of order \(2n\); T39, text / right-middle consequence, says the faces have order \(4n\). Scan 051, T17, display / left-middle item a, excludes critical points of **odd** order from \(S'_K\cap L\).

**Michel Hua’s project:** H1393–1405 describes the two colors but excludes critical points of **even** order. H1421–1435 uses a normalized polygon \(\operatorname{Pol}(F)\) of order \(2n\).

**Assessment:** The \(4n\) count may count both alternating colors, whereas the \(2n\) polygon counts one constituent subdivision; that reconciliation is an inference requiring an explicit dictionary. “Pair” versus “impair” is a direct unresolved reading discrepancy with mathematical consequences.

A related local issue occurs on scan 050, T11, text / left upper-middle item c: the frozen bound is \(\nu(s)\geq\unsure{2|1}\). Michel Hua’s project gives \(\nu(s)\geq1\), H1437–1442, and says its overwritten numeral might be 0. Preserve the alternatives as alternatives.

### H05 — Local sign propagation is stronger than the established global argument

**Source:** scan 054, T18, text / left lower item a, has uncertain pairs \((3,2),(3,3),(3,5)\) with an alternative \((3,4)\), alongside the assertion that the counts lie between 3 and 5. Scan 055, T9–15, second corollary / left bottom and continuation right, propagates signs using connectivity, but explicitly leaves exceptional faces to be checked. Scan 050, T3, upper-left question, asks for the relation between the symmetry bijections and the signs.

**Michel Hua’s project:** H1516–1526 normalizes the three pairs to \((3,3),(3,4),(3,5)\), explaining that the latter digits were inferred from the range “3 to 5.” H1534–1548 identifies connectivity as an unproved input and preserves the exceptional-face qualification. H1430–1433 describes the relation between symmetries and signs as not fully resolved.

**Assessment:** The pair list is a contextual reconstruction, not additional manuscript certainty. The local propagation rule and the global connectivity/completeness argument should be recorded separately. Later extension-space connectedness can motivate a proof strategy, but only after comparing the actual graph, excluded exceptional positions, and conventions.

### H06 — The half-turn formula agrees; the global construction remains conditional

**Source:** scan 056 contains the reflection formula at T135, display / right middle; the alternating composition at T66–68, left bottom; the multiplicity sum at T44, display / left middle-lower; and the resulting translation at T59, display / left lower. Scan 058, T8, upper-left boxed display, repeats
\[
\lambda(t)=t-(n-1)\quad\text{in }\mathbb Z/(2n).
\]

**Michel Hua’s project:** H1590–1622 and H1624–1642, Hua pp. 55–57, give the same formulas. It renames the length of a chain \(k\) to avoid conflict with the number \(n\) of pseudolines. Its footnote H1617–1622 explicitly says that the identification of the chain as \(2n\) alternating faces has not been independently redone.

**Assessment:** There is strong textual agreement on the displayed local calculation. The passage does not by itself verify all cell relations needed to make transports a representation of the fundamental group of a specified completed surface. This distinction is essential for the Michel Hua project finding **154-dihedral-monodromy-half-turn**, whose register status remains “conjecture (unsearched).”

### H07 — A reported rotation-group repair is already compatible with the frozen reading

**Source:** scan 058, T18, text / left-middle image and index, already gives the inserted uncertain reading \(\mathbb D^+_{2n}\simeq\mathbb Z/(2n)\) when \(n\) is even, and a contained \(\mathbb Z/n\) when \(n\) is odd.

**Michel Hua’s project:** H1637–1642 says that its underlying reading had \(\mathbb Z/n\) in the even case and corrects that to \(\mathbb Z/(2n)\).

**Assessment:** Do not report this as an error in the present frozen transcription. Our reading already agrees with the mathematical correction, while retaining paleographic uncertainty.

### H08 — Surjectivity requires both the parity qualification and an identified surface

**Source:** scan 059, T4, upper-left first paragraph, explicitly mentions even \(n\), but the covering-space notation is uncertain; T28, bottom-left qualification, revises the relevant exceptional-face order to \(2(n-1)\). Scan 060, T23, right-lower new assertion, announces surjectivity. Scan 061, T6, left upper-middle, intends a reflection relative to \(s\), but the image of \(s\) is transcribed uncertainly as \(s|s'\); vertex-fixing is therefore not a secure reading of that sentence.

**Michel Hua’s project:** H1653–1693 distinguishes the even and odd cases. For odd \(n\), it supplies the additional requirement of a side-axis reflection, referring to Hua pp. 63 and 85. It also interprets the long diagonal strokes across Hua pp. 57–60 as not necessarily annulling the text.

**Assessment:** The algebraic parity qualification is sound under the stated polygon model; it does not identify the uncertain covers or prove the topological realization of every loop. The cancellation interpretation differs from the frozen markup on scans 058–061. Treat that as an editorial disagreement, not a source correction.

### H09 — Three polygon characters, surface orientation, and weighted parity

**Source:** scan 063, T14 and T21–28, displays / left upper-middle and left middle, relates orientation and the two color characters:
\[
\chi_X=\chi_s\chi_a.
\]
T32, diagonal margin note, requires counting an exceptional crossing **twice**. T43, boxed right-middle display, has uncertain subscript \(o|X\); T53, right lower-middle, explicitly gives
\[
\chi_{\mathcal X}=\chi_X\chi_c.
\]
Scan 064, T22–27, upper-right argument, introduces the triviality of \(\chi_c\) with “Il semble que”; T31 displays \(\chi_{\mathcal X}=\chi_X\).

**Michel Hua’s project:** H1695–1758 renames the polygon-orientation character \(\chi_*\), preserving its distinction from \(\chi_{\mathcal X}\). H1728–1733 repairs its reading of the boxed subscript using the neighboring equations. H1755–1758 preserves the tentative wording and notes an outside-range cancelled parity calculation.

**Assessment:** Hua’s \(\chi_*\) is a normalized name for the current transcription’s \(\chi_X\), not an extra invariant. The final formula on scan 063 already agrees with the repaired relation. Weighted path length is essential: replacing it with an unqualified number of graph edges would ignore the marginal correction.

Scan 064, T8, gives translation by \(+(n-1)\), whereas scan 056 gives \(-(n-1)\). Reversing a loop or coordinate orientation inverts a rotation. This is a convention question to resolve before declaring an inconsistency.

### H10 — Eight choices reduce to four, but one arc label disagrees

**Source:** scan 065, T40–44, text below drawings, counts two choices in each factor of \(\{a,a'\}\times\{b,b'\}\), then two identifications, and identifies simultaneous antipodal choices. Scan 066, T6, left upper-middle, tentatively requires \(\alpha=a'\) for the original canonical embeddings, then permits \(\alpha=a\) after replacing the disks by smaller ones.

**Michel Hua’s project:** H1763–1776 agrees on eight choices reducing to four. H1778–1787 instead initially says to identify \(b\) with \(a\), before discussing \(b\leftrightarrow a'\).

**Assessment:** The initial \(a/a'\) is a direct comparison question. It should not be settled by importing the modernized sentence: the ensuing four-case table is much more closely aligned between the editions.

### H11 — The four gluing cases agree, with explicit limitations

| Frozen source | Construction and orientation behavior | Michel Hua’s project |
|---|---|---|
| Scan 069, T8–14, upper-middle and middle text | \(A_1\): opposite orientation transition; \(b\) glued to \(a'\); natural map is an immersion | H1811–1816 |
| Scan 069, T16–18, bottom left continuing right | \(A_2\): opposite orientation transition; \(b\) glued to \(a\); immersion on faces, fold along their common boundary | H1816–1819 |
| Scan 070, T4–6, upper-left and middle text | \(B_1\): orientation transition equals parallel transport; no natural map; facing arc \(a'\) | H1820–1823 |
| Scan 070, T8, bottom left continuing right | \(B_2\): arc \(a\); the desired turning circuits fail | H1822–1823 |

Scans 067, T8, and 068, T11 and T17–19, explicitly correct both the orientation transition and the arc assigned to generization; compare H1789–1805. Scan 071, T6, says “sauf erreur” before accepting the supercritical circuits for \(A_1,A_2,B_1\), with an uncertain subscript in the last item. T8 immediately leaves the general \(A_1\) circuits unresolved. Michel Hua’s project retains these qualifications at H1825–1832.

**Assessment:** The value here is a controlled separation of two choices: the arc used to encode the operation and the orientation of the gluing. The source does not canonically select a fully verified global construction merely by counting four cases.

### H12 — Stable positions end with open circuit and covering questions

**Source:** scan 072, T4 and T21, upper-left and lower continuation, restarts the surface construction using stable positions only. T21 initially counts eight choices, retains the two diagonal arc pairs \((a,b)\) and \((a',b')\) with two orientations for each, and then discusses an antipodal quotient in uncertain wording. It does not securely establish two final geometric objects. Scan 074, T31–44, contrasts a natural immersion with the behavior of supercritical circuits. Scan 075, T4, upper-left, says general circuits remain mysterious; T6–17 introduces \(n\)-gons on \(D\), compared with \(2n\)-gons on its double cover. Scan 076, T4, asks about a branched double cover; T12–20 begins a combinatorial description that continues beyond this packet.

**Michel Hua’s project:** H1834–1885, Hua pp. 71–76, synthesizes these constructions, including continuation outside our scan range.

**Assessment:** The question about a branched covering is not a proved theorem. The involution calculations on scan 073, T54–62, are useful local combinatorial relations; they are not a complete presentation of all deformation moves. General circuits, compatibility around all cells, and the exact surface variant remain the natural follow-up.

## Conditional algebraic check of the half-turn

Use the Michel Hua project convention: \(D_{2n}\) is the automorphism group of a \(2n\)-gon, hence has order \(4n\). Put \(r(t)=t+1\), \(R_a(t)=a-t\), and \(\lambda=r^{-(n-1)}\).

\[
\operatorname{ord}(\lambda)=\frac{2n}{\gcd(2n,n-1)}
=\begin{cases}2n,&n\text{ even},\\ n,&n\text{ odd}.\end{cases}
\qquad
\operatorname{ord}(\lambda^2)=n.
\]

The first equality is elementary cyclic-group arithmetic. A reflection \(R_a\) has a vertex axis when \(a\) is even and a side axis when \(a\) is odd. For even \(n\), \(\lambda\) and any reflection generate the full dihedral group. For odd \(n\), \(\lambda\) and a vertex reflection generate only the index-two subgroup of even rotations and vertex reflections; a side reflection supplies the missing parity. These statements verify the conditional algebra behind H06–H08. They do not establish the geometric loops, invariance under path relations, or a globally defined local system.

There is also a useful obstruction to an overquick comparison. If a space is homotopy equivalent to \(S^2\), every representation of its fundamental group is trivial. Consequently, a verified nontrivial dihedral representation on Grothendieck’s surface would prevent that same surface from being the unmodified rank-three extension-space order complex. If the intended comparison is a free orientation quotient of a simply connected space, its fundamental group is \(C_2\), which likewise cannot surject onto \(D_{2n}\) for \(n\geq2\). This is a conditional logical check, not a disproof of either construction. Removed exceptional positions, cuts, added cells, orientation quotients, and different gluing choices may change the space. Each must be tracked before applying an extension-space theorem.

## Exact links to the internal results register

The statuses in this table are reported statuses of the supplied register, not new verification.

| Register item and location in RESULTS_STATE | Status in the register | What this packet contributes |
|---|---|---|
| Michel Hua’s project, **154-dihedral-monodromy-half-turn**, lines 18 and 506 | Conjecture, unsearched; reach beyond; intake new to us | H06–H09 anchor its formula and character calculations in scans 056–064. Retain the distinctions between algebra, chain identification, relations, and global surface construction. |
| **follow-ups @944**, line 289, from **MPL_154_127-176 P05** | Follow-up problem | H10–H12 supply earlier gluing ambiguities and unresolved general circuits. A solution must specify which surface is constructed before proving a manifold condition, Euler formula, or complete sweep relations. The register’s later counting data are not established anew by this packet. |
| **WG2 B15 (§1.2)**, line 499 | Unchecked question or plan item | A finite specialization-poset model might connect to its shape comparison. The present pages do not prove the required localization equivalence or its real-line analogue. |
| **STRATA A.4**, line 426; **BISITE G.10**, line 412 | Proved according to their returns | Their minimum/least-vertex realizations provide possible comparison machinery once an explicit poset and geometric realization are identified. They do not automatically identify this glued surface or its local system. |
| **EXIT_ONE_TYPE P1a1**, line 434; **P1d1**, line 414 | Proved according to their returns | The concern with transition data and coherent gluing is conceptually relevant, but scans 046–076 do not construct normal-link homotopy fibres or an exit-category reconstruction. Do not claim a direct theorem application. |
| **EXIT_ONE_TYPE P4e**, line 438 | Proved according to its return | Its warning that a coarse combinatorial model may lose link data is a useful methodological comparator. It does not prove failure of any specific construction here. |
| **MPL_154_077-126 C03**, line 485; **MPL_154_127-176 P03**, line 492 | First-pass research leads | Their bounded judgment about the 1986 framework is consistent with the conclusion below. Neighbor reports and original evidence should be cited separately; no independence or consensus count is claimed. |

No novelty conclusion follows from finding the half-turn formula in these pages. “Unsearched” in the Michel Hua project register is an explicit research status, not evidence that the result was unknown.

## Primary literature and historical interpretation

### Esquisse: direct subject match and broader moderate-topology setting

The published French Esquisse §8, p. 41, describes a combinatorial “surface modulaire” classifying stable and unstable positions of an added pseudoline, equivalently affinizations. Section 5, pp. 24–27, explicitly includes pseudoline arrangements among motivating stratified moduli and discusses reconstruction by gluing boundary data. Section 6, pp. 33–34, places dévissage and contractible spaces of choices in a broader framework. These passages are directly verified in the French text (Grothendieck, 1997).

The interpretation is therefore more specific than a generic resemblance between two kinds of topology: the §8 subject is the subject of this dossier. The local gluing calculations can be studied within the motivating environment of §§5–6. However, the supplied pages do not formulate a general moderate category, prove the necessary choice spaces contractible, or establish the axioms of a tame theory. Their assembly choices and unresolved circuits show exactly where such a comparison would require additional work.

### Oriented matroids: a precise theorem with a restricted conclusion

Sturmfels and Ziegler define an extension space using the order complex of the poset of nontrivial one-element extensions, ordered by specialization. Their Theorem 1.2 gives homotopy type \(S^{r-1}\) for strongly Euclidean rank-\(r\) oriented matroids; Corollary 4.5 makes every rank-at-most-three oriented matroid strongly Euclidean. Thus rank three gives a homotopy 2-sphere. They distinguish all extensions from realizable extensions and from extensions of a fixed linear realization (Sturmfels & Ziegler, 1993, Theorem 1.2, Corollary 4.5).

This is a rigorous modern target for a comparison, not a theorem that every construction called a “surface of relative positions” is already a surface or has that homotopy type. The order complex, exceptional parallel positions, and any orientation quotient must match. The theorem alone does not supply Grothendieck’s specific cell links, all sweep relations, the stated genus expression in the later dossier, or the dihedral monodromy. Nor does a 1993 theorem establish historical influence on a 1983–1984 manuscript.

### Geometry of forms: what is and is not verified

In his letter to Ronald Brown dated 17 June 1986, Grothendieck describes another approach as “different from topological spaces, from topoi and from moderate spaces,” and says its basic language is still developing (Grothendieck, 1986, pp. 134–135). This is direct evidence against simply identifying the 1986 programme with moderate topology; it does not exclude earlier sources of inspiration.

A first-hand research presentation by Jean Malgoire describes the 1986 manuscript’s programme as describing a space through the figures it can contain, with stratifications and affine polyhedra as examples and axioms involving compatibility, refinement, disjunction, and shadows (Malgoire, 2002). This is a useful programme-level comparator. It is Malgoire’s introductory account, not a complete independently checked transcription of Grothendieck’s formal definitions.

The present scans supply surfaces, disks, arcs, transitions, and assembly alternatives. They do not yet supply a comparison functor or an axiom-by-axiom correspondence with the 1986 language of figures. Calling them an earlier instance of Grothendieck’s interest in geometric assembly is defensible as a bounded interpretive observation. Calling this packet a demonstrated specific precursor of the 1986 formal theory would exceed the evidence inspected here. An original Yamashita letter and a complete original formal definition were not verified in this research; circulating quotations from them are deliberately not used as foundations.

## Priorities for further work

1. **Keep transcription and mathematical reconstruction distinct.** The frozen reading questions with greatest consequences are scan 051 “pair/impair,” scan 066 \(a/a'\), scan 047’s exceptional-edge index, and the cancellation status of scans 058–061. The scan 048 date is relevant to chronology. These require root’s image-based adjudication in a later version, if authorized; this report makes no changes.
2. **Fix the object before proving invariants.** Specify the relative-position set, equivalence relation, treatment of \(D_i\), choice among \(A_1,A_2,B_1,B_2\), orientation convention, and any cuts or fillings. Record where the stable-only construction changes those choices.
3. **Verify transport around all two-dimensional relations.** The reflection algebra is available. The remaining proof concerns which loops occur and when two move sequences yield the same transport. The exceptional crossing weight in scan 063 must be included.
4. **Build the oriented-matroid comparison explicitly.** Identify specialization relations and the map to an extension poset; check exceptional and oriented positions. Only then transfer connectivity or compare homotopy type. Use the conditional fundamental-group obstruction above as a consistency check.
5. **For the historical forms comparison, obtain a precise original definition.** Compare the later objects and operations with the current gluing data rather than treating shared words such as “forme,” “strate,” or “recollement” as sufficient evidence of identity.

## References and exact verification metadata

Grothendieck, A. (1986, June 17). [Letter to Ronald Brown]. In M. Künzer (Ed., with R. Brown & G. Maltsiniotis), *Correspondance Alexandre Grothendieck–Ronald Brown* (pp. 134–135). [Primary edited correspondence PDF](https://webusers.imj-prg.fr/~georges.maltsiniotis/ps/agrb_web.pdf). The date is the letter date; the publication year of this online edited compilation was not established.

Grothendieck, A. (1997). Esquisse d’un programme. In L. Schneps & P. Lochak (Eds.), *Geometric Galois actions: Vol. 1. Around Grothendieck’s Esquisse d’un Programme* (pp. 7–48; London Mathematical Society Lecture Note Series 242). Cambridge University Press. [https://doi.org/10.1017/CBO9780511758874.003](https://doi.org/10.1017/CBO9780511758874.003). (Original work written 1984.) [Editor-hosted French text](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EsquisseFr.pdf). Locators use this French published pagination: §5 pp. 24–27; §6 pp. 33–34; §8 p. 41. Do not substitute the pagination of the separately hosted English translation.

Malgoire, J. (2002, October 3). *Vers une géométrie des formes (topologiques), présentation introductive à un manuscrit inédit (juin–juillet 86) d’Alexandre Grothendieck* [Seminar abstract]. Institut Montpelliérain Alexander Grothendieck, Université de Montpellier. [Official seminar record](https://imag.umontpellier.fr/?idseance=509&page_id=526). Status: first-hand programme introduction, not an independently verified complete original axiom system.

Sturmfels, B., & Ziegler, G. M. (1993). Extension spaces of oriented matroids. *Discrete & Computational Geometry, 10*, 23–45. [https://doi.org/10.1007/BF02573961](https://doi.org/10.1007/BF02573961). [Author-hosted primary preprint](https://www.mi.fu-berlin.de/math/groups/discgeom/ziegler/Preprintfiles/020PREPRINT.pdf). Theorem 1.2: preprint p. 2, PDF page index 1. Corollary 4.5: preprint p. 16, PDF page index 15. The journal pagination comes from the publisher record and must not be substituted for the preprint’s local pages.

Michel Hua’s project. (2026). *154.modern.tex* [Supplied modernized interpretation of cote 154; AI-produced first pass, with specified later checks]. Local context artifact. The exact editorial status and dated revisions are stated in its header, H1–101. Cited here as a comparison edition, not as primary proof of manuscript readings or historical claims.

### Handoff: web retrieval references for root

Root must open the linked sources itself before using their web citations in the final answer.

| Source | This agent’s verified reference | Exact useful locator |
|---|---|---|
| Brown letter primary PDF | turn3view0 / turn5view1; root independently reported turn4view0 / turn6view0 | Printed pp. 134–135, letter 17 June 1986 |
| French Esquisse primary PDF | turn22view2; §8 find turn23view1 | §8 printed p. 41, PDF index 36; web lines 1340–1348 |
| French Esquisse §§5–6 | turn17view0 / turn17view1 | Printed pp. 24–27 and 33–34 |
| Cambridge French chapter | turn8view1 | 1997, pp. 7–48, DOI .003 |
| Cambridge volume metadata | turn21view1 / turn21view2 | Volume 1, LMS Lecture Note Series 242 |
| Sturmfels–Ziegler primary preprint | turn22view0; Cor. 4.5 find turn23view0 | Thm. 1.2 PDF index 1; Cor. 4.5 PDF index 15 |
| Sturmfels–Ziegler publisher | turn22view1 | DOI, authors, 1993, volume 10, pp. 23–45 |
| Malgoire seminar abstract | turn22view3 | 3 October 2002, title and programme description |

No original scan was opened for this report, no frozen artifact was modified, and no upload was made.
