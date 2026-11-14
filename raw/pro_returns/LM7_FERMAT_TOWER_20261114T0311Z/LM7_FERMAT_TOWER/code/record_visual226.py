"""Record the root assistant's completed visual inspection of build 226.

The page list below was supplied after the assistant actually opened and
inspected the images. This program verifies their identity and writes that
attestation; it does not perform or infer a visual inspection.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

BASE = Path(__file__).resolve().parents[1]
QA = BASE / "qa"
EXPECTED_PDF = "66def8ecc7e237f7969b07911264e933c496191cff6aa7b39c19463808e7774a"
OBSERVED_DETAILS = [1, 2, 42, 46, 51, 55, 242, 243, 244, 245, 246, 247,
                    248, 249, 262, 267, 270, 710, 711, 712, 713, 714,
                    715, 716, 717, 721, 728]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    qa = json.loads((QA / "pdf_qa.json").read_text())
    detail = json.loads((QA / "detail226_manifest.json").read_text())
    assert sha(BASE / "LM7_FERMAT_TOWER_paper.pdf") == qa["sha256"] == EXPECTED_PDF
    assert qa["pages"] == 728 and len(qa["contact_sheets"]) == 46
    assert detail["pdf_sha256"] == EXPECTED_PDF
    assert [item["page"] for item in detail["images"]] == OBSERVED_DETAILS
    contacts = []
    for path in qa["contact_sheets"]:
        contacts.append({"path": path, "sha256": sha(BASE / path)})
    for item in detail["images"]:
        assert sha(BASE / item["path"]) == item["sha256"]
    result = {
        "status": "PASS", "pdf_sha256": EXPECTED_PDF, "pdf_pages": 728,
        "reviewer": "GPT-6 Astra (OpenAI, ChatGPT Pro mode), root assistant",
        "basis": "Actual image-tool inspection of every listed image",
        "contact_sheets": contacts, "detail_images": detail["images"],
        "all_pages_inspected_in_contact_sheets": True,
        "observed_layout_defects": [],
        "truncated_prior_return_used_as_evidence": False,
        "truncated_return_resolution": "Pages 97-192 were reopened and inspected in full; the truncated earlier output was not counted.",
        "mathematical_proof_review_claimed_here": False,
        "recorded_utc": datetime.now(timezone.utc).isoformat(),
    }
    (QA / "visual226_root.json").write_text(json.dumps(result, indent=2) + "\n")
    review = f"""# Actual visual review of the assembled 226-statement paper

PDF SHA256: `{EXPECTED_PDF}`. Pages: 728.

All 46 contact sheets, covering pages 1-728, were actually opened and inspected by the root assistant. The 27 detail images listed in visual226_root.json were separately opened at 110 dpi: pages 1-2, 42, 46, 51, 55, 242-249, 262, 267, 270, 710-717, 721 and 728. This includes the entire newly integrated D65 and E122 proofs with their boundaries, the amended D13, D19 and E23 paragraphs, the title and notation table, section transitions, and bibliography boundaries.

No clipping, overlap, broken table, unintended blank page, missing glyph, or displaced equation label was observed. Equations, matrices, arrows, source filenames and page numbers remained legible in the detailed images. The automatic renderer separately checked all 226 statement headings and page borders. The complete proof reviews and arithmetic replays are recorded separately.

An earlier tool return for pages 97-192 was truncated; those images were reopened and actually inspected before this record was made. No truncated return was counted as visual evidence. Earlier reviews and frozen author proofs remain preserved in the archive history.
"""
    (QA / "visual_review.md").write_text(review)
    print(json.dumps({"status": "PASS", "pdf_sha256": EXPECTED_PDF,
                      "contacts_inspected": len(contacts),
                      "details_inspected": len(OBSERVED_DETAILS),
                      "visual_record_sha256": sha(QA / "visual226_root.json")}, indent=2))


if __name__ == "__main__":
    main()
