"""Recompute only explicit finite counts in the frozen reused typescript.

No scan images or context are read, and no transcription is modified.
Reported counts without their members (e.g. eighteen semantic groups) remain
reported counts; the script does not manufacture an enumeration for them.
"""
from pathlib import Path
from itertools import product
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PAIR_LISTS = [
    {"scan": 173, "lines": [9, 16], "role": "first six",
     "pairs": ["Action-inaction", "activité-passivité", "veille-sommeil",
               "sujet-objet", "engendrer-concevoir (*)",
               "exécution-conception (*)"]},
    {"scan": 177, "lines": [4, 11], "role": "six continued",
     "pairs": ["dynamisme-équilibre", "élan-assise", "ardeur-persévérance",
               "fougue- patience", "passion-sérénité", "tenacité-détachement."]},
    {"scan": 177, "lines": [17, 20], "role": "two proposed additions",
     "pairs": ["savoir-connaître", "expliquer-comprendre."]},
]
PAGE_LABELS = {
    147: "475", 149: "475 bis", 151: "478", 153: "476", 155: "479",
    157: "486", 159: "487", 161: "489", 163: "488", 165: "477",
    167: "482", 169: "483", 171: "484", 173: "491", 175: "490",
    177: "492", 179: "493", 181: "494", 183: "495", 185: "496",
    187: "500", 189: "497", 191: "498", 193: "499",
}
ART_LISTS = [
    {"scan": 189, "lines": [9, 11], "role": "main examples",
     "labels": ["calligraphie", "poésie", "art culinaire", "art médical"],
     "literal_source_strings": ["calligraphie", "poésie", "l'art culinaire", "l'art médical"]},
    {"scan": 189, "lines": [38, 39], "role": "21 October addition",
     "labels": ["art divinatoire"],
     "literal_source_strings": [r"\mbox{a r t\quad d i v i n a t o i r e}"]},
]
REPORTED_COUNTS = [
    {"key": "earlier_pairs", "scan": 175, "lines": [4, 4],
     "literal": "une centaine ou deux", "reported_range": [100, 200],
     "semantics": "Approximate recollected size, five years earlier; not all members printed."},
    {"key": "earlier_groups", "scan": 175, "lines": [4, 4],
     "literal": "une vingtaine de groupes", "nominal_value": 20,
     "semantics": "Initially approximate; the same paragraph restates it as 'au lieu de vingt'."},
    {"key": "revised_groups", "scan": 175, "lines": [4, 7],
     "literal": "dix-huit groupes", "nominal_value": 18,
     "semantics": "Author's reported current total. The complete eighteen-member group list is not printed here."},
    {"key": "diagram_generations", "scan": 173, "lines": [7, 7],
     "literal": "huit", "nominal_value": 8,
     "semantics": "Reported generations in the semantic diagram; no full diagram is supplied on this leaf."},
    {"key": "diagram_drafts", "scan": 175, "lines": [7, 7],
     "literal": "cinq ou six ébauches", "reported_range": [5, 6],
     "semantics": "Reported drafting count, not a count of surviving drawings in this packet."},
    {"key": "late_pairs", "scan": 177, "lines": [13, 15],
     "literal": "une dizaine de", "nominal_value": 10,
     "semantics": "Approximate late-arriving set; only two proposed additions are displayed."},
    {"key": "meditation_leaves", "scan": 151, "lines": [32, 33],
     "literal": "dix huit feuilles", "nominal_value": 18,
     "semantics": "Reported leaves of a prior meditation manuscript; not the eighteen semantic groups or a count of supplied pages."},
    {"key": "unidentified_texts", "scan": 193, "lines": [29, 33],
     "literal": "deux ou trois textes", "reported_range": [2, 3],
     "semantics": "Reported European expositions; neither a complete bibliography nor identified titles."},
]


