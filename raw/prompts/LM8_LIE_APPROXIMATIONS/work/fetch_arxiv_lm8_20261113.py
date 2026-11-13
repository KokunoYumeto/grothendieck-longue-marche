"""Fetch the arXiv e-print (LaTeX source) of every arXiv paper attached as a PDF to the S6 zips (13 Nov 2026; user's
rule: LaTeX wherever it exists, not PDFs). Each source goes into its own new folder literature/arXiv_src/<id>/
(untrusted data: tar 'data' filter, never executed). Prints, per id, how many .tex files it holds.
usage: python -I -B fetch_arxiv_sources_20261113.py ID [ID ...]   (ids like 2609.38442, 1904.11179v2, math/9607215)"""
import gzip
import io
import sys
import tarfile
import time
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
OUT = Path(r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\literature\arXiv_src")
OUT.mkdir(parents=True, exist_ok=True)
for aid in sys.argv[1:]:
    dest = OUT / aid.replace("/", "_")
    if dest.exists():
        print(aid, "already there:", len(list(dest.rglob("*.tex"))), "tex")
        continue
    req = urllib.request.Request("https://arxiv.org/e-print/" + aid, headers={"User-Agent": "research-map-script/1.0"})
    try:
        blob = urllib.request.urlopen(req, timeout=120).read()
    except Exception as e:  # noqa: BLE001
        print(aid, "FAILED", e)
        continue
    time.sleep(3)
    dest.mkdir(parents=True)
    data = gzip.decompress(blob) if blob[:2] == b"\x1f\x8b" else blob
    if data[:5] == b"%PDF-":
        (dest / "PDF_ONLY.txt").write_text("arXiv has no source for this paper; keep the PDF\n", encoding="utf-8")
        print(aid, "PDF only (no source on arXiv)")
        continue
    try:
        with tarfile.open(fileobj=io.BytesIO(data)) as t:
            t.extractall(dest, filter="data")
    except tarfile.ReadError:
        (dest / "main.tex").write_bytes(data)
    texs = list(dest.rglob("*.tex"))
    print(aid, len(blob), "bytes;", len(texs), "tex:", ", ".join(p.name for p in texs[:5]))
