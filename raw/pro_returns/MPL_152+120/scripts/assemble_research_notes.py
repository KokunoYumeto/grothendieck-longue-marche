#!/usr/bin/env python3
"""Assemble research only. Never read or write the frozen transcription files."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research"


def read(name):
    return (RESEARCH / name).read_text(encoding="utf-8")


def replace_once(text, old, new):
    count = text.count(old)
    if count != 1:
        raise ValueError(f"Expected one occurrence, got {count}: {old[:100]}")
    return text.replace(old, new, 1)


intro = r'''# MPL_152+120 — Research notes

## Scope, evidence and reading conventions

These notes accompany the complete diplomatic transcription of **cote 152, PDF scans 1–13, followed by cote 120, PDF scans 1–25**. The transcription was frozen at **2026-11-14 16:52:13 UTC**; the supplied context was opened at **16:52:25 UTC**. Research, contextual comparisons and modern terminology have made no changes to the frozen page files or combined fragment.

The 96 numbered items below contain a source and scan, a kind, a short quotation or formula anchor, and a comparison with the supplied context. Reader constructions give their confidence and reasons. Longer calculations appear in separately labelled verification blocks and Appendices A–B. The note numbers are editorial identifiers, and the mathematical examples carry no claim of novelty.

**Locator convention.** A citation such as `152/008` means page 8 of that cote's current official PDF, counting its institutional cover. Handwritten folios and printed archive footer numbers are reported separately. This convention also governs the newly consulted cotes 67, 121, 134-2, 136, 147, 149, 150 and 151. The *Esquisse* has a separate printed/PDF concordance, supplied with every substantive citation.

**Context convention.** `C147` and a bare contextual `147/NNN` expand to `context/MPL_147_138-190_transcription.tex`; `C149` and contextual `149/NNN` expand to `context/MPL_149_091-136_transcription.tex`. The corresponding `_notes.md` files are earlier first-pass research leads. `STATE` or `RESULTS_STATE.md` means `context/notes/RESULTS_STATE.md`, and `STATEMENTS_WITH_STATUS.md` means `context/STATEMENTS_WITH_STATUS.md`; these files belong to the supplied context archive and are not duplicated in this deliverable.

**Status convention.** “Proved”, “Known”, “Refuted” and “Open” attached to a supplied return ID retain the register's attribution to that return. The register reports no full-effort review of those rows; its medium review does not promote them. An intake reading or unchecked plan retains that status. The calculations in these notes address the displayed models and maps and do not upgrade a register entry merely by analogy.

**Search evidence.** The item-specific ledgers in `research/` record the actual searches: `context_search_root.json` for P01–P18 and R01–R08; `context_search_standing.json` for U01–U09 and T01–T06; `q1_context_by_note.json`, `q3_context_searches.json` and `q4_context_searches.json` for the three corresponding research sections. Source URLs, selected original-page hashes, failed accesses and index limits are retained in the source ledgers. Public machine transcriptions were used to locate external passages; historical claims below rely on the selected originals that were inspected.

### Guide to the four requested questions

| Question | Recorded outcome | Main items |
|---|---|---|
| Where are *tubulure* and *ombre* introduced and defined? | Earlier precise constructions are located; an explicit identification of the objects named at 149/133 remains unlocated in the bounded search. | Q1-01–Q1-07 |
| Did Grothendieck resolve the sphere “Remords” himself, in December 1981? | His own sphere calculation and retraction of the fear are located; the exact month is unverified, and the general proof retains his stated unfinished status. | R01–R05 |
| How do 120–121 compare with o-minimal structures and named variants? | Explicit model functors, Boolean reconstruction, finiteness tests and named comparisons are given; the all-compact countermodel is checked against the precise 120 branch. | Q3-01–Q3-11; A120-24 |
| What is the relation to Shiota's comparison? | The isomorphism-family map and checked Shiota realizations are specified, together with their scope and an explicit test of the final finite-diagram question. | Q4-01–Q4-12; Appendices A–B |

## 1. Cote 152: word types, plane trees and contours

'''

p = read("root_152.md")
p = p[p.index("## P01"):]
p = re.sub(r"^## (P\d+)", r"### \1", p, flags=re.M)

q1 = read("q1_tubulure_ombre.md")
q1 = q1[q1.index("### Q1-01"):q1.index("### Quote budget")]
q1 = re.sub(r"^### (?!Q1-)", "#### ", q1, flags=re.M)
q1 = q1.replace("## Source and search ledger", "### Source and search ledger")
q1intro = '''\n## 2. Tubulure and ombre: constructions and the remaining identification\n\nThe exact comparison sought at 149/133 remains unlocated in this search. The following items retain the formulas of the earlier constructions, their checked dates and their source limits; the discovery index cannot establish an archive-wide first occurrence.\n\n'''

r = read("root_q2.md")
r = r[r.index("## R01"):]
r = re.sub(r"^## ", "### ", r, flags=re.M)
rintro = '''\n## 3. Grothendieck's own return to the Remords\n\nThe continuation was checked in the original images of cote 151, PDF scans 41–44 (archive footers 40–43). The searchable public text served as a locator; the wording and cancellations were checked against those originals after the freeze.\n\n'''

q3 = read("q3_tame_axioms.md")
pre = q3[q3.index("## Source conventions and status"):q3.index("## Direct answer supported by cote 120")]
pre = pre.replace("## Source conventions and status", "### Source conventions and status")
direct = q3[q3.index("### Q3-01"):q3.index("## Page-level notes on the mathematical development")]
page = q3[q3.index("## Page-level notes on the mathematical development"):q3.index("## Primary bibliography and retrieval ledger")]
page = page.replace("## Page-level notes on the mathematical development", "### Page-level notes on the mathematical development")
page = replace_once(page,
    "The words may be aimed at the ideal of relatively compact subsets, but that is a reading question, and the frozen sentence is retained.",
    "Whether this phrase names the ideal of relatively compact subsets remains a reading question; the frozen sentence is retained.")
bib = '''### Primary bibliography and verification scope

1. Lou van den Dries and Chris Miller, *Geometric categories and o-minimal structures*, Duke Mathematical Journal 84 (1996), 497–540; author revision of 20 February 2001: <https://people.math.osu.edu/miller.1987/newg.pdf>. Definitions and comparison: §§1–3 and Appendix D; graph operations: Appendix B; finiteness and dimension inputs: 4.2, 4.3 and 4.7(1).
2. Chris Miller, *An upgrade for “Geometric categories and o-minimal structures”*, version 14 November 2012: <https://people.math.osu.edu/miller.1987/geofix.pdf>. The corrections were consulted; the present notes use no Whitney-stratification-of-maps assertion.
3. Matthias Aschenbrenner and Andreas Fischer, *Definable versions of theorems by Kirszbraun and Helly*, Proceedings of the London Mathematical Society 102 (2011), 468–502, DOI <https://doi.org/10.1112/plms/pdq029>; author manuscript <https://www.mat.univie.ac.at/~maschenbrenner/pdf/KH.pdf>, §6.2, Lemma 6.6 and its proof, p. 31. The proof was checked with its definably complete ordered-field and closed-domain scope; the empty-domain extension here is zero.
4. Artur Piękosz, *O-minimal homotopy and generalized (co)homology*, Rocky Mountain Journal of Mathematics 43 (2013), 573–617; author version <https://arxiv.org/abs/0808.3866>, §6, pp. 20–21, especially WD1–WD6 and the definition of weak polytope. Only the specified countable construction is used; the page range was checked against the author's publication list <https://piekosz.pl/>.
5. Heinrich Tietze, *Über Funktionen, die auf einer abgeschlossenen Menge stetig sind*, Journal für die reine und angewandte Mathematik 145 (1915), 9–14; metadata <https://geodesic.mathdoc.fr/item/JRAM_1915__145_149430/>. The original full text was not successfully fetched, so this is a bibliographical pointer; the extension verification uses item 3 and the displayed calculation.
6. Grothendieck, Montpellier cote 121, <https://grothendieck.umontpellier.fr/121.pdf>, 73 current PDF pages including the institutional cover. The exact selected primary-image checks and page-number convention are recorded above; source hashes and retrieval details are in the research ledger.
7. Michel Coste, *Topological types of fewnomials*, Banach Center Publications 44 (1998), 81–92: <https://matwbn.icm.edu.pl/ksiazki/bcp/bcp44/bcp4416.pdf>, printed p. 82 / PDF p. 2, clauses S1–S6 and graph-defined maps. Direct retrieval succeeded after the web reader returned 403; the operation table gives the present reader's comparison.
8. Ya'acov Peterzil and Charles Steinhorn, *Definable Compactness and Definable Subgroups of o-Minimal Groups*, Journal of the London Mathematical Society 59 (1999), 769–786, DOI <https://doi.org/10.1112/S0024610799007528>. Definition 1.1 and Theorem 2.1 with its proof were read in the author-associated full-text copy <https://www.academia.edu/18806220/Definable_Compactness_and_Definable_Subgroups_of_o_Minimal_Groups>.

'''
late = q3[q3.index("## Cote 121: retrieved primary manuscript and exact comparison"):q3.index("### Cote 121 quotation ledger")]
late = late.replace("## Cote 121: retrieved primary manuscript and exact comparison", "### Cote 121: primary manuscript and exact comparison")
late = replace_once(late,
    "The comparison with 120 sends the coordinate maps to M1, products to M4, coverage to M8, compactness to M9, neighbourhoods to M10, unions to M5, and the arrow \\(f_X|_Y=f_Y\\) to M7; every map is the identical coordinate or scalar function. This records formulas, without ordering the undated drafts chronologically.",
    "For the displayed operations, send each coordinate, product or scalar function to itself; the corresponding 120 labels are M1, M4, M5 and M7–M10. This supplies the comparison maps without ordering the undated drafts chronologically.")
late = late.replace("checked in `turn49view1` and `turn56view0`", "checked in the author text cited in bibliography item 1")
late = replace_once(late,
    "has no finite subcover, because a finite choice leaves algebraic points between its largest \\(a\\) and smallest \\(b\\).",
    "has no finite subcover, because a finite choice covering both endpoints must contain both kinds of set and leaves algebraic points between its largest \\(a\\) and smallest \\(b\\).")
continuity = r'''
#### Additional verification of the displayed extension on compact \(Z\)

For the nonempty compact domain used here, put \(m=\min_Z g>1\) and \(M=\max_Z g<2\). The numerator \(H(x)=\min_{a\in Z}g(a)\|x-a\|\) satisfies \(|H(x)-H(y)|\le M\|x-y\|\), by the triangle inequality, so \(G=H/d(\,\cdot\,,Z)\) is continuous off \(Z\). A nearest point gives \(G(x)\le M\), while every distance ratio is at least one and gives \(G(x)\ge m\); in particular \(\tau^{-1}(G(x))\) is defined.

A minimizing point \(a_x\) obeys \(\|x-a_x\|\le(M/m)d(x,Z)\), so \(a_x\to z\) as \(x\to z\in Z\). With \(b_x\) a nearest point, the inequalities \(g(a_x)\le G(x)\le g(b_x)\) and \(a_x,b_x\to z\) prove continuity at \(z\). Finally \(\tau^{-1}(s)=(2s-3)/\sqrt{1-(2s-3)^2}\) uses rational coefficients, completing the parameter check; the empty-domain extension is zero. These are direct verifications of the already displayed construction, also checked independently in the research review.

'''
late = late.replace("### Scope of the joint answer", continuity + "### Scope of the joint answer")
q3main = "\n## 4. Cotes 120–121 and the o-minimal comparison\n\n" + pre + direct + late + page + bib

q4 = read("q4_shiota.md")
q4 = q4[q4.index("### Q4-01"):]
q4 = replace_once(q4,
    "The canonical comparison displayed in *Esquisse* is the map of isomorphism families written above, and “catégories isotopiques (ou même ∞-isotopiques)” records two specified levels of the programme [S1].",
    r"Grothendieck takes \(T\) finer than \(T'\) and \(T\)-moderate spaces \(X,Y\), and writes the canonical map \(\operatorname{Isom}_{T}(X,Y)\to\operatorname{Isom}_{T'}(X,Y)\) with a requested bijection on components and homotopy equivalence of its semisimplicial models, together with requested analogous comparisons for constrained map families and systems of spaces; “catégories isotopiques (ou même ∞-isotopiques)” records the specified levels [S1].")
q4 = q4.replace("## Appendix A", "### Appendix A").replace("## Appendix B", "### Appendix B")
q4 = q4.replace("### The same calculation for an ordered indexing set", "#### The same calculation for an ordered indexing set")
q4 = q4.replace("## Primary sources and verification scope", "### Primary sources and verification scope")
q4intro = '''\n## 5. Comparison of tame theories, Shiota and the final diagram question\n\nThe following items specify the comparison maps and the verified scope of the cited results. Appendices A–B give the complete calculations for the two readings of 120/025 that are explicitly tested: simultaneous isomorphism of finite diagrams and the displayed nested-subset example.\n\n'''

standing = read("standing_questions.md")
standing = standing.replace("# Standing question I — Steps marked by the manuscript itself", "## 6. Standing question I — Steps marked by the manuscript itself")
standing = standing.replace("# Standing question II — Title sheets and visible numbering", "## 7. Standing question II — Title sheets and visible numbering")
standing = re.sub(r"^## ([UT]\d+)", r"### \1", standing, flags=re.M)

end = r'''
## 8. Verification limits and unresolved tasks indexed to the supplied register

| Register or source question | Contribution of this package | Remaining task recorded here |
|---|---|---|
| WG2 §1.8 #5; INTAKE 20261114 §13.2 | Q1 records original-page definitions and explicit maps; P09–P11 record the rotation revisions and a checking dictionary. | Locate the exact site or universal property behind 149/133's named objects and its comparison morphism; resolve the marked glyphs from further ink evidence. |
| EXIT_ONE_TYPE P1d1; STRATA C.1/C.5/C.6 | R01–R03 add the author's sphere test and the explicitly typed modern truncation map. | The return claims keep their review status; the sphere test alone does not provide the general reconstruction proof left open in the continuation. |
| Chronology of the Remords continuation | R05 records the original folder date and the retrospective period reference. | Obtain an autograph or independently grounded date for the specific 151/041–044 leaves. |
| WG2 B15 (§1.2); BISITE D.12 | Q3 gives models, exact family/graph maps, compactification, parameter tests and local completion. | Identify the actual families and arrows in any proposed full comparison with the open-test realization; the supplied planning/open statuses remain. |
| CATHOT E.17; TOTASPH E.6 | A120-10/A120-13/A120-24 specify the directed and countable presentations and the weak-polytope construction. | The existence of the homotopy-invariant presentation in E.17 remains open as recorded; the explicit exhaustion does not settle that existence problem. |
| MPL_150_001-043 Q4b; STRATA C.5–C.6 | Q4 gives the actual isomorphism-family comparison, checked Shiota statements, compatible marked-subset charts and the rotation computation. | Verify the requested higher-parametric comparison at its full stated scope and identify the abbreviated “essentially” in 120/025; no such interpretation was inserted into the frozen transcription. |
| FLAGGED_149 ZD8; EXIT_ONE_TYPE P4e; RESIDUE H.4 | P12–P16 supply disk-dual and labelled-tree maps; R08 retains the meridian arrows. | Establish any comparison with the exact normal-crossings or moduli objects in those returns through their specified maps; the finite examples do not promote those statuses. |

The complete 38-page transcription, every doubt marker and all 734 inventory rows remain the image-based record. The research records preserve source limits and computations so that further work can address the remaining questions without silently replacing that record.
'''

text = intro + p + q1intro + q1 + rintro + r + q3main + q4intro + q4 + "\n" + standing + end
text = text.replace(
    "`q1_context_by_note.json`, `q3_context_searches.json` and `q4_context_searches.json` for the three corresponding research sections",
    "`q1_context_by_note.json`, `q3_context_by_note.json` and `q4_context_searches.json` for the three corresponding research sections")
text = text.replace(
    "the quotient coordinates and amalgam maps already displayed for M6–M7",
    "the quotient coordinates and amalgam maps in A120-07–A120-08")
for name in (
    "context_search_root.json", "context_search_standing.json",
    "q1_context_by_note.json", "q1_context_search.json",
    "q1_primary_extract_manifest.json", "q1_index_manifest.json",
    "q1_public_index_hits.json", "q1_web_ledger.json",
    "q3_context_searches.json", "q3_context_by_note.json",
    "q4_context_searches.json",
):
    text = text.replace(f"`{name}`", f"`research/{name}`")
ids = re.findall(r"^### ((?:P|R|U|T)\d{2}|Q[134]-\d{2}|A120-\d{2}a?)\b", text, flags=re.M)
if len(ids) != 96 or len(ids) != len(set(ids)):
    raise ValueError(f"Unexpected research item inventory: {len(ids)} / {len(set(ids))}")
target = ROOT / "MPL_152+120_notes.md"
target.write_text(text, encoding="utf-8")
print(f"Wrote {target.name}: {len(text.split())} whitespace-delimited words; {len(ids)} numbered items")

