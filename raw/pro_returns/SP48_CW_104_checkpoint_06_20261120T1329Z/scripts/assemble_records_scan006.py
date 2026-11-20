"""Assemble scan-006 records from text and the main reader's observations.

No image is opened, and no page, authoritative decision or cumulative file is
written. The only output is records/scan006/decision_draft.json. This staged
version includes observations 1--25. Completion requires the existing page
and its matching text-validation record to pass the guards below.
"""
from pathlib import Path
from collections import Counter
import copy
import hashlib
import json
import re

O = Path(__file__).resolve().parents[1]
P = O / "records/scan006"
STAGE = 25
ASSEMBLY_COMPLETE = False
R = {a: json.loads((P / f"reader_{a}/report.json").read_text()) for a in "ABC"}
I = {a: {x["id"]: x for x in R[a]["issues"]} for a in "ABC"}
T = {a: (P / f"reader_{a}/reading.tex").read_text() for a in "ABC"}
W = {a: (O.parent / f"reader_inputs/scan006/{a}.tex").read_text() for a in "CH"}
CW = json.loads((P / "reader_crosswalk.json").read_text())
X = {x["key"]: x for x in CW["loci"]}
PLAN = {x["number"]: x for x in json.loads((P / "main_crop_plan.json").read_text())}
MAIN = (P / "main_observations.md").read_text()
M = {int(n): re.split(r"\n\n(?:Delivery note:|All25 )", body)[0].strip()
     for n, body in re.findall(
    r"^([0-9]+)\. (.*?)(?=\n[0-9]+\. |\Z)", MAIN, re.M | re.S)}
assert set(range(1, STAGE + 1)) <= set(M), "Missing completed main observations"
assert {a: len(I[a]) for a in "ABC"} == {"A": 64, "B": 64, "C": 71}
assert len(PLAN) == 25 and len(set(x["path"] for x in PLAN.values())) == 25
MC = {n: PLAN[n]["path"] for n in range(1, STAGE + 1)}
assert all((O / p).is_file() for p in MC.values())
issues = []
by_key = {}
crosswalk_locus_map = {}
non_text_records = []
main_added_details = []


def decide(key, final, confidence, diff_C, diff_H, kind,
           unresolved=False, alternatives="", consequential="", notes=""):
    source = X[key]
    n = source["main_plan_number"]
    assert n <= STAGE, f"Attempt to decide a later locus: {key}"
    src = copy.deepcopy(source["source_issues"])
    row = {
        "id": source["id"], "location": source["location"],
        "C": source["witness_C"], "H": source["witness_H"],
        "final": final, "confidence": confidence, "diff_C": diff_C,
        "diff_H": diff_H, "kind": kind, "unresolved": unresolved,
        "marked_in_H": "yes" if any(
            I[a][k].get("marked_in_H") == "yes"
            for a in "ABC" for k in src[a]) else "no",
        "readers": copy.deepcopy(source["readers"]),
        "source_issues": src, "main_observations": [n],
        "crop": MC[n], "crops": [MC[n]],
        "evidence": f"Main {n}: {M[n]}",
        "reader_evidence": {
            a: [{"id": k, "evidence": I[a][k]["evidence"]} for k in src[a]]
            for a in "ABC"},
        "crosswalk_keys": [key],
    }
    if alternatives:
        row["alternatives"] = alternatives
    if consequential:
        row["consequential"] = consequential
    if notes:
        row["counting_note"] = notes
    issues.append(row)
    by_key[key] = row
    crosswalk_locus_map[key] = row["id"]
    return row


def merge_source(target_key, other_key):
    """Map a narrower record into one explicitly delimited decision."""
    row = by_key[target_key]
    source = X[other_key]
    row["crosswalk_keys"].append(other_key)
    crosswalk_locus_map[other_key] = row["id"]
    for a in "ABC":
        for key in source["source_issues"][a]:
            if key not in row["source_issues"][a]:
                row["source_issues"][a].append(key)
                row["reader_evidence"][a].append(
                    {"id": key, "evidence": I[a][key]["evidence"]})


def new_issue(number, location, final, main, C, H, readers, confidence="high",
              unresolved=False, alternatives="", kind="drawing or diagram",
              consequential="", approximate_source_point=None):
    assert main <= STAGE
    row = {
        "id": f"006N{number:02d}", "location": location, "C": C, "H": H,
        "final": final, "confidence": confidence, "diff_C": True,
        "diff_H": True, "kind": kind, "unresolved": unresolved,
        "marked_in_H": "no", "readers": readers,
        "source_issues": {a: [] for a in "ABC"},
        "reader_evidence": {a: [] for a in "ABC"},
        "main_observations": [main], "crop": MC[main], "crops": [MC[main]],
        "evidence": f"Main {main}: {M[main]}", "crosswalk_keys": [],
    }
    if alternatives:
        row["alternatives"] = alternatives
    if consequential:
        row["consequential"] = consequential
    if approximate_source_point:
        row["approximate_source_point"] = approximate_source_point
        row["coordinate_source"] = "Approximate point in main observation; not measured by assembler."
    issues.append(row)
    return row


# Main 1. The complete omitted passage excludes the two locally different
# synopsis readings. Its omitted word amountsto is not counted a second time.
row = decide(
    "I01",
    "Complete English paragraph and three heading groups as in witness C, "
    "including amountsto and both completion signs.",
    "high", False, True, "omission",
    notes="Residual full-strip omission excludes the separately counted 0/O "
          "and n--N gap loci. The omitted amountsto is included here once.")
row["location"] = "Otherwise untranscribed typed passage and heading content"
merge_source("I01", "I03")
decide("I02", r"\underline{\mathrm B}(\unsure{0|\mathrm O})^\wedge; "
       r"repeated \underline{\mathrm B}(0) follows the same doubt.",
       "medium", False, True, "misread symbol or index", True,
       alternatives=r"\mathrm O")
