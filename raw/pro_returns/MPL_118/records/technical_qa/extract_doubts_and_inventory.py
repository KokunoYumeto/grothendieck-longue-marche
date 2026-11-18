#!/usr/bin/env python3
"""Literal doubt extraction and structural counts; no scans, context, or edits."""
import argparse, collections, csv, hashlib, json, re
from datetime import datetime, timezone
from pathlib import Path
from static_checks import control, group, line, uncomment

PAIRS={"diagram":"diagram","figure":"drawing","margin":"margin note","inserted":"insertion","deleted":"deletion"}
KINDS={"text","display","diagram","drawing","margin note","insertion","deletion"}
SHEET_KINDS={"text","reused_typed","cancelled_draft","cover"}

def scan_number(path):
    match=re.search(r"_scan(\d+)\.tex$",path.name)
    if not match: raise ValueError("unexpected page filename: "+path.name)
    return int(match.group(1))

def literal_macros(raw):
    cleaned=uncomment(raw); macros=[]; i=0
    while i<len(cleaned):
        if cleaned[i]!="\\":
            i+=1; continue
        at=i; cmd,i=control(cleaned,i); macros.append((cmd,at,i))
    return cleaned,macros

def brief(s):
    return re.sub(r"\s+"," ",s).strip()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[2])
    parser.add_argument("--out",type=Path,default=Path(__file__).resolve().parent)
    args=parser.parse_args(); args.out.mkdir(parents=True,exist_ok=True)
    pages=sorted((args.root/"pages").glob("*.tex"))
    inventory_path=args.root/"MPL_118_inventory.csv"
    inventory=list(csv.DictReader(inventory_path.open(newline="")))
    byscan=collections.defaultdict(list); issues=[]
    for row_index,row in enumerate(inventory,2):
        try: scan=int(row["scan"])
        except (ValueError,KeyError):
            issues.append({"type":"invalid_inventory_scan","csv_row":row_index});continue
        byscan[scan].append(row)
        if row.get("cote")!="118":
            issues.append({"type":"unexpected_cote","csv_row":row_index,"value":row.get("cote")})
        if row.get("transcribed")!="yes":
            issues.append({"type":"not_transcribed_yes","csv_row":row_index,"scan":scan,"element":row.get("element")})
        if row.get("kind") not in KINDS:
            issues.append({"type":"unknown_inventory_kind","csv_row":row_index,"value":row.get("kind")})
        if row.get("sheet_kind") not in SHEET_KINDS:
            issues.append({"type":"unknown_sheet_kind","csv_row":row_index,"value":row.get("sheet_kind")})
    ids=collections.Counter((r.get("cote"),r.get("scan"),r.get("element")) for r in inventory)
    for element,count in ids.items():
        if count>1: issues.append({"type":"duplicate_element_id","id":element,"count":count})
    observations=[]; all_doubts=[]; hashes={}
    for page in pages:
        scan=scan_number(page);raw=page.read_text()
        hashes[page.name]=hashlib.sha256(raw.encode()).hexdigest()
        cleaned,macros=literal_macros(raw); counts=collections.Counter(m[0] for m in macros)
        if counts["scanpage"]!=1:
            issues.append({"type":"scanpage_macro_count","scan":scan,"count":counts["scanpage"]})
        invrows=byscan.get(scan,[])
        if not invrows: issues.append({"type":"page_without_inventory_rows","scan":scan})
        kinds=collections.Counter(r["kind"] for r in invrows)
        info={"scan":scan,"file":page.name,"tex_lines":raw.count("\n"),"inventory_rows":len(invrows),
              "inventory_counts":{k:kinds[k] for k in sorted(KINDS)},
              "macro_counts":{k:counts[k] for k in (*PAIRS,"unsure","illegible","scanpage","mspage","cotefile")},
              "display_delimiter_count":counts["["],"comparisons":[]}
        for macro,kind in PAIRS.items():
            info["comparisons"].append({"macro":macro,"inventory_kind":kind,"macro_count":counts[macro],
                "inventory_rows":kinds[kind],"macro_minus_inventory":counts[macro]-kinds[kind]})
        observations.append(info);occurrence=0
        for cmd,start,aftercmd in macros:
            if cmd not in ("unsure","illegible"):continue
            opening=aftercmd
            while opening<len(cleaned) and cleaned[opening].isspace():opening+=1
            body,end=group(cleaned,aftercmd)
            if body is None or opening>=len(cleaned) or cleaned[opening]!="{":
                issues.append({"type":"doubt_argument_unbalanced_or_missing","scan":scan,"tex_line":line(raw,start),"macro":cmd});continue
            occurrence+=1
            all_doubts.append({"occurrence_id":f"118-{scan:03d}-{occurrence:03d}",
                "cote":118,"scan":scan,"file":page.name,"tex_line":line(raw,start),"tex_line_end":line(raw,end-1),
                "macro":cmd,"body":raw[opening+1:end-1],"fragment":raw[start:end],
                "before":brief(raw[max(0,start-110):start]),"after":brief(raw[end:min(len(raw),end+110)]),
                "offset_start":start,"offset_end":end})
    page_scans={scan_number(p) for p in pages}
    for scan in sorted(set(byscan)-page_scans):issues.append({"type":"inventory_without_page_file","scan":scan})
    timestamp=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    notes=("Literal balanced-brace extraction from existing TeX fragments, not a new reading of manuscript images. "
        "tex_line is the exact line in the fragment, not a manuscript line number. No confidence rating or reading "
        "alternative is invented. JSON retains exact macro bodies and fragments; TSV JSON-encodes text fields to "
        "stay one physical line per occurrence.")
    extraction={"created_utc":timestamp,"method":notes,"page_sha256":hashes,"occurrences":all_doubts}
    (args.out/"doubt_occurrences.json").write_text(json.dumps(extraction,ensure_ascii=False,indent=2)+"\n")
    with (args.out/"doubt_occurrences.tsv").open("w",newline="") as out:
        fields=["occurrence_id","cote","scan","file","tex_line","tex_line_end","macro","body_json","fragment_json","before_json","after_json"]
        writer=csv.DictWriter(out,fieldnames=fields,delimiter="\t",lineterminator="\n");writer.writeheader()
        for item in all_doubts:
            row={k:item[k] for k in fields if k in item}
            for field in ["body","fragment","before","after"]:row[field+"_json"]=json.dumps(item[field],ensure_ascii=False)
            writer.writerow(row)
    coverage={"created_utc":timestamp,"scope":"Structural correspondence only; no scan reading or mathematical judgment.",
        "limitations":"Macro counts do not prove element completeness or omissions. Display rows can represent inline or array material, so their count is not directly compared to display delimiters. Text blocks cannot be inferred reliably from paragraph breaks.",
        "inventory_sha256":hashlib.sha256(inventory_path.read_bytes()).hexdigest(),"page_sha256":hashes,
        "page_count":len(pages),"inventory_row_count":len(inventory),"issues":issues,"pages":observations}
    (args.out/"inventory_coverage.json").write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+"\n")
    with (args.out/"inventory_coverage.tsv").open("w",newline="") as out:
        fields=["scan","file","inventory_rows"]+[v+"_"+k for k in PAIRS for v in ("macro","inventory","delta")]+["unsure","illegible","display_delimiters","inventory_display"]
        writer=csv.DictWriter(out,fieldnames=fields,delimiter="\t",lineterminator="\n");writer.writeheader()
        for p in observations:
            row={k:p[k] for k in ["scan","file","inventory_rows"]}
            for c in p["comparisons"]:
                k=c["macro"];row["macro_"+k]=c["macro_count"];row["inventory_"+k]=c["inventory_rows"];row["delta_"+k]=c["macro_minus_inventory"]
            row.update(unsure=p["macro_counts"]["unsure"],illegible=p["macro_counts"]["illegible"],
                display_delimiters=p["display_delimiter_count"],inventory_display=p["inventory_counts"]["display"])
            writer.writerow(row)
    discrepancy_lines=[]
    for p in observations:
        differences=[c for c in p["comparisons"] if c["macro_minus_inventory"]]
        if differences:
            discrepancy_lines.append("| "+f'{p["scan"]:03d}'+" | "+"; ".join(
                f'{c["macro"]}: {c["macro_count"]}/{c["inventory_rows"]} ({c["macro_minus_inventory"]:+d})' for c in differences)+" |")
    summary=f"""# Structural inventory and doubt extraction

Checked {timestamp}. This is a technical pass over saved TeX and CSV files;
no scan images or contextual sources were opened, and no source file was changed.

## Doubt extraction

{len(all_doubts)} literal doubt occurrences were extracted from {len(pages)} pages.
The JSON and TSV include page, exact TeX fragment line, exact body, and short
surrounding text. No confidence judgments have been assigned. TeX fragment line
numbers are not manuscript line numbers.

## Inventory structure

The CSV has {len(inventory)} rows for {len(byscan)} scan numbers.
Structural errors detected: {len(issues)}. See inventory_coverage.json for any
invalid rows, missing pages, duplicate IDs, or transcribed values other than yes.

## Count differences for primary-reader review

Each entry below is macro: occurrences/inventory rows (difference).
A positive difference means more literal macro occurrences than rows of its
corresponding kind. A negative difference means more inventory rows. Neither
proves omission: inventory rows sometimes group several insertions or deletions,
and a drawing or diagram can occur inside a different container. The primary
reader should decide whether separate inventory rows are needed.

| Scan | Nonzero count differences |
| --- | --- |
"""+("\n".join(discrepancy_lines) if discrepancy_lines else "| — | None |")+"""
Displays and prose are not matched one-to-one automatically. The inventory's
display category includes material inside arrays and other containers, whereas
the display-delimiter count includes only explicit display-math delimiters.
Text-block boundaries cannot be recovered reliably from blank lines. Counts
are review aids, not a certification of diplomatic completeness.

## Reproduce

    python3 MPL_118/records/technical_qa/static_checks.py
    python3 MPL_118/records/technical_qa/extract_doubts_and_inventory.py

Both JSON reports preserve the SHA-256 of the actual page versions inspected.
Rerun after final edits before using the extracted positions in a final table.
"""
    (args.out/"STRUCTURAL_REVIEW.md").write_text(summary)
    totals={k:sum(p["macro_counts"][k] for p in observations) for k in (*PAIRS,"unsure","illegible")}
    print(json.dumps({"pages":len(pages),"inventory_rows":len(inventory),"doubt_occurrences":len(all_doubts),
        "macro_totals":totals,"structural_issues":issues,
        "positive_differences":[{"scan":p["scan"],"macro":c["macro"],"macro_count":c["macro_count"],"inventory_rows":c["inventory_rows"]}
        for p in observations for c in p["comparisons"] if c["macro_minus_inventory"]>0]},ensure_ascii=False,indent=2))
if __name__=="__main__":main()