def main():
    sources = {}
    for scan in PAGE_LABELS:
        path = ROOT / "pages" / f"MPL_84_146-193_84_scan{scan}.tex"
        sources[scan] = path.read_text()
    final = json.loads((ROOT / "records/tex_validation.json").read_text())
    hashes = {x["file"]: x["sha256"] for x in final["pages"]}
    manifest = []
    for scan, label in PAGE_LABELS.items():
        relative = f"pages/MPL_84_146-193_84_scan{scan}.tex"
        digest = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
        assert digest == hashes[relative], f"Frozen source hash changed: {relative}"
        command = next(line for line in sources[scan].splitlines()
                       if line.startswith(r"\mspage{"))
        if scan == 149:
            assert command == r"\mspage{47\deleted{\unsure{6}}\inserted{5 bis}}"
        else:
            assert command == r"\mspage{" + label + "}"
        assert r"\margin{" + str(scan-1) + "}" in sources[scan]
        manifest.append({"scan": scan, "source": relative, "sha256": digest,
                         "printed_label": label, "printed_label_source_command": command,
                         "archival_pencil": scan-1})
    for entry in PAIR_LISTS:
        lo, hi = entry["lines"]
        block = "\n".join(sources[entry["scan"]].splitlines()[lo-1:hi])
        extracted = re.findall(r"\\text\{([^{}]*)\}", block)
        assert extracted == entry["pairs"], (entry["scan"], extracted)
    pair_sizes = [len(x["pairs"]) for x in PAIR_LISTS]
    assert pair_sizes == [6, 6, 2] and sum(pair_sizes) == 14
    assert "les quatorze couples" in sources[183]
    for item in REPORTED_COUNTS:
        assert item["literal"] in re.sub(r"\s+", " ", sources[item["scan"]]), item
    assert "au lieu de vingt" in sources[175]
    for item in ART_LISTS:
        for literal in item["literal_source_strings"]:
            assert literal in sources[item["scan"]], (item, literal)
    assert [len(item["labels"]) for item in ART_LISTS] == [4, 1]
    binary_sequences = ["".join(word) for word in product("01", repeat=6)]
    assert len(binary_sequences) == 2**6 == 64
    assert "000000" in binary_sequences and "111111" in binary_sequences
    assert "64" in sources[189] and r"$2^{\inserted{6}}$" in sources[189]
    numbered = sorted(int(label) for label in PAGE_LABELS.values() if label.isdigit())
    missing = sorted(set(range(475, 501)) - set(numbered))
    assert len(PAGE_LABELS) == 24 and len(numbered) == 23
    assert len(set(PAGE_LABELS.values())) == 24
    assert missing == [480, 481, 485]
    report = {
        "utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "scope": __doc__,
        "source_manifest": manifest,
        "literal_pair_lists": PAIR_LISTS,
        "pair_check": {"summands": pair_sizes, "computed_total": sum(pair_sizes),
                       "explicit_author_total": 14, "author_total_source": "scan183:37",
                       "november_6_reclassification": {
                           "source": "scan173:20",
                           "transferred_pairs": ["engendrer-concevoir", "exécution-conception"],
                           "destination": "père-mère",
                           "semantics": "The later note revises membership; no final replacement group list or total is printed. Do not silently replace the original fourteen."}},
        "binary_count": {"length": 6, "alphabet_size": 2, "computed_total": 2**6,
                         "author_total": 64, "source": "scan189:40–43",
                         "editorial_encoding": {"0": "yin", "1": "yang"},
                         "sequences": binary_sequences,
                         "semantics": "Finite binary counting only; no verification of divination or archetypal claims."},
        "pagination_check": {"leaves": 24, "numbered_pages": 23,
                             "supplement": ["475 bis"], "numbered_interval": [475, 500],
                             "missing_numbered_pages": missing,
                             "archival_order_differs_from_printed_order": True},
        "reported_counts": REPORTED_COUNTS,
        "named_arts": {"lists": ART_LISTS, "count": sum(len(item["labels"]) for item in ART_LISTS),
                       "semantics": "Four main examples plus one dated addition; no exhaustive catalogue is claimed."},
        "group_count_comparison": {"earlier_nominal": 20, "later_reported": 18,
                                   "nominal_arithmetic_difference": 20-18,
                                   "semantics": "Reported 20→18 regrouping; arithmetic difference two does not identify two removed groups. Earlier count is first described approximately. No full group enumeration is supplied."},
        "all_assertions_passed": True,
    }
    target = Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print("Verified literal lists 6+6+2=14, binary count 2^6=64, pagination 24=23+bis, missing480/481/485.")
    print("Reported counts preserved with explicit semantics: 20→18 groups,18 meditation leaves, and other reported totals.")
    print("All24 typed sources match frozen compilation hashes.")


if __name__ == "__main__":
    main()
