"""Record targeted supplied-context searches for extension research items.

This only reads supplied context and writes the research search log.
It never reads images, OCR, or any transcription output.
"""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
CONTEXT = ROOT / "context"
FILES = [
    CONTEXT / "README.md",
    CONTEXT / "notes/RESULTS_STATE.md",
    CONTEXT / "LM2_CONGRUENCE_ROWS.md",
    CONTEXT / "same_cote_84/MPL_84_146-193_notes.md",
]
DEST = ROOT / "MPL_84_097-145/research/extension_context_searches.md"
ROWS = [
    ("B01", ["E170.3"], r"compatib|complement|complément", "Later complementary identities are a conditional comparison lead, not a reading correction."),
    ("B02", ["E170.3"], r"exactness|exactitude|monomorph|epimorph", "The new proof uses exactness and the cited identities; it does not assume cancellation of chi."),
    ("B03", ["E170.2", "R11"], r"functor|fonctor|groupoid", "Separate the asserted general homomorphisms from the declared local groupoid."),
    ("B04", ["E148.1", "E170.5"], r"gamma|gamma|comparison|comparaison", "The earlier square has the same scalar-conditioned comparison issue."),
    ("B05", ["E170.4", "E170.5"], r"endpoint|translation|arrow matrix|T_", "The literal surviving minus is checked as an endomorphism; endpoint conventions matter."),
    ("B06", ["E146.1", "E170.5"], r"complement|swapp|coefficient|splitting", "Later coordinate choices do not decide the two uses of the earlier tilde coefficient."),
    ("B07", ["E148.1", "E156.1", "E164.3", "R11"], r"gamma|delta|all.*chi|all.*χ", "A conditional comparison and an all-chi local product have distinct scopes."),
    ("B08", ["E154.2", "R13"], r"annihilator|automorphism|canonic", "The new modulo-four gamma example instantiates an existing annihilator issue."),
    ("B09", ["E146.3"], r"coordinate|increment|residu|χ.*u", "A later coordinate identity motivates the factor check without changing scan 130."),
    ("B10", ["E146.1", "E170.5"], r"sign|signe|splitting.change", "The earlier positive and negative conventions must be distinguished."),
    ("B11", ["E170.5", "R11"], r"cocycle|composition|associativ", "Only the new mixed-sign residual is recomputed; full model laws are not re-proved."),
    ("B12", ["E146.1", "E170.5"], r"successive|increment|splitting.change", "Context gives a convention for the three proposed reading questions, not a new transcription."),
    ("B13", ["E160.2", "E160.3", "E170.4"], r"dual|trace|endpoint|minus", "The local minus on the special dual's endpoint is not a universal sign reconciliation."),
    ("B14", ["E148.3", "E160.1", "E160.2", "E160.3"], r"Hom|prime|primed|shifted|faithful|trace", "Special Hom, scalar restriction, three primes, and later shifted pi need separate definitions."),
    ("B15", ["E160.3", "E170.5"], r"sign|dual|quotient|vector", "Map inputs and vector inputs differ; the source sign warning remains scoped."),
    ("B16", ["E156.2", "E166.3"], r"mixed|compatib|check|automatic", "The source's single mixed-input check is discharged, not all descent conditions."),
    ("B17", ["E164.1", "R13"], r"division|divisib|annihilator|zero.divisor", "The undivided identity is weaker than dividing by chi."),
    ("B18", ["E146.1", "E152.1"], r"cancel|withdraw|normaliz|scind", "Cancelled normalization is not reinstated."),
    ("B19", ["E152.1"], r"normaliz|o.K|2.*χ|2.*chi", "The later differently written scalar correction is only a comparison lead."),
    ("B20", ["E166.1", "E166.2", "E166.3", "E168.1"], r"F.?11|strict|block|carr", "Conditional strict-extension comparison depends on constructing the remaining block."),
    ("B21", ["E156.2", "E164.3"], r"candidate|delta|gamma|coefficient", "Identify the earlier tuple only conditionally on the primed-operator convention."),
    ("B22", ["E150.2", "E160.3"], r"involution|eig|sigma|trace", "The new converse uses exact factorization, without division by two."),
    ("B23", ["E170.1", "E170.2", "R11"], r"morphism|functor|compatib|preserv", "The broad endomorphism proposal needs splitting compatibility."),
    ("B24", ["R11"], r"morphism|relation|counterexample|shear", "A new shear counterexample tests the broader earlier hypothesis, not R11's declared morphisms."),
    ("B25", ["E158.1", "E158.2"], r"faithful|coefficient|annihilat|scalar", "The last map equality cannot be obtained by unjustified scalar cancellation."),
    ("B26", ["E170.2", "E170.3", "E170.4", "E170.5", "R10", "R11", "R12", "R13"], r"T.?0|V.*chi|V.*χ|coherence|invertib|unit", "Separate product, invertibility, global coherence, and fixed-endpoint comparison in Hua's register."),
]


