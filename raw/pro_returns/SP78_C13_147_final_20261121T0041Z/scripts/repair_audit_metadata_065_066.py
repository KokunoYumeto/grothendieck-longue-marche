"""Repair nine stale metadata fields after the completed scans065/066 audits.

Idempotent. Writes only the two reviewed JSON files after validating the
completed adjudications. Does not rebuild or modify any generated file.
"""

import copy
import json
from pathlib import Path


WORK = Path(__file__).resolve().parents[1]


def field(document, path):
    for key in path:
        document = document[key]
    return document


def replace_once(document, path, old, new):
    current = field(document, path)
    if new in current and old not in current:
        return
    if current.count(old) != 1:
        raise ValueError(f"Unexpected current value at {path!r}; no files written")
    field(document, path[:-1])[path[-1]] = current.replace(old, new, 1)


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


def main():
    originals = {}
    authorities = {}
    for scan in [65, 66]:
        originals[scan] = json.loads(
            (WORK / "reviewed" / f"147_scan{scan:03}.json").read_text()
        )
        authorities[scan] = {
            item["box"]: item for item in json.loads(
                (WORK / "second" / f"147_scan{scan:03}_adjudications.json").read_text()
            )
        }
        assert originals[scan]["audit_complete"] is True

    required = {
        65: {
            "B07": r"\unsure{\longrightarrow}",
            "B11": r"\deleted{\unsure{4|+}}",
            "B12": r"\deleted{\unsure{\zeta|4}}",
        },
        66: {
            "B03": r"Dans \unsure{de|le}",
            "B06": r"\operatorname{Isom}(\{0,1,\infty\},I'')",
            "B17": r"\unsure{elmts|elts}",
        },
    }
    for scan, boxes in required.items():
        for box, reading in boxes.items():
            decision = authorities[scan][box]
            assert decision["changed"] and decision["root_viewed"], (scan, box)
            assert reading in decision["final"], (scan, box)
    assert "attach it to the marginal formula" in authorities[66]["B03"]["evidence"]
    assert "Its parenthesized arguments continue along the same sloping baseline" in authorities[66]["B06"]["evidence"]

    for index, element in [(6, "07"), (12, "13"), (14, "15")]:
        assert originals[65]["inventory"][index]["element"] == element
    assert originals[66]["doubts"][2]["reading"] == r"\unsure{de|le}"
    changes66 = {item["id"]: i for i, item in enumerate(originals[66]["changes"])}

    repairs = {
        65: [
            (
                ("inventory", 6, "first_words_or_objects"),
                "i_p!:K_!(double-stroked Z_p)→K_!(double-stroked Z).",
                "i_p!:K_!(double-stroked Z_p)→K_!(double-stroked Z), with the probable rightward arrow explicitly uncertain.",
            ),
            (
                ("inventory", 12, "first_words_or_objects"),
                "Tentative canceled plus, obscured by angular overwork",
                "Tentative canceled 4|+, with 4 preferred; the crossed strokes do not settle the character",
            ),
            (
                ("inventory", 14, "first_words_or_objects"),
                "Tentative canceled zeta, under crossing strokes",
                "Tentative canceled zeta|4, under crossing strokes",
            ),
        ],
        66: [
            (
                ("notes", 6),
                "sloping tuple insertion (1)",
                "sloping continuation of the marginal Isom arguments (1)",
            ),
            (
                ("doubts", 2, "alternatives"),
                "de or le; possible attachment to adjacent sloping insertion",
                "de or le in the separate main-line word; the sloping tuple is the resolved continuation of the marginal Isom formula",
            ),
            (
                ("doubts", 2, "reason"),
                "The word is visible at the main baseline with no separate strike, but the initial loop and its relation to the insertion are not fully secure.",
                "The separate word after Dans is visible at the main baseline with no independent strike. Its initial loop remains ambiguous between de and le. The completed B03/B06 adjudications identify the nearby sloping tuple as the continuation of the marginal Isom formula, not as a prose insertion; the main-line letter doubt remains.",
            ),
            (
                ("changes", changes66["066-06"], "evidence"),
                "It sits above the end of the sloping tuple insertion, so its attachment is recorded as a remaining doubt.",
                "The separate main-line word remains doubtful as de/le. The nearby sloping tuple is now identified as the continuation of the marginal Isom formula, not as a prose insertion.",
            ),
            (
                ("changes", changes66["066-32"], "evidence"),
                "start of éléments",
                "start of the written abbreviation elmts|elts",
            ),
            (
                ("notation", 5, "reading"),
                r"\operatorname{Isom}(\{0,1,\infty\},I\prime\prime)",
                r"\operatorname{Isom}(\{0,1,\infty\},I'')",
            ),
        ],
    }

    pending = []
    for scan, entries in repairs.items():
        updated = copy.deepcopy(originals[scan])
        for path, old, new in entries:
            replace_once(updated, path, old, new)
        actual = set(changed_paths(originals[scan], updated))
        allowed = {item[0] for item in entries}
        assert actual <= allowed, (scan, actual - allowed)
        if scan == 66:
            assert updated["doubts"][2]["reading"] == r"\unsure{de|le}"
            assert updated["notation"][5]["reading"].endswith("I'')")
        pending.append((scan, updated, actual))

    # Validate every proposed field change before writing either reviewed file.
    for scan, updated, actual in pending:
        path = WORK / "reviewed" / f"147_scan{scan:03}.json"
        if actual:
            path.write_text(json.dumps(updated, ensure_ascii=False, indent=2) + "\n")
            for key_path in sorted(actual, key=str):
                print(f"{path}: {key_path}")
        else:
            print(f"{path}: already repaired")


if __name__ == "__main__":
    main()
