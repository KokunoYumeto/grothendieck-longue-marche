#!/usr/bin/env python3
"""Parent-requested exact Gram assertion; preserves both original runs."""
from pathlib import Path
import difflib
import hashlib
import json
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
records = []
for stem, backup_stem in [
    ("notes/fgh_A77_certificate", "notes/fgh_A77_certificate_before_exact_gram"),
    ("code/a_commutator_order_two", "notes/fgh_A77_canonical_before_exact_gram"),
]:
    for suffix in (".py", ".json", ".out"):
        original = root / (stem + suffix)
        backup = root / (backup_stem + suffix)
        assert not backup.exists()
        backup.write_bytes(original.read_bytes())
    source = root / (stem + ".py")
    old = source.read_text()
    needle = "    gram=[[sum(a*b for a,b in zip(v,w))//32 for w in chars] for v in chars]\n    assert gram==[[int(i==j) for j in range(4)] for i in range(4)]"
    assert old.count(needle) == 1
    new = old.replace(needle,
        "    gram_numerators=[[sum(a*b for a,b in zip(v,w)) for w in chars] for v in chars]\n"
        "    assert gram_numerators==[[32*int(i==j) for j in range(4)] for i in range(4)]\n"
        "    gram=[[value//32 for value in row] for row in gram_numerators]\n"
        "    assert gram==[[int(i==j) for j in range(4)] for i in range(4)]")
    new = new.replace("'nonlinear_character_gram':gram,", "'nonlinear_character_gram_numerators':gram_numerators,'nonlinear_character_gram':gram,")
    source.write_text(new)
    diff = "".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
                  fromfile=backup_stem + ".py", tofile=stem + ".py"))
    (root / (backup_stem + ".diff")).write_text(diff)
    with (root / (stem + ".out")).open("w") as output:
        subprocess.run([sys.executable, str(source)], stdout=output,
                       stderr=subprocess.STDOUT, check=True)
    before = json.loads((root / (backup_stem + ".json")).read_text())
    after = json.loads((root / (stem + ".json")).read_text())
    exact = after.pop("nonlinear_character_gram_numerators")
    assert exact == [[32 * int(i == j) for j in range(4)] for i in range(4)]
    assert after == before
    records.append({"source": stem + ".py", "preserved_original_stem": backup_stem,
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "result_sha256": hashlib.sha256((root / (stem + ".json")).read_bytes()).hexdigest(),
        "all_previous_output_fields_unchanged": True,
        "exact_undivided_gram": exact})

record = {"status": "PASS", "reason": "Parent-requested literal undivided orthogonality check",
          "theorem_or_proof_changed": False, "records": records}
(root / "notes/fgh_A77_orthogonality_precision.json").write_text(json.dumps(record, indent=2) + "\n")
with (root / "notes/fgh_A77_sources.md").open("a") as output:
    output.write("\n\n## Exact Gram assertion strengthened after integration\n\n"
        "The candidate and canonical certificates now assert the undivided nonlinear "
        "character dot products are exactly 32 times the identity before forming the Gram matrix. "
        "Both reruns passed; all prior output fields are unchanged. Original sources/outputs "
        "and exact diffs are preserved under notes/fgh_A77_certificate_before_exact_gram "
        "and notes/fgh_A77_canonical_before_exact_gram. Current hashes and the exact "
        "numerator matrix are in notes/fgh_A77_orthogonality_precision.json. "
        "No theorem or proof change was needed.\n")
print(json.dumps(record, indent=2))
