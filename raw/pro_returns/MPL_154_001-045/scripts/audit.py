from pathlib import Path
from datetime import datetime,timezone
import csv,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from workflow import combine

def audit(n,note):
 p=ROOT/'progress.log'
 token=f'scan {n:03d} audited '
 assert token not in p.read_text(),f'already audited {n}'
 with p.open('a') as f:
  f.write(f'154 scan {n:03d} second visual comparison: {note}\n')
  f.write(token+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
 combine()
 print(f'Audited {n:03d}: {note}')

def doubt(n,location,reading,issue,confidence='low'):
 p=ROOT/'MPL_154_001-045_doubts.md'
 s=p.read_text()
 row='| 154 | '+str(n)+' | '+' | '.join(x.replace('|',' / ') for x in (location,reading,issue,confidence))+' |\n'
 s=s.replace('\n# Abbreviations\n','\n'+row+'\n# Abbreviations\n')
 p.write_text(s)

if __name__=='__main__':audit(int(sys.argv[1]),' '.join(sys.argv[2:]))
