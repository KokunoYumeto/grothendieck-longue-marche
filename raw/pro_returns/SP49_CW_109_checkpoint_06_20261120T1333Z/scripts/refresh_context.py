"""Select page-specific witness tables by their Scan column, not numeric row IDs."""
from pathlib import Path
import re,json,sys
W=Path(__file__).resolve().parents[1]
S=W.parent/'source/SP49_CW_109_witnesses/codex'
def applies(cell,n):
 # Page-column values may be a scan or a range/list of scans. Other numeric columns are never inspected.
 for lo,hi in re.findall(r'\b0*(\d+)\s*[–−-]\s*0*(\d+)\b',cell):
  if int(lo)<=n<=int(hi):return True
 return bool(re.search(r'(?<!\d)0*'+str(n)+r'(?!\d)',cell))
def table_rows(content,n):
 scan_col=None
 for line in content.splitlines():
  if not line.lstrip().startswith('|'):
   scan_col=None;continue
  cells=[c.strip() for c in line.strip().strip('|').split('|')]
  hits=[i for i,c in enumerate(cells) if re.fullmatch(r'(?i)(?:our\s+)?scans?',c)]
  if hits:scan_col=hits[0];continue
  if all(re.fullmatch(r'[:\s-]*',c) for c in cells):continue
  if scan_col is not None and scan_col<len(cells) and applies(cells[scan_col],n):yield line
start=int(sys.argv[1]);changed=[]
for p in sorted((W/'inputs').iterdir()):
 if not p.name.isdigit() or int(p.name)<start:continue
 n=int(p.name);folder=json.loads((p/'metadata.json').read_text())['folder'];context=[]
 for kind in ['doubts','notes']:
  content=(S/folder/f'{folder}_{kind}.md').read_text()
  for line in table_rows(content,n):
   if line not in context:context.append(line)
  if kind=='notes':
   for para in content.split('\n\n'):
    if not para.lstrip().startswith('|') and re.search(r'(?i)scan\s+0*'+str(n)+r'\b',para):context.append(para)
 text='# Earlier witness C doubts, notation and notes for this page\n\n'+'\n\n'.join(context)
 (p/'C_context.md').write_text(text);changed.append(n)
print('Refreshed source context by Scan column:',changed)
