"""Normalize verified Montpellier section/folio loci and stale dependencies."""
from pathlib import Path
import csv

base = Path(__file__).resolve().parents[1]
path = base / "code" / "generate_f_registers.py"
text = path.read_text()
replacements = {
    "Sector germs define the canonical tangential functor (243), an equivalence compatible with all generizations and etale descent, without a tubular embedding.":
        "Sector germs define the canonical tangential equivalence (243) for spaces and proper or common-stage controlled etale stacks, with all flag coherences and without a tubular embedding; arbitrary atlas-local germs remain a distinct object.",
    "All comparison 2-cells retained; open faces model punctured normal bundles. Original Longue Marche53 scans were recovered and are audited in root statement F.48.":
        "All comparison 2-cells retained. The parabolic quotient in F.51 refutes the unrestricted intrinsic-stack-neighbourhood equivalence; the chartwise sector functor remains canonical. Original Longue Marche53 scans were recovered and audited in F.48.",
    "Full neighbourhood pro-topoi satisfy both gluing theorems and the ambient open/tube pushout, with all intersections and flags, also for analytic DM stacks.":
        "Full neighbourhood pro-topoi satisfy both gluing theorems and the ambient open/tube pushout for spaces and properly presented analytic DM stacks, or atlases with explicit common-stage control.",
    "Proof in pro-Grothendieck topoi; infinite chart descent justified by explicit uniformization; non-simple branches handled through an etale atlas.":
        "Proof in pro-Grothendieck topoi with synchronized radii. Proper etale groupoids have finite local descent control; arbitrary nonproper infinite-isotropy atlas germs need an extra hypothesis, as refuted in F.51. Intrinsic actual-stack neighbourhoods are distinguished.",
    "Coordinates t=s6,x=s2X,y=s3Y; F:Y2=X3+1; open action free. Characteristic0 only, no residue-characteristic2 or3 assertion.":
        "Explicit old cusp-resolution node kernels Z(-3,1),Z(-2,1) and their profinite versions; stable vertical and marked projective corner lattices inject. Coordinates t=s6,x=s2X,y=s3Y; exact blow-up certificates attached. Characteristic0 only.",
    "The solvably closed quotient-group Isom theorem does not imply this kernel-group Hom assertion. No literature-wide minimality or openness claim.":
        "Centralizer and semilinear constructions are excluded; finite-extension descent is proved but all arithmetic obstructions persist after algebraic extension. The solvably closed quotient-group Isom theorem does not imply this kernel-group Hom assertion. No literature-wide minimality or openness claim.",
    "MPL 149; unnumbered notes; folios 1 and 9; scans 3-4 and 18-19":
        "MPL 149; section1; folios1-1v and8v-9; scans3-4 and18-19",
    "MPL 149; unnumbered notes; folio 9; scan 20":
        "MPL 149; section1; folio9v; scan20",
    "MPL 149; Theorem 2; folio 10; scans 21-22":
        "MPL 149; section1 Theorem2; folios10-10v; scans21-22",
    "MPL 149; scan 52 question; folio 25; scan 52":
        "MPL 149; section2; folio25v; scan52",
    "MPL 149; end of scan 52; folio 25; scan 52":
        "MPL 149; section2; folio25v; end of scan52",
    "MPL149; scan52 question; folio25; scan52":
        "MPL149; section2; folio25v; scan52",
    "MPL149; unnumbered notes; folios65-67; scans132-135":
        "MPL149; section4; folios65v-67; scans132-135",
    "MPL149; unnumbered notes; folios66-67; scans133-135":
        "MPL149; section4; folios66-67; scans133-135",
    "MPL149; arithmetic local-tube question; scans133-135; EXIT P1e-cusp-stack":
        "MPL149; section4; folios66-67; scans133-135; supplemental EXIT P1e-cusp-stack test, not a manuscript assertion",
    "MPL147; folio85; scans179-180; MPL149 folio67 scan135":
        "MPL147; section12; folios85-85v; scans179-180; MPL149 section4 folio67 scan135",
    "Additional F(h)(1); MPL149 folios66-67 scans133-135":
        "Additional F(h)(1); MPL149 section4 folios66-67 scans133-135",
    "LM8 intake; MPL147 folios70-81 scans143-148 and157-169; MPL149 scans133-135":
        "Supplemental LM8 coherent-etale-limit question; context MPL147 sections11-12 folios70-81 scans143-148 and157-169; MPL149 section4 folios66-67 scans133-135",
    "MPL149 folios66-67 scans133-135; EXIT task6 andP3b rows":
        "MPL149 section4 folios66-67 scans133-135; EXIT task6 andP3b rows",
    "PartE(c); LM3 F.18; LM3b H.9; MPL147 scan179":
        "Supplemental PartE(c) n=5 question; LM3 F.18 and LM3b H.9; manuscript context MPL147 section12 folio85 scan179",
    "EXIT task6; MPL149 scans132-135":
        "Supplemental EXIT task6 source audit; manuscript context MPL149 section4 folios65v-67 scans132-135",
}
count = 0
for old, new in replacements.items():
    if old in new and new in text:
        continue
    count += text.count(old)
    text = text.replace(old, new)
path.write_text(text)

paper = base / "F.tex"
text = paper.read_text().replace(
    r"MPL~149, fol.~25, scan~52", r"MPL~149, \S2, fol.~25v, scan~52")
paper.write_text(text)

for name in ("invariance_results.csv", "point_map_results.csv"):
    file = base / name
    with file.open() as handle:
        reader = csv.DictReader(handle)
        schema = reader.fieldnames
        rows = list(reader)
    for row in rows:
        row["manuscript_passages (section; folio; scan)"] = row[
            "manuscript_passages (section; folio; scan)"].replace(
                "MPL 149; folio 66; scan 133",
                "MPL 149; section4; folio66; scan133; additional F(h)(2) tests")
        row["depends_on"] = row["depends_on"].replace(
            "F.44 Kummer setup; ", "")
    with file.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=schema)
        writer.writeheader()
        writer.writerows(rows)
print(f"Normalized {count} source-locus occurrences in the main generator.")
print("F.7 prose: section2, folio25v, scan52.")
print("F.40-F.42: section4, folio66, scan133, with supplemental-test scope.")
print("F.46: removed stale dependency on the former F.44 Kummer setup.")
print("F.13: records proper/controlled atlas scope and the F.51 obstruction.")
print("F.23/F.44: explicit cusp kernels and finite-extension attack recorded.")
