#!/usr/bin/env python3
"""Reproduce the per-note, text-only context search ledger.

This script reads supplied context text and the completed research notes only.
It never reads images, OCR, frozen pages, or the combined transcription, and
writes only records/context_search_ledger.json. Run from any working directory.

The ID-to-query and ID-to-cited-passage mappings below are hand curated. A hit
means lexical retrieval, not independent corroboration or a new proof. The
original source-status distinctions remain in force.
"""
from __future__ import annotations

import bisect
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess


PACKAGE = Path(__file__).resolve().parents[1]
WORKSPACE = PACKAGE.parent
CONTEXT = WORKSPACE / "context"
NOTES = PACKAGE / "MPL_83_178-222_notes.md"
OUTPUT = PACKAGE / "records/context_search_ledger.json"
HUA = "context/hua_project/83.modern.tex"
ESQUISSE = "context/Esquisse_cote119_copy1_API_transcription.tex"
MAX_HITS_PER_FILE_PER_ITEM = 3
MAX_SNIPPET_CHARS = 135


# ID: (literal, case-insensitive OR terms, cited-passage aliases).
# Terms are split on ||, so TeX backslashes and primes remain literal.
CURATED = {
    "Q01": (r"cartes de congruence||polyhedron of level||quatre variables||28||lambda$-scindées", ["plan", "H.ext", "H.four", "H.variables", "state.open"]),
    "Q02": (r"congruence||bitriangle||icosaèdre||M_{1,1}||X(n)", ["LM2.570-572", "H.groups", "LM2.rows", "plan"]),
    "Q03": (r"icosaèdre||bitriangle||PSL_2||60||douze sommets", ["LM2.571-572", "state.B38"]),
    "Q04": (r"scalaires||carrés||projectif||congruence||C.r3", ["LM3.27-30", "LM2.rows"]),
    "Q05": (r"outer congruence||congruence kernels||multiplier||carrés||GT_0", ["LM3.22-30", "LM2.rows"]),
    "Q06": (r"anneau de base||caractéristique||bases||polyèdres réguliers||quotients plats", ["LM2.573-574", "E.21-25", "H.ext"]),
    "Q07": (r"drapeau||projectif||polyèdres réguliers||épingl||flag", ["E.21-23", "plan"]),
    "Q08": (r"drapeau||réflexion||cartographique||adjacentes||involutions", ["E.20-23", "H.orientation", "H.groups"]),
    "Q09": (r"réduction||dégén||Pic||classes de carrés||C^{*}(e)", ["E.24-26", "H.classes"]),
    "Q10": (r"épingl||réflexions||alpha_1||universel||cosinus", ["E.23", "plan"]),
    "Q11": (r"M_{0,5}||M(0,5)||16 - 3||R097||icosaèdre", ["E.8", "N146.R097", "H.four", "state.five"]),
    "Q12": (r"Petersen||disjoint||two-element||boundary divisors||N066", ["N147.N066-01", "N147.N066-02", "N147.N066-03", "N147.N067-01", "state.five"]),
    "Q13": (r"full symmetric||orientation||five-point||five labels||N068-02", ["N147.N067-02", "N147.N068-02", "N146.R072", "N146.R075", "N146.R076", "state.open"]),
    "Q14": (r"bi-icosaèdre||complémentaires||vecteurs||antipod||240", ["H.orientation", "H.groups"]),
    "Q15": (r"240||PGL||GL}_2||antipod||bi-icosaèdre", ["H.groups", "LM2.571", "state.B39", "state.B41"]),
    "Q16": (r"biicosa||bi-icosa||S_5||binaire||120", ["LM2.S2", "LM2.571", "H.groups", "state.B39", "state.B41"]),
    "Q17": (r"boundary compatibility||forgetting||clutching||compatib||compactification", ["N147.N075", "LM2.402-403", "state.E35", "state.five", "state.O20"]),
    "Q18": (r"centralizer||centralisateur||nonsolvable||K_5||icosahedral", ["state.F7", "state.B38", "state.B39", "state.B40", "state.B41"]),
    "E01": (r"quotients plats||injective à gauche||lambda$-scindées||bigotimes F_i", ["H.ext"]),
    "E02": (r"lambda$-rétraction||scindée||trivialisation||u_i||b_i", ["H.ext"]),
    "E03": (r"accouplement||x_i + \alpha_i||applications multilinéaires||deux conditions", ["H.ext.formula"]),
    "E04": (r"associative et commutative||question de l'unité||beta = 1||compatibilités", ["H.ext.unit"]),
    "E05": (r"E_\beta||beta$ est inversible||trivialisation||surjectif||cisaillement", ["H.ext.unit"]),
    "E06": (r"conditions équivalentes||inversibles||surjectif||Pic||modules inversibles", ["H.ext.unit", "H.classes"]),
    "E07": (r"f^{\circ}||solution universelle||accouplement||bigotimes E_i||produit $*$", ["H.product", "H.ext.formula"]),
    "A01": (r"forme trace||caractéristique $2$||non dégénérée||pairing||trace form", ["H.criterion", "H.orientation3"]),
    "A02": (r"polar form||forme polaire||psi(u,v)||phi(u,v)||Tr u Tr v", ["H.notation", "H.orientation3", "H.gram"]),
    "A03": (r"l'opposée||orientation||multiplication||bigwedge^4||Azumaya", ["H.orientation3", "LM2.245", "LM2.249-250"]),
    "A04": (r"caractéristique $2$||orientation||bigwedge^4||adjug||involution canonique", ["H.orientation3", "H.ring"]),
    "A05": (r"bt + b't'||tau + \tau'||Hamilton||traces classique", ["H.sum"]),
    "A06": (r"tau' - \tau||tau - \tau'||operatorname{Tr}yxz||convention d'orientation", ["H.volume"]),
    "A07": (r"2(\tau - \tau')||coefficient surchargé||varepsilon_0\Delta||page 188", ["H.volume", "H.gram"]),
    "A08": (r"E_{21}||E_{12}||triplet||2$ est inversible||convention d'orientation", ["H.volume", "H.ring"]),
    "A09": (r"fâcheux||seuls échoue||Delta^2||déterminant de Gram", ["H.volume", "H.gram"]),
    "A10": (r"déterminant de Gram||4\tau\tau'||Sigma^2 - \Delta^2||2c''", ["H.gram"]),
    "A11": (r"4cc'c''||terme manquant||omet le terme||Pi = tt't''", ["H.pi", "H.variables"]),
    "A12": (r"À vérifier||base quelconque||pas vérifié||libre de rang||anneau $B$", ["H.ring"]),
    "A13": (r"Sibirskii||Procesi||Formanek||invariants de trois matrices||libre de rang $2$", ["H.ring"]),
    "A14": (r"n'engendre rien||caractéristique $2$||Delta \equiv||anneau de base", ["H.ring"]),
    "A15": (r"Artin||Schreier||tau^2 - \Sigma\tau||caractéristique $2$||étale", ["H.ring"]),
    "A16": (r"transpositions||permutations circulaires||involution canonique||mathfrak{S}_3 \times", ["H.ring", "H.four"]),
    "A17": (r"Sigma - \tau||sous-anneaux fixes||spécialisation||changement de base||caractéristique $2$", ["H.ring", "H.four"]),
    "A18": (r"conjugaison||quotient||invariants||faisceau||conjugacy", ["LM3.255-258", "state.H5"]),
    "A19": (r"underline{\operatorname{Aut}}||mathbb{G}_m||schéma en groupes||group scheme||conjugaison", ["H.ring", "LM3.255-258"]),
    "A20": (r"4cc'c''||singulier||terme manquant||caractéristique $2$", ["H.pi", "H.variables"]),
    "A21": (r"alterné||alternating||transpositions||symétrique||sous-anneaux fixes", ["H.ring", "H.four", "LM4.147"]),
    "A22": (r"Delta = \tau - \tau'||2$ est inversible||n'engendre rien||Sigma^2 -", ["H.ring"]),
    "C01": (r"4 + 4 + 6||16 - 3||il doit||déterminant de Gram||une relation", ["H.four"]),
    "C02": (r"déterminant de Gram||16 - 3||relation cherchée||caractéristique $2$||primitive", ["H.four", "H.gram"]),
    "C03": (r"présume||fini et libre||2^4||quatre variables||orientation", ["H.four"]),
    "C04": (r"t_{ijk}||caractéristique $2$||générat||quatre variables||Tr}(x_1x_2x_3x_4)", ["H.four", "H.ring"]),
    "C05": (r"degré au plus||x_3x_4||Tr}(u^n)||équation du second degré", ["H.four"]),
    "C06": (r"x_3x_4||t_{ij}||t_{34}||invariants de||second degré", ["H.four"]),
    "C07": (r"ordres circulaires||antipodaux||quatre grandes diagonales||sommet orienté||face orientée", ["H.cube", "H.variables"]),
    "C08": (r"direction de||douze quantités||ne retient pas||trois valeurs", ["H.cube", "H.linear", "H.endpoint"]),
    "C09": (r"de produit||racines||anneau de base||dégén||adjacentes", ["H.four", "H.cube", "E.23-25"]),
    "C10": (r"pi_a||sigma_a||X_kX_l||terme manquant||Variables et relations", ["H.variables", "H.pi"]),
    "C11": (r"28||32||Trop lourd||terme manquant||Variables et relations", ["H.variables"]),
    "C12": (r"six dernières||cinq autres||douze||relations linéaires||demi-hexagone", ["H.linear"]),
    "C13": (r"six dernières||relations linéaires indépendantes||demi-hexagone||intégral||indice", ["H.linear"]),
    "C14": (r"octaèdre||cycles impairs||injective||image de rang||adjacence des faces", ["H.linear"]),
    "C15": (r"demi-hexagone||demi-sommes||cycles impairs||parité||image de rang", ["H.linear"]),
    "C16": (r"delta' + \delta''||trois paramètres||demi-sommes||delta'' + \delta", ["H.linear"]),
    "C17": (r"gamma' - c||a' - \beta'||delta''||différences égales", ["H.linear"]),
    "C18": (r"1024||2^{10}||page 210||développer sans conclure", ["H.determinants"]),
    "C19": (r"728||512||M^2 - I||déterminant||27", ["H.determinants"]),
    "C20": (r"1024||512||demi-sommes||application linéaire||arêtes des faces", ["H.linear", "H.determinants"]),
    "C21": (r"lambda = a + a'||mu = b + b'||nu = c + c'||direction de", ["H.endpoint", "H.cube"]),
    "C22": (r"direction de||douze quantités||ne retient pas||sigma_a", ["H.cube", "H.variables"]),
    "X01": (r"Azumaya||GP(1||projective-line||fibrés||gerbe", ["LM2.245", "LM3.258", "LM2.P025R09"]),
    "X02": (r"gerbe||relèvement||Brauer||2-catégorie||Azumaya", ["LM2.245", "LM2.249-250", "LM2.P025R16-19", "LM2.P025I06"]),
    "X03": (r"trace||norme||Macbeath||H5||outer automorphism", ["LM3.257-258", "LM3.267-268", "state.H5"]),
    "X04": (r"Delta||Δ||E.65||E.49||tau - \tau'", ["state.E65", "state.E49", "H.ring"]),
    "X05": (r"boundary compatibility||coherence||clutching||oubli||tour", ["E.8", "N147.N075", "state.E35", "state.E39", "state.O20"]),
    "T01": (r"L 17||L17||L 19||L19||prendre forme et chair", ["H.exclusions", "H.L19"]),
    "T02": (r"yin||yang||intuitions riches||langage précis||versant féminin", ["E.45-46", "H.L19"]),
    "T03": (r"banques de données||énoncés purs et durs||aplatissement||répertoriable", ["H.L19"]),
    "T04": (r"Heidelberg||15.3.1985||Byrne||K.F. Springer||K. F. Springer", ["H.exclusions"]),
    "T05": (r"Grundlehren||Heinze||18 février||dix-huit", ["H.exclusions"]),
    "T06": (r"SGA 1||directeur du Séminaire||Michèle Raynaud||Giraud||Hakim", ["N142.N015.1", "N142.bibliography", "N142.SGA1", "E.45-46"]),
    "T07": (r"pulsion de service||maisons||La clef du yin||Yin le serviteur", ["E.45-46"]),
    "T08": (r"ma propre part||part de responsabilité||réticences||impliqué", ["H.L19"]),
    "T09": (r"Mai 1986||Juillet 1986||verso||Petrich||Juin 1978", ["H.dates", "N146.R074", "LM1.5", "LM1.7"]),
    "R01": (r"rang 4||rank 4||Trois variables||libre de rang $2$", ["H.notation", "H.orientation3", "H.ring"]),
    "R02": (r"det y||det z||underline{c}''||trois variables", ["H.ring"]),
    "R03": (r"voisins de||pi_s||terme manquant||c_s", ["H.variables"]),
    "R04": (r"demi-sommes||b \pm b'||différences égales||beta'", ["H.linear"]),
    "R05": (r"demi-sommes||c \pm c'||beta'||c' - c", ["H.linear"]),
    "R06": (r"trois paramètres||delta''||delta' + \delta''||demi-sommes", ["H.linear"]),
    "R07": (r"4 + 4 + 6||t_{ij}||x_3x_4||t_{34}", ["H.four"]),
    "R08": (r"demi-sommes||La page 220 pose||lambda = a + a'||paramètre par direction", ["H.linear", "H.endpoint"]),
    "P01": (r"Icosaèdres, bi-icosaèdres||pages 1-221||Not transcribed||whole folder", ["plan", "H.header", "H.exclusions"]),
    "P02": (r"I bis||Mai 1986||Juillet 1986||May-July 1986", ["H.dates"]),
    "P03": (r"L 17||L 19||L 22||paginée||I bis", ["H.L19", "H.dates"]),
    "P04": (r"deux pages machine||allemand||K.F. Springer||K. F. Springer||Byrne", ["H.exclusions"]),
    "P05": (r"Récoltes et Semailles||Quatre||Fil d'Ariane||La clef du yin||Giraud||Hakim", ["H.L19", "E.45-46"]),
    "P06": (r"Grundlehren||288||589||dix-huit||SGA 1", ["H.exclusions", "N142.bibliography", "N142.SGA1"]),
}

