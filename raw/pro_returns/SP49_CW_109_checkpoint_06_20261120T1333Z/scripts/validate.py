from pathlib import Path
import json,re,csv,hashlib
W=Path(__file__).resolve().parents[1]
records=[json.loads(p.read_text()) for p in sorted((W/'records').glob('scan*.json'))]
errors=[];counts={'unsure':0,'illegible':0,'deleted':0,'inserted':0,'diagram':0,'figure':0}
for r in records:
    path=W/'pages'/r['filename'];text=path.read_text()
    body=re.sub(r'(?<!\\)%.*','',text)
    braces=0
    for m in re.finditer(r'(?<!\\)[{}]',body):
        braces+=1 if m.group()=='{' else -1
        if braces<0:errors.append(f'{path.name}: early closing brace')
    if braces:errors.append(f'{path.name}: brace balance {braces}')
    if len(re.findall(r'(?<!\\)\$',body))%2:errors.append(f'{path.name}: odd dollar count')
    # Tokenize control sequences: the second slash in \\\\[.5ex] is not a display opener.
    controls=re.findall(r'\\(?:[A-Za-z@]+|.)',body)
    if controls.count('\\[')!=controls.count('\\]'):errors.append(f'{path.name}: display imbalance')
    stack=[]
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',body):
        k,name=m.groups()
        if k=='begin':stack.append(name)
        elif not stack or stack.pop()!=name:errors.append(f'{path.name}: environment mismatch {name}')
    if stack:errors.append(f'{path.name}: open environments {stack}')
    for k in counts:counts[k]+=len(re.findall(r'\\'+k+r'\{',body))
    if f"\\scanpage{{{r['scan']}}}" not in body:errors.append(f'{path.name}: missing scan macro')
    if len(r['readers'])!=3:errors.append(f'{path.name}: requires 3 readers')
    for reader in 'ABC':
        rp=W/'readers'/f"{r['scan']:03}"/reader
        for file in ['reading.tex','report.json']:
            if not (rp/file).exists():errors.append(f'{path.name}: missing reader {reader} {file}')
    for item in r['inventory']:
        if item.get('transcribed')!='yes':errors.append(f'{path.name}: incomplete inventory item')
        if item.get('sheet_kind') not in ['text','reused_typed','typescript','letter','list','cancelled_draft','cover']:errors.append(f'{path.name}: invalid sheet kind {item.get("sheet_kind")}')
        if item.get('kind') not in ['text','display','diagram','drawing','margin note','insertion','deletion']:errors.append(f'{path.name}: invalid element kind {item.get("kind")}')
    for d in r['decisions']:
        if d.get('diff_h') and r['hua_has']!='text':errors.append(f'{path.name}: spurious H row')
        for crop in d.get('crops',[]):
            if not (W/crop).exists():errors.append(f'{path.name}: missing crop {crop}')
result={'completed_pages':len(records),'scans':[r['scan'] for r in records],'macro_counts':counts,'errors':errors,'scope':'Static brace, dollar, display, environment, page/readers/inventory/crop checks. No LaTeX compilation, per the supplied transcription conventions.'}
(W/'records/validation.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
if errors:raise SystemExit(1)
