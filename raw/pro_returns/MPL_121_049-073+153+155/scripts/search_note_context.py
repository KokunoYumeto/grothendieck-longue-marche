"""Reproducible post-freeze context searches, one record per numbered note/source."""
from pathlib import Path
import hashlib
import json
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
CONTEXT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / "context"
SOURCES = [
    "MPL_147_138-190_transcription.tex",
    "MPL_149_091-136_transcription.tex",
    "MPL_147_138-190_notes.md",
    "MPL_149_091-136_notes.md",
    "STATEMENTS_WITH_STATUS.md",
    "notes/RESULTS_STATE.md",
]

def norm(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s.lower())
                   if not unicodedata.combining(c))

TERMS = {
 "H01": ["tubulure", r"\bombres?\b", "germe", "local"],
 "H02": ["voisinage", "tubul", "immersion", "sauf erreur"],
 "H03": ["ponct", "image inverse", "normal", "groupo"],
 "H04": [r"\bombres?\b", "tubulure", "localis", "complet"],
 "H05": [r"\bombres?\b", "etale convenable", "complet", "ponct"],
 "H06": [r"pi_2", "bord", "T^J", "obstruction"],
 "H07": ["remords", r"S\^2", "fleche", "cohom"],
 "H08": ["gerbe", "cohom", "reconstit", "P1d1"],
 "H09": ["verific", "reconst", "groupo", "P1a1"],
 "H10": ["1981", "decembre", "janvier", "151"],
 "H11": ["exit", "groupo", "cohom", "construct"],
 "H12": ["amalg", "homotop", "P1d1", "sphere"],
 "R121-01": ["partition", "adapte", "stratification", "§13.4"],
 "R121-02": ["ouvert", "interieur", "feuille", "partition"],
 "R121-03": ["ordre", "fermeture", "feuille", "G.10"],
 "R121-04": ["filtration", "codim", "fermeture"],
 "R121-05": ["connexe", "restriction", "partition", "localement fin"],
 "R121-06": ["feuilles ferme", "localement fin", "fermeture", "intersection"],
 "R121-07": ["feuille", "fermeture", "adherence", "Phi"],
 "R121-08": ["incidence", "maquette", "remords", "P4e"],
 "R121-09": ["conservatif", "fidele", "exact", "D.12"],
 "R121-10": ["epim", "effectif", "graphe", "amalg"],
 "R121-11": ["ind-objet", "suite", "denombrable", "transportable", "E.17"],
 "R121-12": ["propre", "pseudo", "image", "D.6", "D.12"],
 "R121-13": ["modere", "ration", "constante", "corps"],
 "R121-14": ["modere", "corps", "vectoriel", "multiplication"],
 "R121-15": ["plong", "puissance", "compact", "B15"],
 "R121-16": ["compos", "graphe", "fibre", "projection"],
 "R121-17": ["Ker", "egal", "diagonal", "fibre"],
 "R121-18": ["effectif", "union", "coher", "D.12"],
 "R121-19": ["codiagon", "epim", "amalg", "C.3"],
 "R121-20": ["universel", "chgt", "changement de base", "amalg", "C.8"],
 "R121-21": ["injectif", "retract", "amalg", "extension"],
 "R121-22": ["fonction", "composition", "projection", "foncteur"],
 "R121-23": ["graphe", "fonction", "image", "independ"],
 "R121-24": ["point", "dimension", "notation", "§1.8"],
 "R121-25": ["triangul", "simplic", "fini", "Q4b"],
 "R121-26": ["triangul", "induit", "prolong", "isotop"],
 "R121-27": ["Chern", "Grass", "normal", "fibre", "F.43"],
 "R121-28": ["noyau", "fibre", "quotient", "amalg"],
 "R121-29": ["quotient", "produit", "amalg", "zero"],
 "R121-30": ["extension", "amalg", "quotient", "image"],
 "R121-31": ["fibre", "injectif", "zero", "noyau"],
 "R121-32": ["projection", "intersection", "produit", "modere"],
 "R121-33": ["bijectif", "isom", "graphe", "homeom"],
 "R121-34": ["fonction", "modele", "plong", "local"],
 "R121-35": ["recouvr", "compact", "local", "B15"],
 "R121-36": ["graphe", "compact", "continu", "separe"],
 "R121-37": ["faisceau", "local", "reunion", "D.12"],
 "R121-38": ["amalg", "reunion", "fini", "C.8"],
 "R121-39": ["prolong", "amalg", "clair", "D.12"],
 "R121-40": ["analyseur", "rigid", "modere", "foncteur"],
 "R121-41": ["intersection", "projection", "produit", "Q4b"],
 "TC01": ["o-min", "modere", "structure", "B15"],
 "TC02": ["coher", "effectif", "fini", "D.12"],
 "TC03": ["conservatif", "fidele", "graphe", "E.17"],
 "TC04": ["fonction", "graphe", "projection", "§13.2"],
 "TC05": ["intersection", "inverse", "modere", "B15"],
 "TC06": ["compact", "Cantor", "modere", "D.12"],
 "TC07": ["extension", "zero", "injectif", "D.12"],
 "TC08": ["triangul", "fini", "maquette", "ZD8"],
 "TC09": ["corps", "ordre", "parametre", "ration"],
 "TC10": ["compact", "propre", "local", "E.17"],
 "TC11": ["modere", "axiome", "prolong", "§13.2"],
 "TC12": ["complement", "connexe", "fini", "partition"],
 "TC13": ["analyt", "faisceau", "local", "B15"],
 "TC14": ["Nash", "o-min", "Shiota", "geometri"],
 "TC15": ["Shiota", "Hauptvermutung", "triangul", "Q4b"],
 "TC16": ["Shiota", "isotop", "triangul", "Q4b"],
 "TC17": ["Shiota", "Yokoi", "isotop", "Q4b"],
 "TC18": ["comparaison", "isotop", "homotop", "Q4b"],
 "TC19": ["comparaison", "homotop", "parametre", "B15"],
 "TC20": ["D.12", "E.17", "P1b1", "ZD8", "modere"],
 "A01": ["analyseur", "composition", "anneau"],
 "A02": ["analyseur", "composition", "somme", "produit"],
 "A03": ["analyseur", "Witt", "endomorph", "W_k"],
 "A04": ["binomial", "polyn", "factoriel"],
 "A05": ["binomial", "presentation", "polyn", "entier"],
 "A06": ["binomial", "difference", "polyn"],
 "A07": ["anneau", "fraction", "inclusion"],
 "A08": ["composition", "polyn", "analyseur"],
 "A09": ["coaddition", "coproduit", "tenseur", "tensor"],
 "A10": ["comultiplication", "coproduit", "substitution"],
 "A11": ["module libre", "polyn", "tensor"],
 "A12": ["unicite", "tensor", "plethor", "polyn"],
 "A13": ["analyseur", "plethor", "biring", "facultatif"],
 "A14": ["substitution", "decomposition", "analyseur"],
 "A15": ["constante", "zero", "analyseur"],
 "A16": ["constante", "augmentation", "analyseur"],
 "A17": ["unitaire", "constante", "pseudo-anneau"],
 "A18": ["App", "fonction", "analyseur"],
 "A19": ["topos", "constante", "section globale"],
 "A20": ["polyn", "endomorph", "W_k"],
 "A21": ["serie formelle", "nilpot", "composition"],
 "A22": ["constante", "fidele", "polyn"],
 "A23": ["binomial", "lambda", "plethor"],
 "A24": ["puissances div", "polyn", "Roby"],
 "A25": ["1982", "82.109", "Analyseur", "pages"],
 "A26": ["module libre", "extension", "tensor", "polyn"],
 "T01": ["foncteur fibre", "tensor", "reconstruction"],
 "T02": ["pro-objet", "dual", "complet"],
 "T03": ["corps", "extension", "End", "central"],
 "T04": ["ideal", "normalisat", "quotient", "tensor"],
 "T05": ["descente", "groupo", "foncteur fibre"],
 "T06": ["End", "Morita", "extension finie"],
 "T07": ["coproduit", "multiplicatif", "bialgeb"],
 "T08": ["rigid", "fidele", "exact", "diagonal"],
 "T09": ["foncteur fibre", "tensor", "diagonal", "Tannak"],
 "T10": ["Tannak", "Deligne", "rigid", "intrinseque"],
 "T11": ["etale", "fidele", "descente"],
 "T12": ["insepar", "extension finie", "exact"],
 "T13": ["dualite", "exact", "contravar"],
 "T14": ["pro-objet", "module", "regulier"],
 "T15": ["module", "commut", "dualite"],
 "T16": ["dualite", "trace", "lineaire", "fini"],
 "T17": ["rigid", "evaluation", "antipode"],
 "T18": ["Hom", "tensor", "evaluation"],
 "T19": ["gauche", "droite", "module"],
 "T20": ["foncteur fibre", "neutral", "extension"],
 "T21": ["rigid", "evaluation", "regular", "regulier"],
 "T22": ["bialgeb", "tensor", "extension"],
 "T23": ["bialgeb", "Hopf", "tensor", "rigid"],
 "T24": ["1984", "juillet", "octobre", "juin"],
 "T25": ["preference", "contrat", "publ", "pages"],
}

