"""Assemble research only. This script never writes frozen transcription files."""
from pathlib import Path
import re
import json

ROOT = Path(__file__).resolve().parents[1]
REC = ROOT / "records"

def read(name):
    return (REC / name).read_text(encoding="utf-8")

def between(text, start, end=None):
    part = text.split(start, 1)[1]
    return part.split(end, 1)[0].strip() if end else part.strip()

def items(text, prefix):
    pattern = rf"(?ms)^#{{2,3}} ({prefix}\d+[a-z]?) — ([^\n]+)\n(.*?)(?=^#{{1,3}} |\Z)"
    found = re.findall(pattern, text)
    return "\n\n".join(f"### {key} — {title}\n{body.rstrip()}" for key, title, body in found), [x[0] for x in found]

def clean_bibliography(text):
    text = re.sub(r"(?m)^\d+\. ", "- ", text)
    text = re.sub(r" Retrieval references?:[^\n]*", "", text)
    text = re.sub(r" Web retrieval:[^\n]*", "", text)
    text = re.sub(r" retrievals? turn[^\n]*", "", text, flags=re.I)
    text = re.sub(r"(?m)^Web retrieval references[^\n]*\n?", "", text)
    # Convert bare URLs to Markdown links while preserving existing links.
    text = re.sub(r"(?<!\()https?://[^\s<>]+", lambda m: "[source](" + m[0].rstrip(".,") + ")" + m[0][len(m[0].rstrip(".,")):], text)
    text = re.sub(r";[ \t]*(?=\n|$)", ".", text)
    text = text.replace(") .", ").").replace(") ,", "),")
    return text.strip()

fr = read("research_frobenius.md")
cm = read("research_cm_addendum.md")
tn = read("research_tannaka.md")
ar = read("research_artin_addendum.md")
lf = read("research_lefschetz.md")
rt = read("research_root.md")
st = read("research_standing.md")

chunks = [read("research_synthesis.md").strip()]
all_ids = []
groups = [
    ("Frobenius, norms, CM fields, and finite-field realization", fr, "FR"),
    ("Valuation descent and the maximal CM quotient", cm, "CM"),
    ("Real fibre functors, polarizations, gerbes, and motivic quotients", tn, "T"),
    (None, ar, "T"),
    ("Lefschetz correspondences, tensor groups, and standard-conjecture lettering", lf, "L"),
    ("Reused texts, source identifications, and further comparison", rt, "R"),
]
for title, text, prefix in groups:
    body, ids = items(text, prefix)
    assert ids, (title, prefix)
    all_ids.extend(ids)
    if title:
        chunks.append("## " + title)
    chunks.append(body)

chunks.append(between(st, "# Standing registers"))
chunks.append("## Supporting calculations")
chunks.append("The calculations below establish the maps used in the short notes. They preserve the source's readings and record all convention changes in the research discussion.")
proofs = "## Proof A" + between(lf, "## Proof A", "## Primary references actually consulted")
proofs = re.sub(r"The requested table row can therefore be stated as:\n.*?(?=For RESULTS_STATE)", "", proofs, flags=re.S)
chunks.append(proofs)
chunks.append("## Proof E — Rational Artin correspondences and the arithmetic quotient\n\n" +
              between(ar, "## Supporting construction", "## Primary comparison and source-status note"))

s15 = between(tn, "## Suggested S15 summary", "## Primary references inspected")
chunks.append("## S15: verified modern results and the remaining comparison maps\n\n" + s15)
chunks.append(
    "The quoted Nori–Ayoub, pure-Nori/André and arithmetic-descent results use their stated "
    "characteristic-zero and coefficient setups, without a standard-conjecture assumption. "
    "For the manuscript's category, the concrete remaining maps are the cycle quotient "
    r"\(A_{\mathrm{hom}}\to A_{\mathrm{num}}\), the inclusion \(A_{\mathrm{hom}}\hookrightarrow A_{\mathrm{mot}}\), "
    "and the Artin comparison triangle of Proof E; the notes do not declare their unproved "
    "faithfulness, surjectivity, or essential-image identifications. "
    "The finite-field gerbe and its real obstruction retain the precise additional data in T01–T17."
)

