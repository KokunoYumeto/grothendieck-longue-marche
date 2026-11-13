"""Rebuild LM6_POINTS_AS_SECTIONS_background.zip (13 Nov 2026, Claude Fable 5.2, effort max): add the FLAGGED_149 return
(LaTeX), its intake, its source check, the Connes-Consani map and source (ZIP_ADD_20261113.md); replace every arXiv PDF in
literature/ by its LaTeX e-print; drop our returns' PDFs where their TeX is in the zip (user's rule: LaTeX, not PDFs);
refresh the copy of PROMPT.md inside the zip. Entries under proof_packs/ are copied byte for byte and not looked at.
Regenerates MANIFEST.tsv in its own format; first name to "user" in new text entries; CRC check of every kept entry.
usage: python -I -B rebuild_zip_flagged149_20261113.py"""
import hashlib
import shutil
import sys
import zipfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
NAME = "Flo" + "ris"
D = Path(r"C:\Users") / NAME / "Documents"
UP = D / "longue_marche_pro_pilot_20261104/pro_prompts_draft_20261111/LM6_POINTS_AS_SECTIONS"
WK = D / "longue_marche_pro_pilot_20261104/pro_prompts_draft_20261111_work/LM6_POINTS_AS_SECTIONS"
ZIPF = UP / "LM6_POINTS_AS_SECTIONS_background.zip"
AX = D / "Free or receipted/free/anabelian-149-20261113/arXiv_src"
F149 = D / "longue_marche_pro_pilot_20261104/answers/FLAGGED_149_unzipped"
REV = D / "grothendieck_archive_montpellier/pro_reviews_archive_20261112"
TEXT = {".md", ".tex", ".csv", ".bib", ".py", ".txt", ".out", ".tsv", ".json", ".sage", ".gp", ".log", ".sty", ".cls", ".bbl", ".bst", ".clo"}
BK = WK / "LM6_POINTS_AS_SECTIONS_background_before_flagged149_20261113.zip"
PB = WK / "PROMPT_before_zip_tex_20261113.md"
assert not BK.exists() and not PB.exists(), "backups exist: already rebuilt?"

# the prompt: where the FLAGGED_149 return is, and what form the literature has
p = UP / "PROMPT.md"
raw = p.read_bytes().decode("utf-8")
nl = "\r\n" if "\r\n" in raw else "\n"
t = raw.replace("\r\n", "\n")
for old, new in (
    ("**New since this prompt was drafted, second block: the return FLAGGED_149** (attached in\n`LM6_POINTS_AS_SECTIONS_new_results.zip`, folder `FLAGGED_149_return/`:",
     "**New since this prompt was drafted, second block: the return FLAGGED_149** (attached in\n`LM6_POINTS_AS_SECTIONS_background.zip`, folder `FLAGGED_149_return/`:"),
    ("`CONNES_CONSANI_MAP.md` and the LaTeX source of arXiv:2501.06560.",
     "`CONNES_CONSANI_MAP.md` and the LaTeX source of arXiv:2501.06560. Under `literature/` every arXiv paper is attached as its LaTeX source (a folder `src_arXiv_<id>/`, the version current on 13 November 2026), every other text as PDF; `MANIFEST.tsv` lists each file with its origin."),
):
    assert t.count(old) == 1, old[:60]
    t = t.replace(old, new)

z = zipfile.ZipFile(ZIPF)
old_crc = {i.filename: i.CRC for i in z.infolist()}
entries = {n: z.read(n) for n in z.namelist() if not n.endswith("/") and n != "MANIFEST.tsv"}
mlines = z.read("MANIFEST.tsv").decode("utf-8").splitlines()
z.close()
assert mlines[1].split("\t") == ["path_in_zip", "source_path_or_url", "sha256", "bytes", "note"], mlines[1]
old_rows = {ln.split("\t")[0]: ln for ln in mlines[2:] if ln.strip()}
packs = [n for n in entries if "proof_packs" in n]
new_rows, sub = {}, {}


def add(zp, b, src, note):
    entries[zp] = b
    new_rows[zp] = (src, note)


def add_tree(zdir, folder, src, note, skip_pdf=False):
    k = 0
    for f in sorted(Path(folder).rglob("*")):
        if f.is_file() and not (skip_pdf and f.suffix.lower() == ".pdf"):
            add(zdir + f.relative_to(folder).as_posix(), f.read_bytes(), src, note)
            k += 1
    assert k, folder
    return k


