from pathlib import Path
from datetime import datetime,timezone
import re,json,hashlib,sys
OUT=Path(__file__).resolve().parents[1]
expected=[3,4,5,6,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,29,31,32,33,35,79,80,81]
ds=[json.loads(p.read_text()) for p in sorted((OUT/'decisions').glob('scan*.json'))]
partial='--partial' in sys.argv
assert not (partial and '--freeze' in sys.argv), 'Partial validation cannot freeze a transcription'
assert [d['scan'] for d in ds]==(expected[:len(ds)] if partial else expected)
records=[];errors=[]
allowed_kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
inventory_kinds={'text','display','diagram','drawing','margin note','insertion','deletion'}
sheet_kinds={'text','reused_typed','typescript','letter','list','cancelled_draft','cover'}
for d in ds:
 for i,row in enumerate(d['rows'],1):
  if row['kind'] not in allowed_kinds:errors.append(f"scan {d['scan']} row {i}: unsupported difference kind {row['kind']}")
  if set(row.get('readers',{}))!={'R1','R2','R3'}:errors.append(f"scan {d['scan']} row {i}: missing independent-reader comparison")
  if row['confidence'] not in {'high','medium','low'}:errors.append(f"scan {d['scan']} row {i}: invalid confidence")
 for i,row in enumerate(d['inventory'],1):
  if row['kind'] not in inventory_kinds or row['sheet_kind'] not in sheet_kinds or row['transcribed']!='yes':errors.append(f"scan {d['scan']} inventory {i}: invalid type or incomplete coverage")
 for i,row in enumerate(d['doubts'],1):
  if row['confidence'] not in {'high','medium','low'}:errors.append(f"scan {d['scan']} doubt {i}: invalid confidence")
 p=OUT/'pages'/d['filename'];s=p.read_text();clean=re.sub(r'(?<!\\)%[^\n]*','',s)
 braces=0
 for c in re.finditer(r'(?<!\\)[{}]',clean):
  braces+=1 if c.group()=='{' else -1
  if braces<0:errors.append(p.name+': closing brace before opening')
 if braces:errors.append(p.name+': braces unbalanced '+str(braces))
 for a,b in [(r'\[',r'\]'),(r'\(',r'\)')]:
  if clean.count(a)!=clean.count(b):errors.append(p.name+': '+a+' '+b+' unbalanced')
 if len(re.findall(r'(?<!\\)\$',clean))%2:errors.append(p.name+': odd dollar count')
 stack=[]
 for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
  kind,name=m.groups()
  if kind=='begin':stack.append(name)
  elif not stack or stack.pop()!=name:errors.append(p.name+': environment mismatch '+name)
 if stack:errors.append(p.name+': unclosed environments '+repr(stack))
 if re.search(r'\\(?:newcommand|renewcommand|def|documentclass|usepackage)\b',clean):errors.append(p.name+': unauthorized definition/preamble')
 if clean.count('\\scanpage{'+str(d['scan'])+'}')!=1:errors.append(p.name+': scan marker mismatch')
 records.append(dict(file=p.name,unsure=s.count('\\unsure{'),illegible=s.count('\\illegible{'),deleted=s.count('\\deleted{'),sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
combined=OUT/'SP42_CW_29_transcription.tex'
joined='\n\n'.join((OUT/'pages'/d['filename']).read_text().rstrip() for d in ds)+'\n'
if combined.read_text()!=joined:errors.append('Combined transcription differs from concatenated decided pages')
if joined.count('\\cotefile{29}')!=1:errors.append('Cote marker must occur exactly once')
report={'page_count':len(ds),'scope':'completed prefix only' if partial else 'all 30 pages','checks':'static syntax, markers and assembly only; no LaTeX engine run','errors':errors,'pages':records,'combined_sha256':hashlib.sha256(combined.read_bytes()).hexdigest()}
validation_name='validation_partial' if partial else 'validation'
(OUT/(validation_name+'.json')).write_text(json.dumps(report,indent=2)+'\n')
(OUT/(validation_name+'.txt')).write_text(f"Pages: {len(ds)}\nScope: {report['scope']}\nStatic validation: {'PASS' if not errors else 'FAIL'}\n"+'\n'.join(errors)+'\n'+''.join(f"{r['file']}: unsure={r['unsure']} illegible={r['illegible']} deleted={r['deleted']}\n" for r in records))
print(json.dumps(report))
if errors:sys.exit(1)
if '--freeze' in sys.argv:
 now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
 hashes={str((OUT/'pages'/d['filename']).relative_to(OUT)):r['sha256'] for d,r in zip(ds,records)}
 hashes[combined.name]=report['combined_sha256']
 (OUT/'frozen_hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
 with (OUT/'progress.log').open('a') as f:
  f.write('transcription frozen '+now+'\n')
  for name,h in hashes.items():f.write('SHA-256 '+h+' '+name+'\n')
