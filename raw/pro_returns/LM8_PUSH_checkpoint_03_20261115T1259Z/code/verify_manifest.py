"""Check the supplied archive against its own manifest; no network access."""
import csv
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[2] / "background"
rows = list(csv.DictReader((root / "MANIFEST.tsv").open(), delimiter="\t"))
checks = []
for row in rows:
    path = root / row["path_in_zip"]
    data = path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    checks.append({"path": row["path_in_zip"], "bytes_ok": len(data) == int(row["bytes"]),
                   "sha256_ok": digest == row["sha256"], "actual_sha256": digest})
listed = {row["path_in_zip"] for row in rows}
unlisted = sorted(str(p.relative_to(root)) for p in root.rglob("*")
                  if p.is_file() and str(p.relative_to(root)) not in listed
                  and p.name != "MANIFEST.tsv")
result = {"manifest_rows": len(rows), "valid_rows": sum(c["bytes_ok"] and c["sha256_ok"] for c in checks),
          "unlisted_files": unlisted, "checks": checks}
print(json.dumps(result, indent=2))
assert all(c["bytes_ok"] and c["sha256_ok"] for c in checks)
