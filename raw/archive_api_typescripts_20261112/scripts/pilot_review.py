r"""Write pilot/pilot_review.tsv: the automatic verdicts of pilot_eval.py with the verdicts of the review by hand
(crops in pilot/crops). usage: python pilot_review.py"""
import csv
import pathlib
from collections import Counter

BASE = pathlib.Path(__file__).resolve().parent.parent
OVER = {
    "roman s, t, k": ("missed", "not reported (the prompt told the model not to list font conventions)"),
    "'stablilise' -> 'stabilise'": ("missed", "transcribed 'stabilise'; the scan has the misspelling (crop ps_134-2_044_stab_zoom.png): the API followed the draft"),
    "struck 'pouvoir' printed ('pour espérer pouvoir conclure')": ("missed", "'pouvoir' is struck on the scan (crop ps_134-2_044_pouvoir.png) but transcribed as live text, as in the draft"),
    "commas after '(non-ordered simplices)', 'boundary maps)', one removed": ("missed", "not reported"),
    "handwritten '1' and '7' of the N.B.": ("missed", "transcribed as superscripts without the handwriting mark (crop m_esq3.png)"),
    "'point ξ de X à valeurs dans k′'": ("missed (disputed)", "API reads 'k' and a handwritten comma; the stroke after k is comma-like (crop m_kint.png); the check read k′; the scan does not decide"),
    "'Je n'ai pas encore rédigé le n° 16'": ("caught", "API: 'rédi\\unsure{-}': the line runs into the page edge and only 'rédi' is visible (crop ega25_002_redige.png)"),
    "'m_x' (lower-case x)": ("caught", "\\underline{m}_x (the regex did not allow the underline)"),
    "'Remarques 2'": ("caught", "\\uline{Remarques} 2 (the regex did not allow the underline)"),
    "'in Â' not printed in '(ii) The product of two W-aspheric objects [in Â]'": ("caught", "transcribed \\inserted{in $A^\\wedge$}; not listed as hand-missing"),
    "closing quotation mark after 'pour 0<=i<=n'": ("caught", "the transcription has the closing quotes after i=n+1, which the draft lacks; not listed"),
    "'nothing on'": ("caught; the check corrected", "typed above the line, not handwritten (crop m_typed.png); API: \\inserted[typed]{nothing on}"),
    "'handy criterion'": ("caught; the check probably corrected", "API: \\inserted[typed]{...} after a typed strike-out"),
    "'one or the other'": ("caught; the check probably corrected", "API: \\inserted[typed]{...}"),
    "'but only'": ("caught; the check probably corrected", "API: \\xout{xxxxxxxx}\\inserted[typed]{but only}"),
    "'cases'": ("caught; the check probably corrected", "API: \\inserted[typed]{cases}"),
}


def main():
    rows = list(csv.reader(open(BASE / "pilot" / "pilot_auto.tsv", encoding="utf-8"), delimiter="\t"))
    out = [rows[0] + ["reviewed_verdict", "review_note"]]
    for r in rows[1:]:
        v, n = OVER.get(r[2], ("caught" if r[5] == "caught" else "missed", ""))
        out.append(r + [v, n])
    with open(BASE / "pilot" / "pilot_review.tsv", "w", encoding="utf-8", newline="") as f:
        csv.writer(f, delimiter="\t", lineterminator="\n").writerows(out)
    c = Counter((r[0].split("_")[0], r[-2].startswith("caught")) for r in out[1:])
    print(sorted(c.items()))
    ok = sum(1 for r in out[1:] if r[-2].startswith("caught"))
    print(ok, len(out) - 1, round(ok / (len(out) - 1), 4))


if __name__ == "__main__":
    main()
