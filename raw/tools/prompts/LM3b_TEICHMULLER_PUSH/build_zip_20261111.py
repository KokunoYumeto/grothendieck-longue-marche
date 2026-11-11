# build_zip_20261111.py -- work file (Claude, Fable 5.2; 11 Nov 2026).
# Builds LM3b_TEICHMULLER_PUSH_background.zip and PROMPT.md in the upload folder, MANIFEST.tsv here and in the zip.
import io, os, sys, zipfile, hashlib, csv
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
STACK = os.path.join(ROOT, "pro_prompts_draft_20261111")
UP = os.path.join(STACK, "LM3b_TEICHMULLER_PUSH")
LM3ZIP = os.path.join(STACK, "LM3_TEICHMULLER_TOWER", "LM3_TEICHMULLER_TOWER_background.zip")
LM3MAN = os.path.join(HERE, "..", "LM3_TEICHMULLER_TOWER", "MANIFEST.tsv")
RET = os.path.join(ROOT, "pro_returns_20261111", "LM3_TEICHMULLER_TOWER")
REV = os.path.join(ROOT, "pro_reviews_20261111", "LM3_TEICHMULLER_TOWER")
DL = os.path.join(HERE, "_downloads")
sha = lambda b: hashlib.sha256(b).hexdigest()

# ---- prompt: head edits, then head + common block
hp = os.path.join(HERE, "PROMPT_head.md"); head = io.open(hp, encoding="utf-8").read()
a = "are attached, with the prompt it answered."
b = ("are attached, with the prompt it answered (`LM3_prompt/PROMPT.md`). The other folders of the zip are those of the LM3 package: `longue_marche/` (the transcription packages and their notes), "
     "`scans/`, `papers/`, `proof_packs/`, `context/`, `CATHOT_return/`, `CATHOT_review/`, `GALOIS_return/`, `STRATA_return/`, `STRATA_review/`. `MANIFEST.tsv` lists every file with its origin; "
     "the papers added for this prompt are in `papers/boggi_congruence_topologies/`, `papers/boggi_automorphisms/`, `papers/boggi_zalesskii/`, `papers/boggi_funar/`, `papers/minamide_nakamura/`, "
     "`papers/lochak_nakamura_schneps_2026/`, `papers/hoshi_mochizuki_tsujimura/`, `papers/mochizuki_global_solvably_closed/`, `papers/paris_residual_p/`, `papers/gt_shadows/`, `papers/willwacher_2026/`. "
     "The code of the LM3 answer is not attached; do not ask for it.")
if a in head: head = head.replace(a, b)
a = "open the later preprint that LM3 reports (Willwacher, arXiv:2610.15592; resolve it by title, and say so if it cannot be found) and say"
b = "read the later preprint that LM3 reports (Willwacher, arXiv:2610.15592v4, attached under `papers/willwacher_2026/`; not read by the author of this prompt) and say"
if a in head: head = head.replace(a, b)
head = head.replace("DRAFT, provisional (11 November 2026); not sent.", "DRAFT, provisional (11 November 2026).")
io.open(hp, "w", encoding="utf-8", newline="\n").write(head)
assert "LM3_prompt/PROMPT.md" in head and "papers/willwacher_2026/" in head
prompt = head.rstrip() + "\n\n---\n\n" + io.open(os.path.join(STACK, "_COMMON_BLOCK.md"), encoding="utf-8").read()
io.open(os.path.join(HERE, "PROMPT.md"), "w", encoding="utf-8", newline="\n").write(prompt)

# ---- file list
rows = []   # (path_in_zip, origin, bytes_data, note)
old = {}
for r in csv.reader(io.open(LM3MAN, encoding="utf-8"), delimiter="\t"):
    if r and not r[0].startswith("#") and r[0] != "path_in_zip": old[r[0]] = r
z = zipfile.ZipFile(LM3ZIP)
for n in z.namelist():
    if n.endswith("/"): continue
    r = old.get(n)
    rows.append((n, r[1] if r else "LM3_TEICHMULLER_TOWER_background.zip (no manifest line)", z.read(n), (r[4] if r and len(r) > 4 else "") + " [from the LM3 zip]"))
def add(zpath, src, note):
    rows.append((zpath, src, open(src, "rb").read(), note))
