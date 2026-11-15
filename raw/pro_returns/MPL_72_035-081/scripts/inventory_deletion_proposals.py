#!/usr/bin/env python3
"""Generate reviewed source-to-record deletion mappings; write supporting proposals only."""

from __future__ import annotations

import csv
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True
from inventory_coverage import macro_calls

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent
PREFIX = "MPL_72_035-081"

# These mappings were manually compared with the saved TeX and record descriptions.
# Each entry identifies a combined existing row and the separately marked source calls.
SPLITS = [
    (41, 9, [3, 4], "2; 2"),
    (46, 10, [5, 6], "c_i; +1"),
    (46, 29, [11, 12], "two coefficients"),
    (47, 9, [1, 2], "earlier i_1+ terms"),
    (48, 2, [1, 2, 3, 4], "earlier conditions and coefficient"),
    (48, 34, [14, 15, 16, 17], "lambda zeta_i; repeated condition; index 0; zeta_-1"),
    (49, 20, [5, 6], "interval and J_i notation"),
    (49, 27, [7, 8], "Delta_n(...)=; delta_n(...)=beta_0"),
    (49, 38, [11, 12, 13], "Attention; et une puissance; au moins"),
    (49, 40, [14, 15], "earlier suite notation; J''"),
    (50, 8, [3, 4], "earlier B and alpha terms"),
    (50, 10, [5, 6], "B_3; alpha terms"),
    (50, 15, [9, 10, 11, 12], "earlier factors and alpha_4"),
    (50, 30, [20, 21, 22], "L_2; half delta_n+1; L_3"),
    (50, 34, [24, 25, 26], "1; B_0^2 B_1; 2"),
    (51, 8, [2, 3], "earlier powers and delta_2m fragment"),
    (52, 7, [2, 3], "prime; coefficient 2"),
    (53, 7, [1, 2], "2 and earlier ratio"),
    (53, 10, [3, 4], "two coefficients"),
    (54, 10, [3, 4], "dans; ce qui"),
    (54, 20, [7, 8], "droite; et o'"),
    (54, 30, [11, 12], "précisons; mu"),
    (55, 2, [1, 2], "g identically zero; Alors f(...)=0"),
    (55, 23, [9, 10], "tels; Ceci définit donc"),
]

CHILDREN = [
    (50, 16, [14], "long expanded expression", "Retain the outer cancelled expression; add its separately marked inner +alpha_3 deletion."),
    (50, 19, [16], "final L_4 alpha formula", "Retain the display row; add its separately marked +alpha_0 alpha_3+alpha_2 alpha_3 segment."),
    (61, 2, [1], "cancelled tilde rho_ij=half rho_ij", "The existing margin row already describes the cancelled formula; a deletion child makes its marking separately locatable."),
    (69, 13, [5], "cancelled alpha_0+2", "The existing margin row already describes the cancelled expression; retain that coverage and identify the deletion child."),
    (71, 32, [11], "cancelled 2sigma sigma'-rho sigma", "The existing margin row already describes this cancelled calculation; a deletion child records its marked segment."),
    (74, 9, [1], "deleted dans les fibres", "The existing margin row already names the deleted words; a deletion child records the marking without introducing text."),
    (78, 2, [1], "cancelled s0'=rho s0 tilde; fV(s0')", "One deletion macro encloses both lines already described by this margin row; preserve it as one child, not two."),
]


def markdown_code(value):
    # This is a display convention only. The CSV retains raw source whitespace.
    return "`" + value.replace("`", "ˋ").replace("\n", " ⏎ ").replace("|", "\\|") + "`"


