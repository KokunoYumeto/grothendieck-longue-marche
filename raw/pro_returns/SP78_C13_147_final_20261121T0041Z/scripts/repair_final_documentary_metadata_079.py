#!/usr/bin/env python3
"""Carry finalized 079 audit findings into documentary descriptions.

Only current descriptive metadata/shared prose is repaired. Page text, decisions,
adjudications, frozen readings, audit fields, classification/count fields, global
NCR status, historical hashes and the pending-source-check section are untouched.
The imported helpers read files immediately before guarded atomic writes.
"""
import json

from repair_final_documentary_metadata import (
    ROOT,
    WRITTEN,
    patch_json,
    patch_text,
    replacement,
)


def require_completed_audits():
    expected = [54, *range(56, 69), *range(70, 80)]
    records = [json.loads(path.read_bytes())
               for path in sorted((ROOT / "reviewed").glob("*.json"))]
    if sorted(record["scan"] for record in records) != expected:
        raise RuntimeError("Reviewed records do not match the 24 supplied scans")
    incomplete = [record["scan"] for record in records if record.get("audit_complete") is not True]
    if incomplete:
        raise RuntimeError(f"Cannot certify final audit scope: {incomplete}")


def repair_079(record):
    record["notes"][1] = replacement(
        record["notes"][1],
        "The slanted replacement is read as part of this definition before the live Ils sont donc sentence.",
        "The slanted replacement is read as part of this definition before the live sentence beginning with the qualified prefix Ils sont donc.",
        "079 notes[1] qualified live prefix")
    entries = [entry for entry in record["notation"]
               if entry["sign"] in ("Retraced raised star", "Retraced raised star/left-arrow signs")]
    if len(entries) != 1:
        raise RuntimeError("079 raised-sign notation entry is not unique")
    entries[0]["sign"] = replacement(
        entries[0]["sign"], "Retraced raised star", "Retraced raised star/left-arrow signs",
        "079 neutral raised-sign label")


def repair_concordance(text):
    pending_start = text.index("## Pending source checks")
    pending_end = text.index("## Alphabets", pending_start)
    pending_before = text[pending_start:pending_end]
    pairs = [
        ("Later documentary repairs refresh the references and local-variant index below from existing page text and audit metadata; they make no new image reading.",
         "Later documentary repairs refresh the references and local-variant index below from existing page text and audit metadata; they make no new image reading. The current reviewed records mark the independent box-reading audits complete for all 24 supplied pages."),
        ("Both M bodies in **079:6**, display (100), are bare; only the first star is doubtful.",
         "Both M bodies in **079:6**, display (100), are bare; each raised sign remains `\\unsure{*|\\leftarrow}`. The star/left-arrow alternatives do not supply a roof over either M."),
        ("Opening starred pair, canceled roof state, large canceled formulas, and inserted independent hat with uncertain G bar",
         "Opening starred pair, canceled roof state, whole crossed l’infini/l’âme and de la réunion/sur le germe alternatives, canceled formulas, and inserted independent hat with uncertain G bar"),
        ("Local bare G-prime, prose asterisk, canceled Pi, and both bare M bodies in (100) with first star doubtful",
         "Qualified Ils sont donc prefix, local bare G-prime, prose asterisk, canceled Pi, and both bare M bodies in (100) with both raised signs star/left-arrow uncertain"),
        ("`resp.`, rightward limit, repeated ou, `revêtts`, and the written `[5], n°5, p. 768'` reference",
         "`resp.`, rightward limit, repeated ou, `revêtts`, visible `multi-plicités` hyphen, and the written `[5], n°5, p. 768'` reference"),
        ("This written repetition is already documented and is not collapsed.",
         "This written repetition is already documented and is not collapsed. The same line retains `multi-plicités`: the blind audit identifies a separate hyphen after multi at the physical line end."),
    ]
    for old, new in pairs:
        text = replacement(text, old, new, "079 concordance: " + old[:65])
    pending_start = text.index("## Pending source checks")
    pending_end = text.index("## Alphabets", pending_start)
    if text[pending_start:pending_end] != pending_before:
        raise RuntimeError("Pending source-check section changed unexpectedly")
    return text


