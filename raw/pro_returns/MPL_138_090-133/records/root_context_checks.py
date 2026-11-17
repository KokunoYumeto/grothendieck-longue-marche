#!/usr/bin/env python3
"""Reproducible item-specific text searches; no images and no source edits."""
from pathlib import Path
import json,re,subprocess
from datetime import datetime,timezone

ROOT=Path(__file__).resolve().parents[1]
CTX=ROOT.parent/"context"
queries={
 "BC01":["cartographique","admissibles"], "BC02":["algèbre finie","clôture","Bielyi"],
 "BC03":["opère sur la catégorie","coefficients","Galois"],
 "BC04":["commut","épingl"], "BC05":["ne peut pas être triviale","conjugaison","fidélité"],
 "BC06":["obtiendrait-on toutes","Bielyi","résultat du russe"],
 "BC07":["1976","1977","Helsinki"], "BC08":["fidèle","regular","réguli"],
 "BC09":["nombre fini","orbites","cyclotomique"], "BC10":["cas concrets","degré 6"],
 "BC11":["polyèdre","bi-icos","X(n)","congruence"],
 "BC12":["compatibilité","générisation","sections"], "BC13":["conjugaison","torsion"],
 "BC14":["Kummer","CM","E.3"],
 "OP01":["axiomatique provisoire"], "OP02":["préfaisceau","rigidification"],
 "OP03":["Aut","isotopes"], "OP04":["groupe fini","équivari"],
 "OP05":["varinjlim","sections"], "OP06":["sous-groupes distingués","libres d'indice fini"],
 "OP07":["parties","sphère de référence"], "OP08":["théorie non orientée","conjugaison"],
 "OP09":["1-complexe","sous-1"], "OP10":["connexe","disques","au plus un"],
 "OP11":["A contient au plus","centres des faces"], "OP12":["disques","ramifié"],
 "OP13":["milieux","application","sphère"], "OP14":["varphi f","ramification"],
 "OP15":["cas exceptionnel","bout"], "OP16":["milieu d'arête","étale en"],
 "OP17":["infty","ramification"], "OP18":["involutives","cz + 1"],
 "OP19":["2f","replie"], "OP20":["clean","ramification"],
 "OP21":["stabilisateurs","noyau"], "OP22":["disque fermé","ordre fini"],
 "OP23":["rigidification","évident"], "OP24":["contractile"],
 "OP25":["infini","isotop"], "OP26":["unique","c'est faux"],
 "OP27":["chaque cellule","isotope"], "OP28":["homothétie","Aff"],
 "OP29":["III)","Aff"], "OP30":["au moins trois","représentation conforme"],
 "OP31":["représentation conforme","finies"], "OP32":["orange","face"],
 "OP33":["méridien","orange"], "OP34":["méridien","ramification"],
 "OP35":["seuls","orange"], "OP36":["cartes infinies"],
 "OP37":["centres des faces","milieux"], "OP38":["conditions","compatibl"],
 "OP39":["groupes d'automorphismes"], "OP40":["fixant","fixe","spéciale"],
 "OP41":["ramification","étale"], "OP42":["belyi-extending","Wood"],
 "OP43":["Galois","opération"], "OP44":["degré 6","opérations"],
 "OP45":["orbites","invariant"], "OP46":["conjugaison","opérations"],
 "SR03":["classes","épingl"], "SR04":["degré 6","permutations"],
 "SR05":["6N","ordre du groupe"], "SR06":["inertie","quotient","lacets"],
 "SR07":["complexité","degrés"], "SR08":["rigide","degré 6"],
 "SR09":["symétries","automorphismes"], "SR10":["degré 1","bas degrés"],
 "SR11":["catalogue","énumération"], "SR12":["classification","revêtements finis"],
}
notes=ROOT/"records/root_research.md"
supp=ROOT/"records/root_research_supplement.md"
alltext=notes.read_text()+"\n"+supp.read_text()
ids=re.findall(r"^### ((?:BC|OP|SR)\d\d) —",alltext,re.M)
assert set(ids)==set(queries), (set(ids)-set(queries),set(queries)-set(ids))
results=[]
for ident in ids:
    args=["rg","-n","-i","-F","--no-heading"]
    for q in queries[ident]:
        args+=["-e",q]
    args += [str(CTX)]
    r=subprocess.run(args,text=True,capture_output=True)
    assert r.returncode in (0,1),r.stderr
    lines=r.stdout.splitlines()
    results.append({"note_id":ident,"queries":queries[ident],"hit_count":len(lines),
                    "files":sorted({x.split(":",1)[0].replace(str(CTX)+"/","") for x in lines}),
                    "sample_hits":[x.replace(str(CTX)+"/","") for x in lines[:24]],
                    "sample_is_truncated":len(lines)>24})
source_patterns=["Belyi","Bielyi","Белый","fidélité","fidèle","polyèdr","icosa",
                 "X(n)","toute courbe","toutes les courbes","corps de nombres"]
source_results=[]
for q in source_patterns:
    r=subprocess.run(["rg","-n","-i","-F",q,str(ROOT/"pages")],text=True,capture_output=True)
    assert r.returncode in (0,1)
    source_results.append({"query":q,"hits":r.stdout.splitlines()})
now=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
out={"date":now,"scope":"Text/context comparisons after freeze, not image reading or theorem verification.",
     "notes":results,"b6_negative_search_support":source_results,
     "absence_limit":"Negative strings supplement the root's full reading; they alone cannot prove semantic absence."}
(ROOT/"records/root_context_search.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"searched_note_ids":len(ids),"no_hits":[x["note_id"] for x in results if not x["hit_count"]],"date":now}))
