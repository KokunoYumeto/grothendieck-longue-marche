#!/usr/bin/env python3
"""Record item-by-item searches in the supplied post-freeze context."""
import json, re, subprocess
from pathlib import Path

base=Path(__file__).resolve().parents[2]
context=base/"context"
out=base/"work"/"research"
out.mkdir(exist_ok=True)
queries={
 "P01":["composition","insertion","arbre","cycle","graphe"],
 "P02":["catégorie","isotop","disque","corde","maquette"],
 "P03":["R_0","S_0","ordre réduit","comp. conn","marqué"],
 "P04":["involution","admissible","contraction"],
 "P05":["involution","non pénétr","nonpénétr","admissible"],
 "P06":["orientation","opposé","circular"],
 "P07":["cyclic","circul","degré","orientation"],
 "P08":["contour","déploi","composante","comp. conn"],
 "P09":[r"\sigma",r"\rho","involution","déploi"],
 "P10":[r"\rho",r"\sigma","rotation"],
 "P11":["rotation","involution","graphe","recollement"],
 "P12":["non pénétr","corde","maquette","arbre"],
 "P13":["quotient","recollement","orientations","groupoïde"],
 "P14":["dual","région","maquette","drapeau"],
 "P15":["orient","opposé"],
 "P16":["arbre","stable","flag","drapeau","modul"],
 "P17":["PREDONTA","CSSBATCH","19 MAY 82","types de mots"],
 "P18":["déploiement","rotation renversée",r"\rho",r"\sigma"],
 "R01":["Remords","S^2","recollement","K(\\pi,1)"],
 "R02":["gerbe","H^2","sphère","sphere"],
 "R03":["gerbe","recollement","cohérent","coherent"],
 "R04":["homotopie","colimit","limite inductive","P1d1"],
 "R05":["décembre","december","1981","151","150"],
 "R06":["catégorie topologique","drapeau","303"],
 "R07":["tubulaire","canonique","Admettant","295"],
 "R08":["pi_2","T^J","inertie","Z^","P1b1"],
}
files=sorted(p for p in context.rglob("*") if p.is_file())
contents={p:p.read_text() for p in files}
def locate_scan(path, lineno):
 s="\n".join(contents[path].splitlines()[:lineno])
 scans=re.findall(r"\\scanpage\{(\d+)\}",s)
 return int(scans[-1]) if scans else None
report={}
for note,terms in queries.items():
 cmd=["rg","--json","-i","-F"]
 for term in terms:cmd+=["-e",term]
 cmd += [str(p) for p in files]
 run=subprocess.run(cmd,text=True,capture_output=True)
 assert run.returncode in (0,1),run.stderr
 matches=[]
 for ln in run.stdout.splitlines():
  item=json.loads(ln)
  if item["type"]!="match":continue
  d=item["data"];p=Path(d["path"]["text"]);n=d["line_number"]
  matches.append({"file":p.relative_to(base).as_posix(),"line":n,
                  "scan":locate_scan(p,n),
                  "excerpt":d["lines"]["text"].strip()[:700]})
 report[note]={"terms":terms,"matches":matches}
 counts={}
 scans={}
 for m in matches:
  counts[m["file"]]=counts.get(m["file"],0)+1
  if m["scan"] is not None:scans.setdefault(m["file"],set()).add(m["scan"])
 print(note,{"matches":len(matches),"transcription_scans":{k:sorted(v) for k,v in scans.items()}})
(out/"context_search_root.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
