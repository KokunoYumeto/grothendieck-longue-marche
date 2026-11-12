"""Write each fix's outcome on its line of second_pass/merge_fixes_open.md (dated copy:
work_merge_20261112/merge_fixes_open_20261112_before.md). usage: python -I record_outcomes.py"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(__file__).resolve().parent
P = W.parent / "merge_fixes_open.md"
F = "fuzzy_merge.py, 8 Nov"
OUT = {
    "01-013": "APPLIED: the display I=S_0(K̄)⊂S(K̄) [vide ssi S=∅] and the bracketed description are now one tikz-cd "
              "with S(K̄), a vertical ≃ and S_0(K̄)∧_ΣΓ under it, so S(K̄) is not doubled (Pro's note). Scan 110: "
              "the vertical sign is a wavy and a straight stroke, as Pro reads.",
    "01-014": "ALREADY IN: the second pass reads «sinon pas de pb», Pro's missing word. Pro's \\inserted over the whole "
              "remark not taken: on scan 118 «cas ν=1,» is on the line; only «dans le» is above it.",
    "09-008": "REJECTED: on scan 112 the struck mark after S̄'_0 is buried in the cancellation loops; its left end "
              "points left but its right end is a loop, not a head. ↔ is not in the ink; \\deleted{\\illegible{1}} "
              "stays.",
    "09-009": "APPLIED, one letter changed: scan 126 shows a lowered U and a comma, then an E-shaped letter with a "
              "small i, all struck. Written \\unsure{E|e}: it looks like a capital E (Pro: e).",
    "01-021": f"ALREADY IN ({F}). Scan 154 agrees: B_J → B_E with ρ? above the arrow.",
    "01-022": f"ALREADY IN ({F}). Scan 154 agrees: B_E → B_J, vertical ≃ under both, π-Ens and Ens. sur J.",
    "01-025": f"ALREADY IN ({F}). Scan 159 agrees (margin): 1→T→E_i→Γ_i→1, vertical ≃ and T under E_i, dotted "
              "n_i id_T.",
    "01-026": f"ALREADY IN ({F}). Scan 163 agrees: ρ_i stroke without a head, σ_i arrow to Γ_i, overwritten "
              "letters.",
    "01-030": f"ALREADY IN ({F}), one correction: on scan 166 the Π_1 of the bottom object is hatched out, so it is "
              "now B_{\\deleted{\\unsure{\\Pi_1}}X}, as the paragraph above writes it.",
    "01-031": f"ALREADY IN ({F}). Scan 170 agrees in outline: two diamonds, [B_{{D_1^*}}] with a dotted arrow, the "
              "broken B_U—B_U link, braces U_1 and X, the struck label.",
    "02-003": "REJECTED: on scan 178 the short stroke between B_{D*} and B_S has no head at its top; it thickens and "
              "curls at its lower end. Pro's upward arrow is not in the ink; the second pass's description (arrow "
              "B_{D*}→B_S or insertion mark) stays.",
    "09-013": "APPLIED: \\deleted{\\unsure{\\geq}2} before 2-2g. Scan 182: a struck sign shaped like his ≥ in "
              "«ν≥2» on the same line, then a clear 2.",
    "02-007": f"ALREADY IN ({F}). Scan 212 agrees: the two rows, the curved Γ_{{g,ν}} strokes, the hooked inclusions, "
              "∥ down to [(A°_{g,ν})_a].",
    "09-021": "APPLIED: ≃ℂ is legible on scan 215. As Pro's note says, the ink has U_{0,1}, not U_{g,ν}; corrected "
              "in the same struck note.",
    "09-022": "APPLIED: on scan 217 (diagonal margin note) the struck matter is inside the subscript of A: "
              "G×A°_{g,[struck]ν+k}, not a factor before A.",
    "09-023": "ALREADY IN (the second pass has the same reading). Scan 225: struck Γ_g before (51 bis).",
    "02-010": f"ALREADY IN ({F}), completed: the display (65) above the diagram repeated its top row; removed, as the "
              "fix's scope says. Scan 236 has one (65) line, with a vertical ≃ and Π_2(S^3)=0 under its last term. "
              "The struck Sl(2,ℂ) keeps the second pass's spelling.",
    "02-012": "APPLIED: scan 246 shows three arrow strokes at T (the middle one retraced) and two at the gerbes, "
              "with ≃/∼ marks.",
    "09-025": "APPLIED: scan 254: struck (·,1), parentheses, comma and 1 legible; v^{-1} tentative under the "
              "hatching.",
    "09-026": "APPLIED: scan 254: struck subscript of ρ with a tilde stroke, an A-like body and g,ν below.",
    "10-002": "ALREADY IN (the second pass has the same reading). Scan 256: struck word under «ℂ algébriques».",
    "02-013": f"ALREADY IN ({F}). Scan 265 agrees: top and left strokes without heads, f_U and ρ arrows, the α curve "
              "up to the right.",
    "02-019": f"ALREADY IN ({F}). Scan 299 agrees: B_I→B_{{D^*}}, both verticals down, pt.s→B_U, the curve to the "
              "upper left labelled isom de comm.",
    "10-007": "ALREADY IN: the mark is no longer \\illegible; the second pass reads \\unsure{s_\\nu|g,\\nu}, which "
              "contains Pro's g,ν. Both kept: on scan 300 the first letter is smudged and may be s (cf. «le dernier "
              "élément s_ν» just after).",
    "10-009": "ALREADY IN: Pro's row keeps \\deleted{\\illegible{1}} (unresolved); the text is already the same.",
    "10-011": "APPLIED: scan 318: after the first commutator a second bracket [x,y] and an ℓ with a small subscript "
              "under the hatching; all of it \\unsure.",
    "02-022": f"ALREADY IN ({F}). Scan 329 agrees: struck Π̂ before Ĝ, thick arrow down, Aut[struck ext]_lac, "
              "= Ĝ̂ and = T̂̂ below.",
    "10-013": "REJECTED: on scan 323 the struck argument ends with π and a ♮-shaped mark (π^♮ is written so "
              "elsewhere on the page); Pro's (π) drops it. The second pass's \\deleted{\\unsure{(\\pi_0^{\\natural})}} "
              "stays.",
    "10-015": "APPLIED: scan 327: the last struck glyph has a long top bar and a short stem: \\unsure{\\Gamma}.",
    "10-017": "APPLIED, one part not taken: the struck double hat over 𝒯_{g,ν} (scan 339) is in; 𝒯_{g,ν} stays "
              "certain (clear on the scan; Pro had made it \\unsure).",
    "03-002": f"ALREADY IN ({F}). Scan 348 agrees: three rows, hooked verticals, ∥ between the π̂, struck word under "
              "the middle T̂.",
    "10-024": "APPLIED: scan 347: the struck glyph after Γ_Σ= is a calligraphic T with two hats.",
    "03-013": f"ALREADY IN ({F}). Scan 400 agrees: two ∪-shaped inclusion signs, ∥, ψ_i^{{'-1}}(T̂ with no closing "
              "parenthesis.",
}
t = P.read_text(encoding="utf-8")
lines, seen = [], set()
for ln in t.split("\n"):
    m = re.match(r"^- LM_FIX_(\d\d-\d\d\d) ", ln)
    if m and m.group(1) in OUT:
        seen.add(m.group(1))
        ln = ln + " | 12 Nov: " + OUT[m.group(1)]
    lines.append(ln)
assert seen == set(OUT), set(OUT) - seen
head = ("# Fixes still to merge by hand into second-pass texts\n\n"
        "Outcomes of 12 Nov 2026 after each line (checked against the scans; files: second_pass/PKG_checked_fixed.tex; "
        "work files and the dated copy of this list: second_pass/work_merge_20261112/). Applied 12, rejected 3, already "
        "in 18.")
out = "\n".join(lines).replace("# Fixes still to merge by hand into second-pass texts", head, 1)
P.write_text(out + "\n", encoding="utf-8")
print(len(seen), "outcomes written")
