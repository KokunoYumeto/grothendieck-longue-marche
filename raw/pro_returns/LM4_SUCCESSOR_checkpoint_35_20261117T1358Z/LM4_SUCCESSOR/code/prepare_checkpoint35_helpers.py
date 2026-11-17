"""Author separate checkpoint35 helper sources; execute no archive helper."""
from pathlib import Path
from hashlib import sha256
import ast
import difflib
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def one(text, before, after):
    assert text.count(before) == 1, before
    return text.replace(before, after)


def main():
    pairs = [
        ("preserve_checkpoint34_versions_inductive.py", "preserve_checkpoint35_versions_inductive.py"),
        ("verify_checkpoint34_inductive_retention.py", "verify_checkpoint35_inductive_retention.py"),
        ("estimate_checkpoint34_size.py", "estimate_checkpoint35_size.py"),
        ("verify_checkpoint34_system_tars.py", "verify_checkpoint35_system_tars.py"),
        ("build_checkpoint34_parent_anchor.py", "build_checkpoint35_parent_anchor.py"),
    ]
    rows, diffs = [], []
    old_sha = "5c68edb5a023c97cb400b506f7e1b7303f19e3cac9212947491e47793d77ef96"
    new_sha = "28dbe8b35a6f9e1c6b7e606aa59ceed041f2ab217959e0cc243ab7e83761d8fb"
    for old_name, new_name in pairs:
        old_path, new_path = ROOT/"code"/old_name, ROOT/"code"/new_name
        assert not new_path.exists()
        before = old_path.read_text()
        protected = before.replace(old_sha, "__PARENT_ARCHIVE_SHA__")
        changes = {"33": "34", "34": "35"}
        if "inductive" in new_name or "anchor" in new_name:
            changes.update({"32": "33", "10053": "10387",
                            "142600": "152653", "152653": "163040"})
        if "anchor" in new_name:
            changes.update({"31": "32", "9680": "10053",
                            "508499680": "529409669", "5195": "83033",
                            "28023": "88075", "66162": "81129"})
        pattern = r"(?<!\d)(" + "|".join(sorted(changes, key=len, reverse=True)) + r")(?!\d)"
        after = re.sub(pattern, lambda match: changes[match.group(0)], protected)
        after = after.replace("__PARENT_ARCHIVE_SHA__", new_sha)
        if "anchor" in new_name:
            after = one(after,
                'for name, session in [("archive", 83033), ("system_tars", 88075), ("inductive", 81129)]:',
                'for name, session, chunk in [("archive", 83033, "a92f0e"), ("system_tars", 88075, "0c93d3"), ("inductive", 81129, "25e218")]:')
            after = one(after,
                '"producer_session": session, "actual_exit_code_observed": 0}',
                '"producer_session": session, "producer_tool_chunk": chunk, "actual_exit_code_observed": 0}')
        if "system_tars" in new_name:
            after = one(after,
                "document_dictionary_bytes == 8388608 == packaging['document_lzma_dictionary_bytes']",
                "document_dictionary_bytes == 67108864 == packaging['document_lzma_dictionary_bytes']")
        if "estimate" in new_name:
            after = one(after,
                "Old changed direct costs remain in the baseline as a deliberate overcount.",
                "Old changed direct costs remain conservatively, except the proved direct-to-document migration of the old main PDF.")
            after = one(after, "    removed_direct_data = []",
                "    removed_direct_data = []\n    removed_direct_main_pdf = None")
            after = one(after,
                "                predicted_history.append({'path': historical, 'bytes': len(data), 'sha256': row['sha256']})",
                "                predicted_history.append({'path': historical, 'bytes': len(data), 'sha256': row['sha256']})\n"
                "            if rel == 'LM4_SUCCESSOR_paper.pdf':\n"
                "                info = prior.z.getinfo(PREFIX+rel)\n"
                "                assert PREFIX+rel in prior.direct and info.compress_type == zipfile.ZIP_DEFLATED\n"
                "                assert not unchanged and info.file_size == len(data)\n"
                "                assert bucket(historical, len(data)) == 'documents'\n"
                "                assert prospective[historical] == data\n"
                "                assert not is_data_bundle_member(rel, len(data))\n"
                "                removed_direct_main_pdf = {'path': rel, 'historical_path': historical,\n"
                "                    'bytes': len(data), 'sha256': digest(data),\n"
                "                    'compressed_payload_bytes': info.compress_size,\n"
                "                    'headers_removed': 0, 'reason': 'The same exact old direct PDF is measured once in the prospective document TAR.'}")
            after = one(after, "    del prospective",
                "    if removed_direct_main_pdf is not None:\n"
                "        documents = dict(groups['documents'])\n"
                "        old_pdf = documents[removed_direct_main_pdf['historical_path']]\n"
                "        assert len(old_pdf) == removed_direct_main_pdf['bytes']\n"
                "        assert digest(old_pdf) == removed_direct_main_pdf['sha256']\n"
                "        assert any(rel == 'LM4_SUCCESSOR_paper.pdf' for _, rel in new_direct)\n"
                "        assert all(rel != 'LM4_SUCCESSOR_paper.pdf' for _, rel in removed_direct_data)\n"
                "        del documents, old_pdf\n"
                "    del prospective")
            after = one(after,
                "        method = 'data-lzma' if kind in {'images','data'} else 'lzma'",
                "        method = 'data-lzma'  # All three checkpoint35+ TARs use native64MiB method14.")
            after = one(after,
                "'dictionary_bytes': DATA_DICTIONARY_BYTES if kind in {'images','data'} else 8*1024*1024,",
                "'dictionary_bytes': DATA_DICTIONARY_BYTES,")
            after = one(after,
                "    estimate = ARCHIVE.stat().st_size-sum(removed_containers.values())-migrated_removed+sum(x['compressed_bytes'] for x in bundle_reports.values())+direct_added",
                "    main_removed = 0 if removed_direct_main_pdf is None else removed_direct_main_pdf['compressed_payload_bytes']\n"
                "    estimate = ARCHIVE.stat().st_size-sum(removed_containers.values())-migrated_removed-main_removed+sum(x['compressed_bytes'] for x in bundle_reports.values())+direct_added")
            after = one(after,
                "        'previous_direct_data_compressed_bytes_removed': migrated_removed,",
                "        'previous_direct_data_compressed_bytes_removed': migrated_removed,\n"
                "        'previous_direct_main_pdf_migrated': removed_direct_main_pdf,\n"
                "        'previous_direct_main_pdf_compressed_payload_removed': main_removed,\n"
                "        'previous_direct_main_pdf_headers_removed': 0,")
            after = one(after,
                "Images and data use the actual64MiB ZIP-LZMA compressor; historical documents use the default8MiB compressor.",
                "All three buckets use the actual64MiB ZIP-LZMA compressor on their complete prospective35 bytes; no gain from the separate closed34 comparison is substituted.")
            after = one(after,
                "Changed old direct payload costs remain conservatively in the baseline while every new direct payload is added. The previous direct main PDF is also counted in the historical document TAR, deliberately overcounting it.",
                "Changed old direct payload costs otherwise remain conservatively while every new direct payload is added. The old direct main PDF compressed payload is subtracted exactly once only when its identical size/hash bytes are explicitly present in the measured prospective document TAR and the changed current main PDF is counted separately. Its headers remain counted; it is not part of the removed data payloads.")
        ast.parse(after, filename=str(new_path))
        with new_path.open("x") as stream:
            stream.write(after)
        rows.append({"source": str(old_path.relative_to(ROOT)),
                     "source_sha256": sha256(before.encode()).hexdigest(),
                     "target": str(new_path.relative_to(ROOT)),
                     "target_sha256": sha256(after.encode()).hexdigest(),
                     "target_bytes": len(after.encode())})
        diffs.extend(difflib.unified_diff(before.splitlines(True), after.splitlines(True),
                     fromfile=old_name, tofile=new_name))
    with (ROOT/"records/checkpoint35_helper_source_adaptation.json").open("x") as stream:
        json.dump({"archive_created": False, "retention_published": False,
                   "helpers_executed": False, "copies": rows,
                   "parent_logical_entries": 10387, "inherited_rows": 152653,
                   "expected_child_retention_rows": 163040,
                   "document_dictionary_change": "Only separate35 verifier/estimator expect64MiB; actual packaging awaits measured-gain approval.",
                   "parent_verification_observations": [
                       {"session": 83033, "tool_chunk": "a92f0e", "actual_exit_code": 0},
                       {"session": 88075, "tool_chunk": "0c93d3", "actual_exit_code": 0},
                       {"session": 81129, "tool_chunk": "25e218", "actual_exit_code": 0}]},
                  stream, indent=2)
        stream.write("\n")
    with (ROOT/"records/checkpoint35_helper_source_adaptation.diff").open("x") as stream:
        stream.writelines(diffs)
    print(json.dumps(rows, indent=2))


if __name__ == "__main__":
    main()
