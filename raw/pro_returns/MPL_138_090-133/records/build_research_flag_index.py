#!/usr/bin/env python3
"""Index literal questions and proof/reservation phrases in saved page TeX only."""
from pathlib import Path
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import json
import re
import validate_package as v

ROOT = Path(__file__).resolve().parent.parent
PREFIX = "MPL_138_090-133"
PATTERNS = {
    "literal question mark": r"\?",
    "question wording": r"\bquestions?\b|\bQue\s+se\s+passe",
    "verification or reservation": r"\bv[ée]rifi\w*|\bsauf\s+erreur\b|\bje\s+pr[ée]sume\b|\badmis\b|\bconjectur\w*",
    "expectation or impression": r"\bsembl\w*|\bimpression\b|\bprobable\w*|\bsans\s+doute\b|\bespoir\b|\besp[ée]r\w*|\bon\s+devrait\b|\bon\s+pourrait\b|\bil\s+serait\s+int[ée]ressant\b",
    "proof or knowledge phrase": r"\bfacile\w*|\b[ée]viden\w*|\bon\s+voit\b|\bon\s+verra\b|\bon\s+peut\s+(?:montrer|voir|d[ée]montrer)\b|\bon\s+prouve\b|\bil\s+suffit\b|\bil\s+faut\b|\bon\s+sait\b|\bimm[ée]diat\w*|\breste\s+[àa]\b|\b[ée]quivalen\w*",
    "proof or theorem label": r"(?<!\w)(?:Th\.|Prop\.|D[ée]m\.|Lemme\b|preuve\b|d[ée]monstration\b)",
    "provisional label": r"\bprovisoire\b",
}


def main():
    entries, hashes = [], {}
    for path in sorted((ROOT / "pages").glob(f"{PREFIX}_138_scan[0-9][0-9][0-9].tex")):
        scan = int(re.search(r"scan(\d+)", path.name).group(1))
        data = path.read_bytes()
        raw = data.decode("utf-8")
        clean = v.uncomment(raw)
        lines = raw.splitlines()
        hashes[path.name] = hashlib.sha256(data).hexdigest()
        hits = defaultdict(lambda: {"labels": set(), "triggers": set()})
        for label, pattern in PATTERNS.items():
            for match in re.finditer(pattern, clean, re.I):
                first = v.line_at(raw, match.start())
                last = v.line_at(raw, max(match.start(), match.end() - 1))
                hits[(first, last)]["labels"].add(label)
                hits[(first, last)]["triggers"].add(raw[match.start():match.end()])
        for (first, last), hit in sorted(hits.items()):
            entries.append({"scan": scan, "first_tex_line": first, "last_tex_line": last, "labels": sorted(hit["labels"]), "literal_triggers": sorted(hit["triggers"]), "exact_tex": "\n".join(lines[first - 1:last])})
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    md = f"# Mechanical research-flag evidence index\n\nGenerated: {now}\n\n"
    md += ("This index mechanically extracts every literal question mark and matches from the phrase families listed below in the saved page TeX. It does not read scans or research context, evaluate a claim, identify a proof, classify a question as unresolved, or change the frozen transcription. A matched phrase may occur in cancelled text, an insertion, a margin, or a diagram; the exact TeX retains that apparatus. Line numbers are local TeX source lines.\n\n")
    md += ("Phrase families include question/questions; vérifier and related forms; sauf erreur; je présume; admis; conjecture; semble; impression; probable; sans doute; hope/expectation forms; facile; évident; on voit/on verra/on peut montrer/on prouve/on sait; il suffit/il faut; immédiat; reste à; équivalent; theorem/proof labels; and provisoire. This is a literal screening index, not an exhaustive semantic classification of unproved claims.\n\n")
    md += f"Found {len(entries)} line/range entries on {len({x['scan'] for x in entries})} scans. Exact source hashes and match details are in `research_flag_index.json`.\n"
    current_scan = None
    for entry in entries:
        if current_scan != entry["scan"]:
            current_scan = entry["scan"]
            md += f"\n## Scan {current_scan}\n"
        location = str(entry["first_tex_line"]) if entry["first_tex_line"] == entry["last_tex_line"] else f"{entry['first_tex_line']}–{entry['last_tex_line']}"
        md += f"\n### TeX line {location}\n\nTriggers: " + "; ".join(entry["literal_triggers"]).replace("\n", " ") + ".\n\n"
        md += "```tex\n" + entry["exact_tex"] + "\n```\n"
    (ROOT / "records/research_flag_index.md").write_text(md)
    (ROOT / "records/research_flag_index.json").write_text(json.dumps({"generated_utc": now, "source_hashes": hashes, "patterns": PATTERNS, "entries": entries}, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"time": now, "entries": len(entries), "scans": sorted({x["scan"] for x in entries}), "literal_question_marks": sum(len(re.findall(r"\?", x["exact_tex"])) for x in entries if "literal question mark" in x["labels"])}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