def main():
    scans = sorted({item[0] for item in SPLITS + CHILDREN})
    sources = {}
    for scan in scans:
        record_path = ROOT / "records" / f"scan{scan:03d}.json"
        page_path = ROOT / "pages" / f"{PREFIX}_72_scan{scan:03d}.tex"
        record_bytes, page_bytes = record_path.read_bytes(), page_path.read_bytes()
        sources[scan] = {
            "record": json.loads(record_bytes),
            "deletions": [call for call in macro_calls(page_bytes.decode()) if call["macro"] == "deleted"],
            "record_hash": hashlib.sha256(record_bytes).hexdigest(),
            "page_hash": hashlib.sha256(page_bytes).hexdigest(),
        }
    groups, rows = [], []
    for action, entries in (("split_combined_row", SPLITS), ("add_nested_child", CHILDREN)):
        for entry in entries:
            scan, row_number, call_numbers, expected_content = entry[:4]
            source = sources[scan]
            element = source["record"]["elements"][row_number - 1]
            if element[2] != expected_content:
                raise RuntimeError(f"Record {scan:03d}.{row_number:02d} changed; review the mapping before regenerating")
            reason = (
                "This existing row explicitly groups the listed separately marked source segments. Replace its grouped description with individually located deletion entries."
                if action == "split_combined_row" else entry[4]
            )
            group_id = f"{scan:03d}.{row_number:02d}"
            calls = [source["deletions"][number - 1] for number in call_numbers]
            group = {"scan": scan, "element": group_id, "action": action, "existing_kind": element[0], "position": element[1], "content": element[2], "call_numbers": call_numbers, "calls": calls, "reason": reason}
            groups.append(group)
            for number, call in zip(call_numbers, calls):
                rows.append({
                    "scan": f"{scan:03d}",
                    "existing_element": group_id,
                    "existing_kind": element[0],
                    "existing_position": element[1],
                    "existing_first_words_or_objects": element[2],
                    "proposal": action,
                    "source_call_id": f"{scan:03d}.deleted.{number:03d}",
                    "tex_line": call["line"],
                    "proposed_kind": "deletion",
                    "source_argument": call["argument"],
                    "reason": reason,
                })
    csv_path = OUT / "inventory_deletion_proposals.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    net_split = sum(len(item[2]) - 1 for item in SPLITS)
    child_count = sum(len(item[2]) for item in CHILDREN)
    lines = [
        "# Deletion inventory reconciliation proposals",
        "",
        f"Text/record snapshot: {now}. No image or supplied context was read.",
        "",
        "## Finding",
        "",
        f"The deletion-count differences in the specified scans map to {len(SPLITS)} existing combined deletion rows "
        f"and {child_count} separately marked children inside already listed blocks. Splitting those combined rows gives "
        f"{net_split} additional granular rows; listing the children gives {child_count} more. The proposed structure "
        f"therefore accounts for the 40-call count difference without adding manuscript text.",
        "",
        "The existing inventory already describes most of these source segments in combined form. A count difference "
        "does not establish omitted manuscript content. For the five margin-note parents below, the cancelled text is "
        "explicitly named already; the proposed child row records a second aspect of that same noted material. The primary "
        "transcriber decides the physical element boundaries from the completed image audits. No source or inventory edit "
        "is performed by this report.",
        "",
        "Element IDs refer to the recorded snapshot. Rebuilding the inventory after edits shifts later IDs; use the "
        "recorded position and content as well as the ID. The companion CSV contains all proposed source segments in full, "
        "with original whitespace, and has no `transcribed` or completion-status field.",
        "",
        "## Existing combined deletion rows",
        "",
        "In the evidence column, `D3` means the third `deleted` call in that scan, and `L11` gives its TeX line. "
        "These are source locations, not new manuscript numbering.",
        "",
        "| Existing element | Current description | Separately marked source evidence | Proposal |",
        "|---|---|---|---|",
    ]
    for group in groups:
        if group["action"] != "split_combined_row":
            continue
        evidence = "; ".join(
            f"D{number}, L{call['line']}: {markdown_code(call['argument'])}"
            for number, call in zip(group["call_numbers"], group["calls"])
        )
        lines.append(f"| {group['element']} | {group['content'].replace('|', chr(92)+'|')} | {evidence} | Split into {len(group['calls'])} located deletion rows. |")
    lines.extend([
        "",
        "## Separately marked children within listed blocks",
        "",
        "Retain the existing parent block and add the listed child to make its deletion marking individually addressable. "
        "The five margin parents already contain an explicit description of the cancelled content; they are identified "
        "here as existing coverage, not as absent text.",
        "",
        "| Parent element and kind | Existing coverage | Child source evidence | Proposed treatment |",
        "|---|---|---|---|",
    ])
    for group in groups:
        if group["action"] != "add_nested_child":
            continue
        evidence = "; ".join(
            f"D{number}, L{call['line']}: {markdown_code(call['argument'])}"
            for number, call in zip(group["call_numbers"], group["calls"])
        )
        lines.append(f"| {group['element']} ({group['existing_kind']}) | {group['content']} | {evidence} | {group['reason']} |")
    lines.extend([
        "",
        "## Combined blocks that should remain intact",
        "",
        "- **048.08:** one deletion macro encloses the two endpoint formulas in a single box. The existing row names both; no split is proposed merely because the box contains two formula lines.",
        "- **050.16:** retain the cancelled expanded expression as its own outer deletion element. The inner `+\\alpha_3` is a separately encoded child; the outer element is not replaced by that child.",
        "- **050.37:** one deletion macro encloses a determinant and its expansion. The existing description covers that block; no extra row is proposed for every equality inside it.",
        "- **051.03:** the cancelled even-case heading, congruence, and unfinished expression occur within one outer deletion macro. The existing row describes that block.",
        "- **055.20:** retain the whole cancelled paragraph. Its inner `tels` and `Ceci définit donc` are already grouped in 055.23; split that child row into two, retaining the outer row.",
        "- **078.02:** the two lines of the cancelled marginal calculation are enclosed by one deletion macro. The proposed child remains one deletion entry.",
        "",
        "## Source fingerprints",
        "",
        "These fingerprints identify the mapping snapshot and make no freeze claim.",
        "",
        "| Scan | Page SHA-256 | Record SHA-256 |",
        "|---|---|---|",
    ])
    for scan, source in sorted(sources.items()):
        lines.append(f"| {scan:03d} | `{source['page_hash']}` | `{source['record_hash']}` |")
    path = OUT / "inventory_deletion_proposals.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"markdown": str(path), "csv": str(csv_path), "combined_rows_to_split": len(SPLITS), "net_rows_from_splits": net_split, "child_rows": child_count, "proposed_detail_rows": len(rows)}, indent=2))


if __name__ == "__main__":
    main()
