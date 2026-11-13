"""Rebuild LM8_LIE_APPROXIMATIONS_background.zip for Part G (13 Nov 2026): add the CYCLOTOMIC_KERNEL return (LaTeX) and
review, the whole LM3b return (LaTeX), the references of Part G (c) and (f); replace every arXiv PDF in papers/ by its
LaTeX source and drop our returns' PDFs where their full TeX is in the zip (user's rule: LaTeX, not PDFs). The proof
packs are kept as they are, unopened. Regenerates MANIFEST.tsv; first name to "user" in text entries.
usage: python -I -B rebuild_zip_part_g_20261113.py"""
import hashlib
import shutil
import sys
import zipfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
D = Path(r"C:\Users\user\Documents")
UP = D / "longue_marche_pro_pilot_20261104/pro_prompts_draft_20261111/LM8_LIE_APPROXIMATIONS"
WK = D / "longue_marche_pro_pilot_20261104/pro_prompts_draft_20261111_work/LM8_LIE_APPROXIMATIONS"
ZIPF = UP / "LM8_LIE_APPROXIMATIONS_background.zip"
SRC = D / "s6_pro_prompts_20261112_work/literature/arXiv_src"
CK = D / "longue_marche_pro_pilot_20261104/answers/CYCLOTOMIC_KERNEL_unzipped/CYCLOTOMIC_KERNEL"
LM3B = D / "longue_marche_pro_pilot_20261104/answers/LM3b_TEICHMULLER_PUSH.zip"
LIT = D / "Free or receipted/free/lm8-part-g-20261113"
NAME = "Flo" + "ris"
TEXT = {".md", ".tex", ".csv", ".bib", ".py", ".txt", ".out", ".tsv", ".json", ".sage", ".gp", ".log", ".sty", ".cls", ".bbl"}

BK = WK / "LM8_LIE_APPROXIMATIONS_background_before_part_g_20261113.zip"
PB = WK / "PROMPT_before_zip_tex_20261113.md"
assert not BK.exists() and not PB.exists(), "backups exist: already rebuilt?"
shutil.copy2(ZIPF, BK)
shutil.copy2(UP / "PROMPT.md", PB)
z = zipfile.ZipFile(ZIPF)
entries = {n: z.read(n) for n in z.namelist() if not n.endswith("/") and n != "MANIFEST.tsv"}
old_manifest = {}
if "MANIFEST.tsv" in z.namelist():
    for line in z.read("MANIFEST.tsv").decode("utf-8").splitlines()[1:]:
        c = line.split("\t")
        if len(c) >= 2:
            old_manifest[c[0]] = c[1:]
z.close()
origin = {}
sub = {}

# 1. arXiv PDFs in papers/ -> LaTeX source folders
ARX = {"hain_matsumoto_weighted/Hain_Matsumoto_math-0006158v2.pdf": "math_0006158v2",
       "hain_matsumoto_relative/Hain_Matsumoto_Relative_pro-l_completions_0802.0806.pdf": "0802.0806",
       "hain_modular_groups/Hain_Hodge-de_Rham_theory_of_modular_groups_1403.6443.pdf": "1403.6443",
       "hain_torelli/Hain_Infinitesimal_presentations_Torelli_alg-geom-9512001.pdf": "alg-geom_9512001",
       "enriquez_elliptic_associators/Enriquez_Elliptic_associators_1003.1012.pdf": "1003.1012",
       "behrend_noohi/Behrend_Noohi_Uniformization_of_DM_curves_math-0504309.pdf": "math_0504309",
       "gt_shadows/GT_shadows_2008.00066.pdf": "2008.00066"}
for rel, aid in ARX.items():
    n = "papers/" + rel
    sd = SRC / aid
    if n in entries and sd.exists() and list(sd.rglob("*.tex")):
        del entries[n]
        folder = n.rsplit("/", 1)[0] + "/src_arXiv_" + aid + "/"
        for f in sorted(sd.rglob("*")):
            if f.is_file():
                entries[folder + f.relative_to(sd).as_posix()] = f.read_bytes()
                origin[folder + f.relative_to(sd).as_posix()] = ("arXiv e-print " + aid, "LaTeX source in place of " + n)
        sub[n] = folder
# 2. our returns' PDFs where the full TeX is in the zip
for n in ("LM1_return/LM1_GROUP_SCHEMES_paper.pdf", "LM2_return/LM2_LOOP_EQUATIONS_paper.pdf"):
    if n in entries and (n[:-4] + ".tex") in entries:
        del entries[n]
        sub[n] = n[:-4] + ".tex"
# 3. additions
def add(zp, b, org, why):
    entries[zp] = b
    origin[zp] = (org, why)
for name in ("CYCLOTOMIC_KERNEL_paper.tex", "CYCLOTOMIC_KERNEL_results.csv", "CYCLOTOMIC_KERNEL_report.md", "CYCLOTOMIC_KERNEL_references.bib"):
    add("CYCLOTOMIC_return/" + name, (CK / name).read_bytes(), "CYCLOTOMIC_KERNEL return", "CK E1-E3, A6, A7 (Part G)")
