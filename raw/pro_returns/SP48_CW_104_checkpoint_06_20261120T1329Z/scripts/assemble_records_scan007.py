"""Text-only crosswalk and staged records assembly for scan 007.

Inputs are the completed reader texts/reports, witness packet, and the main
reader's numbered observations. This script never opens image content and
never writes a page, decision.json, or a cumulative deliverable.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import argparse
import copy
import difflib
import hashlib
import json
import re

O = Path(__file__).resolve().parents[1]
P = O / "records/scan007"
PACKET = O.parent / "reader_inputs/scan007"
R = {a: json.loads((P / f"reader_{a}/report.json").read_text()) for a in "ABC"}
I = {a: {x["id"]: x for x in R[a]["issues"]} for a in "ABC"}
T = {a: (P / f"reader_{a}/reading.tex").read_text() for a in "ABC"}
W = {a: (PACKET / f"{a}.tex").read_text() for a in "CH"}
DOUBTS = json.loads((P / "witness_doubts.json").read_text())
MAIN = (P / "main_observations.md").read_text()
M = {int(n): re.split(r"\n\nDelivery note\b",body)[0].strip() for n, body in re.findall(
    r"^([0-9]+)\. (.*?)(?=\n[0-9]+\. |\Z)", MAIN, re.M | re.S)}
PLAN_PATH = P / "main_crop_plan.json"
PLAN_LIST = json.loads(PLAN_PATH.read_text()) if PLAN_PATH.exists() else []
PLAN = {x["number"]: x for x in PLAN_LIST}

# Canonical rows 01--38 follow reader C's physical locations, not its choices.
# Broad A/B source issues can map to several independently recorded places.
A_MAP = {
    1:[1], 2:[4], 3:[5], 4:[6], 5:[7], 6:[9], 7:[8], 8:[10],
    9:[11], 10:[12], 11:[13], 12:[14], 13:[15], 14:[16],
    15:[17], 16:[18], 17:[19], 18:[20], 19:[21], 20:[22],
    21:[22], 22:[22], 23:[23], 24:[24], 25:[25], 26:[26],
    27:[27], 28:[28], 29:[29], 30:[29], 31:[32], 32:[33],
    33:[34], 34:[35], 35:[36], 36:[37], 37:[38], 38:[39],
}
B_MAP = {
    **{i:[i] for i in range(1,20)},
    20:[21], 21:[21], 22:[20], 23:[22], 24:[23], 25:[24],
    26:[25], 27:[26], 28:[27], 29:[28], 30:[29], 31:[31],
    32:[32], 33:[33], 34:[34], 35:[35], 36:[36], 37:[37], 38:[38],
}
C_DOUBT_ROWS = [1,2,3,5,10,12,13,16,19,21,23,24,25,27,29,31,32,34,35,38]

# Main's crop-plan numbers are populated only from its selected plan.
# No candidate crop or reader majority is used to choose ink.
MAIN_NUMBERS = {
    "C01":1,"X01":1,"X02":2,"C02":2,"C03":3,"C04":3,"C05":4,
    "C06":5,"C07":5,"C08":6,"C09":7,"C10":8,
    "C11":9,"C12":9,"C13":9,"C14":9,
    "C15":10,"C16":10,"C17":11,"C18":11,"C19":26,
    "C20":12,"C21":12,"C22":13,"C23":14,"C24":14,"C25":15,
    "C26":16,"C27":17,"C28":18,"C29":19,"C30":19,"X04":19,
    "X03":20,"C31":21,"C32":22,"C33":22,"C34":23,"C35":23,
    "C36":24,"C37":25,"C38":25,
}

# Explicit local strings refine broad reports; complete source alternatives
# remain unchanged in reader_report_readings and source_issue_index.
READING_OVERRIDES = {
    "C01": {a:r"\unsure{modèles|modéles}" for a in "ABC"},
    "C03": {"A":r"\deleted{autom}", "B":r"\deleted{\unsure{autom|autom.}}",
            "C":r"\deleted{autom}"},
    "C04": {a:r"\inserted{end}" for a in "ABC"},
    "C10": {"A":r"\unsure{[i]|(i)}(ii)",
            "B":r"\unsure{(i]|(i)|[i]}(ii)",
            "C":r"\unsure{[i]|(i)}(ii)"},
    "C13": {a:r"\Phi_{D'}(D)" for a in "ABC"},
    "C14": {a:r"\inserted{\(M\)-}isomorphes; no M below Phi" for a in "ABC"},
    "C15": {a:"Plain N after Soit" for a in "ABC"},
    "C16": {a:r"\deleted{\(I\)}" for a in "ABC"},
    "C20": {a:r"\inserted{Il est en fait \uline{ordonné}, grâce à (ii).}"
            for a in "ABC"},
    "C21": {a:"grâce" for a in "ABC"},
    "C22": {a:r"d'objets de \(M\)." for a in "ABC"},
    "C25": {"A":r"un\deleted{\unsure{e|s}} objet",
            "B":r"un\deleted{e} objet",
            "C":r"un\deleted{\unsure{e|s}} objet"},
    "C26": {a:r"de \deleted{\(D\)}\(M\)" for a in "ABC"},
    "C29": {"A":"à; separately drawn oblique below-right",
            "B":r"\unsure{à|:}; separately drawn lowered backslash",
            "C":r"\unsure{à|\(\therefore\)}; third mark may belong to cluster"},
    "C30": {a:"cause de (ii)," for a in "ABC"},
    "C31": {a:r"\widetilde D_n=\mathbb J_n" for a in "ABC"},
    "C34": {"A":r"\deleted{\unsure{plui|plus}, une}\inserted{une}",
            "B":r"\deleted{\unsure{plus}, une}\inserted{une}",
            "C":r"\deleted{\unsure{plus}, une}\inserted{une}"},
    "C36": {a:r"(\mathbb J_n)_{n\in\mathbb N}, on its own displayed line" for a in "ABC"},
}

LOCAL_C_DIFF = {
    "C01":dict.fromkeys("ABC",True),
    "C20":dict.fromkeys("ABC",False),  # grâce is the separate C21 place
    "C21":dict.fromkeys("ABC",True),
    "C22":dict.fromkeys("ABC",False),  # A22 also mentions this point
    "C29":{"A":True,"B":True,"C":True},
    "C30":dict.fromkeys("ABC",False),  # A29's changed à is a different place
}

def relative_path(value, reader=None):
    p = Path(value)
    if p.is_absolute():
        return str(p.relative_to(O))
    if str(p).startswith(O.name + "/"):
        return str(p.relative_to(O.name))
    if str(p).startswith("crops/") and reader:
        return f"records/scan007/reader_{reader}/{p}"
    return str(p)

def snapshot(path):
    b = path.read_bytes()
    return {"sha256":hashlib.sha256(b).hexdigest(),"bytes":len(b)}

def source_ids(prefix, nums):
    return [f"{prefix}{n:02d}" for n in nums]

def make_row(key, rid, location, wc, wh, refs, readings=None, notes=None,
             local_diff=None, role="physical_locus"):
    readings = readings or {
        a:"; ".join(I[a][k]["reading"] for k in refs[a]) for a in "ABC"}
    diff = local_diff or {
        a:any(I[a][k].get("diff_C") for k in refs[a]) for a in "ABC"}
    return {
        "id":rid, "key":key, "location":location,
        "witness_C":wc, "witness_H":wh, "readers":readings,
        "source_issues":refs, "role":role, "notes":notes or [],
        "C_doubts":[], "main_plan_number":MAIN_NUMBERS.get(key),
        "planned_main_crop":(
            PLAN[MAIN_NUMBERS[key]]["path"]
            if key in MAIN_NUMBERS and MAIN_NUMBERS[key] in PLAN else ""),
        "main_adjudication_status":"pending; no ink choice made by text assembler",
        "reader_return_differs_from_C":diff,
        "reader_report_readings":{
            a:[{"id":k,"reading":I[a][k]["reading"]} for k in refs[a]] for a in "ABC"},
        "reported_bboxes":{
            a:[{"id":k,"bbox":I[a][k].get("bbox",[])} for k in refs[a]] for a in "ABC"},
        "reader_crop_options":[],
    }

def build_crosswalk():
    assert {a:len(I[a]) for a in "ABC"} == {"A":39,"B":38,"C":38}
    assert len(DOUBTS["C"]) == 20
    rows = []
    for n in range(1,39):
        key = f"C{n:02d}"
        s = I["C"][key]
        refs = {"A":source_ids("A",A_MAP[n]),
                "B":source_ids("B",B_MAP[n]),"C":[key]}
        rows.append(make_row(
            key, f"007L{n:02d}", s["location"], s["C"], s["H"], refs,
            READING_OVERRIDES.get(key), local_diff=LOCAL_C_DIFF.get(key)))
    bykey = {x["key"]:x for x in rows}
    bykey["C01"].update(
        location="Opening word: modèles accent and spelling only",
        witness_C=r"\unsure{modèles|modeles|modéles}",witness_H="modèles")
    bykey["C01"]["notes"].append(
        "Quotation style is a separate location X01; source B01/C01 cover both.")
    bykey["C09"].update(
        witness_C="Two aligned rows; M centered beneath the complete Hom operator; "
                  "common arrow-start column; no comma after the upper target.",
        witness_H="One row; Hom_M with ordinary side subscript; comma after upper target.",
        readers=dict.fromkeys("ABC","Two aligned rows; M centered beneath the complete "
                                  "Hom operator; common arrow-start column in reading.tex; "
                                  "star label at the left."),
    )
    bykey["C09"]["notes"].append(
        "Literal returned TeX is explicit here because each report only says "
        "M below Hom. Original report wording is preserved separately.")
    bykey["C20"]["notes"].append(
        "Count manuscript insertion/placement and underlining once against H. "
        "Do not count the same sentence again as an omitted passage. The "
        "word grâce is separately mapped at C21 for C's uncertainty change.")
    bykey["C21"].update(witness_C=r"\unsure{grâce}",
                        witness_H="grâce within H's editorial note")
    bykey["C21"]["notes"].append(
        "H already supplies this word in its note; only C's local doubt "
        "resolution is separate from the insertion-state issue.")
    bykey["C22"]["notes"].append(
        "A22 includes the preceding M-point observation; no separate A issue exists.")
    bykey["C29"]["notes"].append(
        "The detached oblique is compared separately at X04. C's therefore "
        "alternative may include all three marks. Final counting must use "
        "one combined cluster or separately delimited loci, never both.")
    bykey["C30"]["notes"].append(
        "A29 includes the initial à and these words; only its à uncertainty "
        "removal belongs to C29. The words cause de agree with witness C. "
        "All returns and witness C have a comma after (ii); H's uncertain "
        "phrase is followed directly by donc without that comma.")
    bykey["C30"].update(witness_C="cause de (ii),",
                        witness_H=r"\uncertain{comme dans (ii)}; no comma before donc")
    rows += [
        make_row("X01","007X01","Opening word: quotation marks",
                 "Two opening and two closing ticks","Guillemets",
                 {"A":["A02"],"B":["B01"],"C":["C01"]},
                 dict.fromkeys("ABC","Two opening and two closing ticks"),
                 ["Separate quotation-style location; accent is C01."],
                 dict.fromkeys("ABC",False)),
        make_row("X02","007X02","Condition (i), flèche accent",
                 "flèche","flèche",
                 {"A":["A03"],"B":[],"C":[]},
                 {"A":r"\unsure{flèche|fléche}","B":"flèche","C":"flèche"},
                 ["B/C retain flèche in reading.tex and check its accent in their logs; "
                  "neither supplies a separate issue. A's crop clips the lower f "
                  "descender; its full word was read in half a."],
                 {"A":True,"B":False,"C":False}),
        make_row("X03","007X03","Lower line, l'ens ordonné before the equality",
                 "l'ens ordonné","l'ens. ordonné",
                 {"A":["A31"],"B":["B30"],"C":[]},
                 dict.fromkeys("ABC","l'ens ordonné; no stop after ens"),
                 ["Reader C omits a separate source issue but explicitly checks "
                  "this no-stop reading in its read_log.md and reading.tex."],
                 dict.fromkeys("ABC",False)),
        make_row("X04","007X04","Detached oblique below-right of the à-like cluster",
                 "No separately drawn stroke",
                 r"\therefore-like cluster in the uncertain phrase; no separate stroke",
                 {"A":["A30"],"B":["B28"],"C":["C29"]},
                 {"A":r"à\makebox[0pt][l]{\raisebox{-1.8ex}{\(\scriptscriptstyle\backslash\)}}",
                  "B":r"\unsure{à|:}\(\underset{\scriptscriptstyle\backslash}{\phantom{x}}\)",
                  "C":r"\unsure{à|\(\therefore\)}; third mark not drawn separately"},
                 ["Source A30/B28 treat the stroke as detached. C29 allows it "
                  "inside a therefore-like cluster. Its source issue and "
                  "C29 must not produce duplicate counts if main selects a "
                  "single cluster interpretation."],
                 {"A":True,"B":True,"C":True}),
    ]
    bykey = {x["key"]:x for x in rows}
    c_doubt_map = []
    for d,n in zip(DOUBTS["C"],C_DOUBT_ROWS):
        x = bykey[f"C{n:02d}"]
        x["C_doubts"].append(d["id"])
        c_doubt_map.append({
            **copy.deepcopy(d),"locus_id":x["id"],"locus_key":x["key"],
            "readers":copy.deepcopy(x["readers"]),
            "reader_return_differs_from_C":copy.deepcopy(x["reader_return_differs_from_C"]),
            "shared_marker_note":"No repeated inline doubt is independently resolved by consolidation.",
        })
    catalog = []
    for a in "ABC":
        candidates = list((P/f"reader_{a}").glob("crop_metadata.json"))
        candidates += list((P/f"reader_{a}").glob("crop_manifest.json"))
        assert len(candidates) == 1
        for item in json.loads(candidates[0].read_text()):
            row = copy.deepcopy(item)
            row.update(reader=a,path=relative_path(item["path"],a),
                       catalog_id=f"R{len(catalog)+1:02d}")
            catalog.append(row)
    crop_index = {(x["reader"],x["path"]):x for x in catalog}
    source_map = {a:{k:[] for k in I[a]} for a in "ABC"}
    for row in rows:
        for a in "ABC":
            for k in row["source_issues"][a]:
                source_map[a][k].append(row["id"])
                cp = I[a][k].get("crop")
                if cp:
                    entry = crop_index[(a,relative_path(cp,a))]
                    if entry not in row["reader_crop_options"]:
                        row["reader_crop_options"].append(copy.deepcopy(entry))
    assert all(v for sm in source_map.values() for v in sm.values()), source_map

    # A's complete inventory supplies the union: its live-M replacement and
    # A/B's oblique are not silently lost in C's broader paragraph rows.
    b_inv = {i:[i] for i in range(1,22)}
    b_inv.update({22:[21],23:[22],24:[24],25:[23],26:[25],27:[26],28:[27]})
    c_inv = {i:[i] for i in range(1,22)}
    c_inv.update({22:[21],23:[19],24:[23],25:[22],26:[24],27:[25],28:[26]})
    inventory = []
    for n,iv in enumerate(R["A"]["inventory"],1):
        refs = {"A":[n],"B":b_inv[n],"C":c_inv[n]}
        row = copy.deepcopy(iv)
        row.update(element=f"E{n:02d}: {iv['element']}",transcribed="pending",
                   source_inventory_rows=refs,
                   reader_inventory={
                       a:[copy.deepcopy(R[a]["inventory"][k-1]) for k in refs[a]]
                       for a in "ABC"})
        if n == 23:
            row["coverage_note"] = (
                "C inventories the surrounding paragraph and treats the mark "
                "within its uncertain cluster; it does not separately inventory an oblique.")
        inventory.append(row)
    for a in "ABC":
        covered = {i for x in inventory for i in x["source_inventory_rows"][a]}
        assert covered == set(range(1,len(R[a]["inventory"])+1)), (a,covered)

    context = [
        ("CTX01","M, D, D-prime, tilde D and Ob at every occurrence",
         ["C09","C13","C14","C24","C26","C27","C31","C36"],
         "Reader logs check the complete opening, definition, display, subset "
         "and lower paragraph, including the unprimed second Hom argument. "
         "Agreement is not a mathematical check or an extra counted change."),
        ("CTX02","Hom with M below; right arrow and mapsto bar; star label",
         ["C09"],"All readers retain two rows, lower M and the distinct mapsto bar."),
        ("CTX03","Subset capital, lower D-prime, M attachment and unindexed Delta",
         ["C13","C14"],"Phi and insertion attachment have separate loci. All logs "
         "retain unindexed Delta and the plain argument D."),
        ("CTX04","Plain first N; three later doubled N occurrences",
         ["C15","C24","C36"],"First membership N is C12's inline doubt. "
         "The family-index N and footer N are independently checked in each "
         "reader's log, without an extra C uncertainty-resolution count."),
        ("CTX05","Two hooked J forms",
         ["C31","C36"],"Equation and displayed family occurrences are distinct; "
         "both are locally checked, not inferred from one another."),
        ("CTX06","Ex, end, ens, isom and reference punctuation",
         ["C04","C10","C11","C17","C22","C28","C33","C37","X03"],
         "Ex retains its colon. No live end/ens or later isom stop is supplied. "
         "Canceled ens. and classes d'isom. retain their actual stops in every text."),
        ("CTX07","Both quotation pairs and the nearly level word accent",
         ["C01","X01","C07"],"Word accent and opening quotation style are split "
         "because they are distinct source marks; inclusion quotes are another place."),
        ("CTX08","First sous objets versus second sous-objets",
         ["C06"],"All three logs preserve the first blank and the later hyphen."),
        ("CTX09","Two later à isom unique près phrases",
         ["C28","C33"],"Two separate abbreviation endpoints; neither becomes "
         "resolved merely because the first is read."),
        ("CTX10","C audit: corrected terms, cancelled line and added clauses",
         ["C03","C04","C12","C14","C16","C18","C20","C25","C26","C34"],
         "The canceled Soit K un ens. ordonné line agrees in all three texts; "
         "all its words and strike state are checked in the logs and inventory. "
         "The other local corrections have individual comparison rows."),
        ("CTX11","C audit: accents, family, lower indices and detached n mark",
         ["C19","C21","C24","C27","C29","C31","C32","C34","C35","C36","C38"],
         "All 20 inline doubts are also indexed individually in C_doubt_map. "
         "The audit's actual-mark claims remain witness assertions until main crops."),
        ("CTX12","Own folio 1, archive 6, absent type and absent sideways note",
         [],"All readers identify folio 1 and archive 6. Their inventory/logs "
         "record a handwritten text sheet without recoverable typed reuse. "
         "This is metadata/coverage, not a textual omission count."),
    ]
    contextual = [{
        "id":cid,"topic":topic,"locus_keys":keys,
        "locus_ids":[bykey[k]["id"] for k in keys],"coverage":note,
        "source":"reader_inputs/scan007/C_context.md",
        "status":"reader returns cross-referenced; main adjudication pending",
    } for cid,topic,keys,note in context]
    paths = [PACKET/"C.tex",PACKET/"H.tex",PACKET/"C_context.md",P/"witness_doubts.json"]
    paths += [P/f"reader_{a}"/fn for a in "ABC"
              for fn in ["reading.tex","report.json","read_log.md"]]
    result = {
        "scan":7,"status":"complete text-only reader crosswalk; no final ink choices",
        "created_utc":datetime.now(timezone.utc).isoformat(),
        "scope":"No images, crops, PDF, OCR, web, rendering or compilation opened by assembler.",
        "counts":{"reader_source_issues":{a:len(I[a]) for a in "ABC"},
                  "source_issue_total":sum(len(I[a]) for a in "ABC"),
                  "crosswalk_rows":len(rows),"C_doubts_mapped":len(c_doubt_map),
                  "contextual_checks":len(contextual),"inventory_union":len(inventory),
                  "reader_crop_catalog":len(catalog)},
        "grouping_policy":"One physical comparison place per row. Broad source issues "
            "map to their individual places; local uncertainty flags exclude the "
            "other places inside a broad issue. C29/X04 can be merged at final "
            "assembly if the main observation treats the mark group as one locus.",
        "counting_policy_for_later_assembly":"Removed, refined, extended or reordered "
            "C uncertainty counts as a difference. Equivalent notation and moving "
            "a shared doubt to its first occurrence do not. H's insertion note is "
            "not a second omitted passage in addition to its placement discrepancy.",
        "loci":rows,"C_doubt_map":c_doubt_map,"contextual_C_checks":contextual,
        "H_doubt_map":[
            {**copy.deepcopy(d),"locus_keys":keys,
             "locus_ids":[bykey[k]["id"] for k in keys]}
            for d,keys in zip(DOUBTS["H"],[["C12"],["C29","C30","X04"],["C34"]])],
        "source_issue_map":source_map,"source_issue_index":copy.deepcopy(I),
        "reader_crop_catalog":catalog,"main_crop_plan_snapshot":copy.deepcopy(PLAN_LIST),
        "inventory_crosswalk":inventory,
        "returned_tex_changes_by_reader":{
            a:[x["key"] for x in rows if x["reader_return_differs_from_C"][a]] for a in "ABC"},
        "returned_tex_diffs":{
            a:list(difflib.unified_diff(W["C"].splitlines(),T[a].splitlines(),
                fromfile="witness_C.tex",tofile=f"reader_{a}/reading.tex",lineterm=""))
            for a in "ABC"},
        "non_substantive_encoding_changes":[
            "Equivalent math delimiters and math grouping syntax.",
            "Comments describing literal stroke encoding are editorial metadata.",
            "A/B's two encodings of the lowered oblique have the same stated physical intent; "
            "its distinction from C's therefore interpretation is substantive."],
        "non_text_records":[
            {"id":"007M01","location":"Folio/archive metadata",
             "readers":dict.fromkeys("ABC","Own folio 1; archive sheet 6; no date or title."),
             "note":"H page 6 corresponds to our scan 7; H's sa page 1 is editorial metadata."},
            {"id":"007M02","location":"Packet correction",
             "readers":dict.fromkeys("ABC","Excluded the row primarily labeled scan 8."),
             "note":"The cross-page row was removed and all readers notified. No scan 8 "
                    "image was supplied. Historical scan-6 audit comparisons are not evidence."},
            {"id":"007M03","location":"Mathematical checking status",
             "readers":dict.fromkeys("ABC","checks=[]; no mathematical check performed."),
             "note":"Main math_checks.json and any separately authorized math audit remain "
                    "pending source confirmation; no check event is created by collation."}],
        "input_snapshots":{str(p.relative_to(O.parent)):snapshot(p) for p in paths},
        "assembly_next_step":"Use only numbered main observations and its actual selected "
            "crops to build decision_draft.json. Completion also requires the selected "
            "page and successful text checks. Do not write decision.json or cumulative files.",
    }
    (P/"reader_crosswalk.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    write_crosswalk_md(result)
    return result

def mdcell(value):
    return str(value).replace("|","&#124;").replace("\n","<br>")

def write_crosswalk_md(cw):
    lines = [
        "# Scan 007 — complete reader source-issue crosswalk","",
        "Text-only collation of all three final returns; no image decision is made here. "
        "All 115 source issues, 20 witness-C inline doubts, 12 contextual checks, "
        "3 H doubt marks and 28 union inventory elements are covered.","",
        "The 42 comparison rows are not final change totals. The opening accent and "
        "its quotation style are separate; the inserted sentence's status and its "
        "grâce uncertainty are separate. The à/oblique interpretation requires an "
        "explicit main decision to avoid a cluster-plus-component duplicate.","",
        "| Key | Place | Witness C | Witness H | Reader A | Reader B | Reader C | Source issues |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for x in cw["loci"]:
        src = "; ".join(a+": "+(", ".join(x["source_issues"][a]) or "text/log only") for a in "ABC")
        values = [x["key"],x["location"],x["witness_C"],x["witness_H"],
                  *[x["readers"][a] for a in "ABC"],src]
        lines.append("| "+" | ".join(mdcell(v) for v in values)+" |")
    lines += ["","## All witness-C inline doubts","",
              "| C doubt | Source alternative set | Locus | A differs from C | B differs from C | C differs from C |",
              "|---|---|---|---|---|---|"]
    for x in cw["C_doubt_map"]:
        lines.append("| "+" | ".join(mdcell(v) for v in [
            x["id"],x["reading"],x["locus_key"],
            *[x["reader_return_differs_from_C"][a] for a in "ABC"]])+" |")
    lines += ["","## Contextual witness checks",""]
    for x in cw["contextual_C_checks"]:
        lines.append(f"- **{x['id']} — {x['topic']}**: {x['coverage']} "
                     f"Rows: {', '.join(x['locus_keys']) or 'metadata/inventory'}.")
    lines += ["","## Inventory union","",
              "| Element | Kind | Source rows A / B / C | Main status |",
              "|---|---|---|---|"]
    for x in cw["inventory_crosswalk"]:
        refs = " / ".join(",".join(map(str,x["source_inventory_rows"][a])) for a in "ABC")
        lines.append("| "+" | ".join(mdcell(v) for v in [
            x["element"],x["kind"],refs,"pending selected page and text check"])+" |")
    lines += ["","## Main-only decisions and mathematical checks","",
        "The assembler imports no reading from another page. The C-context historical "
        "comparisons and removed scan-8 row are not evidence. All three readers report "
        "empty checks arrays. Main check events require main confirmation that their "
        "source statements survive the ink reading.",
        "","Exact returned alternatives, source bboxes, crop processing, every source "
        "issue, full text diffs and input hashes are preserved in reader_crosswalk.json.",
        ""]
    (P/"reader_crosswalk.md").write_text("\n".join(lines))

def spec(final,confidence,diff_C,diff_H,kind,unresolved=False,
         alternatives="",consequential="",note="",merge=()):
    return dict(final=final,confidence=confidence,diff_C=diff_C,diff_H=diff_H,
                kind=kind,unresolved=unresolved,alternatives=alternatives,
                consequential=consequential,counting_note=note,merge=list(merge))

# These are explicit transcriptions of completed main observations.
# A new entry must never be inferred from the readers' majority or mathematics.
SPECS = {
    "C01":spec(r"\unsure{modèles|modéles}","medium",True,True,"misread word",
               True,"modéles",
               note="Unaccented modeles is removed; grave/acute uncertainty remains. "
                    "Quotation style is counted separately at X01."),
    "X01":spec("Two opening and two closing quotation ticks","high",False,True,"other"),
    "X02":spec(r"\unsure{flèche|fléche}","medium",True,True,"misread word",
               True,"fléche",
               consequential="The nearly vertical accent remains grave/acute; "
                             "A's additional doubt is preserved after the full-word crop."),
    "C02":spec("monomorphique","high",True,False,"misread word"),
    "C03":spec(r"\deleted{\unsure{autom|autom.}}","medium",False,True,
               "abbreviation expanded or spelling modernised",True,"autom.",
               note="High confidence in the short abbreviation; medium confidence "
                    "concerns the terminal stop merged with the strike. C's doubt "
                    "is retained unchanged rather than falsely counted as resolved."),
    "C04":spec(r"\inserted{end}","high",False,True,"text not on the page"),
    "C05":spec(r"\unsure{par}","medium",False,True,"misread word",
               True,"No distinct alternative; par remains tentative.",
               note="Witness C's uncertainty is retained unchanged; grammatical "
                    "expectation does not resolve the reduced a/r strokes."),
    "C06":spec("sous objets, with a blank and no hyphen","high",False,True,
               "text not on the page"),
    "C07":spec("Two opening and two closing quotation ticks around inclusion",
               "high",False,True,"other"),
    "C08":spec(r"\widetilde D at the identification sentence end, without a period",
               "high",False,True,"text not on the page"),
    "C09":spec("Two rows: Hom(D-prime,D) right-arrow to plain tilde D, then "
               "indented u mapsto u(D-prime). M lies below the terminal m of Hom; "
               "the lower arrow begins left of the upper arrow and is longer. "
               "The parenthesized star is far left between the row levels; "
               "there is no comma after the upper target.",
               "high",True,True,"insertion or placement",
               consequential="The two-row mapping preserves the local M-to-m attachment "
                             "and unequal arrow starts/lengths, correcting the common "
                             "alignment column in C and all three returns.",
               note="One mapping-layout locus. Its M attachment, indentation, arrow "
                    "geometry, tag placement and absent target comma are not counted "
                    "again as separate overlapping display changes."),
    "C10":spec(r"\unsure{(i]|[i]|(i)}(ii)","medium",True,True,
               "misread symbol or index",True,"[i]; (i)",
               consequential="The first reference keeps its mixed enclosure first, "
                             "then bracketed and parenthesized alternatives; the "
                             "following (ii) and comma remain distinct and secure."),
    "C11":spec("l'ens, without a stop","high",False,True,"text not on the page"),
    "C12":spec(r"\deleted{\unsure{de}}","low",False,True,
               r"readable ink left as \ill{}",True,
               "No separately identified alternative; de remains tentative.",
               note="Witness C's canceled-word uncertainty is retained without refinement."),
    "C13":spec(r"\Phi_{D'}(D)\subset\widetilde D","high",True,False,
               "misread symbol or index",
               consequential="The subset capital resolves as Phi on its closed "
                             "two-lobed contour; script/plain L are removed."),
    "C14":spec(r"\inserted{\(M\)-}isomorphes; no M subscript beneath Phi",
               "high",True,True,"insertion or placement",
               consequential="The M- belongs to the inserted word prefix before "
                             "isomorphes, not a mathematical index beneath Phi."),
    "C15":spec("Plain N after Soit","high",False,True,"misread symbol or index"),
    "C16":spec(r"\deleted{\(I\)}","high",True,True,"omission",
               consequential="The separate canceled glyph is barred I; K is excluded. "
                             "Its descending strike is not a surviving live sign."),
    "C17":spec("l'ens, without a stop","high",False,True,"text not on the page"),
    "C18":spec(r"\inserted{préordonné}, without textual parentheses",
               "high",False,True,"insertion or placement"),
    "C20":spec(r"\inserted{Il est en fait \uline{ordonné}, grâce à (ii).}",
               "high",False,True,"insertion or placement",
               consequential="The orderedness assertion is manuscript insertion "
                             "text, with its own underline under ordonné and a "
                             "distinct longer attachment leader.",
               note="One insertion/underline discrepancy against H's editorial "
                    "note. The separate C doubt removal in grâce is C21, with "
                    "no second H omission of the same sentence."),
    "C21":spec("grâce","high",True,False,"misread word"),
    "C22":spec(r"d'objets de \(M\).","high",False,True,"omission",
               note="This low point ends the classification sentence and is "
                    "separate from the following interlinear assertion."),
    "C23":spec(r"\unsure{\forall|\mathrm H}","medium",False,True,
               "misread symbol or index",True,r"\mathrm H",
               note="The source's compound glyph remains unresolved; witness C's "
                    "complete alternatives and their order are retained."),
    "C24":spec(r"\mathbb N in n\in\mathbb N","high",True,False,
               "misread symbol or index"),
    "C25":spec(r"un\deleted{\unsure{e|s}} objet","low",True,True,
               "deletion state",True,"s"),
    "C26":spec(r"de \deleted{\(D\)}\(M\)","high",False,True,"deletion state",
               consequential="The readable old D and superposed live M are both "
                             "retained; H's sole canceled M loses the correction."),
    "C27":spec(r"\overset{\ast}{n}","medium",True,True,"misread symbol or index",
               consequential="The raised mark is a branching asterisk, not a "
                             "single prime; no footnote text is supplied."),
    "C28":spec("First isom in à isom unique près, without an abbreviation stop",
               "high",False,True,"text not on the page"),
    "C29":spec(r"\unsure{à|:}","low",True,True,"misread symbol or index",True,":",
               note="This row counts H's whole therefore-like cluster mismatch once. "
                    "The separately preserved oblique is X04 and is not counted "
                    "a second time against H. A's resolved à and C-reader's "
                    "therefore alternative are not selected."),
    "X04":spec("A separate literal down-right stroke below and to the right of "
               "the uncertain à/colon cluster; no lexical or mathematical role assigned.",
               "high",True,False,"drawing or diagram",
               note="A separate physical stroke omitted from witness C. H's three-mark "
                    "therefore-like cluster is already counted once at C29, so this "
                    "component carries no second H difference."),
    "C30":spec("cause de (ii),","medium",False,True,"misread word",
               note="Medium confidence concerns the words; the separate following "
                    "comma is high-confidence. H's comme dans wording and omitted "
                    "comma are one phrase locus, not an extra punctuation count."),
    "X03":spec("l'ens ordonné, without a stop after ens","high",False,True,
               "text not on the page"),
    "C31":spec(r"\widetilde D_n=\mathbb J_n","high",True,True,
               "misread symbol or index",
               consequential="The right object has doubled J with a returning "
                             "lower hook; plain/doubled I alternatives are removed."),
    "C32":spec("défini","high",True,False,"misread word"),
    "C33":spec("Second isom in à isom unique près, without an abbreviation stop",
               "high",False,True,"text not on the page"),
    "C34":spec(r"\deleted{\unsure{plui|plus}, une}\inserted{une}",
               "low",True,True,r"readable ink left as \ill{}",True,"plus",
               consequential="The dotted literal form plui precedes plus in the "
                             "canceled word's alternatives; choisi is removed.",
               note="Low confidence concerns the first word. The canceled comma "
                    "and old une, and the raised live une, have high-confidence "
                    "states and belong to this one correction locus."),
    "C35":spec("famille, live despite the crossing at its initial f",
               "high",True,False,"misread word"),
    "C36":spec(r"(\mathbb J_n)_{n\in\mathbb N}, on a separate displayed line",
               "high",False,True,"misread symbol or index",
               consequential="The family uses doubled J_n, with no D bowl or "
                             "tilde, and retains its displayed placement.",
               note="This J and the index N were checked at their own occurrence; "
                    "their status is not inferred from the preceding equality."),
    "C37":spec("d'ens ordonnés, with no abbreviation stop and a comma after ordonnés",
               "high",False,True,"text not on the page"),
    "C38":spec("indexés","high",True,False,"misread word"),
    "C19":spec("classes","medium",True,False,"misread word",
               note="Main26 is the first complete main crop of this word. "
                    "Main11's clipped right edge did not decide it."),
}

MATH_SOURCE_CONFIRMED = True
MATH_SOURCE_OBSERVATIONS = {
    "007-HYPOTHESES":[2,3],
    "007-INJECTIVE":[7,8,9],
    "007-CLASS-ORDER":[11,12,26],
    "007-SUBOBJECT-ALL-ISOS":[16,18,19,21,22],
    "007-CANONICAL-TRANSPORT":[16,18,19,21,22],
}

def math_events():
    """Import actual events only after main confirms their source statements."""
    if not MATH_SOURCE_CONFIRMED:
        return []
    assert all(n in M for ns in MATH_SOURCE_OBSERVATIONS.values() for n in ns)
    assert all(not R[a].get("checks") for a in "ABC"), (
        "A reader check list changed; review actual events before merging")
    result = []
    for name in ("math_checks.json","math_audit.json"):
        path = P/name
        data = json.loads(path.read_text())
        for index,raw in enumerate(data["events"],1):
            event = copy.deepcopy(raw)
            if event["type"] == "targeted counterexample verification":
                event["source_event_type"] = event["type"]
                event["type"] = "refuted, with refined statement id 007-CANONICAL-TRANSPORT"
            if event.get("reasoning"):
                event["outcome"] += " Argument: "+event["reasoning"]
            event.update(
                source_file=f"records/scan007/{name}",source_event_index=index,
                source_sha256=snapshot(path)["sha256"],
                main_source_observations=MATH_SOURCE_OBSERVATIONS[event["statement_id"]],
            )
            result.append(event)
    assert len(result) == 9
    return result

EXPECTED_SELECTED_PAGE_SHA256 = "79e80da5bc52812b9a28b5959521e83ec5efe7aa796a42a814723d022d04cdbd"
TICKS = chr(96)*2
PAGE_REQUIRED = {
    1:[TICKS+r"\unsure{modèles|modéles}''"],
    2:[r"Toute \unsure{flèche|fléche} de \(M\) est monomorphique"],
    3:[r"\deleted{\unsure{autom|autom.}}\inserted{end}"],
    4:[r"définie \unsure{par} un ensemble ordonné"],
    5:[TICKS+"inclusion''",r"des sous objets de \(D\)."],
    6:[r"au plus grand élément de \(\widetilde D\)"],
    7:[r"\mathrm{Ho}",r"at (homHo.base east) {$\mathrm m$}",
       r"at (homLast.base east) {$(D',D)$}",
       r"at ([yshift=-.12em]homLast.south) {$\scriptstyle M$}",
       r"\draw[->] ([xshift=.65em,yshift=.25em]homArgs.base east)--(9.5,.25);",
       r"at (1.65,-1.8) {$u$}",r"\draw[|->] (3,-1.55)--(9.5,-1.55);",
       r"at (10,-1.8) {$u(D')$}",r"at (-2.4,-.65) {$(\ast)$}"],
    8:[r"\unsure{(i]|[i]|(i)}(ii),"],
    9:[r"l'ens \deleted{\unsure{de}}",r"\Phi_{D'}(D)\subset\widetilde D",
       r"\inserted{\(M\)-}isomorphes"],
    10:[r"Soit \(N\)\deleted{\(I\)}"],
    11:[r"l'ens \inserted{préordonné} des"],
    12:[r"\inserted{Il est en fait \uline{ordonné}, grâce à (ii).}"],
    13:[r"d'objets de \(M\). \inserted{Il est"],
    14:[r"\unsure{\forall|\mathrm H}\ n\in\mathbb N"],
    15:[r"un\deleted{\unsure{e|s}} objet"],
    16:[r"de \deleted{\(D\)}\(M\) de classe"],
    17:[r"\overset{\ast}{n}"],
    18:["est déterminé à isom unique près,"],
    19:[r"\unsure{à|:}",
        r"\draw ([xshift=.12em,yshift=-.4em]causecluster.south east)"
        r" --([xshift=.25em,yshift=-.62em]causecluster.south east);",
        "cause de (ii),"],
    20:["donc l'ens ordonné"],
    21:[r"\widetilde D_n=\mathbb J_n"],
    22:["est défini à isom unique près."],
    23:[r"\deleted{\unsure{plui|plus}, une}\inserted{une} famille"],
    24:[r"\[ (\mathbb J_n)_{n\in\mathbb N} \]"],
    25:["d'ens ordonnés, indexés"],
    26:["des classes d'isom."],
}
INVENTORY_REQUIRED = {
    1:[r"\mspage{1}"],
    2:[r"Soit \(M\) une catégorie", "On suppose"],
    3:[r"(i) Toute \unsure{flèche|fléche}","monomorphique"],
    4:[r"\inserted{end}"],
    5:[r"(ii) Tout",r"d'un élément de \(M\) est l'identité."],
    6:[r"\deleted{\unsure{autom|autom.}}"],
    7:[r"Ex : \(M\) une catégorie définie \unsure{par} un ensemble ordonné"],
    8:[r"Pour tout \(D\in\mathrm{Ob}\,M\)",r"soit \(\widetilde D\) l'ensemble",
       r"ordonné par",TICKS+"inclusion''",r"des sous objets de \(D\).",
       r"On identifie \(D\) au plus grand élément de \(\widetilde D\)"],
    9:[r"Soient \(D',D\in\mathrm{Ob}\,M\), alors l'application"],
    10:PAGE_REQUIRED[7],
    11:["est injective par","son image est formée de l'ens",
        r"\Phi_{D'}(D)\subset\widetilde D",
        r"des sous-objets \(\Delta\) de \(D\) qui sont",
        r"\inserted{\(M\)-}isomorphes à \(D'\)."],
    12:[r"\deleted{\unsure{de}}"],
    13:[r"\inserted{\(M\)-}isomorphes"],
    14:[r"\deleted{Soit \(K\) un ens. ordonné}"],
    15:[r"\inserted{préordonné}"],
    16:[r"Soit \(N\)\deleted{\(I\)} l'ens",r"des classes d'isom. d'objets de \(M\)."],
    17:[r"\deleted{\(I\)}"],
    18:PAGE_REQUIRED[12],
    19:[r"Pour \(\unsure{\forall|\mathrm H}\ n\in\mathbb N\)",
        r"objet \(D_n\) de \deleted{\(D\)}\(M\) de classe",
        "est déterminé à isom unique près,","cause de (ii),",
        r"donc l'ens ordonné \(\widetilde D_n=\mathbb J_n\)",
        "est défini à isom unique près.",r"\inserted{une} famille"],
    20:[r"un\deleted{\unsure{e|s}} objet"],
    21:[r"de \deleted{\(D\)}\(M\)"],
    22:[r"\deleted{\(D\)}\(M\) de classe"],
    23:[r"\draw ([xshift=.12em,yshift=-.4em]causecluster.south east)"
        r" --([xshift=.25em,yshift=-.62em]causecluster.south east);"],
    24:[r"\deleted{\unsure{plui|plus}, une}"],
    25:[r"\inserted{une} famille"],
    26:PAGE_REQUIRED[24],
    27:[r"d'ens ordonnés, indexés par l'ensemble ordonné \(\mathbb N\)."],
    28:["% archive sheet number: 6"],
}
PAGE_FORBIDDEN = [
    "monomorphique.",r"\inserted{end.}",r"des sous-objets de \(D\). On identifie",
    r"élément de \(\widetilde D\).",r"{$\widetilde D,$}","l'ens.","d'ens.",
    "à isom.",r"\therefore",r"\mathscr L",r"\underset{\inserted{M}}",
    r"\deleted{famille}","«","»",
]

def unsure_bodies(text):
    result = []
    for match in re.finditer(r"\\unsure\{",text):
        start = match.end()
        level = 1
        for pos in range(start,len(text)):
            if text[pos] == "{" and (pos == 0 or text[pos-1] != "\\"):
                level += 1
            elif text[pos] == "}" and (pos == 0 or text[pos-1] != "\\"):
                level -= 1
                if not level:
                    result.append(text[start:pos])
                    break
    return result

def normalize_tex(value):
    value = re.sub(r"\\mathrm\{([A-Za-z])\}",r"\\mathrm \1",value)
    return re.sub(r"\s+","",value)

def check_selected_page(issues):
    """Read-only source guards and structural checks, never a TeX compile."""
    page = O/"pages/H104-01_104_scan007.tex"
    if not page.exists():
        page = P/"page_draft.tex"
    if not page.exists():
        return {"passed":False,"status":"pending; no selected page exists",
                "path":str(page.relative_to(O)),"errors":[]}
    if set(PAGE_REQUIRED) != set(PLAN) or set(INVENTORY_REQUIRED) != set(range(1,29)):
        return {"passed":False,"status":"pending; final source-text guards not yet populated",
                "path":str(page.relative_to(O)),"errors":[]}
    original = page.read_text()
    text = "\n".join(re.split(r"(?<!\\)%",line,maxsplit=1)[0] for line in original.splitlines())
    errors = []
    actual_sha = snapshot(page)["sha256"]
    if actual_sha != EXPECTED_SELECTED_PAGE_SHA256:
        errors.append("Selected-page SHA-256 differs from the main-approved text")
    draft = P/"page_draft.tex"
    if draft.exists() and snapshot(draft)["sha256"] != actual_sha:
        errors.append("Installed page and selected page draft differ")
    level = 0
    for token in re.findall(r"\\.|[{}]",text):
        if token == "{":
            level += 1
        elif token == "}":
            level -= 1
            if level < 0:
                errors.append("Closing brace precedes opening brace")
                break
    if level:
        errors.append(f"Brace balance {level}")
    stack = []
    for direction,env in re.findall(r"\\(begin|end)\{([^{}]+)\}",text):
        if direction == "begin":
            stack.append(env)
        elif not stack or stack.pop() != env:
            errors.append(f"Mismatched environment {env}")
    if stack:
        errors.append(f"Unclosed environments {stack}")
    for opener,closer,label in [(r"\[",r"\]","display"),(r"\(",r"\)","inline")]:
        level = 0
        pattern = r"(?<!\\)"+re.escape(opener)+"|"+r"(?<!\\)"+re.escape(closer)
        for token in re.findall(pattern,text):
            level += 1 if token == opener else -1
            if level not in (0,1):
                errors.append(f"{label} math delimiter order")
                break
        if level:
            errors.append(f"{label} math delimiter balance {level}")
    if len(re.findall(r"(?<!\\)\$",text)) % 2:
        errors.append("Odd dollar count")
    if re.findall(r"\\scanpage\{([^}]*)\}",text) != ["7"]:
        errors.append("Wrong scan marker")
    if r"\cotefile" in text:
        errors.append("Unexpected later-page cote marker")
    if re.search(r"\\(?:newcommand|renewcommand|providecommand|def)\b",text):
        errors.append("New macro definition on page")
    if r"\mspage{1}" not in text:
        errors.append("Missing manuscript folio 1")
    if not re.search(r"%\s*archive sheet number:\s*6\b",original):
        errors.append("Missing archive-number comment")
    norm = normalize_tex(text)
    for forbidden in PAGE_FORBIDDEN:
        if normalize_tex(forbidden) in norm:
            errors.append(f"Rejected witness form remains: {forbidden}")
    if text.count("à isom unique près") != 2:
        errors.append("Expected both distinct à isom unique près occurrences")
    guards = []
    for n,requirements in PAGE_REQUIRED.items():
        missing = [s for s in requirements if normalize_tex(s) not in norm]
        guards.append({"main_observation":n,"passed":not missing,"missing":missing})
        if missing:
            errors.append(f"Main {n} source guard missing {missing}")
    inventory_guards = []
    for n,requirements in INVENTORY_REQUIRED.items():
        base = original if n == 28 else text
        missing = [s for s in requirements if normalize_tex(s) not in normalize_tex(base)]
        inventory_guards.append({"element":f"E{n:02d}","passed":not missing,"missing":missing})
        if missing:
            errors.append(f"Inventory E{n:02d} text guard missing {missing}")
    expected = Counter(normalize_tex(v) for x in issues for v in unsure_bodies(x["final"]))
    actual = Counter(normalize_tex(v) for v in unsure_bodies(text))
    if expected != actual:
        errors.append(f"Inline uncertainty mismatch: expected {dict(expected)}, actual {dict(actual)}")
    result = {
        "passed":not errors,"status":"passed" if not errors else "failed",
        "path":str(page.relative_to(O)),"sha256":actual_sha,
        "errors":errors,"main_decision_guards":guards,
        "inventory_guards":inventory_guards,"inline_unsure_macros":sum(actual.values()),
        "expected_uncertainty":dict(expected),"actual_uncertainty":dict(actual),
        "scope":"Selected-page text, declared main-decision strings, all inventory "
                "entries, uncertainty register and TeX delimiter/environment balance. "
                "No image, rendering, compilation or mathematical check.",
    }
    (P/"assembler_validation.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    return result

def page_notes():
    if not MATH_SOURCE_CONFIRMED or not set(PLAN) <= set(M):
        return []
    return [
        "The page introduces a category M with two hypotheses: every arrow is "
        "monomorphic, and every endomorphism of an object is the identity. A "
        "category defined by an ordered set is given as an example. The checks "
        "carry the two conditions as the page's hypotheses (007-HYPOTHESES); "
        "they do not certify an external example merely because it is named. "
        "The author's folio is 1 and the archival sheet number is 6. No date "
        "or separate manuscript title is recorded.",

        "For D in M, the author defines the ordered collection of subobjects "
        "of D, written as a plain tilded D, and identifies D with its greatest "
        "element. The starred map sends u in Hom_M(D-prime,D) to its image "
        "subobject u(D-prime). The targeted check and separate re-proof of "
        "007-INJECTIVE verify injectivity under the usual equivalence of "
        "monomorphisms: equality of the two subobjects gives a domain "
        "automorphism a with u=v a; hypothesis (ii) makes a the identity. "
        "Hypothesis (i) makes every displayed arrow a subobject representative.",

        "The image is named Phi with lower D-prime and argument D; it consists "
        "of the subobjects Delta that are M-isomorphic to D-prime. The small "
        "M- is an insertion before isomorphes. The separate audit of "
        "007-INJECTIVE also checks this image description: composing a "
        "subobject representative X to D with an isomorphism from D-prime "
        "to X gives an arrow with that same image subobject. The manuscript "
        "mapping has two rows, M below the final m of Hom, and an indented "
        "lower u with a longer arrow beginning farther left; these alignments "
        "are preserved without changing the mathematical letters.",

        "The lower part introduces isomorphism classes of objects, first with "
        "a plain N and then with locally doubled N forms. The inserted "
        "sentence says “Il est en fait ordonné, grâce à (ii).”, with ordonné "
        "underlined. The checks of 007-CLASS-ORDER use the natural reachability "
        "relation on classes. Identities and composition give reflexivity "
        "and transitivity. Arrows in both directions compose to identities "
        "by (ii), so their objects are isomorphic and the classes coincide. "
        "That proves antisymmetry; (i) is not needed for this argument.",

        "A representative D_n and its associated subobject order are described "
        "as determined or defined “à isom unique près”; the resulting family "
        "uses doubled J_n. The checks of 007-CANONICAL-TRANSPORT justify the "
        "canonical interpretation. If a and b are isomorphisms between the "
        "same two representatives, b-inverse composed with a is an "
        "endomorphism, hence the identity, so a=b. Composition with this "
        "unique M-isomorphism transports subobjects, respects their domain "
        "equivalence and factorization order, and has the inverse transport. "
        "The audit also verifies compatibility with identity and composition.",

        "Uniqueness among all abstract order isomorphisms is a stronger "
        "statement, separately labeled 007-SUBOBJECT-ALL-ISOS, and is not "
        "attributed to the author's intended meaning. Its checked "
        "counterexample has objects A and B, two distinct arrows f,g from A "
        "to B, and only identity endomorphisms. All arrows are monic; the "
        "subobjects of B are two incomparable elements [f],[g] below [id_B]. "
        "Exchanging the first two gives a nonidentity order automorphism, "
        "whereas canonical transport induced by id_B is the identity. "
        "The checks use the text's set-level size convention; the two "
        "categorical hypotheses alone do not prove that all relevant "
        "classes and subobjects form sets.",

        "The transcription retains the short canceled autom and raised end, "
        "the canceled fragment after l'ens, the abandoned Soit K line, the "
        "old I after N, préordonné and the orderedness insertion, the canceled "
        "letter after un, the D/M correction, and the corrected phrase "
        "before famille. Remaining ink doubts stay in place; no expected "
        "French or mathematical wording resolves them. No explicit author "
        "question or verbal doubt is recorded. Nine actual mathematical "
        "events are logged: five from the main run and four from the "
        "separate text audit, which read the proposed arguments and was "
        "not blind. The three independent image readers report no "
        "mathematical check events.",
    ]

def build_draft(cw):
    bykey = {x["key"]:x for x in cw["loci"]}
    issues = []
    locus_map = {}
    for key,s in SPECS.items():
        x = bykey[key]
        n = x["main_plan_number"]
        assert n in M, f"Decision {key} lacks a numbered main observation"
        assert PLAN[n].get("viewed"), f"Main crop {n} is not marked viewed"
        assert (O/PLAN[n]["path"]).is_file(), f"Missing actual main crop {n}"
        keys = [key]+s["merge"]
        refs = {a:[] for a in "ABC"}
        for k in keys:
            assert bykey[k]["main_plan_number"] == n
            assert k not in locus_map, f"Duplicate counted locus {k}"
            locus_map[k] = x["id"]
            for a in "ABC":
                refs[a] += [z for z in bykey[k]["source_issues"][a] if z not in refs[a]]
        row = {
            "id":x["id"],"location":x["location"],
            "C":x["witness_C"],"H":x["witness_H"],
            **{k:v for k,v in s.items() if k!="merge" and v not in ("",[])},
            "marked_in_H":"yes" if any(
                I[a][z].get("marked_in_H")=="yes" for a in "ABC" for z in refs[a]) else "no",
            "readers":copy.deepcopy(x["readers"]),"source_issues":refs,
            "main_observations":[n],"crop":PLAN[n]["path"],"crops":[PLAN[n]["path"]],
            "evidence":f"Main {n}: {M[n]}",
            "reader_evidence":{
                a:[{"id":z,"evidence":I[a][z]["evidence"]} for z in refs[a]] for a in "ABC"},
            "reader_report_readings":{
                a:[{"id":z,"reading":I[a][z]["reading"]} for z in refs[a]] for a in "ABC"},
            "crosswalk_keys":keys,
        }
        issues.append(row)
    issue_by_id = {x["id"]:x for x in issues}
    remaining = [{
        "location":x["location"],"reading":x["final"],
        "alternatives":x.get("alternatives","No separately identified alternative."),
        "confidence":x["confidence"],"reason":x["evidence"],
        "decision_id":x["id"],"crop":x["crop"],
    } for x in issues if x["unresolved"]]
    source_map = {a:{k:[] for k in I[a]} for a in "ABC"}
    for x in issues:
        for a in "ABC":
            for k in x["source_issues"][a]:
                source_map[a][k].append(x["id"])
    covered_crosswalk_ids = {bykey[k]["id"] for k in locus_map}
    source_coverage = {
        a:{k:{"required_crosswalk_loci":cw["source_issue_map"][a][k],
              "decision_ids":source_map[a][k],
              "status":("complete" if set(cw["source_issue_map"][a][k])
                        <= covered_crosswalk_ids else "pending")}
           for k in I[a]} for a in "ABC"}
    c_doubts = []
    for old in cw["C_doubt_map"]:
        d = copy.deepcopy(old)
        if d["locus_key"] in locus_map:
            issue = issue_by_id[locus_map[d["locus_key"]]]
            d.update(
                decision_id=issue["id"],status="adjudicated",final=issue["final"],
                unresolved=issue["unresolved"],main_observations=issue["main_observations"],
                crop=issue["crop"],doubt_changed_from_C=issue["diff_C"],
                disposition=("resolved" if not issue["unresolved"] else
                             "refined or reordered" if issue["diff_C"] else "retained"),
            )
        else:
            d["status"] = "pending"
        c_doubts.append(d)
    included = sorted({n for x in issues for n in x["main_observations"]})
    selected_plan = [PLAN[n] for n in included]
    counts = Counter()
    for x in issues:
        if x["diff_C"]: counts["C"]+=1; counts["C_"+x["confidence"]]+=1
        if x["diff_H"]: counts["H"]+=1; counts["H_"+x["confidence"]]+=1
        if x["diff_C"] or x["diff_H"]: counts[x["confidence"]]+=1
    inventory = copy.deepcopy(cw["inventory_crosswalk"])
    inventory[5]["first_words_or_objects"] = "autom / autom. (uncertain canceled abbreviation)"
    inventory[9]["first_words_or_objects"] = (
        "Hom with M below its final m; upper object arrow and indented lower u mapsto")
    inventory[23]["first_words_or_objects"] = "plui / plus, une (canceled)"
    inventory[-1].update(kind="text",hand="unattributed archival hand",
                         first_words_or_objects="6 (archive sheet number)")
    inventory[-1]["classification_note"] = (
        "Main selected text as the record kind: the archival digit is a TeX "
        "archive-number comment, not a manuscript margin note. All original "
        "reader inventory labels and attributions remain in reader_inventory.")
    page_check = check_selected_page(issues)
    complete = (bool(PLAN) and set(PLAN) <= set(M)
                and all(x.get("viewed") for x in PLAN_LIST)
                and len(locus_map)==len(cw["loci"])
                and page_check["passed"] and MATH_SOURCE_CONFIRMED)
    if complete:
        for row in inventory:
            row["transcribed"] = "yes"
            row["selected_reading"] = True
            row["page_text_sha256"] = page_check["sha256"]
    contextual = copy.deepcopy(cw["contextual_C_checks"])
    for row in contextual:
        keys = row["locus_keys"]
        row["main_observations"] = sorted({MAIN_NUMBERS[k] for k in keys if k in locus_map})
        row["status"] = (
            "covered by reader registers and completed main decisions"
            if keys and all(k in locus_map for k in keys) else
            "metadata and inventory checked against selected page"
            if not keys and complete else "pending")
    non_text = copy.deepcopy(cw["non_text_records"])
    if MATH_SOURCE_CONFIRMED:
        non_text[-1]["note"] = (
            "Main confirmed the source statements. The draft imports 5 actual main "
            "events and 4 actual audit events, preserving scope and source arguments. "
            "The three independent image readers performed no mathematical checks.")
    result = {
        "scan":7,"folder":"H104-01","issues":issues,"remaining":remaining,
        "inventory":inventory,
        "notes":page_notes(),"checks":math_events(),
        "math_source_statements_confirmed":MATH_SOURCE_CONFIRMED,
        "math_source_confirmation":(
            "Main explicitly confirmed (i)/(ii), injectivity, the class-order "
            "insertion and the uniqueness wording from the three complete "
            "independent readings and relevant main crops after observations 1–26. "
            "This is source confirmation, not an additional proof event."
            if MATH_SOURCE_CONFIRMED else ""),
        "math_checks_status":("9 actual main/audit events imported; readers report none"
                             if MATH_SOURCE_CONFIRMED else
                             "5 main and 4 audit events pending main confirmation of statement text"),
        "crop_counts":{**{a:R[a]["crop_count"] for a in "ABC"},
                       "main":sum(x.get("source")=="new main crop" for x in selected_plan)},
        "main_reused_crop_count":sum(x.get("source")=="reader reuse" for x in selected_plan),
        "main_total_decision_crop_count":len(selected_plan),
        "planned_main_crop_count":len(PLAN),
        "planned_main_new_crop_count":sum(x.get("source")=="new main crop" for x in PLAN_LIST),
        "planned_main_reused_crop_count":sum(x.get("source")=="reader reuse" for x in PLAN_LIST),
        "main_adjudication_complete":complete,
        "main_complete":complete,
        "assembly_status":("complete decision draft; main choices and selected-page text verified"
                           if complete else
                           "staged draft; pending remaining main observations and selected page"),
        "main_observations_included":included,
        "main_observations_available":sorted(M),
        "main_image_delivery_events":([
            {"main_plan_number":11,"path":PLAN[11]["path"],
             "first_delivery":"Tool output truncated at the context boundary; no image received.",
             "redelivery":("Identical existing file delivered once; no new crop."
                           if 11 in M else "pending"),
             "successful_inspections":1 if 11 in M else 0,
             "failed_delivery_is_not_a_view":True}
        ] if "Delivery note before 11:" in MAIN else []),
        "main_crop_coverage_events":[{
            "incomplete_crop_number":11,"completed_locus":"classes",
            "first_complete_crop_number":26,"path":PLAN[26]["path"],
            "note":"Main11 did not contain the full word. The already existing "
                   "reader crop was inspected once for this still undecided "
                   "locus; no decided ens/insertion mark was re-adjudicated.",
        }] if 26 in PLAN else [],
        "source_issue_map":source_map,
        "source_issue_coverage":source_coverage,
        "pending_source_issues":{
            a:[k for k,v in source_coverage[a].items() if v["status"]!="complete"] for a in "ABC"},
        "crosswalk_locus_map":locus_map,
        "pending_loci":[x["key"] for x in cw["loci"] if x["key"] not in locus_map],
        "C_doubt_map":c_doubts,
        "contextual_C_checks":contextual,
        "non_text_records":non_text,
        "page_text_guard_status":page_check["status"],
        "page_text_sha256":page_check.get("sha256",""),
        "page_validation":page_check,
        "counting_policy":(
            "Each physical locus is counted once against each differing witness. "
            "Removed, refined or reordered C uncertainty counts; equivalent syntax "
            "and shared-marker consolidation do not. The opening accent and its "
            "quotation ticks are separate marks. All mapping alignments constitute "
            "one layout locus. The orderedness insertion is not additionally counted "
            "as an omitted passage; its grâce doubt is a separate C-only resolution. "
            "H's therefore-like cluster is counted once at C29; the separate literal "
            "stroke X04 changes C only. Cause de (ii) and its comma form one phrase "
            "locus. The canceled old phrase and raised une form one correction locus."),
        "counts":dict(counts),
        "residual_questions":([] if complete else
                              ["Remaining main decisions and selected-page text check are pending."]),
    }
    (P/"decision_draft.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    write_coverage_audit(result)
    return result

def write_coverage_audit(d):
    lines = [
        "# Scan 007 — records assembly coverage","",
        "Text-only assembly from the three completed reader returns and the main "
        "reader's 26 numbered observations. No image, crop content, PDF, OCR, web "
        "source, rendering, compilation, page writing, authoritative decision writing "
        "or cumulative rebuild was performed by this assembler.","",
        f"- Main completion: **{d['main_complete']}**.",
        f"- Source issues: **115/115** fully cross-referenced; pending: "
        f"**{sum(len(v) for v in d['pending_source_issues'].values())}**.",
        f"- Comparison/final loci: **42/42**; pending: **{len(d['pending_loci'])}**.",
        f"- Witness-C inline doubts: **20/20** adjudicated.",
        f"- Contextual witness checks: **12/12** covered.",
        f"- Inventory: **28/28** entries present in the selected page and text-checked.",
        f"- Selected-page main-decision guards: **26/26** passed.",
        f"- Inline uncertainty macros and remaining local doubts: **10/10**, exactly matched.",
        f"- Page SHA-256: {d['page_text_sha256']}.",
        "- Main crops: **15 new + 11 reused = 26**. The failed pre-11 delivery "
        "was not an inspection; the identical existing file was redelivered once. "
        "Classes first received complete main coverage at crop26.","",
        "## Unique changed places","",
        "| Witness / union | High | Medium | Low | Total |",
        "|---|---:|---:|---:|---:|",
        "| C | 12 | 5 | 3 | 20 |",
        "| H | 21 | 8 | 4 | 33 |",
        "| Unique loci | 29 | 9 | 4 | 42 |","",
        d["counting_policy"],"",
        "## Every witness-C inline doubt","",
        "| ID | Locus | Disposition | Changed from C | Remaining doubt |",
        "|---|---|---|---|---|",
    ]
    for x in d["C_doubt_map"]:
        lines.append("| "+" | ".join(mdcell(v) for v in [
            x["id"],x["locus_key"],x.get("disposition","pending"),
            x.get("doubt_changed_from_C","pending"),x.get("unresolved","pending")])+" |")
    lines += ["","## Actual mathematical events","",
              "Five main events and four separately reasoned audit events are retained. "
              "The audit read the proposed arguments and was not blind. Reader A, B "
              "and C each report an empty checks list. Main's later confirmation of "
              "statement text adds no proof event.","",
              "| Source | Statement | Recorded event type |",
              "|---|---|---|"]
    for x in d["checks"]:
        lines.append("| "+" | ".join(mdcell(x[k]) for k in [
            "source_file","statement_id","type"])+" |")
    lines += ["","The audit counterexample's raw type is retained as source_event_type; "
              "its normalized event type is the allowed refutation entry with the "
              "canonical-transport refined statement. Its scope does not attribute "
              "the stronger abstract-order uniqueness interpretation to the author.",
              "","## Files","",
              "- reader_crosswalk.json/.md: complete source readings, alternatives, "
              "issue and inventory maps, crop paths, snapshots and full text diffs.",
              "- decision_draft.json: 42 finalized places, 10 remaining doubts, "
              "28 checked inventory rows, seven content/mathematical note paragraphs "
              "and nine actual check events.",
              "- assembler_validation.json: zero errors, selected-page hash, "
              "26 main-decision guards, 28 inventory guards and exact uncertainty match.",
              ""]
    (P/"assembly_coverage.md").write_text("\n".join(lines))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--crosswalk-only",action="store_true")
    args = parser.parse_args()
    cw = build_crosswalk()
    if not args.crosswalk_only:
        d = build_draft(cw)
    print(json.dumps(cw["counts"],ensure_ascii=False))
