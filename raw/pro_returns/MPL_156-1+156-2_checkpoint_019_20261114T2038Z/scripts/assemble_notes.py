"""Assemble research prose and preserve an actual per-note context search ledger.

This never reads image pixels and never writes a transcription file.
The supplied context is an external input and is not copied into the package.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import json
import re
import subprocess

root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument("--context",type=Path,default=root.parent/"context")
parser.add_argument("--final",action="store_true")
args=parser.parse_args()
parts=root/"records"/"research_parts"
names=["D_definitions.md","A_notes.md","B_notes.md","P_notes.md","T_context.md","Z_bibliography.md"]
missing=[n for n in names if not (parts/n).is_file()]
if args.final:
    assert not missing, f"Missing research sections: {missing}"
text="\n\n".join((parts/n).read_text(encoding="utf-8").rstrip() for n in names if (parts/n).exists())+"\n"
out=root/"MPL_156-1+156-2_notes.md"
out.write_text(text,encoding="utf-8")
matches=list(re.finditer(r"^#{3,4} ([DABPT]\d{2}) — (.+)$",text,re.M))
ledger=[]
for i,m in enumerate(matches):
    stop=matches[i+1].start() if i+1<len(matches) else len(text)
    block=text[m.end():stop]
    search=re.search(r"\*\*Context:\*\* search: (.*?);",block)
    assert search, f"Missing context search: {m.group(1)}"
    terms=[x.strip() for x in search.group(1).split("|") if x.strip()]
    cmd=["rg","-n","-i","-F"]
    for term in terms:cmd+=["-e",term]
    cmd+=["README.md","notes/RESULTS_STATE.md"]
    r=subprocess.run(cmd,cwd=args.context,capture_output=True,text=True)
    assert r.returncode in [0,1],r.stderr
    ledger.append({"note_id":m.group(1),"title":m.group(2),"terms":terms,
        "context_files":["README.md","notes/RESULTS_STATE.md"],
        "command":cmd,"returncode":r.returncode,"matching_lines":r.stdout.splitlines(),
        "comparison":block[search.start():].split("\n\n")[0]})
ids=[r["note_id"] for r in ledger]
assert len(ids)==len(set(ids)),"Duplicate note IDs"
data={"created_utc":datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
      "scope":"Exact literal, case-insensitive searches of the two supplied context files, after transcription freeze. Matches are leads, not verification of upstream files.",
      "notes":ledger}
(root/"records"/"research_context_searches.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"notes":len(ids),"sections":sorted(set(x[0] for x in ids)),"missing_parts":missing,"words":len(text.split()),"path":str(out)},ensure_ascii=False))