decide("I04", r"n\ \underline{\mathrm N}", "high", False, True,
       "text not on the page",
       consequential="The typed n--N gap is left blank; H's supplied membership is removed.")

# Main 2--6: top symbols, maps, qualifiers and unfinished computation.
decide("I05", r"\widetilde{\mathbb D}", "high", True, True,
       "misread symbol or index",
       consequential="Only this isolated top D is resolved as doubled; later D forms remain locally plain.")
decide("I06", r"\unsure{\mathscr N|N}", "medium", True, True,
       "misread symbol or index", True, alternatives="N",
       consequential="The domain remains script/plain N with script first; H's doubled N is not retained.")
decide("I07", "One N-like domain glyph directly followed by mapsto; no intervening ni n.",
       "high", False, True, "text not on the page",
       consequential="No membership and separate n are supplied before the top assignment arrow.")
decide("I08", r"\deleted{\unsure{I_n|D_n}}", "low", False, True,
       "omission", True, alternatives=r"D_n")
decide("I10", "Three distinct rightward arrows: upper bowed, middle straight, lower bowed.",
       "high", False, True, "drawing or diagram",
       consequential="The top D pair has three arrows, not H's two.")
decide("I11", r"n\in\mathbb I", "high", True, True, "misread symbol or index",
       consequential="The I to the right of n under the downward map is doubled.")
decide("X06", "Plain tilded D_n above a downward arrow whose endpoint is aligned to n; "
       "the membership and doubled I stand to n's right.",
       "high", True, True, "insertion or placement",
       consequential="The downward arrow points specifically to n, rather than being centered over the whole membership group.",
       notes="Direction and arrow-to-n alignment are one physical arrow locus.")
new_issue(1, "Down-map: detached point above the I top bar",
          "Small detached dark triangular point above I, without an assigned accent.",
          4, "Omitted.", "Omitted.", {a: "Omitted in reading.tex." for a in "ABC"},
          approximate_source_point=[1057, 541])
decide("I12", r"\deleted{N}", "high", True, True, "deletion state",
       consequential="The canceled target is ordinary N; strike strokes do not supply a doubled alphabet.")
decide("I13", r"\mathbb I", "medium", False, True, "misread symbol or index",
       consequential="The live I after canceled N retains its doubled form.")
decide("I14", "croissante", "high", True, False, "misread word")
decide("I15", r"\unsure{est|\(\subset\)}", "medium", True, True,
       "omission", True, alternatives=r"\subset",
       consequential="The upper image annotation remains est/subset; the equality candidate is removed.")
decide("I16", r"\mathbb I", "high", False, True, "misread symbol or index",
       consequential="The I in the upper image clause is doubled.")
decide("I17", r"\mathbb I_{\deleted{\unsure{\in n|<n}}\leq n}",
       "low", True, True, "deletion state", True, alternatives="<n",
       consequential="The old crossed image qualifier remains in n/<n before the separate live less-or-equal n.")
decide("I09a", r"2^2\ \text{---}\ +2^n", "high", False, True,
       "misread symbol or index",
       consequential="The continuous continuation dash is retained without H's inserted plus/ellipsis.")
decide("I09b", r"(1+2)^n=", "high", False, True, "omission",
       consequential="The final equals remains unfinished; no right member is supplied.")
new_issue(2, "Computation: leading relation on the lower line",
          r"\unsure{>|=}(1+2)^n=", 6, r"=(1+2)^n=", r"=(1+2)^n",
          {a: r"=(1+2)^n=" for a in "ABC"}, confidence="medium",
          unresolved=True, alternatives="=", kind="misread symbol or index",
          consequential="The leading lower relation remains >/= with > first. It is not silently restored to an equality or justified by a calculation.")

# Main 7--8. Shared local doubts remain explicit in these records.
decide("I19", r"J_{n''}", "high", True, True, "omission",
       consequential="The first sideways object is J, with two prime strokes on n.")
decide("I20", r"\unsure{u_\eta|u_g|u_y}", "medium", False, True, "omission",
       True, alternatives=r"u_g; u_y",
       consequential="The first sideways label retains eta/g/y, eta first; g is not pruned.")
decide("I21", r"\eta, with local eta/y doubt retained at the first shared occurrence.",
       "medium", False, True, "omission", True, alternatives="y",
       notes="Shared uncertainty only; this repeated local doubt is not resolved.")
decide("I22", r"\rotatebox{-90}{\(\in\)}", "high", True, True,
       "misread symbol or index",
       consequential="The membership over the middle J opens downward in the readable orientation.")
decide("I23", r"\deleted{\unsure{u_\eta|u_g}}", "low", False, True,
       "omission", True, alternatives=r"u_g")
decide("I24", r"\unsure{u_\xi|u_f|u_x}", "low", True, True,
       "omission", True, alternatives=r"u_f; u_x",
       consequential="The live second-arrow label remains xi/f/x; the crossed-x alternative is added explicitly.")
decide("I25", r"\unsure{u}, placed over/overlapping the sloping arrow shaft.",
       "low", True, True, "insertion or placement", True,
       alternatives="No distinct alternative; the u reading remains tentative.",
       notes="The u doubt is retained. The C change is its physical overlap with the shaft, not a resolution.")
decide("I26", r"\xi, with local xi/x doubt retained under the first shared occurrence.",
       "low", False, True, "omission", True, alternatives="x",
       notes="Local alternatives remain xi/x; shared macro consolidation is not refinement.")
decide("I27", r"\rotatebox{-90}{\(\in\)}", "high", True, True,
       "misread symbol or index",
       consequential="The independently checked membership over the last J also opens downward.")
decide("I28", r"J_{\deleted{\unsure{n'}}n}", "low", False, True,
       "omission", True, alternatives="No distinct alternative; the old n-prime remains uncertain.")
decide("I29", r"\xi, with local xi/x/f doubt retained under the first shared occurrence.",
       "low", False, True, "omission", True, alternatives="x; f",
       notes="Local order remains xi/x/f. The first shared macro xi/f/x does not reorder this local record.")
