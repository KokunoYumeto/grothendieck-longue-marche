#!/usr/bin/env python3
"""Build research notes and a per-item, source-located context search record.

This script only reads the frozen transcription. It never writes a TeX file.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
CTX = ROOT.parent / 'MPL_62_002-050_context'
DATA = ROOT / 'records/research/notes_entries.json'

def context_lines():
    rows = []
    for name in ['README.md', 'notes/RESULTS_STATE.md',
                 'MPL_16+47+54+44_transcription.tex',
                 'MPL_16+47+54+44_notes.md',
                 'MPL_16+47+54+44_doubts.md']:
        cote = scan = heading = None
        for num, line in enumerate((CTX / name).read_text().splitlines(), 1):
            c = re.search(r'\\cotefile\{(\d+)\}', line)
            s = re.search(r'\\scanpage\{(\d+)\}', line)
            if c:
                cote, scan = c.group(1), None
            if s:
                scan = s.group(1)
            if line.startswith('#'):
                heading = line.strip('# ').strip()
            rows.append(dict(file=name, line=num, cote=cote, scan=scan,
                             heading=heading, text=line))
    return rows

def main():
    data = json.loads(DATA.read_text())
    source = context_lines()
    searches = []
    for n in data['notes']:
        queries = n['queries']
        hits = []
        counts = {}
        # Search all supplied textual context for every note before rendering it.
        for q in queries:
            pattern = re.compile(q, re.I)
            matches = [r for r in source if pattern.search(r['text'])]
            counts[q] = len(matches)
            for r in matches[:12]:
                hits.append(dict(query=q, **r))
        searches.append(dict(id=n['id'], queries=queries, counts=counts,
                             excerpts=hits, editorial_comparison=n['context'],
                             register=n['register']))
    record = ROOT / 'records/research/context_searches.json'
    record.write_text(json.dumps(searches, ensure_ascii=False, indent=2) + '\n')
    out = [data['front_matter'].strip(), '']
    section = None
    for n in data['notes']:
        if n['section'] != section:
            section = n['section']
            out += [f'## {section}', '']
        out += [f"### {n['id']} — {n['title']}", '',
                f"**Source:** 62.pdf, cote 62, scan(s) {n['scans']}; {n['position']}.  ",
                f"**Kind:** {n['kind']}.  ",
                f"**Manuscript:** {n['quote']}", '',
                n['body'], '',
                f"**Context comparison:** {n['context']}  ",
                f"**Results register:** {n['register']}  "]
        if n.get('confidence'):
            out += [f"**Own-idea confidence and reason:** {n['confidence']}  "]
        out += [f"**Search record:** {n['id']} in records/research/context_searches.json.", '']
    out += [data['back_matter'].strip(), '']
    target = ROOT / 'MPL_62_002-050_notes.md'
    target.write_text('\n'.join(out))
    print(json.dumps({'notes':len(data['notes']), 'words':len(target.read_text().split()),
                      'bytes':target.stat().st_size, 'context_searches':len(searches)}))

if __name__ == '__main__':
    main()
