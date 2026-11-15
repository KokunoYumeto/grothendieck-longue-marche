#!/usr/bin/env python3
"""Reproduce the context searches attached to the Albanese research notes."""
from pathlib import Path
import re
import subprocess

root = Path(__file__).resolve().parents[2]
work = root / 'MPL_14_002-044_work'
source = work / 'records/research_albanese.md'
context = root / 'context'
files = [context / 'MPL_16+47+54+44_transcription.tex',
         context / 'MPL_16+47+54+44_notes.md',
         context / 'notes/RESULTS_STATE.md']
notes = re.split(r'(?=^### A\d+)', source.read_text(), flags=re.M)[1:]
out = ['# Context-search ledger: Albanese research notes', '',
       'Searches are against supplied context, which remains unreviewed evidence.',
       'Every note has its own query; all matched context scan locators are listed, with compact samples.', '']

for note in notes:
    ident = re.match(r'### (A\d+)', note).group(1)
    pattern = re.search(r'\*\*Context search:\*\* `([^`]+)`', note).group(1)
    out += [f'## {ident}', '', f'Query: `{pattern}`', '']
    for path in files:
        proc = subprocess.run(['rg', '-n', '-i', '-e', pattern, str(path)],
                              capture_output=True, text=True)
        assert proc.returncode in (0, 1), proc.stderr
        lines = path.read_text().splitlines()
        context_by_line = {}
        cote = scan = '?'
        heading = ''
        for n, line in enumerate(lines, 1):
            m = re.search(r'\\cotefile\{([^}]+)\}', line)
            if m: cote = m.group(1)
            m = re.search(r'\\scanpage\{([^}]+)\}', line)
            if m: scan = m.group(1)
            if line.startswith('#'): heading = line.lstrip('# ').strip()
            context_by_line[n] = (cote, scan, heading)
        matches = []
        for line in proc.stdout.splitlines():
            num, text = line.split(':', 1)
            num = int(num)
            matches.append((num, text, context_by_line[num]))
        out.append(f'### `{path.relative_to(root)}` — {len(matches)} matches')
        out.append('')
        if not matches:
            out += ['No match for this query.', '']
            continue
        if path.suffix == '.tex':
            locs = list(dict.fromkeys(f'cote{c}, scan{s}' for _, _, (c,s,_) in matches))
            out += ['Matched scan locators: ' + '; '.join(locs) + '.', '']
            priority = [m for m in matches if m[2][0] in ('44', '54')]
            examples = (priority or matches)[:6]
        else:
            examples = matches[-6:]
        for num, text, (cote, scan, heading) in examples:
            label = f'cote{cote}, scan{scan}' if path.suffix == '.tex' else heading
            out.append(f'- Line{num}, {label}: `{text[:220]}`')
        out.append('')

target = work / 'records/research_albanese_context_search.md'
target.write_text('\n'.join(out) + '\n')
print(f'Wrote {target}; {len(notes)} note queries across {len(files)} context files.')