add("LM3_prompt/PROMPT.md", os.path.join(STACK, "LM3_TEICHMULLER_TOWER", "PROMPT.md"), "the prompt LM3 answered (Claude)")
NOTE_RET = "LM3 answer; AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 11 Nov 2026"
for f in sorted(os.listdir(RET)):
    p = os.path.join(RET, f)
    if os.path.isfile(p): add("LM3_return/" + f, p, NOTE_RET)
for f in sorted(os.listdir(os.path.join(RET, "sections"))):
    add("LM3_return/sections/" + f, os.path.join(RET, "sections", f), NOTE_RET)
add("LM3_review/REVIEW_author.md", os.path.join(REV, "REVIEW_author.md"), "review by Claude (Fable 5.2, Anthropic), 11 Nov 2026")
for f in ("check_lm3.py", "check_lm3.out"):
    add("LM3_review/checks_author/" + f, os.path.join(REV, "checks_author", f), "the reviewer's own program and output (Claude)")
URL = {
 "boggi_congruence_topologies": "https://arxiv.org/pdf/1804.06322",
 "boggi_automorphisms": "https://arxiv.org/pdf/2011.15075v6",
 "boggi_zalesskii": "https://arxiv.org/pdf/1408.5419",
 "lochak_nakamura_schneps_2026": "https://arxiv.org/pdf/2602.12462v1",
 "minamide_nakamura": "https://arxiv.org/pdf/1904.06749v2",
 "willwacher_2026": "https://arxiv.org/pdf/2610.15592v4",
 "paris_residual_p": "https://arxiv.org/pdf/math/0703703",
 "gt_shadows": "https://arxiv.org/pdf/2008.00066",
 "boggi_funar": "https://www-fourier.univ-grenoble-alpes.fr/~funar/bf_final.pdf",
 "hoshi_mochizuki_tsujimura": "https://www.kurims.kyoto-u.ac.jp/~motizuki/Combinatorial%20absolute%20Galois%20groups.pdf",
 "mochizuki_global_solvably_closed": "https://www.math.okayama-u.ac.jp/mjou/mjou48/_07_mochizuki.pdf",
}
for d in sorted(os.listdir(DL)):
    for f in sorted(os.listdir(os.path.join(DL, d))):
        rows.append(("papers/%s/%s" % (d, f), URL[d], open(os.path.join(DL, d, f), "rb").read(), "downloaded 11 Nov 2026 for LM3b; first page checked for title and authors; not read"))
names = [r[0] for r in rows]; assert len(names) == len(set(names))

lines = ["path_in_zip\tsource_path_or_url\tsha256\tbytes\tnote"]
for n, src, data, note in rows: lines.append("\t".join([n, src, sha(data), str(len(data)), note.strip()]))
body = "\n".join(lines) + "\n"
inzip = "# MANIFEST of LM3b_TEICHMULLER_PUSH_background.zip (%d files besides this one, %d bytes unzipped)\n" % (len(rows), sum(len(r[2]) for r in rows)) + body

os.makedirs(UP, exist_ok=True)
zp = os.path.join(UP, "LM3b_TEICHMULLER_PUSH_background.zip")
with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as out:
    out.writestr("MANIFEST.tsv", inzip)
    for n, src, data, note in rows: out.writestr(n, data)
zb = open(zp, "rb").read()
io.open(os.path.join(HERE, "MANIFEST.tsv"), "w", encoding="utf-8", newline="\n").write(
    "# MANIFEST of LM3b_TEICHMULLER_PUSH_background.zip (%d files with MANIFEST.tsv, %d bytes zipped)\n# zip SHA-256: %s\n" % (len(rows) + 1, len(zb), sha(zb)) + body)
io.open(os.path.join(UP, "PROMPT.md"), "w", encoding="utf-8", newline="\n").write(prompt)
t = zipfile.ZipFile(zp); assert t.testzip() is None
tops = sorted({n.split("/")[0] for n in t.namelist()})
print("files in zip:", len(t.namelist()), "zipped bytes:", len(zb), "tops:", tops)
import re
named = set(re.findall(r"`([A-Za-z0-9_]+)/", prompt))
print("folders named in PROMPT not in zip:", sorted(x for x in named if x not in tops and x not in ("sections", "code")))
print("upload folder:", os.listdir(UP))
