"""Check the exact equation-134 gap repair in every edition form."""
from pathlib import Path
import sys, re, json
sys.path.insert(0, str(Path('work/scripts').resolve()))
import build_readers, mechanical_repairs, layout_repairs, editorial

D = Path('work/layout_probes')
records = []
for lang in ['fr', 'en']:
    pkg = 'LM_C4-267-280'
    raw = build_readers.raw_package(pkg, lang)
    t, _ = mechanical_repairs.repair(raw, pkg, lang)
    t, _ = layout_repairs.repair(t, pkg, lang)
    a, b = next((a, b) for n, a, b in layout_repairs._scan_ranges(t) if n == 276)
    section = t[a:b]
    d = next(m[0] for m in re.finditer(r'\\\[.*?\\\]', section, re.S) if '(134)' in m[0])
    old = r'shift right=2ex] \& \operatorname{Cont}'
    newpart = r'shift right=2ex] \&[35pt] \operatorname{Cont}'
    assert d.count(old) == 1
    new = d.replace(old, newpart)
    records.append(dict(id='140-4-276-L1', language=lang, package=pkg, scan=276,
                        old=d, new=new, reason='Equation (134): add 35pt only between the q-map source and target so the unchanged uncertain long-arrow description no longer covers either object; retain all cancellations, notation, endpoints and the surrounding array.'))
    # A document per form keeps the production preamble's mode selection intact.
    for mode in [0, 1, 2]:
        body = r'\scanpage{276}' + '\n' + new
        body, _, _ = editorial.annotate(body, pkg, lang)
        output = build_readers.preamble(lang, mode) + '\n' + r'\begin{document}\LMcote{140-4}' + '\n' + body + '\n' + r'\end{document}'
        (D / f'scan276_clearance_{lang}_{mode}.tex').write_text(output)
(D / 'scan276_clearance.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
