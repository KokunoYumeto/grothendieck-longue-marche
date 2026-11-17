#!/usr/bin/env python3
"""Verify integrated statement ledger, labels, references and final build status."""
from pathlib import Path
import re,csv,hashlib,json
R=Path(__file__).resolve().parents[1]
texts=[p.read_text() for p in sorted(R.glob('part_*.tex'))]
s='\n'.join(texts)
ids=re.findall(r'\\begin\{result\}\{([^}]+)\}',s)
rows=list(csv.DictReader((R/'GT_TOWER_CHECK_results.csv').open()))
assert len(ids)==len(set(ids))
assert set(ids)=={r['id'] for r in rows}
labels=re.findall(r'\\label\{([^}]+)\}',s)
assert len(labels)==len(set(labels))
tags=re.findall(r'\\tag\{([^}]+)\}',s)
assert len(tags)==len(set(tags)), 'Duplicate manual equation tags'
refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',s)
assert set(refs)<=set(labels),set(refs)-set(labels)
log=(R/'GT_TOWER_CHECK_paper.log').read_text()
assert not re.search(r'Overfull|undefined|multiply defined',log)
manifest=json.loads((R/'notes/pdf_qa/manifest.json').read_text())
assert manifest['pdf_sha256']==hashlib.sha256((R/'GT_TOWER_CHECK_paper.pdf').read_bytes()).hexdigest()
build=json.loads((R/'notes/build/current_build_manifest.json').read_text())
assert build['pdf_sha256']==manifest['pdf_sha256']
assert all(hashlib.sha256((R/name).read_bytes()).hexdigest()==digest
           for name,digest in build['source_sha256'].items()), 'Sources changed after the checked PDF build'
assert all(x.get('visually_inspected') for x in manifest['pages'])
print('PASS:',len(ids),'unique statements match the ledger;',len(labels),'unique labels.')
print('PASS: every reference resolves; final log has zero overflows and no undefined or duplicate references.')
print('PASS: PDF hash matches the completed visual-inspection manifest with',len(manifest['pages']),'pages.')