decide("I30", r"u_\xi u_\eta=", "high", False, True, "omission",
       consequential="The sideways composite keeps its equals and blank right continuation.",
       notes="High confidence concerns the equality and incompleteness. Both subscripts inherit the earlier retained uncertainties; this is not an independent glyph resolution.")
scope = X["X01"]
non_text_records.append({
    "id": scope["id"], "location": scope["location"],
    "source_issues": copy.deepcopy(scope["source_issues"]),
    "readers": copy.deepcopy(scope["readers"]),
    "final": "Three-object chain with two right arrows and a lower-right diagonal branch.",
    "evidence": f"Main 7: {M[7]}", "main_observations": [7], "crop": MC[7],
    "diff_C": False, "diff_H": False, "counted": False,
    "reason": "Supporting diagram scope; its labels, signs, cancellations and placement are represented by the physical issues above.",
})
crosswalk_locus_map["X01"] = scope["id"]

# Main 9--12: isolated traces, right map, array and its graphic components.
decide("I18a", "One short nearly horizontal dark trace, slightly raised at its left entry.",
       "high", True, True, "drawing or diagram")
decide("I18b", "Separate filled point above-left of a short uneven horizontal trace; "
       "the weaker right interval ends in a short down-and-up angular return.",
       "medium", True, True, "drawing or diagram",
       notes="The point and trace are secure; medium confidence concerns the terminal geometry. No lexical or mathematical role is assigned.")
decide("X02", r"\widetilde D_{n'}\longrightarrow\widetilde D_n above the x/y array.",
       "high", False, True, "insertion or placement")
decide("I31a", r"x''<x'", "high", False, True, "misread symbol or index",
       consequential="The upper comparison is strict <, with no lower equality bar.")
decide("I31b", r"y''<y'", "high", False, True, "misread symbol or index",
       consequential="The lower comparison is also strict <.")
decide("I32", r"\deleted{\unsure{\downarrow|I|=}}; no separate live left connector.",
       "low", True, True, "deletion state", True, alternatives="I; =",
       consequential="The whole left connector cluster is canceled, with downarrow/I/= retained. No independent live x-double-prime/y-double-prime connector is supplied.",
       notes="The canceled sign and removal of the spurious live connector occupy one physical place.")
decide("I33", r"\deleted{D}", "medium", True, True, "omission")
decide("I34", r"\widetilde D_n, with readable n", "high", False, True,
       r"readable ink left as \ill{}",
       consequential="The common live D has the readable index n, not H's illegibility marker.")
row = decide("I35a", "Two separate rightward membership signs, one at each row.",
             "high", False, True, "drawing or diagram",
             consequential="The two row-specific memberships replace H's one common membership sign.",
             notes="One membership-arrangement discrepancy. H has one common sign, so the two source signs are not counted as two independent omissions.")
row["location"] = "Right array: two row-specific membership signs"
row["C"] = "Two separate memberships, one per row."
row["H"] = "One common membership after the two-row array."
row["readers"] = {a: "Two separate memberships, one per row." for a in "ABC"}
merge_source("I35a", "I35b")
decide("I35c", "Headless x-prime/y-prime connector, separated from the letters.",
       "high", False, True, "drawing or diagram")
decide("I35d", "Separate headless connector below y-prime toward n-prime.",
       "high", False, True, "drawing or diagram")
decide("I35e", r"n' below the right connector", "high", False, True, "omission")
decide("I35f", r"n'' crossing the upper bowed arc, outside the array row.",
       "high", True, True, "insertion or placement",
       consequential="The n-double-prime labels the upper arc rather than a free array cell.")
decide("I36", "One common plain tilded D_n centered vertically between the two memberships.",
       "high", True, False, "insertion or placement",
       consequential="The common object is placed between the row levels, rather than on C's upper-row baseline.",
       notes="H already places its D beside a centered two-row array; its missing second membership is counted separately.")
decide("I37", "Small detached point just left of the first right connector at mid-height.",
       "high", True, True, "drawing or diagram")
row = decide("I38a", "Two bowed strokes with distinct endpoints and no secure arrowheads; "
             "the lower stroke has a real short medial break before resuming.",
             "high", True, True, "drawing or diagram",
             notes="The newly observed lower-arc gap is included in this drawing locus. It is not a second H omission of the same arc.")
main_added_details.append({
    "id": "006D01", "location": "Lower array arc: medial gap",
    "parent_decision_id": row["id"], "main_observations": [12], "crop": MC[12],
    "final": "A short real break near source x1740,y986 before the lower arc resumes.",
    "readers": {a: "Continuous lower arc in reading.tex." for a in "ABC"},
    "C": "Continuous lower arc.", "H": "Arc omitted.",
    "approximate_source_point": [1740, 986],
    "counting_note": "Included in parent decision's C/H flags, without a duplicate count.",
})
decide("I38b", "Two separate filled points below at the right.",
       "high", False, True, "drawing or diagram")

# Main 13--15: prose, overwritten map label and lower qualifiers.
decide("I39", "I ens ordonné, without a stop after ens.",
       "high", True, True, "misread word")
decide("I40", "famille", "high", True, False, "misread word",
       notes="The audit-only symbole suggestion and échelle are rejected at the same physical word.")
decide("I41", "d'ens, no stop", "high", False, True,
       "abbreviation expanded or spelling modernised")
decide("I42", "ordonnés", "medium", True, False, "misread word")
decide("I43", r"\unsure{,|;}", "low", True, True,
       "misread symbol or index", True, alternatives=";")
decide("X04", "A distinct isolated point before n mapsto, with no assigned mathematical function.",
       "high", True, True, "drawing or diagram")
decide("I44", r"\deleted{\phi}", "medium", True, True, "omission")
decide("I45", r"\unsure{k_n|\kappa_n|K_n}", "medium", True, True,
       "misread symbol or index", True, alternatives=r"\kappa_n; K_n",
       consequential="The live map label retains k/kappa/K uncertainty while excluding tau.")
