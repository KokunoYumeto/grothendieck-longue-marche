from pathlib import Path
import csv, re, json

root = Path('/workspace/scratch/36f9c078cbe9/deliverable')
rows = list(csv.DictReader((root/'LM5_MULTI_GALOIS_TOPOI_results.csv').open()))
assert list(rows[0]) == ['id','statement','status','where_proved','depends_on','manuscript_passages (section; folio; scan)','depends_on_doubtful_reading (scan, alternatives)','notes'], 'result schema mismatch'
assert all(r['status'] in {'Proved','Refuted','Known','Open'} for r in rows)
registered = {r['id']:r for r in rows}
declared = {}
for file in sorted((root/'sections').glob('[A-F].tex')):
    for m in re.finditer(r'\\paragraph\{([A-F]\.\d+)\s*\((Proved|Refuted|Known|Open)', file.read_text()):
        assert m.group(1) not in declared, f'duplicate declaration {m.group(1)}'
        declared[m.group(1)] = m.group(2)
assert len(rows)==len(registered), 'duplicate register ID'
assert set(registered)==set(declared), {'unregistered':list(set(declared)-set(registered)), 'undeclared':list(set(registered)-set(declared))}
assert all(registered[k]['status']==v for k,v in declared.items()), 'status mismatch'
assert all(r['manuscript_passages (section; folio; scan)'] for r in rows), 'missing manuscript passage'
bib = (root/'LM5_MULTI_GALOIS_TOPOI_references.bib').read_text()
entries = re.findall(r'(?ms)^@\w+\{([^,]+),\s*\n(.*?)^\}', bib)
keys = {k for k,_ in entries}
assert len(keys)==len(entries), 'duplicate bibliography key'
assert all(re.search(r'\b(?:unverified|verified)\b', t, re.I) for _,t in entries), 'bibliography lacks verification status'
used = set()
for file in (root/'sections').glob('*.tex'):
    for m in re.finditer(r'\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}', file.read_text()):
        used.update(x.strip() for x in m.group(1).split(','))
assert used<=keys, f'missing bibliography keys: {used-keys}'
counts={s:sum(r['status']==s for r in rows) for s in ['Proved','Refuted','Known','Open']}
readings=list(csv.DictReader((root/'LM5_MULTI_GALOIS_TOPOI_readings.csv').open()))
assert list(readings[0]) == ['package','scan','the \\unsure or \\illegible place','what the mathematics supports','how strongly'], 'reading schema mismatch'
log=(root/'build_final.log').read_text() if (root/'build_final.log').exists() else ''
over=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log)]
summary={'statements':len(rows),'status_counts':counts,'readings':len(readings),'bibliography_entries':len(entries),'explicit_citation_keys':len(used),'overfull_boxes_final':len(over),'overfull_above_2pt':sum(x>2 for x in over),'numbering_and_status_check':'PASS','bibliography_integrity':'PASS','exact_csv_schemas':'PASS'}
print(json.dumps(summary,indent=2))
