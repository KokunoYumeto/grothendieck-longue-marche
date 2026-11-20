#!/usr/bin/env python3
"""Check final ZIP filename coverage against the supplied checkpoint ZIPs.

Usage:
  python check_archive_coverage.py FINAL.zip CHECKPOINT_01.zip CHECKPOINT_02.zip
  python check_archive_coverage.py FINAL.zip CHECKPOINT_01.zip CHECKPOINT_02.zip --report REPORT.json

This is independent of the all-pages integrity check. It reads ZIP directories
only: no extraction, member contents, transcription checks or content hashes.
All checkpoint file names, including work documents and ARCHIVE_MANIFEST files,
must persist. Directory entries and nested *.zip members are excluded. File
contents may evolve; ARCHIVE_MANIFEST content changes are explicitly allowed.
"""
from collections import Counter
from pathlib import Path, PurePosixPath
import argparse
import json
import sys
import zipfile


def file_names(path, problems):
    names = []
    nested_zips = []
    directories = 0
    try:
        with zipfile.ZipFile(path) as archive:
            for item in archive.infolist():
                if item.is_dir():
                    directories += 1
                    continue
                name = item.filename
                while name.startswith("./"):
                    name = name[2:]
                parts = PurePosixPath(name).parts
                if not name or name.startswith("/") or ".." in parts or "\\" in name:
                    problems.append(f"Invalid member path in {path.name}: {item.filename}")
                    continue
                if PurePosixPath(name).suffix.lower() == ".zip":
                    nested_zips.append(name)
                    continue
                names.append(name)
    except (OSError, zipfile.BadZipFile, zipfile.LargeZipFile) as exc:
        problems.append(f"Cannot inspect archive {path}: {exc}")
    duplicates = sorted(name for name, count in Counter(names).items() if count > 1)
    if duplicates:
        problems.append(f"Duplicate file names in {path.name}: {duplicates}")
    if not names:
        problems.append(f"Archive has no eligible file members: {path}")
    return set(names), {
        "path": str(path),
        "file_count": len(set(names)),
        "directory_entries_excluded": directories,
        "nested_zip_members_excluded": sorted(nested_zips),
        "duplicate_file_names": duplicates,
    }


def check_coverage(final, checkpoints):
    problems = []
    final_names, final_info = file_names(final, problems)
    required = set()
    checkpoint_info = []
    for checkpoint in checkpoints:
        names, info = file_names(checkpoint, problems)
        required.update(names)
        missing = sorted(names - final_names)
        info["missing_from_final"] = missing
        checkpoint_info.append(info)
        if missing:
            problems.append(f"Checkpoint members missing from final ({checkpoint.name}): {missing}")
    manifests = sorted(
        name for name in required
        if PurePosixPath(name).name.startswith("ARCHIVE_MANIFEST")
    )
    return {
        "mode": "ZIP file-name coverage only",
        "final": final_info,
        "checkpoints": checkpoint_info,
        "required_file_names": len(required),
        "retained_checkpoint_file_names": len(required & final_names),
        "missing_from_final": sorted(required - final_names),
        "additional_final_file_names": sorted(final_names - required),
        "archive_manifest_members": manifests,
        "archive_manifest_content_changes_allowed": True,
        "member_contents_compared": False,
        "work_document_file_names_included": True,
        "problems": problems,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("final", type=Path)
    parser.add_argument("checkpoints", type=Path, nargs="+")
    parser.add_argument("--report", type=Path,
                        help="Optional JSON report; omitted means stdout only.")
    args = parser.parse_args()
    input_paths = {args.final.resolve(), *(path.resolve() for path in args.checkpoints)}
    if len(input_paths) != 1 + len(args.checkpoints):
        parser.error("Final and all checkpoint ZIP paths must be distinct.")
    if args.report and args.report.resolve() in input_paths:
        parser.error("The report path must not overwrite an input ZIP.")
    report = check_coverage(args.final, args.checkpoints)
    encoded = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        args.report.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
    return 1 if report["problems"] else 0


if __name__ == "__main__":
    sys.exit(main())
