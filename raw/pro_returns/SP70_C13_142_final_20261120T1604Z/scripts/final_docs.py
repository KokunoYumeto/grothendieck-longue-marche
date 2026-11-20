"""Reconcile final documentation with the completed primary-reader decisions.

This is an idempotent metadata/report step. It performs no image reading.
"""
from pathlib import Path
import sys, csv
sys.path.insert(0, str(Path(__file__).resolve().parent))
import record as r
import audit as a

notation = [
    (r"G_J; G_3; \widetilde G_3",
     "Open coiled capital G with an interior bar. Its connected upper flourish is "
     "not a separate tilde. Use the same ordinary G rendering throughout; the "
     "genuine detached tilde on G_3 in029 remains. This resolves the initial "
     "026–027 alternative, without changing the written J versus 3 indices.",
     "026–030, 033–034, 036, 039, 044–045, 051"),
    (r"\overline{\underline{\mathrm{I}}} ... \overline{\underline{\mathrm{VIII}}}",
     "Roman graph/groupoid names generally have common upper and lower horizontal "
     "strokes. Render those explicitly where seen. The two II forms on027 also "
     "have distinct pointed hats; the III in028 has no such hat. Keep the "
     "unframed V in039. Framing is not interpreted as a completion operation.",
     "026–030, 033–034, 036, 038–040"),
    (r"\omega,\omega'; {}'\omega",
     "Omega is a two-lobed w-like stroke. A detached short tick is a prime. "
     "Keep the written position of primes, especially040 (71)–(72); retain "
     "cancelled/overwritten ticks as doubtful rather than inventing stars.",
     "026–042, 050–051"),
    (r"\widetilde a,\widetilde b,\widetilde d; a,b,c,d",
     "Path tildes are separate accents. Preserve local absent tildes and the "
     "source's differing inverse-path notation. The angular small alpha accent "
     "in028 is a tilde by the locally defined notation; the isolated hat in035 "
     "is kept as written.",
     "026–041, 050–051"),
    (r"\gamma=(p-1)/2",
     "The curved entrance of live gamma on027 is part of the letter, not a minus. "
     "The crossed draft at (24) has a separate minus. Here p is Latin p, not rho.",
     "027–028"),
    (r"\zeta,\zeta',\zeta_1",
     "Angular upper stroke and one long lower curve. Final cross-page comparison "
     "reads the parameter introduced in030 consistently as zeta, including "
     "primed/subscripted forms. C's xi spelling in this run is corrected; this "
     "does not resolve the unrelated buried xi-like cancellations on026/029.",
     "030–041"),
    (r"\rho,\rho^{-1}; \sigma_\infty,\tau_\infty,\varepsilon_0",
     "Automorphism letters and inverse exponents remain distinct. The question "
     "rho inverse? on031 and the cancellations on036–039 are retained. The "
     "overwritten operator in031 (43) remains sigma/tau uncertain.",
     "026–042"),
    (r"\Pi_{0,3},\widehat\Pi_{0,3}; \pi_1,\pi",
     "Capital Pi with the 0,3 subscript is distinguished from the local "
     "lower-case pi notation. Hats and base-point subscripts are retained "
     "individually; no completion marker is supplied by expectation.",
     "026–042"),
    (r"\Pi_0,\Pi_1",
     "The later component and fundamental-groupoid symbols have capital Pi, "
     "rather than H's occasional lower-case pi.",
     "044, 048–050"),
    (r"H",
     "Two upright strokes and a crossbar in all six exponents of the right "
     "marginal substitutions. It is not mu or an adjacent multiplicative factor.",
     "037"),
    (r"\uline{\bar\omega}; \uline{\omega}; \uline{\varepsilon}",
     "Three two-element orientation/component sets in044 (3). The first has an "
     "upper bar as well as an underline; cyclic-order omega has no upper bar. "
     "The overwritten second orientation-set glyph on050 remains explicitly "
     "barred/unbarred uncertain. The clear opening form on051 has both strokes.",
     "044–051"),
    (r"R_i^\omega; R_{i\omega}; R_J; I,J",
     "Keep visible index position and alphabet differences: raised omega in050 "
     "(16), lowered i-omega in its live explanatory line, capital J at the end "
     "of044, and I in046 (10) and047 (12). These are not homogenized.",
     "044, 046–047, 050"),
    (r"\Sigma^*,\Sigma',\widetilde\Sigma,\widetilde\Sigma^\circ",
     "The punctured sphere, projective blow-up, cut surface and its interior "
     "carry distinct written modifiers. None is replaced by the other because "
     "a later identification is asserted.",
     "046–051"),
    (r"T^*/\mathbb R^*; T^*/\mathbb R^{*+}",
     "The stars and the second quotient's plus are distinct written signs in "
     "the projective/tangent-direction annotations. No expansion of the star "
     "notation is substituted into the manuscript.",
     "047"),
    (r"\widetilde\Sigma^{(\varepsilon)}",
     "The left NB uses a parenthesized raised epsilon and a crossed lower "
     "epsilon-like remnant at both occurrences.",
     "050"),
    ("Dec / Dic",
     "Upper inserted cutting notation Dec has medium confidence; the later "
     "body occurrence has a visible dotted i and is read Dic. Neither an "
     "accent nor uniform spelling is supplied.",
     "051"),
    ("= and =s in prose",
     "Written equality can abbreviate même/mêmes. Preserve the sign and its "
     "written s; distinguish this from equality in a displayed formula.",
     "034, 038, 040"),
    ("double quotation marks",
     "Paired ordinary quotation strokes are represented by two opening "
     "backticks and two closing apostrophes, following the supplied convention.",
     "045–046, 048–049"),
    ("insertions, deletions and frames",
     "Retain local cancellation scope and insertion attachment. A rounded "
     "frame or a shared Roman-numeral bar is not an erasure. Conversely a "
     "hatched old symbol is not omitted because its replacement is legible.",
     "all24 scans"),
]
with (r.W / "NOTATION.tsv").open("w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["sign", "form", "scans"])
    w.writerows(notation)

extra_abbreviations = [
    ("NB", "nota bene", "026–030, 037, 044, 050–051"),
    ("i.e.", "id est / c'est-à-dire", "030–031, 035–037, 039–040, 044, 050–051"),
    ("cf / cf.", "confer / comparer", "028, 030, 044"),
    ("p.", "page", "030"),
    ("Hom.", "homomorphisme (tentative cancelled reading)", "033"),
    ("rel.", "relation(s) or relative (uncertain cancelled context)", "028"),
    ("équiv.", "équivaut / équivalente (completion not imposed in text)", "044"),
    ("sg", "signature / signe d'une permutation", "029, 045–046"),
    ("def", "définition (label above equality)", "048, 050"),
    ("Rev ét / Rev et", "revêtements étales (the local accents remain as written)", "048"),
    ("Rep", "repères (tentative explanation of ordered triples)", "051"),
]
abbr = r.read("ABBREVIATIONS.tsv")
known = {(x["abbreviation"], x["scans"]) for x in abbr}
for short, expansion, scans in extra_abbreviations:
    if (short, scans) not in known:
        r.append("ABBREVIATIONS.tsv", [short, expansion, scans])

path = r.W / "SP70_C13_142_notes.md"
s = path.read_text()
s = s.replace(
    "The angular parameter is provisionally fixed as zeta throughout the page; "
    "cross-page notation comparison remains necessary.",
    "The final cross-page comparison confirms zeta for this parameter and its "
    "later occurrences; the cancelled xi-like signs on026/029 are separate "
    "unresolved readings.")
s = s.replace(
    "the last number is overwritten and remains 79|78.",
    "the last number is overwritten and was resolved as79 at medium confidence "
    "in the second reading: a dark upper loop and descending right stem remain "
    "over an older lower-loop trace.")
old = "This is a notation decision, not a proof of (26) or (30)."
new = old + (
    " Final comparison of the Roman groupoid names also removed the hat supplied "
    "by both witnesses above III in the endomorphism paragraph: the enlarged "
    "ink has only the common upper and lower numeral bars, unlike the distinct "
    "hats on027.")
if new not in s:
    s = s.replace(old, new)
path.write_text(s)

path = r.W / "SP70_C13_142_hand_log.md"
s = path.read_text()
s = s.replace(
    "The interpretation is provisional pending the later notation comparison; "
    "no universally reliable alphabet distinction is claimed.",
    "This was provisional at the first reading. The completed comparison, "
    "recorded below, resolves both occurrences as G_J; it does not establish a "
    "universal rule for every unrelated coiled sign.")
s = s.replace(
    "Adopt zeta consistently on this page, medium confidence, to be compared "
    "with later definitions. This does not yet establish a universal habit "
    "for every Greek squiggle.",
    "The initial zeta reading was kept at medium confidence. The completed "
    "comparison with its later occurrences confirms this parameter as zeta "
    "throughout030–041; it does not resolve unrelated cancelled Greek signs.")
s = s.replace(
    "The final digit in 79|78 is overwritten and does not establish a uniform "
    "numbering correction.",
    "The final digit was initially79|78; the second reading resolved79 at "
    "medium confidence from its surviving upper loop and descending right "
    "stem. This is not a uniform numbering correction.")
heading = "### Final comparison: Roman numeral bars and hats"
if heading not in s:
    s += (
        "\n" + heading + "\n\n"
        "The common upper and lower strokes of the Roman graph names are now "
        "rendered explicitly on026–030, consistently with033–040. On027 the two "
        "pointed hats are separate above the upper bars. In028, the allegedly "
        "hatted III has no separate pointed stroke: both witnesses mistook the "
        "curved upper numeral bar for a hat. The V at the right of039 remains "
        "unframed. The tiny doubtful II-like subscript under rho on029 is not "
        "treated as a graph name or supplied with framing.\n\n"
    )
path.write_text(s)

# Keep mechanically repaired enum strings canonical in the current register.
rows = r.read("CHANGES.tsv")
for row in rows:
    row["kind"] = row["kind"].replace(r"\\ill{}", r"\ill{}")
a.write_rows("CHANGES.tsv", rows)
a.rebuild_collation()

# Minor prose spacing in the new comparison documentation.
for name in ("AUDIT.md", "NOTATION.tsv",
             "SP70_C13_142_notes.md", "SP70_C13_142_hand_log.md"):
    p = r.W / name
    text = p.read_text()
    import re
    text = re.sub(r"(?<=[A-Za-z])(?=0(?:2[6-9]|3[0-9]|4[0-9]|5[01])\b)", " ", text)
    text = text.replace("all24", "all 24").replace("as79", "as 79")
    text = text.replace("initially79", "initially 79").replace("resolved79", "resolved 79")
    text = text.replace("rotation0", "rotation 0")
    p.write_text(text)
r.refresh()
