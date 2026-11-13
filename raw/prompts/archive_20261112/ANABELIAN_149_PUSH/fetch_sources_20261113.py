"""Fetch the sources of ANABELIAN_149_PUSH and of the LM6 zip that were not local (13 Nov 2026, Claude Fable 5.2).
arXiv papers as LaTeX e-prints (https://arxiv.org/e-print/<id>), each unpacked into its own new folder with tarfile
filter="data"; PDFs only where no source exists. Nothing fetched is executed. Writes FETCH_LOG.tsv in the target folder.
usage: python -I -B fetch_sources_20261113.py"""
import gzip
import hashlib
import io
import sys
import tarfile
import time
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
OUT = Path(r"C:\Users") / ("Flo" + "ris") / "Documents" / "Free or receipted" / "free" / "anabelian-149-20261113"
SRC = OUT / "arXiv_src"
UA = {"User-Agent": "paper-fetch/1.0"}
# id -> what it is (titles and authors confirmed on export.arxiv.org/api, 13 Nov 2026)
ANA = {
    "1203.3236": "Stix, On the birational section conjecture with local conditions",
    "math/0305226": "Koenigsmann, On the 'Section Conjecture' in anabelian geometry",
    "2108.13397": "Bresciani, On the birational section conjecture with strong birationality assumptions",
    "math/0701680": "Bertin-Romagny, Champs de Hurwitz",
    "math/0503247": "Noohi, Foundations of Topological Stacks I",
    "1705.03034": "Dupuy-Rabinoff, A rigid analytic proof that the Abel-Jacobi map extends to compact-type models",
    "1005.1302": "Harari-Stix, Descent obstruction and fundamental exact sequence",
    "math/0606465": "Stoll, Finite descent obstructions and rational points on curves",
    "0801.1452": "Saidi-Tamagawa, A prime-to-p version of the Grothendieck anabelian conjecture (finite fields)",
    "1301.4429": "Borne-Emsalem-Stix, Lifting Galois sections along torsors",
    "1804.07176": "Bresciani, Some implications between Grothendieck's anabelian conjectures",
}
LM6 = ["1303.4812", "1308.3864", "math/0512352", "2012.06278", "2611.09080", "2603.02848", "2605.02577", "math/0703877",
       "2510.13325", "2608.21232", "2610.24986", "2604.26131", "1111.1354", "2607.27746", "2507.13701", "2602.17746", "0802.4125"]
PDFS = {
    "andreatta_iovita_kim_2015_core187927532.pdf": "https://core.ac.uk/download/187927532.pdf",
    "asada_matsumoto_oda_core39215208.pdf": "https://core.ac.uk/download/39215208.pdf",
}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read(), r.headers.get("Content-Type", ""), r.geturl()


log = []
SRC.mkdir(parents=True, exist_ok=True)
for aid in list(ANA) + LM6:
    folder = SRC / aid.replace("/", "_")
    if folder.exists() and any(folder.iterdir()):
        print("have", aid)
        continue
    try:
        b, ctype, final = get("https://arxiv.org/e-print/" + aid)
    except Exception as e:  # noqa: BLE001
        print("FAILED", aid, repr(e)[:120])
        log.append((aid, "FAILED " + repr(e)[:80], 0, "", ""))
        time.sleep(4)
        continue
    sha = hashlib.sha256(b).hexdigest()
    folder.mkdir(parents=True, exist_ok=False)
    kind = ""
    if b[:4] == b"%PDF":
        kind = "PDF only (no source on arXiv)"
        (folder / "eprint.pdf").write_bytes(b)
    elif b[:2] == b"\x1f\x8b":
        raw = gzip.decompress(b)
        try:
            with tarfile.open(fileobj=io.BytesIO(raw)) as t:
                t.extractall(folder, filter="data")
            kind = "tar: %d files" % sum(1 for p in folder.rglob("*") if p.is_file())
        except tarfile.ReadError:
            if raw[:4] == b"%PDF":
                kind = "PDF only (gzipped)"
                (folder / "eprint.pdf").write_bytes(raw)
            else:
                kind = "single TeX file"
                (folder / "main.tex").write_bytes(raw)
    else:
        try:
            with tarfile.open(fileobj=io.BytesIO(b)) as t:
                t.extractall(folder, filter="data")
            kind = "plain tar: %d files" % sum(1 for p in folder.rglob("*") if p.is_file())
        except tarfile.ReadError:
            kind = "unknown type " + ctype
            (folder / "eprint.bin").write_bytes(b)
    ntex = sum(1 for p in folder.rglob("*.tex")) + sum(1 for p in folder.rglob("*.TEX"))
    print("%-13s %8d bytes  %s  tex files: %d  %s" % (aid, len(b), kind, ntex, ANA.get(aid, "")[:50]))
    log.append((aid, kind, len(b), sha, "https://arxiv.org/e-print/" + aid))
    time.sleep(4)
for name, url in PDFS.items():
    dst = OUT / name[:-4] / name
    if dst.exists():
        print("have", name)
        continue
    try:
        b, ctype, final = get(url)
    except Exception as e:  # noqa: BLE001
        print("FAILED", name, repr(e)[:120])
        log.append((name, "FAILED " + repr(e)[:80], 0, "", url))
        continue
    if b[:4] != b"%PDF":
        print("NOT A PDF", name, ctype, b[:60])
        log.append((name, "not a PDF: " + ctype, len(b), "", url))
        continue
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(b)
    print("%-45s %8d bytes  %s" % (name, len(b), final[:60]))
    log.append((name, "PDF", len(b), hashlib.sha256(b).hexdigest(), url))
    time.sleep(4)
new = not (OUT / "FETCH_LOG.tsv").exists()
with open(OUT / "FETCH_LOG.tsv", "a", encoding="utf-8") as fh:
    if new:
        fh.write("item\tkind\tbytes\tsha256\turl\n")
    for r in log:
        fh.write("\t".join(str(x) for x in r) + "\n")
print("logged", len(log))
