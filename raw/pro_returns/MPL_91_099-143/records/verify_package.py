"""Structural/package checks only. Does not OCR, interpret, or rewrite the transcription."""
from pathlib import Path
import re,csv,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
EXPECTED=[99,100,101,102,104,105,106,107,108,109,110,111,113,114,115,116,118,119,120,121,122,123,124,126,127,128,129,131,132,134,135,136,138,139,140,141,142,143]
pages=sorted((ROOT/'pages').glob('*.tex'))
assert [int(re.search(r'scan(\d+)',p.name)[1]) for p in pages]==EXPECTED
combined=(ROOT/'MPL_91_099-143_transcription.tex').read_text()
assert combined=='\n\n'.join(p.read_text().strip() for p in pages)+'\n'
assert combined.startswith('\\cotefile{91}\n\\scanpage{99}')
assert combined.count('\\cotefile{')==1
assert [int(n) for n in re.findall(r'\\scanpage\{(\d+)\}',combined)]==EXPECTED
assert '\\documentclass' not in combined and '\\begin{document}' not in combined
rows=list(csv.DictReader((ROOT/'MPL_91_099-143_inventory.csv').open()))
assert list(rows[0])==['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']
assert sorted({int(r['scan']) for r in rows})==EXPECTED
assert all(r['transcribed']=='yes' for r in rows)
for n in EXPECTED:
 rr=[r for r in rows if int(r['scan'])==n]
 assert len({r['sheet_kind'] for r in rr})==1
 assert [int(r['element']) for r in rr]==list(range(1,len(rr)+1))
log=(ROOT/'progress.log').read_text()
assert [int(n) for n in re.findall(r'^91 scan (\d+) done ',log,re.M)]==EXPECTED
assert [int(n) for n in re.findall(r'^scan (\d+) audited ',log,re.M)]==EXPECTED
# Environments and group braces: supplementary to the successful full XeLaTeX compile.
for p in pages:
 s=p.read_text();stack=[]
 for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
  mode,env=m.groups()
  if mode=='begin':stack.append(env)
  else:assert stack.pop()==env,(p,env)
 assert not stack,p
 depth=0
 for m in re.finditer(r'(?<!\\)[{}]',s):
  depth+=1 if m.group()=='{' else -1
  assert depth>=0,p
 assert depth==0,p
manifest=ROOT/'records/transcription.sha256'
if manifest.exists():
 for line in manifest.read_text().splitlines():
  expected,relative=line.split('  ',1)
  assert hashlib.sha256((ROOT/relative).read_bytes()).hexdigest()==expected,relative
 print('Frozen hashes verified: 39 files unchanged.')
print(f'PASS: {len(pages)} page fragments, {len(rows)} inventory elements, all 38 done/audited records, ordered markers, balanced groups/environments.')
