"""ANABELIAN_149_PUSH, 13 Nov 2026 (Claude Fable 5.2, effort max): (1) write into PROMPT.md the references verified
against the sources and the list of attachments as built; (2) build the upload folder with PROMPT.md and
ANABELIAN_149_PUSH_background.zip (LaTeX wherever a source exists, PDFs only where none does), MANIFEST.tsv inside,
first name to "user" in text entries, testzip check; (3) regenerate ZIP_LIST.md from the same table.
Backups before any overwrite. usage: python -I -B build_zip_20261113.py"""
import hashlib
import re
import shutil
import sys
import zipfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
NAME = "Flo" + "ris"
D = Path(r"C:\Users") / NAME / "Documents"
WK = D / "grothendieck_archive_montpellier/pro_prompts_archive_20261112_work/ANABELIAN_149_PUSH"
UP = D / "grothendieck_archive_montpellier/pro_prompts_archive_20261112/ANABELIAN_149_PUSH"
ZIPF = UP / "ANABELIAN_149_PUSH_background.zip"
RET = D / "grothendieck_archive_transcription_20261110/returns"
PKG = D / "grothendieck_archive_transcription_20261110/packages_done"
F149 = D / "longue_marche_pro_pilot_20261104/answers/FLAGGED_149_unzipped"
CK = D / "longue_marche_pro_pilot_20261104/answers/CYCLOTOMIC_KERNEL_unzipped/CYCLOTOMIC_KERNEL"
REV = D / "grothendieck_archive_montpellier/pro_reviews_archive_20261112"
FREE = D / "Free or receipted/free"
NEW = FREE / "anabelian-149-20261113"
LME = FREE / "lm-expert-20261112"
GR = FREE / "good-reduction-20261112"
SC = REV / "FLAGGED_149_SOURCE_CHECK_OPUS/sources"
TEXT = {".md", ".tex", ".csv", ".bib", ".py", ".txt", ".out", ".tsv", ".json", ".sage", ".gp", ".log", ".sty", ".cls", ".bbl", ".bst", ".clo"}

