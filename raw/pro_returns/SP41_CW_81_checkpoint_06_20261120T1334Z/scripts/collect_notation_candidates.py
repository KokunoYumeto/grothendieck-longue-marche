"""Index exact notation records for the later cross-page visual audit.

String matches identify review candidates only. They do not equate handwritten
forms, decide case, or alter any transcription.
"""
from pathlib import Path
import json

w = Path(__file__).resolve().parents[1]
records = [json.loads(p.read_text()) for p in sorted((w / 'decisions').glob('scan*.json'))]
groups = {
    'Pi/pi spellings': [r'\Pi', r'\pi'],
    'P alphabets': [r'\mathcal{P}', r'\mathfrak{P}', r'\mathscr{P}', r'\mathcal P', r'\mathfrak P'],
    'Gamma and its marks': [r'\Gamma'],
    'Sigma and its marks': [r'\Sigma'],
    'Omega and small omega': [r'\omega', r'\Omega'],
    'Arrows and inclusion signs': ['arrow', r'\subset', r'\hook', r'\mapsto', r'\in'],
    'Circle/letter/numeral candidates': [r'\circ', '|o|0', '|0'],
    'Plus/T-shaped candidates': [r'\top'],
    'Repeated shorthand': ['sss', 'p.ex', 'p. ex', 'Card', 'Cor', 'Déf', 'en =', 'de ='],
    'Quotation marks': ['quotation', '``', 'guillem']
}
items = []
for d in records:
    for i, n in enumerate(d.get('notation', []), 1):
        combined = n.get('form','') + ' ' + n.get('reading','')
        matches = [name for name, needles in groups.items() if any(s in combined for s in needles)]
        items.append({'scan':d['scan'],'notation_index':i,'candidate_groups':matches,**n})
result = {
    'status':'pending final cross-page visual comparison',
    'through_scan':records[-1]['scan'] if records else None,
    'warning':'Candidate grouping is exact-string indexing only. Every final identity or rendering choice requires the main reader’s recorded comparison against the ink.',
    'notation_records':items,
    'abbreviations':[a for d in records for a in d.get('abbreviations',[])]
}
(w / 'validation/notation_review_candidates.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print('Indexed',len(items),'notation records through scan',result['through_scan'])
