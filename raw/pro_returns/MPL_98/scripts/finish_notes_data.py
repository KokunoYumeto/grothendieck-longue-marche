from pathlib import Path
import datetime
import json
import subprocess

root = Path(__file__).resolve().parents[1]
research = root / "research"
f = research / "note_entries_part3.json"
entries = json.loads(f.read_text())
by = {e["id"].split(".")[-1]: e for e in entries}
by["T02"]["sentences"] = [
    r"The quoted phrase is self-referential, whereas the quotient-subspace criterion requires that every relatively saturated subset \(B\subseteq A\) open in \(A\) have \(f(B)\) open in \(f(A)\), equivalently the trace on \(f(A)\) of an open subset of the quotient.",
    "There is an equivalent formulation with closed subsets; the criterion is an additional requirement, not a property enjoyed by every restriction of a quotient map.",
    r"Taking inverse images proves this equivalence and identifies the natural proposed correction of the second \(f(B)\) to \(f(A)\).",
    "This adds an omitted typescript issue to the context while preserving the literal phrase in the transcription."
]
by["T03"]["sentences"][1] = (
    "For compatible gluing, the overlaps must all be open in both participating pieces, "
    "or all be closed in both pieces; saturation of an open or respectively closed subset "
    "of one piece then proves that the pieces embed."
)
by["T05"]["sentences"][1] = (
    r"In the modern abelian-variety formulation, \(\phi_L:A\to A^\vee\) with finite kernel "
    r"is an isogeny, while \(\phi_L=0\) is equivalent to \([L]\in\operatorname{Pic}^0(A)\); "
    "these are different conditions (Milne, 1986/2022, Propositions 8.1 and 9.2)."
)
by["T06"]["sentences"] = [
    "For a nonzero finite-dimensional space with an injective local-expansion map, imposing successive coefficient-vanishing conditions drops the dimension by at most one and has zero intersection.",
    r"The final nonzero kernel is therefore one-dimensional, and it has a \(K\)-rational generator if the space and coefficient functionals are defined over \(K\).",
    r"The rationality conclusion uses that \(K\)-structure on the ambient space, not merely coefficients in \(K\) in an unrelated chosen basis.",
    "This checks the intended flag mechanism in the omitted typescript; the separate indexing defect is treated in T07."
]
by["T10"]["kind"] = "reading question / possible marginal query"
f.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n")

f = research / "note_entries_part2a.json"
entries = json.loads(f.read_text())
by = {e["id"].split(".")[-1]: e for e in entries}
by["B11"]["kind"] = "self-flagged: requested generalization / own illustrative example"
by["B11"]["confidence"] = (
    "High: the tensor product of the two point modules is computed by the sum "
    "of their annihilator ideals, which depends on their relative embeddings."
)
f.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n")

ident = "MPL98.T13"
plan_path = research / "note_plan.json"
plan = json.loads(plan_path.read_text())
if not any(n["id"] == ident for n in plan):
    ctx = root.parent / "context"
    query = r"recollement|exerc|imprimées|retapées|tapuscrit"
    result = subprocess.run(["rg", "-n", "--no-heading", query, str(ctx)],
                            capture_output=True, text=True)
    if result.returncode not in (0, 1):
        raise RuntimeError(result.stderr)
    matches = []
    for line in result.stdout.splitlines():
        filename, number, _ = line.split(":", 2)
        matches.append({"file": str(Path(filename).relative_to(ctx)),
                        "line": int(number)})
    item = {
        "id": ident, "scans": "010",
        "title": "Compatible overlap homeomorphisms need not embed the pieces",
        "query": query,
        "searched_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "exit_status": result.returncode, "matches": matches,
    }
    plan.append(item)
    with (research / "context_searches.jsonl").open("a") as out:
        out.write(json.dumps(item, ensure_ascii=False) + "\n")
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n")

entry = {
    "id": ident,
    "kind": "unproved exercise / own counterexample",
    "quote": "“n’est pas suffisante … (exerc.)”",
    "context": "Hua98 omits scan 010, printed p. 36; its omission statement is the relevant contextual match.",
    "register": "RS–Ø.",
    "sentences": [
        r"Take \(X_1=\{a,b\}\) discrete, \(X_2=\{a,c\}\) with the upper-set topology of \(a<c\), and \(X_3=\{c,b\}\) with that of \(c<b\), identifying equal labels on the singleton overlaps.",
        r"Every overlap map is a homeomorphism and the compatibility conditions hold, but the quotient has opens \(\varnothing,\{b\},\{b,c\},\{a,b,c\}\).",
        r"The induced topology on \(X_1\) omits the open singleton \(\{a\}\), so its canonical map is not an embedding.",
        "This supplies a checked example for the exercise absent from Hua’s account; it does not weaken the uniform open-overlap or closed-overlap hypotheses of T03."
    ],
    "confidence": "High: all eight subsets of the three-point quotient were checked directly; a research collaborator independently checked the same finite topology."
}
(research / "note_entries_part6.json").write_text(
    json.dumps([entry], ensure_ascii=False, indent=2) + "\n"
)

p = research / "primary_sources.md"
s = p.read_text().replace(
    "The norm memo used the reverse local Rydh a/b labels; use the keys or titles when transferring citations.",
    "The norm memo and final notes use these same suffixes; older event wording has been normalized by title."
)
s = s.replace(
    "Theorem 7.1, corrected-version p. 10; Propositions 9.1–9.2 and following Pic⁰ additivity and multiplication formulas, p. 15",
    "Theorem 7.1 and Remark 7.3; Proposition 8.1; Propositions 9.1–9.2 and following Pic⁰ additivity and multiplication formulas, p. 15"
)
s = s.replace(
    "R reports checking all these passages. B independently reopened",
    "R checked these statements, including Remark 7.3 and Proposition 8.1; N independently checked the relevant isogeny and Picard criteria. B independently reopened"
)
p.write_text(s)
print(f"Prepared {len(plan)} registered notes.")
