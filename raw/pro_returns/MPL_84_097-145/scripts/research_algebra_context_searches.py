#!/usr/bin/env python3
"""Executed per-item context searches for algebra research notes, never OCR."""
from pathlib import Path
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "MPL_84_097-145/research"
C84 = "context/same_cote_84/MPL_84_146-193_notes.md"
RS = "context/notes/RESULTS_STATE.md"
FILES = ["context/README.md", "context/LM2_CONGRUENCE_ROWS.md", C84, RS]
QUERIES = {
"A01": [r"Attention au signe|signe.*(dualit|isom)|dualit.*signe", r"dualit|déterminant|L174\.2"],
"A02": [r"Q_N|\\delta_N|\\varphi_N", r"forme quadratique|rang.?deux|L182\.3"],
"A03": [r"transpos|inc.*2|xi.*bar", r"L172\.5|factori[sz]|withdraw|retir"],
"A04": [r"transpos|sans.*quadrati", r"E160\.2|L174\.2|coh[ée]rence"],
"A05": [r"trace réduite|pushout|somme amalgam", r"L180\.1|exact|E170\.1"],
"A06": [r"univers.*inject|invariant|étale", r"L172\.[345]|L192\.1"],
"A07": [r"remont|relative norm|norme relative", r"L172\.[45]|L190\.2"],
"A08": [r"surject|inject|kernel", r"L172\.4|L192\.1|R06"],
"A09": [r"b_1b_2|b₁b₂|4c_1c_2|4c₁c₂", r"84-product-quadratic-algebras-formula|L172\.1|R05"],
"A10": [r"qi=2|iq=|projector|idempotent", r"L172\.5|trace"],
"A11": [r"quadratic.*unique|application quadratique unique|relative norm", r"L172\.5|L190\.2"],
"A12": [r"relative norm|mixed coefficients|polarization|polarisation", r"L172\.5|L190\.2|rank-four"],
"A13": [r"transitiv|four conjugates|quatre conjugu", r"L172\.4|L172\.5"],
"A14": [r"quasi.?quadrati|ni même plat", r"noninject|non-inject|L172\.4"],
"A15": [r"norm.*invar|n.*bar.*n|invariance", r"multiplicativ|E148\.4"],
"A16": [r"multiplication.*(form|trace)|facteur.*2", r"E148\.4|division|L172\.5"],
"A17": [r"polarization|polarisation|varphi_n", r"injectiv|E148\.4|L172\.4"],
"A18": [r"facultati|2n.*forme|tower", r"norm|L190\.2"],
"A19": [r"quasi.?quadrati", r"multiplicativ|five.axiom|E148\.4"],
"A20": [r"quasi.?quadrati|five.axiom|Z/4|mathbb Z/4", r"multiplicativ|E148\.4"],
"A21": [r"biquadrati|trois.*alg|three.*algebra", r"quasi.?quadrati|L172\.4"],
"A22": [r"sigma_1.*sigma_2.*sigma_3|three.*involution", r"biquadrati|compatibilit"],
"A23": [r"6 diagrammes|six.*(square|diagram)|noyau", r"base change|chgt|E170\.1"],
"A24": [r"Il reste à vérifier|bilin|polar", r"relative norm|L190\.2"],
"A25": [r"t_1\(x_1\)|n_1\(x_1\)|chgt.*base", r"trace.*norm|norm.*trace|L190\.2"],
"A26": [r"common.*trace|trace.*commune|t_1.*T_1", r"injectiv|L172\.4"],
"A27": [r"quatre.*conjugu|four.*conjugate|n_1.*N_1", r"injectiv|multiplicativ|E148\.4"],
"A28": [r"even.*parity|parité|F_2\^3|three.*involution", r"GT|LM2|R09"],
"A29": [r"deux au moins|three.factor|triple|non.étale", r"L172\.3|L192\.1|car.*2"],
"A30": [r"three.factor|triple|even.*parity|invariant", r"L172\.[12345]|L192\.1"],
"A31": [r"constant.*section|j'ai envie de prouver|fixed.ring|invariant", r"L192\.1"],
"A32": [r"dual.number|e\+f|fixed.ring|invariant", r"L192\.1|R06"],
"A33": [r"frac.14|1/4|4a|common.*trace", r"L172\.5|projector"],
"A34": [r"twist|parity|transitive|transitif", r"étale|E170\.1"],
"A35": [r"X_J|sous.schéma|subscheme|transiti", r"kernel|noyau"],
"A36": [r"sous.schéma|closed.*subscheme|D\(2\)|transiti", r"closed immersion|immersion ferm"],
"A37": [r"sans condition étale|biquadrati|pi.*varepsilon", r"L192\.1|R06"],
"A38": [r"plat|flat|surject|univers.*inject", r"L172\.4|L192\.1|E170\.1"],
"A39": [r"dual.number|triple|nonflat|non.flat", r"L192\.1|R06"],
"A40": [r"B_0|B_1|quasi.?quadrati|relative norm", r"L172\.5|L190\.2"],
}

