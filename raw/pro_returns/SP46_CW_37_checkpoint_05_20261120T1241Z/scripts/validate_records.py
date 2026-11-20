"""Validate documentary structure and TeX balance without running a TeX engine."""
from pathlib import Path
import json,re,sys,csv
O=Path(__file__).resolve().parents[1]
order=json.loads((O/'page_order.json').read_text())
allowed_kinds={'text','display','diagram','drawing','margin note','insertion','deletion'}
allowed_sheets={'text','reused_typed','typescript','letter','list','cancelled_draft','cover'}
collation_kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
errors=[]
def check(ok,msg):
 if not ok:errors.append(msg)
def texcheck(p):
 t='\n'.join(re.split(r'(?<!\\)%',s)[0] for s in p.read_text().splitlines())
 # Escaped braces are literal glyphs, not grouping.
 level=0
 for m in re.finditer(r'(?<!\\)[{}]',t):
  level+=1 if m[0]=='{' else -1
  check(level>=0,f'{p.name}: negative brace nesting')
 check(level==0,f'{p.name}: brace balance {level}')
 stack=[]
 for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',t):
  op,env=m.groups()
  if op=='begin':stack.append(env)
  elif not stack or stack.pop()!=env:errors.append(f'{p.name}: environment mismatch {env}')
 check(not stack,f'{p.name}: open environments {stack}')
 # An odd run of backslashes ends in a control symbol: \\\( is a
 # line break followed by \(, whereas \\[ is a line-break option.
 math_tokens=[m.group(2) for m in re.finditer(r'(\\+)([()\[\]])',t) if len(m.group(1))%2]
 for a,b in [('(',')'),('[',']')]:check(math_tokens.count(a)==math_tokens.count(b),f'{p.name}: unmatched \\{a}/\\{b}')
 check(len(re.findall(r'(?<!\\)\$',t))%2==0,f'{p.name}: unmatched inline math dollar')
 check(t.count(r'\begingroup')==t.count(r'\endgroup'),f'{p.name}: unmatched explicit group')
 check('\\newcommand' not in t and '\\def' not in t,f'{p.name}: unexpected macro definitions')
 return t
decisions=sorted((O/'decisions').glob('scan*.json'))
for p in decisions:
 d=json.loads(p.read_text());n=d['scan'];meta=next(x for x in order if int(x['our_scan'])==n)
 target=O/'pages'/Path(meta['codex_file']).name
 check(target.exists(),f'{n}: missing page')
 if target.exists():
  t=texcheck(target);check(t.count(f'\\scanpage{{{n}}}')==1,f'{n}: scan marker')
 for x in d['decisions']:
  check(x['confidence'] in {'high','medium','low'},f'{n}: confidence {x["place"]}')
  check(x['kind'] in collation_kinds,f'{n}: collation kind {x["kind"]}')
  check(not x['diff_h'] or meta['hua_has']=='text',f'{n}: H row on description-only page')
  check(set(x.get('readers',{}))==set('ABC'),f'{n}: missing three readings {x["place"]}')
  crop=x.get('crop','')
  if crop:check((O/crop).exists(),f'{n}: absent crop {crop}')
 for x in d['inventory']:
  check(x['kind'] in allowed_kinds,f'{n}: inventory kind {x["kind"]}')
  check(x['sheet_kind'] in allowed_sheets,f'{n}: sheet kind {x["sheet_kind"]}')
  check(x['transcribed']=='yes',f'{n}: inventory item not transcribed')
 for a in 'ABC':
  r=json.loads((O/f'readers/scan{n:03}/{a}/report.json').read_text())
  check(len(r['image_views'])==3,f'{n}/{a}: source view record')
  check((O/f'readers/scan{n:03}/{a}/reading.tex').exists(),f'{n}/{a}: missing returned reading')
  for c in r['crops']:
   raw=Path(c['file'])
   f=raw if raw.is_absolute() else O/f'readers/scan{n:03}/{a}'/raw
   if not f.exists() and not raw.is_absolute():
    for candidate in (O.parent/raw,O/raw):
     if candidate.exists():f=candidate;break
   # Preserve original session paths in the reports; resolve archive-local copies after restoration.
   if not f.exists() and '/out/' in str(f):
    f=O/str(f).split('/out/',1)[1]
   check(f.exists(),f'{n}/{a}: missing reader crop {f}')
combined=O/'SP46_CW_37_transcription.tex'
if combined.exists():
 t=texcheck(combined)
 check(t.count(r'\cotefile{37}')==(1 if decisions else 0),'combined cote marker count')
 check(len(re.findall(r'\\scanpage\{',t))==len(decisions),'combined page count')
print(f'Checked {len(decisions)} decided pages, combined fragment, report records, crop paths and inventory enums.')
if errors:
 print('\n'.join(errors));sys.exit(1)
print('PASS. Structural validation only; no TeX compilation or mathematical proof is asserted.')
