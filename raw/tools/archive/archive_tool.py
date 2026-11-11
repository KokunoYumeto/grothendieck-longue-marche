"""Grothendieck's mathematical archive at the University of Montpellier (grothendieck.umontpellier.fr), the open part
("Archives en accès libre"): index the listing page, download every cote into folders by the archive's own topics,
and report the state. User, 10 Nov 2026: "Download it, organize it on topic", "download fucking everything".

usage:
  python -I archive_tool.py index LISTING.html   writes MANIFEST.json / MANIFEST.csv (and keeps a copy of the listing)
  python -I archive_tool.py download            downloads every missing cote, one at a time, resumable; logs each file
  python -I archive_tool.py status              counts present / missing files, bytes and PDF pages per topic

Archive folder: C:\\Users\\user\\Documents\\grothendieck_archive_montpellier (only downloaded data there)."""
import csv
import hashlib
import html
import json
import pathlib
import re
import shutil
import subprocess
import sys
import time
import unicodedata
import urllib.error
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(r"C:\Users\user\Documents\grothendieck_archive_montpellier")
BASE = "https://grothendieck.umontpellier.fr/"
UA = "Mozilla/5.0 (research client)"
SEC = re.compile(r'<div class="cotelink title[^"]*" data-target="([^"]*)">\s*<div class="date[^"]*">(.*?)</div>\s*'
                 r'<div class="titrewrapper[^"]*">\s*<p class="ptitre"(?: style="padding-left:\s*(\d+)px")?>(.*?)</p>', re.S)
COTE = re.compile(r'<div id="cote-([^"]+)" class="cote">(.*?)</a>\s*</div>', re.S)
NOTE = re.compile(r"<div><sup>(\d+)</sup>(.*?)</div>", re.S)


def clean(s):
    s = re.sub(r"<sup>(\d+)</sup>", r"[\1]", s or "")
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"<!--.*?-->", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def nofn(s):
    return re.sub(r"\s*\[\d+\]", "", s).strip()


def slug(s):
    s = unicodedata.normalize("NFKD", nofn(s)).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_").lower()[:50]


