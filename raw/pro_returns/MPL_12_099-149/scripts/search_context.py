#!/usr/bin/env python3
"""Research-phase, read-only contextual search. Never reads scan images or edits TeX.

Usage: search_context.py NOTE_ID 'regex' [--limit 35]
Each call saves all matching locators in records/research_searches/NOTE_ID.json.
The source context is deliberately not copied into the deliverable.
"""
import argparse, json, re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTEXT = ROOT.parents[1] / 'context'
parser = argparse.ArgumentParser()
parser.add_argument('note_id')
parser.add_argument('pattern')
parser.add_argument('--limit', type=int, default=35)
args = parser.parse_args()
pattern = re.compile(args.pattern, re.I)
paths = ['README.md', 'MPL_16+47+54+44_transcription.tex',
         'MPL_16+47+54+44_notes.md', 'MPL_16+47+54+44_doubts.md',
         'notes/RESULTS_STATE.md', 'hua_project/README.md', 'hua_project/12.modern.tex']
matches = []
for relative in paths:
    path = CONTEXT / relative
    cote = scan = section = None
    for number, line in enumerate(path.read_text().splitlines(), 1):
        cm = re.search(r'\\cotefile\{([^}]+)\}', line)
        sm = re.search(r'\\scanpage\{([^}]+)\}', line)
        if cm: cote = cm.group(1)
        if sm: scan = sm.group(1)
        if line.startswith('#') or re.match(r'\\(?:sub)*section\*?\{', line):
            section = line.strip()
        if pattern.search(line):
            matches.append({'file':relative,'line':number,'cote':cote,
                            'scan':scan,'section':section,'text':line})
record = {'note_id':args.note_id,'query':args.pattern,
          'searched_at_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
          'files':paths,'match_count':len(matches),
          'matches':[{k:v for k,v in m.items() if k != 'text'} for m in matches],
          'record_policy':'Complete match locators; source text remains in supplied context.'}
dest = ROOT / 'records' / 'research_searches'
dest.mkdir(parents=True, exist_ok=True)
(dest / f'{args.note_id}.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'note_id':args.note_id,'query':args.pattern,'match_count':len(matches),
                  'matches':matches[:args.limit]},ensure_ascii=False,indent=2))
