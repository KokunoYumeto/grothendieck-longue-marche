"""Create a due hourly checkpoint without reading scans or context sources."""

from datetime import datetime, timezone, timedelta
from pathlib import Path
import re
import sys
import time
import zipfile


PACKAGE = "MPL_136_002-046"
ROOT = Path(__file__).resolve().parents[1]
STARTED = datetime(2026, 11, 17, 13, 21, 10, tzinfo=timezone.utc)
EXPECTED_SCANS = tuple(n for n in range(2, 47) if n != 19)
PAGE_PATTERN = re.compile(r"^MPL_136_002-046_136_scan(\d{3})\.tex$")
EXCLUDED_DIRECTORIES = {"__pycache__", "upload", "uploads", "scans", "context"}
ATTACHED_PROMPT = "PROMPT(20261117-132016).md"


def utc_text(value):
    return value.strftime("%Y-%m-%d %H:%M:%S UTC")


def scan_list(scans):
    return ", ".join(f"{scan:03d}" for scan in sorted(scans)) or "none"


def derive_state(page_names, log_text, combined_exists):
    """Derive status from filenames and explicit log records, not page contents."""
    expected = set(EXPECTED_SCANS)
    saved = set()
    unexpected_names = []
    for name in page_names:
        match = PAGE_PATTERN.fullmatch(name)
        if match and int(match.group(1)) in expected:
            saved.add(int(match.group(1)))
        else:
            unexpected_names.append(name)
    done = {
        int(match.group(1))
        for match in re.finditer(r"(?m)^136 scan (\d+) done\s+", log_text)
    }
    audited = {
        int(match.group(1))
        for match in re.finditer(r"(?m)^scan (\d+) audited\s+", log_text)
    }
    lines = log_text.splitlines()
    freezes = [line for line in lines if line.startswith("transcription frozen ")]
    contexts = [line for line in lines if line.startswith("context opened ")]
    unchanged = [
        line for line in lines
        if re.search(r"hash.*unchanged|unchanged.*hash", line, flags=re.IGNORECASE)
    ]
    return {
        "saved": saved,
        "done": done & expected,
        "completed": saved & done & expected,
        "audited": audited & expected,
        "saved_without_done": saved - done,
        "done_without_file": (done & expected) - saved,
        "unexpected_names": sorted(unexpected_names),
        "unexpected_logged_scans": (done | audited) - expected,
        "combined_exists": combined_exists,
        "freeze_record": freezes[-1] if freezes else None,
        "context_record": contexts[-1] if contexts else None,
        "unchanged_record": unchanged[-1] if unchanged else None,
    }


def render_work_state(state, number, now):
    missing = set(EXPECTED_SCANS) - state["completed"]
    unaudited = set(EXPECTED_SCANS) - state["audited"]
    next_page = f"scan {min(missing):03d}" if missing else "none; all expected pages have saved files and done records"
    next_audit = f"scan {min(unaudited):03d}" if unaudited else "none; all expected scans have audit records"
    frozen = state["freeze_record"] or "No transcription frozen record."
    context = state["context_record"] or "No context opened record."
    unchanged = state["unchanged_record"] or "No unchanged-hash verification record."
    discrepancies = []
    if state["saved_without_done"]:
        discrepancies.append("Saved page files without done records: " + scan_list(state["saved_without_done"]))
    if state["done_without_file"]:
        discrepancies.append("Done records without page files: " + scan_list(state["done_without_file"]))
    if state["unexpected_names"]:
        discrepancies.append("Unexpected page filenames: " + ", ".join(state["unexpected_names"]))
    if state["unexpected_logged_scans"]:
        discrepancies.append("Unexpected scans in completion/audit records: " + scan_list(state["unexpected_logged_scans"]))
    discrepancy_text = "\n".join("- " + item for item in discrepancies) or "None detected from filenames and completion records."
    return f"""# Work state at hourly checkpoint {number:02d}

Snapshot time: {utc_text(now)}.

The attached source prompt is authoritative. This snapshot is derived from page filenames and progress.log records; it does not independently certify visual reading, transcription accuracy, or completeness. Only root performs image reading, transcription, notation reconciliation, and visual audit, in one sequential stream and without OCR.

## Recorded progress

- Saved expected page files: {len(state['saved'])}/44; scans {scan_list(state['saved'])}.
- Completion records: {len(state['done'])}/44; scans {scan_list(state['done'])}.
- Completed pages with both a saved file and a done record: {len(state['completed'])}/44; scans {scan_list(state['completed'])}.
- Next page lacking completed status: {next_page}.
- Audit records: {len(state['audited'])}/44; scans {scan_list(state['audited'])}.
- Next scan lacking an audit record: {next_audit}.
- Combined transcription file present: {'yes' if state['combined_exists'] else 'no'}.
- Freeze status: {frozen}
- Context status: {context}
- Hash verification status: {unchanged}

The next unfinished page may already be under active reading; the absence of a completion record does not mean it has not been viewed. Blank scan 019 was omitted from the supplied scans and is not one of the 44 required pages.

## Filename and completion-record discrepancies

{discrepancy_text}

## Continuation requirements

Finish any uncompleted scans in order, saving each page, inventory rows, doubts, and UTC completion entry before moving on. Then root must visually audit every page again, reconcile recurring notation, and finish the doubts/abbreviations register. Assemble the combined fragment as exact ordered concatenation; record SHA-256 values for all 44 page files and the combined transcription; then log the freeze. Do not repeat stages already evidenced above without checking the current work.

Only after all pages are audited and the transcription is frozen may the context be opened. Log context opened, then read its README and RESULTS_STATE and write the research notes. Once context has been opened, no transcription bytes may change; context-suggested readings belong in research notes. Confirm the frozen hashes unchanged at the end. Initial inspection of context filename/size metadata, without contents, is disclosed in progress.log.

Ancillary structural checks and upload preparation may be delegated. The validator is scripts/validate_package.py, and the current upload helpers/instructions are in scripts/library_transfer/. Do not delegate image reading, transcription, or visual audit.

## Checkpoint schedule and contents

Checkpoint {number:02d} was due at {utc_text(STARTED + timedelta(hours=number))}. The next hourly checkpoint, {number + 1:02d}, is due at {utc_text(STARTED + timedelta(hours=number + 1))}. Create checkpoints only on this hourly schedule, never overwrite an earlier one, and upload each completed ZIP so it survives a disconnection.

Each checkpoint contains all current deliverables and work documentation under the output directory. Attached inputs, scan/context source directories, previous ZIPs, and Python bytecode/cache directories are excluded. The final ZIP is MPL_136_002-046.zip, offered as the only final download.
"""


