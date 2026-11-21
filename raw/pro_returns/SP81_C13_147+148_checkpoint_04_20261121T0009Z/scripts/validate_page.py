from pathlib import Path
import json,csv,re,sys
r=Path(__file__).resolve().parents[1];s=r.parent/'source';page=sys.argv[1]
p=r/'work'/f'{page}_report.json'
x=json.loads(p.read_text());cote,scan=page.split('_scan')
marks=list(csv.DictReader((s/'SP81_C13_147+148_texts/MARKS.tsv').open(),delimiter='\t',quoting=csv.QUOTE_NONE))
expected={m['id'] for m in marks if m['cote']==cote and int(m['scan'])==int(scan)}
seen=[d['id'] for d in x['decisions']]
errors=[];warnings=[]
if expected!=set(seen):errors.append('mark coverage: missing '+str(expected-set(seen))+' extra '+str(set(seen)-expected))
if len(seen)!=len(set(seen)):errors.append('duplicate decisions')
diffs=list(csv.DictReader((s/'SP81_C13_147+148_C_H_differences.tsv').open(),delimiter='\t',quoting=csv.QUOTE_NONE))
dexpected={i for i,d in enumerate(diffs,1) if d['page']==page}
dseen={int(d['row']) for d in x.get('diff_coverage',[])}
if dexpected!=dseen:errors.append('difference-list coverage: missing '+str(dexpected-dseen)+' extra '+str(dseen-dexpected))
views=(r/'work/root_views.tsv').read_text() if (r/'work/root_views.tsv').exists() else ''
for c in x['changes']:
 if c.get('crop'):
  if not (r/'crops'/c['crop']).exists():errors.append(c['id']+' missing crop '+c['crop'])
  if c['crop'] not in views:warnings.append(c['id']+' root has not recorded viewing '+c['crop'])
 else:warnings.append(c['id']+' no crop attached; main reader must inspect/create one for disagreement')
 if c['confidence'] not in ['high','medium','low']:errors.append(c['id']+' bad confidence')
 if c.get('differs_H') and not (s/'SP81_C13_147+148_texts/hua'/f'hua_{page}.tex').exists():errors.append('false H-absence collation '+c['id'])
for d in x['decisions']:
 if d['decision']!='undecided' and d['crop']=='page':errors.append(d['id']+' resolved without crop')
text=(r/'work'/f'{page}.tex').read_text()
if re.search(r'\\(ill|uncertain|struck|add|marginal|note)\{',text):errors.append('witness H macro left in page')
bal=0
for line in text.splitlines():
 for tok in re.findall(r'\\.|[{}]|[^{}\\]+',line.split('%')[0]):
  if tok=='{':bal+=1
  elif tok=='}':bal-=1
  if bal<0:errors.append('brace underflow');break
if bal:errors.append('brace imbalance '+str(bal))
if not text.startswith('\\cotefile{'+cote+'}'):warnings.append('missing cote header')
print(json.dumps({'page':page,'changes':len(x['changes']),'decisions':len(seen),'second_boxes':len(x['second_boxes']),'errors':errors,'warnings':warnings},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