def index(listing):
    t = pathlib.Path(listing).read_text(encoding="utf-8", errors="replace")
    notes = {int(n): clean(x) for n, x in NOTE.findall(t)}
    items = [(m.start(), "sec", m) for m in SEC.finditer(t)] + [(m.start(), "cote", m) for m in COTE.finditer(t)]
    items.sort(key=lambda x: x[0])
    stack, rows, top = [], [], 0
    for _, kind, m in items:
        if kind == "sec":
            pad = int(m.group(3) or 0)
            while stack and stack[-1]["pad"] >= pad:
                stack.pop()
            if not stack:
                top += 1
            stack.append(dict(pad=pad, title=nofn(clean(m.group(4))), date=clean(m.group(2)), range=m.group(1), top=top))
            continue
        cid, body = m.group(1), m.group(2)
        src = re.search(r'data-src="([^"]*)"', body)
        date = re.search(r'<div class="date[^"]*">(.*?)</div>', body, re.S)
        tit = re.search(r'<p class="ptitre"(?: style="padding-left:\s*(\d+)px")?>(.*?)</p>', body, re.S)
        nb = re.search(r'<div class="nbpages[^"]*">(.*?)</div>', body, re.S)
        pad = int(tit.group(1) or 0) if tit else 0
        while stack and stack[-1]["pad"] >= pad:
            stack.pop()
        if not stack:
            top += 1
            path = [nofn(clean(tit.group(2))).split(" : ")[0][:60] if tit else "cote " + cid]
            ti = top
        else:
            path = [s["title"] for s in stack]
            ti = stack[0]["top"]
        f = None
        if src:
            mm = re.search(r"file=\.\./([^&\"]+\.pdf)", src.group(1))
            f = mm.group(1) if mm else None
        nbt = clean(nb.group(1)) if nb else ""
        pg = re.search(r"\((\d+)\s*p\.\)", nbt)
        refs = [int(x) for x in re.findall(r"<sup>(\d+)</sup>", (date.group(1) if date else "") + (tit.group(2) if tit else ""))]
        rows.append(dict(order=len(rows) + 1, cote=cid, file=f, url=(BASE + f) if f else None,
                         date=clean(date.group(1)) if date else "", title=clean(tit.group(2)) if tit else "",
                         pages_site=int(pg.group(1)) if pg else None, topic=path[0], subtopic=" / ".join(path[1:]),
                         folder=f"{ti:02d}_{slug(path[0])}", notes=[notes[r] for r in refs if r in notes]))
    ROOT.mkdir(parents=True, exist_ok=True)
    (ROOT / "source").mkdir(exist_ok=True)
    shutil.copy2(listing, ROOT / "source" / "archives-grothendieck_listing_20261110.html")
    (ROOT / "MANIFEST.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    with open(ROOT / "MANIFEST.csv", "w", encoding="utf-8", newline="") as g:
        w = csv.writer(g)
        w.writerow(["order", "cote", "topic", "subtopic", "date", "title", "pages_site", "file", "url", "folder"])
        for r in rows:
            w.writerow([r["order"], r["cote"], r["topic"], r["subtopic"], r["date"], r["title"], r["pages_site"],
                        r["file"], r["url"], r["folder"]])
    tops = {}
    for r in rows:
        k = (r["folder"], r["topic"])
        a = tops.setdefault(k, [0, 0, 0, []])
        a[0] += 1
        a[1] += r["pages_site"] or 0
        a[2] += 1 if r["url"] else 0
        a[3].append(r["cote"])
    for (fo, tp), (n, p, u, cs) in sorted(tops.items()):
        print(f"{fo:40s} cotes {n:3d} online {u:3d} pages {p:5d}  [{cs[0]} .. {cs[-1]}]")
    print("rows", len(rows), "online", sum(1 for r in rows if r["url"]), "pages (site)", sum(r["pages_site"] or 0 for r in rows))


def pdfpages(p):
    try:
        out = subprocess.run(["pdfinfo", str(p)], capture_output=True, text=True, timeout=120).stdout
        m = re.search(r"Pages:\s+(\d+)", out)
        return int(m.group(1)) if m else None
    except Exception:
        return None


def download():
    rows = json.loads((ROOT / "MANIFEST.json").read_text(encoding="utf-8"))
    # Optional DOWNLOAD_PRIORITY.txt (cotes separated by spaces or newlines): these come first, in that order; an
    # entry without a dash also covers its sub-files ("156" covers 156-1 ...). The rest keep the manifest order.
    prio = ROOT / "DOWNLOAD_PRIORITY.txt"
    if prio.exists():
        order = prio.read_text(encoding="utf-8").split()

        def rank(c):
            for i, e in enumerate(order):
                if c == e or ("-" not in e and c.startswith(e + "-")):
                    return i
            return len(order)
        rows.sort(key=lambda r: rank(r["cote"]))
    log = ROOT / "DOWNLOAD_LOG.jsonl"
    old = ROOT / "cote_134_modelizing_story"
    for r in rows:
        if not r["url"]:
            continue
        d = ROOT / r["folder"]
        d.mkdir(exist_ok=True)
        dest = d / r["file"]
        if dest.exists() and pdfpages(dest):
            continue
        if (old / r["file"]).exists() and pdfpages(old / r["file"]):
            shutil.move(str(old / r["file"]), str(dest))
            how = "moved from cote_134_modelizing_story"
        else:
            part = dest.with_suffix(".pdf.part")
            ok = False
            for attempt in range(6):
                try:
                    have = part.stat().st_size if part.exists() else 0
                    hdr = {"User-Agent": UA}
                    if have:
                        hdr["Range"] = f"bytes={have}-"  # resume a partial file (the server answers 206)
                    req = urllib.request.Request(r["url"], headers=hdr)
                    with urllib.request.urlopen(req, timeout=600) as resp:
                        mode = "ab" if have and resp.status == 206 else "wb"
                        with open(part, mode) as g:
                            while True:
                                b = resp.read(1 << 20)
                                if not b:
                                    break
                                g.write(b)
                    if pdfpages(part):
                        ok = True
                        break
                except urllib.error.HTTPError as e:
                    if e.code == 416 and pdfpages(part):  # the partial file was already complete
                        ok = True
                        break
                    print(r["cote"], "attempt", attempt + 1, "failed:", e, flush=True)
                except Exception as e:
                    print(r["cote"], "attempt", attempt + 1, "failed:", e, flush=True)
                time.sleep(10 * (attempt + 1))
            if not ok:
                print(r["cote"], "FAILED", flush=True)
                with open(log, "a", encoding="utf-8") as g:
                    g.write(json.dumps(dict(cote=r["cote"], url=r["url"], status="failed"), ensure_ascii=False) + "\n")
                continue
            part.replace(dest)
            how = "downloaded"
            time.sleep(2)
        h = hashlib.sha256(dest.read_bytes()).hexdigest()
        rec = dict(cote=r["cote"], file=str(dest.relative_to(ROOT)), bytes=dest.stat().st_size, pdf_pages=pdfpages(dest),
                   pages_site=r["pages_site"], sha256=h, how=how, url=r["url"], at=time.strftime("%Y-%m-%dT%H:%M:%S"))
        with open(log, "a", encoding="utf-8") as g:
            g.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(rec["cote"], rec["bytes"], "bytes", rec["pdf_pages"], "pages", how, flush=True)
    if old.exists() and not any(old.iterdir()):
        old.rmdir()
    print("download pass finished", flush=True)


def status():
    rows = json.loads((ROOT / "MANIFEST.json").read_text(encoding="utf-8"))
    have = miss = by = 0
    for r in rows:
        if not r["url"]:
            continue
        p = ROOT / r["folder"] / r["file"]
        if p.exists():
            have += 1
            by += p.stat().st_size
        else:
            miss += 1
    print("present", have, "missing", miss, "GB", round(by / 1e9, 2))


if __name__ == "__main__":
    {"index": lambda: index(sys.argv[2]), "download": download, "status": status}[sys.argv[1]]()
