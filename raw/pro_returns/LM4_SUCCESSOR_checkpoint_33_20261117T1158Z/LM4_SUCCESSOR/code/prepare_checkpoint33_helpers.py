"""Create separate 32-to-33 helpers without changing any checkpoint32 source.

This program only writes new reviewed-source candidates. It does not open,
create, compress, or modify an archive, and does not publish retention.
"""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def shifted(text, retention):
    replacements = {
        "30": "31", "31": "32", "32": "33",
        "9388": "9680", "123532": "132920", "132920": "142600",
    }
    # The native ZIP reader's 30-byte header is a format constant, not a
    # checkpoint number. Shift30 only in the two retention helpers.
    pattern = r"(?<!\d)(123532|132920|9388|30|31|32)(?!\d)" if retention else r"(?<!\d)(31|32)(?!\d)"
    return re.sub(pattern,
                  lambda match: replacements[match.group(0)], text)


def main():
    specifications = [
        ("code/preserve_checkpoint_versions_inductive.py",
         "code/preserve_checkpoint33_versions_inductive.py"),
        ("code/verify_checkpoint_inductive_retention.py",
         "code/verify_checkpoint33_inductive_retention.py"),
        ("code/estimate_checkpoint32_size.py", "code/estimate_checkpoint33_size.py"),
        ("code/verify_checkpoint32_system_tars.py", "code/verify_checkpoint33_system_tars.py"),
    ]
    rows = []
    for source, target in specifications:
        old = (ROOT / source).read_bytes()
        text = shifted(old.decode(), "inductive" in target)
        text = text.replace("work_DE/checkpoint33_retention_parent_anchor.json",
                            "records/checkpoint33_retention_parent_anchor.json")
        if target.endswith("preserve_checkpoint33_versions_inductive.py"):
            text = text.replace(
                "SOURCE RECONSTRUCTION: retain parent32 and compose its pinned historical map.\n\n"
                "This is newly reconstructed source, not the lost pre-outage source bytes.",
                "Retain parent32 and compose its freshly verified historical map.\n\n"
                "This separate33 helper adapts the reviewed32 source; that source is unchanged.")
            text = text.replace("This reconstructed helper is bound specifically to32->33",
                                "This helper is bound specifically to32->33")
            text = text.replace("reconstructed_source=True, parent_number=32, child_number=33",
                                "adapted_from_reviewed_checkpoint32_source=True, parent_number=32, child_number=33")
        elif target.endswith("verify_checkpoint33_inductive_retention.py"):
            text = text.replace("SOURCE RECONSTRUCTION: independently verify the CLOSED33 induction step.",
                                "Independently verify the CLOSED33 induction step.")
            text = text.replace("from preserve_checkpoint_versions_inductive import (",
                                "from preserve_checkpoint33_versions_inductive import (")
        new = text.encode()
        destination = ROOT / target
        assert not destination.exists(), target
        compile(text, str(destination), "exec")
        with destination.open("xb") as stream:
            stream.write(new)
        rows.append({"source": source, "source_bytes": len(old),
                     "source_sha256": digest(old), "target": target,
                     "target_bytes": len(new), "target_sha256": digest(new)})
    report = {"mode": "source-only adaptation", "archive_created": False,
              "retention_published": False, "copies": rows,
              "parent_logical_entries": 9680, "inherited_rows": 132920,
              "expected_child_retention_rows": 142600}
    path = ROOT / "records/checkpoint33_helper_source_adaptation.json"
    with path.open("x") as stream:
        json.dump(report, stream, indent=2)
        stream.write("\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
