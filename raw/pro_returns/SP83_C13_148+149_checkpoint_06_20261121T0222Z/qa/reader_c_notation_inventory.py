"""Read-only inventory for reader_c's notation QA; no source or record edits."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def unsure_units(text):
    units = []
    for match in re.finditer(r"\\unsure\s*\{", text):
        i, level = match.end(), 1
        while i < len(text) and level:
            ch = text[i]
            if ch in "{}":
                backslashes = 0
                k = i - 1
                while k >= 0 and text[k] == "\\":
                    backslashes += 1
                    k -= 1
                if backslashes % 2 == 0:
                    level += 1 if ch == "{" else -1
            i += 1
        units.append({
            "reading": text[match.start():i],
            "line": text.count("\n", 0, match.start()) + 1,
            "context": text[max(0, match.start()-70):min(len(text), i+70)].replace("\n", " "),
        })
    return units


def norm(text):
    # Exactish comparison only. Candidates need manual contextual review.
    text = text.replace("&#124;", "|")
    text = text.replace("\\geq", "\\ge").replace("\\neq", "\\ne")
    text = text.replace("R^{\\prime}", "R'")
    text = text.replace("\\widetilde{\\Sigma}", "\\widetilde\\Sigma")
    text = text.replace("\\overline{\\Sigma}", "\\overline\\Sigma")
    return re.sub(r"\s+", "", text)


out = {"method": "balanced unsure extraction; normalized exact containment in final doubts only; no adjudication", "pages": []}
for path in sorted((ROOT / "pages").glob("*.tex")):
    text = path.read_text()
    record_path = ROOT / "records" / (path.stem + ".json")
    data = json.loads(record_path.read_text()) if record_path.exists() else {}
    doubts = data.get("doubts", [])
    doubt_text = json.dumps(doubts, ensure_ascii=False)
    doubt_readings = "\n".join(str(d.get("reading", "")) for d in doubts)
    units = unsure_units(text)
    unique = []
    seen = set()
    for unit in units:
        key = norm(unit["reading"])
        if key in seen:
            continue
        seen.add(key)
        unit["covered_by_final_doubt_reading"] = key in norm(doubt_readings)
        unique.append(unit)
    controls = {}
    for name in ["gamma", "sigma", "Sigma", "Gamma", "phi", "varnothing", "ell", "pm", "widetilde", "overline", "mathbb", "mathcal", "mid", "vert", "Vert"]:
        matches = list(re.finditer(r"\\" + name + r"\b", text))
        if matches:
            controls[name] = [{"line": text.count("\n", 0, m.start())+1, "context": text[max(0,m.start()-30):m.end()+70].replace("\n", " ")} for m in matches]
    out["pages"].append({
        "page": path.stem,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "doubt_entries": len(doubts),
        "unsure_occurrences": len(units),
        "unique_unsure": unique,
        "notation": data.get("notation", []),
        "controls": controls,
    })

target = ROOT / "qa" / "reader_c_notation_inventory.json"
target.write_text(json.dumps(out, ensure_ascii=False, indent=2)+"\n")
print("pages", len(out["pages"]))
print("unsure occurrences", sum(p["unsure_occurrences"] for p in out["pages"]))
print("unique page-local unsure", sum(len(p["unique_unsure"]) for p in out["pages"]))
for page in out["pages"]:
    candidates = [u for u in page["unique_unsure"] if not u["covered_by_final_doubt_reading"]]
    if candidates:
        print("\n"+page["page"]+" coverage candidates:")
        for u in candidates:
            print(" line", u["line"], u["reading"][:500])