# 1. arXiv PDFs -> LaTeX e-prints
ARX = {
    "abbr-lifting/abbr_lifting_harmonic_morphisms_I_arxiv_1303.4812v3.pdf": "1303.4812",
    "baker-rabinoff/baker_rabinoff_skeleton_jacobian_arxiv_1308.3864v1.pdf": "1308.3864",
    "behrstock-minsky-rank/behrstock-minsky-math0512352.pdf": "math_0512352",
    "bresciani-vistoli/bresciani_vistoli_real_section_arxiv_2012.06278v2.pdf": "2012.06278",
    "carlson-corwin-2611.09080/2611.09080.pdf": "2611.09080",
    "collas-2603.02848/2603.02848.pdf": "2603.02848",
    "collas-philip-yamaguchi-2605.02577/2605.02577.pdf": "2605.02577",
    "esnault-hai/esnault_hai_packets_arxiv_math0703877.pdf": "math_0703877",
    "harari-stix/harari_stix_finidesc.pdf": "1005.1302",
    "holzschuh-2510.13325/2510.13325.pdf": "2510.13325",
    "holzschuh-schmidt-stix-2608.21232/2608.21232.pdf": "2608.21232",
    "koenigsmann-2005/koenigsmann_section_conjecture_arxiv_math0305226v1.pdf": "math_0305226",
    "luo-watanabe-2610.24986/2610.24986.pdf": "2610.24986",
    "pop-2604.26131/2604.26131.pdf": "2604.26131",
    "pop-stix-2011/pop_stix_arxiv_1111.1354v1.pdf": "1111.1354",
    "porowski-2026/porowski_families_separating_points_arxiv_2607.27746v1.pdf": "2607.27746",
    "power-quotients-2507.13701/power-quotients-2507.13701.pdf": "2507.13701",
    "steklov-2026/steklov_flt_selmer_sections_arxiv_2602.17746v2.pdf": "2602.17746",
    "stix-cuspidal/stix_cuspidal_sections_arxiv_0809.0017.pdf": "0809.0017",
    "stix-local-conditions/stix_birational_local_conditions_arxiv_1203.3236v3.pdf": "1203.3236",
    "stix-period-index/stix_period_index_arxiv_0802.4125.pdf": "0802.4125",
    "stoll-finite-descent/stoll_covers_revised.pdf": "math_0606465",
}
def srcdir(aid):
    return (D / "s6_pro_prompts_20261112_work/literature/arXiv_src/0809.0017") if aid == "0809.0017" else AX / aid


for rel, aid in ARX.items():  # every check before anything is written
    assert "literature/" + rel in entries, rel
    assert srcdir(aid).exists() and any(f.suffix.lower() == ".tex" for f in srcdir(aid).rglob("*") if f.is_file()), aid
for q in (F149 / "FLAGGED_149_paper.tex", F149 / "sections", F149 / "code", REV / "FLAGGED_149_REVIEW_FABLE/REVIEW.md", REV / "FLAGGED_149_SOURCE_CHECK_OPUS/CHECK.md",
          D / "research_maps_20261112/CONNES_CONSANI_CFT/MAP.md", D / "research_maps_20261112/CONNES_CONSANI_CFT/papers/2501.06560/src"):
    assert q.exists(), q
shutil.copy2(ZIPF, BK)
shutil.copy2(UP / "PROMPT.md", PB)
for rel, aid in ARX.items():
    n = "literature/" + rel
    sd = srcdir(aid)
    folder = n.rsplit("/", 1)[0] + "/src_arXiv_" + aid + "/"
    add_tree(folder, sd, "https://arxiv.org/e-print/" + aid.replace("_", "/"), "LaTeX source (arXiv e-print) in place of " + n)
    del entries[n]
    sub[n] = folder
# 2. our returns' PDFs where the TeX is in the zip
for n in ("LM3_return/LM3_TEICHMULLER_TOWER_paper.pdf", "LM3b_return/LM3b_TEICHMULLER_PUSH_paper.pdf"):
    if n in entries and (n[:-4] + ".tex") in entries:
        del entries[n]
        sub[n] = n[:-4] + ".tex"
# 3. additions of ZIP_ADD_20261113.md
add("FLAGGED_149_return/FLAGGED_149_paper.tex", (F149 / "FLAGGED_149_paper.tex").read_bytes(), "FLAGGED_149 return", "the return's paper in LaTeX (inputs sections/); second New-since block")
add_tree("FLAGGED_149_return/sections/", F149 / "sections", "FLAGGED_149 return", "statements and proofs cited as F149-<id>")
for fn in ("FLAGGED_149_results.csv", "FLAGGED_149_readings.csv", "FLAGGED_149_report.md", "FLAGGED_149_references.bib"):
    add("FLAGGED_149_return/" + fn, (F149 / fn).read_bytes(), "FLAGGED_149 return", "register, report or bibliography")
