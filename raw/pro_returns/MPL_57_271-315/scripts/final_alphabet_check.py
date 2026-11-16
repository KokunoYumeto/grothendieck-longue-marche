from pathlib import Path
import json,subprocess
from datetime import datetime,timezone
root=Path('MPL_57_271-315')
for scan in [272,281,285,289,291,292]:
 p=root/'records'/f'scan{scan}.json';d=json.loads(p.read_text());t=d['tex']
 if scan==281:
  t=t.replace(r'\unsure{\mathbf Q|\mathbb Q}',r'\unsure{\mathbb Q|\mathbf Q}')
 else:
  for letter in ['C','Q','Z']:t=t.replace('\\mathbf '+letter,'\\mathbb '+letter)
 if scan==285:
  t=t.replace(r'\mathcal O_X',r'\unsure{\uline{\mathcal O}|\mathcal O}_X')
  d['doubts'].append({'line':'two H1 structure-sheaf occurrences','reading':'underlined script O','alternatives':'the lower stroke may belong to the script letter itself','confidence':'medium'})
 d['tex']=t
 d['observations'].append('Pre-freeze alphabet comparison: doubled C/Q/Z strokes compared directly with scans 272, 281, 285, 289, 291, 292 and retained consistently as mathbb; the residual Q uncertainty on 281 remains marked.')
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');subprocess.run(['python3',str(root/'scripts/manage.py'),'save','--input',str(p)],check=True,stdout=subprocess.DEVNULL)
with (root/'progress.log').open('a') as f:f.write('notation alphabet comparison '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'; source images 272,281,285,289,291,292 revisited for doubled C/Q/Z; uniform mathbb rendering, remaining doubt retained\n')
print('Alphabet consistency saved for six pages.')
