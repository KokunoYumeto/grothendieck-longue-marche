"""Repair five stale narrative/inventory fields after completed blind audits.

This script is idempotent. It reads the completed adjudications as authority and
writes only the three reviewed JSON files. It does not rebuild generated files.
"""

import copy
import json
from pathlib import Path


WORK = Path(__file__).resolve().parents[1]


def field(document, path):
    for key in path:
        document = document[key]
    return document


def replace_field(document, path, old, new):
    current = field(document, path)
    if current == new:
        return False
    if current != old:
        raise ValueError(f"Unexpected current value at {path!r}; no files written")
    parent = field(document, path[:-1])
    parent[path[-1]] = new
    return True


def changed_paths(before, after, prefix=()):
    if type(before) is not type(after):
        return [prefix]
    if isinstance(before, dict):
        if before.keys() != after.keys():
            return [prefix]
        return [p for key in before
                for p in changed_paths(before[key], after[key], prefix + (key,))]
    if isinstance(before, list):
        if len(before) != len(after):
            return [prefix]
        return [p for i, value in enumerate(before)
                for p in changed_paths(value, after[i], prefix + (i,))]
    return [] if before == after else [prefix]


REPAIRS = {
    57: [(
        ("root_review_notes",),
        "Main reader inspected the whole scan and all sixteen crops. The cancelled head adjective is changed to doubtful prédéfini (alternative particulier), with the strike and uncertainty preserved. Both readers agree no clear g-descender supports privilégié. The live un before iso, separate marginal cancellation, inserted MD- prefixes, and exact exclamation marks are accepted. Other unresolved readings remain for blind audit. Blind audit: all thirteen differing boxes personally viewed. The adjective and comma are updated; unresolved letter shapes, insertions and decorations remain explicitly qualified.",
        "Main reader inspected the whole scan and all sixteen crops. The completed blind audit reads the cancelled head adjective as doubtful pondérés|pondéré, superseding the first-stage prédéfini|particulier; the strike and uncertainty remain. The crossed déterminée|déterminé ending and par le also remain doubtful. The live un before iso, separate marginal cancellation, inserted MD- prefixes, and exact exclamation marks are accepted. All thirteen differing boxes were personally viewed. The independent second reading and root adjudication are complete; the updated head reading and comma after 4 ou 1 are reflected in the current page, while unresolved letter shapes, insertions and decorations remain explicitly qualified. The frozen first-stage records are unchanged.",
    )],
    58: [(
        ("notes", 3),
        "Both live displays carry (72); the author’s repeated numbering is retained. The cancelled leading label also appears more like (72) than (71), but remains uncertain. The abandoned d’ordre sign is not forced to fit a genus or weight argument: its proposed first reading is <, with 2 and ≤ remaining alternatives.",
        "Both live displays carry (72); the author’s repeated numbering is retained. The cancelled leading label also appears more like (72) than (71), but remains uncertain. The completed blind audit finds no independent mathematical sign after d’ordre: the terminal chevron belongs to the cancellation stroke, and the deleted text ends with d’ordre. The first-stage < / 2 / ≤ candidates are superseded and survive only in the frozen first-stage records.",
    ), (
        ("inventory", 10, "first_words_or_objects"),
        "Dans le cas gα0=0 tous les sommets sauf 1 sont d’ordre < / 2 / ≤",
        "Dans le cas gα0=0 tous les sommets sauf 1 sont d’ordre; the terminal chevron belongs to the cancellation stroke, with no independent mathematical sign",
    )],
    61: [(
        ("root_review_notes",),
        "The full scan and all 13 crops were reviewed. Crop03 disproves the initial full-image impression of a missing second hat: both angular hats are separate from the letters. The connector leaves des live; the inserted se partageant has no separate trailing comma. The table brace, crossing arrow, capital Codim headers and restricted underline under et were checked. Double-struck P/Z are retained; Cas de/des remains uncertain. M1034 is resolved from its crop. Check-event references were aligned to the actual mathematical notes. The independent second reading is still pending. All thirteen differing second-reading boxes and the focused B08 crop personally viewed; two certainty changes retained in the audit history.",
        "The full scan and all 13 crops were reviewed. Crop03 disproves the initial full-image impression of a missing second hat: both angular hats are separate from the letters. The connector leaves des live; the inserted se partageant|se partage remains uncertain and has no separate trailing comma. The table brace, crossing arrow, capital Codim headers and restricted underline under et were checked. Double-struck P/Z are retained; Cas de/des remains uncertain. The completed blind audit supersedes the first-stage resolution of M1034: its decision is undecided, with se partageant preferred and se partage retained as an alternative. Maxima|maxim. also remains explicitly uncertain. Check-event references were aligned to the actual mathematical notes. The independent second reading and root adjudication are complete. All thirteen differing second-reading boxes and the focused B08 crop were personally viewed; the two certainty changes are retained in the audit history, and the frozen first-stage records are unchanged.",
    ), (
        ("witness_comparison",),
        "C is substantially stronger on the author’s short forms and wording: quelc., chacun, maxima, sûr aux and on aura. H correctly leaves des live and uses the double-struck alphabet in (77). Both supplied array layouts place the arrow on the wrong side of the divider; the ink shows it crossing. C preserves the real left brace that H omits. The inserted se partageant can be resolved to C’s first reading, while the Cas de/des disagreement remains open. H’s broad heading emphasis overstates the visible underline extent.",
        "C is substantially stronger on the author’s short forms and wording: quelc., chacun, sûr aux and on aura. Maxima remains the preferred reading but is explicitly uncertain against maxim. H correctly leaves des live and uses the double-struck alphabet in (77). Both supplied array layouts place the arrow on the wrong side of the divider; the ink shows it crossing. C preserves the real left brace that H omits. The completed blind audit leaves the insertion undecided as se partageant|se partage, superseding the first-stage resolution to C’s reading; Cas de/des also remains open. H’s broad heading emphasis overstates the visible underline extent.",
    )],
}