notes = (ROOT / "MPL_121_049-073+153+155_notes.md").read_text()
ids = re.findall(r"^### ((?:R121-|H|TC|A|T)\d+) —", notes, re.M)
assert set(ids) == set(TERMS), (set(ids)-set(TERMS), set(TERMS)-set(ids))

loaded = {}
for source in SOURCES:
    data = (CONTEXT / source).read_bytes()
    lines = data.decode("utf-8").splitlines()
    scans = []
    scan = None
    for line in lines:
        m = re.search(r"\\scanpage\{(\d+)\}", line)
        if m:
            scan = int(m[1])
        scans.append(scan)
    loaded[source] = (lines, scans, hashlib.sha256(data).hexdigest())

out = ROOT / "research/context_search_log.jsonl"
with out.open("w") as f:
    for note in ids:
        terms = TERMS[note]
        patterns = [(t, re.compile(norm(t), re.I)) for t in terms]
        for source, (lines, scans, digest) in loaded.items():
            matches = []
            for i, line in enumerate(lines):
                found = [t for t, p in patterns if p.search(norm(line))]
                if found:
                    matches.append({"line": i+1, "scan": scans[i],
                                    "terms": found, "text": line[:400]})
            # Keep varied examples rather than only the first repeated word.
            examples, seen = [], set()
            for term in terms:
                for m in matches:
                    if term in m["terms"] and m["line"] not in seen:
                        examples.append(m)
                        seen.add(m["line"])
                        break
            record = {
                "note": note, "source": source, "source_sha256": digest,
                "normalization": "case-folded and diacritics removed; regex terms",
                "patterns": terms, "hit_count": len(matches),
                "example_matches": examples,
                "interpretation": "See the numbered note; lexical hits alone do not establish a mathematical parallel.",
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
print(f"{len(ids)} notes searched across {len(SOURCES)} context sources: {len(ids)*len(SOURCES)} records.")