# ------------------------------------------------------------------ 1. the prompt
P = WK / "PROMPT.md"
t = P.read_text(encoding="utf-8")
MARK = "Opened by the drafter: Asada, Matsumoto and Oda"
if MARK not in t:
    shutil.copy2(P, WK / "PROMPT_before_verification_20261113.md")
    LIT = ("- **`literature/`**, in LaTeX source wherever a source exists (arXiv e-prints, each in a folder `src_arXiv_<id>/`): Stix, *On cuspidal sections of algebraic fundamental groups* (arXiv:0809.0017, its one version); Stix, *On the birational section conjecture with local conditions* (arXiv:1203.3236); Saïdi–Tamagawa, *A prime-to-p version of the Grothendieck anabelian conjecture for hyperbolic curves over finite fields of characteristic p > 0* (arXiv:0801.1452; published in Publ. RIMS 45 (2009); the numbers quoted in R4 (c) occur in this source); Saïdi–Tamagawa, *A refined version of Grothendieck's anabelian conjecture for hyperbolic curves over finite fields* (arXiv:1708.08773); Koenigsmann, *On the \"section conjecture\" in anabelian geometry* (arXiv:math/0305226); Bresciani, *On the birational section conjecture with strong birationality assumptions* (arXiv:2108.13397; Invent. Math.); Bresciani, *Some implications between Grothendieck's anabelian conjectures* (arXiv:1804.07176; Algebraic Geometry 8 (2021)); Borne–Emsalem–Stix, *Lifting Galois sections along torsors* (arXiv:1301.4429; the return quotes the authors' version of 23 March 2015, whose numbering may differ: locate its Theorem 27 by content); Harari–Stix, *Descent obstruction and fundamental exact sequence* (arXiv:1005.1302); Stoll, *Finite descent obstructions and rational points on curves* (arXiv:math/0606465); Bertin–Romagny, *Champs de Hurwitz* (arXiv:math/0701680); Noohi, *Foundations of topological stacks I* (arXiv:math/0503247); Dupuy–Rabinoff (arXiv:1705.03034); Connes–Consani, *Knots, primes and class field theory* (arXiv:2501.06560); SGA 1 (arXiv:math/0206203); `SGA7I_expose_IX.tex` (SGA 7 I, exposé IX, from our edition: AI-transcribed, checked against the scans). "
           "As PDF, no source being available: Mochizuki, *A combinatorial version of the Grothendieck conjecture* (author's version of April 2007), with two of the papers it rests on, *The profinite Grothendieck conjecture for closed hyperbolic curves over number fields* (1996) and *The absolute anabelian geometry of hyperbolic curves* (2003); Hoshi–Mochizuki, *On the combinatorial anabelian geometry of nodally nondegenerate outer representations* (2011) and *Topics surrounding the combinatorial anabelian geometry of hyperbolic curves I* (2012); Tamagawa, *The Grothendieck conjecture for affine curves* (1997); Mochizuki, *The local pro-p anabelian geometry of curves* (1999); Nakamura 1994; Illusie, *An overview of the work of K. Fujiwara, K. Kato and C. Nakayama on logarithmic étale cohomology* (Astérisque 279, 2002); Hoshi, *The exactness of the log homotopy sequence* (RIMS-1558, July 2006); Mochizuki, *Extending families of curves over log regular schemes* (1999, author's version); the paper of Katz and Lang with Ribet's appendix (1981); Knudsen 1983; Deligne–Mumford 1969; Saïdi, *Revêtements modérés et groupe fondamental de graphe de groupes* (1997); Asada–Matsumoto–Oda, *Local monodromy on the fundamental groups of algebraic curves along a degenerate stable curve* (in its version RIMS Kôkyûroku 808 (1992) 91–146; published in J. Pure Appl. Algebra 103 (1995) 235–283); Andreatta–Iovita–Kim, *A p-adic nonabelian criterion for good reduction of curves* (the authors' accepted manuscript; Duke Math. J. 164 (2015)); OpenAI, *The p-adic section conjecture* (6 October 2026; unrefereed). `MANIFEST.tsv` lists every file with its origin. Open every further source you use and record it.")
    L1 = ("Opened by the drafter: Asada, Matsumoto and Oda, *Local monodromy on the fundamental groups of algebraic curves along a degenerate stable curve* (attached in its version RIMS Kôkyûroku 808 (1992) 91–146; the version of J. Pure Appl. Algebra 103 (1995) 235–283 was not opened), Theorem (3.2), the non-abelian Picard–Lefschetz formula: for the local universal deformation over `C`, with one parameter `t_e` for each node (local equation `uv = t_e`), and the topological fundamental group, the loop around `t_e = 0` acts by the edge twist `D_e` of the graph of groups. The thickness enters by the base change `t_e = ϖ^{m_e}` and the profinite group by completion: both steps are to be written. The profinite statement is in Hoshi–Mochizuki 2012 (opened by the drafter): Definition 4.4 (profinite Dehn multi-twists), Theorem 4.8 (iv) (`Dehn(𝒢) ≅ ⊕_{nodes} Λ_𝒢`), Lemma 5.4 (ii), (iii) (the log inertia of the base maps to `⊕_e Λ_e` by the lengths of the nodes, and the universal outer representation lands in `Dehn(𝒢)`), Corollary 5.9. Not opened: Oda's two notes (J. Number Theory 34 (1990) 225–228, doi:10.1016/0022-314X(90)90152-H, and 53 (1995) 342–355, doi:10.1006/jnth.1995.1095; bibliographic data from Crossref; the publisher's site refuses automated clients); the introduction of Asada–Matsumoto–Oda cites an earlier paper of Oda for the case where the graph is a tree.")
    L8 = ("(opened by the drafter: Hoshi–Mochizuki 2012, Theorem 4.8 (iv), (v): `Dehn(𝒢) ≅ ⊕_{nodes} Λ_𝒢`, functorially, with the conjugation action of `Aut(𝒢)` given by the cyclotomic action and the permutation of the nodes; Mochizuki 2007, Corollary 2.7 (iii) and Corollary 2.8: an isomorphism between the groups of two stable log curves over log points, compatible with the outer actions and matching the `l`-inertia subgroups, is graphic when the actions are `l`-logarithmically full; 2.7 (iii) assumes no cusps, 2.8 allows cusps and assumes arithmetically full actions over a base field embeddable in a finitely generated extension of `F_p` or `Q_p`. Those hypotheses are to be checked in the setting of B11)")
    AIK = ("(opened by the drafter in the authors' accepted manuscript, attached: Andreatta, Iovita and Kim, *A p-adic nonabelian criterion for good reduction of curves*, Duke Math. J. 164 (2015), Theorems 1.6 and 1.9: for a smooth proper curve of genus ≥ 2 with semistable reduction over a complete discrete valuation field of characteristic 0 with perfect residue field of characteristic `p`, good reduction holds if and only if the unipotent `p`-adic étale fundamental group at a base point is crystalline, equivalently the representations `E^et_{n,b}` are crystalline for every `n ≥ 1`; their Theorem 1.2 is the crystalline criterion for abelian varieties, their Theorem 1.3 Oda's `ℓ`-adic criterion). Quote the theorem with its hypotheses, prove what it gives for the pair `(Ū, D)` and without the hypothesis of semistable reduction, and check it on the curve `y² = (x³ − 5⁶)(x³ − 1)` over `Q_5`.")
    edits = [
        ("attached are the images of scans 35, 36,", "attached in `scans/` are the images of scans 35, 36,", False),
        (r"- \*\*`literature/`\*\*, in LaTeX source wherever a source exists:.*?Open every further source you use and record it\.", LIT, True),
        ("From memory, unverified: Asada, Matsumoto and Oda, *Local monodromy on the fundamental groups of algebraic curves along a degenerate stable curve*, J. Pure Appl. Algebra 103 (1995), and Oda's notes in J. Number Theory (1990; 53 (1995) 342–355) treat this formula.", L1, False),
        ("(Hoshi–Mochizuki 2012, Theorem 4.8; Mochizuki 2007, Corollary 2.7; numbers from memory, unverified)", L8, False),
        (r"\(from memory, unverified: Andreatta.*?over `Q_5`\.", AIK, True),
        ("quote the theorem (expected: SGA 7 I, exposé IX, §5; number to be taken from the attached text)", "quote the theorem (in the attached text of SGA 7 I, exposé IX: Corollaire 5.10 and Proposition 5.13 a), which for `ℓ = p` assume `K` of characteristic 0; opened by the drafter)", False),
        ("and prove the statement from the attached text of SGA 7 I, exposé IX:", "and prove the statement from the attached text of SGA 7 I, exposé IX (its criteria are Corollaire 5.10 and Propositions 5.13, 5.14):", False),
        ("the references [Mzk1] §3 and [Mzk2] §2 of that paper, and Hoshi–Mochizuki 2011, Definition 2.10 (iv).", "the references [Mzk1] §3 and [Mzk2] §2 of that paper (*The geometry of the compactification of the Hurwitz scheme*, Publ. RIMS 31 (1995), not attached; *The profinite Grothendieck conjecture for closed hyperbolic curves over number fields*, 1996, attached), and Hoshi–Mochizuki 2011, Definition 2.10 (iv).", False),
    ]
    for old, new, rx in edits:
        c = len(re.findall(old, t, re.S)) if rx else t.count(old)
        assert c == 1, (c, old[:60])
        t = re.sub(old, lambda m: new, t, flags=re.S) if rx else t.replace(old, new)
    assert "from memory" not in t.lower().replace("recalled from memory", ""), "a from-memory mark is left"
    P.write_text(t, encoding="utf-8", newline="")
    print("prompt: 7 edits written; backup PROMPT_before_verification_20261113.md")
