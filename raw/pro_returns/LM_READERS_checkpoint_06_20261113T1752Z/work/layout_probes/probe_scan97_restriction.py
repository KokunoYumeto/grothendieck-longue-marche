"""Probe one source-local arrow-label clearance in both languages and forms."""
from pathlib import Path
import hashlib
import json
import re
import sys

sys.path.insert(0, str(Path('work/scripts').resolve()))
import build_readers
import editorial
import layout_repairs
import mechanical_repairs

D = Path('work/layout_probes')
records = []
for lang in ('fr', 'en'):
    package = 'LM_P068-069'
    text = build_readers.raw_package(package, lang)
    text, _ = mechanical_repairs.repair(text, package, lang)
    text, _ = layout_repairs.repair(text, package, lang)
    a, b = next((a, b) for n, a, b in layout_repairs._scan_ranges(text) if n == 97)
    diagrams = re.findall(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}', text[a:b], re.S)
    old = next(d for d in diagrams if 'restriction' in d)
    before = r'''\arrow[r,"{\text{restriction}}","\sim"']'''
    after = r'''\arrow[r,"{\text{restriction}}"{yshift=3pt},"\sim"']'''
    assert old.count(before) == 2
    new = old.replace(before, after, 1)
    records.append({
        'language': lang, 'package': package, 'scan': 97, 'tag': '49',
        'old': old, 'new': new,
        'reason': 'Raise only the upper unchanged restriction label by 3pt to clear the upper arrowhead barb; preserve the lower label, objects, arrow routes and endpoints, notation, uncertainty and cancellation wrappers.',
        'old_sha256': hashlib.sha256(old.encode()).hexdigest(),
        'new_sha256': hashlib.sha256(new.encode()).hexdigest(),
    })
    parts = [build_readers.preamble(lang, 1), r'\begin{document}\LMcote{140-3}']
    for label, diagram in [('before', old), ('candidate', new)]:
        body, _, _ = editorial.annotate(r'\scanpage{97}\diagram{' + diagram + '}', package, lang)
        for mode in (0, 1, 2):
            parts.append(f'\\clearpage\\LMform={mode}\n' + body)
    parts.append(r'\end{document}')
    (D / f'scan97_restriction_{lang}.tex').write_text('\n'.join(parts))
(D / 'scan97_restriction_candidate.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
