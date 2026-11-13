"""Typed-text score per page for the next Codex-web batch (13 Nov 2026): every page of cotes 27, 29, 32, 35, 36, 45, 46
and 123 is rendered at 100 dpi and read by Tesseract (eng); the score is the number of words of 3+ letters read with
confidence >= 80. Typed pages score high, handwriting low. Used only to choose pages, never to transcribe.
Writes codex_web_20261113/scoring_C/scores.tsv."""
import csv, json, pathlib, subprocess, sys, tempfile
sys.stdout.reconfigure(encoding="utf-8")
A = pathlib.Path.home() / "Documents" / "grothendieck_archive_montpellier"
OUT = pathlib.Path(__file__).resolve().parent.parent / "scoring_C" / "scores.tsv"
TES = "C:/Program Files/Tesseract-OCR/tesseract.exe"
M = {r["cote"]: r for r in json.loads((A / "MANIFEST.json").read_text(encoding="utf-8"))}
done = set()
if OUT.exists():
    done = {(r["cote"], int(r["pdf_page"])) for r in csv.DictReader(open(OUT, encoding="utf-8"), delimiter="\t")}
new = not OUT.exists()
f = open(OUT, "a", encoding="utf-8", newline="")
w = csv.writer(f, delimiter="\t")
if new:
    w.writerow(["cote", "pdf_page", "words", "good", "mean_conf"])
for cote in ["27", "29", "32", "35", "36", "45", "46", "123"]:
    r = M[cote]; pdf = A / r["folder"] / r["file"]
    info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True, errors="replace").stdout
    n = int([l for l in info.splitlines() if l.startswith("Pages:")][0].split()[-1])
    for p in range(1, n + 1):
        if (cote, p) in done:
            continue
        with tempfile.TemporaryDirectory() as t:
            subprocess.run(["pdftoppm", "-r", "100", "-gray", "-png", "-f", str(p), "-l", str(p), str(pdf), t + "/pg"], check=True)
            img = sorted(pathlib.Path(t).glob("pg*.png"))[0]
            o = subprocess.run([TES, str(img), "stdout", "-l", "eng", "--psm", "3", "tsv"], capture_output=True, text=True, errors="replace").stdout
        words = good = 0; confs = []
        for line in o.splitlines()[1:]:
            c = line.split("\t")
            if len(c) < 12 or not c[11].strip():
                continue
            try:
                conf = float(c[10])
            except ValueError:
                continue
            words += 1; confs.append(conf)
            tok = c[11].strip()
            if conf >= 80 and len(tok) >= 3 and sum(ch.isalpha() for ch in tok) >= 3:
                good += 1
        w.writerow([cote, p, words, good, round(sum(confs) / len(confs), 1) if confs else 0]); f.flush()
    print("cote", cote, "done", flush=True)