new_issue(3, "Lower map label: detached oblique above-left",
          "Short literal detached oblique, without an assigned accent or prime.",
          14, "Omitted.", "Omitted.", {a: "Omitted in reading.tex." for a in "ABC"},
          approximate_source_point=[686, 918])
decide("I46", "str. croiss. image; no additional comma after croiss.",
       "high", False, True, "abbreviation expanded or spelling modernised",
       notes="The clipped upper bar of the later I is context only; no new alphabet choice is made from that clipping.")
new_issue(4, "Lower qualifier: point beneath the I baseline",
          "Small detached dark point below I, slightly left of its stem before the subscript.",
          15, "Omitted.", "Omitted.", {a: "Omitted in reading.tex." for a in "ABC"},
          approximate_source_point=[1577, 982])

# Main 16--20: canceled opening, definition, canceled line and lower chain.
decide("I47", r"\deleted{\unsure{Soit|Sinon}} within the canceled opening.",
       "low", False, True, "deletion state", True, alternatives="Sinon",
       notes="The surviving initial is capital S; the retained alternatives are not resolved.")
decide("I48", "Canceled l'ens, without a terminal stop.",
       "high", False, True, "abbreviation expanded or spelling modernised")
decide("I49", "Readable capital K inside the canceled opening.",
       "high", True, True, r"readable ink left as \ill{}",
       consequential="The canceled capital is recovered as K instead of H's illegibility marker.")
decide("X05", "Live Soit with capital S, outside the strike.",
       "high", False, True, "misread word")
decide("I50", r"\Phi_{n',n}", "medium", True, False,
       "misread symbol or index",
       consequential="The named subset is resolved as Phi with indices n-prime,n; script L and L are removed.")
decide("I51", "Two vertical equality strokes below the subset-name region toward "
       "the left, above the brace definition; no comma after the upper D_n.",
       "high", True, True, "insertion or placement",
       consequential="The definition retains its two-level left alignment, rather than centering the equality beneath the full set-builder or flattening the formula into a horizontal chain.",
       notes="Main's left alignment is a real C placement change. H's inline layout and added comma are represented at this same definition-layout locus.")
new_issue(5, "Subset definition: point above-left of the vertical equals",
          "Small detached dark point above-left of the vertical equality strokes, without assigned meaning.",
          17, "Omitted.", "Omitted.", {a: "Omitted in reading.tex." for a in "ABC"},
          approximate_source_point=[1512, 1127])
decide("I52", r"k_n(x)=n', with the earlier k/kappa/K uncertainty retained.",
       "medium", True, True, "misread symbol or index", True,
       alternatives=r"\kappa_n; K_n",
       consequential="The clean set-builder label excludes tau while retaining the earlier k/kappa/K alternatives.",
       notes="The repeated marker is shared, but replacing C's tau alternative by K is substantive at this independently checked occurrence.")
decide("I53", r"\Phi within the canceled Soit line.",
       "high", True, False, "misread symbol or index",
       consequential="The canceled subset capital is Phi rather than witness C's script L.")
decide("I54", r"n' within the canceled Soit line.",
       "high", True, False, "misread symbol or index",
       consequential="The canceled subset index has one clear prime; no second index is supplied.")
decide("I55", "Trailing comma inside the canceled Soit phrase.",
       "high", False, True, "omission")
decide("I56", "Considérons", "high", True, False, "misread word")
decide("I57", "l'ens, without a terminal stop.",
       "high", False, True, "abbreviation expanded or spelling modernised")
decide("I58", r"\deleted{\(\unsure{\widetilde D_{n'}|D_n}\)}",
       "low", False, True, r"readable ink left as \ill{}", True,
       alternatives=r"D_n",
       notes="The tilde and index remain entangled; C's alternatives and order are retained.")
decide("I59", r"\unsure{B|\mathbb B|\mathscr B}",
       "low", True, True, "omission", True,
       alternatives=r"\mathbb B; \mathscr B",
       consequential="The large live B retains ordinary/doubled/script alphabet uncertainty, with ordinary B first.")
decide("I60", r"\mathbb F_1", "high", False, True,
       "misread symbol or index",
       consequential="The middle object of the lower chain has doubled F.")
decide("X03", r"\mathbb F_2", "high", True, True,
       "misread symbol or index",
       consequential="The last chain object also has doubled F; the plain F_2 in both witnesses is not retained.")
new_issue(6, "Lower F chain: lower arrowhead in the first pair",
          "A detached curved C-like left head, separated by a white gap from the "
          "lower shaft of the first pair; the other three heads join their shafts.",
          20, "Standard joined left arrow.", "Standard joined left arrow.",
          {a: "Standard joined left arrow in reading.tex." for a in "ABC"},
          consequential="The lower arrow of the first F pair is preserved as a detached curved head and shaft, without silently joining the visible gap.")

# Main 21--25: loop, lower sketches, interrupted trace and final expression.
decide("I61", "Literal open rounded contour beside a separate plain x; upper-left "
       "inward/down-left head, separate lower-left end with upright and left-curving "
       "short returns, clear gap and no filled joining vertex.",
       "high", True, True, "drawing or diagram",
       consequential="The loop has separated ends and no filled shared vertex; the lower returns are preserved as strokes without declaring a second arrowhead.",
       notes="B's literal open-contour construction is selected. H's actual closed path and filled pt node are one geometry discrepancy, not duplicated by its prose caption.")
decide("I62", "x-prime over y-prime, with a nearly vertical headless connector "
       "separated from both letters.",
       "high", False, True, "drawing or diagram",
       notes="This locus covers only the two primed letters and connector. The separate point beside the y-prime tick is excluded and recorded once at 006N07.")
new_issue(7, "Foot vertical sketch: detached point beside the y-prime tick",
          "Separate filled point just below-left of the lower end of the y-prime "
          "tick, to the right of the y body; the prime remains a prime.",
          22, "Omitted.", "Omitted.", {a: "Omitted in reading.tex." for a in "ABC"})
