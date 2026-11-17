#!/usr/bin/env python3
"""Run the root-authored research-item searches against the supplied context.

Only writes search locators, not copies of the supplied context or transcription.
"""
from pathlib import Path
from collections import Counter
import re
import subprocess
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
CONTEXT=ROOT.parent/'context'
NOTES=ROOT/'MPL_138_001-045_notes.md'
text=NOTES.read_text()
heads=list(re.finditer(r'^### ([A-Z]\d\d) — (.+)$',text,re.M))
lines=['# Per-item context searches','',
       'Run after the transcription freeze. All queries are the root author\'s expressions from the notes.',
       'Input scope: the four supplied context files; output contains locators and counts only, not copies of those files.',
       '',f'Run time: {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")}.','',
       '| Note | Search expression | Matches by context file | Selected matching line numbers |',
       '|---|---|---|---|']
errors=[]
counts={}
for index,h in enumerate(heads):
    end=heads[index+1].start() if index+1<len(heads) else len(text)
    block=text[h.end():end]
    found=re.search(r'\*\*Search:\*\* `([^`]+)`',block)
    if not found:
        errors.append((h[1],'missing Search field')); continue
    expr=found[1]
    proc=subprocess.run(['rg','-n','--no-heading','-e',expr,str(CONTEXT)],text=True,capture_output=True)
    if proc.returncode not in (0,1):
        errors.append((h[1],expr,proc.stderr.strip())); continue
    locators={}
    for line in proc.stdout.splitlines():
        path,lineno,_=line.split(':',2)
        short='context/'+str(Path(path).relative_to(CONTEXT))
        locators.setdefault(short,[]).append(int(lineno))
    counts[h[1]]=sum(len(v) for v in locators.values())
    filecounts='; '.join(f'`{p}`: {len(v)}' for p,v in sorted(locators.items())) or 'No matches'
    loc='; '.join(f'`{p}`: '+', '.join(map(str,v[:12]))+(' …' if len(v)>12 else '') for p,v in sorted(locators.items())) or '—'
    lines.append('| '+h[1]+' | `'+expr.replace('|','&#124;')+'` | '+filecounts+' | '+loc+' |')
if errors:
    for error in errors: print(error)
    raise SystemExit('Search errors must be resolved before the final log is written.')
lines += ['',f'Completed {len(heads)} item searches; all result counts above come from actual rg calls.',
          'The author compared these hits with the already-read subsections and the exact RS rows cited in each note. A keyword hit records retrieval, not acceptance of a mathematical claim.','']
(ROOT/'records'/'context_searches.md').write_text('\n'.join(lines))
print({'items':len(heads),'zero_match_items':[k for k,v in counts.items() if not v], 'files':sorted(str(p.relative_to(CONTEXT)) for p in CONTEXT.rglob('*') if p.is_file())})
