"""Requested structural verification and SHA-256 freeze; no LaTeX compilation."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,re,json,hashlib,csv
root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('mode',choices=['check','freeze','verify-frozen'],default='check',nargs='?');a=p.parse_args()
def now():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
files=sorted((root/'pages').glob('*.tex'),key=lambda p:int(re.search(r'scan(\d+)',p.name).group(1)))
combined=root/'SP38_CW_75_transcription.tex'
if a.mode=='verify-frozen':
    hashes=json.loads((root/'frozen_sha256.json').read_text())
    mismatches=[name for name,digest in hashes.items() if not (root/name).exists() or sha(root/name)!=digest]
    if mismatches:raise SystemExit('FROZEN HASH MISMATCH: '+str(mismatches))
    with (root/'progress.log').open('a') as f:f.write('frozen hashes unchanged '+now()+' '+str(len(hashes))+' files\n')
    print(json.dumps({'frozen_hashes_unchanged':len(hashes),'time':now()}));raise SystemExit
errors=[];details=[]
for path in files:
    s=path.read_text();clean=re.sub(r'(?<!\\)%[^\n]*','',s)
    scan_number=int(re.search(r'scan(\d+)',path.name).group(1))
    if re.findall(r'\\scanpage\{(\d+)\}',clean)!=[str(scan_number)]:errors.append(path.name+': wrong or repeated scan marker')
    if scan_number!=2 and r'\cotefile{' in clean:errors.append(path.name+': repeated cote marker')
    braces=[]
    for m in re.finditer(r'(?<!\\)[{}]',clean):
        if m.group()=='{':braces.append(m.start())
        elif braces:braces.pop()
        else:errors.append(path.name+': unmatched closing brace')
    if braces:errors.append(path.name+': unclosed braces '+str(len(braces)))
    # A dollar after a row-break control token (two backslashes) is unescaped.
    # Consume control tokens first, so a literal escaped dollar is not counted.
    math_tokens=re.findall(r'\\(?:[A-Za-z]+|[^A-Za-z])|\$',clean)
    if math_tokens.count('$')%2:errors.append(path.name+': odd dollar delimiter count')
    # Tokenize control sequences so a row break with spacing, \\[-.3ex], is not
    # mistaken for a display opener starting at its second backslash.
    controls=re.findall(r'\\(?:[A-Za-z]+|[^A-Za-z])',clean)
    for opening,closing in [(r'\[',r'\]'),(r'\(',r'\)')]:
        if controls.count(opening)!=controls.count(closing):errors.append(path.name+': display delimiter mismatch '+opening)
    stack=[]
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
        kind,env=m.groups()
        if kind=='begin':stack.append(env)
        elif not stack or stack.pop()!=env:errors.append(path.name+': environment mismatch '+env)
    if stack:errors.append(path.name+': unclosed environments '+str(stack))
    if re.search(r'\\(newcommand|renewcommand|def|documentclass|usepackage)\b',clean):errors.append(path.name+': preamble/custom macro in fragment')
    for m in re.finditer(r'\\begin\{tikzcd\}(\[[^\]]*\])?',clean):
        if 'ampersand replacement' not in (m.group(1) or ''):errors.append(path.name+': tikzcd missing ampersand replacement')
    details.append({'file':path.name,'unsure':s.count(r'\unsure{'),'illegible':s.count(r'\illegible{'),'deleted':s.count(r'\deleted{')})
if combined.exists():
    expected='\n\n'.join(x.read_text().rstrip() for x in files)+'\n'
    if combined.read_text()!=expected:errors.append('Combined transcription differs from ordered concatenation')
    if files and combined.read_text().count(r'\cotefile{75}')!=1:errors.append('Cote marker count is not one')
inventory=list(csv.DictReader((root/'SP38_CW_75_inventory.csv').open()))
if any(x['transcribed']!='yes' for x in inventory):errors.append('Untranscribed inventory item')
if a.mode=='freeze':
    scans=[int(re.search(r'scan(\d+)',p.name).group(1)) for p in files]
    if scans!=list(range(2,26)):errors.append('Expected exactly scans 002–025')
    allowed_kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
    allowed_events={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found','refuted'}
    allowed_sheet={'text','reused_typed','typescript','letter','list','cancelled_draft','cover'}
    allowed_element={'text','display','diagram','drawing','margin note','insertion','deletion'}
    for row in inventory:
        if row['sheet_kind'] not in allowed_sheet:errors.append('Invalid inventory sheet kind: '+str(row))
        if row['kind'] not in allowed_element:errors.append('Invalid inventory element kind: '+str(row))
    if sorted({int(row['scan']) for row in inventory})!=list(range(2,26)):errors.append('Inventory does not cover exactly scans 002–025')
    sweep_decisions={}
    for event in csv.DictReader((root/'CHECK_EVENTS.tsv').open(),delimiter='\t'):
        if event['type'] not in allowed_events:errors.append('Invalid check-event type: '+str(event))
        if not all(event.get(k,'').strip() for k in ['statement_id','date','who','outcome']):errors.append('Incomplete check event: '+str(event))
    for n in range(2,26):
        for r in ['R1','R2','R3']:
            if not (root/'readings'/f'scan{n:03d}'/r/'report.json').exists():errors.append(f'Missing independent report {n} {r}')
            if not (root/'readings'/f'scan{n:03d}'/r/'reading.tex').exists():errors.append(f'Missing independent page reading {n} {r}')
        if not (root/'records'/f'scan{n:03d}.json').exists():errors.append(f'Missing adjudication {n}')
        else:
            rec=json.loads((root/'records'/f'scan{n:03d}.json').read_text())
            if rec.get('readers')!=['R1','R2','R3']:errors.append(f'Incomplete reader set {n}')
            if not rec.get('notes','').strip():errors.append(f'Missing page notes {n}')
            viewed=set(rec.get('main_crop_views',[]))
            for crop in viewed:
                if not (root/crop).is_file():errors.append(f'Missing inspected crop {n}: '+crop)
            for f in rec.get('findings',[]):
                if f.get('confidence') not in {'high','medium','low'}:errors.append(f'Invalid confidence {n} '+str(f.get('id')))
                if f.get('kind') not in allowed_kinds:errors.append(f'Invalid collation kind {n} '+str(f.get('id'))+': '+str(f.get('kind')))
                if f.get('marked_in_H') not in {'yes','no'}:errors.append(f'Invalid H doubt flag {n} '+str(f.get('id')))
                if not isinstance(f.get('diff_c'),bool) or not isinstance(f.get('diff_h'),bool):errors.append(f'Invalid change flag {n} '+str(f.get('id')))
                if (f.get('diff_c') or f.get('diff_h')) and not f.get('crop'):errors.append(f'Missing adjudication crop {n} '+str(f.get('id')))
                for crop in str(f.get('crop','')).split(';'):
                    crop=crop.strip()
                    if crop and crop not in viewed:errors.append(f'Finding crop absent from main view record {n} '+str(f.get('id'))+': '+crop)
                rd=f.get('readers')
                if isinstance(rd,dict) and set(rd)!={'R1','R2','R3'}:errors.append(f'Incomplete reader comparison {n} '+str(f.get('id')))
                if not isinstance(rd,(str,dict)) or not rd:errors.append(f'Missing reader comparison {n} '+str(f.get('id')))
                if f.get('s_id'):sweep_decisions[f['s_id']]=f.get('s_decision','')
            for u in rec.get('unresolved',[]):
                if not isinstance(u.get('alternatives'),str):errors.append(f'Non-string doubt alternatives {n}')
            coverage=root/'decisions'/f'scan{n:03d}_C_doubt_coverage.json'
            if coverage.exists():
                for d in json.loads(coverage.read_text()).get('doubts',[]):
                    if d.get('disposition') not in {'retain','resolve'}:errors.append(f'Unfinished original C doubt disposition {n}: '+str(d.get('c_doubt_id')))
    for sid in ['SA01-K75-01','SA01-K75-02']:
        if not sweep_decisions.get(sid,'').strip():errors.append('Missing explicit sweep decision '+sid)
result={'time':now(),'pages':len(files),'inventory_elements':len(inventory),'marks':{k:sum(d[k] for d in details) for k in ['unsure','illegible','deleted']},'errors':errors,'per_page':details,'compiled':False}
(root/'structural_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
if errors:raise SystemExit(1)
if a.mode=='freeze':
    hashes={str(x.relative_to(root)):sha(x) for x in files+[combined]}
    (root/'frozen_sha256.json').write_text(json.dumps(hashes,indent=2)+'\n')
    with (root/'progress.log').open('a') as f:
        f.write('transcription frozen '+now()+'\n')
        for name,digest in hashes.items():f.write('SHA256 '+digest+' '+name+'\n')