decide("I63", "Filled lower-left point joined by a rising curve to a filled "
       "upper-right point with two arrowhead wings; third detached filled point farther right and lower.",
       "high", False, True, "drawing or diagram",
       notes="The separate low sloping segment is recorded at its own locus; no paler pinpoint is added.")
decide("I64", "Disconnected low segment rising gently rightward, with a tiny "
       "downward left return and rounded headless right end.",
       "high", True, True, "drawing or diagram",
       notes="One lower-segment locus; the new left return is not counted again within the neighboring curved-arrow sketch.")
row = decide("I65", "Shallow broken-V disposition: descending-right left stroke "
             "and detached rising-right trace, whose right arm itself has two "
             "short dark pieces separated by a weak interval.",
             "medium", True, True, "drawing or diagram",
             notes="Presence is secure; medium confidence concerns the precise interruption geometry. No letter, arrowhead or mathematical function is assigned.")
main_added_details.append({
    "id": "006D02", "location": "Detached V trace: interruption in its right arm",
    "parent_decision_id": row["id"], "main_observations": [24], "crop": MC[24],
    "final": "The right arm consists of two dark pieces with a weak/light interval.",
    "readers": {"A": "Entire V trace omitted.",
                "B": "Two arms drawn, each arm continuous.",
                "C": "Two arms drawn, each arm continuous."},
    "C": "Entire V trace omitted.", "H": "Entire V trace omitted.",
    "counting_note": "Included in the V-geometry issue, without a duplicate omission count.",
})
decide("I66", r"F_*", "high", True, False, "misread symbol or index",
       consequential="The F subscript is an asterisk, distinct from the following x; pi_0 is retained literally.")
decide("I67", "ens, without a stop", "high", True, True,
       "abbreviation expanded or spelling modernised")
decide("I68", "classes", "medium", True, True, "misread word",
       notes="Both witness doubts resolve; reader B's remaining uncertainty is not selected.")
decide("I69", "d'hom.topie. des, with the visible internal abbreviation point.",
       "high", True, True, "omission",
       consequential="The explicit hom.topie phrase is retained in the description of loop classes; it is not expanded to homotopie or omitted as in H.",
       notes="The H omission of this entire phrase includes its terminal stop. That stop is separately counted against C at I70, without a second H omission count.")
decide("I70", "A separate terminal stop after topie, before des.",
       "high", True, False, "omission",
       notes="Distinct added punctuation against C. Its absence from H is already included in the omitted hom.topie phrase at I69.")
decide("I71", "lacets", "high", True, False, "misread word")

# The inventory is explicitly provisional until selected page text exists.
# All observed elements are selected; the archive digit is report-backed metadata.
INV_MAIN = {
    "E01": [2], "E02": [1], "E03": [2], "E04": [6], "E05": [2],
    "E06": [7, 8], "E07": [7], "E08": [3], "E09": [5], "E10": [5],
    "E11": [5], "E12": [4], "E13": [5], "E14": [5], "E15": [9],
    "E16": [11], "E17": [10], "E18": [7], "E19": [12], "E20": [12],
    "E21": [13], "E22": [12], "E23": [12], "E24": [13], "E25": [7],
    "E26": [12], "E27": [14, 15], "E28": [14], "E29": [17], "E30": [8],
    "E31": [16], "E32": [16], "E33": [18], "E35": [19], "E36": [19],
    "E34": [23], "E37": [22], "E38": [20], "E39": [25],
    "E40": [21], "E41": [24],
}
INV_TEXT = {
    "E04": "Long continuation dash; lower leading >/= doubt; final unfinished equals",
    "E05": "Script/plain N, script first, directly maps to plain tilded D_n",
    "E07": "J chain; retained eta/g/y and xi/f/x families; two downward memberships; overlapping diagonal caption",
    "E11": "strictement croissante; image est/subset; old in n/<n before live <=n",
    "E12": "Plain tilded D_n, down arrow aligned to n, membership and doubled I to the right",
    "E14": "Canceled in n/<n, followed by separate live <=n",
    "E17": "Detached point above-left of uneven stroke with weaker interval and angular right return",
    "E19": "Strict comparisons; two memberships; common D between levels; right headless connectors and labels",
    "E20": "Resolved canceled D above the common live D_n",
    "E22": "Canceled downarrow/I/= cluster, without a separate live left connector",
    "E24": "Initial isolated point; famille d'ens ordonnés, terminal comma/semicolon",
    "E26": "Two bowed strokes; n-double-prime on upper arc; medial gap in lower arc; two separate dots",
    "E27": "Plain tilded D_n to plain I, old phi and k/kappa/K; str. croiss. image I_<=n",
    "E28": "Resolved overwritten phi",
    "E29": "Phi_n-prime,n subset D_n; left-aligned vertical equals; set-builder using the shared k/kappa/K uncertainty",
    "E31": "Si n-prime <= n; canceled opening; live capital Soit",
    "E32": "Canceled Soit/Sinon l'ens K, no stop after ens",
    "E33": "Canceled Soit x in resolved Phi_n-prime with trailing comma",
    "E35": "Canceled tilded D_n-prime / plain D_n alternatives retained",
    "E36": "Resolved Considérons l'ens; old D group; B/mathbb B/script B",
    "E38": "Plain F_0, doubled F_1 and F_2; four left arrows, first pair's lower head detached",
    "E34": "Three filled points, rising curved arrow with two wings, disconnected headless lower segment with left return",
    "E37": "x-prime and y-prime with headless connector and separate point beside the y-prime tick",
    "E39": "pi_0(F_*,x)=ens des classes d'hom.topie. des / lacets en x",
    "E40": "Open contour beside x, upper returning head, two lower returns, gap and no filled joining vertex",
    "E41": "Broken V-like trace with its right arm itself interrupted",
}
inventory = []
for source in R["C"]["inventory"]:
    key = source["element"]
    if key not in INV_MAIN:
        continue
    row = copy.deepcopy(source)
    row["first_words_or_objects"] = INV_TEXT.get(key, row["first_words_or_objects"])
    row["transcribed"] = "pending"
    row["selected_reading"] = True
    row["main_observations"] = INV_MAIN[key]
    row["crop"] = MC[INV_MAIN[key][0]]
    inventory.append(row)
