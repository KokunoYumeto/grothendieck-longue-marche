from pathlib import Path
import json,csv,re,hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT.parent/'source'
SCANS=[103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,126,127,128,129]
errors=[];warnings=[];seen_marks=[];all_crops=set()
for n in SCANS:
 page=f'149_scan{n:03d}';p=ROOT/'pages'/f'{page}.tex';meta=ROOT/'review/accepted'/f'{page}.json'
 if not p.exists() or not meta.exists():errors.append(f'{page}: missing accepted text or metadata');continue
 d=json.loads(meta.read_text());s=p.read_text()
 if not d.get('audited'):errors.append(f'{page}: independent visual audit not completed')
 if f'\\scanpage{{{n}}}' not in s:errors.append(f'{page}: scan marker')
 if '\\documentclass' in s or '\\begin{document}' in s:errors.append(f'{page}: not a fragment')
 stripped=re.sub(r'(?<!\\)%.*','',s)
 balance=0
 for c in re.sub(r'\\[{}]','',stripped):
  if c=='{':balance+=1
  elif c=='}':balance-=1
  if balance<0:errors.append(f'{page}: premature closing brace');break
 if balance:errors.append(f'{page}: brace balance {balance}')
 if re.search(r'\\(?:ill|add|del|ms|page)\b',s):warnings.append(f'{page}: possible nonstandard witness macro')
 for r in d['decisions']:
  seen_marks.append(r['id'])
  if r['decision']!='undecided' and r.get('crop') in [None,'','page']:errors.append(f'{page}: resolved {r["id"]} lacks crop')
 for r in d['changes']+d['decisions']:
  crop=r.get('crop','page')
  if crop!='page':
   if not (ROOT/crop).is_file():errors.append(f'{page}: missing crop {crop}')
   else:all_crops.add(crop)
   if len(r.get('bbox',[]))!=4:errors.append(f'{page}: missing original bbox for {crop}')
 for r in d['inventory']:
  if r.get('transcribed')!='yes':errors.append(f'{page}: untranscribed inventory element {r.get("element")}')
 for suffix in ['boxes','first','second']:
  if not (ROOT/'second'/f'{page}_{suffix}.tsv').exists():errors.append(f'{page}: missing {suffix} independent-audit table')
 if (ROOT/'second'/f'{page}_boxes.tsv').exists() and (ROOT/'second'/f'{page}_second.tsv').exists():
  tables={suffix:list(csv.DictReader((ROOT/'second'/f'{page}_{suffix}.tsv').open(),delimiter='\t')) for suffix in ['boxes','first','second']}
  if any([r['box'] for r in tables[suf]]!=[r['box'] for r in tables['boxes']] for suf in ['first','second']):errors.append(f'{page}: audit box identity/order mismatch')
  for r in tables['boxes']:
   b=[int(r[k]) for k in ['x0','y0','x1','y1']]
   if not (0<=b[0]<b[2] and 0<=b[1]<b[3]):errors.append(f'{page}: invalid box {r["box"]}')
source_marks=list(csv.DictReader((SRC/'SP88_C13_149_texts/MARKS.tsv').open(),delimiter='\t'))
expected=[r['id'] for r in source_marks]
if sorted(seen_marks)!=sorted(expected):errors.append('MARKS id coverage mismatch: '+str({'missing':sorted(set(expected)-set(seen_marks)),'extra':sorted(set(seen_marks)-set(expected))}))
if len(set(seen_marks))!=len(seen_marks):errors.append('Duplicate MARKS decisions')
frozen=ROOT/'second/FIRST_READINGS_SHA256.json'
if frozen.exists():
 for row in json.loads(frozen.read_text()):
  p=ROOT/row['path']
  if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=row['sha256']:errors.append('Frozen audit input changed: '+row['path'])
else:errors.append('Missing frozen independent-audit input hashes')
sealed_second=ROOT/'second/SECOND_READINGS_SHA256.json'
if sealed_second.exists():
 sealed=json.loads(sealed_second.read_text())
 if set(sealed)!=set(f'149_scan{n:03d}' for n in SCANS):errors.append('Sealed independent-reading coverage mismatch')
 for page,entry in sealed.items():
  for row in entry['files']:
   p=ROOT/row['path']
   if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=row['sha256']:errors.append('Sealed independent reading changed: '+row['path'])
else:errors.append('Missing sealed independent-reading hashes')
combo=ROOT/'SP88_C13_149_transcription.tex'
if combo.exists():
 scans=re.findall(r'\\scanpage\{(\d+)\}',combo.read_text())
 if scans!=list(map(str,SCANS)):errors.append('Combined transcription order/coverage mismatch')
print(json.dumps({'errors':errors,'warnings':warnings,'accepted_pages':len(list((ROOT/'pages').glob('*.tex'))),'marks':len(seen_marks),'referenced_crops':len(all_crops)},ensure_ascii=False,indent=2))
if errors:sys.exit(1)
