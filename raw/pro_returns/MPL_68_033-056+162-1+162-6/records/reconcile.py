from pathlib import Path
from datetime import datetime, timezone
import re, json
root=Path(__file__).resolve().parents[1]
prefix='MPL_68_033-056+162-1+162-6'
changed=[]
for p in sorted((root/'pages').glob('*.tex')):
    s=p.read_text()
    t=re.sub(r'\\mathbf\s+([QNRZ])',lambda m:r'\mathbb{'+m[1]+'}',s)
    t=re.sub(r'\\mathbf\{([QNRZ])\}',lambda m:r'\mathbb{'+m[1]+'}',t)
    if 'scan038' in p.name:
        t=t.replace('on trouve $x$ nilpotent, cqfd.',r'on trouve $x$ \unsure{nilp.t|nilpotent}, cqfd.')
    if t!=s:
        p.write_text(t)
        changed.append(p.name)
with (root/'doubts_rows.jsonl').open('a') as f:
    f.write(json.dumps(dict(cote='68',scan=38,position='last line, after x',reading='nilp.t',alternatives='nilpotent; ending is abbreviated or compressed',confidence='medium',audit=True),ensure_ascii=False)+'\n')
with (root/'progress.log').open('a') as f:
    f.write('notation reconciliation '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
    f.write('Reconciled doubled number alphabets as mathbb after comparing Q/N on 036 and 038, R/N on 050–054, and N/Z on 056. Ordinary variables and unit 1 are distinguished. Rechecked bars, primes, literal equals shorthand, arrows and font differences; retained all ink-supported local discrepancies. Scan 038 final compressed nilp.t is explicitly doubtful rather than expanded without warning.\n')
    f.write('reconciliation affected: '+', '.join(changed)+'\n')
(root/f'{prefix}_transcription.tex').write_text('\n'.join(p.read_text().rstrip()+'\n' for p in sorted((root/'pages').glob('*.tex'))))
print('Combined transcription assembled from',len(list((root/'pages').glob('*.tex'))),'pages.')