for element, kind, pos, words, main in [
    ("down_I_point", "drawing", "Above the down-map I; approximate source [1057,541]",
     "Detached dark triangular point", 4),
    ("lower_computation_relation", "display", "Start of the lower computation line",
     "Unresolved >/=, greater-than first", 6),
    ("array_lower_arc_gap", "drawing", "Lower bowed arc; approximate source [1740,986]",
     "Short real medial break before continuation", 12),
    ("family_initial_point", "drawing", "Immediately before n mapsto on the family line",
     "Literal detached point", 13),
    ("map_label_oblique", "drawing", "Above-left of overwritten label; approximate source [686,918]",
     "Detached oblique, no accent or prime assigned", 14),
    ("qualifier_I_point", "drawing", "Below lower qualifier I; approximate source [1577,982]",
     "Detached dark point, no index or punctuation assigned", 15),
    ("subset_equals_point", "drawing", "Above-left of vertical equals; approximate source [1512,1127]",
     "Detached dark point without assigned meaning", 17),
    ("F_chain_detached_head", "drawing", "Lower arrow in the first pair of the F chain",
     "Curved C-like left head with a white gap to the shaft", 20),
    ("foot_yprime_point", "drawing", "Below-left of lower end of y-prime tick, right of y body",
     "Separate filled point; prime retained separately", 22),
]:
    inventory.append({
        "element": element, "kind": kind, "position": pos,
        "first_words_or_objects": words, "sheet_kind": "reused_typed",
        "hand": "his hand", "transcribed": "pending", "selected_reading": True,
        "main_observations": [main], "crop": MC[main],
    })
archive = copy.deepcopy(next(x for x in R["C"]["inventory"] if x["element"] == "E42"))
archive["transcribed"] = "pending"
archive["selected_reading"] = True
archive["source_evidence"] = (
    "All three independent reader reports identify archive 5, and all three "
    "returned texts encode it only as an archive-sheet comment. Main did not "
    "inspect an archive-digit crop.")
inventory.append(archive)
non_text_records.extend([
    {
        "id": "006M01", "location": "Archive number and manuscript metadata",
        "source_issues": {a: [] for a in "ABC"},
        "readers": {a: "Archive 5 in a comment; no author title, date or own folio." for a in "ABC"},
        "final": "Archive 5 remains a comment; H's title and contextual note are explicitly editorial.",
        "evidence": "All three final read logs and returned texts agree. No unviewed crop is offered as main evidence.",
        "diff_C": False, "diff_H": False, "counted": False,
    },
    {
        "id": "006M02", "location": "Pale background impressions and recovery limits",
        "source_issues": {a: [] for a in "ABC"},
        "readers": {a: "No additional securely recoverable words; no unreadable-word count supplied." for a in "ABC"},
        "final": "No background passage or invented unreadable-word count.",
        "evidence": "The three independent reports state this recovery limit. Main observations reject isolated pale context specks at the inspected loci.",
        "diff_C": False, "diff_H": False, "counted": False,
    },
])

source_issue_map = {a: {key: [] for key in I[a]} for a in "ABC"}
for row in issues + non_text_records:
    for a, keys in row["source_issues"].items():
        for key in keys:
            source_issue_map[a][key].append(row["id"])
pending_source_issues = {
    a: [key for key, mapped in source_issue_map[a].items() if not mapped]
    for a in "ABC"}
pending_loci = [
    {"key": row["key"], "id": row["id"], "location": row["location"],
     "main_plan_number": row["main_plan_number"], "status": "awaiting main decision"}
    for row in CW["loci"] if row["key"] not in crosswalk_locus_map]
assert all(row["main_plan_number"] > STAGE for row in pending_loci)
assert not pending_loci
assert all(all(mapped for mapped in source_issue_map[a].values()) for a in "ABC")

# Distinguish the doubt's disposition from another change at its same locus.
DISPOSITION = {
    1: ("retained", False), 2: ("resolved to doubled D", True),
    3: ("reordered to script N first", True), 4: ("retained", False),
    5: ("resolved to doubled I", True), 6: ("resolved to canceled N", True),
    7: ("resolved to croissante", True), 8: ("equals alternative removed", True),
    9: ("less-than-n alternative added", True), 10: ("resolved to J", True),
    11: ("all eta/g/y alternatives retained", False),
    12: ("eta/y retained through shared marker", False),
    13: ("retained", False), 14: ("x alternative added", True),
    15: ("u doubt retained; only physical placement changes", False),
    16: ("local xi/x retained through shared marker", False),
    17: ("retained", False),
    18: ("local xi/x/f retained in that order through shared marker", False),
    19: ("refined and reordered to downarrow/I/=", True),
    20: ("resolved to canceled D", True), 21: ("resolved to ens", True),
    22: ("resolved to famille", True), 23: ("resolved to ordonnés", True),
    24: ("resolved to canceled phi", True),
    25: ("tau removed and K added, k first", True),
    26: ("Soit/Sinon retained", False),
    27: ("resolved to canceled K", True),
    28: ("resolved to Phi", True),
    29: ("tau removed and K added; uncertainty shared at first label", True),
    30: ("resolved to n-prime", True),
    31: ("resolved to Considérons", True),
    32: ("tilded D_n-prime / D_n retained in order", False),
    33: ("doubled B added between ordinary and script B", True),
    34: ("resolved to asterisk", True),
    35: ("resolved to ens", True),
    36: ("resolved to classes", True),
    37: ("resolved to hom.topie with its internal point", True),
    38: ("resolved to lacets", True),
}
doubt_map = []
issue_by_id = {x["id"]: x for x in issues}
for d in CW["C_doubt_map"]:
    row = copy.deepcopy(d)
    n = int(row["id"][1:])
    key = row["locus_key"]
    if key in crosswalk_locus_map:
        decision_id = crosswalk_locus_map[key]
        decision = issue_by_id[decision_id]
        row.update({
            "decision_id": decision_id, "status": "adjudicated",
            "final": decision["final"], "unresolved": decision["unresolved"],
            "main_observations": decision["main_observations"],
            "crop": decision["crop"], "disposition": DISPOSITION[n][0],
            "doubt_changed_from_C": DISPOSITION[n][1],
        })
    else:
        row.update({"status": "pending", "decision_id": None,
                    "disposition": "No main choice yet"})
    doubt_map.append(row)
