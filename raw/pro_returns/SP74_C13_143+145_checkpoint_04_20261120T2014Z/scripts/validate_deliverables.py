#!/usr/bin/env python3
"""Check artifact completeness, provenance links and TeX grouping; no compilation/OCR."""
from pathlib import Path
import csv,json,re,sys,collections
W=Path(__file__).resolve().parents[1];B=W.parent;P='SP74_C13_143+145';final='--final' in sys.argv
order=json.loads((W/'page_order.json').read_text());keys=[x['key'] for x in order]
rows=lambda p,sep='\t':list(csv.DictReader(p.open(),delimiter=sep))
source=rows(B/'source'/f'{P}_texts/MARKS.tsv');dec=rows(W/'decisions.tsv')
errors=[];checks=[]
def check(ok,msg):
 (checks if ok else errors).append(msg)
records=[json.loads(p.read_text()) for p in sorted((W/'reviews').glob('*_accepted.json'))]
allowed_kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
allowed_inventory={'text','display','diagram','drawing','margin note','insertion','deletion'}
allowed_sheets={'text','reused_typed','typescript','letter','list','cancelled_draft','cover'}
allowed_events={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found','refuted'}
check(len({d['id'] for d in dec})==len(dec),'decision ids are unique')
rank={x['id']:i for i,x in enumerate(source)}
check(all(x['id'] in rank for x in dec),'all decision ids come from supplied MARKS')
check([x['id'] for x in dec]==sorted([x['id'] for x in dec],key=rank.get),'decisions preserve supplied MARKS order')
for r in records:
 key=r['key'];check((W/'pages'/f'{key}.tex').exists(),f'{key}: page fragment exists')
 check(all(x['transcribed']=='yes' for x in r['inventory']),f'{key}: inventory transcribed flags complete')
 check(len({x['element'] for x in r['inventory']})==len(r['inventory']),f'{key}: inventory element ids unique')
 check(all(x['kind'] in allowed_inventory and x['sheet_kind'] in allowed_sheets for x in r['inventory']),f'{key}: authorized inventory categories')
 check(all(x.get('kind','other') in allowed_kinds for x in r['changes']),f'{key}: authorized collation categories')
 check(all(x.get('confidence') in {'high','medium','low'} for x in r['changes']+r['decisions']),f'{key}: confidence vocabulary valid')
 check(all(x.get('decision') in {'first','alternative','other','undecided'} for x in r['decisions']),f'{key}: decision vocabulary valid')
 check(all(x.get('type') in allowed_events or x.get('type','').startswith('refuted,') for x in r.get('check_events',[])),f'{key}: check-event vocabulary valid')
 check({d['id'] for d in r['decisions']}=={m['id'] for m in source if str(m['cote'])==key.split('_scan')[0] and int(m['scan'])==int(key.split('_scan')[1])},f'{key}: original marks complete')
 for d in r['changes']+r['decisions']:
  c=d.get('crop','page')
  if c=='page':continue
  check((W/c).is_file(),f'{key}: crop exists {c}')
  b=d.get('box');check(isinstance(b,list) and len(b)==4 and b[0]<b[2] and b[1]<b[3],f'{key}: crop coordinates valid {c}')
 text=(W/'pages'/f'{key}.tex').read_text();depth=0;bad=False
 text=re.sub(r'(?<!\\)%[^\n]*','',text)
 for m in re.finditer(r'(?<!\\)[{}]',text):
  depth+=1 if m[0]=='{' else -1
  if depth<0:bad=True
 check(depth==0 and not bad,f'{key}: TeX groups balance without compilation')
 envs=[];env_ok=True
 for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',text):
  if m[1]=='begin':envs.append(m[2])
  elif envs and envs[-1]==m[2]:envs.pop()
  else:env_ok=False
 check(env_ok and not envs,f'{key}: TeX environments balance without compilation')
 check(not re.search(r'\\(?:documentclass|usepackage|newcommand|renewcommand)\b|\\begin\{document\}',text),f'{key}: fragment adds no preamble or custom macro definitions')
 if 'audited_at' in r:check(r['audit_reader']!=r['reader'],f'{key}: second reader differs from first')
 if final:
  check('audited_at' in r and (W/r.get('audit_record','missing')).is_file(),f'{key}: second reading recorded')
  check(not r.get('unresolved_for_main') and bool(r.get('final_documentary_review')),f'{key}: main adjudication complete; retained source doubts distinguished from pending work')
  check({n['id'] for n in r.get('notes',[])} <= {e['statement_id'] for e in r.get('check_events',[])},f'{key}: every note has an explicitly classified check event')
  check(all(c.get('against_C') or c.get('against_H') for c in r['changes']),f'{key}: every material row differs from an available witness')
  check(len({c['place'] for c in r['changes']})==len(r['changes']),f'{key}: material locus names are unique')
  if r.get('audit_record') and (W/r['audit_record']).is_file():
   a=json.loads((W/r['audit_record']).read_text())
   check(len(a.get('main_adjudication',{}).get('outcomes',[]))==len(a.get('findings',[])),f'{key}: every second-reading finding has a main decision')
combined=(W/f'{P}_transcription.tex').read_text()
expected=[];cote=None
for key in keys:
 if not (W/'pages'/f'{key}.tex').exists():continue
 c=key.split('_')[0]
 if c!=cote:expected.append('\\cotefile{'+c+'}');cote=c
 expected.append((W/'pages'/f'{key}.tex').read_text().rstrip())
check(combined=='\n\n'.join(expected)+'\n','combined fragment equals ordered page fragments with cote headers')
col=rows(W/f'{P}_collation.tsv');check(not any(r['folder']=='143' and r['our_scan']=='34' for r in col),'no H collation rows for scan034')
check(len(col)==sum(c.get('against_H',False) for r in records if r['key']!='143_scan034' for c in r['changes']),'H collation count matches adjudication records')
if final:
 check(len(records)==24 and {r['key'] for r in records}==set(keys),'all 24 page records accepted')
 check([r['id'] for r in dec]==[r['id'] for r in source],'all original doubt marks decided exactly once')
 check(len(list((W/'pages').glob('*.tex')))==24,'exactly 24 page fragments')
 check('Assessment remains in progress' not in (W/f'{P}_doubts.md').read_text(),'final legibility assessment present')
 check(all(r.get('audited_at','')>=max(x['accepted_at'] for x in records) for r in records),'every audit recorded after all first readings were accepted')
summary={'accepted_pages':len(records),'audit_pages':sum('audited_at' in r for r in records),'decisions':len(dec),'source_marks':len(source),'changes':sum(len(r['changes']) for r in records),'collation':len(col),'inventory':sum(len(r['inventory']) for r in records),'checks_passed':len(checks),'errors':errors,'mode':'final' if final else 'in progress'}
if '--save' in sys.argv:(W/'validation.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
print(json.dumps(summary,ensure_ascii=False,indent=2));sys.exit(bool(errors))