NOTATION_ROWS = r"""| Whole crossed word groups | `\unsure{l'infini\|l'âme}`; `\unsure{de la réunion\|sur le germe}` | 079 canceled main trial: the crossing strokes prevent isolating a certain quoted word or certain short words before the central noun. Both groups remain under whole-group uncertainty. |
| Qualified live sentence prefix | `\unsure{Ils sont donc}` | 079: the prefix is live, but its compact internal letters are not all independently readable. The following des and filter wording remain separate from this doubt. |
| Visible word-division hyphen | `multi-plicités` | 079 definition paragraph: a separate short hyphen follows multi at the physical line end. It is retained without imposing a new line-layout rule. |"""


def repair_notation(text):
    text = replacement(
        text,
        "| Raised star versus a roof over M | Both M bodies bare in079(100), first star doubtful | The overworked mark sits right of M in star position; blank space above the body does not supply a hat. |",
        r"| Raised star/left-arrow alternatives | Both M bodies bare in079(100); both superscripts `\unsure{*\|\leftarrow}` | Each sign sits to the upper right of M and is retraced. Neither sign supplies a roof over its M body. |",
        "079 notation raised signs")
    if NOTATION_ROWS not in text:
        anchor = "\nThe faint pencil foliation near the lower edge"
        if text.count(anchor) != 1:
            raise RuntimeError("Notation closing paragraph is not unique")
        text = text.replace(anchor, NOTATION_ROWS + "\n" + anchor, 1)
    return text


FEEDBACK_ADDITIONS = """- Scan 079: the canceled l’infini/l’âme and de la réunion/sur le germe groups remain whole alternatives, while the live prefix Ils sont donc is separately qualified. A recognizable beginning or a plausible sentence does not make the overlapped internal letters certain.
- Scan 079: both raised signs in (100) retain star/left-arrow alternatives, although the M bodies are independently bare. The clear stars in the opening pair do not resolve these retraced signs. The separate hyphen in multi-plicités is retained at the physical word division.
"""


def repair_feedback(text):
    if FEEDBACK_ADDITIONS in text:
        return text
    anchor = "These are concrete recurring subpatterns, not additional mutually exclusive counting categories."
    if text.count(anchor) != 1:
        raise RuntimeError("Feedback category paragraph is not unique")
    return text.replace(anchor, FEEDBACK_ADDITIONS + "\n" + anchor, 1)


LEGIBILITY_079 = "On079 the canceled l’infini/l’âme and de la réunion/sur le germe groups, the live Ils sont donc prefix, and both star/left-arrow signs in (100) remain qualified. The visible hyphen in multi-plicités is retained."
FINAL_AUDIT_SCOPE = "All 24 supplied pages have completed independent readings of their designated boxes and main-reader adjudication of the differing boxes. The final text retains the unresolved readings recorded in those audits."


def repair_legibility(text):
    text = replacement(
        text, "The blind-audit findings on066 and071–078",
        "The blind-audit findings on066 and071–079", "079 legibility range")
    previous_end = "On078 the full la flèche/l’hom. group and the retraced third-margin Gamma exponent remain unresolved."
    text = replacement(text, previous_end, previous_end + " " + LEGIBILITY_079,
                       "079 legibility findings")
    if FINAL_AUDIT_SCOPE not in text:
        anchor = "Witness C usually follows the physical order"
        if text.count(anchor) != 1:
            raise RuntimeError("Legibility witness paragraph is not unique")
        text = text.replace(anchor, FINAL_AUDIT_SCOPE + "\n\n" + anchor, 1)
    return text


def main():
    require_completed_audits()
    patch_json(79, ["notes", "notation"], repair_079)
    patch_text("workflow/notation_concordance.md", repair_concordance)
    patch_text("notation.md", repair_notation)
    patch_text("feedback_extra.md", repair_feedback)
    patch_text("legibility.txt", repair_legibility)
    print(json.dumps({"updated": WRITTEN, "count": len(WRITTEN), "completed_page_audits": 24},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