else:
    print("prompt: already edited")

# ------------------------------------------------------------------ 2. the zip
entries, origin = {}, {}


def add(zp, src, why, data=None):
    b = Path(src).read_bytes() if data is None else data
    assert zp not in entries, zp
    entries[zp] = b
    origin[zp] = (str(src), why)


def add_tree(zdir, folder, why, skip_pdf=False):
    folder = Path(folder)
    n = 0
    for f in sorted(folder.rglob("*")):
        if f.is_file() and not (skip_pdf and f.suffix.lower() == ".pdf"):
            add(zdir + f.relative_to(folder).as_posix(), f, why)
            n += 1
    assert n, folder
    return n


def add_scans(zipname, pattern, why):
    with zipfile.ZipFile(zipname) as z:
        ms = [n for n in z.namelist() if re.search(pattern, n, re.I)]
        assert ms, (zipname, pattern, z.namelist()[:3])
        for n in sorted(ms):
            add("scans/" + Path(n).name, "member %s of %s" % (n, zipname), why, z.read(n))
    return len(ms)


for stem, why in (("MPL_149_001-090", "cote 149, scans 1-90 (Parts A, D; B8)"), ("MPL_149_091-136", "cote 149, scans 91-136 (Parts B, D)"), ("MPL_142_001-093", "cote 142; scans 15-21 are Part E")):
    add(stem + "_transcription.tex", RET / (stem + "_unzipped") / (stem + "_transcription.tex"), why + "; first-pass transcription")
    add(stem + "_notes.md", RET / (stem + "_unzipped") / (stem + "_notes.md"), "notes of the transcribing model (unreviewed)")