notes = (OUT / "algebra_notes.md").read_text()
blocks = re.split(r"(?=^### A\d\d —)", notes, flags=re.M)
metadata = {}
for block in blocks:
    m = re.match(r"### (A\d\d) — (.+)", block)
    if not m:
        continue
    context_line = next((line for line in block.splitlines() if line.startswith("**Context:**")), "")
    metadata[m.group(1)] = {"title": m.group(2), "comparison": context_line}
assert set(QUERIES) == set(metadata) == {f"A{i:02}" for i in range(1,41)}

record = {
    "scope": "All forty note IDs searched separately in all four supplied context files; no scans or images inspected.",
    "prerequisite_reading": ["context/README.md", RS],
    "interpretation": "Matches are search evidence, not promotion of earlier leads to reviewed results. Negative exact-topic queries do not assert absence from all literature.",
    "items": [],
}
tick = chr(96)
md = [
    "# Executed context searches for algebra notes A01–A40", "",
    "The full supplied context/README.md and context/notes/RESULTS_STATE.md were read before these research notes were drafted. Each of the forty proposed items was searched separately against all four supplied context files: the README, LM2 congruence rows, same-cote notes, and results register. The final two-file search record was expanded to all four by the root reviewer before packaging.", "",
    "Commands used rg -n -i -e PATTERN -- FILE from the workspace root. Every match is retained in algebra_context_searches.json; this readable record shows the first eight matching lines for each query/file, gives the complete count, and explicitly records negative searches. Long displayed match lines are shortened to 900 characters, with the unabridged text preserved in the JSON.", "",
    "A hit identifies a comparison to inspect; it is not evidence that the hit proves the proposed note. In particular the earlier same-cote notes remain first-pass leads, the two Hua entries remain claims being checked, and broad words such as 'norm' or 'GT' do not establish an LM connection. Context paragraphs cited in algebra_notes.md were read, rather than inferred from the search snippets.", "",
]
for item_id, queries in QUERIES.items():
    entry = {"id": item_id, **metadata[item_id], "queries": []}
    md += [f"## {item_id} — {metadata[item_id]['title']}", "", metadata[item_id]["comparison"], ""]
    for pattern in queries:
        query_record = {"pattern": pattern, "files": []}
        md += [f"**Executed query:** {tick}{pattern}{tick}", ""]
        for file in FILES:
            proc = subprocess.run(["rg", "-n", "-i", "-e", pattern, "--", file],
                                  cwd=ROOT, text=True, capture_output=True)
            if proc.returncode not in (0, 1):
                raise RuntimeError((item_id, pattern, file, proc.stderr))
            matches = []
            for line in proc.stdout.splitlines():
                number, text = line.split(":", 1)
                matches.append({"line": int(number), "text": text})
            query_record["files"].append({
                "file": file, "exit_code": proc.returncode,
                "match_count": len(matches), "matches": matches,
            })
            if not matches:
                md += [f"- {tick}{file}{tick}: **negative** (no matching line).", ""]
            else:
                md += [f"- {tick}{file}{tick}: **{len(matches)} matching lines**; shown below"
                       + (" (first eight; all in JSON)." if len(matches)>8 else "."), "",
                       tick*3 + "text"]
                for match in matches[:8]:
                    text = match["text"]
                    if len(text) > 900:
                        text = text[:900] + " … [full line in JSON]"
                    md.append(f"{file}:{match['line']}: {text}")
                md += [tick*3, ""]
        entry["queries"].append(query_record)
    record["items"].append(entry)

(OUT / "algebra_context_searches.json").write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
(OUT / "algebra_context_searches.md").write_text("\n".join(md) + "\n")
print(json.dumps({
    "items": len(record["items"]),
    "queries": sum(len(x["queries"]) for x in record["items"]),
    "file_searches": sum(len(q["files"]) for x in record["items"] for q in x["queries"]),
    "negative_file_searches": sum(not f["matches"] for x in record["items"] for q in x["queries"] for f in q["files"]),
    "markdown_bytes": (OUT / "algebra_context_searches.md").stat().st_size,
    "json_bytes": (OUT / "algebra_context_searches.json").stat().st_size,
}, indent=2))

