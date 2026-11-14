#!/usr/bin/env python3
"""Write the exact requested CSV schemas for the local-stratification fragment."""
import csv
from pathlib import Path

root = Path(__file__).resolve().parents[1]
schema = ["id", "statement", "status", "where_proved", "depends_on",
          "manuscript_passages (section; folio; scan)",
          "depends_on_doubtful_reading (scan, alternatives)", "notes"]
rows = [
    ["F.31", "Global stratifications form a separated presheaf but not a sheaf; its sheafification is compatible local atlases and gives intrinsic leaves.", "Proved", "F_local.tex, F.31", "Local connectedness; frontier condition; connected boundary germs", "MPL 147; section 13, folios 86-87; scans 181-184", "182: deleted separated versus inserted a sheaf; margin known locally", "Full proof of restriction including local finiteness and frontier condition. Circle with one marked point is an explicit sheaf counterexample satisfying e locally. Compact-Hausdorff qualification for local compactness."],
    ["F.32", "Germ flag spaces satisfy every Segal homeomorphism and form a topological category; literal first-vertex maps are finite coverings on all D0.", "Proved", "F_local.tex, F.32", "F.31 and connected germ axiom d", "MPL 147; section 13, folios 88-90; scans 185-189", "185: open in Sigma_0 versus Sigma_*; 187: origin lies in closure X_i; degeneracy isomorphisms; 189: special-to-SNC aside", "Uses actual germ topology and weak chains. Degeneracies are isomorphisms onto repeated-entry summands, not onto an entire next degree. Refutes special-to-SNC scope of (304) in literal chart model."],
    ["F.33", "Axiom e forces a stationary conical link for punctured neighbourhoods.", "Refuted", "F_local.tex, F.33", "Explicit one-ended infinite-genus surface; pro-Mittag-Leffler image criterion proved in text", "MPL 147; section 13, folios 86 and 90; scans 181-182 and 190", "190: e will express locally trivial tubes; counterexample satisfies either local or entire-stratum product reading", "One-point compactification satisfies a-e but tail H1 images strictly decrease at every stage. No constant pro-homology and no conical fixed-link model."],
    ["F.34", "Full elementary pro-topoi satisfy neighbourhood gluing; controlled compact conical links give bundle and shape models, with exact 1-type replacement criterion and both requested tests.", "Proved", "F_local.tex, F.34", "F.12-F.14; open sheaf descent; filtered mapping categories; Mather 1970 section 7 and Corollaries 10.2-10.6; STRATA C.3 C.5 C.6 audited", "MPL 147; section 13, folio 90; scan 190; gluing scans 150 and 155", "190: three half-lines are in a plane and written count is seven; e is an announced future application", "Full sheaf pro-object is never silently replaced by a homotopy or covering model. Extra conical/control hypotheses explicit; e alone insufficient. S2 point gives suspension S1 and loses H2 under ordinary groupoid colimit. Three rays give seven strata and an S1 link."],
]
with (root / "local_results.csv").open("w", newline="") as f:
    w = csv.writer(f)
    w.writerow(schema)
    w.writerows(rows)

read_schema = ["package", "scan", r"the \unsure or \illegible place", "what the mathematics supports", "how strongly"]
readings = [
    ["MPL_147_138-190", "181-182", "d: connected topological germ; e: deleted local before product and transverse pi0 cardinal one", "Use the explicitly explained fundamental neighbourhood basis with connected stratum intersection. The counterexamples satisfy both local and whole-stratum product readings of e.", "Strong mathematical interpretation; both original scans 181 and 182 visually inspected."],
    ["MPL_147_138-190", "182", "deleted separated and inserted a sheaf; margin global stratification is known locally", "The presheaf is separated by connected-plaque overlap chains. It fails sheaf existence by the marked-circle atlas.", "Conclusive proof; actual image inspected, deletion and insertion visible."],
    ["MPL_147_138-190", "183-184", "leaf topology need not be induced; compact implies finitely many locally compact leaves", "Plaque topology gives local immersions and commutes with restriction. Finite chart cover proves finiteness; local compactness is stated for compact Hausdorff X.", "Direct proof; transcription read, no disputed formula used."],
    ["MPL_147_138-190", "185", "base of opens with origin varying in Sigma_0 or Sigma_*", "Smallest stratum S_i0 is forced for strict flags; its closure is used for full pointed flags. Formula (300) explicitly requires x in S_i0.", "Actual image inspected; formula (300) clear. Mathematical consistency resolves the ambiguous subscript."],
    ["MPL_147_138-190", "187", "full flag origin x in closure X_i; degeneracies provide isomorphisms", "Origin must lie in smallest closure. Degeneracies give isomorphisms onto equal-entry summands, not entire adjacent degrees.", "Actual image inspected; missing i0 reconstructed from (303), and two-element chain refutes literal whole-degree isomorphism."],
    ["MPL_147_138-190", "188", "(303), matching middle closure germs; composition or multiplication", "The Segal map is a homeomorphism in every degree, with matching germ and common origin. Either word for composition gives the same operation.", "Conclusive local-chart proof; actual image and displayed fibre product inspected."],
    ["MPL_147_138-190", "189", "finite etale above D0*; finite etale on all D0 allegedly special to normal crossings", "Literal coproduct-of-closures topology makes the first-vertex map locally a finite disjoint union of identities on all D0. Its special-to-SNC aside must be corrected for this model.", "Actual image inspected; precise conditional correction proved, not a conjectural reading change."],
    ["MPL_147_138-190", "190", "three half-lines diagram, count seven, no power of two; hypothesis e will serve later", "Three rays are embedded in the plane: origin, three rays, three sectors. Link is S1 subdivided into three points and three arcs; e alone does not imply fixed conical links.", "Actual image inspected; count seven is clear and determines planar interpretation. Both claims independently computed or refuted."],
]
with (root / "local_readings.csv").open("w", newline="") as f:
    w = csv.writer(f)
    w.writerow(read_schema)
    w.writerows(readings)
print(f"Wrote {len(rows)} result rows and {len(readings)} reading rows with exact schemas.")
