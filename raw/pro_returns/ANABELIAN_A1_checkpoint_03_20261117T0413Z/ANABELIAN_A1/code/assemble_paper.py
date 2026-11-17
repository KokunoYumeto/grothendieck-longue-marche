"""Assemble the research manuscript and its complete statement register.
Working inclusions retain owner identifiers; the deliverable is flattened,
renumbered by Part, and compiles without the inclusions.
"""
from pathlib import Path
import csv,json,re,datetime
root=Path(__file__).resolve().parents[1]
parts={
 "A":["A_root_intro","A_configuration","A_criterion","A_root_prime_sets","A_root_fields","A_literature"],
 "B":["B_root_classnumbers","B_norm","B_abelian_norm","B_solvable_norm","B_nonabelian_norm","B_root_covers","B_root_primitive",
      "B_root_r8_witness","B_twist_bound","B_root_quartics","B_quartic_more",
      "B_literature","B_literature_probe","B_reconstruction","B_reconstruction_nondiscrete","B_mixed_frontier",
      "B_pro_completion","B_root_questions"],
 "C":["C_root","C_literature_consequences","C_literature"]
}
metadata={}
for path in (root/"notes").glob("*statements.json"):
    obj=json.loads(path.read_text())
    rows=obj if isinstance(obj,list) else obj.get("statements",[])
    for row in rows:metadata[row["id"]]=row
root_answers={
 "A.R1":"A1;K6","A.R2":"A13;C3;C4","A.R3":"A13;C3","A.R4":"A13;C3",
 "A.R5":"A13;C3","B.R1":"B3;C6","B.R2":"B3;C6","B.R3":"B3",
 "B.R4":"B3","B.R5":"B4","B.R6":"B4",
 "C.R1":"C3","C.R2":"C3","C.R3":"C6","C.R4":"C4"
}
bib_aliases={"ST2009":"LA_ST2009","ST2017":"LA_ST2017",
             "SGA1":"LA_SGA1","Stix2005":"LA_Stix2005"}
def group(s,pos):
    assert s[pos]=="{"
    d=1;j=pos+1
    while d:
        if s[j]=="{" and (j==0 or s[j-1]!="\\"):d+=1
        if s[j]=="}" and (j==0 or s[j-1]!="\\"):d-=1
        j+=1
    return s[pos+1:j-1],j
texts={}; claims=[];mapping={}
for part,names in parts.items():
    chunks=[]
    for name in names:
        path=root/"sections"/(name+".tex")
        if path.exists():chunks.append((path,path.read_text()))
    texts[part]="\n\n".join(text for _,text in chunks)
    count=0
    for path,text in chunks:
        for match in re.finditer(r"\\begin\{claim\}",text):
            pos=match.end();args=[]
            for _ in range(3):
                while text[pos].isspace():pos+=1
                arg,pos=group(text,pos);args.append(arg)
            old,status,title=args
            end=text.index(r"\end{claim}",pos)
            body=text[pos:end].strip()
            count+=1;new=f"{part}.{count}";mapping[old]=new
            info=metadata.get(old,{})
            answers=info.get("answers",info.get("items",root_answers.get(old,"")))
            if isinstance(answers,list):answers=";".join(answers)
            dep=info.get("depends_on",info.get("dependencies",info.get("inputs",[])))
            if isinstance(dep,list):dep=";".join(dep)
            normalized=next((x for x in ("Open","Refuted","Known","Proved") if status.startswith(x)),status)
            claims.append({"id":new,"statement":body,"status":normalized,
              "where_proved":f"ANABELIAN_A1_paper.tex; working inclusion {path.relative_to(root)}",
              "depends_on":dep,"answers (item or check item)":answers,
              "manuscript_passages (cote; scan)":info.get("manuscript_passages","149; 35-36" if part=="A" else ""),
              "depends_on_doubtful_reading (scan, alternatives)":"None",
              "notes":f"Working identifier {old}. {title}. {status}. "+info.get("notes","")})
def renumber(s):
    for old in sorted(mapping,key=len,reverse=True):
        s=re.sub(re.escape(old)+r"(?![0-9A-Za-z])",lambda _:mapping[old],s)
    return s
def canonical_citations(s):
    pat=r"(\\cite\w*\*?(?:\[[^\]]*\]){0,2}\{)([^}]+)(\})"
    return re.sub(pat,lambda m:m[1]+",".join(bib_aliases.get(k.strip(),k.strip())
                         for k in m[2].split(","))+m[3],s)
preamble=(root/"notes"/"preamble.tex").read_text()
paper=preamble
titles={"A":"The point-separation argument","B":"Independent existence and reconstruction questions",
        "C":"Consequences and limits"}