ns = [add_scans(PKG / "05_MPL_149_001-090/MPL_149_001-090_scans.zip", r"scan(035|036|044|045|048|049|056|059|06[0-3]|07[4-8]|090)(_[ab])?\.(jpg|jpeg|png)$", "scan image, the authority for the readings"),
      add_scans(PKG / "06_MPL_149_091-136/MPL_149_091-136_scans.zip", r"scan(099|10[0-4]|126|127)(_[ab])?\.(jpg|jpeg|png)$", "scan image, the authority for the readings"),
      add_scans(PKG / "09_MPL_142_001-093/MPL_142_001-093_scans.zip", r"scan(01[5-9]|02[01])(_[ab])?\.(jpg|jpeg|png)$", "scan image of cote 142 (Part E)")]
print("scan images:", ns)
add("FLAGGED_149_return/FLAGGED_149_paper.tex", F149 / "FLAGGED_149_paper.tex", "the return this prompt continues (LaTeX; inputs sections/)")
add_tree("FLAGGED_149_return/sections/", F149 / "sections", "statements and proofs cited as F149-<id>")
for fn in ("FLAGGED_149_results.csv", "FLAGGED_149_readings.csv", "FLAGGED_149_report.md", "FLAGGED_149_references.bib"):
    add("FLAGGED_149_return/" + fn, F149 / fn, "register, report or bibliography of the return")
add_tree("FLAGGED_149_return/code/", F149 / "code", "programs with outputs (F7_test, AB_checks for Part A)")
add("FLAGGED_149_REVIEW.md", REV / "FLAGGED_149_REVIEW_FABLE/REVIEW.md", "the intake: verdicts quoted in R1-R26")
add("FLAGGED_149_SOURCE_CHECK.md", REV / "FLAGGED_149_SOURCE_CHECK_OPUS/CHECK.md", "check of the nine sources of F17.6-F17.7; item B0")
add("CYCLOTOMIC_KERNEL_return/CYCLOTOMIC_KERNEL_paper.tex", CK / "CYCLOTOMIC_KERNEL_paper.tex", "R15-R18, R22 (LaTeX)")
add_tree("CYCLOTOMIC_KERNEL_return/sections/", CK / "sections", "sections of the CYCLOTOMIC_KERNEL return")
for fn in ("CYCLOTOMIC_KERNEL_results.csv", "CYCLOTOMIC_KERNEL_report.md", "CYCLOTOMIC_KERNEL_references.bib"):
    add("CYCLOTOMIC_KERNEL_return/" + fn, CK / fn, "register, report or bibliography of CYCLOTOMIC_KERNEL")