def rg(pattern, paths):
    proc = subprocess.run(
        ["rg", "-n", "-i", "--with-filename", "--no-heading", "-e", pattern, *map(str, paths)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode not in (0, 1):
        raise RuntimeError(proc.stderr)
    return proc.stdout.splitlines()


def short(line, limit=350):
    line = line.replace(str(ROOT) + "/", "")
    return line if len(line) <= limit else line[:limit] + " …"


out = [
    "# Per-item supplied-context searches: extension block",
    "",
    "These searches were executed after the transcription freeze. The context "
    "README and RESULTS_STATE were read first; the matched sections of the supplied "
    "same-cote notes were then read as unreviewed leads. No image, OCR, external "
    "transcription, or Library content was accessed in this research task.",
    "",
    "Search corpus: context/README.md; context/notes/RESULTS_STATE.md; "
    "context/LM2_CONGRUENCE_ROWS.md; context/same_cote_84/MPL_84_146-193_notes.md.",
    "",
    "Citations in extension_notes.md use the same-cote item labels shown below. "
    "An item-heading search retrieves the precise cited leads, and a separate "
    "case-insensitive lexical search checks related terminology across the four "
    "files. For compactness, lexical hits below show at most two lines per file; "
    "reported counts include every match. A hit is not a verified theorem and "
    "a missing keyword is not proof of mathematical absence.",
    "",
    "Direct register search: rg -n -i -e 84-chi-trivialised-extension-product "
    "context/notes/RESULTS_STATE.md",
    "",
]
register = rg("84-chi-trivialised-extension-product", [FILES[1]])
out += ["> " + short(line, 1200) for line in register]
out += [
    "",
    "The direct related ID is Hua, findings register, "
    "84-chi-trivialised-extension-product (conjectural candidate; statement-level "
    "intake). No LM2 identification is inferred from shared symbols such as "
    "trace, norm, or a two-by-two matrix.",
    "",
]

counts = []
for item, refs, terms, conclusion in ROWS:
    pattern = r"^### (" + "|".join(re.escape(ref) for ref in refs) + r")\b"
    anchors = rg(pattern, [FILES[3]])
    if len(anchors) != len(refs):
        raise RuntimeError(f"{item}: requested {refs}, found {len(anchors)} headings")
    hits = rg(terms, FILES)
    shown = []
    per_file = {}
    for line in hits:
        filename = line.split(":", 1)[0]
        per_file[filename] = per_file.get(filename, 0) + 1
        if per_file[filename] <= 2:
            shown.append(line)
    out += [
        f"## {item}",
        "",
        f"**Item-locator query:** {pattern}",
        "",
        *["- " + short(line) for line in anchors],
        "",
        f"**Lexical query:** {terms}",
        "",
        f"**Matches:** {len(hits)} total across {len(per_file)} files "
        "(up to two per file shown).",
        "",
        *["- " + short(line) for line in shown],
        "",
        f"**Disposition:** {conclusion}",
        "",
    ]
    counts.append((item, len(anchors), len(hits)))

# Locate and record the explicitly cited calculation sections as well.
sections = rg(r"^##.*10\.[23]|^###.*10\.[23]", [FILES[3]])
out += [
    "## Shared detailed calculation sections",
    "",
    "These sections were read for B05/B09/B10/B11 as comparisons of "
    "coordinate conventions; their model conclusions were not silently imported "
    "into the frozen handwriting.",
    "",
    *["- " + short(line) for line in sections],
    "",
]
DEST.write_text("\n".join(out), encoding="utf-8")
print(f"Wrote {DEST.relative_to(ROOT)}")
for item, anchor_count, hit_count in counts:
    print(f"{item}: {anchor_count} cited headings; {hit_count} lexical hits")
