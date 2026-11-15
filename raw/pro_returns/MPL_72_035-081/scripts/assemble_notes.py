#!/usr/bin/env python3
"""Assemble the complete post-freeze notes; never write a transcription file."""
from pathlib import Path
import csv,json,re

ROOT=Path(__file__).resolve().parent.parent
R=ROOT/"research"
parts=["self_flags_review.md","documentary_and_scope.md","bridge_definition.md",
       "source_register.md","enumerations.md","computation_conventions.md",
       "group_quadric.md","invariant_subspaces.md","split_clifford.md","reproducibility.md"]

def integrate(text):
    text=re.sub(r"(?m)^(#{1,5}) ",r"#\1 ",text)
    # Component links are relative to research/; the combined file sits at root.
    def link(m):
        target=m.group(2)
        if re.match(r"(?:https?://|#|research/)",target): return m.group(0)
        if "context/" in target: return m.group(1)+" (supplied context)"
        return "["+m.group(1)+"](research/"+target+")"
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)",link,text)

def case_table():
    rows=list(csv.DictReader((R/"case_catalogue.csv").open()))
    def esc(s):return str(s).replace("|",r"\|").replace("\n"," ")
    lines=["## Numbered cases and parameter-family enumeration",
           "",
           "The following 31 rows catalogue the prose case lists in addition to the mathematical arrays above. Their totals count the specified labels or members; the state column preserves cancelled labels and source qualifications. The companion case_catalogue.py evaluates each indexed total for dimensions 1–6 and exports the complete inputs and totals.",
           "",
           "| ID | Scan | What is enumerated | Parameters | Total | Documentary state |",
           "|---|---:|---|---|---|---|"]
    for row in rows:
        lines.append("| "+" | ".join(esc(row[k]) for k in ["id","scan","enumerates","parameters","total_expression","state"])+" |")
    return "\n".join(lines)+"\n"

def full_catalogue():
    rows=list(csv.DictReader((R/"enumeration_catalogue.csv").open()))
    def esc(s):return str(s).replace("|",r"\|").replace("\n"," ")
    lines=["## Complete table and enumeration catalogue","",
           "All 36 groups are listed below with their source scans, inputs and totals. The output-name column identifies the complete individual entries; the companion CSV also records the exact context ID, source quotation, qualification and executed command.",
           "",
           "| ID | Scans | What is enumerated | Parameters | Total or formula | Detailed outputs |",
           "|---|---|---|---|---|---|"]
    for row in rows:
        lines.append("| "+" | ".join(esc(row[k]) for k in ["id","scans","what_is_enumerated","parameters","total_or_formula","outputs"])+" |")
    return "\n".join(lines)+"\n"

def literal_questions():
    rows=list(csv.DictReader((R/"enumeration_reading_questions.csv").open()))
    lines=["## Literal formula and index comparisons","",
           "These 28 items retain the first frozen reading and record its exact comparison. Each has kind **reading question**; its context is **Hua, findings register, 72-automorphisms-deform-gm-to-ga**, through the continuant or associated pairing calculation, and none promotes that prior-run group-scheme claim. The quoted source expressions are compact formula encodings; the original typography and uncertainty macros remain in the frozen page.",
           ""]
    for row in rows:
        lines += ["### "+row["id"],"",
                  "**72/"+str(row["scan"]).zfill(3)+"; kind: reading question; source: “"+row["short_quote"]+"”.** "+row["observation"]+" "+row["verification_task"],
                  "",
                  "**Exact residual:** "+row["computed_residual"]+"  \n**Explicit substitution or input:** "+row["explicit_substitution"],""]
    return "\n".join(lines)+"\n"

contents=[(R/"notes_preface.md").read_text()]
for name in parts:
    path=R/name
    if not path.is_file(): raise SystemExit("Missing research component: "+name)
    contents.append(integrate(path.read_text()))
    if name=="enumerations.md":
        contents.extend([full_catalogue(),case_table(),literal_questions()])
notes="\n\n---\n\n".join(contents).rstrip()+"\n"
bad=[(i,ord(c)) for i,c in enumerate(notes) if ord(c)<32 and c not in "\n\r\t"]
if bad:raise SystemExit("Control characters in assembled notes: "+str(bad[:10]))
target=ROOT/"MPL_72_035-081_notes.md"
target.write_text(notes)
print(json.dumps({"path":str(target),"words":len(notes.split()),"bytes":target.stat().st_size,
                  "component_files":len(parts)+1,"case_rows":31}))
