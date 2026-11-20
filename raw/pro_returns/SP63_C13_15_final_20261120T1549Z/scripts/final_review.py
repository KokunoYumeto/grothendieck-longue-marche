"""Apply the root reader's final notation decision and syntax-only corrections.

The scans were read by the root reader. This script performs no image reading.
"""
from workflow import ROOT, assemble, utc
import json

p = ROOT / 'pages/15_scan176.tex'
t = p.read_text()
old = r'\uline{\unsure{\mathrm{Div}|D^0}}_X'
assert old in t
p.write_text(t.replace(old, r'\uline{\mathrm{Div}}_X'))
p = ROOT / 'records/176.json'
d = json.loads(p.read_text())
evidence = ('The compressed continuation after the tall D agrees with the short i and upward-looped v '
            'in all three underlined Div labels on scan 179, whose sequence (5.1) explicitly names '
            'the divisor sheaf. The earlier crop 176 (697,321,804,392), the second whole-page audit, '
            'and crop 179 (1041,1273,1156,1336) supply the comparison; no second crop was made. '
            'The common notation resolves Div at medium confidence.')
for r in d['rows']:
    if r['place'] == 'first display, divisor notation':
        r['final'] = r'\uline{\mathrm{Div}}_X'
        r['ink'] = evidence
        r['confidence'] = 'medium'
for x in d['decisions']:
    if x['id'] == 'M0069':
        x['decision'] = 'first'
        x['reading'] = r'\mathrm{Div}'
        x['what the ink shows'] = evidence
        x['confidence'] = 'medium'
        x['crop'] = '176 (697,321,804,392); comparison 179 (1041,1273,1156,1336)'
d['doubts'] = [x for x in d['doubts'] if x[1] != 'first displayed sheaf']
for x in d['inventory']:
    if x[0] == 'display' and x[1] == 'upper third':
        x[2] = 'H¹(X, underlined Div_X)=0'
for x in d['notation']:
    if x[0] == 'Divisor sheaf':
        x[1] = r'\uline{\mathrm{Div}}_X'
        x[2] = '176, 179'
        x[3] = evidence
d['notes'] = d['notes'].replace(
    'The first divisor label remains uncertain in its compressed strokes; the later divisor notation will be compared in the notation review.',
    'The final notation review resolves the compressed first label as underlined Div by comparison with the three explicit Div labels and the divisor-sheaf definition on scan 179. This is a recurring-notation decision at medium confidence; the cohomology statement was not separately proved.')
d['hand'].append('The compressed iv after D has the same short stem and upward-looped ending as the three Div labels on scan 179. All four occurrences are read Div after the final comparison. C marked this occurrence as Div/D⁰; H read Div but omitted its underline.')
d['extra'] += '\nFinal notation review: M0069 resolved to the first reading, Div, at medium confidence. This removes a certainty mark without adding a substantive change against C. ' + evidence
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')

# Preserve exactly the small drawn strokes while boxing them in math mode.
p = ROOT / 'pages/15_scan173.tex'
t = p.read_text()
a = r'\underset{\figure{\begin{tikzpicture}'
b = r'\underset{\text{\begin{tikzpicture}'
assert a in t
p.write_text(t.replace(a, b))

# One spelling for the prompt's collation category; no reading or count changes.
for p in sorted((ROOT / 'records').glob('*.json')):
    d = json.loads(p.read_text())
    for r in d['rows']:
        if r['kind'] == r'readable ink left as \ill{}':
            r['kind'] = r'readable ink left as `\ill{}`'
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')

assemble()
with (ROOT / 'progress.log').open('a') as f:
    f.write('final recurring-notation review completed; M0069 resolved; small drawing wrapper repaired ' + utc() + '\n')
