from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[3]
n=int(sys.argv[1]);folder='J156-5-05' if n<42 else 'J156-5-06'
base=ROOT/'source/SP58_CW_156-5_witnesses'
print('WITNESS C\n'+(base/f'codex/{folder}/pages/{folder}_156-5_scan{n:03d}.tex').read_text())
batch='02' if n<42 else '03'
s=(base/f'hua/transcripts/156-5/batch-{batch}.fr.tex').read_text()
m=re.search(r'\\page\{'+str(n-1)+r'\}(.*?)(?=\\page\{|\Z)',s,re.S)
print('\nWITNESS H\n'+(m.group(0) if m else 'MISSING'))
s=(base/f'codex/{folder}/{folder}_doubts.md').read_text()
pat=r'### Scan 0?'+str(n)+r'\b(.*?)(?=### Scan|\Z)'
m=re.search(pat,s,re.S)
if not m:
    rows=[l for l in s.splitlines() if re.match(r'\|\s*0?'+str(n)+r'\s*\|',l)]
    print('\nC DOUBTS\n'+'\n'.join(rows))
else: print('\nC DOUBTS\n'+m.group(0))