add_tree("FLAGGED_149_return/code/", F149 / "code", "FLAGGED_149 return", "programs with outputs")
add("FLAGGED_149_REVIEW.md", (REV / "FLAGGED_149_REVIEW_FABLE/REVIEW.md").read_bytes(), "intake by Claude Fable 5.2 (effort max), 13 Nov 2026", "the verdicts the second block quotes")
add("FLAGGED_149_SOURCE_CHECK.md", (REV / "FLAGGED_149_SOURCE_CHECK_OPUS/CHECK.md").read_bytes(), "source check by Claude Opus 5.5 (effort max), 13 Nov 2026", "the nine sources of F17.6-F17.7 (Part F (f))")
add("CONNES_CONSANI_MAP.md", (D / "research_maps_20261112/CONNES_CONSANI_CFT/MAP.md").read_bytes(), "map by Claude Fable 5.2 (effort max), 13 Nov 2026", "notes L6 (F (g)), L10 (F (d)); reference of C (b), (c)")
add_tree("literature/connes-consani-2501.06560/src_arXiv_2501.06560/", D / "research_maps_20261112/CONNES_CONSANI_CFT/papers/2501.06560/src", "https://arxiv.org/e-print/2501.06560", "Connes-Consani, Remark 3.13 (Part C (b), (c)); LaTeX source")
# 4. names in the new text entries; the prompt copy
named = []
for n in new_rows:
    if Path(n).suffix.lower() in TEXT and NAME.encode() in entries[n]:
        entries[n] = entries[n].decode("utf-8", errors="surrogateescape").replace(NAME, "user").encode("utf-8", errors="surrogateescape")
        named.append(n)
for a, b in sub.items():
    for cand in (a, a.split("/", 1)[1]):
        if cand in t:
            t = t.replace(cand, b + (" (LaTeX source)" if b.endswith("/") else ""))
p.write_bytes(t.replace("\n", nl).encode("utf-8"))
had_prompt = "PROMPT.md" in entries
if had_prompt:
    entries["PROMPT.md"] = p.read_bytes()
    new_rows["PROMPT.md"] = ("the prompt as of 13 Nov 2026", "copy of the prompt")
# 5. manifest (its own format), zip, checks
body = []
for n in sorted(entries):
    if n in new_rows:
        src, note = new_rows[n]
        b = entries[n]
        body.append("\t".join([n, src.replace(NAME, "user"), hashlib.sha256(b).hexdigest(), str(len(b)), note]))
    elif n in old_rows:
        body.append(old_rows[n])
    else:
        b = entries[n]
        body.append("\t".join([n, "(already in the zip)", hashlib.sha256(b).hexdigest(), str(len(b)), ""]))
head = "# MANIFEST of LM6_POINTS_AS_SECTIONS_background.zip (%d files besides this one, %d bytes unzipped); built 12 Nov 2026 by package_20261112.py (Claude Opus 5.5); rebuilt 13 Nov 2026 by rebuild_zip_flagged149_20261113.py (Claude Fable 5.2): FLAGGED_149 return added, arXiv PDFs replaced by LaTeX e-prints" % (len(entries), sum(len(b) for b in entries.values()))
entries["MANIFEST.tsv"] = ("\n".join([head, mlines[1]] + body) + "\n").encode("utf-8")
with zipfile.ZipFile(ZIPF, "w", zipfile.ZIP_DEFLATED) as zz:
    for n in sorted(entries):
        zz.writestr(n, entries[n])
with zipfile.ZipFile(ZIPF) as zz:
    info = {i.filename: i for i in zz.infolist()}
    bad = [n for n in info if n in old_crc and n not in new_rows and n != "MANIFEST.tsv" and info[n].CRC != old_crc[n]]
    print("zip %d bytes (%.1f MB), %d entries, %.1f MB unzipped; testzip %s" % (ZIPF.stat().st_size, ZIPF.stat().st_size / 1e6, len(info), sum(i.file_size for i in info.values()) / 1e6, zz.testzip()))
    print("kept entries with a changed CRC:", bad)
    print("pdf entries left:", sum(1 for n in info if n.lower().endswith(".pdf")), "| tex entries:", sum(1 for n in info if n.lower().endswith(".tex")))
print("proof_packs entries (copied, not looked at):", len(packs))
print("replaced:", len(sub), "| added rows:", len(new_rows), "| first name replaced in", len(named), "new entries")
print("old rows without entry dropped:", len([n for n in old_rows if n not in entries]), "| prompt copy refreshed:", had_prompt)
