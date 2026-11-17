"""Consolidate manually entered reading records; no image processing or OCR."""
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parent
records = [json.loads(s) for s in (ROOT/'reading_records.jsonl').read_text().splitlines() if s.strip()]
def esc(s):
    return str(s).replace('|', r'\|').replace('\n', ' ')
lines = ['# Notation table', '', '| Source sign or form | LaTeX / transcription convention | Evidence and distinction |', '|---|---|---|']
fixed = [
 ('Archive numbers', '`% archive foliation: n`', 'Never represented by mspage; printed reused-page numbers are ordinary text.'),
 ('Quotation marks', "``...''", 'Double quotes retained in LaTeX form; no guillemets supplied without ink evidence.'),
 ('Prime / double prime / star / exclamation', "`G'`, `G''`, `D^*`, `^!` as separately read", 'No blanket prime/exclamation substitution; weak superscripts carry unsure.'),
 ('Abbreviations', 'Kept as written', 'Expansions occur only in the abbreviations list below.'),
 ('Plain stroke versus arrow', '`-`, `\\longrightarrow`, or tikz-cd no head', 'No arrowhead supplied merely because a map is expected.'),
 ('Uncertain ink', '`\\unsure{reading}` or `\\unsure{reading|alternative}`', 'First reading follows the perceived ink, including unusual grammar and mathematics.'),
 ('Underlines', '`\\uline`, `\\uuline`, mathematical `\\underline`', 'Underline is distinguished from closure bar and limit arrow.'),
 ('Nilpotent iterate', '`f^j`, `f^{n-j}`', 'Looped handwritten j is checked against neighbouring indices; parenthesized exponents remain parenthesized.'),
 ('Divided powers', '`x^{(n)}`, `J^{(n)}`', 'Parenthesized superscripts are not ordinary powers.'),
 ('Left torsion subscripts', '`{}_{p^n}G`', 'Not modernized to G[p^n].'),
]
for row in fixed: lines.append('| '+' | '.join(map(esc,row))+' |')
for r in records:
    for row in r['notation']:
        a,b,*c=row
        lines.append('| '+' | '.join(map(esc,[a,b,f"129 scan {r['scan']:03d}: "+' '.join(c)]))+' |')
lines += ['', '# Doubts and literal anomalies', '', 'Confidence describes the visual reading, not mathematical correctness. A high-confidence anomaly is deliberately retained when the ink supports it.', '', '| File / cote | Scan | Approximate place | Reading | Alternatives / qualification | Confidence |', '|---|---:|---|---|---|---|']
for r in records:
    for row in r['doubts']:
        if len(row)!=4: raise ValueError((r['scan'],row))
        pos,reading,alternative,confidence=row
        lines.append('| '+' | '.join(map(esc,['129.pdf / 129',f"{r['scan']:03d}",pos,reading,alternative or 'No secure alternative.',confidence]))+' |')
lines += ['', '# Abbreviations', '', 'These are proposed expansions, not additions to the transcription. Where an abbreviation itself is uncertain, its expansion remains uncertain.', '', '| Form on the page | Proposed expansion | Scans |', '|---|---|---|']
ab={}
for r in records:
    for a,b in r['abbreviations']:
        ab.setdefault((a,b),[]).append(f"{r['scan']:03d}")
for (a,b),scans in ab.items():lines.append('| '+' | '.join(map(esc,[a,b,', '.join(scans)]))+' |')
lines += ['', '# Legibility and limits', '', 'The blue typescripts are generally clear, although missing type, overtyping, handwritten insertions, and a few symbol forms still require care. The rapid handwritten sheets are substantially less secure. In particular, the lower part of scan 100, the compact derived-category notes in scans 092–095, the revisions in scans 104 and 106–110, and the clipped lower writing of scan 113 contain low-confidence readings; the local doubt marks are part of the deliverable, not silent editorial repairs.', '', 'Whole scans and their supplied halves are read visually in one stream. Enlargements and rotations are used only for inspection; no OCR is used. Faint mirrored show-through on reused backs is distinguished from the face text and is transcribed from the corresponding clearly printed face when available. Scan 112 has no discernible author text, only archive foliation; it is retained as a page. Ink offsets, paper defects, and stains are not treated as words.', '', 'This file is regenerated from the per-page manual reading records. The final audit and notation check are documented in progress.log. The frozen transcription is not revised from the later research context.', '']
(ROOT/'MPL_129_077-115_doubts.md').write_text('\n'.join(lines),encoding='utf-8')
print(f'Consolidated {len(records)} page records, {sum(len(r["doubts"]) for r in records)} doubt rows.')
