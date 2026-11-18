"""Build a complete current uncertainty index from manual records and TeX."""
import json,re
from pathlib import Path
from collections import defaultdict
root=Path(__file__).resolve().parents[1]
records=[json.loads(s) for s in (root/'records/readings.jsonl').read_text().splitlines()]
def esc(s):return str(s).replace('|',r'\|').replace('\n',' ')
def cell(s):return '`'+esc(s).replace('`','′')+'`'
out=['# MPL_67_053–101: notation, doubts, and abbreviations','',
 '## Notation table','',
 '| Recurring sign or form | LaTeX reading | Scan | Observation |',
 '|---|---|---:|---|']
for sign,tex,scans,note in json.loads((root/'records/notation_table.json').read_text()):
 out.append(f'| {esc(sign)} | {cell(tex)} | {scans} | {esc(note)} |')
out+=['','This is the final cross-page notation table. The image-based decisions are documented in `records/notation_audit.md`. Original page-save records are retained only as a historical audit trail; the final page files and this index govern the readings.','']
out+=['','## Complete in-place uncertainty index','',
 'Every `\\unsure` and `\\illegible` occurrence in the current page files is listed below, including uncertainties within deleted text and drawings. Line numbers refer to the page fragment and are approximate locators, not manuscript lineation. Confidence is medium by default for an `unsure` mark and low for an `illegible` mark; dense cancellations, overwritten marginalia, and character-art beneath drawings should be treated as low confidence even where a plausible partial reading is given. A first alternative is an ink reading, never a silent correction.','',
 '| Cote | Scan | TeX line | Mark | Reading | Alternatives | Confidence |',
 '|---:|---:|---:|---|---|---|---|']
for p in sorted((root/'pages').glob('*.tex')):
 s=p.read_text(); scan=int(re.search(r'scan(\d+)',p.name)[1])
 for m in re.finditer(r'\\(unsure|illegible)\{',s):
  start=m.end();i=start;depth=1
  while i<len(s) and depth:
   c=s[i]
   if c in '{}':
    j=i-1;slashes=0
    while j>=0 and s[j]=='\\':slashes+=1;j-=1
    if slashes%2==0:depth+=1 if c=='{' else -1
   i+=1
  body=s[start:i-1];parts=body.split('|');line=s.count('\n',0,m.start())+1
  out.append(f'| 67 | {scan} | {line} | {m[1]} | {cell(parts[0])} | {cell(" / ".join(parts[1:])) if len(parts)>1 else "—"} | {"low" if m[1]=="illegible" else "medium"} |')
out+=['','## Abbreviations encountered','',
 'Expansions below are suggestions for the reader only; none is inserted into the diplomatic text.','',
 '| Form in the manuscript | Proposed expansion | Scans |','|---|---|---|']
ab=defaultdict(lambda:defaultdict(set))
for rec in records:
 for short,long in rec['abbreviations']:ab[short][long].add(rec['scan'])
for short,forms in sorted(ab.items(),key=lambda x:x[0].casefold()):
 for long,scans in forms.items():out.append(f'| {esc(short)} | {esc(long)} | {", ".join(map(str,sorted(scans)))} |')
out+=['','## Legibility and limits','',
 'All 47 supplied whole-page images and both supplied halves of every page were inspected directly, in scan order, without OCR. The main prose is usually readable; many formula indices, inserted words, and overwritten cancellations are substantially less secure. The doubts are part of the transcription, not a claim that every unmarked reading is certain.','',
 'The least secure areas are the heavily reworked preliminary sheet 53; diagonal margins on 56, 65, 71, and 86; cancellations on 57, 60, 75–78, 87, 91, 93–95, and 100; and small lettering beneath colored drawing strokes on the reused computer printout 96. The printed character-art banners on 92 and 96 were transcribed manually; spacing and repeated-character counts are less certain than ordinary printed words and numbers. The freehand shapes on 96 are TikZ approximations, as explicitly marked, not exact digital tracings.','',
 'Paper perforations, paper ruling, stains, and mirror-reversed show-through from the other side are not treated as authored marks on this face. Archive pencil foliation is recorded only in TeX comments; author pagination is separate. Cancellations remain in place, including mathematically surprising formulas.','']
(root/'MPL_67_053-101_doubts.md').write_text('\n'.join(out))
print(f'Wrote doubts and notation index for {len(records)} pages.')