assert len(doubt_map) == 38

remaining = [
    {"location": x["location"], "reading": x["final"],
     "alternatives": x.get("alternatives", "No distinct alternative supplied."),
     "confidence": x["confidence"], "reason": x["evidence"],
     "decision_id": x["id"], "crop": x["crop"]}
    for x in issues if x["unresolved"]]
allowed_kinds = {
    "misread word", "misread symbol or index", "omission", "text not on the page",
    "deletion state", "insertion or placement",
    "abbreviation expanded or spelling modernised", r"readable ink left as \ill{}",
    "drawing or diagram", "other",
}
for row in issues:
    assert set(row["readers"]) == set("ABC")
    assert row["confidence"] in {"high", "medium", "low"}
    assert row["kind"] in allowed_kinds
    assert row["crop"] in MC.values()
    assert all((O / c).is_file() for c in row["crops"])
assert len(issue_by_id) == len(issues)
PAGE_PATH = O / "pages/H104-01_104_scan006.tex"
PAGE_VALIDATION_PATH = P / "assembler_validation.json"
page_guard_status = "pending; consolidated page does not yet exist"
page_sha256 = None
page_validation_summary = None
if PAGE_PATH.is_file():
    PAGE = PAGE_PATH.read_text()
    assert PAGE_VALIDATION_PATH.is_file(), "Page exists without its text-validation record."
    page_validation = json.loads(PAGE_VALIDATION_PATH.read_text())
    page_sha256 = hashlib.sha256(PAGE_PATH.read_bytes()).hexdigest()
    assert page_validation.get("sha256") == page_sha256, "Page validation is stale."
    assert page_validation.get("errors") == [], "Page structural validation has errors."
    checks = page_validation.get("decision_checks", [])
    assert {x["main_observation"] for x in checks} == set(range(1, 26))
    for check in checks:
        assert check["passed"] and not check["missing_tokens"], check["main_observation"]
        assert all(token in PAGE for token in check["required_tokens"]), (
            "Page changed after validation", check["main_observation"])
    # Independently guard the actual selected alternatives, resolved words,
    # signed rotations, unfinished relations and archive-only numbering.
    for literal in [
        r"\scanpage{6}", r"\unsure{0|\mathrm O}",
        r"\widetilde{\mathbb D}", r"\unsure{\mathscr N|N}",
        r"\deleted{\unsure{I_n|D_n}}", r"\deleted{N}\mathbb I",
        r"\unsure{est|\(\subset\)}", r"\unsure{\in n|<n}",
        r"\unsure{>|=}(1+2)^n=", r"\unsure{u_\eta|u_g|u_y}",
        r"\deleted{\unsure{u_\eta|u_g}}", r"\unsure{u_\xi|u_f|u_x}",
        r"\(u_\xi u_\eta=\)", r"\deleted{\unsure{\downarrow|I|=}}",
        r"\overset{\deleted{D}}{\widetilde D_n}", r"\unsure{,|;}",
        r"\deleted{\phi}\unsure{k_n|\kappa_n|K_n}",
        r"\deleted{\unsure{Soit|Sinon} l'ens \(K\)} Soit",
        r"\Phi_{n',n}\subset\widetilde D_n",
        r"\mid k_n(x)=n'", r"\deleted{Soit \(x\in\Phi_{n'},\)}",
        r"\unsure{\widetilde D_{n'}|D_n}",
        r"\unsure{B|\mathbb B|\mathscr B}", r"\mathbb F_1", r"\mathbb F_2",
        r"\pi_0(F_*,x)", "ens des classes d'hom.topie. des",
        r"\text{lacets en }x", "% archive sheet number: 5",
    ]:
        assert literal in PAGE, f"Selected page text differs at {literal}"
    assert PAGE.count(r"\scanpage{6}") == 1
    assert PAGE.count(r"\rotatebox{-90}{\(\in\)}") == 2
    assert r"\rotatebox{90}{\(\in\)}" not in PAGE
    assert PAGE.count(r"\unsure{") == 17, "Unexpected inline-doubt coverage."
    for rejected in [
        r"\unsure{croissante}", r"\unsure{famille", r"\unsure{ordonnés}",
        r"\unsure{Considérons}", r"\unsure{classes}", r"\unsure{lacets}",
        r"\unsure{\phi}", r"\unsure{K}", r"\tau_n",
    ]:
        assert rejected not in PAGE, f"Rejected or resolved reading remains: {rejected}"
    assert "All25 distinct adjudication crops" in MAIN
    ASSEMBLY_COMPLETE = True
    page_guard_status = (
        "passed: existing authoritative page, matching SHA-256, zero structural "
        "errors, 25/25 main-decision mappings and independent selected-text guards")
    page_validation_summary = {
        "path": "records/scan006/assembler_validation.json",
        "sha256": page_sha256, "main_decisions_verified": 25,
        "inline_unsure_macros": 17, "remaining_local_doubt_records": len(remaining),
        "scope": "Text checks only; no image reading, compilation, rendering or mathematical check.",
    }
    for row in inventory:
        row["transcribed"] = "yes"
if ASSEMBLY_COMPLETE:
    assert STAGE == 25 and PAGE_PATH.is_file()
    assert all(row["transcribed"] == "yes" for row in inventory)
    assert not pending_loci and not any(pending_source_issues.values())
    assert all(row["status"] == "adjudicated" for row in doubt_map)

