#!/usr/bin/env python3
"""Assemble research notes only; never reads or writes the frozen transcription.

Candidate bodies and their prior context-search records are retained in records/.
This script performs editorial selection, grouping, and Markdown presentation.
"""
from pathlib import Path
import argparse
import re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / "records"


def candidates(filename):
    text = (RECORDS / filename).read_text(encoding="utf-8")
    matches = list(re.finditer(r"^#{2,3} ([A-Z]\d{2}) — (.+)$", text, re.M))
    result = {}
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[match.start():end]
        # Stop at the next non-candidate section, including bibliographies.
        rest = block[block.index("\n") + 1:]
        section = re.search(r"^## (?![A-Z]\d{2} —)", rest, re.M)
        if section:
            rest = rest[:section.start()]
        block = f"### {match.group(1)} — {match.group(2)}\n" + rest
        result[match.group(1)] = block.strip()
    return result


HEADER = r"""# Research notes: cote 154, scans 127–176

## Scope, evidence, and reading conventions

These notes concern the fifty selected pages of `154.pdf`, transcribed in `pages/MPL_154_127-176_154_scanNNN.tex` and in the combined fragment. **The transcription was frozen at 2026-11-15 01:44:43 UTC; the context archive was opened at 01:44:50 UTC.** Interpretations and reading questions below do not change its text, uncertain readings, drawings, or cancellation marks.

The closest contextual identification is the relative-position “surface modulaire” described in the *Esquisse*, §8, within its programme of topological and combinatorial moduli problems; P01–P03 answer the requested comparison with tame topology and the 1986 geometry of forms. C01–C10 examine the supplied `154-generisation-cube` lead, including what a conditional local proof can establish and what remains unidentified. The principal unresolved construction in this window concerns the critical endpoints of semistable edges, alongside questions about operators, quotients, and local incidence data.

**Locators.** Unless another cote is specified, “scan” means a page of `154.pdf`; a locator such as `154:31–44` means scan 154, approximate lines 31–44 of its frozen TeX source, not numbered manuscript lines. The low marginal pagination runs 126–175; this is kept distinct from the scan numbering and from printed computer page numbers. “119/50” denotes the supplied Esquisse transcription's cote/scan marker, with its separately recorded manuscript or typescript page number when stated.

**Context and status.** `RESULTS_STATE` means the supplied `notes/RESULTS_STATE.md`; `STATEMENTS` means `STATEMENTS_WITH_STATUS.md`; “supplied Esquisse” means `Esquisse_cote119_copy1_API_transcription.tex`. Their README, the entire results register, and the statements register were read before the notes, as were the relevant Esquisse sections. The earlier materials are leads or research-return claims unless their entries explicitly record review: labels such as *Proved*, *Known*, *Refuted*, and *Open* are reported as register labels, and the original proof files named by those registers were not supplied for independent review. No register status is promoted or changed here.

**Searches and kinds.** Every numbered candidate was preceded by a separate search of the supplied context for its objects and terms; the timestamped queries and hits are retained in `records/root_context_searches.jsonl`, `records/research_doubts_searches.md`, `records/research_cube_searches.md`, and `records/research_gluing_searches.md`. The selected notes state the relevant match and its limits, or record that no matching item was found. Each body is one to four sentences; Source, Kind, Quote, Context and Relation fields are metadata. “Own idea” identifies an editorial inference, conditional calculation, suggested construction, or comparison made here, with confidence and a reason; it claims neither novelty nor an established archival result. Quotations containing `\unsure`, `\deleted`, or related macros reproduce the frozen reading as code, including its uncertainty.

**Primary literature.** External comparisons use the primary sources listed at the end; numbered results refer to the version actually consulted. The published Esquisse was checked for the direct historical matches, while the supplied API transcription remains the navigable preliminary context. Documentary dates and title evidence appear in D01–D04 and the date appendix; the manuscript's own hesitation is distinguished from our reading uncertainty in the two separate sections below.
"""


