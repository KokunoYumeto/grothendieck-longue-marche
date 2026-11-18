#!/usr/bin/env python3
"""Primary-reader refinements after personal cross-page image comparison."""
from pathlib import Path
from datetime import datetime, timezone
import csv, json

ROOT = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
changes = []
def replace(scan, old, new):
    p = ROOT / 'pages' / f'MPL_118_118_scan{scan:03d}.tex'
    t = p.read_text()
    assert old in t, (scan, old)
    count = t.count(old)
    p.write_text(t.replace(old, new))
    changes.append({'scan': scan, 'old': old, 'new': new, 'count': count})

# Image comparison: closed upper loop and horizontal cap match the sigma in 040/041.
for scan in (31, 34):
    replace(scan, r'\unsure{\gamma|\sigma}', r'\unsure{\sigma|\gamma}')
# These short overhead strokes do not resolve into secure arrowheads at their ends.
replace(15, r'$\overrightarrow{\mathrm{Cat}},\overrightarrow{\widehat A}$',
        r'$\unsure{\overline{\mathrm{Cat}}|\overrightarrow{\mathrm{Cat}}},\unsure{\overline{\widehat A}|\overrightarrow{\widehat A}}$')
replace(25, r"\deleted{\unsure{X'}}&I\times X", r"\deleted{\unsure{X'}}&I\unsure{\times|\alpha} X")
replace(25, r'\unsure{\mathcal M}', r'\unsure{\mathcal M|\mathcal A}')
replace(25, r'(ii) Si \deleted', r'''\margin{\figure{\begin{tikzpicture}[x=.45cm,y=.7cm]
\draw (0,1.4) .. controls (-.35,1.25) and (-.15,.6) .. (-.2,.25)
.. controls (-.22,.08) and (-.4,.03) .. (-.5,0)
.. controls (-.3,-.03) and (-.2,-.12) .. (-.2,-.35)
.. controls (-.18,-.8) and (-.35,-1.25) .. (0,-1.4);
\end{tikzpicture}}}
(ii) Si \deleted''')

inv = ROOT / 'MPL_118_inventory.csv'
rows = list(csv.DictReader(inv.open(newline='')))
fields = list(rows[0])
before = [dict(r) for r in rows]
for r in rows:
    r['_old'] = r['element']
    r['_order'] = float(r['element'].split('-')[1])

def row(e):
    found = [r for r in rows if r['_old'] == e]
    assert len(found) == 1, e
    return found[0]

def split(e, texts):
    r = row(e)
    base = r['_order']
    r['first_words_or_objects'] = texts[0]
    for i, text in enumerate(texts[1:], 1):
        n = dict(r)
        n['first_words_or_objects'] = text
        n['_old'] = e + f'.{i+1}'
        n['_order'] = base + i/100
        rows.append(n)

def add(scan, order, kind, position, text, tag):
    template = next(r for r in rows if int(r['scan']) == scan)
    n = dict(template)
    n.update(kind=kind, position=position, first_words_or_objects=text,
             _old=f'{scan:03d}-new-{tag}', _order=order)
    rows.append(n)

split('005-07', ['WSB∩Sm', 'WSB∩Pr'])
split('005-12', ['SprB', 'SprF', 'SprC', 'pre below WSF', 'pre below WSC'])
split('005-13', ['WSF', 'WSC'])
split('005-24', ['W', 'As', '°'])
add(5, 4.1, 'deletion', 'within insertion above hence equation', 'Pr (uncertain)', 'pr')
add(5, 6.1, 'diagram', 'within top-right definitions', 'T = X → Y with deformation/retraction arrows', 'definition-diagram')
row('005-09')['first_words_or_objects'] = 'C,F/E ≠ or ⊄ WSF,WSC! C⊄WSF; F⊄WSC; C∩WSF⊄S? F∩WSC⊄S?'
split('008-02', ['T', 'F'])
row('008-01')['first_words_or_objects'] = 'TF or T∩F; deleted T; ⊄T; deleted F; prime or exclamation'
split('009-05', ['a\\X→b\\Y', '⇔(aX→aX)'])
split('009-13', ['fibrés', '⇔', '∈W'])
split('009-22', ['F', '∈'])
split('009-28', ['dans', 'et'])
add(9, 7.1, 'diagram', 'proper left-edge marginal note', 'implication pointer beside proper with trivial fibers', 'pointer')
add(9, 25.1, 'insertion', 'bottom, beside first oval object', 'X[u]', 'xu')
add(9, 25.2, 'insertion', 'bottom, beside second oval object', "X[u′]", 'xuprime')
row('009-31')['_order'] = 25.3
split('012-18', ['nor trivial after cofibration', 'nor trivial after fibration'])
row('012-19')['_order'] = 15.1
row('012-20')['_order'] = 17.1
split('015-14', ['beta', 'q1', 'q0'])
split('015-21', ['3', 'a'])
split('015-31', ['en', 'X0a ou X1a soit', 'cat. ponctuelles, l’une des', 'cat.'])
split('019-14', ['y', 'f(y)'])
row('020-21')['_order'] = 13.1
row('023-29')['_order'] = 17.1
row('025-38')['_order'] = 9.1
row('025-39')['_order'] = 24.5
add(25, 17.1, 'drawing', 'left beside (ii) through beginning of (iii)', 'curly grouping stroke next to cancelled marginal note', 'brace')
row('026-33')['_order'] = 21.5
row('027-15')['_order'] = 4.1
row('027-16')['_order'] = 5.5
row('028-15')['_order'] = 5.5
row('032-20')['_order'] = 3.5
split('033-22', ['est', 'cat. test faible'])
row('033-21')['first_words_or_objects'] = 'si: saturation forte or si: résolution forte; si A W-asph.'
row('035-22')['_order'] = 17.1
row('035-23')['_order'] = 19.1
row('040-45')['_order'] = 20.5

rows.sort(key=lambda r: (int(r['scan']), r['_order']))
counts = {}
mapping = []
for r in rows:
    scan = int(r['scan'])
    counts[scan] = counts.get(scan, 0) + 1
    new_id = f'{scan:03d}-{counts[scan]:02d}'
    mapping.append({'old': r['_old'], 'new': new_id})
    r['element'] = new_id
    del r['_old'], r['_order']
with inv.open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader(); w.writerows(rows)
(ROOT/'records'/'pre_freeze_refinement_record.json').write_text(json.dumps(
    {'utc': stamp, 'page_edits': changes, 'inventory_before_count': len(before),
     'inventory_after_count': len(rows), 'inventory_id_mapping': mapping}, ensure_ascii=False, indent=2)+'\n')
with (ROOT/'progress.log').open('a') as f:
    f.write(f'notation comparison completed {stamp}; primary reader compared recurring signs across saved pages and revisited images; alternatives retained where ink does not decide\n')
    f.write(f'inventory refinement {stamp}; {len(before)} to {len(rows)} rows; grouped deletions/insertions separated and audit additions reordered\n')
print(json.dumps({'utc': stamp, 'page_edits': len(changes), 'inventory_rows': len(rows)}))
