from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parents[1]
rows=list(csv.reader((ROOT/'documentation/doubts_rows.tsv').open(),delimiter='\t'))
def esc(x): return x.replace('|','\\|').replace('\n',' ')
text=(ROOT/'documentation/notation.md').read_text()+'\n## Doubts recorded during the visual reading and audit\n\n'
text+='Approximate lines count visible manuscript lines or identify the region of the sheet. Earlier alternative readings are retained in this record even where the audit subsequently favoured one; the page files are the authoritative current readings.\n\n'
text+='| Cote | Scan | Approximate line / region | Reading | Alternative / difficulty | Confidence |\n|---|---:|---|---|---|---|\n'
for row in rows:
    if len(row)!=6: raise ValueError(row)
    row[-1]={'very low':'low','medium-low':'low'}.get(row[-1],row[-1])
    text+='| '+' | '.join(map(esc,row))+' |\n'
for name in ['abbreviations.md','legibility.md']:
    p=ROOT/'documentation'/name
    if p.exists():text+='\n'+p.read_text()
(ROOT/'MPL_93_092-134_doubts.md').write_text(text)
print(f'Assembled {len(rows)} doubt records.')