notes = [
    "The reused sheet carries a sideways English typescript paragraph about "
    "projective and direct limits in Gr-stacks, with underlined B, D and N and "
    "two completion signs. The heading argument remains 0/O; amountsto is joined, "
    "and the final n--underlined-N gap contains no membership sign.",
    "The isolated top D is doubled; the domain remains script/plain N, script "
    "first, directly before mapsto. Three arrows join the upper D pair. A separate "
    "downward arrow is aligned to n, beside doubled I. The upper image annotation "
    "retains est/subset and an old in n/<n qualifier. The computation has a long "
    "continuation dash, a lower leading >/= doubt with > first, and a blank final equals.",
    "The sideways J construction has two downward-opening memberships. Its first "
    "label retains eta/g/y and its second xi/f/x; the repeated local eta/y, upper "
    "xi/x and endpoint xi/x/f limits remain distinct. The tentative diagonal u "
    "overlaps its shaft. The following u_xi u_eta= has no right member.",
    "The x/y array has strict comparisons and a wholly canceled downarrow/I/= "
    "cluster, without a live left connector. Two memberships flank one common "
    "plain D_n between the row levels; the right connectors are headless. "
    "n-double-prime crosses the upper bowed arc, while the lower arc has a real "
    "medial break. Detached points and traces have no assigned mathematical role.",
    "I ens ordonné introduces a family of ordered sets and increasing maps "
    "into I. Famille and ordonnés resolve; terminal comma/semicolon remains open. "
    "The overwritten phi resolves, while k/kappa/K excludes tau and remains shared "
    "with the fiber-like set-builder. Phi resolves, with a left-aligned vertical "
    "equality and a point above-left. Canceled K, n-prime and the trailing comma are retained.",
    "Considérons is readable; its canceled tilded D_n-prime/plain D_n remains "
    "uncertain, followed by ordinary/doubled/script B. The lower chain has plain "
    "F_0 and doubled F_1/F_2, with a detached lower head in its first arrow pair. "
    "The open contour beside x has separate ends and no filled common vertex. "
    "Other sketches retain their points, headless strokes, endpoint return and interrupted V trace.",
    "The footer reads pi_0(F_*,x)=ens des classes d'hom.topie. des lacets en x. "
    "The asterisk and words resolve; both the internal and terminal abbreviation "
    "points remain. Pi_0 and the unfinished expressions are preserved literally. "
    "These are transcription observations: no mathematical proof or computation was performed.",
    "No explicit written author doubt, manuscript title, author date or own folio "
    "was identified by the independent readers. Archive 5 is represented only "
    "in a comment. H's heading and contextual note are explicitly editorial; "
    "its supplied loop drawing belongs to this scan. Pale background impressions "
    "supply no further securely recoverable passage or invented unreadable-word count.",
]
decision = {
    "scan": 6, "folder": "H104-01", "issues": issues, "remaining": remaining,
    "inventory": inventory, "notes": notes, "checks": [],
    "crop_counts": {"A": R["A"]["crop_count"], "B": R["B"]["crop_count"],
                   "C": R["C"]["crop_count"],
                   "main": sum(p.startswith("crops/") for p in MC.values())},
    "main_reused_crop_count": sum(not p.startswith("crops/") for p in MC.values()),
    "main_total_decision_crop_count": len(MC),
    "planned_main_crop_count": 25, "planned_main_new_crop_count": 12,
    "planned_main_reused_crop_count": 13,
    "main_adjudication_complete": ASSEMBLY_COMPLETE,
    "assembly_status": (
        "complete decision draft; main observations and selected page text verified"
        if ASSEMBLY_COMPLETE else
        "full observation draft; selected page text and verification pending"),
    "main_observations_included": list(range(1, STAGE + 1)),
    "source_issue_map": source_issue_map,
    "pending_source_issues": pending_source_issues,
    "crosswalk_locus_map": crosswalk_locus_map, "pending_loci": pending_loci,
    "C_doubt_map": doubt_map, "non_text_records": non_text_records,
    "main_added_details": main_added_details,
    "main_image_delivery_events": [{
        "main_plan_number": 21, "path": PLAN[21]["path"],
        "first_delivery": "truncated before image reached main",
        "redelivery": "same existing crop delivered once",
        "successful_inspections": 1,
    }],
    "page_text_guard_status": page_guard_status,
    "page_text_sha256": page_sha256,
    "page_validation": page_validation_summary,
    "counting_policy": "Each physical locus is counted once against each differing "
    "witness. Actual C doubt resolution/refinement/reordering counts; shared-marker "
    "consolidation and equivalent syntax do not. Typed amountsto is included in "
    "the residual full-strip omission; 0/O and the n--N gap are separate. The "
    "membership pair is one arrangement change. The lower-arc gap is included in "
    "the paired-arc drawing. The terminal hom.topie stop changes C separately, "
    "while H's missing phrase is counted once. Broad marginal scope is supporting metadata only.",
    "residual_questions": (
        [] if ASSEMBLY_COMPLETE else ["Selected page text and its verification are pending."]),
}
(P / "decision_draft.json").write_text(
    json.dumps(decision, ensure_ascii=False, indent=2) + "\n")
counts = Counter()
for row in issues:
    for witness in "CH":
        if row[f"diff_{witness}"]:
            counts[witness] += 1
            counts[f'{witness}_{row["confidence"]}'] += 1
print(json.dumps({
    "stage": STAGE, "main_adjudication_complete": ASSEMBLY_COMPLETE,
    "issues": len(issues), "remaining": len(remaining), "inventory": len(inventory),
    "counts": dict(counts),
    "source_issue_coverage": {
        a: sum(bool(v) for v in source_issue_map[a].values()) for a in "ABC"},
    "C_doubts_adjudicated": sum(x["status"] == "adjudicated" for x in doubt_map),
}, ensure_ascii=False))
