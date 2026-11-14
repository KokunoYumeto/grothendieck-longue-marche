"""Render the changed proof and status pages for actual visual inspection.

This program records rendering and hashes only. It makes no claim that the
images have been inspected; the separate visual review records that action.
"""
from pathlib import Path
import hashlib
import json
import subprocess

BASE = Path(__file__).resolve().parents[1]
PDF = BASE / "LM7_FERMAT_TOWER_paper.pdf"
QA = BASE / "qa"
PAGES = sorted({1, 2, 42, 46, 51, 55, 262, 267, 270, 721, 728,
                *range(242, 250), *range(710, 718)})


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    assert sha(PDF) == "66def8ecc7e237f7969b07911264e933c496191cff6aa7b39c19463808e7774a"
    images = []
    for page in PAGES:
        prefix = QA / f"detail226_{page:03d}"
        result = subprocess.run(
            ["pdftoppm", "-f", str(page), "-l", str(page), "-singlefile",
             "-r", "110", "-jpeg", "-jpegopt", "quality=93", str(PDF), str(prefix)],
            capture_output=True, check=True)
        assert not result.stdout
        assert not result.stderr, result.stderr.decode()
        path = prefix.with_suffix(".jpg")
        images.append({"page": page, "path": str(path.relative_to(BASE)),
                       "bytes": path.stat().st_size, "sha256": sha(path)})
    record = {"pdf": PDF.name, "pdf_sha256": sha(PDF), "dpi": 110,
              "renderer": "pdftoppm", "images": images,
              "visual_review_claimed_by_program": False}
    (QA / "detail226_manifest.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
