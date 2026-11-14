#!/usr/bin/env python3
"""Check the B/C statement and coverage ledgers against the manuscript files."""
import json
import re
from pathlib import Path

base=Path(__file__).resolve().parent.parent
texts={name:(base/'sections'/f'{name}.tex').read_text() for name in ('B','B_equal_char_extension','B_marked_cover_extension','B_fixed_tree_extension','B_inertia_jsj_extension','B_pdiv_cover_extension','C','C_local_extension','C_full_winding_extension','C_local_prop_extension','C_genus_zero_detection_extension','C_generic_local_fixed_extension','C_finite_exception_extension','C_elliptic_detection_extension','C_RNS_full_fixed_extension')}
claims={}
for name,text in texts.items():
    for ident,status in re.findall(r'\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}',text):
        assert ident not in claims, ident
        assert status in {'Proved','Known','Refuted','Unresolved'}, (ident,status)
        claims[ident]=status
    assert text.count(r'\begin{claim}') == text.count(r'\end{claim}'),name
    assert text.count(r'\begin{proof}') == text.count(r'\end{proof}'),name

rows=json.loads((base/'audit'/'BC_results.json').read_text())
assert len(rows)==len({x['id'] for x in rows})
assert set(claims)=={x['id'] for x in rows}
for row in rows:
    assert row['status']==claims[row['id']],row['id']
    for key in ('statement','where_proved','depends_on','manuscript_passages','notes'):
        assert row[key],(row['id'],key)

coverage=json.loads((base/'audit'/'BC_coverage.json').read_text())
expected={f'B{i}' for i in range(15)}|{f'C{i}' for i in range(1,5)}|{f'L{i}' for i in range(1,11)}
assert {x['item'] for x in coverage}==expected
assert len(coverage)==len(expected)
for row in coverage:
    assert row['statement_ids']
    assert set(row['statement_ids'])<=set(claims),row['item']
    if 'unresolved' in row['status'].lower():
        assert row['remaining_obligation'],row['item']

bib=(base/'sources'/'BC_refs.bib').read_text()
keys=re.findall(r'@\w+\{([^,]+),',bib)
assert len(keys)==len(set(keys))
cites=set()
for text in texts.values():
    for group in re.findall(r'\\cite\w*(?:\[[^\]]*\])?\{([^}]+)\}',text):
        cites.update(k.strip() for k in group.split(','))
all_bib='\n'.join(path.read_text() for path in (base/'sources').glob('*_refs.bib'))
all_keys=set(re.findall(r'@\w+\{([^,]+),',all_bib))
assert cites<=all_keys,sorted(cites-all_keys)
checks=json.loads((base/'code'/'BC_checks_output.json').read_text())
assert checks['all_assertions_passed']
equal_checks=json.loads((base/'code'/'BC_equal_char_checks_output.json').read_text())
assert all(row['passed'] for row in equal_checks['checks'])
marked_checks=json.loads((base/'code'/'BC_marked_cover_checks_output.json').read_text())
assert all(row['passed'] for row in marked_checks['checks'])
jsj_checks=json.loads((base/'code'/'BC_jsj_checks_output.json').read_text())
assert all(row['passed'] for row in jsj_checks['checks'])
pdiv_checks=json.loads((base/'code'/'BC_pdiv_cover_checks_output.json').read_text())
assert all(row['passed'] for row in pdiv_checks['checks'])
local_checks=json.loads((base/'code'/'BC_local_fixed_checks_output.json').read_text())
assert all(row['passed'] for row in local_checks['checks'])
derivation_checks=json.loads((base/'code'/'BC_local_derivation_checks_output.json').read_text())
assert all(row['passed'] for row in derivation_checks['checks'])
genus_zero_checks=json.loads((base/'code'/'BC_genus_zero_detection_checks.json').read_text())
assert genus_zero_checks['all_checks_passed']
assert genus_zero_checks['group_order']==60
assert genus_zero_checks['explicit_missing_simple_quotient']['projective_classes_enumerated']==51888
elliptic_checks=json.loads((base/'code'/'BC_elliptic_detection_checks.json').read_text())
assert elliptic_checks['all_checks_passed']
assert all(row['passed'] for row in elliptic_checks['checks'])
result={
 'passed':True,
 'statement_count':len(claims),
 'status_counts':{s:list(claims.values()).count(s) for s in ('Proved','Known','Refuted','Unresolved')},
 'coverage_item_count':len(coverage),
 'bibliography_entry_count':len(keys),
 'cited_bibliography_entry_count':len(cites),
 'exact_computation_checks':checks['number_of_named_checks']+equal_checks['passed']+marked_checks['passed']+jsj_checks['passed']+pdiv_checks['passed']+local_checks['passed']+derivation_checks['passed']+1+elliptic_checks['number_of_named_checks'],
 'unresolved_statement_ids':[i for i,s in claims.items() if s=='Unresolved'],
 'scope':'Metadata and exact computational checks; no substitute for mathematical or PDF visual review.'
}
(base/'code'/'BC_validate_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
