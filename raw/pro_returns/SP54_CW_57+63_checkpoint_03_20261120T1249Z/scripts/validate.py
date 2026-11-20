#!/usr/bin/env python3
"""Static syntax and deliverable coverage checks; does not infer manuscript text."""
from pathlib import Path
import re,json,hashlib,csv
OUT=Path(__file__).resolve().parent.parent
order=json.loads((OUT/'records/page_order.json').read_text())
errors=[]; counts={}; checked=[]
for row in order:
    p=OUT/'pages'/(row['page']+'.tex')
    if not p.exists():errors.append('Missing page '+p.name);continue
    raw=p.read_text();t=re.sub(r'(?<!\\)%[^\n]*','',raw)
    balance=0
    for match in re.finditer(r'(?<!\\)[{}]',t):
        balance+=1 if match.group()=='{' else -1
        if balance<0:errors.append(p.name+': premature closing brace');break
    if balance:errors.append(p.name+': unbalanced braces '+str(balance))
    if len(re.findall(r'(?<!\\)\$',t))%2:errors.append(p.name+': odd dollar delimiter count')
    if len(re.findall(r'\\\[',t))!=len(re.findall(r'\\\]',t)):errors.append(p.name+': unbalanced display delimiters')
    stack=[]
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',t):
        if m.group(1)=='begin':stack.append(m.group(2))
        elif not stack or stack.pop()!=m.group(2):errors.append(p.name+': environment mismatch '+m.group())
    if stack:errors.append(p.name+': unclosed environments '+str(stack))
    if re.findall(r'\\scanpage\{(\d+)\}',t)!=[str(row['our_scan'])]:errors.append(p.name+': scan marker mismatch')
    for command in ['documentclass','newcommand','renewcommand','input','include','includegraphics']:
        if '\\'+command+'{' in t or '\\'+command+'[' in t:errors.append(p.name+': unexpected command '+command)
    counts[p.name]={x:len(re.findall('\\\\'+x+r'\{',t)) for x in ['unsure','illegible','deleted','inserted','diagram','figure']}
    recp=OUT/'records'/(row['page']+'.json')
    if not recp.exists():errors.append(p.name+': missing adjudication record')
    else:
        rec=json.loads(recp.read_text())
        if row['hua_has']!='text' and any(x.get('differs_h') for x in rec.get('changes',[])):
            errors.append(p.name+': H collation row on a page without H text')
        for x in rec.get('changes',[]):
            if set(x.get('reader_readings',{}))!={'R1','R2','R3'}:
                errors.append(p.name+': incomplete three-reader comparison at '+x.get('place',''))
            if not (x.get('differs_c') or x.get('differs_h')):
                errors.append(p.name+': counted row changes neither witness at '+x.get('place',''))
            crop=x.get('crop')
            if crop and not Path(crop).exists():
                errors.append(p.name+': missing adjudication crop '+crop)
        for x in rec.get('inventory',[]):
            if x.get('transcribed')!='yes':errors.append(p.name+': unfinished inventory '+str(x.get('element')))
        for reader in ['R1','R2','R3']:
            d=OUT/'readers'/row['page']/reader
            for name in ['reading.tex','report.json','observations.md']:
                if not (d/name).exists():errors.append(p.name+': missing '+reader+'/'+name)
            if (d/'report.json').exists():
                report=json.loads((d/'report.json').read_text())
                coverage=report.get('coverage',{})
                if not coverage.get('all_lines_read') or not coverage.get('all_elements_included'):
                    errors.append(p.name+': incomplete reported coverage for '+reader)
                if len(report.get('images_viewed',[]))!=3:
                    errors.append(p.name+': expected whole and two halves for '+reader)
    checked.append(p.name)
combined=OUT/'SP54_CW_57+63_transcription.tex'
if combined.exists():
    expected='\n'.join((OUT/'pages'/(r['page']+'.tex')).read_text().rstrip()+'\n' for r in order if (OUT/'pages'/(r['page']+'.tex')).exists())
    if combined.read_text()!=expected:errors.append('Combined transcription differs from ordered page concatenation')
frozen=OUT/'records/frozen_hashes.json'
unchanged=None
if frozen.exists():
    unchanged=True
    for name,digest in json.loads(frozen.read_text()).items():
        actual=hashlib.sha256((OUT/name).read_bytes()).hexdigest()
        if actual!=digest:unchanged=False;errors.append('Frozen hash changed: '+name)
result={'checked_pages':len(checked),'errors':errors,'macro_counts':counts,'frozen_hashes_unchanged':unchanged,'method':'Static delimiter/environment/order/inventory/file-presence checks; no LaTeX compilation, OCR or mathematical inference.'}
(OUT/'records/validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps({'checked_pages':len(checked),'errors':errors,'macro_totals':{x:sum(v[x] for v in counts.values()) for x in ['unsure','illegible','deleted','inserted','diagram','figure']},'frozen_hashes_unchanged':unchanged},ensure_ascii=False))
