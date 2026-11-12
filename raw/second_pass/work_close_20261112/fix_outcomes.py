"""Close of the second pass (12 Nov 2026): the outcome of every item of the fix packages (fixes/items*.csv with Pro's
replacements answers/LM_FIX_*_fixes.csv) in the current second-pass texts. Reads fix_status.tsv (written by
fix_status.py before the close merge) and writes fix_outcomes_20261112.tsv. usage: python -I fix_outcomes.py"""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(__file__).resolve().parent
# decisions of the close (12 Nov), checked against the scans where the fix changes the reading
D = {
    "LM_FIX_03-020": "REJECTED: scan 417 (140-2): the annotation under the strike reads «comm.?» (c-o-m-m), not «canon.?»; "
                     "the second pass's tikz-cd and description («non|pas comm.?», thickened ends) stay",
    "LM_FIX_04-002": "SETTLED BY THE SECOND PASS: P05 change 10 drew the prism in tikz-cd from the scan; Pro's f^0 not taken "
                     "(the mark is the f's detached top hook)",
    "LM_FIX_04-012": "SETTLED BY THE SECOND PASS: the second pass reads \\unsure{\\mathrm{lac}} where Pro kept the mark",
    "LM_FIX_04-013": "SETTLED BY THE SECOND PASS: the second pass reads \\unsure{\\mathrm{lac}} where Pro kept the mark",
    "LM_FIX_08-009": "SETTLED BY THE SECOND PASS: the mark on scan 270 is resolved in the second-pass text",
    "LM_FIX_08-018": "ALREADY IN: the text equals Pro's display",
    "LM_FIX_10-001": "ALREADY IN: «des \\deleted{courbes algébriques} \\inserted{surfaces} \\deleted{\\unsure{compactes}}»",
    "LM_FIX_11-022": "APPLIED (LM_P046_checked_fixed.tex): scan 451 (140-2): the struck mark after -z is raised; now "
                     "\\unsure{-z}^{\\deleted{\\illegible{1}}}",
    "LM_FIX_14-026": "REJECTED: scan 107 (140-3): the struck cluster after «S=» is longer than «ad»; the second pass's "
                     "\\illegible{1} after \\unsure{ad} stays",
    "LM_FIX_14-027": "APPLIED (LM_P068-069_checked_fixed.tex): scan 107 (140-3): a c is legible after the hatched block; "
                     "now \\deleted{\\illegible{1}c}=\\delta+c(...)",
    "LM_FIX_16-002": "SETTLED BY THE SECOND PASS: it reads u where the first pass and Pro had \\unsure{u|bu}",
    "LM_FIX_16-025": "APPLIED (LM_C3-321-339_checked_fixed.tex): scan 329 (140-3): after the struck «v+w^2=» only the "
                     "strike line continues; the \\illegible{1} operand is removed, as Pro gives it",
    "LM_FIX_03-008": "SETTLED 8 Nov: drawn by hand in the second-pass text (manual_LM_FIX_03_P038_checked.py)",
    "LM_FIX_03-009": "SETTLED 8 Nov: drawn by hand in the second-pass text (manual_LM_FIX_03_P038_checked.py)",
    "LM_FIX_03-010": "SETTLED 8 Nov: drawn by hand in the second-pass text (manual_LM_FIX_03_P038_checked.py)",
}
for i in ("01-016", "01-018", "01-020", "02-008", "09-016", "10-016"):
    D["LM_FIX_" + i] = ("SETTLED BY THE SECOND PASS (8 Nov, classify_not_carried.py): the scan page no longer has the "
                        "description or mark the fix was for")
NOREAD = "NOTHING TO MERGE: Pro keeps the mark (no reading); the second-pass text already has it"
for i in ("05-015", "06-004", "06-012", "06-015", "08-006", "08-013", "11-023", "11-025", "11-026", "12-021",
          "12-025", "13-009", "13-010", "16-014", "16-016"):
    D["LM_FIX_" + i] = NOREAD
rows = [l.split("\t") for l in (W / "fix_status.tsv").read_text(encoding="utf-8").splitlines()]
out = ["item\tpackage\tscan\tkind\tsecond_pass_input\tfix_in_input\tcurrent_file\tstate_before_close\toutcome"]
tally = {}
for r in rows:
    iid, pkg, scan, kind, inp, infp, cur, st = r
    if iid in D:
        o = D[iid]
    elif "12Nov outcome" in st:
        o = "12 Nov merge: outcome in merge_fixes_open.md"
    elif inp == "fixed" and infp in ("rep", "neither"):
        o = ("IN THE SECOND PASS'S INPUT: applied to the fixed first pass, then checked by the second pass"
             + ("" if "rep in" in st else " (which changed it)"))
    elif "rep in" in st:
        o = "ALREADY IN: merged 8 Nov (merge_fixes_into_checked.py, fuzzy_merge.py)"
    else:
        o = "OPEN"
    k = o.split(":")[0].split(" (")[0]
    tally[k] = tally.get(k, 0) + 1
    out.append("\t".join(r + [o]))
(W / "fix_outcomes_20261112.tsv").write_text("\n".join(out) + "\n", encoding="utf-8")
for k, v in sorted(tally.items(), key=lambda x: -x[1]):
    print(v, k)
print("items:", len(rows))
