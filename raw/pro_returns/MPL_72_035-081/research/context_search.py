#!/usr/bin/env python3
"""Reproduce note-by-note literal searches of the three supplied context files."""
from pathlib import Path
import argparse, csv, hashlib, json, re

HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument("--context",type=Path,default=HERE.parent.parent/"context")
args=parser.parse_args()
files=[args.context/"README.md",args.context/"LM2_CONGRUENCE_ROWS.md",
       args.context/"notes"/"RESULTS_STATE.md"]
for p in files:
    if not p.is_file():
        raise SystemExit("Missing supplied context file: "+str(p))
context=[(p.relative_to(args.context).as_posix(),p.read_text().splitlines()) for p in files]
manifest=[{"path":p.relative_to(args.context).as_posix(),
           "sha256":hashlib.sha256(p.read_bytes()).hexdigest(),
           "bytes":p.stat().st_size} for p in files]
source_files=["source_register.md","group_quadric.md","invariant_subspaces.md",
              "bridge_definition.md","enumerations.md","documentary_and_scope.md",
              "split_clifford.md","self_flags_review.md"]
heading=re.compile(r"(?m)^(?:#{2,4}\s+|\*\*)(?P<id>N\d{3}(?:[–-]\d{3})?(?:\.\d+)?|A\d{2}|IS\d{2}|BD\.\d+|E\d{2}|D\d{3}|O\d{2}|T01|B12\.\d+|F\d{2})(?=\s|[. —*])")
id_re=re.compile(r"(?:LM\d(?:_PUSH)?\s+[A-Z]\.[A-Za-z]?\d+|72-(?:automorphisms-deform-gm-to-ga|invariant-subspaces-string))")
notes=[]
for name in source_files:
    path=HERE/name
    if not path.exists():
        raise SystemExit("Missing note source: "+name)
    content=path.read_text()
    matches=list(heading.finditer(content))
    for index,m in enumerate(matches):
        end=matches[index+1].start() if index+1<len(matches) else len(content)
        block=content[m.start():end]
        # A proof appendix after the final note is not part of that note's query.
        first_proof=re.search(r"(?m)^## (?:Appendix|B\. |Explicit|The conic|Literature|Context scope|Reproduction)",block)
        if first_proof: block=block[:first_proof.start()]
        explicit=re.search(r"<!-- context-query:\s*(.*?)\s*-->",block,re.S)
        queries=[q.strip() for q in explicit.group(1).split(";")] if explicit else []
        queries += id_re.findall(block)
        item=m.group("id")
        if item.startswith("IS"): queries+=["72-invariant-subspaces-string"]
        elif item.startswith("A"): queries+=["72-automorphisms-deform-gm-to-ga"]
        elif item.startswith("E"): queries+=["72-automorphisms-deform-gm-to-ga","enumerations"]
        elif item.startswith("BD"): queries+=["B5","B12"]
        elif item.startswith("F"): queries+=["calculations","72-invariant-subspaces-string","72-automorphisms-deform-gm-to-ga"]
        queries=list(dict.fromkeys(q for q in queries if q))
        if not queries: queries=["calculations","regular polyhedron"]
        notes.append({"id":item,"source":name,"line":content[:m.start()].count("\n")+1,"queries":queries})
for name in ["enumeration_reading_questions.csv","enumeration_catalogue.csv","case_catalogue.csv"]:
    with (HERE/name).open() as f:
        for line,row in enumerate(csv.DictReader(f),2):
            ids=id_re.findall(row.get("context_id",""))
            queries=ids+["enumerations","calculations"]
            if row["id"].startswith("P") and row.get("scan") in {"080","081"}:
                queries+=["72-invariant-subspaces-string"]
            notes.append({"id":row["id"],"source":name,"line":line,"queries":list(dict.fromkeys(queries))})
rows=[]
for note in notes:
    note_hits=0
    for query in note["queries"]:
        hits=[]
        for name,lines in context:
            for n,line in enumerate(lines,1):
                if query.casefold() in line.casefold():
                    hits.append({"note_id":note["id"],"note_source":note["source"],
                                 "query":query,"context_file":name,"context_line":n,
                                 "matched_ids":"; ".join(dict.fromkeys(id_re.findall(line))),
                                 "excerpt":line[:220]})
        if not hits:
            hits=[{"note_id":note["id"],"note_source":note["source"],"query":query,
                   "context_file":"","context_line":"","matched_ids":"","excerpt":"No literal match in the three supplied files."}]
        note_hits+=sum(bool(h["context_file"]) for h in hits)
        rows.extend(hits)
    note["matching_rows"]=note_hits
with (HERE/"context_search_audit.csv").open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["note_id","note_source","query","context_file","context_line","matched_ids","excerpt"])
    w.writeheader();w.writerows(rows)
(HERE/"context_search_manifest.json").write_text(json.dumps({"sources":manifest,"notes":notes,"note_count":len(notes),"audit_rows":len(rows)},indent=2,ensure_ascii=False)+"\n")
print(json.dumps({"status":"PASS","note_count":len(notes),"query_count":sum(len(n["queries"]) for n in notes),"audit_rows":len(rows),"source_files":len(files)}))
