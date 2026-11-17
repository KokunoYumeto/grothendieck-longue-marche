#!/usr/bin/env python3
"""Assemble finalized research blocks; never write a transcription file."""
from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research"


def between(text, start, end=None):
    position = text.index(start)
    stop = len(text) if end is None else text.index(end, position + len(start))
    return text[position:stop].strip()


def body(text, start, end=None):
    return between(text, start, end)[len(start):].strip()


def main():
    frozen = sorted((ROOT / "pages").glob("*.tex")) + [ROOT / "MPL_91_019-058_transcription.tex"]
    before = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in frozen}
    a = (RESEARCH / "notes_019-032.md").read_text()
    b = (RESEARCH / "notes_034-049.md").read_text()
    c = (RESEARCH / "notes_050-058.md").read_text()
    synthesis = (RESEARCH / "synthesis.md").read_text().strip()
    aliases = between(b, "| Abbreviation |", "\nRS's orientation")
    synthesis = synthesis.replace(
        "## P01 —",
        "### Compact context aliases used in the catalogue\n\n" + aliases +
        "\n\nThe catalogue contains 97 scan-level items (A01–A36, B01–B35 and C01–C26). "
        "P01–P03 are the three separately searched synthesis tables. "
        "The two standing questions are collected after the catalogue.\n\n## P01 —",
        1,
    )
    synthesis = synthesis.replace(
        "**Search record:** P01.",
        "**Brief source quote:** “est fini sur S ?” (054). **Search record:** P01.",
        1,
    ).replace(
        "**Search record:** P02.",
        "**Brief source quote:** “Compléments dans le cas de Greenberg” (034). **Search record:** P02.",
        1,
    ).replace(
        "**Search record:** P03,",
        "**Brief source quote:** “Greenberg d'égale caractéristique” (037). **Search record:** P03,",
        1,
    )

    a_catalogue = between(a, "## A. Obstructions", "## C. Separate")
    a_catalogue = a_catalogue.replace(
        "## A. Obstructions and the proposed rigidification argument",
        "## Scans 019–024 — Obstructions and the proposed rigidification argument",
    ).replace(
        "## B. Scheme representability, the corollaries and the letter",
        "## Scans 025–032 — Scheme representability, the corollaries and the letter",
    )
    b_catalogue = between(b, "## A. Plans", "## Standing question:")
    headings = {
        "## A. Plans, formal identities and non-effective descent":
            "## Scans 034–037 — Plans, formal identities and non-effective descent",
        "## B. Vector bundles and the intersection problem":
            "## Scans 038–039 — Vector bundles and the intersection problem",
        "## C. Gluing and the scheme-existence criterion":
            "## Scans 040–044 — Gluing and the scheme-existence criterion",
        "## D. Properness, projectivity and determinant bundles":
            "## Scans 044–045 — Properness, projectivity and determinant bundles",
        "## E. Grassmannian equations, finiteness and dimension":
            "## Scans 046–049 — Grassmannian equations, finiteness and dimension",
        "## F. Links not developed on these leaves":
            "## Further links from scans 034–049",
    }
    for old, new in headings.items():
        b_catalogue = b_catalogue.replace(old, new)
    c_catalogue = between(c, "### C01", "## Root-range standing index:")

    a_flags = body(a, "### Self-flagged or explicitly conditional steps",
                   "### Mathematically significant withdrawals and revisions")
    b_flags = body(b, "## Standing question: steps the manuscript marks as unfinished or unverified",
                   "## Standing question: titles, internal sequences and page counts")
    c_flags = body(c, "## Root-range standing index: authorial uncertainty",
                   "\nThere is no separate title sheet")
    withdrawals = body(a, "### Mathematically significant withdrawals and revisions",
                      "### Titles, sequences and page counts")
    a_titles = body(a, "### Titles, sequences and page counts",
                   "## D. Disposition of the two relevant supplied findings")
    b_titles = body(b, "## Standing question: titles, internal sequences and page counts",
                   "## Checked primary comparisons and limits")
    c_titles = c[c.index("There is no separate title sheet"):].strip()
    a_refs = body(a, "## E. Primary references and verification limits")
    b_refs = body(b, "## Checked primary comparisons and limits")
    c_refs = (RESEARCH / "root_primary_references.md").read_text().split("\n", 1)[1].strip()

    parts = [
        synthesis,
        a_catalogue,
        b_catalogue,
        "## Scans 050–058 — Smoothness, numerical claims, finite étale objects and compatibility\n\n" + c_catalogue,
        "## Standing question 1 — Steps marked unfinished, conditional or unverified\n\n"
        "These tables index the searched catalogue items. They distinguish an explicit authorial question "
        "from an uncertain reading, a conditional hypothesis, an organizational instruction and a cancelled attempt.",
        "### Scans 019–032\n\n" + a_flags,
        "### Scans 034–049\n\n" + b_flags,
        "### Scans 050–058\n\n" + c_flags,
        "## Significant withdrawals and revisions in the early argument\n\n" + withdrawals,
        "## Standing question 2 — Title sheets, internal sequences and page counts\n\n"
        "The assignment contains 38 retained scan faces; that count is not an authorial page total. "
        "No secure independent manuscript page number was identified, and archive foliation remains in TeX comments.",
        "### Scans 019–032\n\n" + a_titles,
        "### Scans 034–049\n\n" + b_titles,
        "### Scans 050–058\n\n" + c_titles,
        "## Primary comparisons and verification limits\n\n"
        "The following references were checked after the freeze. They inform these research notes only; "
        "their conventions and statements were not used to repair the diplomatic transcription.",
        "### Obstruction, representability and automorphism comparisons\n\n" + a_refs,
        "### Descent, norms and relative-morphism comparisons\n\n" + b_refs,
        "### Infinitesimal and finite étale comparisons\n\n" + c_refs,
        "## Supporting proof and search records\n\n"
        "- [Finite étale criterion and counterexample review](research/etale_criterion_review.md): "
        "EC01–EC09, including the full equivalence proof under finite locally free hypotheses and its exact primary references.\n"
        "- [Linear compatibility review](research/linear_argument_review.md): "
        "the independent calculation behind A11–A13, with the mixed relation, corrected quotient and fixed-diagram base change.\n"
        "- The three research-range files retain the source blocks from which this catalogue was assembled; "
        "the accompanying query plans and search logs record every item's comparison with all six supplied context files.\n"
        "- The doubts file, inventory, audit record and progress log document the separate visual transcription. "
        "Research confidence is not a substitute for visual confidence in the handwriting.\n\n"
        "No supplied first-pass result, candidate finding or open register item is promoted to a new status by this package. "
        "The explicit calculations and the finite locally free proof have the bounded conclusions stated beside them.",
    ]
    result = "\n\n".join(part.strip() for part in parts) + "\n"
    ids = re.findall(r"^### ([ABC]\d{2}) —", result, re.M)
    expected = [f"A{i:02}" for i in range(1, 37)] + [f"B{i:02}" for i in range(1, 36)] + [f"C{i:02}" for i in range(1, 27)]
    assert ids == expected, (len(ids), len(expected))
    assert all(hashlib.sha256(p.read_bytes()).hexdigest() == h for p, h in before.items())
    target = ROOT / "MPL_91_019-058_notes.md"
    target.write_text(result)
    assert all(hashlib.sha256(p.read_bytes()).hexdigest() == h for p, h in before.items())
    print(f"Assembled {target.name}: {len(ids)} scan-level notes; {len(result.split())} words including metadata and tables.")


if __name__ == "__main__":
    main()