def main():
    expected_readings = {
        57: {"B01": ("pondérés|pondéré", "déterminée|déterminé")},
        58: {"B13": ("sont d'ordre}",)},
        61: {"B08": ("se partageant|se partage",), "B11": ("maxima|maxim.",)},
    }
    pending = []
    for scan, repairs in REPAIRS.items():
        authority_path = WORK / "second" / f"147_scan{scan:03}_adjudications.json"
        authority = {item["box"]: item for item in json.loads(authority_path.read_text())}
        for box, required in expected_readings[scan].items():
            decision = authority[box]
            assert decision["changed"] and decision["root_viewed"], (scan, box)
            assert all(value in decision["final"] for value in required), (scan, box)
        if scan == 58:
            assert "There is no independent numeral2 or less-than relation" in authority["B13"]["evidence"]

        path = WORK / "reviewed" / f"147_scan{scan:03}.json"
        original = json.loads(path.read_text())
        assert original["audit_complete"] is True, scan
        if scan == 58:
            assert original["inventory"][10]["element"] == "11"
        if scan == 61:
            mark = next(item for item in original["decisions"] if item["id"] == "M1034")
            assert mark["decision"] == "undecided"
            assert "se partageant|se partage" in mark["reading"]

        updated = copy.deepcopy(original)
        for key_path, old, new in repairs:
            replace_field(updated, key_path, old, new)
        actual = set(changed_paths(original, updated))
        allowed = {entry[0] for entry in repairs}
        assert actual <= allowed, (scan, actual - allowed)
        pending.append((path, updated, actual))

    # Validate every target before writing any file.
    for path, updated, actual in pending:
        if actual:
            path.write_text(json.dumps(updated, ensure_ascii=False, indent=2) + "\n")
            for key_path in sorted(actual, key=str):
                print(f"{path}: {key_path}")
        else:
            print(f"{path}: already repaired")


if __name__ == "__main__":
    main()
