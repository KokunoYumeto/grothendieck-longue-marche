"""Apply the primary reader's final cross-page notation decisions once.

This script records decisions already made visually. It does not recognise ink.
The ordered whole-page second reading had been completed before this comparison.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import audit as a
import record as r

marker = "final notation comparison recorded"
assert marker not in (r.W / "progress.log").read_text(), "Already applied"

def framed(roman):
    return r"\overline{\underline{\mathrm{" + roman + "}}}"

def save(n, text):
    (r.W / f"pages/142_scan{n:03}.tex").write_text(text)

def bars(place, old, final, evidence, h=None, crop="page", marked="no"):
    a.add(place, old, old if h is None else h, final, evidence,
          dc=True, dh=True, kind="misread symbol or index", cat=1,
          crop=crop, marked=marked)

# G is one recurring letter. The temporary calligraphic macro did not denote a
# second alphabet in the source; C's ordinary G rendering is used consistently.
for n in (26, 27, 51):
    t = a.begin(n)
    old = t
    t = t.replace(r"\mathcal G", "G")
    if old != t:
        a.log("consistent rendering of the group capital",
              r"\mathcal G_J", "G_J",
              "Same open G with an interior bar and a connected upper flourish; "
              "render consistently with C's G convention. Macro/font rendering "
              "alone is not a new divergence row.",
              view="completed visual readings and final notation comparison")
        save(n, t)

rows = r.read("CHANGES.tsv")
for row in rows:
    row["final"] = row["final"].replace(r"\mathcal G", "G")
    row["kind"] = row["kind"].replace(r"\\ill{}", r"\ill{}")
a.write_rows("CHANGES.tsv", rows)
a.rebuild_collation()

# The common upper and lower horizontal strokes are part of the written Roman
# graph names. A separate pointed hat, where actually present, remains separate.
t = a.begin(26)
assert t.count(r"\mathrm{II}") == 1
t = t.replace(r"\mathrm{II}", framed("II"))
a.amend("026-23",
        final="TikZ figure, with the caption " + framed("II") + "_J",
        against_C="yes",
        scan_shows="Three puncture dots, six R endpoints, three Q junctions, "
        "paired a arcs and six c arcs. The caption II_J has common upper and lower "
        "horizontal strokes, now rendered explicitly. No Q_1 label is supplied "
        "where none is written.")
save(26, t)

t = a.begin(27)
assert t.count(r"\mathrm{II}") == 3
t = t.replace(r"\mathrm{II}", framed("II"))
for place, tail, hat in [
    ("opening groupoid label", "_J", True),
    ("opening subgroupoid label", "_{J,i}", True),
    ("opening unhatted subgroupoid label", "_{J,i}", False),
]:
    old = (r"\widehat{\mathrm{II}}" if hat else r"\mathrm{II}") + tail
    final = ((r"\widehat{" + framed("II") + "}") if hat else framed("II")) + tail
    bars(place, old, final,
         "Two upright strokes are joined by a common upper and lower bar. "
         + ("A distinct pointed hat stands above the upper bar and is retained."
            if hat else "No separate pointed hat is present."))
save(27, t)

t = a.begin(28)
assert t.count(r"\mathrm{III}") == 3 and t.count(r"\mathrm{II}") == 2
t = t.replace(r"\widehat{\mathrm{III}}", framed("III"))
t = t.replace(r"\mathrm{III}", framed("III"), 1)
# The remaining plain III is the figure caption; avoid rewrapping the two
# occurrences already framed by targeting the exact caption.
t = t.replace(r"\node at(-2,-1.55){$\mathrm{III}_J$};",
              r"\node at(-2,-1.55){$" + framed("III") + r"_J$};")
t = t.replace(r"\mathrm{II}", framed("II"))
for place, roman in [
    ("inserted name of the induced groupoid", "III"),
    ("inserted name of the preceding groupoid", "II"),
    ("sphere caption: Roman numeral bars", "III"),
]:
    bars(place, r"\mathrm{" + roman + "}_J", framed(roman) + "_J",
         "The Roman numeral has a common horizontal upper stroke and a common "
         "lower stroke, both distinct from its vertical stems.")
bars("endomorphism paragraph: groupoid hat and bars",
     r"\widehat{\mathrm{III}}_J", framed("III") + "_J",
     "The tight crop shows three vertical stems, one shallow curved upper bar "
     "and one lower bar. There is no additional pointed hat above them. Both "
     "witnesses supplied a hat, unlike the separately hatted II forms on scan027.",
     crop="028 (1490,1240,1660,1410), rotation 0",
     h=r"\widehat{\mathrm{III}}_J")
a.amend("028-19",
        final="comparer à la définition dans le groupoïde "
              + framed("II") + "_J !",
        against_C="yes",
        scan_shows="The parenthetical words are legible along the lower passage; "
        "the Roman II in the groupoid name also has a common upper and lower bar, "
        "rendered explicitly in the final notation comparison.")
save(28, t)

t = a.begin(29)
assert t.count(r"\mathrm{III}") == 1
t = t.replace(r"\mathrm{III}", framed("III"))
a.amend("029-03", final=framed("III") + "_{J,i}", against_C="yes",
        scan_shows="The slanted marginal Roman III has its common horizontal "
        "top and bottom bars, rendered explicitly; no separate pointed hat is "
        "present. This agrees with the clearer groupoid-label forms.")
save(29, t)

# Split the audit's aggregate Roman-label row into its individual locations.
# The final IV occurrence is already covered by 030-14, and is not counted twice.
t = a.begin(30)
a.amend("030-14", final=framed("IV") + "_J", against_C="yes",
        scan_shows="IV has common upper and lower horizontal framing strokes, "
        "but no separate pointed hat. The framing is not assigned a completion "
        "meaning.")
a.amend("030-29",
        place="sphere caption: Roman numeral bars",
        C=r"\mathrm{IV}_J", H=r"\mathrm{IV}_J",
        final=framed("IV") + "_J",
        scan_shows="The IV caption has common upper and lower horizontal strokes "
        "around the Roman letters.")
for place, roman in [
    ("equivalence sentence: first groupoid label", "III"),
    ("equivalence sentence: second groupoid label", "IV"),
    ("after (35): constitutive-relations groupoid label", "III"),
]:
    bars(place, r"\mathrm{" + roman + "}_J", framed(roman) + "_J",
         "The written Roman groupoid label has common upper and lower horizontal "
         "strokes; these are reproduced without an inferred completion hat.")
save(30, t)

# Syntax-only separations exposed when uncertain wrappers were removed.
t = a.begin(44)
assert r"\simeqG" in t and r"\setminusV" in t
t = t.replace(r"\simeqG", r"\simeq G").replace(r"\setminusV", r"\setminus V")
a.log("TeX control-word separators", r"\simeqG; \setminusV",
      r"\simeq G; \setminus V",
      "Syntax-only delimiters after the selected macros; no manuscript reading "
      "or divergence count changes.", view="mechanical token inspection")
save(44, t)

with (r.W / "AUDIT.md").open("a") as f:
    f.write(
        "## Final cross-page notation comparison\n\n"
        "After the ordered second reading of all24 pages, the primary reader "
        "compared the Roman groupoid labels on scans026–030 with the forms already "
        "read on033–040. The original page views026–029 were consulted specifically "
        "for this comparison. One newly identified ambiguity in028 was enlarged "
        "once at (1490,1240,1660,1410), rotation0: its supposed completion hat is "
        "only the upper Roman-numeral bar. Common upper/lower strokes are now "
        "rendered consistently where seen; the distinct hats on027 and the "
        "unframed V on039 remain. This was a notation comparison, not a new "
        "unordered substitute for the completed second reading.\n\n"
        "The coiled acting-group capital is rendered G throughout. Its connected "
        "flourish is not an independent tilde; the genuine tilde on G_3 in029 "
        "remains. The parameter introduced on030 is zeta throughout its later "
        "occurrences; unrelated, buried cancelled xi-like signs are not forced "
        "into that reading. Written prime positions, missing tildes, omega versus "
        "epsilon, and Dec/Dic variations remain local source differences.\n\n"
    )
with (r.W / "progress.log").open("a") as f:
    f.write(marker + " " + r.now() + "\n")
a.rebuild_collation()
r.refresh()