add_tree("CYCLOTOMIC_KERNEL_return/code/", CK / "code", "programs with outputs of CYCLOTOMIC_KERNEL")
add("CYCLOTOMIC_REVIEW.md", REV / "CYCLOTOMIC_REVIEW_OPUS/REVIEW.md", "review by Claude Opus 5.5: verdicts quoted in R15-R18")
add("R149_NOTES_20261112.md", D / "grothendieck_archive_montpellier/wargame_work/R149_NOTES_20261112.md", "the reader's notes on cote 149")
add("CONNES_CONSANI_MAP.md", D / "research_maps_20261112/CONNES_CONSANI_CFT/MAP.md", "R23 (note L6), L10 (note L11), Part C")
AX = NEW / "arXiv_src"
for zdir, folder, why in (
    ("stix_cuspidal_sections/src_arXiv_0809.0017/", D / "s6_pro_prompts_20261112_work/literature/arXiv_src/0809.0017", "Stix: Prop. 8, 11, Cor. 12, 13, Thm 14, Lemma 19, Thm 20, Cor. 21, 22 (R10, R15, R24, B0)"),
    ("stix_birational_local_conditions/src_arXiv_1203.3236/", AX / "1203.3236", "Stix 2015 (R24, D2)"),
    ("saidi_tamagawa_prime_to_p/src_arXiv_0801.1452/", AX / "0801.1452", "Saidi-Tamagawa 2009: Def. 1.5, Prop. 1.8, Cor. 1.11 (R4 (c), A1)"),
    ("saidi_tamagawa_refined/src_arXiv_1708.08773/", FREE / "arxiv-tex/1708.08773", "Saidi-Tamagawa 2017: Thm 1.9 (R4 (c), A1)"),
    ("koenigsmann/src_arXiv_math_0305226/", AX / "math_0305226", "Koenigsmann (route for D2)"),
    ("bresciani_birational/src_arXiv_2108.13397/", AX / "2108.13397", "Bresciani, Theorems A, B (R21: ZD11; D3)"),
    ("bresciani_implications/src_arXiv_1804.07176/", AX / "1804.07176", "Bresciani 2021, A.22, A.23 (R26)"),
    ("borne_emsalem_stix/src_arXiv_1301.4429/", AX / "1301.4429", "Borne-Emsalem-Stix (cited by F149-ZD10; D3, D4)"),
    ("harari_stix/src_arXiv_1005.1302/", AX / "1005.1302", "Harari-Stix: finite descent (route for D1)"),
    ("stoll_finite_descent/src_arXiv_math_0606465/", AX / "math_0606465", "Stoll: finite descent (route for D1)"),
    ("bertin_romagny/src_arXiv_math_0701680/", AX / "math_0701680", "Champs de Hurwitz 6.9, 6.14, 6.20 (R26, E1)"),
    ("noohi/src_arXiv_math_0503247/", AX / "math_0503247", "Noohi, Theorem 20.4 (R26)"),
    ("dupuy_rabinoff/src_arXiv_1705.03034/", AX / "1705.03034", "compact-type Jacobians (R7, R14, B7)"),
    ("connes_consani/src_arXiv_2501.06560/", D / "research_maps_20261112/CONNES_CONSANI_CFT/papers/2501.06560/src", "Connes-Consani, Prop. 3.4, 4.1, Thm 4.2 (C1)"),
    ("SGA1/src_arXiv_math_0206203/", FREE / "arxiv-tex/math_0206203", "SGA 1, expose XIII (R4 (b), B0 (4), C1)"),
):
    add_tree("literature/" + zdir, folder, why)
