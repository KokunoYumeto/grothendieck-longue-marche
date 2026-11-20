#!/usr/bin/env python3
"""Clarify overprint record wording without changing any transcription judgment.

The permitted edits are administrative prose only. The exact JSON leaf changes,
brief-history append, and unchanged-file hashes are retained in an audit log.
No images, compiler, build, or reading-generation code is used.
"""

from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path


WORK = Path(__file__).resolve().parents[1]
ROOT = WORK.parent
SCANS = ("065", "068", "070", "071")
LOG = WORK / "decisions/overprint_record_wording_changes.json"
AUDIT = WORK / "decisions/overprint_convention_audit.md"
BRIEF_HISTORY = WORK / "brief_changes.md"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def get_at(document, path):
    for item in path:
        document = document[item]
    return document


def leaves(value, path=()):
    if isinstance(value, dict):
        for key, child in value.items():
            yield from leaves(child, path + (key,))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from leaves(child, path + (index,))
    else:
        yield path, value


def main():
    if LOG.exists():
        prior = json.loads(LOG.read_text())
        for change in prior["json_changes"]:
            current = json.loads((ROOT / change["file"]).read_text())
            assert get_at(current, change["path"]) == change["after"]
        print("Administrative overprint wording correction is already applied.")
        return

    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    date = stamp[:10]
    files = {scan: WORK / f"decisions/156-4_{scan}.json" for scan in SCANS}
    original_text = {scan: path.read_text() for scan, path in files.items()}
    original = {scan: json.loads(text) for scan, text in original_text.items()}
    revised = deepcopy(original)
    touched = set()

    # These are the final page files under review, their exact C sources, the
    # consolidated text, and every historical brief. None may be written here.
    protected = []
    for number in range(65, 72):
        suffix = f"_156-4_scan{number:03}.tex"
        protected.extend(WORK.joinpath("pages").glob("*" + suffix))
        protected.extend(ROOT.joinpath("source/SP52_CW_156-4+156-6_witnesses/codex").glob("*/pages/*" + suffix))
    protected.extend(WORK.joinpath("briefs").glob("brief_v*.md"))
    protected.append(WORK / "SP52_CW_156-4+156-6_transcription.tex")
    protected = sorted(set(protected))
    before_hashes = {str(p.relative_to(ROOT)): digest(p) for p in protected}

    def set_value(scan, path, value, expected=None, missing=False):
        target = revised[scan]
        for item in path[:-1]:
            target = target[item]
        if missing:
            assert path[-1] not in target, (scan, path)
        elif expected is not None:
            assert target[path[-1]] == expected, (scan, path)
        target[path[-1]] = value
        touched.add((scan, tuple(path)))

    prose_fields = {"scan_shows", "evidence", "reason", "consequence", "workflow_note"}

    def replace_prose(scan, old, new, expected_count):
        matches = [(path, value) for path, value in leaves(revised[scan])
                   if isinstance(value, str) and old in value]
        assert len(matches) == expected_count, (scan, old, len(matches))
        for path, value in matches:
            assert path[-1] in prose_fields or path[:2] == ("notes", "math_reading_decisions"), path
            set_value(scan, path, value.replace(old, new))

    old065 = "A single word-sized group has reinforced val-like initial strokes and an idité-like ending. There is no separate old word followed by a second complete validité. Whether the initial val is crossed or retraced remains uncertain."
    new065 = "A single word-sized group has reinforced val-like initial strokes and an idité-like ending. Whether the initial val is crossed or retraced remains uncertain. The recorded difference from C concerns its proposed older déd/val and live validité/déduction alternatives: the retained alternatives are live validité or cancellation of its val prefix. Convention 4 permits an older form before its live replacement, so that encoding alone does not assert separate manuscript positions."
    replace_prose("065", old065, new065, 2)
    replace_prose("065", "The val-like start and subsequent idité-like ink form one word-sized group. Whether the first letters are crossed or joined/retraced remains unsettled.", "The val-like start and subsequent idité-like ink form one word-sized group. Whether the first letters are crossed or joined/retraced remains unsettled. The difference from C concerns the proposed older-prefix/live-word alternatives and cancellation uncertainty; old-before-live encoding alone does not establish separate positions.", 1)
    replace_prose("065", "The visible remainder is only the latter part of a validity-like word; a separate complete validité or déduction after a canceled word is not supported.", "The visible remainder is the latter part of a validity-like word. The retained alternatives are live validité or cancellation of its val prefix, replacing C's proposed older déd/val and live validité/déduction alternatives. Convention 4 allows old-before-live notation for overwritten layers; the difference concerns the letter alternatives and cancellation uncertainty.", 1)
    set_value("065", ("c_doubts", 8, "location"), "Inserted sentence: live-word alternatives", expected="Inserted sentence: alleged following complete word")
    replace_prose("065", "The first group may be crossed or retraced; no independent second word is visible.", "The val-like initial group may be crossed or retraced. The remaining uncertainty concerns cancellation of that prefix within the retained validité reading; C's old-before-live notation alone does not establish separate positions.", 1)

    old068 = "One densely worked suffix follows anti. A dark crossing runs through the early cluster, while a looped ascender and a tion-like ending survive. The ink does not independently establish two complete successive words isomorph/homéo and involution. The first alternative retains a possibly cancelled invo within one word; the other candidates keep the exact lettering and cancellation state open."
    new068 = "One densely worked suffix follows anti. A dark crossing runs through the early cluster, while a looped ascender and a tion-like ending survive. The recorded difference replaces C's uncertain older isomorph/homéo layers with the retained invo-prefix/whole-word alternatives. The first alternative retains a possibly cancelled invo; involution, bijection and dualité remain whole-word alternatives with the exact lettering and cancellation state open. Convention 4 permits older and live forms at one overwritten position; the difference concerns the retained letter and state alternatives."
    replace_prose("068", old068, new068, 6)
    replace_prose("068", "The correction is represented as one uncertain worked mathematical word, rather than asserting a complete deleted morphism term and a separate complete live term. Its exact property remains unresolved.", "The retained correction alternatives replace C's uncertain older isomorph/homéo layers with possible cancellation of invo or the whole-word alternatives involution, bijection and dualité. Its exact property remains unresolved. Old-before-live encoding alone is not a difference in manuscript positions.", 1)
    replace_prose("068", "Ordinary partial-cancellation notation is used; an additional complete older word is not asserted.", "Ordinary partial-cancellation notation is used for the retained invo-prefix alternative; this is a change in proposed letters and cancellation state, not a positional inference from C's macros.", 1)
    replace_prose("068", "The densely revised anti-compound was inspected because its property matters mathematically. Only one worked suffix is established; neither a complete deleted isomorph/homéo nor a separate certain final word can be asserted. Involution, with possible partial cancellation, remains first among the uncertain candidates.", "The densely revised anti-compound was inspected because its property matters mathematically. The retained alternatives replace C's uncertain older isomorph/homéo layers with possible cancellation of invo and whole-word alternatives. Involution, with possible partial cancellation, remains first among the uncertain candidates. This reading/state difference does not depend on interpreting C's permitted old-before-live notation as separate positions.", 1)
    replace_prose("068", "Three returns differed in representing the worked anti-word; final uses one uncertain partially cancelled word, without inventing an additional unreadable complete substrate.", "Three returns differed in representing the worked anti-word; the final retains uncertain invo-prefix/whole-word alternatives in place of the proposed older isomorph/homéo layers. This concerns the letters and cancellation state, while convention 4 permits old-before-live notation for overprinting.", 1)

    old070 = "One heavily worked d/apostrophe position precedes a reduced une/un continuation. The initial d-like form may be live or cancelled; no second complete d’un or d’une-sized group is visible. A literal two-bar repetition mark follows. The alternatives concern the one prefix’s state, not two sequential whole words."
    new070 = "One heavily worked d/apostrophe position precedes a reduced une/un continuation. The initial d-like form may be live or cancelled. A literal two-bar repetition mark follows. The recorded difference concerns the d' prefix's uncertain cancellation in place of C's proposed older complete d'un layer, with une/un alternatives retained and the literal equals sign resolved. Convention 4 allows the older form before the live form; that notation alone does not assert separate manuscript positions."
    replace_prose("070", old070, new070, 6)

    scope26 = "Folio cancellation and certainty only: the retained reading removes C's outer broad deletion and outer uncertainty while retaining the older-digit 4/3 doubt. The rlap placement alone is formatting under convention 4; old-before-live digit notation does not itself assert a third position. Draft-boundary geometry is D47."
    scope27 = "The difference from C concerns the added Phi-only retracing alternative alongside the retained possible older F layers. The rlap placement alone is formatting under convention 4; old-before-live notation does not itself assert separate positions."
    set_value("071", ("differences", 25, "scope_note"), scope26, expected="Folio identity, two-position overprint and its cancellation state only. Draft-boundary geometry is D47.")
    set_value("071", ("differences", 26, "scope_note"), scope27, missing=True)
    for section, index, scope in (("c_doubts", 12, scope26), ("c_doubts", 14, scope27), ("disputes", 7, scope26), ("disputes", 8, scope27)):
        set_value("071", (section, index, "scope_note"), scope, missing=True)
    replace_prose("071", "Root supersedes all three: only two positions exist, and the broad cancellation begins below the folio.", "Root supersedes the readers' broad folio cancellation because the broad strokes begin below the folio. The retained surface 55 is certain while the underlying 4/3 remains uncertain. Their old-before-live digit notation is permitted by convention 4 and does not itself assert a third position.", 1)

    # Compare all leaves, including missing fields, so no readings, source quotes,
    # flags, crop references, confidence, or any other unlisted value can change.
    changes = []
    for scan in SCANS:
        before = dict(leaves(original[scan]))
        after = dict(leaves(revised[scan]))
        for path in sorted(set(before) | set(after), key=str):
            if path not in before or before[path] != after[path]:
                assert (scan, path) in touched, (scan, path)
                changes.append({"file": str(files[scan].relative_to(ROOT)), "path": list(path), "before_present": path in before, "before": before.get(path), "after": after[path]})
    assert len(changes) == len(touched)

    brief_append = f"\n\n## {date} — administrative clarification of overprint rationale\n\nThe v08 history above described the readers' old-before-new folio notation as three successive digits. That wording is corrected here: convention 4 explicitly permits an overwritten older form to be placed as deleted text immediately before the live form, so the notation itself does not assert three manuscript positions. The retained scan071 D26 difference concerns the folio's broad cancellation and certainty; the `\\rlap` placement alone is formatting. D27 differs by allowing Phi-only retracing, with its `\\rlap` placement also formatting. The related scan065 D017, scan068 D048 and scan070 D027 record prose now identifies the actual letter/state alternatives instead of treating old-before-live macro order as a spatial claim. No page text, final reading, source quotation, flag, count, crop, or ink judgment changed. The original brief files remain unchanged as historical versions. Exact administrative changes and unchanged-file hashes are recorded in `decisions/overprint_record_wording_changes.json`; the retained script is `scripts/review_overprint_record_wording.py`.\n"
    history_before = BRIEF_HISTORY.read_text()
    audit_append = f"\n\n## Administrative clarification applied — {stamp}\n\nRoot authorized a wording-only correction after this candidate audit. The retained script `scripts/review_overprint_record_wording.py` corrected the related evidence, dispute, doubt, consequence and summary copies for scan065 D017, scan068 D048 and scan070 D027; added explicit formatting/substantive scope notes for scan071 D26/D27 and their doubt/dispute copies; and corrected the folio dispute's positional rationale. The scan065 live-word doubt location was renamed to remove its misleading 'following complete word' description. A dated clarification was appended to `brief_changes.md`; the original history paragraph and historical brief files were retained.\n\nThe exact before/after text of every changed JSON leaf is retained in `overprint_record_wording_changes.json`, together with the precise history append and protected-file SHA-256 values. All other JSON leaves were compared and left unchanged. Seven final page files, their seven C source pages, the consolidated transcription and eight historical brief files were hashed before and after and remained byte-identical. No images, compilation, build, finalization or new manuscript judgment occurred.\n"
    audit_before = AUDIT.read_text()

    # Prepare and verify the entire narrow mutation before any writes.
    encoded = {scan: json.dumps(revised[scan], ensure_ascii=False, indent=2) + "\n" for scan in SCANS}
    for scan in SCANS:
        assert json.loads(encoded[scan]) == revised[scan]
        assert files[scan].read_text() == original_text[scan], "Record changed concurrently"
    assert BRIEF_HISTORY.read_text() == history_before
    assert AUDIT.read_text() == audit_before
    for scan in SCANS:
        files[scan].write_text(encoded[scan])
    BRIEF_HISTORY.write_text(history_before + brief_append)
    AUDIT.write_text(audit_before + audit_append)

    after_hashes = {str(p.relative_to(ROOT)): digest(p) for p in protected}
    assert before_hashes == after_hashes, "Protected transcription/source/brief changed"
    for scan in SCANS:
        assert json.loads(files[scan].read_text()) == revised[scan]
    log = {"applied_utc": stamp, "scope": "Administrative prose only; no reading, quotation, flag/count, crop, confidence or ink-judgment changes.", "script": str(Path(__file__).resolve().relative_to(ROOT)), "json_changes": changes, "brief_history_append": brief_append, "audit_append": audit_append, "protected_sha256_before": before_hashes, "protected_sha256_after": after_hashes, "all_protected_files_unchanged": True, "unlisted_json_leaves_unchanged": True, "changed_json_leaf_count": len(changes)}
    LOG.write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n")
    totals = {scan: sum(change["file"].endswith(f"156-4_{scan}.json") for change in changes) for scan in SCANS}
    print(json.dumps({"changed_json_leaves": totals, "total": len(changes), "protected_files_unchanged": len(protected), "log": str(LOG), "brief_history": "dated clarification appended"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
