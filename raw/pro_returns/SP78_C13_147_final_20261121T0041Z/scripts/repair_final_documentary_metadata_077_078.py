#!/usr/bin/env python3
"""Synchronize authorized 077–078 metadata with completed root adjudications.

Uses the guarded, idempotent file helpers from the preceding documentary repair.
No page, frozen reading, adjudication, classification/count, global NCR status or
historical hash is changed. Root's B02 finding supplies the local 077 index scope.
"""
import json

from repair_final_documentary_metadata import (
    LEGIBILITY_ADDITION,
    WRITTEN,
    patch_json,
    patch_text,
    replacement,
)


def only(items, key, value):
    found = [item for item in items if item.get(key) == value]
    if len(found) != 1:
        raise RuntimeError(f"Expected one {key}={value!r}, found {len(found)}")
    return found[0]


def repair_077(record):
    doubt = only(record["doubts"], "place", "Canceled par, absent from MARKS.tsv")
    doubt["reading"] = replacement(
        doubt["reading"], r"\deleted{de \unsure{par}}",
        r"\deleted{\unsure{de} \unsure{par}}", "077 canceled-span doubt")

    inventory = only(record["inventory"], "element", "09")
    inventory["first_words_or_objects"] = replacement(
        inventory["first_words_or_objects"],
        "de, crossed by a long horizontal pen stroke",
        "Doubtful de, crossed by a long horizontal pen stroke; its low ending is obscured.",
        "077 inventory 09")
    inventory = only(record["inventory"], "element", "11")
    inventory["position"] = replacement(
        inventory["position"], "above canceled de",
        "Raised row above the separate canceled de and par clusters",
        "077 inventory 11 position")
    inventory["first_words_or_objects"] = replacement(
        inventory["first_words_or_objects"],
        "dans; une follows on the baseline of structure d’extension",
        "dans une; both words belong to the insertion before structure d’extension",
        "077 inventory 11 insertion extent")

    hand = only(record["hand_log"], "habit",
        "A compact French ending under retracing must not be recovered from expected syntax alone.")
    hand["all_occurrences"] = replacement(
        hand["all_occurrences"],
        "Applied specifically to s’insère, canceled par and quotient, each retained with uncertainty; composée was distinguished by its acute and lack of a separate i dot.",
        "Applied specifically to s’insère, canceled de and par, and quotient, each retained with uncertainty; composée was distinguished by its acute and lack of a separate i dot.",
        "077 hand-log scope")
    record["root_review_notes"] = replacement(
        record["root_review_notes"], "only sorte de inserted;",
        "only sorte de inserted in the later variance sentence;",
        "077 root-review insertion scope")

    notation = only(record["notation"], "sign", r"\widehat I_\alpha")
    notation["scope"] = replacement(
        notation["scope"], "(95) only",
        "(95), the I index of the M factor only. The upper Teichmüller factor has bare I, and the lower factor has bare nu.",
        "077 M-factor I scope")
    notation["evidence"] = replacement(
        notation["evidence"],
        "The roof is detached above a capital with top/bottom bars and a dark central stem. No former glyph separates from the dark body.",
        "The roof is detached above a capital with top/bottom bars and a dark central stem. No former glyph separates from the dark body. Root’s B02 review found no detached roof over either Teichmüller index; these local absences are preserved alongside the hatted I of the M factor.",
        "077 B02 local index evidence")
    inventory = only(record["inventory"], "element", "02")
    inventory["first_words_or_objects"] = replacement(
        inventory["first_words_or_objects"], "lower alpha indices, hat on I",
        "lower alpha indices, hat on the M-factor I only; bare I and nu in the two Teichmüller products",
        "077 display inventory index scope")


def repair_078(record):
    inventory = only(record["inventory"], "element", "12")
    inventory["position"] = replacement(
        inventory["position"], "After doubtful flèche",
        "After the doubtful la flèche/l’hom. group", "078 inventory noun label")
    change = only(record["changes"], "id", "078-13")
    change["place"] = replacement(
        change["place"], "Canceled adjective after flèche",
        "Canceled adjective after the doubtful article/noun group",
        "078-13 place label")


