#!/usr/bin/env python3
"""Apply authorized documentary repairs after the blind audits.

This script changes only the listed reviewed-record fields and shared prose.
It does not adjudicate ink, edit page text or frozen readings, resolve NCR-01–03,
or replace the historical cross-page review hashes. Every file is read directly
before its targeted change; a concurrent-change guard precedes each atomic write.
The replacements are idempotent and fail closed if their expected context changes.
"""
from pathlib import Path
import json
import os
import tempfile


ROOT = Path(__file__).resolve().parents[1]
WRITTEN = []


def replacement(text, old, new, label):
    if new in text:
        return text
    if old in text:
        if text.count(old) != 1:
            raise RuntimeError(f"Ambiguous replacement: {label}")
        return text.replace(old, new, 1)
    raise RuntimeError(f"Expected context absent: {label}")


def write_guarded(path, before, after, fields):
    if before == after:
        return
    if path.read_bytes() != before:
        raise RuntimeError(f"Concurrent change detected: {path.relative_to(ROOT)}")
    fd, temporary = tempfile.mkstemp(prefix=path.name + ".metadata-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(after)
        if path.read_bytes() != before:
            raise RuntimeError(f"Concurrent change detected: {path.relative_to(ROOT)}")
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    WRITTEN.append({"file": str(path.relative_to(ROOT)), "fields": fields})


def patch_json(scan, allowed_fields, edit):
    path = ROOT / "reviewed" / f"147_scan{scan:03}.json"
    before = path.read_bytes()
    original = json.loads(before)
    revised = json.loads(before)
    edit(revised)
    changed = [key for key in set(original) | set(revised)
               if original.get(key) != revised.get(key)]
    if not set(changed) <= set(allowed_fields):
        raise RuntimeError(f"Unexpected field change on {scan}: {changed}")
    if changed:
        after = (json.dumps(revised, ensure_ascii=False, indent=2) + "\n").encode()
        write_guarded(path, before, after, sorted(changed))


def append_unique(items, value):
    if value not in items:
        items.append(value)


def patch_text(relative, edit):
    path = ROOT / relative
    before = path.read_bytes()
    revised = edit(before.decode())
    write_guarded(path, before, revised.encode(), ["targeted documentary prose"])


def repair_056(record):
    record["notes"][4] = replacement(
        record["notes"][4],
        "with its inherited alternative readings pending parent review.",
        "with its alternative readings retained after main-reader review and the completed blind audit.",
        "056 notes[4] review status")


def repair_060(record):
    record["notes"][5] = replacement(
        record["notes"][5],
        "qui sont replaced by ils sont deux",
        "the canceled qui sont/savoir trial and its replacement, whose short groups remain ils/qui and deux/donc",
        "060 notes[5] qualified replacement")
    record["witness_comparison"] = replacement(
        record["witness_comparison"],
        "C is substantially closer in the central prose (par rapport aux schémas modulaires and ils sont deux), preserves the abbreviation trivialt, the exclamation in the slanted note and more of the cancelled material.",
        "C is substantially closer in the central prose, including par rapport aux schémas modulaires, and preserves the abbreviation trivialt, the exclamation in the slanted note and more of the canceled material. The nearby canceled and replacement words retain the local uncertainties recorded after the blind audit.",
        "060 witness comparison")
    entries = [entry for entry in record["notation"] if entry["sign"] == r"\widehat M^!"]
    if len(entries) != 1:
        raise RuntimeError("060 bang-bearing M notation entry is not unique")
    entry = entries[0]
    entry["scope"] = replacement(
        entry["scope"],
        "All displayed and inline modular-multiplicity symbols on scan 60.",
        "The M factors in numbered displays (74) and (75), and the two new-case factors in the prose below (75). The two NB factors and both inserted M_G formulas are written without bangs in the current transcription.",
        "060 notation scope")
    entry["evidence"] = replacement(
        entry["evidence"],
        "Each M roof is separate from the raised upright and detached dot at its right. Checked throughout both numbered displays and the inline formulas.",
        "The reviewed evidence describes each roof at the bang-bearing occurrences as separate from the raised upright and detached dot at its right. Its scope is restricted here to the factors in (74), (75), and the two inline new-case factors below (75); this metadata repair makes no new source reading.",
        "060 notation evidence scope")


def repair_068(record):
    append_unique(record["unresolved"],
        "The final delimiter after combinatoire remains a closing parenthesis versus square bracket; the preferred parenthesis is explicitly qualified.")


def repair_071(record):
    record["unresolved"][1] = replacement(
        record["unresolved"][1],
        "The inline definition has a definite low point but an uncertain colon as a whole.",
        "The inline J definition remains J-prime followed by colon versus J with a raised exclamation; the detached low point is definite, but its grouping is unresolved.",
        "071 unresolved inline J")


def repair_072(record):
    append_unique(record["unresolved"],
        "Explicite after structure réelle remains the preferred word, but its compressed ending is not independently readable and is explicitly qualified.")


def repair_074(record):
    append_unique(record["unresolved"],
        "The live noun notations remains preferred under uncertainty because its compressed internal letters are not individually separable.")
    append_unique(record["unresolved"],
        "The first canceled comparison between card I-prime and card I-double-prime remains ≥ versus >; the later ≥3 is separately readable.")
    record["notes"][7] = replacement(
        record["notes"][7],
        "No OCR, internet search, other page, TeX compilation or blind second reading was used.",
        "No OCR, internet search or TeX compilation was used. This paragraph records the assigned reader’s first-reading workflow, which did not consult another manuscript page; the completed blind audit is recorded separately.",
        "074 first-reading scope")


def repair_075(record):
    record["notes"][4] = replacement(
        record["notes"][4],
        "Subsequent use of saved crops served the same first-pass decisions. No OCR, research, TeX compilation, or second reading was performed.",
        "The assigned reader’s reuse of saved crops in this paragraph served the same first-pass decisions. No OCR, research or TeX compilation was used. This paragraph records the first-reading workflow; the completed blind audit is recorded separately.",
        "075 first-reading scope")


def repair_076(record):
    record["notes"][0] = replacement(
        record["notes"][0],
        "No OCR, outside research, TeX compilation, or blind second reading was used.",
        "No OCR, outside research or TeX compilation was used. This paragraph records the assigned reader’s first-reading workflow; the completed blind audit is recorded separately.",
        "076 first-reading scope")


def repair_078(record):
    record["notes"][8] = replacement(
        record["notes"][8],
        "Saved crops were reused only within the same first pass. No OCR, research, TeX compilation, or second reading was undertaken.",
        "The assigned reader’s saved-crop reuse described here was confined to the first pass. No OCR, research or TeX compilation was used. This paragraph records only that first-reading workflow; blind-audit records are separate.",
        "078 first-reading scope")


def repair_079(record):
    record["notes"][0] = replacement(
        record["notes"][0],
        "No decided place was recropped. No OCR, outside research, TeX compilation, or blind second reading was used.",
        "The assigned reader did not recrop a decided place during this first reading. No OCR, outside research or TeX compilation was used. This paragraph records only that first-reading workflow; blind-audit records are separate.",
        "079 first-reading scope")


def repair_concordance(text):
    pairs = [
        ("No page, reviewed JSON, frozen reading or generated deliverable was changed.",
         "No page, reviewed JSON, frozen reading or generated deliverable was changed by the initial concordance review. Later documentary repairs refresh the references and local-variant index below from existing page text and audit metadata; they make no new image reading. The original cross-page source checks and historical hashes remain in `workflow/notation_crosspage_review.json`."),
        ("Confirm the NB’s local exponent absence. Separately, `reviewed/147_scan060.json`’s notation scope for `\\widehat M^!` says all displayed/inline modular-multiplicity symbols; that scope is broader than the current text. The metadata has not been edited.",
         "Confirm the NB’s local exponent absence. The formerly overbroad `reviewed/147_scan060.json` scope for `\\widehat M^!` has been narrowed to the current bang-bearing occurrences. That documentary repair does not certify the local source absences; the source check remains pending."),
        ("| `car` | 064:22 |", "| `car` | 064:23 |"),
        ("| `car.` | 064:22 |", "| `car.` | 064:23 |"),
        ("| `pts` | 061:19, 062:21, 064:14, 066:32, 067:2, 068:6, 070:29, 071:2, 071:16, 075:2 |",
         "| `pts` | 061:19, 064:14, 066:32, 067:2, 068:6, 070:29, 071:2, 071:16, 075:2 |"),
        ("| `élts` | 071:2, 075:2 |",
         "| `élts` | 071:2, 075:2 |\n| `elmts` | 066:35, within `\\unsure{elmts\\|elts}` |\n| `elts` | 066:35, alternative to elmts |"),
        ("Additional raised/doubtful forms: **054:7** `isom\\unsure{.}`; **063:14** `resp\\textsuperscript{t}`; **076:7** `\\unsure{canoniq\\textsuperscript{t}}`.",
         "Additional raised/doubtful forms: **054:7** `isom\\unsure{.}`; **062:21** `p\\textsuperscript{ts}`; **063:14** `resp\\textsuperscript{t}`; **076:7** `\\unsure{canoniq\\textsuperscript{t}}`."),
        ("- **071:2,4:** three `\\widetilde A'_0` tokens; no tilde-A bang.",
         "- **071:2,4:** three `\\widetilde A'_0` tokens; no tilde-A bang.\n- **071:2:** the inline `\\unsure{J':|J^!}` retains prime-plus-colon versus raised-bang uncertainty. The detached low point is definite, but clean J primes elsewhere do not resolve its local grouping."),
        ("**065:30** (between zeta 2/zeta 3), **074:82** (between 2/ell)",
         "**065:30** (between zeta 2/zeta 3), **074:25** (first canceled cardinality comparison, `\\geq|>`), **074:82** (between 2/ell)"),
        ("**070:29** retains `z\\longmapsto z^{-1}`;",
         "**065:18** has `\\unsure{\\longrightarrow}`: the recorded blind audit qualifies its rounded endpoint. **070:29** retains `z\\longmapsto z^{-1}`;"),
    ]
    for old, new in pairs:
        text = replacement(text, old, new, "concordance: " + old[:65])
    return text


NOTATION_ROWS = r"""| Continuous sloping marginal formula | `\operatorname{Isom}(\{0,1,\infty\},I'')` | 066: the arguments continue the marginal definition along the same sloping baseline. The complete rotated crop resolves Isom and its tuple; they are not a separate prose insertion. |
| Local raised J mark | `\unsure{J':\|J^!}` | 071 inline definition: the detached low point may belong to punctuation or to a bang. Clean J primes elsewhere and the three A-prime forms do not resolve this local grouping. |
| Compressed live words | `\unsure{explicite}` on072; `\unsure{notations}` on074; `\unsure{définissent}` on075 | The preferred words remain qualified where their endings or internal letters cannot be separated from the compressed or retraced strokes. |
| Compressed pronoun and clipped word | `\unsure{la\|le}`; `\unsure{action}` | 076: the final vowel before remplacer remains ambiguous; the right scan edge cuts the ending of action. The visible beginning supports the word as a candidate, not a complete certain reading. |
| Crossings in canceled text | Doubtful deux and I-prime on073; first canceled `≥\|>` on074 | Cancellation and neighboring descenders obscure the relevant letter bodies or small strokes. Clear nearby words, primes or relations do not establish the obscured occurrence. |
| Raised restart above cancellation | `\inserted{Or on a}` | 074: the live phrase sits above the canceled a il y a restart and retains its insertion status. |"""


def repair_notation(text):
    anchor = "\nThe faint pencil foliation near the lower edge"
    if NOTATION_ROWS in text:
        return text
    if text.count(anchor) != 1:
        raise RuntimeError("Notation closing paragraph is not unique")
    return text.replace(anchor, NOTATION_ROWS + "\n" + anchor, 1)


FEEDBACK_ADDITIONS = r"""- Scan 066: a sloping marginal formula continues into an area that resembles an interlinear prose insertion. The complete rotated crop joins the arguments \((\{0,1,\infty\},I'')\) to Isom. Reading the cropped fragments separately split one formula and encouraged a false primed-pair reading.
- Scans 071–074: familiar repeated forms do not settle a locally obscured mark. The inline J on071 retains prime-plus-colon/bang alternatives; explicite on072 and notations on074 retain word uncertainty; the canceled deux and I-prime on073, and the first canceled ≥/> comparison on074, remain qualified. These certainty refinements are recorded separately from substantive witness corrections.
- Scan 074: the live Or on a is a raised restart above the canceled a il y a. Retaining its insertion status preserves the revision sequence even when a linear reading gives the same words.
- Scans 075–076: compressed endings and clipped text remain qualified even where a familiar phrase is plausible. Définissent on075 has a densely retraced ending; la/le on076 has an ambiguous final vowel, and action loses its ending at the right scan edge. The visible beginnings do not certify the missing or merged letters.
"""


def repair_feedback(text):
    text = replacement(
        text,
        "- Scans 074–075: both drafts supply an expected index in a repetitive chain. The source has no separate ell in the b_{-1} label on074 and repeats c_{i-1} in the upper local chain on075. Other thickened plus/minus strokes remain explicit doubts rather than being repaired by the intended pattern.",
        "- Scans 074–075: expected sequences can supply absent or repeated labels. Scan074 retains the literal b_{-1}, its open vertex and the missing upper weight; scan075 repeats c_{i-1} in the upper local chain. Other thickened plus/minus strokes remain explicit doubts. Neither the intended chain nor its arithmetic supplies missing ink.",
        "feedback chain details")
    anchor = "These are concrete recurring subpatterns, not additional mutually exclusive counting categories."
    if FEEDBACK_ADDITIONS not in text:
        if text.count(anchor) != 1:
            raise RuntimeError("Feedback category paragraph is not unique")
        text = text.replace(anchor, FEEDBACK_ADDITIONS + "\n" + anchor, 1)
    return text


LEGIBILITY_ADDITION = "The blind-audit findings on066 and071–076 distinguish recovered continuity from residual uncertainty. On066 the full sloping context resolves the marginal Isom formula and its arguments. Elsewhere, additional inspection preserves doubt: the raised inline J mark on071, explicite on072, canceled deux and I-prime on073, notations plus the first canceled comparison on074, and définissent on075. On076, la/le remains unresolved and action is a candidate whose ending is cut by the right scan edge. The raised Or on a on074 is retained as an insertion. The chain’s open point, literal b_{-1} and absent upper weight remain separate visible features; mathematical expectations do not fill them in."


def repair_legibility(text):
    anchor = "Witness C usually follows the physical order"
    if "The blind-audit findings on066 and071–" in text:
        return text
    if text.count(anchor) != 1:
        raise RuntimeError("Legibility witness paragraph is not unique")
    return text.replace(anchor, LEGIBILITY_ADDITION + "\n\n" + anchor, 1)


def main():
    for scan, allowed, edit in [
        (56, ["notes"], repair_056),
        (60, ["notes", "witness_comparison", "notation"], repair_060),
        (68, ["unresolved"], repair_068),
        (71, ["unresolved"], repair_071),
        (72, ["unresolved"], repair_072),
        (74, ["notes", "unresolved"], repair_074),
        (75, ["notes"], repair_075),
        (76, ["notes"], repair_076),
        (78, ["notes"], repair_078),
        (79, ["notes"], repair_079),
    ]:
        patch_json(scan, allowed, edit)
    patch_text("workflow/notation_concordance.md", repair_concordance)
    patch_text("notation.md", repair_notation)
    patch_text("feedback_extra.md", repair_feedback)
    patch_text("legibility.txt", repair_legibility)
    print(json.dumps({"updated": WRITTEN, "count": len(WRITTEN)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
