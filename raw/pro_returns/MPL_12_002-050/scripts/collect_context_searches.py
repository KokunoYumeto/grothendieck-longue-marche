#!/usr/bin/env python3
"""Record one actual bounded context search per research item, after freeze.

Only the four supplied text context files are searched. No scan/OCR access,
network retrieval, Library enumeration, or transcription mutation occurs.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

root = Path(__file__).resolve().parents[1]
workspace = root.parent
notes = root / 'MPL_12_002-050_notes.md'
targets = [
    workspace / 'context/MPL_16+47+54+44_transcription.tex',
    workspace / 'context/MPL_16+47+54+44_notes.md',
    workspace / 'context/hua_project/12.modern.tex',
    workspace / 'context/notes/RESULTS_STATE.md',
]
manifest = json.loads((root / 'frozen_hashes.json').read_text())
expected = manifest.get('files', manifest)
def verify_frozen():
    for name, digest in expected.items():
        if hashlib.sha256((root / name).read_bytes()).hexdigest() != digest:
            raise RuntimeError(f'Frozen file changed: {name}')
verify_frozen()

positions = {}
for path in targets:
    rows = path.read_text(encoding='utf-8').splitlines()
    locations = []
    cote = scan = None
    heading = '(file opening)'
    for number, line in enumerate(rows, 1):
        c = re.search(r'\\cotefile\{([^}]+)\}', line)
        s = re.search(r'\\scanpage\{([^}]+)\}', line)
        if c:
            cote = c.group(1)
        if s:
            scan = s.group(1)
        if line.startswith('#'):
            heading = line.lstrip('#').strip()
        if re.match(r'\\(?:sub)*section\{', line):
            heading = line
        locations.append(f'{cote}/{int(scan):03d}' if cote and scan else heading)
    positions[path] = (rows, locations)

source = notes.read_text(encoding='utf-8')
blocks = re.split(r'(?=^#### N\d{3} —)', source, flags=re.M)
items = []
for block in blocks:
    match = re.match(r'#### (N\d{3}) — (.*)', block)
    if not match:
        continue
    query = re.search(r'\*\*Search:\*\* `([^`]+)`', block)
    if not query:
        raise RuntimeError(f'{match.group(1)} has no search field')
    terms = [s.strip() for s in query.group(1).split('|') if s.strip()]
    patterns = []
    for term in terms:
        # Fixed-string searches avoid cross-engine ambiguity in TeX braces.
        # Dots in the note's compact search terms allow hyphen/space variants.
        for variant in (term, term.replace('.', '-'), term.replace('.', ' ')):
            if variant not in patterns:
                patterns.append(variant)
    files = []
    for path in targets:
        command = ['rg', '--fixed-strings', '--no-heading', '-n', '--color', 'never', '-i']
        for pattern in patterns:
            command += ['-e', pattern]
        command += ['--', str(path)]
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        if result.returncode not in (0, 1):
            raise RuntimeError(f'{match.group(1)}: {result.stderr}')
        hits = []
        for hit in result.stdout.splitlines():
            n, sep, excerpt = hit.partition(':')
            if sep and n.isdigit():
                line_number = int(n)
                hits.append({'line': line_number,
                             'locator': positions[path][1][line_number-1],
                             'excerpt': excerpt[:230]})
        # Spread the samples through the hits, rather than record only a
        # possibly repeated opening-heading match. Counts retain full scope.
        selected = []
        if hits:
            picks = sorted({0, min(1,len(hits)-1), len(hits)//2, len(hits)-1})
            selected = [hits[i] for i in picks]
        files.append({'file': str(path.relative_to(workspace)),
                      'matching_lines': len(hits), 'samples': selected})
    items.append({'id': match.group(1), 'title': match.group(2),
                  'terms': terms, 'rg_patterns': patterns, 'files': files})

if [item['id'] for item in items] != [f'N{i:03d}' for i in range(1,102)]:
    raise RuntimeError('Expected exactly N001–N101 in order')

stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
out = [
    '# Context searches for all numbered research notes', '',
    f'Executed: {stamp}.', '',
    'All 101 items were searched individually with `rg` in the four supplied text files listed below. '
    'Fixed-string queries preserve the terms attached to each final note, with hyphen/space variants for '
    'the compact dotted terms. The file lists contain matching-line counts and up to four spread-out samples, '
    'not every hit. The main notes supply the selected substantive relation and source locator; a lexical hit '
    'alone is not evidence for an implication. A zero here is a bounded negative search, not an archive-wide claim.', '',
    'No manuscript scan was processed by this script. All 48 frozen file hashes were checked before and after.', '',
]
for item in items:
    out += [f"## {item['id']} — {item['title']}", '',
            'Search terms: ' + ', '.join('`'+term+'`' for term in item['terms']) + '.', '']
    for file in item['files']:
        out.append(f"### {file['file']} — {file['matching_lines']} matching lines")
        out.append('')
        if not file['samples']:
            out += ['No matching line for these terms in this file.', '']
            continue
        for hit in file['samples']:
            out += [f"- Line {hit['line']}; locator: `{hit['locator']}`.",
                    '', '    '+hit['excerpt'].replace('\t','    '), '']

directory = root / 'research_records'
(directory / 'context_searches.md').write_text('\n'.join(out)+'\n', encoding='utf-8')
(directory / 'context_searches.json').write_text(json.dumps({'executed_utc': stamp, 'items': items},
                                                         ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
verify_frozen()
with (root / 'progress.log').open('a',encoding='utf-8') as log:
    log.write(f'research context searches completed {stamp}; 101 items; 4 supplied text files per item; frozen hashes unchanged\n')
print(f'101 individual searches recorded across four approved context files; 48 frozen hashes unchanged at {stamp}.')