# Standing questions receive their own execution, even when their subject is
# already discussed in a main note. They are not merely links to another search.
STANDING = {
    "S01": (r"solution universelle||injective à gauche||bigotimes E_i||quotients plats", ["H.ext.formula"]),
    "S02": (r"accouplement||x_i + \alpha_i||applications multilinéaires||deux conditions", ["H.ext.formula"]),
    "S03": (r"associative et commutative||à vérifier||compatibilités", ["H.ext.unit"]),
    "S04": (r"question de l'unité||beta = 1||E_\beta||conditions équivalentes", ["H.ext.unit"]),
    "S05": (r"tau\tau' = \Pi||4cc'c''||polynôme||omet le terme", ["H.sum", "H.pi"]),
    "S06": (r"convention d'orientation||coefficient surchargé||2(\tau - \tau')||varepsilon_0", ["H.volume"]),
    "S07": (r"fâcheux||seuls échoue||Delta^2||déterminant de Gram", ["H.volume", "H.gram"]),
    "S08": (r"trilinéaire||alternée||E_{21}||fixe \varepsilon||triplet", ["H.volume"]),
    "S09": (r"fâcheux||première tentative||seuls échoue||exemple", ["H.volume", "H.gram"]),
    "S10": (r"À vérifier||libre de rang $2$||pas vérifié||tau^2 - \Sigma\tau||base quelconque", ["H.ring"]),
    "S11": (r"4 + 4 + 6||16 - 3||relation cherchée||il doit", ["H.four"]),
    "S12": (r"présume||fini et libre||2^4||anneau $A$ engendré", ["H.four"]),
    "S13": (r"degré au plus $8$||x_3x_4||équation du second degré||degrés $2$ et $3$", ["H.four"]),
    "S14": (r"pi_a||sigma_a||X_kX_l||Variables et relations", ["H.variables"]),
}
CURATED.update(STANDING)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_kind(path: str) -> str:
    if path == HUA:
        return "AI modernized interpretation; unchecked; not a transcription"
    if path == ESQUISSE:
        return "supplied Esquisse transcription; header says not checked by eye"
    if re.search(r"LM_140-[1-4]_text\.tex$", path):
        return "supplied LM transcription; package describes second passes"
    if path.endswith("RESULTS_STATE.md") or path.endswith("LM2_CONGRUENCE_ROWS.md"):
        return "research/status digest; claims retain each row's stated review status"
    if path.endswith("_notes.md"):
        return "prior-run research notes; lead, not an independently inspected manuscript"
    return "context inventory, planning, or project conventions"


