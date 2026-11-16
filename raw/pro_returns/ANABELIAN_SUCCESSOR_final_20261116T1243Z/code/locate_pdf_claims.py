"""Locate selected current claims and unusually short pages for visual QA."""
import json
from pathlib import Path
import fitz

W=Path(__file__).resolve().parents[1]
mapping=json.loads((W/'notes/statement_map.json').read_text())
keys=['AR.3','AC.45','AG.1','AG.39','AG.40','AG.41','AG.42','AR.11','FF.49','FF.50']
pdf=fitz.open(W/'ANABELIAN_SUCCESSOR_paper.pdf')
texts=[p.get_text() for p in pdf]
result={
    'pdf_pages':len(pdf),
    'claim_pages':{key:{'id':mapping[key],
        'pages':[i+1 for i,t in enumerate(texts) if mapping[key]+'.' in t]}
        for key in keys if key in mapping},
    'pages_with_fewer_than_250_text_characters':
        [{'page':i+1,'text':t} for i,t in enumerate(texts) if len(t.strip())<250],
    'note':'Claim strings may occur in references as well as at claim headings. Rendering and actual image inspection remain necessary.'
}
print(json.dumps(result,indent=2,ensure_ascii=False))
