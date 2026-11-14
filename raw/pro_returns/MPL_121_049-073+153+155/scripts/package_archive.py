"""Package the canonical deliverables and supporting records, excluding source images."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "MPL_121_049-073+153+155"
root_files = [
    f"{PREFIX}_transcription.tex", f"{PREFIX}_doubts.md",
    f"{PREFIX}_inventory.csv", f"{PREFIX}_notes.md",
    "progress.log", "freeze_manifest.json", "pre_freeze_verification.json",
    "final_verification.json", "audit_records.jsonl", "notation_records.jsonl",
    "doubt_records.jsonl", "tex_validation.json", "validation_history.jsonl",
    "checkpoint_receipts.jsonl",
]
scripts = ["record_page.py", "audit_page.py", "validate_tex.py", "build_doubts.py",
           "doubts_header.txt", "search_note_context.py", "verify_final.py", "package_archive.py"]
research = ["context_search_log.jsonl", "source_verification.md", "image_evidence_manifest.json"]
files = [ROOT/f for f in root_files] + sorted((ROOT/"pages").glob("*.tex"))
files += [ROOT/"scripts"/f for f in scripts] + [ROOT/"research"/f for f in research]
assert all(p.is_file() for p in files)
manifest = {
    "canonical_deliverables": root_files[:5] + ["pages/ (44 page fragments)"],
    "omissions": [
        "Supplied scan and context archives and their extracted sources",
        "Externally retrieved research facsimiles, PDFs, and machine search leads",
        "Superseded integration drafts, assembly inputs, and interpreter caches",
    ],
    "files": [{"path": str(p.relative_to(ROOT)), "bytes": p.stat().st_size,
               "sha256": hashlib.sha256(p.read_bytes()).hexdigest()} for p in files],
}
manifest_path = ROOT/"archive_manifest.json"
manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+"\n")
files.append(manifest_path)
out = ROOT.parent/f"{PREFIX}.zip"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for p in files:
        z.write(p, str(p.relative_to(ROOT)))
with zipfile.ZipFile(out) as z:
    assert z.testzip() is None
    assert len(z.namelist()) == len(set(z.namelist())) == len(files)
    assert len([n for n in z.namelist() if n.startswith("pages/") and n.endswith(".tex")]) == 44
    assert not any(n.lower().endswith((".jpg",".jpeg",".png",".pdf")) for n in z.namelist())
    for entry in manifest["files"]:
        assert hashlib.sha256(z.read(entry["path"])).hexdigest() == entry["sha256"]
print(json.dumps({"path":str(out),"files":len(files),"bytes":out.stat().st_size,
                  "sha256":hashlib.sha256(out.read_bytes()).hexdigest(),
                  "zip_crc_check":"passed","manifest_hashes":"passed"}))
