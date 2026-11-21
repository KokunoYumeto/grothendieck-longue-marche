"""Repair seven stale scan064 metadata fields after the completed blind audit.

Idempotent; reads completed adjudications and writes only reviewed/147_scan064.json.
Frozen readings, pages, adjudications, check events, and generated files are untouched.
"""

import copy
import json
from pathlib import Path


WORK = Path(__file__).resolve().parents[1]
TARGET = WORK / "reviewed" / "147_scan064.json"


def field(document, path):
    for key in path:
        document = document[key]
    return document


def replace_once(document, path, old, new):
    current = field(document, path)
    if new in current and old not in current:
        return
    if current.count(old) != 1:
        raise ValueError(f"Unexpected current value at {path!r}; no file written")
    parent = field(document, path[:-1])
    parent[path[-1]] = current.replace(old, new, 1)


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
    adjudications = json.loads(
        (WORK / "second" / "147_scan064_adjudications.json").read_text()
    )
    authority = {item["box"]: item for item in adjudications}
    for box in ["B11", "B12"]:
        assert authority[box]["changed"] and authority[box]["root_viewed"]
    assert r"\deleted{\unsure{\mathbb E}}" in authority["B11"]["final"]
    assert "two close parallel uprights" in authority["B11"]["evidence"]
    assert "Preserve the crossed-letter uncertainty" in authority["B11"]["evidence"]
    assert "Move the U equation above the braced group" in authority["B12"]["evidence"]

    original = json.loads(TARGET.read_text())
    assert original["audit_complete"] is True
    assert len(original["changes"]) == 29
    assert len(original["doubts"]) == 11
    for index, element in [(15, "16"), (16, "17"), (19, "20")]:
        assert original["inventory"][index]["element"] == element
    assert original["doubts"][6]["reading"] == r"\deleted{\unsure{\mathbb E}}"

    repairs = [
        (
            ("notes", 3),
            "and defines U, {a_2,a_3}, S'_0 and S'_1 under a brace.",
            "and defines U above the lower brace; the brace groups only the intersection equation for {a_2,a_3} and the definitions of S'_0 and S'_1.",
        ),
        (
            ("inventory", 19, "position"),
            "lower brace, three main formula rows",
            "U equation above the brace; two following main formula rows grouped by the brace",
        ),
        (
            ("inventory", 15, "first_words_or_objects"),
            r"\deleted{\unsure{E}}",
            r"\deleted{\unsure{\mathbb E}}",
        ),
        (
            ("inventory", 16, "first_words_or_objects"),
            r"\deleted{\unsure{E}}",
            r"\deleted{\unsure{\mathbb E}}",
        ),
        (
            ("doubts", 6, "alternatives"),
            "Exact original letter and any internal doubling unresolved.",
            r"The original canceled letter remains uncertain. Two close parallel uprights are now seen and represented by \mathbb E; the crossed-letter uncertainty is retained.",
        ),
        (
            ("notes", 6),
            "The report has 28 substantive comparison rows",
            "The completed report has 29 substantive comparison rows",
        ),
        (
            ("witness_comparison",),
            "The final candidate retains nine doubts",
            "The final candidate retains eleven doubts",
        ),
    ]

    updated = copy.deepcopy(original)
    for path, old, new in repairs:
        replace_once(updated, path, old, new)
    actual = set(changed_paths(original, updated))
    allowed = {item[0] for item in repairs}
    assert actual <= allowed, actual - allowed
    assert updated["doubts"][6]["reading"] == original["doubts"][6]["reading"]
    assert r"\unsure{\mathbb E}" in updated["inventory"][16]["first_words_or_objects"]

    if actual:
        TARGET.write_text(json.dumps(updated, ensure_ascii=False, indent=2) + "\n")
        for path in sorted(actual, key=str):
            print(f"{TARGET}: {path}")
    else:
        print(f"{TARGET}: already repaired")


if __name__ == "__main__":
    main()
