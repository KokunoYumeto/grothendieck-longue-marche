from pathlib import Path
import csv
root=Path(__file__).resolve().parents[1]
prefix='MPL_93_002-046'
def cell(s):return s.replace('|','\\|').replace('\n',' ')
text=(root/'notation_table.md').read_text()+'\n# Doubt register\n\n| File | Scan | Approximate line / location | Reading | Alternatives | Confidence | Reason |\n|---|---|---|---|---|---|---|\n'
with (root/'doubt_records.csv').open(newline='') as f:
 for r in csv.reader(f):
  if r[0]=='file':continue
  text+='| '+' | '.join(cell(s) for s in r)+' |\n'
text+='\n'+(root/'legibility_note.md').read_text()
(root/f'{prefix}_doubts.md').write_text(text)