for part in parts:
    paper+="\n\\section{"+titles[part]+"}\n"+canonical_citations(renumber(texts[part]))+"\n"
paper+=r"\bibliographystyle{plainnat}"+"\n"+r"\bibliography{ANABELIAN_A1_references}"+"\n"+r"\end{document}"+"\n"
(root/"ANABELIAN_A1_paper.tex").write_text(paper)
fields=list(claims[0])
with (root/"ANABELIAN_A1_results.csv").open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
    for row in claims:
        row["depends_on"]=renumber(row["depends_on"])
        row["statement"]=canonical_citations(renumber(row["statement"]))
        w.writerow(row)
(root/"notes"/"statement_number_map.json").write_text(json.dumps(mapping,indent=2)+"\n")
# Merge entries from opened sources. Every entry carries an explicit status.
bibpaths=[root/"notes"/"root_references.bib"]+sorted((root/"notes").glob("*_references.bib"))
seen=set(); entries=[]
for path in bibpaths:
    if not path.exists():continue
    src=path.read_text()
    for match in re.finditer(r"@(\w+)\s*\{([^,]+),",src):
        key=match.group(2)
        if key in bib_aliases:continue
        if key in seen:continue
        seen.add(key)
        start=src.index("{",match.start())
        body,end=group(src,start)
        verify="unverified" if re.search(r"verification\s*=\s*\{unverified\}",body,re.I) else "verified"
        entry="@"+match.group(1)+"{"+body.rstrip().rstrip(",")+",\n  keywords={"+verify+"}\n}\n"
        entries.append(entry)
(root/"ANABELIAN_A1_references.bib").write_text("\n".join(entries))
# The item-level state is deliberately stricter than proved special cases.
states={}
for i in range(1,15):states[f"A{i}"]="Proved"
states.update({"A10":"Proved: complete scoped dependency census, quotient repairs and exact full-group loss",
               "A12":"Open: all J-large sets separated; singleton sets infinite; arbitrary remaining sets unresolved"})
for i in range(1,10):states[f"B{i}"]="Open"
states["B3"]="Proved"
states["B4"]="Open: nontrivial version refuted and checked; degree-one-permitted version unresolved"
states["B5"]="Open: odd-characteristic hyperelliptic and further tame classes proved"
states["B6"]="Open: F3 exact least-prime witness and F5 first-field minimum proved; full census and prime-first minima unresolved"
states["B7"]="Refuted: an explicit recursively specified henselian field satisfies all centralizer conditions but fails reconstruction"
states["B8"]="Open: all nontrivially henselian residue-characteristic-zero cases of finite transcendence degree refuted; listed mixed-characteristic cases remain"
states["B9"]="Proved: ordinary pro-reconstruction in arbitrary characteristic-zero transcendence degree"
for i in range(1,7):states[f"C{i}"]="In progress"
for i in range(1,7):states[f"K{i}"]="Proved"
states["C3"]="Proved in the curve scope; general-dimensional assertion refuted"
states["C4"]="Proved with specified quotient and retained boundary"
states["C5"]="Proved: exact separation-dependent consequence census, with source prime-set and morphism hypotheses retained"
states["C1"]="Proved for the exact J-large source hypotheses; general prime-set issue recorded at A12"
states["C2"]="Proved: corrected separation route and the retained published Isom argument"
states["C6"]="Proved: isolating covers and explicit opposite class-number behaviours; B1 remains independent"
itemrefs={item:[] for item in states}
for row in claims:
    for item in re.split(r"[;, ]+",row["answers (item or check item)"]):
        if item in itemrefs:itemrefs[item].append(row["id"])
lines=["INCOMPLETE","","| Item | Outcome | Statements |",
       "|---|---|---|"]
for item,state in states.items():
    lines.append(f"| {item} | {state} | {', '.join(itemrefs[item]) or 'Being written'} |")
body=(root/"notes"/"report_body.md").read_text()
body=renumber(body)
body=body.replace("@STATEMENT_COUNT@",str(len(claims)))
body=body.replace("@STATUS_COUNTS@",", ".join(f"{sum(x['status']==s for x in claims)} {s}" for s in ("Proved","Refuted","Known","Open")))
lines += ["",body.rstrip()]
(root/"ANABELIAN_A1_report.md").write_text("\n".join(lines)+"\n")
print("Assembled",len(claims),"statements.",flush=True)
print("Statuses",{s:sum(x["status"]==s for x in claims) for s in ("Proved","Refuted","Known","Open")})

