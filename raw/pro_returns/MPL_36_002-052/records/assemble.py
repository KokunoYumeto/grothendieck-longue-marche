from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
scans=json.loads((root/'records/run_state.json').read_text())['expected_scans']
parts=[]
for n in scans:
 p=root/'pages'/f'MPL_36_002-052_36_scan{n:03}.tex'
 parts.append(p.read_text().rstrip()+'\n')
combined='\n'.join(parts)
assert combined.startswith('\\cotefile{36}\n\\scanpage{3}\n')
(root/'MPL_36_002-052_transcription.tex').write_text(combined)
print('Assembled',len(scans),'pages;',len(combined.encode()),'bytes.')