def repair_concordance(text):
    pairs = [
        ("- Definite Gamma bangs: **057:8–9,059:5–7,070:26,28–29,071:12,078:24–25,31,36,38**. Bare Gamma remains separately. No `\\Gamma'` occurs.",
         "- Definite Gamma bangs: **057:8–9,059:5–7,070:26,28–29,071:12,078:24–25,31,36**. Bare Gamma remains separately. No `\\Gamma'` occurs."),
        (r"078:38     \Gamma^!_{\underline G,G'}",
         r"078:38     \Gamma^{\unsure{!}}_{\underline G,G'}"),
        ("- **077:10** retains the three-way exponent/state doubt; all three 077 Teichmüller capitals are script T with their local plus/bang-plus exponents.",
         "- **077:10** retains the three-way exponent/state doubt; all three 077 Teichmüller capitals are script T with their local plus/bang-plus exponents.\n- **078:38** retains a qualified bang in the third margin. The retraced raised mark does not separate a clean stem and detached dot. The first G underline and the absence of the second underline remain separately established."),
        ("| `autom` | 072:8, 078:25 |",
         "| `autom` | 072:8, 078:25 |\n| `hom.` | 078:25, candidate within `\\unsure{la flèche\\|l'hom.}` |"),
    ]
    for old, new in pairs:
        text = replacement(text, old, new, "077–078 concordance: " + old[:65])
    return text


NOTATION_ROWS = r"""| Local index accents in (95) | Hatted I in the M factor; bare I and nu in the Teichmüller products | 077 B02: the M-factor I has a distinct two-arm roof; no detached roof appears over either T-factor index. Preserve the contrast with the hatted nu indices in072. |
| Whole article/noun uncertainty | `\unsure{la flèche\|l'hom.}` | 078: marginal strokes overlap the entire group. The detached upper mark may be an accent or an apostrophe, so the article is not separately certified. |
| Retraced raised Gamma mark | `\Gamma^{\unsure{!}}_{\underline G,G'}` | 078 third margin: the raised mark remains doubtful because its stem and dot are not separately clear. The local index underlines are recorded independently. |
| Extent of a raised insertion | `\inserted{dans une}` | 077: both words lie above the separately canceled, doubtful de and par. In the later variance sentence, only sorte de belongs to the insertion. |"""


def repair_notation(text):
    if NOTATION_ROWS in text:
        return text
    anchor = "\nThe faint pencil foliation near the lower edge"
    if text.count(anchor) != 1:
        raise RuntimeError("Notation closing paragraph is not unique")
    return text.replace(anchor, NOTATION_ROWS + "\n" + anchor, 1)


FEEDBACK_ADDITION = "- Scans 077–078: insertion and uncertainty can extend across more than one word. On077 both dans and une belong to the raised addition, while the canceled de and par remain qualified. On078 the article and noun form one unresolved la flèche/l’hom. group; the overlapping strokes do not support a separately certain article. The retraced Gamma exponent in the third margin remains qualified despite clearer bangs elsewhere."


def repair_feedback(text):
    if FEEDBACK_ADDITION in text:
        return text
    anchor = "These are concrete recurring subpatterns, not additional mutually exclusive counting categories."
    if text.count(anchor) != 1:
        raise RuntimeError("Feedback category paragraph is not unique")
    return text.replace(anchor, FEEDBACK_ADDITION + "\n\n" + anchor, 1)


def repair_legibility(text):
    if "The blind-audit findings on066 and071–079" in text:
        return text
    expanded = LEGIBILITY_ADDITION.replace("on066 and071–076", "on066 and071–078")
    expanded += " On077 the audit extends the raised insertion to dans une and qualifies the canceled de. On078 the full la flèche/l’hom. group and the retraced third-margin Gamma exponent remain unresolved."
    return replacement(text, LEGIBILITY_ADDITION, expanded, "077–078 legibility findings")


def main():
    patch_json(77, ["doubts", "inventory", "hand_log", "root_review_notes", "notation"], repair_077)
    patch_json(78, ["inventory", "changes"], repair_078)
    patch_text("workflow/notation_concordance.md", repair_concordance)
    patch_text("notation.md", repair_notation)
    patch_text("feedback_extra.md", repair_feedback)
    patch_text("legibility.txt", repair_legibility)
    print(json.dumps({"updated": WRITTEN, "count": len(WRITTEN)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