BIBLIOGRAPHY = r"""## References and consulted versions

### Archival and supplied materials

Grothendieck, A. (1983–1984, undated portions). *[Système de pseudo-droites]* [Unpublished manuscript notes, cote 154, selected scans 127–176]. Archives Grothendieck, Université de Montpellier. Catalogue dating is external metadata; the selected manuscript's local date and reused printed dates are discussed in D02–D03.

Grothendieck, A. (1997). Esquisse d'un Programme. In L. Schneps & P. Lochak (Eds.), *Geometric Galois actions* (Vol. 1, pp. 7–48). Cambridge University Press. https://doi.org/10.1017/CBO9780511758874.003. Consulted French text: https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EsquisseFr.pdf; direct comparisons concern §§3, 5–6 and 8, especially the relative-position surface on printed p. 41.

Université de Montpellier. (n.d.). *Archives Grothendieck*. Retrieved November 15, 2026, from https://grothendieck.umontpellier.fr/archives-grothendieck/. Consulted for catalogue metadata of cotes 154 and 156-1–9; the catalogue entries are not substitutes for the texts of the 1986 volumes.

*MPL_154_127-176_context* [User-supplied context archive]. (n.d.). `README.md`; `notes/RESULTS_STATE.md`; `STATEMENTS_WITH_STATUS.md`; `Esquisse_cote119_copy1_API_transcription.tex`. Exact return IDs, statuses, named source files and archive locations are identified note by note and in the search ledgers; unavailable original return files have not been silently treated as inspected evidence.

### Mathematical primary sources

Ayala, D., Francis, J., & Rozenblyum, N. (2019). A stratified homotopy hypothesis. *Journal of the European Mathematical Society, 21*(4), 1071–1178. https://doi.org/10.4171/JEMS/856. The numbered comparisons in G09 use the consulted author version at https://math.montana.edu/dayala/documents/Striation.pdf, Lemma 3.3.5, Corollary 3.3.11 and Theorem 4.2.5; the framework is conically smooth.

Backman, S., Santos, F., & Yuen, C. H. (2026). Extension-lifting bijections for oriented matroids. *Discrete & Computational Geometry, 75*, 969–994. https://doi.org/10.1007/s00454-026-00834-w. The relevant passage is §2.1, Lemma 2.4, explicitly attributed there to Las Vergnas: compatibility of an extension signature is tested on the indicated rank-two minors.

Björner, A. (1984). Posets, regular CW complexes and Bruhat order. *European Journal of Combinatorics, 5*(1), 7–16. https://doi.org/10.1016/S0195-6698(84)80012-8. Consulted primary article text at https://core.ac.uk/download/pdf/82377898.pdf, §3, printed pp. 10–11, on regular cell complexes and their face posets.

Douteau, S., & Waas, L. (2022). *From homotopy links to stratified homotopy theories* (arXiv:2112.02394v2) [Preprint]. https://arxiv.org/pdf/2112.02394. The fetched text identifies version 2, dated December 29, 2022; Theorem 6.1, printed p. 60, is the version-specific comparison cited in G09.

Goodman, J. E., & Pollack, R. (1980). On the combinatorial classification of nondegenerate configurations in the plane. *Journal of Combinatorial Theory, Series A, 29*(2), 220–235. https://doi.org/10.1016/0097-3165(80)90011-4. Consulted publisher abstract and indexed introductory primary text at https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/PollackRichard/Pollack5.pdf, printed pp. 220–221; this is the allowable-sequence comparison used in C09, with no theorem about the manuscript's particular space inferred from it.

Hass, J., & Scott, P. (1994). Shortening curves on surfaces. *Topology, 33*(1), 25–43. https://doi.org/10.1016/0040-9383(94)90033-7. Consulted author-hosted article: https://www.math.ucdavis.edu/~hass/Research/Papers/Minimal/ShorteningCurves.pdf, especially Lemmas 1.2, 1.4 and 1.6 and the proof of Lemma 1.6, printed pp. 26–28.

Sturmfels, B., & Ziegler, G. M. (1993). Extension spaces of oriented matroids. *Discrete & Computational Geometry, 10*, 23–45. https://doi.org/10.1007/BF02573961. Consulted 21-page author preprint: https://www.mi.fu-berlin.de/math/groups/discgeom/ziegler/Preprintfiles/020PREPRINT.pdf; Theorem 1.2 and Corollary 4.5 for the rank-three homotopy-sphere conclusion, and Theorem 1.1/Proposition 2.2 with Proposition 2.1 for the distinction between fixed and varying realizations. Result and preprint-page locators are not silently transferred to the journal pagination.
"""