chunks.append("## Context searches and evidence limits")
chunks.append("### Lefschetz and correspondence searches\n\n" +
              between(lf, "## Evidence and search scope", "### Requested questions: findings at this evidence level"))
chunks.append("### Tannakian and period searches\n\n" +
              between(tn, "## Context search record", "## Candidate notes"))
chunks.append("### Frobenius and CM searches\n\n" +
              between(fr, "## Context-search ledger and source limits", "## Verified primary references"))
cm_context = between(cm, "## Context search and primary verification", "**[ANT]**")
chunks.append(cm_context)
chunks.append(
    "The root research searches are recorded per item in records/research_context_search.json "
    "with their generating script. The current-source questions were also checked against "
    "the full frozen batch for question marks, deferred proofs, conjectures, corrections and "
    "title/page-count witnesses. These searches supplement the complete visual reading; "
    "they do not supply readings for the transcription."
)
chunks.append(between(lf, "## Remaining evidence limits"))

chunks.append("## Primary references and verification scope")
chunks.append("These references were used after the transcription freeze. Page numbers below are printed page numbers unless a PDF index is explicitly given. They support the research comparisons and never replace the manuscript witness.")
chunks.append("### Correspondences and standard conjectures\n\n" +
              clean_bibliography(between(lf, "1. **Jannsen", "## Remaining evidence limits").join(["- **Jannsen", ""])))
chunks.append("### Fibre functors, Nori, Ayoub, and periods\n\n" +
              clean_bibliography(between(tn, "1. **CG2017", "## Source for root's separate bridge research").join(["- **CG2017", ""])))
chunks.append(
    "The Artin comparison additionally uses Deligne–Milne, Proposition 6.17 and Remark 6.19, p.61; "
    "Proof E supplies its orbit-matrix and averaging calculations explicitly. "
    "The Giraud reference in T18b is checked as a citation in Deligne–Milne Proposition 5.8, p.50."
)
chunks.append("### Frobenius, abelian varieties, and local arithmetic\n\n" +
              clean_bibliography(between(fr, "## Verified primary references").split("Web retrieval references", 1)[0]))
chunks.append(clean_bibliography("- **[ANT]** " + between(cm, "**[ANT]**").split("Retrieval references", 1)[0]))
chunks.append("### Reused sheets and the spectral anabelian comparison\n\n" +
              clean_bibliography(between(rt, "## Root bibliography / verification scope")))

out = "\n\n".join(x.strip() for x in chunks if x.strip()) + "\n"
out = out.replace("research_frobenius.md, FR14", "FR14 above")
out = out.replace("MPL_15_087-138_work/pages/", "pages/")
assert len(all_ids) == len(set(all_ids)), "Duplicate research note identifiers"
assert not re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", out), "Unexpected control character"
assert "Research in progress" not in out
assert not re.search(r"\bturn\d+(?:view|search)\d+", out), "Internal retrieval reference leaked into main notes"
target = ROOT / "MPL_15_087-138_notes.md"
target.write_text(out, encoding="utf-8")
report = {
    "research_note_ids": all_ids,
    "research_note_count": len(all_ids),
    "standing_unverified_ids": re.findall(r"(?m)^\| (U\d+) \|", out),
    "title_count_ids": re.findall(r"(?m)^### (P\d+) —", out),
    "word_count": len(out.split()),
    "bytes": len(out.encode("utf-8")),
    "sources": [name for name in (
        "research_synthesis.md", "research_frobenius.md", "research_cm_addendum.md",
        "research_tannaka.md", "research_artin_addendum.md", "research_lefschetz.md",
        "research_root.md", "research_standing.md")],
}
(REC / "notes_assembly_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print({key: report[key] for key in ("research_note_count", "word_count", "bytes")})
