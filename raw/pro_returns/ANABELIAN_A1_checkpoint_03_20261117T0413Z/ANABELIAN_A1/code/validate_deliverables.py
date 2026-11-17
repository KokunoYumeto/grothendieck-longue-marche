#!/usr/bin/env python3
"""Check the requested register, statement references and bibliography coverage."""
from pathlib import Path
import csv, json, re
from collections import Counter
root=Path(__file__).resolve().parents[1]
paper=(root/'ANABELIAN_A1_paper.tex').read_text()
rows=list(csv.DictReader((root/'ANABELIAN_A1_results.csv').open()))
expected=['id','statement','status','where_proved','depends_on',
          'answers (item or check item)','manuscript_passages (cote; scan)',
          'depends_on_doubtful_reading (scan, alternatives)','notes']
assert list(rows[0]) == expected
ids=[r['id'] for r in rows]; assert len(ids)==len(set(ids))
claims=re.findall(r'\\begin\{claim\}\{([^}]+)\}',paper)
assert claims==ids
for part in 'ABC':
    numbers=[int(x.split('.')[1]) for x in ids if x.startswith(part+'.')]
    assert numbers==list(range(1,len(numbers)+1))
assert set(r['status'] for r in rows) <= {'Proved','Refuted','Known','Open'}
refs=set(re.findall(r'\\statementref\{([^}]+)\}',paper))
assert not refs-set(ids), sorted(refs-set(ids))
items=[f'{p}{i}' for p,n in [('A',14),('B',9),('C',6),('K',6)] for i in range(1,n+1)]
answers={item:[r['id'] for r in rows if item in re.split(r'[;, ]+',r['answers (item or check item)'])]
         for item in items}
assert all(answers.values()), {k:v for k,v in answers.items() if not v}
bib=(root/'ANABELIAN_A1_references.bib').read_text()
keys=re.findall(r'@\w+\s*\{([^,]+),',bib)
assert len(keys)==len(set(keys))
cites=set()
for match in re.finditer(r'\\cite\w*\*?(?:\[[^\]]*\]){0,2}\{([^}]+)\}',paper):
    cites.update(x.strip() for x in match[1].split(','))
assert cites<=set(keys), sorted(cites-set(keys))
assert len(re.findall(r'keywords\s*=\s*\{(?:un)?verified\}',bib))==len(keys)
status={r['id']:r['status'] for r in rows}
open_dependencies=[]
for row in rows:
    if row['status'] in ('Proved','Refuted','Known'):
        for dep in re.findall(r'\b[ABC]\.\d+\b',row['depends_on']):
            if status.get(dep)=='Open': open_dependencies.append((row['id'],dep))
assert not open_dependencies, open_dependencies
report=(root/'ANABELIAN_A1_report.md').read_text()
assert report.startswith('INCOMPLETE\n\n| Item |')
assert all(re.search(r'^\| '+item+r' \|',report,re.M) for item in items)
assert '@STATEMENT_' not in report and '@STATUS_' not in report
result={'verified':True,'statement_count':len(rows),'statuses':dict(Counter(status.values())),
        'bibliography_count':len(keys),'cited_key_count':len(cites),
        'statement_reference_count':len(refs),'all35items_have_rows':True,
        'proved_claims_depending_on_open_claims':open_dependencies,
        'item_statement_mapping':answers}
(root/'code'/'validate_deliverables.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='item_statement_mapping'},indent=2))
