#!/usr/bin/env python3
"""Validate and aggregate actual, explicitly recorded visual inspections.

This checks hashes and coverage. It does not perform or infer visual inspection.
The four reviewer records contain the observations made after viewing images.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize(record):
    if "viewed_assets" in record:
        return record["viewed_assets"]
    if "sheets" in record:
        return [dict(path=a["contact_sheet"], sha256=a["contact_sha256"],
                     pages=a["visually_viewed_printed_pages"], inspection="contact_sheet")
                for a in record["sheets"]] + [
            dict(path=a["image"], sha256=a["image_sha256"],
                 pages=[a["visually_viewed_printed_page"]], inspection="full_resolution_page")
            for a in record["individual_pages"]]
    return [dict(path=a["file"], sha256=a["sha256"], pages=a["pages"],
                 inspection="contact_sheet") for a in record["contact_sheets"]] + [
        dict(path=a["file"], sha256=a["sha256"], pages=[a["page"]],
             inspection="full_resolution_page") for a in record["full_resolution"]]


def main():
    metadata_path = ROOT / "code/PDF_layout_audit_output.json"
    metadata = json.loads(metadata_path.read_text())
    pdf_hash = digest(ROOT / "ANABELIAN_149_PUSH_paper.pdf")
    assert pdf_hash == metadata["pdf_sha256"]
    assert metadata["pages"] == 365
    reviewed, contact_pages, full_pages, sheets = set(), set(), set(), set()
    records, all_assets = [], []
    for reviewer in ["root", "finite_field", "degeneration", "topos"]:
        relative = f"audit/typesetting_review_365pages_{reviewer}.json"
        record = json.loads((ROOT / relative).read_text())
        assert record["pdf_sha256"] == pdf_hash, relative
        assets = normalize(record)
        own_pages = set()
        for asset in assets:
            assert digest(ROOT / asset["path"]) == asset["sha256"], asset["path"]
            own_pages.update(asset["pages"])
            reviewed.update(asset["pages"])
            if asset["inspection"] == "contact_sheet":
                sheets.add(asset["path"])
                contact_pages.update(asset["pages"])
                number = int(Path(asset["path"]).stem.rsplit("_", 1)[1])
                assert asset["pages"] == metadata["rendered_pages"][(number-1)*9:number*9]
            else:
                full_pages.update(asset["pages"])
            all_assets.append(dict(reviewer=reviewer, **asset))
        records.append(dict(reviewer=reviewer, record=relative,
                            record_sha256=digest(ROOT/relative),
                            unique_page_count=len(own_pages), pages=sorted(own_pages)))
    assert sheets == set(metadata["contact_sheets"])
    assert contact_pages == set(metadata["rendered_pages"])
    assert reviewed == set(metadata["rendered_pages"])
    assert len(reviewed) == 190
    assert len(full_pages) == 16
    result = dict(status="PASS for the explicitly reviewed sample",
                  pdf="ANABELIAN_149_PUSH_paper.pdf", pdf_sha256=pdf_hash,
                  document_pages=365, visually_reviewed_page_count=len(reviewed),
                  visually_reviewed_pages=sorted(reviewed),
                  contact_sheet_count=len(sheets),
                  full_resolution_page_count=len(full_pages),
                  full_resolution_pages=sorted(full_pages),
                  reviewer_records=records, verified_viewed_assets=all_assets,
                  all_record_and_image_hashes_verified=True,
                  limitations="190 of 365 physical pages were actually viewed at contact-sheet scale; the listed 16 were additionally viewed individually at full rendered resolution. The audit does not claim visual inspection of the remaining 175 pages or external human peer review. Rendering and log checks alone are not visual inspection.")
    output = ROOT / "audit/typesetting_review_365pages.json"
    output.write_text(json.dumps(result, indent=2)+"\n")
    metadata.update(visually_reviewed_pages=sorted(reviewed),
                    full_resolution_reviewed_pages=sorted(full_pages),
                    review_status=result["status"],
                    review_record=str(output.relative_to(ROOT)))
    metadata_path.write_text(json.dumps(metadata, indent=2)+"\n")
    print(json.dumps({k: result[k] for k in ["status", "pdf_sha256",
                     "document_pages", "visually_reviewed_page_count",
                     "contact_sheet_count", "full_resolution_page_count",
                     "full_resolution_pages"]}, indent=2))


if __name__ == "__main__":
    main()
