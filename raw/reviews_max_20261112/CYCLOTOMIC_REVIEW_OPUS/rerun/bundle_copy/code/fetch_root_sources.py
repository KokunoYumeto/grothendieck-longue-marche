"""Retrieve primary sources used by the root contribution and record checksums.

Downloaded source PDFs remain outside the deliverable.  Run from the workspace.
The output records successful retrieval, not a claim that every page was read.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / "source_text" / "root_sources"
DEST.mkdir(parents=True, exist_ok=True)
SOURCES = {
    "esnault_hai_published": "https://page.mi.fu-berlin.de/esnault/preprints/helene/86-Grothendieck.pdf",
    "bresciani_2021": "https://content.algebraicgeometry.nl/2021-2/2021-2-005.pdf",
    "ihara_kaneko_yukinari": "https://www2.math.kyushu-u.ac.jp/~mkaneko/papers/02properties_universal.pdf",
    "nakamura_2019": "https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/2120-09.pdf",
}

records = []
for name, url in SOURCES.items():
    path = DEST / f"{name}.pdf"
    try:
        if not path.exists():
            req = urllib.request.Request(url, headers={"User-Agent": "Mathematical source verification"})
            with urllib.request.urlopen(req, timeout=45) as response:
                path.write_bytes(response.read())
        data = path.read_bytes()
        assert data.startswith(b"%PDF"), "Retrieved file is not a PDF"
        subprocess.run(["pdftotext", "-layout", str(path), str(path.with_suffix(".txt"))], check=True)
        records.append({"source": name, "url": url, "bytes": len(data),
                        "sha256": hashlib.sha256(data).hexdigest(), "retrieved": True})
    except Exception as exc:
        records.append({"source": name, "url": url, "retrieved": False, "error": str(exc)})

result = json.dumps(records, indent=2)
(Path(__file__).parent / "fetch_root_sources_output.json").write_text(result + "\n")
print(result)