add("literature/SGA7I_expose_IX.tex", D / "sga_scan_check_20261105/sga7i/current/expose_IX_body.tex", "SGA 7 I, expose IX, our edition: Cor. 5.10, Prop. 5.13, 5.14 (B2, B4, B7)")
for fn, src, why in (
    ("combgc.pdf", LME / "mochizuki-combgc/combgc.pdf", "Mochizuki 2007: Example 2.5, Prop. 1.2, 2.4, Cor. 2.7, 2.8 (R10, B0, B11); no LaTeX source"),
    ("closed_number_fields.pdf", LME / "mochizuki-1996-closed/closed_number_fields.pdf", "Mochizuki 1996 = [Mzk2] of combgc (B0 (2) (ii)); no LaTeX source"),
    ("absolute_anabelian.pdf", LME / "mochizuki-absolute-anabelian/absolute_anabelian.pdf", "Mochizuki 2003 = [Mzk4] of combgc (B0 (2) (ii)); no LaTeX source"),
    ("nodnon.pdf", LME / "hoshi-mochizuki-nodnon/nodnon.pdf", "Hoshi-Mochizuki 2011: Def. 2.10, Lemma 2.11, Rem. 2.14.1 (R10, B0); no LaTeX source"),
    ("hoshi_mochizuki_combinatorial_anabelian_topics_I.pdf", GR / "hoshi_mochizuki_combinatorial_anabelian_topics_I.pdf", "Def. 4.4, Thm 4.8, Lemma 5.4, Cor. 5.9 (L1, L8, B1, B11); no LaTeX source"),
    ("tamagawa_affine_curves.pdf", LME / "tamagawa-1997-affine/tamagawa_affine_curves.pdf", "Theorem (5.3) (R6, C1); journal PDF"),
    ("local_pro_p.pdf", LME / "mochizuki-local-pro-p/local_pro_p.pdf", "Mochizuki 1999: Theorems 16.5, 17.1 (R20); no LaTeX source"),
    ("jms010103.pdf", LME / "nakamura-1994-profinite-calculus/jms010103.pdf", "Nakamura 1994, 2.1 (R15, L9); journal PDF"),
    ("deligne_mumford_1969_PMIHES36.pdf", GR / "deligne_mumford_1969_PMIHES36.pdf", "stable reduction (B1, B2); journal scan"),
    ("saidi_1997_compositio107.pdf", GR / "saidi_1997_compositio107.pdf", "graph of groups of a degenerating curve (L1, C2); journal PDF"),
    ("padic_section_conjecture_2026.pdf", D / "recent_results_20261110/papers/019_The-p-adic-section-conjecture-October-6-2026.pdf", "R24 (unrefereed tool); no source published"),
    ("illusie_2002_asterisque279.pdf", SC / "illusie2002_numdam/AST_2002__279__271_0.pdf", "Theorem 7.6, 7.3 (R10, B0); Numdam scan"),
    ("hoshi_RIMS1558.pdf", SC / "hoshi2009_rims1558/RIMS1558.pdf", "Cor. 3.9, Rem. 1.10 in the numbering of RIMS-1558 (R10, B0); preprint PDF"),
    ("knudsen_1983.pdf", SC / "knudsen1983_mscand/knudsen1983.pdf", "Theorem 2.7 (R11); journal scan"),
    ("mochizuki_1999_extending_families.pdf", SC / "mochizuki1999_extending/extending.pdf", "Theorem 3.3, log purity (B0 (2) (i)); author's PDF"),
    ("katz_lang_ribet_appendix.pdf", REV / "CYCLOTOMIC_REVIEW_OPUS/papers/Katz_Lang_Ribet_AbsFinThm.pdf", "Ribet's Theorem 1 behind Stix's Lemma 19 (B0 (1)); journal scan"),
    ("asada_matsumoto_oda_1992_kokyuroku808.pdf", NEW / "asada_matsumoto_oda_1992_rims_kokyuroku808/0808-04.pdf", "Theorem (3.2), non-abelian Picard-Lefschetz formula (L1, B1); scan from the Kyoto repository"),
    ("andreatta_iovita_kim_2015_accepted_manuscript.pdf", NEW / "andreatta_iovita_kim_2015_wrap135638/WRAP-p-adic-nonabelian-criterion-good-reduction-curves-Kim-2015.pdf", "Theorems 1.6, 1.9 (B7); accepted manuscript from the Warwick repository"),
):
    add("literature/" + fn, src, why)

named, mails, keys = [], {}, []
for n in list(entries):
    if Path(n).suffix.lower() in TEXT:
        s = entries[n].decode("utf-8", errors="surrogateescape")
        if NAME in s:
            s = s.replace(NAME, "user")
            entries[n] = s.encode("utf-8", errors="surrogateescape")
            named.append(n)
        ms = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+", s))
        if ms:
            mails[n] = sorted(ms)
        if re.search(r"sk-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{20,}|github_pat_|AKIA[0-9A-Z]{16}|(?i:api[_-]?key\s*[=:]\s*['\"][^'\"]{12,})|Bearer [A-Za-z0-9._-]{20,}", s):
            keys.append(n)
lines = ["path_in_zip\torigin\tbytes\tsha256\twhy_attached"]
for n in sorted(entries):
    org, why = origin[n]
    lines.append("\t".join([n, org.replace(NAME, "user"), str(len(entries[n])), hashlib.sha256(entries[n]).hexdigest(), why]))
