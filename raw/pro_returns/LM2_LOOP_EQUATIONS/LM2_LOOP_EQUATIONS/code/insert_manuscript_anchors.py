#!/usr/bin/env python3
"""Add explicit manuscript locators where a claim lacks one; idempotent.

The locator records come from the attached transcription audit. This utility
does not infer folios from page numbers or alter mathematical statements.
"""
from pathlib import Path
import json
import re

ROOT=Path(__file__).resolve().parents[1]
records={}
for p in (ROOT/'code'/'ledger_inputs').glob('*_results.json'):
    records.update({r['id']:r for r in json.loads(p.read_text())})

def escape(s):
    for a,b in [('&',r'\&'),('%',r'\%'),('_',r'\_'),('#',r'\#')]:s=s.replace(a,b)
    return s.replace('§',r'\S ').replace('–','--').replace('≈',r'$\simeq$')

added=[]
for path in sorted((ROOT/'sections').glob('*.tex')):
    text=path.read_text()
    def insert(m):
        block=m.group(0); ident=m.group(1)
        if ident=='F.1' or ('fol' in block and 'scan' in block):return block
        marker='% anchor:'+ident
        if marker in text:return block
        loc=records[ident]['manuscript_passages (section; folio; scan)']
        added.append(ident)
        return block+'\n'+marker+'\n'+r'\manuscriptanchor{'+escape(loc)+'}\n'
    text=re.sub(r'\\begin\{claim\}\{([^}]+)\}.*?\\end\{claim\}',insert,text,flags=re.S)
    path.write_text(text)
print('Added manuscript anchors:', ', '.join(added) if added else 'none; already current')
