"""Index recurring notation for human comparison; never infer or edit readings."""
from pathlib import Path
from collections import defaultdict
import json,re
out=Path(__file__).resolve().parents[1]
ds=[json.loads(p.read_text()) for p in sorted((out/'decisions').glob('scan*.json'))]
forms=defaultdict(list)
commands=defaultdict(set)
reader_notes=[]
for d in ds:
    text=(out/'pages'/d['filename']).read_text()
    clean=re.sub(r'(?<!\\)%[^\n]*','',text)
    for m in re.finditer(r'\\(mathcal|mathfrak|mathscr|mathbb|mathbf|mathrm|operatorname)\{([^{}]+)\}',clean):
        key=m.group(2)
        forms[key].append({'scan':d['scan'],'form':m.group(0),'context':re.sub(r'\s+',' ',clean[max(0,m.start()-65):m.end()+65])})
    for m in re.finditer(r'\\([A-Za-z]+)',clean):commands[m.group(1)].add(d['scan'])
    for reader in ['R1','R2','R3']:
        p=out/'readers'/f"scan{d['scan']:03d}"/reader/'report.json'
        for n in json.loads(p.read_text()).get('notation',[]):
            reader_notes.append({'scan':d['scan'],'reader':reader,**n})
report={'decided_pages':len(ds),'status':'index for main-reader review; no automatic equivalence or correctness decision','alphabet_forms':dict(forms),'commands':{k:sorted(v) for k,v in sorted(commands.items())},'independent_reader_notation':reader_notes}
(out/'notation_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
lines=['# Recurring-notation review index\n','This mechanical index records strings already transcribed or reported; it does not recognize text in images, adjudicate a glyph, or alter a page. Independent-reader entries may differ from the final decision.\n',f"Decided pages indexed: {len(ds)}.\n",'## Alphabet forms\n']
for key,rows in sorted(forms.items()):
    values=sorted(set(r['form'] for r in rows))
    lines.append(f"- `{key}`: "+'; '.join('`'+v+'`' for v in values)+'. Scans: '+', '.join(f'{x:03d}' for x in sorted(set(r['scan'] for r in rows)))+'.\n')
lines+=['\n## Command inventory for static review\n',', '.join('`\\'+k+'`' for k in sorted(commands))+'\n','\nAll source contexts and independent notation observations are retained in `notation_audit.json`. The final main-reader review must record whether each apparent difference reflects the ink or inconsistent transcription.\n']
(out/'notation_audit.md').write_text('\n'.join(lines))
print(json.dumps({'decided_pages':len(ds),'alphabet_keys':len(forms),'commands':len(commands),'reader_notation_entries':len(reader_notes)}))