entries["MANIFEST.tsv"] = ("\n".join(lines) + "\n").encode("utf-8")
UP.mkdir(parents=True, exist_ok=True)
if ZIPF.exists():
    k = 1
    while (WK / ("ANABELIAN_149_PUSH_background_before_rebuild_%d_20261113.zip" % k)).exists():
        k += 1
    shutil.copy2(ZIPF, WK / ("ANABELIAN_149_PUSH_background_before_rebuild_%d_20261113.zip" % k))
with zipfile.ZipFile(ZIPF, "w", zipfile.ZIP_DEFLATED) as zz:
    for n in sorted(entries):
        zz.writestr(n, entries[n])
shutil.copy2(P, UP / "PROMPT.md")
with zipfile.ZipFile(ZIPF) as zz:
    names = zz.namelist()
    print("zip %s: %d bytes (%.1f MB), %d entries, %.1f MB unzipped; testzip %s" % (ZIPF.name, ZIPF.stat().st_size, ZIPF.stat().st_size / 1e6, len(names), sum(i.file_size for i in zz.infolist()) / 1e6, zz.testzip()))
    pdfs = [n for n in names if n.lower().endswith(".pdf")]
    print("pdf entries:", len(pdfs), "| tex entries:", sum(1 for n in names if n.lower().endswith(".tex")), "| images:", sum(1 for n in names if n.lower().endswith((".jpg", ".jpeg", ".png"))))
print("first name replaced in", len(named), "entries:", named[:12])
own = {n: m for n, m in mails.items() if not n.startswith("literature/")}
print("e-mail addresses in our own entries:", own)
print("e-mail addresses inside literature sources (authors' addresses in the papers):", sum(len(m) for n, m in mails.items() if n.startswith("literature/")), "in", sum(1 for n in mails if n.startswith("literature/")), "files")
print("key-like strings:", keys)
print("upload folder:", sorted(p.name for p in UP.iterdir()))

# ------------------------------------------------------------------ 3. ZIP_LIST.md
zl = WK / "ZIP_LIST.md"
if zl.exists() and not (WK / "ZIP_LIST_before_build_20261113.md").exists():
    shutil.copy2(zl, WK / "ZIP_LIST_before_build_20261113.md")
out = ["# ANABELIAN_149_PUSH: files attached", "",
       "Generated by `build_zip_20261113.py` on 13 November 2026 (Claude Fable 5.2, effort max) from the table that built `ANABELIAN_149_PUSH_background.zip`; the same rows are in `MANIFEST.tsv` inside the zip, with sizes and SHA-256. LaTeX wherever a source exists; a PDF only where none does. The earlier hand-written list is `ZIP_LIST_before_build_20261113.md`.", "",
       "| Path in zip | Full source path | Why |", "|---|---|---|"]
groups = {}
for n in sorted(origin):
    org = origin[n][0]
    if org.startswith("member "):
        key = "scans/ from " + Path(org.split(" of ", 1)[1]).name
    elif "/src_arXiv_" in n:
        key = n.split("/src_arXiv_")[0] + "/src_arXiv_" + n.split("/src_arXiv_")[1].split("/")[0] + "/"
    elif n.startswith("literature/") or "/" not in n:
        key = n
    else:
        key = n.rsplit("/", 1)[0] + "/"
    groups.setdefault(key, []).append(n)
for key in sorted(groups):
    ms = groups[key]
    org, why = origin[ms[0]]
    if key.startswith("scans/ from "):
        nums = sorted({re.search(r"scan(\d+)", m).group(1) for m in ms})
        out.append("| `scans/` (%d images: scans %s) | members of `%s` | %s |" % (len(ms), ", ".join(nums), org.split(" of ", 1)[1], why))
    elif key.endswith("/"):
        out.append("| `%s` (%d files) | `%s` | %s |" % (key, len(ms), str(Path(org).parent), why))
    else:
        out.append("| `%s` | `%s` | %s |" % (ms[0], org, why))
zl.write_text("\n".join(out) + "\n", encoding="utf-8")
print("ZIP_LIST.md rows:", len(out) - 6)