def present(block):
    # Raw custom editorial macros are exact quotations, not KaTeX commands.
    block = re.sub(r"<code>(.*?)</code>", lambda m: "`" + m[1] + "`", block, flags=re.S)
    def inline_math(match):
        value = match[1]
        if re.search(r"\\(?:unsure|deleted|inserted|illegible|uline|uuline|margin)\b", value):
            return "`" + value + "`"
        return match[0]
    block = re.sub(r"\\\((.*?)\\\)", inline_math, block, flags=re.S)
    for before, after in {
        "comparison158": "comparison, scan 158",
        "comparisons147/": "comparisons 147/",
        ";119/": "; 119/",
        "sourcesI ms": "sources I ms",
        "sourcesIX-": "sources IX-",
        "label1": "label 1",
        "Scan151": "Scan 151",
        "cote154": "cote 154",
        "Hua154-generisation-cube": "Hua, 154-generisation-cube",
        "Esquisse§8": "Esquisse §8",
        "APIunchecked": "API unchecked",
        "rank18": "rank 18",
        "conjecture(unsearched)": "conjecture (unsearched)",
        "their2ν": "their 2ν",
        "manuscript’sν": "manuscript’s ν",
        "Backman,Santos,&Yuen2026,Definition2.1 andLemma2.4": "Backman, Santos, and Yuen (2026), Definition 2.1 and Lemma 2.4",
        "Goodman&Pollack1980,abstract/introduction": "Goodman and Pollack (1980), abstract and introduction",
        "sequences,Goodman/Pollack,or": "sequences, Goodman/Pollack, or",
        "In the support-controlled model": "In the model restricting changes to the chosen disks",
        "because the same-position and local-incidence assumptions are not supplied": "because the position and local incidences have not been identified between the two descriptions",
    }.items():
        block = block.replace(before, after)
    block = re.sub(r"\*\*Source:\*\* cote 154,(\d{3}):", r"**Source:** 154.pdf, scan \1, TeX lines ", block)
    block = block.replace(
        "Only with additional same-position, distinct-incidence, and regular-surface assumptions would a",
        "Only if both passages concern the same position, the listed incidences are distinct local incidences, and the cell structure is a regular surface cellulation would a")
    return block


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--draft-without-cube", action="store_true")
    args = parser.parse_args()
    all_notes = {}
    for filename in ("root_research_notes.md", "research_doubts_memo.md",
                     "research_gluing_memo.md", "research_extension_space_memo.md"):
        all_notes.update(candidates(filename))
    cube_path = RECORDS / "research_cube_memo.md"
    if cube_path.exists():
        all_notes.update(candidates(cube_path.name))
    elif not args.draft_without_cube:
        raise SystemExit("Cube memo is required for the final notes.")

    groups = [
        ("1. Classification: the relative-position project and its historical setting", [f"P{i:02}" for i in range(1, 6)]),
        ("2. Standing question: steps explicitly questioned or left unfinished", [f"U{i:02}" for i in range(2, 9)]),
        ("3. Standing question: title sheets, pagination, and dated layers", [f"D{i:02}" for i in range(1, 5)]),
        ("4. The generization cube: scope, local model, and compatibility", [f"C{i:02}" for i in range(1, 11)]),
        ("5. Frames, orientations, and combinatorial counts", [f"M{i:02}" for i in range(1, 7)]),
        ("6. The cellular surface and the missing attachment data", ["G01", "G02", "G03", "G04", "G06", "G09", "G10", "G11", "G12", "G13"]),
        ("7. Extension spaces and the distinction between homotopy and surface structure", ["X01", "X02", "X03"]),
        ("8. Immersed configurations, exceptional facets, and numerical tests", [f"I{i:02}" for i in range(1, 9)]),
        ("9. Curve moves and possible proof methods", ["L01", "L02"]),
        ("10. Answered questions, rejected trials, and substantive revisions", ["U01", "W01", "W02", "W03", "W04", "W05", "W07", "W08", "W09", "W10"]),
        ("11. Reading questions that affect mathematical interpretation", [f"Q{i:02}" for i in range(2, 12)]),
    ]
    parts = [HEADER.strip()]
    selected = []
    for title, ids in groups:
        available = [key for key in ids if key in all_notes]
        if available != ids and not (args.draft_without_cube and title.startswith("4.")):
            raise SystemExit(f"Missing candidates in {title}: {set(ids) - set(available)}")
        if not available:
            continue
        parts.append("## " + title)
        for key in available:
            block = all_notes[key]
            # Align documentary/revision kinds with the requested note taxonomy.
            if key.startswith("D"):
                block = block.replace("**Kind:** documentary observation", "**Kind:** own idea / documentary observation", 1)
            if key == "U01":
                block = block.replace("**Kind:** own classification", "**Kind:** own idea / classification", 1)
            if key == "U07":
                block = block.replace("**Kind:** explicit mathematical question", "**Kind:** self-flagged / explicit mathematical question", 1)
            if key == "U08":
                block = block.replace("**Kind:** incomplete written construction", "**Kind:** reading question / incomplete written construction", 1)
            if key in {"W02", "W03", "W04", "W05", "W08", "W09", "W10"}:
                block = block.replace("**Kind:** ", "**Kind:** own idea / ", 1)
            if key == "Q10":
                block = block.replace("**Kind:** bounded declarative claims", "**Kind:** unproved claim / bounded declarative claims", 1)
            if key == "C01":
                block = block.replace("**Kind:** manuscript assertion", "**Kind:** unproved claim", 1)
            if key == "C05":
                block = block.replace("**Kind:** notation question", "**Kind:** reading question", 1)
            if key == "C07":
                block = block.replace("**Kind:** manuscript claim", "**Kind:** unproved claim", 1)
            if key == "C08":
                block = block.replace("**Kind:** bounded literature comparison / own explanatory identification", "**Kind:** own idea / bounded literature comparison", 1)
            if key == "C09":
                block = block.replace("**Kind:** bounded primary-literature comparison", "**Kind:** unpursued implication / primary-literature comparison", 1)
            if key == "C10":
                block = block.replace("**Kind:** explicit manuscript question", "**Kind:** self-flagged / explicit manuscript question", 1)
            parts.append(present(block))
            selected.append(key)
    documentary = (RECORDS / "research_doubts_memo.md").read_text(encoding="utf-8")
    appendix = documentary[documentary.index("## Documentary appendix:"):].strip()
    parts.extend([present(appendix), BIBLIOGRAPHY.strip()])
    output = ROOT / "MPL_154_127-176_notes.md"
    output.write_text("\n\n".join(parts) + "\n", encoding="utf-8")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    (RECORDS / "research_notes_selection.txt").write_text(
        f"Assembled {now}\n{len(selected)} selected notes\n" + " ".join(selected) + "\n"
        "Omitted duplicate candidates: G05 (I01), W06 (I01), Q01 (C01).\n"
        "Every selected candidate retains its original prior context-search record.\n"
        "Frozen page and combined files were neither read nor written by the assembler.\n",
        encoding="utf-8")
    print(f"{output}: {len(selected)} notes; {len(output.read_text().split())} whitespace-delimited words")


if __name__ == "__main__":
    main()
