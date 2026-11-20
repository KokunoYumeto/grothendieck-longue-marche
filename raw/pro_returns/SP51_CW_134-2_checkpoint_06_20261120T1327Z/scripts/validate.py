from pathlib import Path
import re,json,sys,hashlib,csv
root=Path(__file__).resolve().parents[1]
issues=[];summary=[]
for f in sorted((root/'pages').glob('*.tex')):
    t=f.read_text();s=re.sub(r'(?<!\\)%[^\n]*','',t)
    depth=0
    for m in re.finditer(r'(?<!\\)[{}]',s):
        depth+=1 if m.group()=='{' else -1
        if depth<0:issues.append(f'{f.name}: premature closing brace')
    if depth:issues.append(f'{f.name}: brace balance {depth}')
    if len(re.findall(r'(?<!\\)\$',s))%2:issues.append(f'{f.name}: odd dollar count')
    if s.count('\\[')!=s.count('\\]'):issues.append(f'{f.name}: display delimiter mismatch')
    stack=[]
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
        act,name=m.groups()
        if act=='begin':stack.append(name)
        elif not stack or stack.pop()!=name:issues.append(f'{f.name}: environment mismatch at {name}')
    if stack:issues.append(f'{f.name}: unclosed environments {stack}')
    for m in re.finditer(r'\\begin\{tikzcd\}(\[[^\]]*\])?',s):
        if not m.group(1) or 'ampersand replacement=\\&' not in m.group(1):issues.append(f'{f.name}: tikzcd lacks ampersand replacement')
    summary.append({'file':f.name,'sha256':hashlib.sha256(t.encode()).hexdigest(),'unsure':t.count('\\unsure{'),'illegible':t.count('\\illegible{'),'deleted':t.count('\\deleted{')})
combined=root/'SP51_CW_134-2_transcription.tex'
if combined.exists():
    if combined.read_text().count('\\cotefile{134-2}')!=1:issues.append('Combined transcription must have exactly one cote marker')
    expected=''.join((root/'pages'/x['file']).read_text().rstrip()+'\n' for x in summary)
    if combined.read_text()!=expected:issues.append('Combined transcription differs from ordered pages')
for f in sorted((root/'records').glob('scan*/decision.json')):
    d=json.loads(f.read_text())
    for r in 'ABC':
        p=f.parent/r/'report.json'
        if not p.exists():issues.append(f'{f.parent.name}: missing reader {r}')
        elif not json.loads(p.read_text()).get('complete'):issues.append(f'{f.parent.name}: reader {r} not complete')
    for x in d.get('differences',[]):
        if x.get('crop') and not (root/x['crop']).exists():issues.append(f'{f.parent.name}: missing crop {x["crop"]}')
        if not x.get('differs_C') and not x.get('differs_H'):issues.append(f'{f.parent.name}: no actual difference in changes row {x["place"]}')
    allowed_kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
    for x in d.get('differences',[]):
        if x.get('kind') not in allowed_kinds:issues.append(f'{f.parent.name}: invalid collation kind {x.get("kind")}')
        if x.get('confidence') not in {'high','medium','low'}:issues.append(f'{f.parent.name}: invalid confidence')
        if x.get('marked_in_H') not in {'yes','no'}:issues.append(f'{f.parent.name}: invalid H doubt flag')
    for x in d.get('abbreviations',[]):
        if not x.get('written'):issues.append(f'{f.parent.name}: empty abbreviation form')
    for x in d.get('inventory',[]):
        if x.get('transcribed')!='yes':issues.append(f'{f.parent.name}: incomplete inventory element')
        if x.get('kind') not in {'text','display','diagram','drawing','margin note','insertion','deletion'}:issues.append(f'{f.parent.name}: invalid inventory kind')
        if x.get('sheet_kind') not in {'text','reused_typed','typescript','letter','list','cancelled_draft','cover'}:issues.append(f'{f.parent.name}: invalid sheet kind')

report={'pages':len(summary),'issues':issues,'counts':{k:sum(x[k] for x in summary) for k in ['unsure','illegible','deleted']},'files':summary}
(root/'records/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='files'},ensure_ascii=False))
sys.exit(bool(issues))
