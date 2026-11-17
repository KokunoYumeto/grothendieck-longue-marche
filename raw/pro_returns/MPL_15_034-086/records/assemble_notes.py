"""Assemble reviewed research sections only; never opens a TeX file for writing."""
from pathlib import Path
import argparse
import re

PACKAGE = Path(__file__).resolve().parent.parent
RECORDS = PACKAGE / "records"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--final", action="store_true")
    parser.add_argument("--section", action="append", default=[])
    args = parser.parse_args()
    mode = "" if args.final else "\n**Working research report; additional sections are still being reviewed.**\n"
    header = """# Research notes — MPL_15_034-086

## Scope and status

The witnesses are the 31 supplied scans of cote 15: 034, 036, 038, 040, 042, 044, 046, 048, 050, 052, 054, 056, 060, 061, 066, 067, 068, 069, 070, 071, 072, 073, 074, 075, 076, 077, 078, 079, 084, 085 and 086. All were transcribed and visually audited before the context was opened; the transcription was frozen at 2026-11-17 20:48:04 UTC, and the context was opened at 20:48:11 UTC. These notes do not amend the frozen transcription.

The supplied context was used as research evidence only. Its earlier returned notes are first-pass leads, and an entry marked proved in RESULTS_STATE remains a research return's claim unless that entry explicitly records review. No open result in that register is marked solved by this report.

### Context citation key

| Short name | Supplied file |
|---|---|
| CT | MPL_16+47+54+44_transcription.tex |
| CN | MPL_16+47+54+44_notes.md |
| N15a | same_cote_15/MPL_15_087-138_notes.md |
| N15b | same_cote_15/MPL_15_195-228+18_002-017_notes.md |
| RS / RESULTS_STATE | notes/RESULTS_STATE.md |
| Hua | hua_project/15.modern.tex, read with hua_project/README.md |
| Oda | Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf |

Hua's page n corresponds to archive scan n+1. A statement attributed to his modernised reading or findings register is his project's interpretation, not a transcription and not an established result of this report. References to neighboring scan numbers through N15a or N15b are reports in those supplied notes; the corresponding original scans were not supplied here and have not been re-read.

Each numbered research item gives its witness, kind, brief source words when applicable, contextual comparison and relevant result-register entry. Own calculations carry their confidence and reason. Quotations containing doubtful words remain identified as such, and cancellations are distinguished from live assertions.
"""
    header += """
### Reading guide

The planning answers and comparison tables come first, followed by the scan-specific studies of Deuring gerbes (D01–D18), Brandt and Picard categories (B01–B21), compact tori and norms (R01–R14), and reused sheets (X01–X08). The final two registers collect the manuscript's own unverified steps (U01–U22) and its titles and page-number evidence (P01–P18). MB01–MB16 provide individual witnesses for the planning answers.

Validation is documented separately in the records. Full LaTeX compilation was unavailable, and X08 identifies one prose/math-font markup defect discovered after the freeze on scan 069; neither that discovery nor the research comparisons changed the frozen files.
"""
    chunks = [header, mode]
    for name in args.section:
        path = RECORDS / name
        if not path.is_file():
            raise SystemExit(f"Missing reviewed section: {path}")
        content = path.read_text(encoding="utf-8")
        if name == "research_root.md":
            content = content[content.index("## R01"):].replace(
                "## R01", "## Compact tori, norm maps, and the final NB\n\n### R01", 1
            )
            for prefix in ("R", "X"):
                content = re.sub(r"(?m)^## (" + prefix + r"\d+)", r"### \1", content)
            content = content.replace(
                "### X01", "## Reused typed and printed leaves\n\n### X01", 1
            )
            content = content.replace("## Primary references checked for this section", "### Primary references for the torus and reused-sheet notes")
        elif name == "research_deuring.md":
            content = content[content.index("## D01"):]
            content = re.sub(r"(?m)^(#{2,5}) ", r"#\1 ", content)
            content = "## Deuring gerbes and crystalline orientations (scans 034–056)\n\n" + content
        elif name == "research_brandt.md":
            content = content[content.index("**Context and status conventions."):]
            content = re.sub(r"(?m)^(#{2,5}) ", r"#\1 ", content)
            content = "## Brandt and Picard categories (scans 060–078)\n\n" + content
        elif name == "research_motivic_bridges.md":
            content = content[content.index("## Evidence and inherited status"):]
            content = re.sub(r"(?m)^(#{2,5}) ", r"#\1 ", content)
            content = "## Planning questions and motivic comparisons\n\n" + content
        elif name == "research_standing.md":
            content = content[content.index("## Steps the manuscript itself marks as unverified"):]
        chunks.append(content.strip())
    output = PACKAGE / "MPL_15_034-086_notes.md"
    output.write_text("\n\n".join(chunks).strip() + "\n", encoding="utf-8")
    print(f"{output}: {len(output.read_text().split())} whitespace-separated words")

if __name__ == "__main__":
    main()
