from pathlib import Path
import datetime
import json
import subprocess

root = Path(__file__).resolve().parents[1]
r = root / "research"
p = r / "note_plan.json"
plan = json.loads(p.read_text())
for n in plan:
    if n["id"] == "MPL98.T03":
        n["title"] = "The product topology and regrouping"
        n["scans"] = "004,008"
ident = "MPL98.T14"
if not any(n["id"] == ident for n in plan):
    ctx = root.parent / "context"
    query = r"recollement|topologie|page 9|imprimées|tapuscrit"
    result = subprocess.run(["rg", "-n", "--no-heading", query, str(ctx)],
                            capture_output=True, text=True)
    if result.returncode not in (0, 1):
        raise RuntimeError(result.stderr)
    matches = []
    for line in result.stdout.splitlines():
        f, num, _ = line.split(":", 2)
        matches.append({"file": str(Path(f).relative_to(ctx)), "line": int(num)})
    item = {
        "id": ident, "scans": "010",
        "title": "The sufficient gluing hypotheses and the interval quotient",
        "query": query,
        "searched_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "exit_status": result.returncode, "matches": matches,
    }
    plan.append(item)
    with (r / "context_searches.jsonl").open("a") as out:
        out.write(json.dumps(item, ensure_ascii=False) + "\n")
p.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n")

p = r / "note_entries_part3.json"
entries = json.loads(p.read_text())
for n in entries:
    if n["id"] == "MPL98.T03":
        n["quote"] = "“Produit d’espaces topologiques”"
        n["context"] = "Hua98 omits reused scans 004 and 008, printed pp. 39 and 37; its scope statement is the relevant contextual match."
        n["sentences"] = [
            "The finite-support basis for an arbitrary product gives the coordinatewise continuity criterion.",
            "Applying that criterion to the canonical regrouping maps in both directions proves the asserted product homeomorphisms and their agreement with the initial-topology formulation.",
            "This checks the mechanism of the reused text and adds background omitted by Hua, without importing it as another norm axiom."
        ]
p.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n")

p = r / "note_entries_part6.json"
entries = json.loads(p.read_text())
for n in entries:
    n["sentences"][-1] = n["sentences"][-1].replace("of T03", "of T14")
p.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n")
entry = {
    "id": ident,
    "kind": "unproved claim / targeted proof check",
    "quote": "“recollement”; “ouverts … fermés”",
    "context": "Hua98 omits scan 010, printed p. 36; its scope statement is the relevant contextual match.",
    "register": "RS–Ø.",
    "sentences": [
        "For compatible gluing, the positive result applies when all overlaps are open in both participating pieces, or when all are closed in both pieces.",
        "Saturating an open or respectively closed subset of one piece gives the same kind of trace on every other piece and proves that the original pieces embed.",
        "The interval-to-circle example similarly uses the locally finite family of closed integral translates to verify the quotient topology.",
        "These checks fill the topological mechanism omitted by Hua; T13 separately supplies the exercise’s counterexample when the overlap conditions are removed."
    ],
    "confidence": ""
}
(r / "note_entries_part7.json").write_text(json.dumps([entry], ensure_ascii=False, indent=2) + "\n")
p = r / "note_entries_part2a.json"
entries = json.loads(p.read_text())
for n in entries:
    if n["id"] == "MPL98.B09":
        n["sentences"] = [s.replace("BR10", "BR04") for s in n["sentences"]]
p.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n")
print(f"Registered {len(plan)} notes.")
