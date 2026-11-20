"""Extract page-specific prior questions; recognizes inclusive scan ranges."""
from pathlib import Path
import json,re,argparse
OUT=Path(__file__).resolve().parents[1];ROOT=OUT.parent
SRC=ROOT/'source/SP43_CW_29+32_witnesses'
p=argparse.ArgumentParser();p.add_argument('stem');a=p.parse_args()
m=json.loads((ROOT/'work'/a.stem/'meta.json').read_text());n=int(m['our_scan']);folder=SRC/'codex'/m['folder']
def covers(cell):
 for aa,bb in re.findall(r'(\d+)\s*[–—-]\s*(\d+)',cell):
  if int(aa)<=n<=int(bb):return True
 return bool(re.search(r'(?<!\d)'+str(n)+r'(?!\d)',cell))
s=(folder/(m['folder']+'_doubts.md')).read_text();selected=[];heading=''
for line in s.splitlines():
 if line.startswith('#'):heading=line
 if line.startswith('|') and covers(line.split('|')[1]):selected.append(heading+'\n'+line)
notes=(folder/(m['folder']+'_notes.md')).read_text()
paragraphs=re.split(r'\n\s*\n|\n(?=\s*[-*]\s)',notes)
for q in paragraphs:
 if covers(q):
  # A notes paragraph may be a table. Keep its headings and only the rows
  # whose first column identifies the assigned scan, never other-page titles.
  filtered=[]
  for line in q.splitlines():
   if line.startswith('|'):
    first=line.split('|')[1].strip()
    if re.search(r'\d',first) and not covers(first):continue
   filtered.append(line)
  q='\n'.join(filtered)
  # Shared notes sometimes discuss several scans in one paragraph. Remove
  # sentences explicitly assigned only to other scans, retaining common
  # introductory qualifications and the current scan/range sentences.
  sentences=re.split(r'(?<=\.)\s+(?=[A-Z])',q)
  kept=[]
  for sentence in sentences:
   if 'archive numbers are' in sentence and 'respectively' in sentence:
    sentence=re.sub(r'The lower-corner archive numbers are .*?respectively; these are recorded only as comments in the transcription, not treated as the text.s own pagination\.', 'Archive numbers are recorded as comments, not as the text\'s own pagination.', sentence)
   mentions=re.findall(r'(?i)\bscans?\s+(\d+(?:\s*[–—-]\s*\d+)?)',sentence)
   if mentions and not any(covers(x) for x in mentions):continue
   kept.append(sentence)
  if kept:selected.append('Prior note excerpt for this scan (other explicit scan sentences removed):\n'+' '.join(kept))
result='\n\n'.join(selected)+'\n'
# Some current-page doubt rows contain a comparative aside naming another
# scan without the word "scan". The question and its own-page ink survive;
# remove only these explicit cross-page comparative clauses before assignment.
result=re.sub(r'Side-by-side comparison with (\d+) shows the same composite\.\s*',lambda m: m.group(0) if covers(m.group(1)) else '',result)
result=re.sub(r', consistently with (\d+)\.',lambda m: m.group(0) if covers(m.group(1)) else '.',result)
result=result.replace('Same composite numeral family as the previous page; both shapes retained.', 'Both shapes retained in the current-page prior question.')
result=re.sub(r'Same rounded outer U and inner diagonal as on (\d+)\.',lambda m: m.group(0) if covers(m.group(1)) else 'Rounded outer U and inner diagonal in the current-page question.',result)
result=result.replace('The final comparison keeps the same visual primary and all four candidates on both pages.', '')
outside=[x for x in re.findall(r'(?i)\bscans?\s+(\d+(?:\s*[–—-]\s*\d+)?)',result) if not covers(x)]
if outside:raise RuntimeError('Out-of-page scan references remain in prior questions: '+str(outside))
(ROOT/'work'/a.stem/'C_prior_questions.md').write_text(result)
print('Refreshed prior questions for',a.stem)
