"""Recover exact current-page C rows missed by zero-padded scan identifiers.

This selects text metadata only. It does not read images, infer readings, or
rebuild existing packets. Run with one packet stem when that page is opened.
"""
from pathlib import Path
from datetime import datetime, timezone
import json, re, sys

ROOT = Path(__file__).resolve().parents[2]
stem = sys.argv[1]
packet = ROOT / 'packets' / stem
meta = json.loads((packet / 'meta.json').read_text())
scan = int(meta['our_scan'])
folder = meta['folder']
base = ROOT / 'source/SP57_CW_97+123+162-1+162-6_witnesses/codex' / folder
dest = packet / 'C_questions.md'
old = dest.read_text()
added = []
for suffix in ('doubts', 'notes'):
    source = base / f'{folder}_{suffix}.md'
    selected = []
    for line in source.read_text().splitlines():
        cells = [c.strip() for c in line.strip().split('|')]
        first = cells[1] if len(cells) > 2 else ''
        if line.lstrip().startswith('|'):
            match = bool(re.fullmatch(r'0*' + str(scan), first))
        else:
            mentioned = {int(n) for n in re.findall(r'\b[Ss]cans?\s+(\d+)', line)}
            match = mentioned == {scan}
            if not match and scan in mentioned:
                # A shared prose paragraph can contain distinct scan-specific
                # sentences. Preserve only the literal current-page sentence.
                for sentence in re.split(r'(?<=[.!?])\s+', line):
                    sentence_pages = {int(n) for n in re.findall(r'\b[Ss]cans?\s+(\d+)', sentence)}
                    if sentence_pages == {scan} and sentence not in old:
                        selected.append(sentence)
        if match and line not in old:
            selected.append(line)
    if selected:
        added.append('\nExact current-page C rows from ' + source.name + ':\n' + '\n'.join(selected) + '\n')
if added:
    dest.write_text(old + ''.join(added))
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (ROOT / 'out/progress.log').open('a') as handle:
        handle.write(now + ' supplemented exact C metadata rows for ' + stem + '; zero-padded scan keys accepted.\n')
print(json.dumps({'page': stem, 'sections_added': len(added)}))