def short(text: str, term: str | None = None) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= MAX_SNIPPET_CHARS:
        return text
    pos = text.casefold().find(term.casefold()) if term else 0
    start = max(0, pos - 38) if pos >= 0 else 0
    end = start + MAX_SNIPPET_CHARS - 2
    return ("…" if start else "") + text[start:end] + ("…" if end < len(text) else "")


def main() -> None:
    paths_run = subprocess.run(["rg", "--files", "context"], cwd=WORKSPACE,
                               check=True, capture_output=True, text=True)
    paths = sorted(paths_run.stdout.splitlines())
    assert all(Path(p).suffix in {".md", ".tex", ".txt"} for p in paths), paths
    texts = {p: (WORKSPACE / p).read_text(encoding="utf-8").splitlines() for p in paths}
    scans = {}
    headings = {}
    for path, lines in texts.items():
        scans[path] = []
        headings[path] = []
        for number, line in enumerate(lines, 1):
            match = re.match(r"\\scanpage\{([^}]+)\}", line)
            if match:
                scans[path].append((number, match.group(1)))
            if re.match(r"^#{1,6} ", line) or re.match(r"^\\(?:sub)*section\*?\{", line):
                headings[path].append((number, short(line)))

    def location(path: str, number: int) -> dict:
        answer = {"file": path, "line": number}
        if scans[path]:
            idx = bisect.bisect_right([x[0] for x in scans[path]], number) - 1
            if idx >= 0:
                answer["scan"] = scans[path][idx][1]
        if headings[path]:
            idx = bisect.bisect_right([x[0] for x in headings[path]], number) - 1
            if idx >= 0:
                answer["section"] = headings[path][idx][1]
        return answer

    passages = {}

    def passage(key: str, path: str, first: int, last: int, label: str) -> None:
        assert 1 <= first <= last <= len(texts[path]), (key, first, last)
        passages[key] = {"file": path, "first_line": first, "last_line": last,
                         "source_label": label, "source_kind": source_kind(path)}

    def scan_passage(key: str, volume: str, first: str, last: str | None = None) -> None:
        path = ESQUISSE if volume == "E" else f"context/LM_140-{volume}_text.tex"
        first = str(first)
        last = str(last or first)
        indexes = {scan: i for i, (_, scan) in enumerate(scans[path])}
        a, b = indexes[first], indexes[last]
        first_line = scans[path][a][0]
        last_line = scans[path][b + 1][0] - 1 if b + 1 < len(scans[path]) else len(texts[path])
        passage(key, path, first_line, last_line,
                f"{'Esquisse' if volume == 'E' else 'LM 140-' + volume}, scans {first}–{last}")
        passages[key]["scans"] = [first, last]

    def note_passage(key: str, path: str, prefix: str) -> None:
        found = [n for n, line in enumerate(texts[path], 1) if line.startswith(prefix)]
        assert len(found) == 1, (key, prefix, found)
        first = found[0]
        level = len(prefix) - len(prefix.lstrip("#"))
        last = len(texts[path])
        for n in range(first + 1, len(texts[path]) + 1):
            match = re.match(r"^(#{1,6}) ", texts[path][n-1])
            if match and len(match.group(1)) <= level:
                last = n - 1
                break
        passage(key, path, first, last, texts[path][first-1])

    # Hua's page numbers are his own coordinates; only the matched tail has the
    # known +1 relationship to this package's scan numbers.
    hblocks = {
        "header": (1, 18, "header and interpretation status"),
        "exclusions": (26, 30, "header's explicit exclusions"),
        "notation": (57, 72, "global notation conventions"),
        "orientation": (845, 871, "VI Orientations, pages 52–55"),
        "groups": (872, 911, "VI Les groupes, pages 55–59"),
        "classes": (971, 1010, "VII Les classes C*(e), pages 64–68"),
        "criterion": (1216, 1303, "IX Le critère, pages 92–99"),
        "product": (1624, 1686, "XI Le produit *, pages 149–160 (including 151–152)"),
        "ext": (1718, 1756, "XI Extensions lambda-scindées, pages 171–180"),
        "ext.formula": (1721, 1747, "XI extension and universal-pair formula, pages 171–178"),
        "ext.unit": (1744, 1756, "XI flatness, unit and invertibility summary, pages 175–180"),
        "dates": (1758, 1763, "XII I bis heading and May–July 1986"),
        "orientation3": (1764, 1779, "XII reconstruction and orientation, pages 182–183"),
        "sum": (1774, 1783, "XII symmetric triple-trace formula, page 183"),
        "volume": (1782, 1799, "XII volume calibration, sign and rejected ansatz, pages 184–186"),
        "gram": (1795, 1813, "XII Gram determinant and product, pages 186–188"),
        "pi": (1808, 1818, "XII product polynomial and missing-term footnote, page 188"),
        "ring": (1818, 1834, "XII invariant ring, reversal, characteristic two, pages 189–191"),
        "four": (1836, 1855, "XII four-variable invariants and degree discussion, pages 191–199"),
        "cube": (1856, 1867, "XII cube dictionary and discarded direction-only claim, pages 198–200"),
        "variables": (1876, 1905, "XIII Variables et relations, pages 202–206"),
        "linear": (1907, 1929, "XIII octahedral adjacency and half-sums, pages 202, 208–216"),
        "determinants": (1928, 1941, "XIII determinants, Hua pages 210 and 218"),
        "endpoint": (1942, 1944, "XIII direction sums only, page 220"),
        "L19": (1946, 1964, "XIV final L19, page 221"),
    }
    for key, (a, b, label) in hblocks.items():
        passage("H." + key, HUA, a, b, "Hua " + label)

    passage("plan", "context/README.md", 9, 32, "Archive title and planning bridges B5/B6")
    passage("LM2.rows", "context/LM2_CONGRUENCE_ROWS.md", 1,
            len(texts["context/LM2_CONGRUENCE_ROWS.md"]), "LM2 C.d1, C.r1–C.r3; unreviewed return claims")
    for key, vol, a, b in [
        ("LM2.570-572", "2", "570", "572"), ("LM2.571-572", "2", "571", "572"),
        ("LM2.571", "2", "571", "571"), ("LM2.573-574", "2", "573", "574"),
        ("LM2.245", "2", "245", "245"), ("LM2.249-250", "2", "249", "250"),
        ("LM2.402-403", "2", "402", "403"), ("LM3.22-30", "3", "22", "30"),
        ("LM3.27-30", "3", "27", "30"), ("LM3.255-258", "3", "255", "258"),
        ("LM3.257-258", "3", "257", "258"), ("LM3.258", "3", "258", "258"),
        ("LM3.267-268", "3", "267", "268"), ("LM4.147", "4", "147", "147"),
        ("LM1.5", "1", "5", "5"), ("LM1.7", "1", "7", "7"),
        ("E.8", "E", "119/8", "119/8"), ("E.20-23", "E", "119/20", "119/23"),
        ("E.21-23", "E", "119/21", "119/23"), ("E.21-25", "E", "119/21", "119/25"),
        ("E.23", "E", "119/23", "119/23"), ("E.23-25", "E", "119/23", "119/25"),
        ("E.24-26", "E", "119/24", "119/26"), ("E.45-46", "E", "119/45", "119/46"),
    ]:
        scan_passage(key, vol, a, b)

    for ident in ["R072", "R074", "R075", "R076", "R097"]:
        note_passage("N146." + ident, "context/MPL_146_001-099_notes.md", "### " + ident + " —")
    for ident in ["N066-01", "N066-02", "N066-03", "N067-01", "N067-02", "N068-02"]:
        note_passage("N147." + ident, "context/MPL_147_048-137_notes.md", "### " + ident + " —")
    note_passage("N147.N075", "context/MPL_147_003-047_notes.md", "### N075 —")
    note_passage("N142.N015.1", "context/MPL_142_001-093_notes.md", "### N015.1 —")
    passage("N142.bibliography", "context/MPL_142_001-093_notes.md", 3071, 3077, "Primary bibliography and verification limits")
    passage("N142.SGA1", "context/MPL_142_001-093_notes.md", 3139, 3145, "SGA 1 bibliography; not correspondence evidence")
    passage("LM2.P025R09", "context/LM_140-2_notes.md", 2914, 2919, "LM_P025 R09–R10, scan 245")
    passage("LM2.P025R16-19", "context/LM_140-2_notes.md", 2935, 2946, "LM_P025 R16–R19, scans 249–250")
    passage("LM2.P025I06", "context/LM_140-2_notes.md", 2962, 2963, "LM_P025 I06, scans 245 and 250")
    # Find the actual scan-571 S2 paragraph instead of relying on a generic S2 hit.
    lm2notes = texts["context/LM_140-2_notes.md"]
    s2 = [n for n, line in enumerate(lm2notes, 1) if "S2" in line and "571" in line]
    assert s2, "Could not locate the cited LM2 S2 paragraph"
    passage("LM2.S2", "context/LM_140-2_notes.md", s2[0], min(s2[0] + 7, len(lm2notes)), "Earlier LM2 S2 at scan 571; rejection qualified in Q16")

    statepath = "context/notes/RESULTS_STATE.md"
    passage("state.open", statepath, 14, 27, "Package-facing open items and provisional tests")
    passage("state.five", statepath, 44, 53, "EXIT_TOWER B.12/B.25 and tower claims")
    passage("state.E49", statepath, 94, 97, "EXIT_TOWER E.49; explicitly unrefereed")
    for key, ident in {
        "F7": "LM4 F.7", "B38": "LM4_SUCCESSOR B.38", "B39": "LM4_SUCCESSOR B.39",
        "B40": "LM4_SUCCESSOR B.40", "B41": "LM4_SUCCESSOR B.41",
        "O20": "PUSH_ORDER5_FRAME Itemsfromt 2", "E35": "EXIT_TOWER E.35",
        "E39": "EXIT_TOWER E.39", "E65": "LM7_PUSH E.65", "H5": "WG H5",
    }.items():
        found = [n for n, line in enumerate(texts[statepath], 1) if line.startswith("- **" + ident + "**")]
        assert len(found) == 1, (key, found)
        passage("state." + key, statepath, found[0], found[0], ident + "; retain the row's status")

    # Extract the live note inventory; missing/new IDs fail loudly.
    note_lines = NOTES.read_text(encoding="utf-8").splitlines()
    note_items = {}
    for n, line in enumerate(note_lines, 1):
        m = re.match(r"^### ([QECAXTRP]\d+) — (.+)$", line)
        if m:
            note_items[m.group(1)] = {"id": m.group(1), "kind": "main note", "title": m.group(2), "notes_line": n}
        m = re.match(r"^\| (S\d+) \|", line)
        if m:
            cells = [x.strip() for x in line.strip("|").split("|")]
            note_items[m.group(1)] = {"id": m.group(1), "kind": "standing question", "title": cells[2], "notes_line": n,
                                      "current_scan_locator": cells[1], "context_comparison_from_main_notes": cells[-1]}
    assert set(note_items) == set(CURATED), {"unmapped": sorted(set(note_items) - set(CURATED)), "stale": sorted(set(CURATED) - set(note_items))}
    for ident, item in note_items.items():
        if item["kind"] != "main note":
            continue
        for line in note_lines[item["notes_line"]:item["notes_line"]+4]:
            if "**Context comparison:**" in line:
                item["context_comparison_from_main_notes"] = line.split("**Context comparison:**", 1)[1].split("**Register:**", 1)[0].strip()
                item["register_from_main_notes"] = line.split("**Register:**", 1)[1].split("**Literature:**", 1)[0].split("**Confidence", 1)[0].strip()
                item["current_scan_locator"] = line.split("**Kind:**", 1)[0].replace("**File / scans / location:**", "").replace("**File / scan / location:**", "").strip()
                break

    line_catalog = {}

    def line_reference(path: str, number: int, term: str | None = None) -> str:
        key = f"{path}:{number}"
        if key not in line_catalog:
            line_catalog[key] = {**location(path, number), "snippet": short(texts[path][number-1], term)}
        return key

    def run_search(terms: list[str], only_paths: list[str] | None = None, word: bool = False) -> list[dict]:
        cmd = ["rg", "--json", "--ignore-case", "--fixed-strings"]
        if word:
            cmd.append("--word-regexp")
        for term in terms:
            cmd.extend(["-e", term])
        cmd.extend(["--", *(only_paths or ["context"])])
        result = subprocess.run(cmd, cwd=WORKSPACE, capture_output=True, text=True)
        assert result.returncode in (0, 1), result.stderr
        matches = []
        for raw in result.stdout.splitlines():
            obj = json.loads(raw)
            if obj.get("type") != "match":
                continue
            data = obj["data"]
            textline = data["lines"]["text"].rstrip("\r\n")
            matching = [q for q in terms if q.casefold() in textline.casefold()]
            if word:
                matching = [q for q in matching if re.search(r"(?<!\w)" + re.escape(q) + r"(?!\w)", textline, re.I)]
            matches.append({"file": data["path"]["text"], "line": data["line_number"], "terms": matching})
        return matches

    # These additional searches establish the exact scope of negative findings.
    # A zero result is a statement only about the supplied files/terms searched.
    negative_specs = {
        "T02": (["yin", "yang"], "LM texts and neighbouring-package notes", True),
        "T03": (["banques de données", "énoncés purs et durs", "aplatissement", "répertoriable"], "all context except Hua", False),
        "T04": (["Heidelberg", "15.3.1985", "Byrne", "K.F. Springer", "K. F. Springer"], "all context except Hua", False),
        "T05": (["Grundlehren", "Heinze", "18 février", "dix-huit"], "all context except Hua", False),
        "T07": (["pulsion de service", "maisons", "La clef du yin", "Yin le serviteur"], "LM texts", False),
        "T08": (["ma propre part", "part de responsabilité", "réticences"], "all context except Hua", False),
        "P04": (["deux pages machine", "K.F. Springer", "K. F. Springer", "Byrne"], "all context except Hua", False),
    }

    explanations = {
        "Q02": "The named modular-map identification is conditional and also cites external primary literature; a congruence or icosahedron keyword is not itself this identification.",
        "Q07": "This is an expressly proposed modern strict definition. The Esquisse passages motivate it; the search does not attribute these axioms verbatim to the author.",
        "Q08": "The left/right action distinction is the note's explanation. Retrieved reflection/flag language supplies context, not an exact authorial definition.",
        "Q09": "Base-change limitations are the note's mathematical analysis; Hua's Picard and square-class text is an interpretation of earlier, unavailable images.",
        "Q10": "External Ji discussion is outside this supplied-context ledger. The Esquisse passage supplies the authorial constructional lead only.",
        "Q11": "The earlier cote146 source is available only through prior-run notes; dimensions also use local calculation and external literature.",
        "Q12": "The cote147 boundary assertions are supplied as prior-run notes, not the underlying manuscript; external Keel citation is not searched here.",
        "Q13": "The cited five-point passages are prior-run notes. Keyword hits do not identify the local four-index cube with a five-label object.",
        "Q14": "The complementary-pair description comes from Hua's AI modernized reading of earlier pages. The present independent finite enumeration is outside the supplied context. Its two edge sets partition non-antipodal pairs, not all pairs of distinct vertices.",
        "Q15": "Hua supplies the group-model lead; the present finite verification and external exceptional-isomorphism citation are not context-search results.",
        "Q16": "This compares an earlier notes claim with supplied LM text and Hua. The earlier notes rejection is not accepted as a reviewed result.",
        "Q18": "Status-register matches state open problems; no finite keyword match changes them to proved results.",
        "A01": "The note corrects a Hua claim using its own matrix calculation; a matching characteristic-two passage is not corroboration of Hua's claim.",
        "A03": "Hua's paraphrase is expressly in disagreement with the frozen local reading. LM Azumaya passages concern a different reconstruction problem.",
        "A13": "The field theorem is sourced to external primary literature, not established by Hua's names or by these search hits.",
        "A15": "The Artin–Schreier/derivative distinction is the note's conditional calculation. An étale keyword elsewhere is only a retrieval lead.",
        "A17": "No arbitrary-fiber theorem is being inferred from generic specialization/invariant words; the note supplies a formal-algebra counterexample.",
        "A18": "LM quotient-versus-conjugacy discussion is a direct contextual parallel. The actual orbit-closure example is the current note's calculation.",
        "A21": "LM's alternating/full-symmetric comparison is methodological, not the same invariant-ring calculation.",
        "C03": "Hua preserves the freeness presumption but omits the explicit rank 2^4; the rank being tested comes from frozen local text.",
        "C04": "The generator/word-length theorem is from external primary literature; Hua is a summary lead only.",
        "C06": "Hua suppresses the exact coefficient-ring detail; its grouped-variable text is background, not an independent t34 reading.",
        "C09": "Esquisse ring cautions are an analogy; they do not assert the root-pair counterexample or its sufficient hypotheses.",
        "C10": "Hua supplies the grouped-variable method and omitted product slot. The explicit substitution formula is the current note's calculation.",
        "C13": "The integral lattice-index calculation is current work; Hua's rational linear summary is its context only.",
        "C14": "The note qualifies Hua's unqualified injectivity assertion; retrieval does not validate that assertion over every ring.",
        "C15": "The parity obstruction is a current calculation; Hua contains the linear/half-sum background, not an integral image theorem.",
        "X02": "The primary supplied LM text is present; its earlier research-note commentary is a separate lead, not additional manuscript evidence.",
        "X04": "The same Delta symbol labels different objects. Register E.65 is reported refereed; E.49 remains explicitly unrefereed.",
        "X05": "The comparison is methodological. Neither local associativity words nor a tower keyword prove global sewing/forgetting compatibility.",
        "T01": "Only final L19 has a Hua parallel. The duplicate revision-state evidence is local; other folios were excluded by Hua.",
        "T02": "Esquisse is a thematic language/intuitions comparison, not an independent yin/yang witness. The scoped whole-word search tests the stated lexical absence.",
        "T03": "Hua summarizes only final L19. Other lexical matches, if any, do not constitute an independent version of the revised passage.",
        "T04": "No independent letter text is supplied. The Hua exclusion passage is negative coverage evidence, not corroboration of the Heidelberg letter.",
        "T05": "No independent resignation account is supplied. The specified names/dates are searched; bibliography references would not corroborate this narrative.",
        "T06": "SGA bibliography and Esquisse foundations discussion are separate leads. Neither verifies the correspondence narrative or authorship dispute.",
        "T07": "The Esquisse passage is only a thematic parallel. Exact house/service wording is separately searched in the supplied LM transcripts.",
        "T08": "Hua XIV is a comparison by omission. It does not reproduce the responsibility passage; no independent matching passage is identified.",
        "T09": "Hua supplies the I-bis dates. The Petrich/reused-paper comparison is independently present in supplied LM text and prior-run notes; it does not date the local mathematics from reused typescript dates.",
        "R01": "Context gives a mathematical expectation, not a reading of the local rank glyph. The diplomatic uncertainty is untouched.",
        "R02": "Hua explicitly normalizes det y to det z; this supports a mathematical expectation, not alteration of the frozen transcription.",
        "R03": "Hua's normalized vertex pattern is a mathematical comparison, not independent access to the local subscript ink.",
        "R04": "Hua supplies the half-sum structure but not the exact alpha-prime formula; local frozen algebra supplies the sharper expectation.",
        "R05": "Hua supplies the half-sum structure but not this exact apparent extra-c glyph; the uncertainty remains a local reading issue.",
        "R06": "The three-parameter system supplies notation context only, not a fresh image reading.",
        "R07": "Hua lists six pair invariants and grouped variables; the exact t34 expectation also depends on the local earlier list.",
        "R08": "Hua page216 gives half-sums; its page220 endpoint gives direction sums only. It does not interpret the difference coordinates or final identity.",
        "P01": "The archive description is dossier-level, and Hua headings are editorial; neither is a title-only cover in this supplied scan packet.",
        "P02": "Hua restates the I-bis heading and two month inscriptions; no new image reading is made.",
        "P03": "Hua confirms only final L19 directly; the full folio list and scan/pencil relationship come from the local frozen packet.",
        "P04": "No independent copy or page-count witness for the quoted German letter is supplied. Hua explicitly excludes the corresponding typescript.",
        "P05": "Hua and Esquisse supply partial title/person parallels only. There is no independent title-sheet witness for the complete reused-page list.",
        "P06": "Numeric hits (288/589) are retrieval candidates, not corroboration of series-volume assertions. The SGA bibliography is separate from this numbered list.",
        "S12": "Hua omits the precise rank 2^4 while reporting the freeness presumption; that rank is a local frozen-text claim.",
        "S14": "Hua provides the product relation and method, not the missing expanded edge-product formula.",
    }

    total_rg_calls = 0
    for ident, item in note_items.items():
        raw_terms, refs = CURATED[ident]
        terms = raw_terms.split("||")
        assert all(terms) and all(ref in passages for ref in refs), ident
        matches = run_search(terms)
        total_rg_calls += 1
        by_file = defaultdict(list)
        for hit in matches:
            hit["cited_passage_ids"] = [ref for ref in refs if passages[ref]["file"] == hit["file"]
                                        and passages[ref]["first_line"] <= hit["line"] <= passages[ref]["last_line"]]
            by_file[hit["file"]].append(hit)
        term_counts = {q: Counter(hit["file"] for hit in matches if q in hit["terms"]) for q in terms}
        item["search"] = {
            "mode": "rg --json --ignore-case --fixed-strings, OR across -e terms, scope=context/",
            "queries": [{"term": q, "matching_lines": sum(term_counts[q].values()), "files": dict(sorted(term_counts[q].items()))} for q in terms],
            "total_matching_lines": len(matches),
            "matched_file_count": len(by_file),
            "per_file": [],
        }
        for path, hits in sorted(by_file.items()):
            # Prefer a cited source passage and multiple topic terms, then line order.
            ordered = sorted(hits, key=lambda h: (-bool(h["cited_passage_ids"]), -len(h["terms"]), h["line"]))
            selected = ordered[:MAX_HITS_PER_FILE_PER_ITEM]
            item["search"]["per_file"].append({
                "file": path, "source_kind": source_kind(path), "matching_lines": len(hits),
                "omitted_hit_count": max(0, len(hits) - len(selected)),
                "hits": [{"line_ref": line_reference(path, h["line"], h["terms"][0] if h["terms"] else None),
                          "matched_terms": h["terms"], "cited_passage_ids": h["cited_passage_ids"]} for h in selected],
            })
        item["cited_passages"] = []
        for ref in refs:
            p = passages[ref]
            within = [h for h in by_file.get(p["file"], []) if p["first_line"] <= h["line"] <= p["last_line"]]
            within.sort(key=lambda h: (-len(h["terms"]), h["line"]))
            if within:
                h = within[0]
                line_ref = line_reference(h["file"], h["line"], h["terms"][0] if h["terms"] else None)
                matched_terms = h["terms"]
            else:
                eligible = [n for n in range(p["first_line"], p["last_line"] + 1)
                            if texts[p["file"]][n-1].strip() and not texts[p["file"]][n-1].startswith("\\scanpage")]
                line_ref = line_reference(p["file"], eligible[0])
                matched_terms = []
            item["cited_passages"].append({"passage_id": ref, "sample_line_ref": line_ref,
                                           "matching_lines_in_passage": len(within), "sample_matched_terms": matched_terms,
                                           "use": "passage cited for the comparison stated in the main note; not automatic corroboration"})
        item["evidence_limit"] = explanations.get(ident,
            "The cited Hua passage is the supplied modernized parallel. Other lexical hits are background leads only. Any exact verification, correction, or stronger conclusion in this note comes from the current analysis, not from a generic matching word.")
        if ident.startswith("S") and ident not in explanations:
            item["evidence_limit"] = "Hua is the supplied modernized parallel for this standing question. The question's local wording and its resolved/open/withdrawn status are determined in the completed notes; keyword retrieval alone does not settle it."
        cited_kinds = sorted({passages[r]["source_kind"] for r in refs})
        item["cited_source_kinds"] = cited_kinds
        item["cited_context_only_hua"] = all(passages[r]["file"] == HUA for r in refs)
        item["contains_prior_run_notes_citation"] = any(passages[r]["file"].endswith("_notes.md") for r in refs)
        if ident in negative_specs:
            nterms, scope, word = negative_specs[ident]
            if scope == "LM texts":
                npaths = [p for p in paths if re.search(r"LM_140-[1-4]_text\.tex$", p)]
            elif scope == "LM texts and neighbouring-package notes":
                npaths = [p for p in paths if re.search(r"LM_140-[1-4]_text\.tex$", p) or re.search(r"/MPL_14[2679]_.*_notes\.md$", p)]
            else:
                npaths = [p for p in paths if not p.startswith("context/hua_project/")]
            nhits = run_search(nterms, npaths, word=word)
            total_rg_calls += 1
            item["scoped_absence_check"] = {
                "scope": scope, "files_searched": npaths, "queries": nterms,
                "mode": "case-insensitive fixed strings" + (" with whole-word matching" if word else ""),
                "total_matching_lines": len(nhits),
                "query_matching_lines": {q: sum(q in h["terms"] for h in nhits) for q in nterms},
                "hits": [{"line_ref": line_reference(h["file"], h["line"], h["terms"][0] if h["terms"] else None),
                          "matched_terms": h["terms"]} for h in nhits[:20]],
                "limit": "A negative lexical result is restricted to these exact strings and supplied files; it is not a claim of historical nonexistence.",
            }

    # Store one short source snippet per unique line, rather than repeat passages
    # across all notes. Complete text remains in the supplied context files.
    ledger = {
        "schema_version": 1,
        "purpose": "Per-item audit of actual text-only searches in supplied context; retrieval record, not new research or independent proof",
        "built_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "reproduce": "python MPL_83_178-222/scripts/build_context_search_ledger.py",
        "script": "MPL_83_178-222/scripts/build_context_search_ledger.py",
        "notes_file": str(NOTES.relative_to(WORKSPACE)), "notes_sha256": digest(NOTES),
        "source_scope": "Only context/ text files returned by rg --files. No images, OCR, frozen page TeX, combined transcription, web, or other archives searched.",
        "source_status_rule": "Hua is unchecked AI modernization; Esquisse is not eye-checked; prior-run notes and research returns are claims unless their own row explicitly reports review. Hits do not upgrade their status.",
        "corroboration_rule": "Per-note cited passages are selected from the main notes' existing citations. Search hits elsewhere are lexical leads only. A cited range with no literal hit is recorded as such. Current calculations and external references are outside this ledger.",
        "snippet_policy": {"max_selected_hits_per_file_per_item": MAX_HITS_PER_FILE_PER_ITEM,
                           "max_chars_per_unique_line_snippet": MAX_SNIPPET_CHARS,
                           "selection": "Prefer cited passage, then number of matching topic terms, then earliest line; each cited passage also has one sample locator.",
                           "storage": "Snippets deduplicated in line_catalog; omitted hit counts retain search extent."},
        "rg_version": subprocess.run(["rg", "--version"], check=True, capture_output=True, text=True).stdout.splitlines()[0],
        "counts": {"main_notes": sum(x["kind"] == "main note" for x in note_items.values()),
                   "standing_questions": sum(x["kind"] == "standing question" for x in note_items.values()),
                   "entries": len(note_items), "per_item_searches": len(note_items),
                   "extra_scoped_absence_searches": len(negative_specs), "total_rg_search_calls": total_rg_calls,
                   "context_files": len(paths), "cited_passages": len(passages), "unique_snippet_lines": len(line_catalog)},
        "context_inventory": [{"file": p, "line_count": len(texts[p]), "sha256": digest(WORKSPACE / p), "source_kind": source_kind(p)} for p in paths],
        "passage_catalog": passages,
        "line_catalog": line_catalog,
        "items": list(note_items.values()),
    }
    assert ledger["counts"]["entries"] == 111 and ledger["counts"]["main_notes"] == 97
    assert total_rg_calls == 118
    OUTPUT.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(OUTPUT.relative_to(WORKSPACE)), **ledger["counts"], "bytes": OUTPUT.stat().st_size}, ensure_ascii=False))
    print(json.dumps({"scoped_absence_results": {i["id"]: i["scoped_absence_check"]["query_matching_lines"]
                                                    for i in note_items.values() if "scoped_absence_check" in i}}, ensure_ascii=False))


if __name__ == "__main__":
    main()
