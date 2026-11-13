"""Append explicitly authored observations of images actually viewed by root.

This helper supplies identifiers and verifies prepared evidence hashes only.
It neither inspects images nor generates a visual assessment.
"""
import hashlib
import json
from pathlib import Path


def record(book, rows, revision=578, kind="final_candidates"):
    queue = json.loads(Path("work/data/pagination_final_queues", book + ".json").read_text())
    target = Path(f"work/data/pagination_final_{book}_root{revision}_observations.json")
    output = json.loads(target.read_text()) if target.exists() else []
    for index, tag_page, display_pages, note, *status_override in rows:
        item = queue[kind][index]
        assert item["id"] not in {row["id"] for row in output}, item["id"]
        assert note.strip() and display_pages
        images = [im for im in item["images"] if kind != "known_detachments" or im.get("page") in {tag_page, *display_pages}]
        assert images
        for image in images:
            assert hashlib.sha256(Path(image["path"]).read_bytes()).hexdigest() == image["sha256"]
        status = status_override[0] if status_override else (
            "RESOLVED_ON_FINAL_PDF" if kind == "known_detachments" else "CLEARED_ON_FINAL_PDF"
        )
        output.append({
            "id": item["id"], "reader": book, "pdf_sha256": queue["pdf_sha256"],
            "status": status, "reviewer": "assistant/root", "observation": note,
            "tag_page": tag_page, "display_pages": display_pages, "images": images,
        })
    target.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    print(book, "actual observations:", len(output))


def record_headings(book, rows, target_name):
    queue = json.loads(Path("work/data/generated_heading_final_queues", book + ".json").read_text())
    target = Path("work/data", target_name)
    output = json.loads(target.read_text()) if target.exists() else []
    for index, page, note in rows:
        item = queue["known_witnesses"][index]
        assert item["id"] not in {row["id"] for row in output}, item["id"]
        images = [im for im in item["images"] if im.get("page") == page]
        assert note.strip() and images
        for image in images:
            assert hashlib.sha256(Path(image["path"]).read_bytes()).hexdigest() == image["sha256"]
        row = {key: item[key] for key in ("id", "reader", "heading_kind", "cote", "scan", "package")}
        row.update(pdf_sha256=queue["pdf_sha256"], status="RESOLVED_ON_FINAL_PDF",
                   reviewer="assistant/root", observation=note, heading_page=page,
                   first_content_page=page, rule_page=page, images=images)
        output.append(row)
    target.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    print(book, "actual heading observations:", len(output))