def eligible_for_checkpoint(path, root):
    relative = path.relative_to(root)
    if any(part in EXCLUDED_DIRECTORIES for part in relative.parts):
        return False
    if path.name == ATTACHED_PROMPT or path.suffix.lower() in {".zip", ".pyc", ".pyo"}:
        return False
    return not path.is_symlink() and path.is_file()


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        raise SystemExit("Usage: python scripts/create_checkpoint.py CHECKPOINT_NUMBER")
    try:
        number = int(args[0])
    except ValueError:
        raise SystemExit("Checkpoint number must be a positive integer.")
    if number < 1:
        raise SystemExit("Checkpoint number must be a positive integer.")
    zip_path = ROOT.parent / f"{PACKAGE}_checkpoint_{number:02d}.zip"
    if zip_path.exists():
        raise SystemExit("Refusing to overwrite an earlier checkpoint.")
    due = STARTED + timedelta(hours=number)
    remaining = (due - datetime.now(timezone.utc)).total_seconds()
    if remaining > 60:
        raise SystemExit("Checkpoint is not yet due; checkpoints may be made only hourly.")
    if remaining > 0:
        time.sleep(remaining)

    now = datetime.now(timezone.utc)
    page_names = [path.name for path in (ROOT / "pages").glob("*.tex") if path.is_file()]
    log_path = ROOT / "progress.log"
    log_text = log_path.read_text(encoding="utf-8")
    state = derive_state(page_names, log_text, (ROOT / f"{PACKAGE}_transcription.tex").is_file())

    # Exclusive archive creation preserves the no-overwrite rule even if a
    # second caller appears after the existence check above.
    with zipfile.ZipFile(zip_path, "x", zipfile.ZIP_DEFLATED) as archive:
        (ROOT / "WORK_STATE.md").write_text(render_work_state(state, number, now), encoding="utf-8")
        context_status = "opened" if state["context_record"] else "no open record"
        freeze_status = "yes" if state["freeze_record"] else "no"
        with log_path.open("a", encoding="utf-8") as log:
            log.write(
                f"hourly checkpoint {number:02d} created {utc_text(now)}; "
                f"{len(state['completed'])} completed pages; "
                f"{len(state['saved'])} page files; "
                f"audits {len(state['audited'])}/44; "
                f"frozen {freeze_status}; context {context_status}\n"
            )
        for path in sorted(ROOT.rglob("*")):
            if eligible_for_checkpoint(path, ROOT):
                archive.write(path, path.relative_to(ROOT))
    print(zip_path)
    print(f"{zip_path.stat().st_size} bytes")


if __name__ == "__main__":
    main()
