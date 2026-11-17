from pathlib import Path
import subprocess, json, csv, datetime
root=Path("work/context")
out=Path("work/MPL_91_019-058/research")
queries={
"B01":r"Serre.?Lang|Greenberg|NPLAN-01|S19|reporter.*fin|Deux plans",
"B02":r"Picard|projectif sur|objets plats|fondamentaux|NPLAN-01|MPL_131 RN001|Deux plans",
"B03":r"relative.product|produit.fibr|restriction.of.scalars|restriction de Weil|N91-21|NCTX-07|97.11|Hom.*T",
"B04":r"effectiv|descente|descent|égalisateur|equalizer|immersivit|immersité|N91-13|RN101-01",
"B05":r"Nagata|Hironaka|diagonal|non.effective|non effective|contre.exemple|91-res-representable",
"B06":r"orbite|trajectoire|affine.*ouvert|ouvert.*affine|Nagata|détailler|N91-13",
"B07":r"algebraic.space|espace.algébri|scheme.*represent|représentable|NCTX-06|91-res-representable",
"B08":r"Fibrés vectoriels|fibre.*vector|check|sections|corepresent|N91-17|dual|dualisation",
"B09":r"envelope|enveloppe|plus petit|plus grand|intersection|intersections|compl[eè]t|N90-09|N070",
"B10":r"intersection|intersections|quasi.coh|cohérent|par intersections|N070",
"B11":r"intersection|intersections|sheaf|faisceau|cohérent|local et complet|N070",
"B12":r"intersection|intersections|cofinal|Chevalley|Krull|adic|adique|compl[eè]t|N91-17|N070",
"B13":r"Proposition 2|2 bis|extension finie|type fini|finitude|Recollement|91-res-representable",
"B14":r"universal|universalit|recolle|gluing|injection|factoris|plus grand|91-res-representable",
"B15":r"voisinage|neighbourhood|neighborhood|fini.*ferm|finite.*closed|factoris|Recollement",
"B16":r"radiciel|géométr.*injectif|geometrically.injective|Corollaire 1|abracadabr|Recollement",
"B17":r"exact.*gauche|left.exact|fermée|closed.immersion|morphismes affines|affine.morphism|91-res-representable",
"B18":r"recouvrement|open.cover|réunion|whole|multisection|91-res-representable",
"B19":r"séparable|separable|Chow|projectif|proper|noeth|N91-09|N070",
"B20":r"surjectif|surjective|Chow|dual.number|nilpotent|séparable|Lissité",
"B21":r"proper|propre|fpqc|fidèlement plat|faithfully.flat|non fini|N070",
"B22":r"norme|norm|determinant|déterminant|det.*f|ample|line.bundle",
"B23":r"très ample|very.ample|immersion projective|fermée|grassmann|N070",
"B24":r"dual.number|tangent|projectif|proper|propre|inséparable|séparable",
"B25":r"grassmann|quotient|localement fermé|locally.closed|loc.*libre|fermé",
"B26":r"varphi.*lambda|équations|equations|stabilité|stabilit|NCTX-04|grassmann",
"B27":r"d[eé]terminant|inversib|unit|loc.*libre|base.change|changement de base|RN142-03",
"B28":r"X.*nu|noeth|finitude|finite.type|type fini|rédiger|Recollement|N070",
"B29":r"noeth|finite.cover|nombre fini|partie finie|rank|rang|Recollement|N070",
"B30":r"Spec|Sym|fibré vectoriel|affine|finitude|finite.type|N070",
"B31":r"dimension|dim.|radiciel|automorphis|dual.number|contre.exemple|Lissité",
"B32":r"automorphis|endomorphis|nilpotent|dual.number|RN142-04|tronc|truncat",
"B33":r"NCTX-04|RN142-03|minor|mineur|d[eé]terminant|91-hom-unramified",
"B34":r"A.185|Weil.restriction|restriction.de.Weil|isogen|Prym|séparable|separable",
"B35":r"RN138-01|RN140-01|RN142-01|RN142-04|jet|filtration|Greenberg|différentielle|coordonnées",
}
files=sorted(p for p in root.rglob("*") if p.is_file())
assert len(files)==6, [str(p) for p in files]
timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
(out/"search_plan_034-049.json").write_text(json.dumps({"time_utc":timestamp,"scope":[str(p) for p in files],"queries":queries},ensure_ascii=False,indent=2)+"\n")
rows=[]; blocks=["# Per-item context searches — B01–B35\n",f"Run UTC: {timestamp}\n","Every regular expression below was run case-insensitively with rg against each of all six supplied context files. Exit 1 is a recorded negative match; errors are not treated as negative matches. The notes cite substantive inspected passages, not every incidental word hit.\n"]
for ident,pattern in queries.items():
    blocks += [f"\n## {ident}\n",f"Pattern: {pattern}\n"]
    for path in files:
        result=subprocess.run(["rg","-n","-i","--",pattern,str(path)],text=True,capture_output=True)
        if result.returncode not in (0,1):
            raise RuntimeError((ident,str(path),result.stderr))
        lines=result.stdout.splitlines()
        rows.append({"note_id":ident,"pattern":pattern,"context_file":str(path.relative_to(root)),"matching_lines":len(lines),"rg_exit":result.returncode,"utc":timestamp})
        blocks += [f"\n### {path.relative_to(root)} — {len(lines)} matching lines\n"]
        blocks += ["\n".join("    "+line for line in lines)+"\n" if lines else "    (no matching line)\n"]
with (out/"context_searches_034-049.tsv").open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter="\t")
    w.writeheader();w.writerows(rows)
(out/"context_searches_034-049.md").write_text("".join(blocks))
print(json.dumps({"notes":len(queries),"files_per_note":len(files),"searches":len(rows),"matching_lines":sum(r["matching_lines"] for r in rows),"notes_bytes":(out/"notes_034-049.md").stat().st_size,"log_bytes":(out/"context_searches_034-049.md").stat().st_size}))