for f in sorted((CK / "sections").rglob("*")):
    if f.is_file():
        add("CYCLOTOMIC_return/sections/" + f.relative_to(CK / "sections").as_posix(), f.read_bytes(), "CYCLOTOMIC_KERNEL return", "its sections (E1-E3 in E_root.tex)")
for name in ("root_math_checks.py", "root_math_checks_output.json"):
    add("CYCLOTOMIC_return/code/" + name, (CK / "code" / name).read_bytes(), "CYCLOTOMIC_KERNEL return", "Lyndon and Heisenberg checks (Part G (e) reruns them)")
add("CYCLOTOMIC_review/REVIEW.md", (D / "grothendieck_archive_montpellier/pro_reviews_archive_20261112/CYCLOTOMIC_REVIEW_OPUS/REVIEW.md").read_bytes(),
    "review by Claude Opus 5.5 (effort max), 12 Nov 2026", "the verdicts quoted in 'After CYCLOTOMIC_KERNEL'")
with zipfile.ZipFile(LM3B) as lz:
    for m in lz.namelist():
        if m.endswith("/") or m.lower().endswith(".pdf"):
            continue
        rest = m.split("/", 1)[1] if "/" in m else m
        add("LM3b_return/" + rest, lz.read(m), "LM3b_TEICHMULLER_PUSH return", "A.12-A.16, D.4, D.5 and the elliptic programs (Part G (d), (e))")
for aid, zdir, why in (("0809.0017", "papers/stix_cuspidal_sections/src_arXiv_0809.0017/", "CK A6 (Stix, Corollary 22, Theorem 14)"),
                       ("1512.03975", "papers/hain_matsumoto_universal_mixed_elliptic_motives/src_arXiv_1512.03975/", "Part G (a), (c): the derivations epsilon_2n")):
    for f in sorted((SRC / aid).rglob("*")):
        if f.is_file():
            add(zdir + f.relative_to(SRC / aid).as_posix(), f.read_bytes(), "arXiv e-print " + aid, why)
cmr = D / "research_maps_20261112/CONNES_CONSANI_CFT/papers/math0501424/src"
for f in sorted(cmr.rglob("*")):
    if f.is_file():
        add("papers/connes_marcolli_ramachandran_KMS_CM/src_arXiv_math_0501424/" + f.relative_to(cmr).as_posix(), f.read_bytes(),
            "arXiv e-print math/0501424", "Part G (f): the CM system and its symmetry group (Theorem KMSCM)")
for fn, why in (("nakamura_1995_jms020107.pdf", "Part G (c): Nakamura's characters for open elliptic curves; no LaTeX source exists"),
                ("tsunogai_1995_prims31.pdf", "Part G (c): Tsunogai's derivations; no LaTeX source exists"),
                ("pollack_2009_duke_thesis.pdf", "Part G (a), (c): relations between the epsilon_2n; no LaTeX source found")):
    add("papers/part_g/" + fn, (LIT / fn).read_bytes(), "open access copy", why)
# 4. names, manifest, zip
named = []
for n in list(entries):
    if "proof_packs" not in n and Path(n).suffix.lower() in TEXT and NAME.encode() in entries[n]:
        entries[n] = entries[n].decode("utf-8", errors="surrogateescape").replace(NAME, "user").encode("utf-8", errors="surrogateescape")
        named.append(n)
lines = ["path_in_zip\torigin\tbytes\tsha256\twhy_attached"]
for n in sorted(entries):
    b = entries[n]
    if n in origin:
        org, why = origin[n]
    elif n in old_manifest and len(old_manifest[n]) >= 4:
        org, why = old_manifest[n][0], old_manifest[n][-1]
    else:
        org, why = "(already in the zip)", ""
    lines.append("\t".join([n, org.replace(NAME, "user"), str(len(b)), hashlib.sha256(b).hexdigest(), why]))
entries["MANIFEST.tsv"] = ("\n".join(lines) + "\n").encode("utf-8")
with zipfile.ZipFile(ZIPF, "w", zipfile.ZIP_DEFLATED) as zz:
    for n in sorted(entries):
        zz.writestr(n, entries[n])
with zipfile.ZipFile(ZIPF) as zz:
    print("zip", ZIPF.stat().st_size, "bytes,", len(zz.namelist()), "entries; testzip", zz.testzip())
print("replaced:", sub)
print("first name replaced in", len(named), "entries")
p = UP / "PROMPT.md"
t = p.read_text(encoding="utf-8")
k = 0
for a, b in sub.items():
    for cand in (a, a.split("/", 1)[1] if a.startswith("papers/") else a):
        if cand in t:
            t = t.replace(cand, b + (" (LaTeX source)" if b.endswith("/") else ""))
            k += 1
p.write_text(t, encoding="utf-8")
print("prompt references changed:", k)
