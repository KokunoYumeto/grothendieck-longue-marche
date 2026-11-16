#!/usr/bin/env python3
"""Reproduce the per-note lexical search; never modifies a transcription.

Run from the workspace containing context_source/ and MPL_45_033-080/.
Hit locations support, but do not replace, the prose comparison in the notes.
"""
from pathlib import Path
import csv
import json
import re
import unicodedata
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / 'MPL_45_033-080'
CONTEXT = ROOT / 'context_source'
OUT = PACKAGE / 'research'
OUT.mkdir(exist_ok=True)

def fold(value):
    return ''.join(c for c in unicodedata.normalize('NFD', value.casefold())
                   if unicodedata.category(c) != 'Mn')

sources = {
    'CT': CONTEXT / 'MPL_16+47+54+44_transcription.tex',
    'CN': CONTEXT / 'MPL_16+47+54+44_notes.md',
    'CD': CONTEXT / 'MPL_16+47+54+44_doubts.md',
    'RS': CONTEXT / 'notes/RESULTS_STATE.md',
    'README': CONTEXT / 'README.md',
    'Oda_text': CONTEXT / 'oda_text.txt',
}
indexed = {}
for key, path in sources.items():
    if not path.exists():
        if key == 'Oda_text':
            continue
        raise FileNotFoundError(path)
    cote = scan = None
    rows = []
    for n, line in enumerate(path.read_text().splitlines(), 1):
        for kind, val in re.findall(r'\\(cotefile|scanpage)\{(\d+)\}', line):
            if kind == 'cotefile':
                cote, scan = val, None
            else:
                scan = val
        rows.append((n, line, fold(line), cote, scan))
    indexed[key] = rows

notes = (PACKAGE / 'MPL_45_033-080_notes.md').read_text()
entries = []
csvrows = []
for match in re.finditer(r'^### ([A-Z]\d{2}) — ([^\n]+)\n(.*?)(?=^### |^## |\Z)', notes, re.M | re.S):
    note_id, title, body = match.groups()
    query = re.search(r'<!-- search: (.*?) -->', body)
    if query is None:
        raise ValueError(f'Missing per-note query for {note_id}')
    terms = [x.strip() for x in query.group(1).split(';') if x.strip()]
    entry = {'id': note_id, 'title': title, 'terms': terms, 'searches': []}
    for term in terms:
        needle = fold(term)
        # Short standalone object names should not match TeX's tikzpicture
        # (Pic), ordinary words ending in -lie, or French "algebre" (Br).
        short_name = bool(re.fullmatch(r'[a-zA-Z]{1,3}', term))
        pattern = re.compile(r'(?<!\w)' + re.escape(needle) + r'(?!\w)') if short_name else None
        for key, rows in indexed.items():
            hits = [{'line': n, 'cote': cote, 'scan': scan, 'excerpt': line[:200]}
                    for n, line, normalized, cote, scan in rows
                    if (bool(pattern.search(normalized)) if pattern else needle in normalized)]
            locations = sorted({f'{h["cote"]}:{int(h["scan"]):03d}' for h in hits
                                if h['cote'] and h['scan']})
            # Keep all exact line locations; excerpts are bounded reading aids.
            entry['searches'].append({'term': term, 'source': key,
                'file': str(sources[key].relative_to(CONTEXT)),
                'count': len(hits), 'locations': locations,
                'line_numbers': [h['line'] for h in hits], 'sample_hits': hits[:8]})
            csvrows.append([note_id, term, key, len(hits), '; '.join(locations)])
    entries.append(entry)
result = {'searched_at_utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
          'method': 'Case- and accent-insensitive literal searches; word boundaries for bare alphabetic terms of up to three letters, substrings otherwise; no OCR; full supplied text files.',
          'scope_limit': 'Lexical audit only. Prose notes distinguish a same-statement hit from a related or incidental hit.',
          'notes': entries}
(OUT / 'context_searches.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
with (OUT / 'context_searches.csv').open('w', newline='') as stream:
    writer = csv.writer(stream)
    writer.writerow(['note_id', 'term', 'source', 'hit_count', 'cote_scan_hits'])
    writer.writerows(csvrows)
print(json.dumps({'notes_searched': len(entries), 'queries': len(csvrows),
                  'output': str(OUT)}, indent=2))
